"""SQLite store. This is the only module that runs SQL."""

from app.db import apply_schema, connect
from app.domain.models import Contact, EmailAddress, PhoneNumber, SocialLink
from app.seed import directory


class SqliteContactRepository:
    def __init__(self, db_path):
        self._db_path = str(db_path)

    def prepare(self):
        """Create tables and insert the dummy directory once."""
        connection = connect(self._db_path)
        try:
            apply_schema(connection)
            people = directory()
            count = connection.execute("SELECT COUNT(*) AS n FROM contacts").fetchone()["n"]
            if count:
                return
            for person in people:
                connection.execute(
                    """
                    INSERT INTO contacts (
                        id, first_name, last_name, job_title, bio, address,
                        avatar_file, status, dial, meeting_url
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        person["id"], person["first_name"], person["last_name"],
                        person["job_title"], person["bio"], person["address"],
                        person["avatar_file"], person["status"], person["dial"],
                        person["meeting_url"],
                    ),
                )
                for email, is_primary in person["emails"]:
                    connection.execute(
                        "INSERT INTO email_addresses (contact_id, email, is_primary) VALUES (?, ?, ?)",
                        (person["id"], email, is_primary),
                    )
                for number, is_primary in person["phones"]:
                    connection.execute(
                        "INSERT INTO phones (contact_id, number, is_primary) VALUES (?, ?, ?)",
                        (person["id"], number, is_primary),
                    )
                for network, url in person["social"]:
                    connection.execute(
                        "INSERT INTO social_links (contact_id, network, url) VALUES (?, ?, ?)",
                        (person["id"], network, url),
                    )
            connection.commit()
        finally:
            connection.close()

    def list_contacts(self):
        connection = connect(self._db_path)
        try:
            rows = connection.execute(
                "SELECT * FROM contacts ORDER BY id"
            ).fetchall()
            return [self._contact(connection, row) for row in rows]
        finally:
            connection.close()

    def get_contact(self, contact_id):
        connection = connect(self._db_path)
        try:
            row = connection.execute(
                "SELECT * FROM contacts WHERE id = ?", (contact_id,)
            ).fetchone()
            if row is None:
                return None
            return self._contact(connection, row)
        finally:
            connection.close()

    def list_email_addresses(self, contact_id):
        connection = connect(self._db_path)
        try:
            rows = connection.execute(
                """
                SELECT id, email, is_primary
                FROM email_addresses
                WHERE contact_id = ?
                ORDER BY id
                """,
                (contact_id,),
            ).fetchall()
            return [
                EmailAddress(row["id"], row["email"], bool(row["is_primary"]))
                for row in rows
            ]
        finally:
            connection.close()

    def _contact(self, connection, row):
        phones = tuple(
            PhoneNumber(item["number"], bool(item["is_primary"]))
            for item in connection.execute(
                "SELECT number, is_primary FROM phones WHERE contact_id = ? ORDER BY id",
                (row["id"],),
            )
        )
        social = tuple(
            SocialLink(item["network"], item["url"])
            for item in connection.execute(
                "SELECT network, url FROM social_links WHERE contact_id = ? ORDER BY id",
                (row["id"],),
            )
        )
        email_rows = connection.execute(
            """
            SELECT email, is_primary FROM email_addresses
            WHERE contact_id = ? ORDER BY id
            """,
            (row["id"],),
        ).fetchall()
        primary = next((item["email"] for item in email_rows if item["is_primary"]), "")
        if not primary and email_rows:
            primary = email_rows[0]["email"]
        return Contact(
            id=row["id"],
            first_name=row["first_name"],
            last_name=row["last_name"],
            job_title=row["job_title"],
            bio=row["bio"],
            address=row["address"],
            avatar_file=row["avatar_file"],
            status=row["status"],
            dial=row["dial"],
            meeting_url=row["meeting_url"],
            primary_email=primary,
            phones=phones,
            social_links=social,
        )
