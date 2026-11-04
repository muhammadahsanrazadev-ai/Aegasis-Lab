import { provideHttpClient } from '@angular/common/http';
import { HttpTestingController, provideHttpClientTesting } from '@angular/common/http/testing';
import { ComponentFixture, TestBed } from '@angular/core/testing';

import { API_ORIGIN } from '../../../core/api/api-origin';
import { ContactSelectionService } from '../../../core/state/contact-selection.service';
import { sampleContact } from '../../../testing/contact.fixture';
import { ContactListComponent } from './contact-list.component';

describe('ContactListComponent', () => {
  let fixture: ComponentFixture<ContactListComponent>;
  let http: HttpTestingController;
  let selection: ContactSelectionService;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ContactListComponent],
      providers: [provideHttpClient(), provideHttpClientTesting()],
    }).compileComponents();
    fixture = TestBed.createComponent(ContactListComponent);
    http = TestBed.inject(HttpTestingController);
    selection = TestBed.inject(ContactSelectionService);
  });

  afterEach(() => http.verify());

  it('shows Loading and waits for an id before requesting emails', () => {
    fixture.detectChanges();
    expect(fixture.nativeElement.textContent).toContain('Loading');
    http.expectNone((request) => request.url.includes('email_addresses'));

    selection.setContacts([sampleContact({ id: 3, first_name: 'Johanna', last_name: 'Stevens' })]);
    const request = http.expectOne(`${API_ORIGIN}/contacts/3/email_addresses`);
    expect(request.request.method).toBe('GET');
    request.flush([
      { id: 1, email: 'johanna.stevens@gmail.com', is_primary: true },
      { id: 2, email: 'johanna.stevens@whiteui.store', is_primary: false },
    ]);
    fixture.detectChanges();
    expect(fixture.nativeElement.textContent).toContain('johanna.stevens@gmail.com');
    expect(fixture.nativeElement.textContent).toContain('johanna.stevens@whiteui.store');
  });

  it('does not request emails when the directory failed', () => {
    selection.setListFailed('Contacts could not be loaded.');
    fixture.detectChanges();
    http.expectNone((request) => request.url.includes('/contacts'));
    expect(fixture.nativeElement.textContent.trim()).toBe('');
  });
});
