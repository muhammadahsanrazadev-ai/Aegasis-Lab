# Contacts

Customer-service contacts screen. The API is Flask. The screen is Angular.

Use two terminals. Finish the backend setup and leave the API running, then start the screen.

You need Python 3.12, and Node.js 18.19 or newer with npm.

## 1. Backend setup

Open a terminal in the `backend` folder.

Create the virtual environment:

```powershell
python -m venv .venv
```

Install every package listed in `backend/requirements.txt`:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

On macOS or Linux, use `.venv/bin/python` in place of `.\.venv\Scripts\python.exe` for this command and the ones below.

## 2. Run the API

In the same `backend` terminal:

```powershell
.\.venv\Scripts\python.exe run.py
```

Leave this terminal open. The API is at http://127.0.0.1:5000.

The first start creates `backend/contacts.db` and fills it with the sample contacts. There is no separate seed command. Contacts already in that file stay as they are. A later seed person is added on the next start.

## 3. Frontend setup

Open a second terminal in the `frontend` folder.

Install the packages listed in `frontend/package.json`:

```powershell
npm install
```

## 4. Run the screen

In the same `frontend` terminal:

```powershell
npx ng serve --host localhost --port 4200
```

Leave this terminal open. Open http://localhost:4200/contacts.

## 5. Tests

Backend, from the `backend` folder, with the virtual environment already created:

```powershell
.\.venv\Scripts\python.exe -m pytest
```

Frontend, from the `frontend` folder, after `npm install`:

```powershell
npx ng test --watch=false --browsers=ChromeHeadless
```
