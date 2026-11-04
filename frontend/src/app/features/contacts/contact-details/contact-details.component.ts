import { AsyncPipe } from '@angular/common';
import { Component, DestroyRef, OnInit, inject } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { combineLatest } from 'rxjs';
import { map } from 'rxjs/operators';

import { Contact } from '../../../core/api/contact.model';
import { ContactsApiService } from '../../../core/api/contacts-api.service';
import { ContactSelectionService } from '../../../core/state/contact-selection.service';
import { primaryPhone } from '../contact-match';

@Component({
  selector: 'contact-details',
  imports: [AsyncPipe],
  templateUrl: './contact-details.component.html',
  styleUrl: './contact-details.component.scss',
})
export class ContactDetailsComponent implements OnInit {
  private readonly api = inject(ContactsApiService);
  private readonly selection = inject(ContactSelectionService);
  private readonly destroyRef = inject(DestroyRef);

  readonly profile$ = combineLatest([
    this.selection.selectedContact$,
    this.selection.listLoading$,
    this.selection.listError$,
  ]).pipe(map(([contact, loading, error]) => ({ contact, loading, error })));

  ngOnInit(): void {
    this.api.listContacts().pipe(takeUntilDestroyed(this.destroyRef)).subscribe({
      next: (contacts) => this.selection.setContacts(contacts),
      error: () => this.selection.setListFailed('Contacts could not be loaded.'),
    });
  }

  phone(contact: Contact): string {
    return primaryPhone(contact);
  }

  label(network: string): string {
    const labels: Record<string, string> = {
      facebook: 'Facebook',
      pinterest: 'Pinterest',
      twitter: 'Twitter',
      linkedin: 'LinkedIn',
      google: 'Google',
    };
    return labels[network] ?? network;
  }
}
