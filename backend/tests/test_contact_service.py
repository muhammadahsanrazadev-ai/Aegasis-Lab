"""Service rules against a temporary database, with no HTTP."""

import pytest

from app.adapters.sqlite_repository import SqliteContactRepository
from app.domain.exceptions import ContactNotFound
from app.services.contact_service import ContactService


@pytest.fixture
def service(tmp_path):
    repository = SqliteContactRepository(tmp_path / "test.db")
    repository.prepare()
    return ContactService(repository)


def test_directory_matches_the_screen_order(service):
    contacts = service.list_contacts()
    assert [contact.last_name for contact in contacts] == [
        "Gordon", "Malone", "Stevens", "Lambert", "Lloyd",
        "Haynes", "Peters", "Watson", "Richardson",
    ]


def test_johanna_uses_the_panel_title_and_primary_email(service):
    johanna = service.list_contacts()[2]
    assert johanna.job_title == "UI/UX Designer"
    assert johanna.primary_email == "johanna.stevens@gmail.com"
    assert johanna.phones[0].number == "439-582-1578"
    assert johanna.phones[0].is_primary is True
    assert len(johanna.social_links) == 5


def test_every_contact_has_one_primary_email(service):
    for contact in service.list_contacts():
        emails = service.list_email_addresses(contact.id)
        primaries = [email for email in emails if email.is_primary]
        assert len(primaries) == 1
        assert contact.primary_email == primaries[0].email
        assert contact.avatar_file.startswith("https://randomuser.me/api/portraits/")
        assert contact.address


def test_unknown_contact_is_not_an_empty_email_list(service):
    with pytest.raises(ContactNotFound) as caught:
        service.list_email_addresses(99999)
    assert caught.value.contact_id == 99999


def test_prepare_does_not_duplicate_rows(tmp_path):
    repository = SqliteContactRepository(tmp_path / "test.db")
    repository.prepare()
    repository.prepare()
    assert len(repository.list_contacts()) == 9
