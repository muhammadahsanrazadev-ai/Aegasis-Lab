"""Flask application factory.

The brief asks for Flask-RESTPlus. The venv pins Flask 1.1.4 and Werkzeug
1.0.1, and restplus_compat repairs the two imports that package still uses.
Flask-RESTX is not used.
"""

from pathlib import Path

import app.restplus_compat  # noqa: F401  must run before flask_restplus
from flask import Flask
from flask_cors import CORS
from flask_restplus import Api

from app.adapters.sqlite_repository import SqliteContactRepository
from app.api.resources import register_contacts
from app.db import DEFAULT_DB_PATH
from app.services.contact_service import ContactService


def create_app(db_path=None):
    app = Flask(__name__, static_folder=None)
    # The Angular route is also /contacts, so the browser calls this origin
    # directly. Do not proxy /contacts through the dev server.
    CORS(app, resources={r"/contacts*": {"origins": [
        "http://localhost:4200",
        "http://127.0.0.1:4200",
    ]}})
    app.url_map.strict_slashes = False

    path = Path(db_path) if db_path else DEFAULT_DB_PATH
    repository = SqliteContactRepository(path)
    repository.prepare()
    app.extensions["contact_service"] = ContactService(repository)

    api = Api(
        app,
        title="Contacts API",
        version="1.0",
        description="Contact directory for customer-service representatives.",
        doc="/docs",
    )
    register_contacts(api)
    return app
