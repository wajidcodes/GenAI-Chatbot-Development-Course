# Lecture 11 — Supabase, n8n & AI Expense Tracker

## Overview

This lecture introduced Supabase as a backend platform for creating projects, databases, and tables. It then connected Supabase to n8n and used AI to generate and import an n8n workflow in JSON format. After importing the workflow, the required credentials are configured before the automation is tested.

The practical automation is an email-based expense tracker. It reads an expense email, uses Groq AI to extract structured expense details, saves the result in a Supabase table, and sends an updated expense report by email.

## Topics Covered

- Supabase projects, databases, and tables
- Creating database tables in Supabase
- Connecting Supabase to n8n
- Using Claude or another AI assistant to draft an n8n workflow
- Importing an n8n workflow from a JSON file
- Configuring Gmail, Groq, and Supabase credentials
- Extracting structured data with an LLM
- Saving expenses and sending email reports

## Included Materials

| File | Description |
|------|-------------|
| [notes.md](notes.md) | Lecture concepts, workflow explanation, and setup notes |
| [task.md](task.md) | Expense-tracker assignment, database design, and test checklist |
| [workflows/expense-tracker-workflow.json](workflows/expense-tracker-workflow.json) | n8n workflow exported for import; its contents have not been modified |
| [screenshots/expense-tracker-workflow.png](screenshots/expense-tracker-workflow.png) | Screenshot of the supplied task workflow |

## Learning Outcome

After this lecture, I can create a Supabase table, import an AI-generated n8n workflow, configure the required credentials, and use it to store parsed email expenses and send a report.
