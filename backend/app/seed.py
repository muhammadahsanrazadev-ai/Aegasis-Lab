"""Sample rows for the nine people on the contacts screen.

Assumption: the desktop frame does not show an address block. The brief still
requires an address, so each contact has one and the details pane shows it
under the social row.

The list row for Johanna says Project Manager and the open panel says
UI/UX Designer. One contact has one title. The panel title is the one stored.
"""

# Dummy portraits are remote image links, one per contact, in directory order.
PORTRAIT_URLS = {
    1: "https://randomuser.me/api/portraits/men/11.jpg",
    2: "https://randomuser.me/api/portraits/men/22.jpg",
    3: "https://randomuser.me/api/portraits/women/44.jpg",
    4: "https://randomuser.me/api/portraits/men/33.jpg",
    5: "https://randomuser.me/api/portraits/women/65.jpg",
    6: "https://randomuser.me/api/portraits/men/41.jpg",
    7: "https://randomuser.me/api/portraits/women/17.jpg",
    8: "https://randomuser.me/api/portraits/men/52.jpg",
    9: "https://randomuser.me/api/portraits/women/28.jpg",
}


def _person(
    contact_id,
    first_name,
    last_name,
    job_title,
    status,
    bio,
    address,
    dial,
    meeting_url,
    emails,
    phones,
):
    slug = "{0}.{1}".format(first_name, last_name).lower().replace(" ", "")
    return {
        "id": contact_id,
        "first_name": first_name,
        "last_name": last_name,
        "job_title": job_title,
        "status": status,
        "bio": bio,
        "address": address,
        "dial": dial,
        "meeting_url": meeting_url,
        "avatar_file": PORTRAIT_URLS[contact_id],
        "emails": emails,
        "phones": phones,
        "social": (
            ("facebook", "https://facebook.com/{0}".format(slug)),
            ("pinterest", "https://pinterest.com/{0}".format(slug)),
            ("twitter", "https://twitter.com/{0}".format(slug)),
            ("linkedin", "https://linkedin.com/in/{0}".format(slug)),
            ("google", "https://google.com/search?q={0}".format(slug)),
        ),
    }


def directory():
    """Nine contacts, in the same order as the desktop frame."""
    johanna_bio = (
        "When I first got into the advertising, I was looking for the magical "
        "combination that would put website into the top search engine rankings"
    )
    people = (
        _person(
            1, "Nicholas", "Gordon", "Developer", "online",
            "Builds the billing service. Send a written note before booking a call.",
            "18 King Street, London, EC2V 8AY",
            "n.gordon@ymsg.com", "http://go.betacall.com/meet/n.gordon",
            (("nicholas.gordon@northwind.example", 1), ("nicholas.gordon@gmail.example", 0)),
            (("020-7946-0101", 1), ("07700-900101", 0)),
        ),
        _person(
            2, "Bradley", "Malone", "Sales Manager", "away",
            "Owns the renewal this month. Ask about extra seats before a discount.",
            "410 Market Street, San Francisco, CA 94105",
            "b.malone@ymsg.com", "http://go.betacall.com/meet/b.malone",
            (("bradley.malone@contoso.example", 1), ("bradley.malone@gmail.example", 0)),
            (("415-555-0142", 1), ("415-555-0170", 0)),
        ),
        _person(
            3, "Johanna", "Stevens", "UI/UX Designer", "online",
            johanna_bio,
            "44 Folsom Street, San Francisco, CA 94105",
            "j.stevens@ymsg.com", "http://go.betacall.com/meet/j.stevens",
            (("johanna.stevens@gmail.com", 1), ("johanna.stevens@whiteui.store", 0)),
            (("439-582-1578", 1), ("621-770-7689", 0)),
        ),
        _person(
            4, "Marvin", "Lambert", "Designer", "online",
            "Reviews onboarding screens. Attach the browser name with every bug.",
            "22 Peel Street, Manchester, M4 1NQ",
            "m.lambert@ymsg.com", "http://go.betacall.com/meet/m.lambert",
            (("marvin.lambert@tailspin.example", 1), ("marvin.lambert@gmail.example", 0)),
            (("0161-496-0120", 1), ("07700-900220", 0)),
        ),
        _person(
            5, "Teresa", "Lloyd", "PR agent", "away",
            "Handles press for the spring launch. Do not promise a date that is not on the brief.",
            "5 Herald Square, New York, NY 10001",
            "t.lloyd@ymsg.com", "http://go.betacall.com/meet/t.lloyd",
            (("teresa.lloyd@litware.example", 1), ("teresa.lloyd@gmail.example", 0)),
            (("212-555-0188", 1), ("917-555-0133", 0)),
        ),
        _person(
            6, "Fred", "Haynes", "Support Team", "online",
            "Escalation contact for priority tickets. He can see the same account as the caller.",
            "700 Boylston Street, Boston, MA 02116",
            "f.haynes@ymsg.com", "http://go.betacall.com/meet/f.haynes",
            (("fred.haynes@adventure-works.example", 1), ("fred.haynes@outlook.example", 0)),
            (("617-555-0160", 1), ("617-555-0199", 0)),
        ),
        _person(
            7, "Rose", "Peters", "Project Manager", "away",
            "Runs the data-migration weekend. Confirm the freeze window before Friday.",
            "120 Collins Street, Melbourne, VIC 3000",
            "r.peters@ymsg.com", "http://go.betacall.com/meet/r.peters",
            (("rose.peters@wideworld.example", 1), ("rose.peters@gmail.example", 0)),
            (("03-7010-1234", 1), ("04-1234-5678", 0)),
        ),
        _person(
            8, "Brian", "Watson", "Developer", "online",
            "API owner for the partner webhook. Include the request id with every failure.",
            "1600 Amphitheatre Parkway, Mountain View, CA 94043",
            "b.watson@ymsg.com", "http://go.betacall.com/meet/b.watson",
            (("brian.watson@adventure-works.example", 1), ("brian.watson@gmail.example", 0)),
            (("650-555-0109", 1), ("650-555-0190", 0)),
        ),
        _person(
            9, "Hettie", "Richardson", "Developer", "online",
            "Covers Friday releases. She can reset the staging environment herself.",
            "18 King Street, London, EC2V 8AY",
            "h.richardson@ymsg.com", "http://go.betacall.com/meet/h.richardson",
            (("hettie.richardson@northwind.example", 1), ("hettie.richardson@gmail.example", 0)),
            (("020-7946-0044", 1), ("07700-900244", 0)),
        ),
    )
    return people
