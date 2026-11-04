import { provideHttpClient } from '@angular/common/http';
import { HttpTestingController, provideHttpClientTesting } from '@angular/common/http/testing';
import { ComponentFixture, TestBed } from '@angular/core/testing';

import { API_ORIGIN } from '../../core/api/api-origin';
import { Contact } from '../../core/api/contact.model';
import { sampleContact } from '../../testing/contact.fixture';
import { ContactsPageComponent } from './contacts-page.component';

describe('ContactsPageComponent', () => {
  let fixture: ComponentFixture<ContactsPageComponent>;
  let http: HttpTestingController;

  const nicholas = sampleContact();
  const johanna = sampleContact({
    id: 3,
    first_name: 'Johanna',
    last_name: 'Stevens',
    job_title: 'UI/UX Designer',
    primary_email: 'johanna.stevens@gmail.com',
    phones: [{ number: '439-582-1578', is_primary: true }],
  });

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ContactsPageComponent],
      providers: [provideHttpClient(), provideHttpClientTesting()],
    }).compileComponents();
    fixture = TestBed.createComponent(ContactsPageComponent);
    http = TestBed.inject(HttpTestingController);
  });

  afterEach(() => http.verify());

  function flushEmails(bodyFor: (id: number) => object[]): void {
    const requests = http.match((request) => request.url.includes('/email_addresses'));
    for (const request of requests) {
      const id = Number(request.request.url.match(/contacts\/(\d+)\/email_addresses/)?.[1]);
      request.flush(bodyFor(id));
    }
  }

  function load(contacts: Contact[], bodyFor: (id: number) => object[] = () => []): void {
    fixture.detectChanges();
    http.expectOne(`${API_ORIGIN}/contacts`).flush(contacts);
    flushEmails(bodyFor);
    fixture.detectChanges();
  }

  it('renders the directory from GET /contacts and requests the first contact emails', () => {
    fixture.detectChanges();
    const contacts = http.expectOne(`${API_ORIGIN}/contacts`);
    expect(contacts.request.method).toBe('GET');
    contacts.flush([nicholas, johanna]);
    const emails = http.match(`${API_ORIGIN}/contacts/1/email_addresses`);
    expect(emails.length).toBeGreaterThan(0);
    expect(emails[0].request.method).toBe('GET');
    flushEmails((id) => id === 1
      ? [{ id: 9, email: 'nicholas.gordon@northwind.example', is_primary: true }]
      : []);
    fixture.detectChanges();

    const names = Array.from(fixture.nativeElement.querySelectorAll('.who-name')).map(
      (node) => (node as HTMLElement).textContent?.trim(),
    );
    expect(names).toEqual(['Nicholas Gordon', 'Johanna Stevens']);
    expect(fixture.nativeElement.querySelector('.profile-name').textContent).toContain('Nicholas Gordon');
    const arrows = fixture.nativeElement.querySelectorAll('.arrows button');
    expect(arrows.length).toBe(2);
    expect((arrows[0] as HTMLButtonElement).disabled).toBeTrue();
    expect((arrows[1] as HTMLButtonElement).disabled).toBeTrue();
    expect(fixture.nativeElement.querySelectorAll('.row .more').length).toBe(2);
    expect(fixture.nativeElement.querySelector('.actions .more')).not.toBeNull();
  });

  it('filters the loaded rows without another contacts request', () => {
    load([nicholas, johanna]);
    const input: HTMLInputElement = fixture.nativeElement.querySelector('input');
    input.value = 'designer';
    input.dispatchEvent(new Event('input'));
    fixture.detectChanges();
    const names = Array.from(fixture.nativeElement.querySelectorAll('.who-name')).map(
      (node) => (node as HTMLElement).textContent?.trim(),
    );
    expect(names).toEqual(['Johanna Stevens']);
    http.expectNone(`${API_ORIGIN}/contacts`);
  });

  it('matches a secondary email from the email endpoint', () => {
    load([nicholas, johanna], (id) => id === 1
      ? [
          { id: 9, email: 'nicholas.gordon@northwind.example', is_primary: true },
          { id: 10, email: 'nicholas.gordon@gmail.example', is_primary: false },
        ]
      : [
          { id: 1, email: 'johanna.stevens@gmail.com', is_primary: true },
          { id: 2, email: 'johanna.stevens@whiteui.store', is_primary: false },
        ]);
    const input: HTMLInputElement = fixture.nativeElement.querySelector('input');
    input.value = 'whiteui';
    input.dispatchEvent(new Event('input'));
    fixture.detectChanges();
    const names = Array.from(fixture.nativeElement.querySelectorAll('.who-name')).map(
      (node) => (node as HTMLElement).textContent?.trim(),
    );
    expect(names).toEqual(['Johanna Stevens']);
  });

  it('does not request emails when the contact list fails', () => {
    fixture.detectChanges();
    http.expectOne(`${API_ORIGIN}/contacts`).flush('no', { status: 500, statusText: 'Server Error' });
    fixture.detectChanges();
    http.expectNone((request) => request.url.includes('email_addresses'));
    expect(fixture.nativeElement.textContent).toContain('Contacts could not be loaded.');
  });

  it('keeps the profile when the email request fails', () => {
    fixture.detectChanges();
    http.expectOne(`${API_ORIGIN}/contacts`).flush([nicholas]);
    http.match(`${API_ORIGIN}/contacts/1/email_addresses`).forEach((request) => {
      request.flush('no', { status: 500, statusText: 'Server Error' });
    });
    fixture.detectChanges();
    expect(fixture.nativeElement.querySelector('.profile-name').textContent).toContain('Nicholas Gordon');
    expect(fixture.nativeElement.textContent).toContain('Email addresses could not be loaded.');
  });

  it('loads the chosen contact emails when a row is selected', () => {
    load([nicholas, johanna]);
    const rows = fixture.nativeElement.querySelectorAll('.row-main');
    (rows[1] as HTMLButtonElement).click();
    http.match(`${API_ORIGIN}/contacts/3/email_addresses`).forEach((request) => request.flush([
      { id: 1, email: 'johanna.stevens@gmail.com', is_primary: true },
    ]));
    fixture.detectChanges();
    expect(fixture.nativeElement.querySelector('.profile-name').textContent).toContain('Johanna Stevens');
    expect(fixture.nativeElement.textContent).toContain('johanna.stevens@gmail.com');
  });
});
