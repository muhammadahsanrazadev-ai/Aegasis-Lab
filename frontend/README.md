# Frontend

Angular 19 app for the contacts screen. Run instructions for the API and this app, and the notes on design differences, are in the repository README at the project root.

Start the API first (`backend`, http://127.0.0.1:5000). Then, from this folder:

```powershell
npm install
npx ng serve --host localhost --port 4200
```

Open http://localhost:4200/contacts.

The client calls http://127.0.0.1:5000 directly. Do not proxy `/contacts`. That path is this app's route.

Unit tests:

```powershell
npx ng test --watch=false --browsers=ChromeHeadless
```

There is no end-to-end suite.
