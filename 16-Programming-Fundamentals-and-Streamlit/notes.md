# Lecture 16 — Programming Fundamentals & Streamlit

## 1. Programming Fundamentals

Programming is the process of giving a computer instructions to perform a task. Python uses readable syntax and is widely used in automation, data work, web applications, and AI projects.

---

## 2. Variables

A variable stores a value so it can be used later in the program.

```python
name = "Wajid"
age = 21
```

In this example, `name` stores text and `age` stores a number.

Variable names should be meaningful and should not begin with a number.

---

## 3. Data Types

Different values have different data types.

| Type | Example | Purpose |
|------|---------|---------|
| `str` | `"Hello"` | Text or strings |
| `int` | `21` | Whole numbers |
| `float` | `10.5` | Decimal numbers |
| `bool` | `True` or `False` | Yes/no values |

Use `type()` to check the type of a value:

```python
price = 250.5
print(type(price))
```

---

## 4. Strings

A string is text written inside quotation marks.

```python
course = "GenAI and Chatbot Development"
```

Strings can be joined together:

```python
first_name = "Wajid"
message = "Hello, " + first_name
print(message)
```

An f-string is another convenient way to insert a variable into text:

```python
age = 21
print(f"I am {age} years old")
```

---

## 5. Numbers

Python supports whole numbers (`int`) and decimal numbers (`float`).

```python
students = 30
fee = 1500.50
total = students * fee
print(total)
```

Common mathematical operators are:

```text
+  addition
-  subtraction
*  multiplication
/  division
%  remainder
** power
```

---

## 6. Functions

A function is a reusable block of code that performs a specific task.

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Wajid")
print(message)
```

In this example:

- `greet` is the function name.
- `name` is a parameter.
- `return` sends a result back to the code that called the function.

Functions help keep programs organized and reduce repeated code.

---

## 7. General Introduction to Functions

The instructor explained functions with a wedding example:

1. **What we bring to the wedding** is like a function's **parameters** or input.
2. **What we do at the wedding**, such as eating lunch or dinner, is like the function's **processing**.
3. **What we receive from the wedding** is like a function's **return value**.

In some cases, a wedding host may give guests a gift, but this is optional. In the same way, a function can return a value, but it does not have to.

```text
Parameters / input
        ↓
Function processing
        ↓
Optional return value
```

For example, `print()` is a function that performs an action by displaying output, but it does not return a useful value for later use.

The lecture introduced the general idea of built-in functions. It did not cover a detailed list of individual built-in functions.

---

## 8. Introduction to Streamlit

Streamlit is a Python framework for creating interactive web apps with Python. It is useful for prototypes, data dashboards, AI demonstrations, and small tools.

A basic Streamlit application can look like this:

```python
import streamlit as st

st.title("My First Streamlit App")
name = st.text_input("Enter your name")

if name:
    st.write(f"Hello, {name}!")
```

The app can be run from a terminal with:

```bash
streamlit run app.py
```

Useful Streamlit functions include:

- `st.title()` for a page title
- `st.write()` for text or data
- `st.text_input()` for a text field
- `st.number_input()` for numeric input
- `st.button()` for a button
- `st.selectbox()` for a dropdown

---

## Learning Outcome

After this lecture, I understand the basic building blocks of Python, the general idea of function input, processing, and optional return values, and how Streamlit can be used to create a small interactive interface with Python code.
