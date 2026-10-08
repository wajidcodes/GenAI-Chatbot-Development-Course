# Lecture 11 — Supabase, n8n & AI Expense Tracker

## 1. Supabase

Supabase is a backend platform that provides a PostgreSQL database and tools for working with application data. A Supabase project can contain a database and many tables.

Key terms:

- **Project:** The Supabase workspace for an application.
- **Database:** The PostgreSQL database inside the project.
- **Table:** A structure that stores related data in rows and columns.
- **Row:** One record in a table.
- **Column:** One type of information stored for every record.

---

## 2. Creating Tables in Supabase

For an expense tracker, a table can store the amount, category, date, payment method, and source email of every expense.

The supplied n8n workflow writes to an `expenses` table and expects these columns:

| Column | Purpose |
|--------|---------|
| `amount` | Numeric expense amount |
| `currency` | Currency code, such as `PKR` |
| `category` | Expense category selected by AI |
| `description` | Short description of the expense |
| `merchant` | Shop, vendor, or place name |
| `payment_method` | JazzCash, Easypaisa, cash, card, and so on |
| `expense_date` | Date on which the expense happened |
| `email_from` | Sender address of the source email |
| `email_subject` | Subject of the source email |
| `raw_email_body` | Original email content for reference |

---

## 3. Supabase in n8n

n8n can connect to Supabase and create, read, update, or delete rows. In this workflow, n8n first inserts the extracted expense, then reads the expense rows to create an all-time report.

```text
Email
  ↓
AI extracts expense details
  ↓
Supabase inserts a row in expenses
  ↓
Supabase reads saved expenses
  ↓
Report email is sent
```

The Supabase credential needs the project URL and an appropriate API key. Treat credentials as private; never place API keys, database passwords, or connection strings in this repository.

---

## 4. AI-Generated n8n Workflows

An AI assistant such as Claude can help draft an n8n workflow. The output can be exported or copied as JSON, then imported into n8n.

General process:

1. Describe the required automation clearly.
2. Ask the AI to create an n8n workflow JSON file.
3. In n8n, use **Import from File** or paste the workflow JSON.
4. Review every node, connection, setting, and expression.
5. Create or choose the credentials required by each node.
6. Test with safe sample data before activating the workflow.

AI-generated JSON is a starting point, not a guarantee. It must be reviewed because node versions, account settings, names of tables, and credential requirements can differ.

---

## 5. Supplied Expense-Tracker Workflow

The included workflow, [expense-tracker-workflow.json](workflows/expense-tracker-workflow.json), is named **Expense Tracker - Email to Supabase (Groq AI)**. It is inactive when imported.

### Workflow Path

```text
Gmail Trigger
  ↓
Basic LLM Chain + Groq Chat Model
  ↓
Structured Output Parser
  ↓
Prepare data for Supabase
  ↓
Insert Expense in Supabase
  ↓
Get All Expenses
  ↓
Build Report Email
  ↓
Gmail sends report
```

### What the AI Extracts

The Groq model receives the email subject, received date, and email body. It returns structured fields for:

- `amount`
- `currency`
- `category`
- `description`
- `merchant`
- `payment_method`
- `expense_date`

The workflow uses `llama-3.3-70b-versatile` at temperature `0` and asks the model to classify expenses into categories such as Food & Dining, Transport, Groceries, Bills & Utilities, and Education.

### Example

An email such as:

```text
1000 expense deducted from JazzCash; it was paid for yesterday's dinner.
```

can be converted into a record similar to:

```text
amount: 1000
currency: PKR
category: Food & Dining
payment_method: JazzCash
description: Dinner payment
```

The exact extracted values should always be checked during testing.

---

## 6. Credentials Required

Before running the imported workflow, configure:

- **Gmail OAuth2:** for receiving expense emails and sending the report.
- **Groq API:** for the `Groq Chat Model` node.
- **Supabase:** for creating and reading rows in the `expenses` table.

The final Gmail node in the supplied JSON has a placeholder recipient, `your-email@example.com`. Replace it inside n8n with the intended report address before activating the workflow.

---

## 7. Important Scope Note: Income

The assignment brief includes income, for example a salary received through JazzCash. The supplied JSON workflow currently extracts and stores **expenses only** in the `expenses` table. It does not include an income path or a transaction-type field.

To meet the full income-and-expense requirement, extend the table and workflow with a field such as `transaction_type` (`expense` or `income`), update the AI prompt and output parser, and adjust the report to show income, expenses, and balance separately.

---

## Learning Outcome

After this lecture, I understand how Supabase can be used with n8n, how an imported workflow is reviewed and configured, and how AI can turn unstructured email text into database records.
