"""Sample rows for the contacts screen.

Assumption: the desktop frame does not show an address block. The brief still
requires an address, so each contact has one and the details pane shows it
above the social row. Social is the last row.

The list row for Johanna says Project Manager and the open panel says
UI/UX Designer. One contact has one title. The panel title is the one stored.
"""

# Dummy portraits are remote image links, one per contact, in directory order.
PORTRAIT_URLS = {
    1: "https://randomuser.me/api/portraits/men/75.jpg",
    2: "https://randomuser.me/api/portraits/men/22.jpg",
    3: "https://randomuser.me/api/portraits/women/44.jpg",
    4: "https://randomuser.me/api/portraits/men/33.jpg",
    5: "https://randomuser.me/api/portraits/women/65.jpg",
    6: "https://randomuser.me/api/portraits/men/41.jpg",
    7: "https://randomuser.me/api/portraits/women/17.jpg",
    8: "https://randomuser.me/api/portraits/men/52.jpg",
    9: "https://randomuser.me/api/portraits/women/28.jpg",
    10: "https://randomuser.me/api/portraits/women/68.jpg",
    11: "https://randomuser.me/api/portraits/men/45.jpg",
    12: "https://randomuser.me/api/portraits/women/32.jpg",
    13: "https://randomuser.me/api/portraits/men/36.jpg",
    14: "https://randomuser.me/api/portraits/women/50.jpg",
    15: "https://randomuser.me/api/portraits/men/61.jpg",
    16: "https://randomuser.me/api/portraits/women/72.jpg",
    17: "https://randomuser.me/api/portraits/men/85.jpg",
    18: "https://randomuser.me/api/portraits/women/12.jpg",
    19: "https://randomuser.me/api/portraits/men/15.jpg",
    20: "https://randomuser.me/api/portraits/women/90.jpg",
    21: "https://randomuser.me/api/portraits/men/29.jpg",
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
    """Frame order first, then extra people so the directory list scrolls."""
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
        _person(
            10, "Claire", "Nguyen", "Customer Success", "online",
            "Owns the renewal call. Confirm the seat count before sending the quote.",
            "200 George Street, Sydney, NSW 2000",
            "c.nguyen@ymsg.com", "http://go.betacall.com/meet/c.nguyen",
            (("claire.nguyen@northwind.example", 1), ("claire.nguyen@gmail.example", 0)),
            (("02-8015-4400", 1), ("04-2211-4400", 0)),
        ),
        _person(
            11, "Omar", "Haddad", "Account Manager", "away",
            "Covers the Gulf accounts. Write the timezone in the meeting invite.",
            "1 Sheikh Zayed Road, Dubai",
            "o.haddad@ymsg.com", "http://go.betacall.com/meet/o.haddad",
            (("omar.haddad@contoso.example", 1), ("omar.haddad@gmail.example", 0)),
            (("04-555-0190", 1), ("050-555-0144", 0)),
        ),
        _person(
            12, "Priya", "Shah", "Analyst", "online",
            "Prepares the weekly usage report. Ask for the export before noon.",
            "12 MG Road, Bengaluru, 560001",
            "p.shah@ymsg.com", "http://go.betacall.com/meet/p.shah",
            (("priya.shah@litware.example", 1), ("priya.shah@gmail.example", 0)),
            (("080-4123-7700", 1), ("098-4500-2211", 0)),
        ),
        _person(
            13, "Leon", "Becker", "Support Team", "online",
            "First response for billing questions. He can see the open invoice.",
            "10 Friedrichstrasse, Berlin, 10117",
            "l.becker@ymsg.com", "http://go.betacall.com/meet/l.becker",
            (("leon.becker@adventure-works.example", 1), ("leon.becker@outlook.example", 0)),
            (("030-555-0177", 1), ("0151-555-0192", 0)),
        ),
        _person(
            14, "Grace", "Kim", "Designer", "away",
            "Reviews the empty states. Send the screenshot with the browser width.",
            "28 Teheran-ro, Seoul",
            "g.kim@ymsg.com", "http://go.betacall.com/meet/g.kim",
            (("grace.kim@tailspin.example", 1), ("grace.kim@gmail.example", 0)),
            (("02-555-0130", 1), ("010-555-0188", 0)),
        ),
        _person(
            15, "Samuel", "Ortiz", "Sales Manager", "online",
            "Runs the partner desk. Do not offer a discount that is not on the sheet.",
            "500 Brickell Avenue, Miami, FL 33131",
            "s.ortiz@ymsg.com", "http://go.betacall.com/meet/s.ortiz",
            (("samuel.ortiz@wideworld.example", 1), ("samuel.ortiz@gmail.example", 0)),
            (("305-555-0166", 1), ("305-555-0102", 0)),
        ),
        _person(
            16, "Elena", "Petrova", "PR agent", "online",
            "Handles the product announcement. Share the approved quote only.",
            "7 Nevsky Prospect, Saint Petersburg",
            "e.petrova@ymsg.com", "http://go.betacall.com/meet/e.petrova",
            (("elena.petrova@litware.example", 1), ("elena.petrova@gmail.example", 0)),
            (("812-555-0140", 1), ("921-555-0175", 0)),
        ),
        _person(
            17, "Noah", "Bennett", "Developer", "away",
            "Owns the import job. Include the file name when a row is rejected.",
            "90 Albert Street, Auckland, 1010",
            "n.bennett@ymsg.com", "http://go.betacall.com/meet/n.bennett",
            (("noah.bennett@northwind.example", 1), ("noah.bennett@gmail.example", 0)),
            (("09-555-0118", 1), ("021-555-0149", 0)),
        ),
        _person(
            18, "Hannah", "Cole", "Project Manager", "online",
            "Keeps the release checklist. The freeze starts the day she names.",
            "15 Sackville Street, Dublin, D02",
            "h.cole@ymsg.com", "http://go.betacall.com/meet/h.cole",
            (("hannah.cole@contoso.example", 1), ("hannah.cole@gmail.example", 0)),
            (("01-555-0194", 1), ("087-555-0126", 0)),
        ),
        _person(
            19, "Caleb", "Brooks", "Support Team", "away",
            "Covers the night queue. He can reset a locked account.",
            "400 Broad Street, Seattle, WA 98109",
            "c.brooks@ymsg.com", "http://go.betacall.com/meet/c.brooks",
            (("caleb.brooks@adventure-works.example", 1), ("caleb.brooks@outlook.example", 0)),
            (("206-555-0181", 1), ("206-555-0137", 0)),
        ),
        _person(
            20, "Maya", "Chen", "Designer", "online",
            "Updates the contact portraits. Ask before swapping a published photo.",
            "88 Queens Road Central, Hong Kong",
            "m.chen@ymsg.com", "http://go.betacall.com/meet/m.chen",
            (("maya.chen@tailspin.example", 1), ("maya.chen@gmail.example", 0)),
            (("852-555-0162", 1), ("852-555-0108", 0)),
        ),
        _person(
            21, "Ethan", "Walsh", "Account Manager", "online",
            "Looks after the education accounts. Term dates change the renewal.",
            "250 University Avenue, Toronto, ON M5H",
            "e.walsh@ymsg.com", "http://go.betacall.com/meet/e.walsh",
            (("ethan.walsh@wideworld.example", 1), ("ethan.walsh@gmail.example", 0)),
            (("416-555-0155", 1), ("416-555-0193", 0)),
        ),
    )
    return people
