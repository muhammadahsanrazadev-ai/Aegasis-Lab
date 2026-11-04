import { sampleContact } from '../../testing/contact.fixture';
import { contactMatches } from './contact-match';

describe('contactMatches', () => {
  const johanna = sampleContact({
    id: 3,
    first_name: 'Johanna',
    last_name: 'Stevens',
    job_title: 'UI/UX Designer',
    primary_email: 'johanna.stevens@gmail.com',
    phones: [{ number: '439-582-1578', is_primary: true }],
  });

  it('matches name, job title, primary email, and phone', () => {
    expect(contactMatches(johanna, 'stevens')).toBeTrue();
    expect(contactMatches(johanna, 'designer')).toBeTrue();
    expect(contactMatches(johanna, 'whiteui')).toBeFalse();
    expect(contactMatches(johanna, 'whiteui', [
      'johanna.stevens@gmail.com',
      'johanna.stevens@whiteui.store',
    ])).toBeTrue();
    expect(contactMatches(johanna, 'johanna.stevens@gmail.com')).toBeTrue();
    expect(contactMatches(johanna, '4395821578')).toBeTrue();
    expect(contactMatches(johanna, 'nobody')).toBeFalse();
  });
});
