"""Contact and email types. No Flask and no SQLite imports in this package."""
from dataclasses import dataclass

@dataclass(frozen=True)
class PhoneNumber:
    number: str
    is_primary: bool

@dataclass(frozen=True)
class SocialLink:
    network: str
    url: str

@dataclass(frozen=True)
class EmailAddress:
    id: int
    email: str
    is_primary: bool

@dataclass(frozen=True)
class Contact:
    """One directory row. Emails stay on their own resource."""

    id: int
    first_name: str
    last_name: str
    job_title: str
    bio: str
    address: str
    avatar_file: str
    status: str
    dial: str
    meeting_url: str
    primary_email: str
    phones: tuple[PhoneNumber, ...]
    social_links: tuple[SocialLink, ...]
