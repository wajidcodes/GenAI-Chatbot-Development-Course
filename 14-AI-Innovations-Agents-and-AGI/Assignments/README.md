# Week 14 Assignment

This folder contains the assignment details shown in the supplied course screenshot, a final prepared PDF submission, editable source drafts, a local JobPilot AI agent, and related n8n workflow exports. The proposed business is an AI-powered job and opportunity discovery service for students and early-career applicants. It is a proposal, not a report of a launched business or completed results.

## Files

| File | Description |
|------|-------------|
| [assignment-question.md](assignment-question.md) | Title, due date, status, and prompt transcribed from the screenshot |
| [RN_882016_Assignment#01.pdf](RN_882016_Assignment%2301.pdf) | Final prepared five-page PDF submission for Assignment #01 |
| [submission-draft.md](submission-draft.md) | Complete editable Markdown draft |
| [submission-draft.txt](submission-draft.txt) | Plain-text version for copying into an assignment portal |
| [agent.py](agent.py) | JobPilot AI agent: collects sample or supplied data, scores job fit, prepares materials, and requires per-email approval before sending |
| [workflows/linkedin-outreach-workflow-dry-run.json](workflows/linkedin-outreach-workflow-dry-run.json) | Latest n8n workflow export; its dry-run behavior avoids treating a missing contact address as a real recipient |
| [workflows/linkedin-outreach-workflow-original.json](workflows/linkedin-outreach-workflow-original.json) | Original n8n workflow export retained for comparison |

## How the Materials Relate

The PDF presents the JobPilot AI business proposal. The Python agent and n8n workflow exports are supporting implementation material for that same idea: they find or process permitted job information, compare it with a user profile, draft truthful application materials, and keep a person in control of any email sent.

The agent is designed to run in a safe dry-run mode when email credentials are absent. Even when credentials are configured, it asks for confirmation before each email. Review the workflow and keep all credentials, API keys, résumés, and personal information out of GitHub.

## Repository

[GenAI and Chatbot Development Course on GitHub](https://github.com/wajidcodes/GenAI-Chatbot-Development-Course)

## Submission Reminder

The source screenshot lists the status as **NOT SUBMITTED** and the due date as **Oct 22, 2026 at 11:59 PM**. This folder records that source status; creating a draft here does not submit the assignment.
