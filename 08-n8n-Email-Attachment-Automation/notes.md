# Lecture 8 — n8n Email Attachment & Data Automation

## 1. Introduction

In this lecture, we moved from basic n8n automation to a more practical automation: working with emails that contain file attachments, and learning how to retrieve, extract, and process the data inside those files.

We also learn how to use loops and conditional logic to process different records and send emails according to specific conditions.

The main idea is to create an automation that can:

- Receive an email.
- Access an attached file.
- Extract data from the file.
- Process multiple records.
- Apply conditions to the records.
- Route records according to their values.
- Send automated emails.

---

## 2. Topics Covered

- Receiving emails in n8n
- Working with email attachments
- Extracting files from emails
- Binary data
- Reading data from XLSX/Excel files
- Processing records from a file
- Looping through multiple records
- Using conditions
- Using the Switch node
- Sending automated emails
- Sending emails based on processed data

---

## 3. Email with Attachment

An email can contain additional files called attachments. Examples include:

- `.xlsx`
- `.csv`
- `.pdf`
- `.jpg`
- `.png`
- Other supported file formats

In this lecture, the important case is an **Excel/XLSX attachment**.

The basic flow is:

```
Email
  ↓
Attachment
  ↓
Extract Attachment
  ↓
Read File
  ↓
Process Data
```

---

## 4. Binary Data

When a file is received by an n8n workflow, the file is handled as **binary data**.

```
Email
  ↓
Binary Attachment
  ↓
File Processing Node
  ↓
Structured Data
```

The binary file must be processed before the information inside it can be used as normal workflow data.

---

## 5. Reading an XLSX File

An XLSX file contains structured data arranged into rows and columns.

Example:

| Name            | Email                    | Profession       |
|-----------------|---------------------------|-------------------|
| Ali             | ali@example.com          | Student           |
| Ahmed           | ahmed@example.com        | Student           |
| Teacher         | teacher@example.com      | Teacher           |
| Business Owner  | owner@example.com        | Business Owner    |

After the file is processed, each row can be treated as a separate item/record.

Conceptually:

```
Excel File
    ↓
Read Excel Data
    ↓
Record 1
Record 2
Record 3
Record 4
```

---

## 6. Processing Multiple Records

When a file contains multiple rows, the workflow needs to process those records individually.

```
Record 1 → Ali
Record 2 → Ahmed
Record 3 → Teacher
Record 4 → Business Owner
```

The workflow can process the records one by one and perform an action for each.

---

## 7. Loop

A loop is used when the same operation needs to be performed for multiple records — for example, if an Excel file contains multiple people:

```
Person 1
Person 2
Person 3
Person 4
Person 5
```

Conceptually:

```
Excel Data
    ↓
Multiple Records
    ↓
Loop
    ↓
Process Each Record
```

Instead of manually creating a separate workflow for every person, the workflow can process the records automatically.

**Example:**

Suppose an Excel file contains: `Ali`, `Ahmed`, `Hassan`, `Usman`.

The workflow processes each one the same way:

```
Ali        Ahmed      Hassan     Usman
 ↓           ↓          ↓          ↓
Check      Check      Check      Check
Data       Data       Data       Data
 ↓           ↓          ↓          ↓
Perform    Perform    Perform    Perform
Action     Action     Action     Action
```

---

## 8. Conditions

Conditions allow a workflow to make decisions based on data, for example:

- `Profession = Student`
- `Attendance = Absent`

A condition determines which action should be performed.

Basic concept:

```
Data
 ↓
Condition
 ↓
True  → Perform Action
False → Different Action
```

---

## 9. Switch Node

The Switch node is used to route data according to different conditions or values — useful when there are multiple possible values or paths.

For example, if the `Profession` field can be `Student`, `Teacher`, or `Business Owner`:

```
                    Profession
                        ↓
                     Switch
                  /     |      \
                 ↓      ↓       ↓
            Student  Teacher  Business Owner
                ↓      ↓       ↓
              Email  Email    Email
```

This is more suitable than creating many separate workflows, and it allows different records to follow different paths.

---

## 10. Classroom Example: Routing by Profession

For the classroom demonstration, a list of people was prepared with:

- Name
- Email
- Profession

The example included different types of people: **Students**, **Teacher**, and **Business owners**.

The workflow uses the profession value to determine which path each record should follow:

```
Input Record
     ↓
Read Profession
     ↓
Switch
     ├── Student
     ├── Teacher
     └── Business Owner
```

---

## 11. Sending Emails Automatically

After the workflow determines the correct path, an email is sent automatically:

```
Student          Teacher          Business Owner
   ↓                ↓                    ↓
Student Email   Teacher Email     Business Owner Email
```

The recipient's email address is obtained from the data being processed.

---

## 12. Using Data from Previous Nodes

n8n allows information from previous nodes to be used in later nodes. For example, if an Excel record contains:

```
Name: Ali
Email: ali@example.com
Profession: Student
```

The workflow can use these values when sending the email:

```
Excel Data
    ↓
Name, Email, Profession
    ↓
Switch
    ↓
Email Node
```

The email node uses the recipient's email address directly from the processed record.

---

## 13. Complete Classroom Example

The overall workflow demonstrated in class can be represented as:

```
Email
  ↓
Receive Attachment
  ↓
Extract XLSX File
  ↓
Read Excel Data
  ↓
Process Records
  ↓
Loop Through Records
  ↓
Switch Based on Profession
       │
       ├── Student
       │     ↓
       │   Send Email
       │
       ├── Teacher
       │     ↓
       │   Send Email
       │
       └── Business Owner
             ↓
           Send Email
```

---

## 14. Why Automation Is Useful

Without automation, a person would have to:

1. Open the email.
2. Download the attachment.
3. Open the Excel file.
4. Find absent students.
5. Copy each student's email address.
6. Write an email.
7. Send the email.
8. Repeat the process for every absent student.

With n8n, these steps can be automated:

```
Receive
   ↓
Read
   ↓
Process
   ↓
Decide
   ↓
Send
```

---

## 15. Important n8n Concepts

| Concept | Description |
|---|---|
| **Email** | Used to receive or send email messages. |
| **Attachment** | A file included with an email. |
| **Binary Data** | The format in which files are carried through an n8n workflow. |
| **File Processing** | Converting or extracting information from an attached file. |
| **XLSX** | An Excel spreadsheet format that can contain structured rows and columns. |
| **Loop** | Used to process multiple records. |
| **Condition** | Used to make decisions based on data. |
| **Switch** | Used to route data through different paths based on values. |
| **Email Automation** | Sending emails automatically based on workflow data and conditions. |

---

## 16. General Workflow Pattern

The concepts learned in this lecture can be generalized into:

```
Trigger
   ↓
Receive Data
   ↓
Extract / Read Data
   ↓
Process Data
   ↓
Loop Through Records
   ↓
Apply Logic
   ↓
Choose Path
   ↓
Perform Action
```

---

## 17. Key Takeaways

After this lecture, we should understand how to:

1. Receive an email through n8n.
2. Work with email attachments.
3. Process an XLSX file.
4. Extract structured information from the file.
5. Work with multiple records.
6. Use loops for repeated processing.
7. Use conditions to make decisions.
8. Use the Switch node for multiple paths.
9. Send automated emails.
10. Build workflows that process data and perform actions automatically.