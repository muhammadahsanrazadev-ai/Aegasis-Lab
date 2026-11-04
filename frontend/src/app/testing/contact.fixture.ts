import { Contact } from '../core/api/contact.model';

export function sampleContact(overrides: Partial<Contact> = {}): Contact {
  return {
    id: 1,
    first_name: 'Nicholas',
    last_name: 'Gordon',
    job_title: 'Developer',
    bio: 'Builds the billing service.',
    address: '18 King Street, London, EC2V 8AY',
    avatar_url: 'http://127.0.0.1:5000/static/avatars/nicholas-gordon.png',
    status: 'online',
    dial: 'n.gordon@ymsg.com',
    meeting_url: 'http://go.betacall.com/meet/n.gordon',
    primary_email: 'nicholas.gordon@northwind.example',
    phones: [
      { number: '020-7946-0101', is_primary: true },
      { number: '07700-900101', is_primary: false },
    ],
    social_links: [
      { network: 'facebook', url: 'https://facebook.com/nicholas.gordon' },
    ],
    ...overrides,
  };
}
