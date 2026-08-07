# Lecture 2 Notes — HTML Fundamentals

## 1. HTML Document Structure

Every HTML page follows a basic skeleton. The browser uses this structure to understand the page content and metadata.

### Syntax

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
</head>
<body>
    <!-- Page content goes here -->
</body>
</html>
```

### Explanation

- `<!DOCTYPE html>` tells the browser the document is HTML5.
- `<html>` is the root element that wraps the entire page.
- `<head>` holds metadata (title, character set, viewport) that is not displayed directly.
- `<body>` contains everything visible on the page.

### Practical Example

See the full document structure at the top of [index.html](index.html).

### Important Points

- Every valid HTML page should include `<!DOCTYPE html>`, `<html>`, `<head>`, and `<body>`.
- The `<title>` appears in the browser tab, not on the page itself.

### Common Mistakes

- Forgetting `<!DOCTYPE html>`, which can cause inconsistent rendering in some browsers.
- Placing visible content inside `<head>` instead of `<body>`.

---

## 2. Headings and Paragraphs

Headings create a hierarchy of titles. Paragraphs hold blocks of text.

### Syntax

```html
<h1>Main Heading</h1>
<h2>Subheading</h2>
<p>This is a paragraph of text.</p>
<p>My Name is Wajid Ali.<br>I am learning HTML.</p>
```

### Explanation

- `<h1>` is the largest/most important heading; `<h6>` is the smallest.
- `<p>` wraps a paragraph of text.
- `<br>` inserts a line break within a paragraph without starting a new paragraph.

### Practical Example

The **Headings**, **Paragraph**, and **Line Break** sections in [index.html](index.html).

### Important Points

- Use headings in order (do not skip from `<h1>` to `<h4>` without reason).
- Only one `<h1>` per page is a common convention for main page title.

### Common Mistakes

- Using headings only for font size — they carry semantic meaning for structure and accessibility.
- Using multiple `<br>` tags for spacing instead of proper block elements or CSS.

---

## 3. Text Formatting Tags

HTML provides several tags to change how text appears or to indicate meaning.

### Syntax

```html
<p><b>Bold Text</b></p>
<p><strong>Strong (important) Text</strong></p>
<p><i>Italic Text</i></p>
<p><em>Emphasized Text</em></p>
<p><u>Underlined Text</u></p>
<p><mark>Highlighted Text</mark></p>
<p><small>Small Text</small></p>
<p><del>Deleted Text</del></p>
<p><ins>Inserted Text</ins></p>
```

### Explanation

- `<b>` and `<strong>` both make text bold; `<strong>` suggests stronger importance.
- `<i>` and `<em>` both make text italic; `<em>` suggests emphasis.
- `<mark>` highlights text, `<del>` shows deleted text, and `<ins>` shows inserted text.

### Practical Example

The **Text Formatting** section in [index.html](index.html).

### Important Points

- Prefer `<strong>` and `<em>` when meaning matters; `<b>` and `<i>` are mainly visual.
- Formatting tags can be nested inside paragraphs.

### Common Mistakes

- Confusing `<b>` with `<strong>` — they look similar but `<strong>` has semantic meaning.
- Overusing formatting tags, making the page hard to read.

---

## 4. Superscript, Subscript, and Span

These tags handle special text positioning and inline styling.

### Syntax

```html
<p>H<sub>2</sub>O</p>
<p>x<sup>2</sup> + y<sup>2</sup></p>
<p>My favorite color is <span style="color:blue;">Blue</span>.</p>
```

### Explanation

- `<sub>` lowers text (e.g., chemical formulas).
- `<sup>` raises text (e.g., exponents).
- `<span>` is an inline container used to style part of a line without breaking the flow.

### Practical Example

The **Superscript and Subscript** and **Span Tag** sections in [index.html](index.html).

### Important Points

- `<span>` is inline — it does not start on a new line.
- Inline `style` attributes were used here for color; CSS is the preferred approach for larger projects.

### Common Mistakes

- Using `<span>` for block-level layout — use `<div>` for that instead.

---

## 5. Div Tag

The `<div>` element is a block-level container used to group content.

### Syntax

```html
<div style="border:2px solid black; padding:15px;">
    <h3>Student Information</h3>
    <p>Name: Wajid Ali</p>
    <p>University: NUML</p>
</div>
```

### Explanation

- `<div>` takes the full width available and starts on a new line.
- It is commonly used to group related content for layout or styling.

### Practical Example

The **Div Tag** section in [index.html](index.html).

### Important Points

- `<div>` has no semantic meaning by itself — it is a generic container.
- Block elements (`<div>`, `<p>`, headings) stack vertically; inline elements (`<span>`) sit in a line.

### Common Mistakes

- Nesting block elements incorrectly (e.g., putting a `<div>` inside a `<span>`).
- Using too many nested `<div>` elements without clear purpose.

---

## 6. Lists

HTML supports ordered (numbered) and unordered (bulleted) lists.

### Syntax

```html
<ol>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ol>

<ul>
    <li>Computer</li>
    <li>Keyboard</li>
    <li>Mouse</li>
</ul>
```

### Explanation

- `<ol>` creates a numbered list; `<ul>` creates a bulleted list.
- Each item uses `<li>`.
- Lists can be nested — an `<ol>` can contain a `<ul>` inside an `<li>`.

### Practical Example

The **Ordered List**, **Unordered List**, and **Nested List** sections in [index.html](index.html).

### Important Points

- List items must be direct children of `<ol>` or `<ul>`.
- Nested lists go inside an `<li>`, not directly inside another list tag.

### Common Mistakes

- Forgetting to wrap items in `<li>` tags.
- Placing `<ul>` or `<ol>` directly inside another list without wrapping in `<li>`.

---

## 7. HTML Comments and Horizontal Rules

Comments help organize code; horizontal rules create visual separators.

### Syntax

```html
<!-- This is a comment — not visible in the browser -->

<hr>
```

### Explanation

- Comments are ignored by the browser and useful for labeling sections in source code.
- `<hr>` draws a horizontal line across the page.

### Practical Example

Throughout [index.html](index.html), comments label each section and `<hr>` separates them.

### Important Points

- Comments do not appear on the rendered page.
- `<hr>` is a self-contained separator element.

### Common Mistakes

- Nesting comments incorrectly (`<!-- <!-- --> -->` breaks the comment).
- Using `<hr>` for layout spacing — CSS margins/padding are better for spacing.
