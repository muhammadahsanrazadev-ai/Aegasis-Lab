import { Routes } from '@angular/router';

import { ContactsPageComponent } from './features/contacts/contacts-page.component';

export const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'contacts' },
  { path: 'contacts', component: ContactsPageComponent },
];
