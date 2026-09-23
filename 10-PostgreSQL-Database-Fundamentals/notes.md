# Lecture 10 — PostgreSQL Database Fundamentals

## 1. What Is a Database?

A database is an organized collection of data that can be stored, searched, updated, and managed efficiently.

Applications use databases to keep information that must remain available after the application is closed, such as user accounts, messages, orders, tasks, and attendance records.

---

## 2. Why Do We Need Databases?

Databases help applications:

- Store large amounts of data in an organized way.
- Find specific information quickly.
- Add, update, and delete data safely.
- Reduce duplicate data.
- Allow multiple users or services to work with the same information.
- Keep important data available between application sessions.

For a To-Do list, a database allows tasks to remain saved instead of disappearing when the application restarts.

---

## 3. Types of Databases

### Relational Databases (SQL)

Relational databases organize data in tables with rows and columns. Tables can be related using keys.

Examples: PostgreSQL, MySQL, SQLite, Microsoft SQL Server.

### Non-Relational Databases (NoSQL)

NoSQL databases can store data in structures such as documents, key-value pairs, graphs, or wide columns.

Examples: MongoDB, Firebase Firestore, Redis, Neo4j.

### Cloud Databases

Cloud databases are hosted online and managed through a cloud service. Neon provides hosted PostgreSQL databases.

---

## 4. PostgreSQL

PostgreSQL is a powerful open-source relational database management system. It uses SQL (Structured Query Language) to define tables and work with data.

Important terms:

- **Database:** A collection of related tables.
- **Table:** A structure that stores related data.
- **Column:** A named property of the data, such as `title` or `completed`.
- **Row:** One stored record in a table.
- **Primary key:** A value that uniquely identifies each row.

---

## 5. Basic SQL Commands

### Create a Table

```sql
CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    completed BOOLEAN DEFAULT FALSE
);
```

This creates a `todos` table with a unique `id`, a required task title, and a completion status.

### Insert Rows

```sql
INSERT INTO todos (title, completed)
VALUES
    ('Complete PostgreSQL practice', FALSE),
    ('Build the To-Do list', FALSE);
```

`INSERT INTO` adds new rows to a table.

### View Rows

```sql
SELECT * FROM todos;
```

`SELECT` reads data from a table.

### Delete a Specific Row

```sql
DELETE FROM todos
WHERE id = 1;
```

`DELETE FROM` removes rows. The `WHERE` clause is important because it limits which rows are deleted.

### Delete All Rows

```sql
DELETE FROM todos;
```

This removes all rows but keeps the table structure.

### Drop a Table

```sql
DROP TABLE todos;
```

`DROP TABLE` removes the table itself, including its structure and data. Use it carefully.

---

## 6. Neon PostgreSQL

Neon is a cloud platform for PostgreSQL databases. It provides a PostgreSQL database that can be created and accessed online.

General workflow:

```text
Create Neon project
    ↓
Open the SQL editor
    ↓
Create a table
    ↓
Insert test data
    ↓
Query, update, and delete data
```

Keep database connection strings and passwords private. They should not be committed to a public repository.

---

## 7. To-Do List Data Model

A basic To-Do list needs one table where each row represents one task.

| Column | Purpose |
|--------|---------|
| `id` | Unique task identifier |
| `title` | Description of the task |
| `completed` | Whether the task is finished |
| `created_at` | Date and time the task was created |

Example table:

```sql
CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Learning Outcome

After this lecture, I understand why databases are used, how relational tables store data, and how to use basic SQL commands with PostgreSQL and Neon.
