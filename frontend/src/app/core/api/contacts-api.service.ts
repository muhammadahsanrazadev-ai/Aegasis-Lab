import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';

import { API_ORIGIN } from './api-origin';
import { Contact, EmailAddress } from './contact.model';

/** The only place this application uses HttpClient. */
@Injectable({ providedIn: 'root' })
export class ContactsApiService {
  private readonly http = inject(HttpClient);

  listContacts(): Observable<Contact[]> {
    return this.http.get<Contact[]>(`${API_ORIGIN}/contacts`);
  }

  listEmailAddresses(contactId: number): Observable<EmailAddress[]> {
    return this.http.get<EmailAddress[]>(`${API_ORIGIN}/contacts/${contactId}/email_addresses`);
  }
}
