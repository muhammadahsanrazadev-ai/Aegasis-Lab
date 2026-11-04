"""Storage port. The SQLite adapter is the only implementation."""

from typing import Protocol

from app.domain.models import Contact, EmailAddress

class ContactRepository(Protocol):
    def list_contacts(self):
        """Return contacts in directory order."""

    def get_contact(self, contact_id):
        """Return one contact, or None when the id is unknown."""

    def list_email_addresses(self, contact_id):
        """Return that contact's emails. The caller already checked the id."""
