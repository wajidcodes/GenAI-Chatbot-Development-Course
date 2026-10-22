# Lecture 13 — Apify & Job Discovery Automation

## 1. Apify

Apify is a platform for running and managing web data extraction and automation tools called **Actors**. An Actor can accept input, perform a defined task, and produce structured output such as a dataset. Actors may be supplied by Apify or built by users. Their availability and permitted use depend on the website, Actor, account, and applicable terms.

For a course workflow, Apify can be connected to n8n through a supported integration or API. Credentials should be stored in n8n's credential manager, not pasted into workflow notes or committed files.

## 2. Proposed Job-Discovery Workflow

The candidate first visits LinkedIn manually, searches for relevant roles, and copies a search/results URL. The URL becomes the workflow input. An allowed Apify Actor or API may then retrieve job data that it is permitted to access.

```text
User supplies search URL and candidate profile
  ↓
Validate input and start the permitted data source
  ↓
Retrieve available job records
  ↓
Normalize fields and remove duplicates
  ↓
Compare each role against profile criteria
  ↓
Show evidence, score, and reasons for each match
  ↓
Draft an application email for selected roles
  ↓
User reviews and approves any outgoing message
```

The exact workflow depends on the selected Actor's input and output schema. A robust implementation should validate the URL, handle missing fields, cap the number of records processed, and report errors clearly.

## 3. Candidate Profile and Matching

The candidate can provide a profile containing skills, experience level, preferred locations, role titles, work arrangement, and other preferences. The workflow can compare these criteria with the structured job fields.

A useful result should explain its reasoning rather than return only a score. For example, it could show matched skills, unmet requirements, location compatibility, and missing information. The score is a prioritization aid, not a hiring prediction or a guarantee of eligibility.

## 4. Email Drafts and Human Review

For jobs a person selects, an LLM can draft a concise email using the job description and accurate details supplied by the candidate. The workflow should not invent qualifications or experience. The candidate should review the listing, verify the recipient and application instructions, edit the draft, and approve sending it.

A safer first version saves drafts or sends a shortlist to the candidate instead of automatically applying to every result. This helps prevent duplicate, inaccurate, or unwanted applications.

## 5. Responsible Use and Platform Rules

Automated LinkedIn collection and automatic applications are not guaranteed to comply with LinkedIn policies or other platform terms. Before running a workflow:

- Use only permitted Apify Actors, official APIs, or other authorized sources.
- Check the relevant website and Actor terms, and obey rate limits.
- Do not bypass sign-in protections, CAPTCHAs, access controls, or technical restrictions.
- Collect only the data needed for the learning task and protect candidate information.
- Review job matches and every email draft.
- Keep a person involved in deciding whether an application is sent.

## 6. n8n Concepts to Practice

- Form, webhook, or manual trigger for receiving the URL and profile
- HTTP/API or supported Apify node for an authorized Actor run
- Wait/polling and dataset retrieval where required by the Actor
- Split Out, Edit Fields, IF, and Remove Duplicates nodes for processing
- LLM step with explicit evidence-based matching instructions
- Gmail or another email node configured to create drafts or send only after approval
- Error branches, logging, and limits on records per run

## Learning Outcome

I can plan an n8n workflow that accepts a manually chosen job-search URL, processes job data from an authorized source, explains potential matches, and prepares application messages for review.
