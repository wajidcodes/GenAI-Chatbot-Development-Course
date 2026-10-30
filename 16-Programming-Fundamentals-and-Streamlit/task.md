# Lecture 16 Self-Practice — Programming Fundamentals & Streamlit

Practice the programming concepts introduced in the lecture and create a small Streamlit application.

## Python Practice

1. Create variables for your name, age, and course name.
2. Print a sentence using an f-string.
3. Create one integer and one float, then perform addition and multiplication.
4. Use `type()` to check the type of each variable.
5. Write a function that accepts a name as a parameter and returns a greeting.
6. Explain the three parts of a function: input/parameters, processing, and an optional return value.
7. Identify `print()` as a built-in function that displays output without returning a useful value.

## Streamlit Practice

Create a file called `app.py` with a title and a text input:

```python
import streamlit as st

st.title("Student Introduction")
name = st.text_input("Enter your name")

if name:
    st.write(f"Welcome, {name}!")
```

Run the app with:

```bash
streamlit run app.py
```

## Completion Checklist

- [ ] Variables created and printed
- [ ] Strings and numbers used correctly
- [ ] A function written and called
- [ ] Function parameters, processing, and optional return values understood
- [ ] A simple Streamlit app started successfully
