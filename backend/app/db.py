"""SQLite connection helpers. SQL for contacts lives in the adapter."""

import sqlite3
from pathlib import Path


DEFAULT_DB_PATH = Path(__file__).resolve().parents[1] / "contacts.db"
SCHEMA_PATH = Path(__file__).resolve().parent / "schema.sql"


def connect(db_path):
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def apply_schema(connection):
    connection.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    connection.commit()
