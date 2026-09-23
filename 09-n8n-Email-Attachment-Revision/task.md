# Assigned Task: Revise the Student Attendance Email Automation

Rebuild or review the attendance-email workflow from Lecture 8. The aim is to confirm that the workflow correctly reads an XLSX attachment and sends an email only to students marked as absent.

## Sample Attendance Data

| Name | Email | Attendance |
|------|-------|------------|
| Student 1 | student1@example.com | Present |
| Student 2 | student2@example.com | Absent |
| Student 3 | student3@example.com | Present |
| Student 4 | student4@example.com | Absent |

## Required Workflow

```text
Email Trigger
    ↓
Attendance XLSX Attachment
    ↓
Extract Attachment
    ↓
Read Excel Data
    ↓
Check Attendance for Each Student
    ↓
Attendance = Absent?
    ├── Yes → Send absence email
    └── No  → Continue without sending an email
```

## Steps

1. Send a test email with an attendance XLSX file attached.
2. Confirm that the workflow receives the attachment.
3. Read the spreadsheet so each student becomes a separate record.
4. Check the `Attendance` value for every student.
5. Send an email only when the value is `Absent`.
6. Test both the present and absent paths.
7. Review the execution data to confirm that only absent students received an email.

## Expected Result

The workflow processes every row in the attendance sheet. Students marked `Absent` follow the email path, while students marked `Present` do not receive an absence email.
