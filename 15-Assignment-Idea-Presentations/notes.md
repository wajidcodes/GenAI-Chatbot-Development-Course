# Lecture 15 — Assignment Idea Presentations

## Overview

This lecture was dedicated to presenting the Week 14 assignment ideas. The goal was to explain a practical business use of AI agents rather than only describe the technology.

---

## 1. My Presented Idea: JobPilot AI

My presentation was based on **JobPilot AI**, a proposed AI-assisted job and opportunity discovery service for students and early-career applicants.

The service would help users:

- Organize job, internship, scholarship, and entry-level opportunities.
- Compare a selected opportunity with the user's skills and preferences.
- Explain matched and missing requirements.
- Draft truthful application emails or résumé suggestions.
- Keep an application tracker.

The service is a proposal. It does not claim that it has been launched or that it guarantees hiring results.

---

## 2. Target Audience

The initial audience is:

- University students
- Recent graduates
- Junior IT and software applicants
- Early-career job seekers

These users may have limited time, may not know which roles match their skills, and may struggle to keep track of deadlines and application status.

---

## 3. Data Sources

The idea uses two main groups of data:

1. **User-provided data:** skills, projects, education, experience, preferred roles, and location preferences.
2. **Opportunity data:** user-selected job links or descriptions, official APIs, permitted feeds, partner data, and other sources that allow the intended use.

The source URL and retrieval date should be kept so the user can verify opportunities. Personal data should be collected only with consent and only when necessary.

---

## 4. Agent Workflow

```text
User profile + selected opportunity
  ↓
Collect and validate information
  ↓
Analyze job requirements and user skills
  ↓
Explain job-fit evidence and uncertainty
  ↓
Prepare résumé suggestions or an email draft
  ↓
User reviews and approves
  ↓
Save the result in an application tracker
```

The agent supports the user's decisions. It should not invent qualifications, decide eligibility, submit applications automatically, or send an email without explicit approval.

---

## 5. Value and Responsible Use

The proposed value is saving time while making application preparation more organized and relevant. A responsible version should:

- Use permitted data sources.
- Explain why a job may be a match.
- Let users correct their profile information.
- Protect résumés and personal information.
- Keep a person responsible for final decisions and messages.

---

## Learning Outcome

After presenting the idea, I understand how to describe an AI-agent solution in terms of a real audience, business value, workflow, constraints, and responsible design.
