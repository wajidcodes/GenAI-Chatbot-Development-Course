# Lecture 9 — n8n Email Attachment & Data Automation Revision

## Overview

Lecture 9 revised the practical automation concepts from Lecture 8. The goal was to understand how an n8n workflow receives an Excel attachment, converts it into usable records, checks each record, and performs the correct action.

---

## 1. Complete Workflow Review

The main workflow can be understood as:

```text
Email Trigger
    ↓
Email Attachment (binary data)
    ↓
Extract Attachment
    ↓
Read XLSX File
    ↓
Records / Items
    ↓
Check Condition
    ↓
Send Email or Continue
```

Each stage has a different responsibility. A workflow works correctly only when the output of one stage is connected to the expected input of the next stage.

---

## 2. Email Trigger and Attachment

The workflow begins when a new email is received. If the email has an attachment, n8n receives the file as binary data.

Before building the workflow, check that:

- The email account credentials are connected.
- The trigger can access incoming emails.
- The test email includes an attachment.
- The attachment is the expected file type, such as `.xlsx`.

---

## 3. Binary Data and File Extraction

Binary data is the file form used by the workflow. It must be passed to a file-processing node before the rows and columns inside the file can be used.

```text
Email message
    ↓
Attachment stored as binary data
    ↓
Extract / read the file
    ↓
Structured workflow data
```

If the next node cannot find the attachment, verify the binary property name and confirm that the email really contained the file.

---

## 4. Reading Excel Data

An Excel file usually contains rows and columns. After it is read, n8n can treat every row as a separate item.

Example attendance data:

| Name | Email | Attendance |
|------|-------|------------|
| Ali | ali@example.com | Present |
| Ahmed | ahmed@example.com | Absent |
| Hassan | hassan@example.com | Present |

The output becomes multiple records that can be processed by the rest of the workflow.

---

## 5. Processing Records

The workflow should use the field names from the spreadsheet exactly as they appear. For example, `Name`, `Email`, and `Attendance` are different from `name`, `email`, and `attendance`.

For each item, the workflow can:

1. Read the relevant value.
2. Compare it with a condition.
3. Send it to the matching path.
4. Continue to the next item.

---

## 6. Conditions and Routing

An IF node is useful for a simple true/false decision.

```text
Attendance = Absent?
    ├── Yes → Send absence email
    └── No  → Do not send an email
```

A Switch node is helpful when more than two outcomes are needed, such as routing by `Student`, `Teacher`, or `Business Owner`.

---

## 7. Dynamic Email Values

The email action should take the recipient address and other details from the current record. This allows one workflow to send personalized messages without manually entering each recipient.

Example values used in an email:

```text
To: current record's Email
Subject: Attendance update
Message: Dear current record's Name, your attendance is marked Absent.
```

Always test with safe sample data before sending messages to real recipients.

---

## 8. Revision Checklist

Before activating the workflow, verify:

- The trigger receives the test email.
- The attachment appears as binary data.
- The Excel reader returns the expected number of records.
- Field names match the spreadsheet headers.
- The condition checks the correct value.
- The email node uses the current record's email address.
- Only the intended branch sends an email.

---

## Learning Outcome

After this lecture, I can review and test an attachment-based n8n workflow from the trigger through conditional email delivery.
