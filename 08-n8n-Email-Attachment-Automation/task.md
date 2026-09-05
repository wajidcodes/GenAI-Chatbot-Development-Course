# Assigned Task: Student Attendance Email Automation

The concepts learned in Lecture 8 (email attachments, reading XLSX data, loops, conditions, and the Switch node) are applied here to build the **Student Attendance Email Automation**.

## Attendance Data

The attendance file may contain information such as:

| Name       | Email                    | Attendance |
|------------|---------------------------|------------|
| Student 1  | student1@example.com     | Present    |
| Student 2  | student2@example.com     | Absent     |
| Student 3  | student3@example.com     | Present    |
| Student 4  | student4@example.com     | Absent     |

The workflow should identify students whose attendance is marked as **Absent**.

## Workflow Logic

```
Email
  ↓
Attendance XLSX Attachment
  ↓
Extract File
  ↓
Read Excel Data
  ↓
Process Students
  ↓
Check Attendance
  ↓
Is Attendance = Absent?
      │
      ├── Yes → Send Email
      │
      └── No  → Continue / No Email
```

## Steps to Build

1. Receive the email with the attendance XLSX attachment.
2. Extract the attachment from the email.
3. Read the Excel data into records.
4. Loop through each student record.
5. Check the `Attendance` field for each student.
6. If `Attendance = Absent`, send that student an email.
7. If `Attendance = Present`, skip and continue to the next record.