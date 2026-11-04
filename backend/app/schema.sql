CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    job_title TEXT NOT NULL,
    bio TEXT NOT NULL,
    address TEXT NOT NULL,
    avatar_file TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('online', 'away')),
    dial TEXT NOT NULL,
    meeting_url TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS email_addresses (
    id INTEGER PRIMARY KEY,
    contact_id INTEGER NOT NULL REFERENCES contacts (id),
    email TEXT NOT NULL,
    is_primary INTEGER NOT NULL CHECK (is_primary IN (0, 1))
);

CREATE TABLE IF NOT EXISTS phones (
    id INTEGER PRIMARY KEY,
    contact_id INTEGER NOT NULL REFERENCES contacts (id),
    number TEXT NOT NULL,
    is_primary INTEGER NOT NULL CHECK (is_primary IN (0, 1))
);

CREATE TABLE IF NOT EXISTS social_links (
    id INTEGER PRIMARY KEY,
    contact_id INTEGER NOT NULL REFERENCES contacts (id),
    network TEXT NOT NULL,
    url TEXT NOT NULL
);
