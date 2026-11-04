# Contacts

Customer-service contacts screen. The API is Flask. The screen is Angular.

Use two terminals. Start the API first, then the screen.

You need Python 3.12, and Node.js 18.19 or newer with npm.

## Backend

Open a terminal in `backend` and run:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe run.py
```

On macOS or Linux, use `.venv/bin/python` in place of `.\.venv\Scripts\python.exe`.

The API is at http://127.0.0.1:5000.

The first start creates `backend/contacts.db` and fills it with the nine contacts. There is no separate seed command. If that file already has contacts, they are left as they are.

## Frontend

Open a second terminal in `frontend` and run:

```powershell
npm install
npx ng serve --host localhost --port 4200
```

Open http://localhost:4200/contacts.

## Tests

Backend, from `backend`:

```powershell
.\.venv\Scripts\python.exe -m pytest
```

Frontend, from `frontend`:

```powershell
npx ng test --watch=false --browsers=ChromeHeadless
```
