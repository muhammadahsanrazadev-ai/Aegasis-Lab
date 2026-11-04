export interface PhoneNumber {
  number: string;
  is_primary: boolean;
}

export interface SocialLink {
  network: string;
  url: string;
}

export interface Contact {
  id: number;
  first_name: string;
  last_name: string;
  job_title: string;
  bio: string;
  address: string;
  avatar_url: string;
  status: 'online' | 'away';
  dial: string;
  meeting_url: string;
  primary_email: string;
  phones: PhoneNumber[];
  social_links: SocialLink[];
}

export interface EmailAddress {
  id: number;
  email: string;
  is_primary: boolean;
}
