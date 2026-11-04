import { AsyncPipe } from '@angular/common';
import { Component, inject } from '@angular/core';
import { BehaviorSubject, combineLatest } from 'rxjs';
import { map } from 'rxjs/operators';

import { Contact } from '../../core/api/contact.model';
import { ContactSelectionService } from '../../core/state/contact-selection.service';
import { ContactDetailsComponent } from './contact-details/contact-details.component';
import { ContactListComponent } from './contact-list/contact-list.component';
import { contactMatches, primaryPhone } from './contact-match';

@Component({
  selector: 'app-contacts-page',
  imports: [AsyncPipe, ContactDetailsComponent, ContactListComponent],
  templateUrl: './contacts-page.component.html',
  styleUrl: './contacts-page.component.scss',
})
export class ContactsPageComponent {
  private readonly selection = inject(ContactSelectionService);
  private readonly querySubject = new BehaviorSubject('');

  readonly view$ = combineLatest([
    this.selection.contacts$,
    this.selection.listLoading$,
    this.selection.listError$,
    this.selection.selectedId$,
    this.selection.showDetail$,
    this.querySubject,
    this.selection.searchEmails$,
  ]).pipe(
    map(([contacts, loading, error, selectedId, showDetail, query, searchEmails]) => ({
      loading,
      error,
      selectedId,
      showDetail,
      query,
      rows: (contacts ?? []).filter((contact) =>
        contactMatches(contact, query, searchEmails[contact.id] ?? []),
      ),
    })),
  );

  onQuery(event: Event): void {
    this.querySubject.next((event.target as HTMLInputElement).value);
  }

  clearQuery(input: HTMLInputElement): void {
    input.value = '';
    this.querySubject.next('');
  }

  select(id: number): void {
    this.selection.select(id);
  }

  back(): void {
    this.selection.showDirectory();
  }

  phone(contact: Contact): string {
    return primaryPhone(contact);
  }
}
