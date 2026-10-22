# Lecture 13 Task — Job Discovery and Application Support

## Objective

Design an n8n workflow that accepts a job-search URL chosen manually by the user, retrieves job data through an authorized Apify Actor or API, identifies roles that may fit a candidate profile, and prepares application email drafts.

## Requirements

1. Create a candidate profile with role titles, skills, experience level, preferred location, and work arrangement. Use sample information for testing.
2. Manually search LinkedIn and provide a relevant search/results URL as workflow input.
3. Use only a permitted Actor/API and document its expected input and output. If no suitable authorized source is available, use a supplied sample dataset instead.
4. Normalize job title, company, location, description, URL, and application method where available. Handle missing fields and duplicate listings.
5. Compare each listing with the profile and show why it may or may not be a match. Do not treat an AI score as a hiring decision.
6. Create a shortlist and draft an application email for user-selected roles. Do not invent qualifications or send applications automatically.
7. Add an error path and a reasonable limit on the number of listings processed.

## Deliverables

- n8n workflow export with credentials excluded
- Sample candidate profile and sample job data, with personal data removed
- Screenshot or short explanation of the workflow
- A brief note describing the data source and its permitted use

## Responsible Use

Automated collection and auto-application are not guaranteed to comply with LinkedIn policies or other site terms. Check the applicable terms, use permitted sources, respect rate limits, do not bypass technical restrictions, and require a person to review job matches and email content before any application is sent.
