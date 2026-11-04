import { Contact } from '../../core/api/contact.model';

export function primaryPhone(contact: Contact): string {
  const primary = contact.phones.find((phone) => phone.is_primary);
  return (primary ?? contact.phones[0])?.number ?? '';
}

/** Filters the contacts already loaded. This does not call the API. */
export function contactMatches(contact: Contact, query: string): boolean {
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
    phoneText,
  ].join(' ').toLowerCase();
  const compact = (value: string) => value.replace(/[-\s]/g, '');
  return haystack.includes(needle) || compact(haystack).includes(compact(needle));
}
