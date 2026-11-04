"""HTTP resources. Business rules stay in the service."""

import app.restplus_compat  # noqa: F401  must run before flask_restplus
from flask import current_app
from flask_restplus import Api, Namespace, Resource, abort, fields

from app.domain.exceptions import ContactNotFound
from app.seed import PORTRAIT_URLS
from app.services.contact_service import ContactService


def register_contacts(api):
    # type: (Api) -> None
    namespace = Namespace("contacts", description="Contacts and their email addresses")

    phone_model = namespace.model("PhoneNumber", {
        "number": fields.String(required=True),
        "is_primary": fields.Boolean(required=True),
    })
    social_model = namespace.model("SocialLink", {
        "network": fields.String(required=True),
        "url": fields.String(required=True),
    })
    contact_model = namespace.model("Contact", {
        "id": fields.Integer(required=True),
        "first_name": fields.String(required=True),
        "last_name": fields.String(required=True),
        "job_title": fields.String(required=True),
        "bio": fields.String(required=True),
        "address": fields.String(required=True),
        "avatar_url": fields.String(required=True),
        "status": fields.String(required=True),
        "dial": fields.String(required=True),
        "meeting_url": fields.String(required=True),
        "primary_email": fields.String(required=True),
        "phones": fields.List(fields.Nested(phone_model), required=True),
        "social_links": fields.List(fields.Nested(social_model), required=True),
    })
    email_model = namespace.model("EmailAddress", {
        "id": fields.Integer(required=True),
        "email": fields.String(required=True),
        "is_primary": fields.Boolean(required=True),
    })

    @namespace.route("")
    class ContactCollection(Resource):
        @namespace.marshal_list_with(contact_model)
        def get(self):
            """List the directory a representative scans."""
            return [_contact_payload(contact) for contact in _service().list_contacts()]

    @namespace.route("/<int:contact_id>/email_addresses")
    class ContactEmailAddresses(Resource):
        @namespace.marshal_list_with(email_model)
        @namespace.response(404, "Contact not found")
        def get(self, contact_id):
            """List every email address for one contact."""
            try:
                emails = _service().list_email_addresses(contact_id)
            except ContactNotFound as error:
                abort(404, message=str(error))
            return [
                {"id": email.id, "email": email.email, "is_primary": email.is_primary}
                for email in emails
            ]

    api.add_namespace(namespace, path="/contacts")


def _service():
    # type: () -> ContactService
    return current_app.extensions["contact_service"]


def _avatar_url(contact):
    stored = contact.avatar_file or ""
    if stored.startswith("http://") or stored.startswith("https://"):
        return stored
    # prepare() does not rewrite a row saved before the https portraits.
    return PORTRAIT_URLS.get(contact.id, "")


def _contact_payload(contact):
    return {
        "id": contact.id,
        "first_name": contact.first_name,
        "last_name": contact.last_name,
        "job_title": contact.job_title,
        "bio": contact.bio,
        "address": contact.address,
        "avatar_url": _avatar_url(contact),
        "status": contact.status,
        "dial": contact.dial,
        "meeting_url": contact.meeting_url,
        "primary_email": contact.primary_email,
        "phones": [
            {"number": phone.number, "is_primary": phone.is_primary}
            for phone in contact.phones
        ],
        "social_links": [
            {"network": link.network, "url": link.url}
            for link in contact.social_links
        ],
    }
