# Lecture 13 — Apify & Job Discovery Automation

## Overview

This lecture introduces Apify and a proposed n8n workflow for finding job opportunities. The user searches LinkedIn manually, copies a relevant search or results URL, and provides it to the workflow. The workflow then retrieves permitted job data, compares opportunities with a user-defined profile, and prepares application emails for review.

## Topics Covered

- Apify actors and structured web data
- Passing a manually selected job-search URL into n8n
- Retrieving and normalizing job listings
- Comparing job requirements with a candidate profile
- Preparing tailored application email drafts
- Human review and safe automation boundaries

## Workflow Outline

```text
Manually search LinkedIn and choose a relevant results page
  ↓
Provide its URL to an n8n workflow
  ↓
Use an allowed Apify actor/API to retrieve permitted listing data
  ↓
Normalize listings and remove duplicates
  ↓
Evaluate fit against the candidate's stated profile
  ↓
Prepare a ranked shortlist and email drafts
  ↓
User reviews each match and message before any application is sent
```

## Responsible Use

This is a learning task, not a guarantee that automated collection or applications are permitted by LinkedIn or any job platform. Use only Apify actors and APIs that are permitted for the source and purpose, follow applicable site terms and rate limits, and avoid bypassing access controls. Review every job match and email. Do not send applications without appropriate user oversight and approval.

## Included Materials

| File | Description |
|------|-------------|
| [notes.md](notes.md) | Apify, workflow design, matching, and responsible-use notes |
| [task.md](task.md) | Practical n8n job discovery and application-support task |

## Learning Outcome

After this lecture, I can describe how a manually selected job-search URL can start an n8n workflow that organizes permitted listing data, evaluates fit transparently, and prepares application drafts for a person to review.
