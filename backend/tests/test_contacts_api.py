"""HTTP contract for the two required routes."""

import pytest

from app import create_app


@pytest.fixture
def client(tmp_path):
    app = create_app(tmp_path / "api.db")
    app.config.update(TESTING=True)
    return app.test_client()


def test_list_contacts(client):
    response = client.get("/contacts")
    assert response.status_code == 200
    body = response.get_json()
    assert body[0]["first_name"] == "Nicholas"
    assert body[2]["primary_email"] == "johanna.stevens@gmail.com"
    assert body[2]["job_title"] == "UI/UX Designer"
    assert body[2]["avatar_url"] == "https://randomuser.me/api/portraits/women/44.jpg"
    assert body[2]["phones"][0]["is_primary"] is True
    assert "emails" not in body[2]
    assert len(body[2]["social_links"]) == 5


def test_list_does_not_embed_every_email(client):
    contact = client.get("/contacts").get_json()[2]
    assert "emails" not in contact
    emails = client.get("/contacts/3/email_addresses").get_json()
    assert [item["email"] for item in emails] == [
        "johanna.stevens@gmail.com",
        "johanna.stevens@whiteui.store",
    ]
    assert emails[0]["is_primary"] is True


def test_unknown_contact_emails_are_404(client):
    response = client.get("/contacts/99999/email_addresses")
    assert response.status_code == 404
    assert "99999" in response.get_json()["message"]
