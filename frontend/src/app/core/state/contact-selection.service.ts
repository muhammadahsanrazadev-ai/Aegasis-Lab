import { Injectable } from '@angular/core';
import { BehaviorSubject, combineLatest } from 'rxjs';
import { map } from 'rxjs/operators';

import { Contact } from '../api/contact.model';

/**
 * Shared selection for the page, contact-details, and contact-list.
 * Those components do not nest inside one another.
 *
 * The first row is selected when the directory arrives so contact-list can
 * call the email endpoint on load. The desktop frame is drawn with Johanna
 * open; the list order starts at Nicholas Gordon, so he is the initial row
 * until the representative chooses another. That automatic choice does not
 * open the narrow-screen detail pane.
 */
@Injectable({ providedIn: 'root' })
export class ContactSelectionService {
  private readonly contactsSubject = new BehaviorSubject<Contact[] | null>(null);
  private readonly selectedIdSubject = new BehaviorSubject<number | null>(null);
  private readonly listErrorSubject = new BehaviorSubject<string | null>(null);
  private readonly listLoadingSubject = new BehaviorSubject<boolean>(true);
  private readonly showDetailSubject = new BehaviorSubject<boolean>(false);
  private readonly searchEmailsSubject = new BehaviorSubject<Readonly<Record<number, readonly string[]>>>({});

  readonly contacts$ = this.contactsSubject.asObservable();
  readonly selectedId$ = this.selectedIdSubject.asObservable();
  readonly listError$ = this.listErrorSubject.asObservable();
  readonly listLoading$ = this.listLoadingSubject.asObservable();
  readonly showDetail$ = this.showDetailSubject.asObservable();
  /** Every address for each contact, primary and secondary, keyed by contact id. */
  readonly searchEmails$ = this.searchEmailsSubject.asObservable();
  readonly selectedContact$ = combineLatest([this.contacts$, this.selectedId$]).pipe(
    map(([contacts, id]) => contacts?.find((contact) => contact.id === id) ?? null),
  );

  setContacts(contacts: Contact[]): void {
    this.listErrorSubject.next(null);
    this.contactsSubject.next(contacts);
    this.listLoadingSubject.next(false);
    if (contacts.length === 0) {
      this.selectedIdSubject.next(null);
      return;
    }
    const current = this.selectedIdSubject.value;
    const stillThere = contacts.some((contact) => contact.id === current);
    if (!stillThere) {
      this.selectedIdSubject.next(contacts[0].id);
    }
  }

  setSearchEmails(emails: Readonly<Record<number, readonly string[]>>): void {
    this.searchEmailsSubject.next(emails);
  }

  setListFailed(message: string): void {
    this.listLoadingSubject.next(false);
    this.listErrorSubject.next(message);
    this.contactsSubject.next(null);
    this.selectedIdSubject.next(null);
    this.searchEmailsSubject.next({});
  }

  select(id: number): void {
    this.selectedIdSubject.next(id);
    this.showDetailSubject.next(true);
  }

  showDirectory(): void {
    this.showDetailSubject.next(false);
  }
}
