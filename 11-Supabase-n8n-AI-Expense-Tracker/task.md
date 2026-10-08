# Assigned Task: AI Email Expense Tracker with Supabase

Create an n8n automation that receives financial messages by email, identifies whether each message describes an expense or income, saves it in Supabase, and sends a report to the user.

## Example Messages

```text
1000 expense deducted from JazzCash; it was paid for yesterday's dinner.
```

```text
Salary of 50,000 received in my bank account.
```

The automation should classify the first message as an expense and the second as income.

## Required Flow

```text
Gmail Trigger
  ↓
AI reads and classifies the message
  ↓
Extract structured transaction details
  ↓
Save transaction in Supabase
  ↓
Calculate totals
  ↓
Send report email
```

## Recommended Database Design

For a complete tracker, create a `transactions` table with fields similar to:

| Column | Purpose |
|--------|---------|
| `id` | Unique transaction ID |
| `transaction_type` | `income` or `expense` |
| `amount` | Numeric amount |
| `currency` | Currency code, for example `PKR` |
| `category` | Food, salary, transport, and so on |
| `description` | Short transaction description |
| `payment_method` | JazzCash, bank, cash, card, and so on |
| `transaction_date` | Date of the transaction |
| `user_email` | Email address of the user |
| `created_at` | Date and time at which the row was saved |

## Provided Workflow

The supplied [workflow JSON](workflows/expense-tracker-workflow.json) is a working starting point for the **expense** side of the task. It:

1. Watches Gmail for emails whose subject contains `expense`.
2. Uses Groq and a structured output parser to extract expense data.
3. Inserts the data into an `expenses` Supabase table.
4. Reads all saved expenses.
5. Sends an HTML expense report.

To support income as required by the task, update the workflow rather than assuming the provided expense-only JSON already handles salary messages.

## Completion Checklist

- [ ] Supabase project and table created
- [ ] Gmail, Groq, and Supabase credentials configured in n8n
- [ ] Expense message tested
- [ ] Income message tested after adding an income path
- [ ] Transaction saved with the correct user email
- [ ] Report shows the new transaction and totals
- [ ] Sensitive keys and connection strings kept out of GitHub
