# Contacts

One screen for a customer-service representative. The directory is on the left and the selected person is on the right. The visual reference is the AR Shakir contacts dashboard (Figma file `7fMi9iwHrMOz3taFMcZDVe`, node `0:1`). There is no separate mobile frame. Where the frame and a smaller window disagree, the reason is a comment next to that code. Those comments are listed at the end of this file.

The API is Flask-RESTPlus. The client is Angular 19, in TypeScript, HTML, and SCSS. Angular Material, Material2, PrimeNG, ng-bootstrap, and third-party pagination or data-table packages are not used. The Material Icons link in `frontend/src/index.html` is only the icon font named in the Figma type spec.

Start the API first, then the Angular app. Use two terminals.

## Prerequisites

- Python 3.12
- Node.js 18.19 or newer, with npm

## Backend

From `backend`:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe run.py
```

On macOS or Linux the same steps use `.venv/bin/python` instead of `.\.venv\Scripts\python.exe`.

The API listens on http://127.0.0.1:5000. Interactive docs are at http://127.0.0.1:5000/docs.

Endpoints, both GET only:

- `/contacts` returns the directory. Each contact includes the profile, phones, social links, `primary_email`, and `avatar_url`. It does not include the full email list.
- `/contacts/{id}/email_addresses` returns that contact's emails (`id`, `email`, `is_primary`). An unknown id is 404.

`requirements.txt` pins Flask 1.1.4, Werkzeug 1.0.1, and flask-restplus 0.13.0. Keep those pins. `app/restplus_compat.py` restores two imports that this RESTPlus release still uses. The package is Flask-RESTPlus.

### Seed

There is no seed command. `python run.py` calls `repository.prepare()`. That creates the tables and, only when `contacts` is empty, inserts the nine people from `app/seed.py`. A database that already has rows is left as it is. To load the current seed from scratch, stop the API, delete `backend/contacts.db`, and start the API again.

`contacts.db` is gitignored. The first start creates it.

Portraits are https links in `PORTRAIT_URLS`. A database created earlier stores a local file name such as `nicholas-gordon.png`. The API maps that name to the current link, so Nicholas Gordon is `men/75.jpg` without deleting the database. `men/11.jpg` was replaced because it was a poor face at 36px. The other eight portraits are unchanged.

## Frontend

From `frontend`, after the API is running:

```powershell
npm install
npx ng serve --host localhost --port 4200
```

Open http://localhost:4200/contacts.

The browser calls http://127.0.0.1:5000 directly (`frontend/src/app/core/api/api-origin.ts`). Do not proxy `/contacts` through the dev server. That path is the Angular route. CORS allows `http://localhost:4200` and `http://127.0.0.1:4200`.

On a wide window both panes show. Below 860px the directory is full width. Choosing a row opens the profile, and Back returns to the directory. The automatic first selection does not open that narrow profile. The arrow buttons hide at that width.

## Tests

Backend, from `backend`:

```powershell
.\.venv\Scripts\python.exe -m pytest
```

Frontend, from `frontend`:

```powershell
npx ng test --watch=false --browsers=ChromeHeadless
```

Unit tests only. There is no end-to-end suite.

## What the screen does

`contact-details` loads `GET /contacts` and shows the selected profile. `contact-list` is the Email block and loads `GET /contacts/{id}/email_addresses` once an id exists. The two components do not nest. The page does not call HTTP itself.

The first row, Nicholas Gordon, is selected when the directory arrives. The frame is drawn with Johanna open. The list order starts at Nicholas, so he is the initial row until someone chooses another person.

Search filters the contacts already loaded, by name, job title, primary email, and phone. It does not call the API.

Message opens a mailto for the primary email. The phone icon dials the primary number. Share screen opens `meeting_url`. More is the three-dot mark from the frame and does not open a menu.

## Differences recorded in the source

The Figma link in the exercise document is the design. These are the places the running screen leaves that frame, and the comment that says why.

| Difference | Why | Where |
| --- | --- | --- |
| No mobile frame. Below 860px one pane shows at a time, with Back. Arrows hide. Checked in the browser, not on a physical device. | A second frame was not provided. | `contacts-page.component.scss` |
| Address sits under Social. | The frame has no address row. The brief requires the field. | `contact-details.component.html`, `backend/app/seed.py` |
| Johanna's title is UI/UX Designer in the list and the profile. | The frame uses two titles for one person. One contact has one title, and the panel title is the one stored. | `backend/app/seed.py` |
| Profile and bio flow inside the right column. Photo stays 114×114, radius 26. Bio keeps a 67px minimum and the frame's label and value type. | The frame's left/top coordinates (profile 770,61 and bio 715,215) belong to a 1440 canvas and overflow other widths. | `contact-details.component.scss` |
| Label column is as wide as its text, with a 16px gap. On a narrow screen the label stacks above the value. | A fixed 55px label column clips Meeting and Address. | `frontend/src/styles.scss` |
| Names and titles wrap. | An ellipsis would hide part of the contact. | `contacts-page.component.scss` |
| A visible scrollbar on the directory and on the profile. | The frame draws no bar. On a short window the last contacts were clipped, and an overlay scrollbar was invisible. | `contacts-page.component.scss` |
| Nicholas Gordon's portrait is `men/75.jpg`. | `men/11.jpg` was a poor face at directory size. An existing database is not rewritten; the API maps the old file name to this link. | `backend/app/seed.py`, `backend/app/api/resources.py` |
| Menu, search, and message use the Material Icons font at 18px. | That is the type spec on those glyphs. `leading-trim` is Figma-only and is not valid CSS. | `frontend/src/styles.scss`, `frontend/src/index.html` |
| The menu mark does not open a menu. The arrow buttons stay visible and disabled on a wide window. | The brief has no menu. Nine contacts fit one screen, so the arrows are not a pager. | `contacts-page.component.html` |
| Search does not add an endpoint. | It filters the directory already loaded. | `contacts-page.component.html`, `contact-match.ts` |
| Message, phone, and share screen are links. More has no menu. | The frame shows the marks. The brief has no edit or delete. | `contact-details.component.html` |
| The first selected row is Nicholas, and that choice does not open the narrow profile. | The list order starts at Nicholas. The frame drawing shows Johanna. | `contact-selection.service.ts` |
| `contact-list` renders the Email block only. | The frame shows the name once, in the profile. | `contact-list.component.ts` |
| Seed runs when the API starts, and only into an empty table. | A second command would be a second way to fill the same table. | `sqlite_repository.py` |
