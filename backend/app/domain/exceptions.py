"""Errors the service raises. The resource chooses the HTTP status."""

class ContactNotFound(LookupError):
    def __init__(self, contact_id: int) -> None:
        self.contact_id = contact_id
        super().__init__(f"No contact exists with id {contact_id}.")
