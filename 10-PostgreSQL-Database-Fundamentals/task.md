# Assigned Task: Create a To-Do List in Neon PostgreSQL

Create a Neon PostgreSQL database and use it to store To-Do list tasks. The task is focused on designing a simple table and practicing the main SQL commands covered in Lecture 10.

## 1. Create a Neon Project

1. Create or sign in to a Neon account.
2. Create a PostgreSQL project.
3. Open the Neon SQL Editor.
4. Do not share or commit the database connection string or password.

## 2. Create the To-Do Table

Run the following SQL in the Neon SQL Editor:

```sql
CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 3. Add Sample Tasks

```sql
INSERT INTO todos (title, completed)
VALUES
    ('Learn PostgreSQL basics', FALSE),
    ('Create a Neon database', TRUE),
    ('Build a To-Do list', FALSE);
```

## 4. View the Tasks

```sql
SELECT * FROM todos;
```

## 5. Practice Deleting Rows

Delete one task by its ID:

```sql
DELETE FROM todos
WHERE id = 1;
```

To remove all task rows while keeping the table:

```sql
DELETE FROM todos;
```

## 6. Practice Dropping the Table

Only after finishing the practice, remove the table if required:

```sql
DROP TABLE todos;
```

## Expected Result

You should be able to create the `todos` table, insert tasks, view them with `SELECT`, delete rows safely with `DELETE`, and explain that `DROP TABLE` removes the entire table.

## Completion Checklist

- [ ] Neon PostgreSQL project created
- [ ] `todos` table created
- [ ] Sample tasks inserted
- [ ] Tasks viewed with `SELECT`
- [ ] A row deleted using `DELETE ... WHERE`
- [ ] Difference between deleting rows and dropping a table understood
