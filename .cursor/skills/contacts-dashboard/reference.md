# Contacts exercise reference

This file records what the brief says. It does not approve a design.

## Given

- Screen: one responsive page a customer-service representative uses to see contacts and the person they select.
- Visual reference: Figma file `7fMi9iwHrMOz3taFMcZDVe`, node `0:1` (AR Shakir contacts dashboard). The editable file is not in the repo. A public preview shows a directory on the left and the selected contact on the right.
- API, as named: `/contacts` and `/contacts/{id}/email_addresses`.
- Server: Flask, resource-based classes, RESTPlus (the brief's words).
- Client: Angular, TypeScript, HTML, SCSS.
- Components, as named: `contact-list`, `contact-details`. Both fetch on load.
- A contact has a first name, last name, address, and further liaison fields. One contact has many emails.
- The implementer chooses which fields the representative actually needs on screen.
- Forbidden: Angular Material, Material2, PrimeNG, ng-bootstrap, third-party pagination, third-party data tables.
- Tests: unit tests are encouraged. End-to-end tests are discouraged.
- GitHub submission with run instructions comes after the app exists. That phase is not open.

## Not decided

Ask one at a time. Do not answer these in code.

1. What the layers are, and which way dependencies point.
2. Backend folder responsibilities.
3. Frontend folder responsibilities.
4. How the client calls the API, and what the JSON contains.
5. Which Figma regions are in scope and which are decoration.
6. Validation, errors, and logging.
7. Auth, if any. The brief does not describe accounts.
8. Persistence. The brief does not require a database. There is no database in this repo.
9. State on the client.
10. Test placement.
