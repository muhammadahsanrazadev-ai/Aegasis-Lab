import { provideHttpClient } from '@angular/common/http';
import { HttpTestingController, provideHttpClientTesting } from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';

import { API_ORIGIN } from './api-origin';
import { ContactsApiService } from './contacts-api.service';

describe('ContactsApiService', () => {
  let service: ContactsApiService;
  let http: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [provideHttpClient(), provideHttpClientTesting()],
    });
    service = TestBed.inject(ContactsApiService);
    http = TestBed.inject(HttpTestingController);
  });

  afterEach(() => http.verify());

  it('requests GET /contacts', () => {
    service.listContacts().subscribe();
    const request = http.expectOne(`${API_ORIGIN}/contacts`);
    expect(request.request.method).toBe('GET');
    request.flush([]);
  });

  it('requests GET /contacts/{id}/email_addresses', () => {
    service.listEmailAddresses(3).subscribe();
    const request = http.expectOne(`${API_ORIGIN}/contacts/3/email_addresses`);
    expect(request.request.method).toBe('GET');
    request.flush([]);
  });
});
