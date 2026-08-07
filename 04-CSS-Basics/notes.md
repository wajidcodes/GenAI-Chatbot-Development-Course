# Lecture 4 Notes — CSS Basics

## 1. Types of CSS

CSS can be added to an HTML page in three ways. Each method has different use cases.

### Syntax

```html
<!-- 1. Inline CSS -->
<p style="color: red; font-size: 24px;">Styled with inline CSS</p>

<!-- 2. Internal CSS -->
<head>
    <style>
        .internal-style {
            color: green;
            font-size: 24px;
        }
    </style>
</head>

<!-- 3. External CSS -->
<head>
    <link rel="stylesheet" href="css/types.css">
</head>
```

```css
/* css/types.css — External CSS */
.external-style {
    color: blue;
    font-size: 24px;
    font-weight: bold;
}
```

### Explanation

- **Inline CSS** applies styles directly on an element using the `style` attribute. It affects only that one element.
- **Internal CSS** goes inside a `<style>` block in the `<head>`. It applies to the current page only.
- **External CSS** lives in a separate `.css` file linked with `<link>`. It can be reused across multiple pages.

### Practical Example

See [01-css-types.html](01-css-types.html) with [css/types.css](css/types.css).

### Important Points

- External CSS is preferred for larger projects because it keeps HTML and styling separate.
- Inline CSS is quick for small changes but becomes hard to maintain on big pages.

### Common Mistakes

- Forgetting the `<link rel="stylesheet" href="...">` tag when using external CSS.
- Wrong path in `href` (e.g., missing `css/` folder prefix).

---

## 2. CSS Selectors

Selectors tell the browser which HTML elements to style.

### Syntax

```css
/* Universal — all elements */
* {
    margin: 0;
    padding: 0;
}

/* Element — all divs */
div {
    background-color: red;
}

/* ID — one unique element */
#box1 {
    background-color: chocolate;
}

/* Class — multiple elements */
.box {
    background-color: aqua;
}
```

### Explanation

- `*` selects every element on the page (often used for resets).
- Element selectors target by tag name (e.g., `div`, `p`, `button`).
- ID selectors (`#name`) target one element with a unique `id`.
- Class selectors (`.name`) target all elements sharing a `class`.

### Practical Example

See [02-css-selectors.html](02-css-selectors.html) with [css/selectors.css](css/selectors.css) — six sections from universal through a practical container example.

### Important Points

- An ID should be unique on a page; classes can be reused on many elements.
- The same class can be applied to different element types (e.g., `.highlight` on `<p>`, `<div>`, and `<button>`).

### Common Mistakes

- Using `#` for classes or `.` for IDs — the symbols are not interchangeable.
- Reusing the same ID on multiple elements (IDs must be unique).

---

## 3. Text Styling

CSS properties control the appearance of text.

### Syntax

```css
.text-example {
    color: blue;
    font-size: 20px;
}

.bold-text {
    font-weight: 700;
}

.italic-text {
    font-style: italic;
}

.underline-text {
    text-decoration: underline;
    text-decoration-color: red;
    text-decoration-thickness: 3px;
}

.spaced-text {
    letter-spacing: 8px;
}

.text-center {
    text-align: center;
}
```

### Explanation

- `color` sets text color.
- `font-size` controls size; `font-weight` controls boldness; `font-style` controls italic.
- `text-align` positions text (left, center, right).
- `letter-spacing` adds space between characters.
- `text-decoration` and related properties control underlines and their appearance.

### Practical Example

Sections 1 and 2 in [03-text-and-box-styling.html](03-text-and-box-styling.html) with styles in [css/styling.css](css/styling.css).

### Important Points

- Text styling applies to block elements like `<p>` and inline content alike.
- `text-align: center` centers text within its container, not the container itself on the page.

### Common Mistakes

- Confusing `text-align: center` with centering a block element on the page (Flexbox or margins are needed for that).
- Using very large `letter-spacing` values that make text hard to read.

---

## 4. Borders and Border Radius

Borders outline elements; border-radius rounds corners.

### Syntax

```css
.solid-border {
    border: 3px solid black;
}

.dashed-border {
    border: 3px dashed black;
}

.rounded-box {
    border: 2px solid black;
    border-radius: 25px;
    background-color: aqua;
    padding: 20px;
}
```

### Explanation

- `border` shorthand combines width, style, and color (e.g., `3px solid black`).
- Border styles include `solid`, `dashed`, `dotted`, and `double`.
- `border-radius` rounds corners — higher values create more rounded shapes.

### Practical Example

Sections 3 and 4 in [03-text-and-box-styling.html](03-text-and-box-styling.html).

### Important Points

- Shorthand `border: width style color` is the most common way to set borders.
- `border-radius` works on any element with a visible background or border.

### Common Mistakes

- Forgetting the border style (e.g., writing `border: 3px black` without `solid`).
- Setting `border-radius` without a visible border or background, making the effect hard to see.

---

## 5. Box Model Basics

Elements are treated as boxes with dimensions, padding, and background.

### Syntax

```css
.padding-box {
    background-color: lightgray;
    width: 250px;
    padding: 20px;
    border: 2px solid black;
}

.box-red {
    width: 150px;
    height: 100px;
    background-color: red;
}
```

### Explanation

- `width` and `height` set the content area size.
- `padding` adds space inside the border, between content and border edge.
- `background-color` fills the element's background.
- `margin` (used in selectors.css) adds space outside the border.

### Practical Example

Sections 5 and 8 in [03-text-and-box-styling.html](03-text-and-box-styling.html).

### Important Points

- Padding affects the inside of the box; margin affects spacing outside.
- `box-sizing: border-box` (used in the navbar) includes padding and border in the element's total width.

### Common Mistakes

- Expecting `width` to include padding and border by default (default is `content-box`).
- Using fixed widths without considering how boxes behave on smaller screens.

---

## 6. Form and Button Styling

Inputs and buttons can be styled like any other HTML element.

### Syntax

```css
input {
    border: 2px solid red;
    border-radius: 15px;
    padding: 5px 20px;
    background-color: black;
    color: white;
}

input::placeholder {
    color: white;
}

button {
    background-color: #ff7d00;
    border: none;
    border-radius: 35px;
    color: white;
    padding: 7.5px 30px;
    cursor: pointer;
}
```

### Explanation

- Input fields can have custom borders, backgrounds, and rounded corners.
- `input::placeholder` styles the placeholder text separately.
- Buttons can use background color, padding, font properties, and `cursor: pointer` for a clickable feel.

### Practical Example

Sections 6 and 7 in [03-text-and-box-styling.html](03-text-and-box-styling.html).

### Important Points

- `cursor: pointer` changes the mouse icon on hover, signaling clickability.
- Form styling reuses the same properties learned for text and boxes.

### Common Mistakes

- Styling inputs but forgetting placeholder contrast (light placeholder on light background).
- Removing button borders without adding other visual cues (background color, padding).

---

## 7. Basic Flexbox Introduction

Flexbox arranges items inside a container along a flexible row or column. This lecture introduced it briefly through a navigation bar and a simple flex demo.

### Syntax

```css
#navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 20px;
}

.flex-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 15px;
}
```

### Explanation

- `display: flex` turns an element into a flex container; its direct children become flex items.
- `justify-content` aligns items along the main axis (horizontal by default).
- `align-items` aligns items along the cross axis (vertical by default).
- `gap` adds space between flex items.

### Practical Example

- Navigation bar at the top of [03-text-and-box-styling.html](03-text-and-box-styling.html)
- Section 9 (Basic Flexbox) in the same file

### Important Points

- Flexbox applies to the **container** — child elements become flex items automatically.
- This was a brief introduction; Lecture 5 covers Flexbox in more detail.

### Common Mistakes

- Applying flex properties to child items instead of the parent container.
- Forgetting `display: flex` on the container — other flex properties have no effect without it.

---

## 8. Important Points (Summary)

- CSS can be inline, internal, or external — external is best for reusable styles.
- Selectors (`*`, element, `#id`, `.class`) determine which elements receive styles.
- Text, border, box, and form styling use standard CSS properties applied via selectors.
- Flexbox was introduced for basic layout (navbar and centered boxes); deeper Flexbox practice is in Lecture 5.

## 9. Common Mistakes (Summary)

- Wrong file path in `<link href="css/...">`.
- Mixing up ID (`#`) and class (`.`) selector syntax.
- Overusing inline CSS instead of external stylesheets.
- Applying flex properties without `display: flex` on the parent.
