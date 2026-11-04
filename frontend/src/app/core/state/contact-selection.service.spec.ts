import { TestBed } from '@angular/core/testing';

import { sampleContact } from '../../testing/contact.fixture';
import { ContactSelectionService } from './contact-selection.service';

describe('ContactSelectionService', () => {
  let service: ContactSelectionService;
  let selectedId: number | null;
  let showDetail: boolean;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ContactSelectionService);
    selectedId = undefined as unknown as number | null;
    showDetail = true;
    service.selectedId$.subscribe((id) => {
      selectedId = id;
    });
    service.showDetail$.subscribe((open) => {
      showDetail = open;
    });
  });

  it('selects the first contact without opening the narrow detail pane', () => {
    const first = sampleContact();
    const second = sampleContact({ id: 3, first_name: 'Johanna', last_name: 'Stevens' });
    service.setContacts([first, second]);
    expect(selectedId).toBe(1);
    expect(showDetail).toBeFalse();
  });

  it('clears the id when the directory fails', () => {
    service.setContacts([sampleContact()]);
    service.setListFailed('Contacts could not be loaded.');
    expect(selectedId).toBeNull();
  });

  it('opens the detail pane when a row is chosen and closes it on Back', () => {
    service.setContacts([sampleContact(), sampleContact({ id: 3 })]);
    service.select(3);
    expect(selectedId).toBe(3);
    expect(showDetail).toBeTrue();
    service.showDirectory();
    expect(showDetail).toBeFalse();
    expect(selectedId).toBe(3);
  });
});
