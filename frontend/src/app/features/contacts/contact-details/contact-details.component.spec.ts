import { provideHttpClient } from '@angular/common/http';
import { HttpTestingController, provideHttpClientTesting } from '@angular/common/http/testing';
import { ComponentFixture, TestBed } from '@angular/core/testing';

import { API_ORIGIN } from '../../../core/api/api-origin';
import { sampleContact } from '../../../testing/contact.fixture';
import { ContactDetailsComponent } from './contact-details.component';

describe('ContactDetailsComponent', () => {
  let fixture: ComponentFixture<ContactDetailsComponent>;
  let http: HttpTestingController;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ContactDetailsComponent],
      providers: [provideHttpClient(), provideHttpClientTesting()],
    }).compileComponents();
    fixture = TestBed.createComponent(ContactDetailsComponent);
    http = TestBed.inject(HttpTestingController);
  });

  afterEach(() => http.verify());

  it('requests GET /contacts on init', () => {
    fixture.detectChanges();
    const request = http.expectOne(`${API_ORIGIN}/contacts`);
    expect(request.request.method).toBe('GET');
    const contact = sampleContact({
      id: 3,
      first_name: 'Johanna',
      last_name: 'Stevens',
      job_title: 'UI/UX Designer',
    });
    request.flush([contact]);
    fixture.detectChanges();
    expect(fixture.nativeElement.textContent).toContain('Johanna Stevens');
    expect(fixture.nativeElement.textContent).toContain('UI/UX Designer');
  });

  it('shows an error and does not keep a contact when the request fails', () => {
    fixture.detectChanges();
    http.expectOne(`${API_ORIGIN}/contacts`).flush('no', { status: 500, statusText: 'Server Error' });
    fixture.detectChanges();
    expect(fixture.nativeElement.textContent).toContain('Contacts could not be loaded.');
    expect(fixture.nativeElement.querySelector('.profile-name')).toBeNull();
  });
});
