"""Use-cases. This module does not import Flask or sqlite3."""

from app.domain.exceptions import ContactNotFound

class ContactService:
    def __init__(self, repository):
        self._repository = repository

    def list_contacts(self):
        return self._repository.list_contacts()

    def list_email_addresses(self, contact_id):
        # An unknown id must not look like a contact who simply has no email.
        if self._repository.get_contact(contact_id) is None:
            raise ContactNotFound(contact_id)
        return self._repository.list_email_addresses(contact_id)
