import { AsyncPipe } from '@angular/common';
import { Component, inject } from '@angular/core';
import { Observable, combineLatest, of } from 'rxjs';
import { catchError, distinctUntilChanged, map, startWith, switchMap } from 'rxjs/operators';

import { EmailAddress } from '../../../core/api/contact.model';
import { ContactsApiService } from '../../../core/api/contacts-api.service';
import { ContactSelectionService } from '../../../core/state/contact-selection.service';

type EmailView =
  | { kind: 'blocked' }
  | { kind: 'loading' }
  | { kind: 'error' }
  | { kind: 'ready'; emails: EmailAddress[] };

/**
 * The brief's contact-list shows the selected contact's emails.
 * The name and the rest of the profile stay in contact-details, because the
 * frame shows that name once. "Emails and contact details" is this email block.
 */
@Component({
  selector: 'contact-list',
  imports: [AsyncPipe],
  templateUrl: './contact-list.component.html',
  styleUrl: './contact-list.component.scss',
})
export class ContactListComponent {
  private readonly api = inject(ContactsApiService);
  private readonly selection = inject(ContactSelectionService);

  readonly view$ = combineLatest([
    this.selection.selectedId$,
    this.selection.listError$,
  ]).pipe(
    distinctUntilChanged((left, right) => left[0] === right[0] && left[1] === right[1]),
    switchMap(([id, listError]): Observable<EmailView> => {
      if (listError) {
        // A failed directory never starts the email request.
        return of({ kind: 'blocked' });
      }
      if (id == null) {
        // Waiting for an id is Loading, not an empty email list.
        return of({ kind: 'loading' });
      }
      return this.api.listEmailAddresses(id).pipe(
        map((emails) => ({ kind: 'ready', emails }) satisfies EmailView),
        startWith({ kind: 'loading' } satisfies EmailView),
        catchError(() => of({ kind: 'error' } satisfies EmailView)),
      );
    }),
  );
}
