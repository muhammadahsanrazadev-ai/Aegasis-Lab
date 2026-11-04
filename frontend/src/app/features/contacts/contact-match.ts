import { Contact } from '../../core/api/contact.model';

export function primaryPhone(contact: Contact): string {
  const primary = contact.phones.find((phone) => phone.is_primary);
  return (primary ?? contact.phones[0])?.number ?? '';
}

/**
 * Filters the contacts already loaded. This does not call the API.
 * `emails` is every address from that contact's email endpoint, primary and
 * secondary. The directory payload only carries primary_email, so the page
 * passes the rest in after those calls return.
 */
export function contactMatches(
  contact: Contact,
  query: string,
  emails: readonly string[] = [],
): boolean {
  const needle = query.trim().toLowerCase();
  if (!needle) {
    return true;
  }
  const phoneText = contact.phones.map((phone) => phone.number).join(' ');
  const haystack = [
    contact.first_name,
    contact.last_name,
    `${contact.first_name} ${contact.last_name}`,
    contact.job_title,
    contact.primary_email,
    ...emails,
    phoneText,
  ].join(' ').toLowerCase();
  const compact = (value: string) => value.replace(/[-\s]/g, '');
  return haystack.includes(needle) || compact(haystack).includes(compact(needle));
}
