# Lecture 5 Notes — CSS Flexbox

## 1. What Is Flexbox?

Flexbox (Flexible Box Layout) is a CSS layout system for arranging elements inside a container. It simplifies alignment, spacing, and direction control compared to older layout methods.

### Concept

- **Flex container** — the parent element with `display: flex`.
- **Flex items** — the direct children inside the container.
- **Main axis** — the primary direction items flow (horizontal by default).
- **Cross axis** — perpendicular to the main axis.

### Practical Example

The red `.container` in [01-flexbox-basics.html](01-flexbox-basics.html) is a flex container; the blue, yellow, and green `.box` elements are flex items.

### Important Points

- Flexbox properties on the container control how all child items are laid out.
- Lecture 4 introduced Flexbox briefly; this lecture practices it in dedicated examples.

### Common Mistakes

- Trying to use Flexbox on elements that are not direct parent-child relationships.
- Expecting Flexbox to work without setting `display: flex` on the container.

---

## 2. display: flex

This property turns an element into a flex container.

### Syntax

```css
.container {
    display: flex;
    padding: 12px;
    gap: 15px;
}
```

### Explanation

- Child elements automatically become flex items and arrange in a row by default.
- The container's children sit side by side instead of stacking vertically.

### Practical Example

The `.container` and `.content-container` classes in [css/flexbox-basics.css](css/flexbox-basics.css).

### Important Points

- Only direct children of the flex container become flex items.
- Nested elements inside flex items are not flex items unless their parent also has `display: flex`.

### Common Mistakes

- Setting `display: flex` on a child instead of the parent wrapper.
- Forgetting that flex items default to a horizontal row layout.

---

## 3. justify-content

Controls alignment along the **main axis** (horizontal when direction is row).

### Syntax

```css
.justify-center {
    justify-content: center;
}

.justify-start {
    justify-content: flex-start;
}

.justify-end {
    justify-content: flex-end;
}
```

### Explanation

- `flex-start` — items align to the start of the container (left in a row).
- `center` — items are centered along the main axis.
- `flex-end` — items align to the end (right in a row).

### Practical Example

Section 1 in [02-flexbox-properties.html](02-flexbox-properties.html) shows center, flex-start, and flex-end side by side.

### Important Points

- `justify-content` affects spacing along the main axis only.
- When `flex-direction` is `column`, the main axis becomes vertical, so `justify-content` controls vertical alignment instead.

### Common Mistakes

- Confusing `justify-content` (main axis) with `align-items` (cross axis).
- Expecting `justify-content: center` to center the container itself on the page — it only centers items inside the container.

---

## 4. align-items

Controls alignment along the **cross axis** (vertical when direction is row).

### Syntax

```css
.align-center {
    align-items: center;
}
```

### Explanation

- `align-items: center` vertically centers flex items within the container (when direction is row).
- Useful when the container is taller than its items.

### Practical Example

Section 2 in [02-flexbox-properties.html](02-flexbox-properties.html).

### Important Points

- Works on the flex container, not on individual items.
- Combined with `justify-content: center`, it centers items both horizontally and vertically.

### Common Mistakes

- Applying `align-items` to flex items instead of the container.
- Not giving the container enough height to see vertical alignment effects.

---

## 5. flex-direction

Changes the direction flex items flow.

### Syntax

```css
.direction-row {
    flex-direction: row;
}

.direction-row-reverse {
    flex-direction: row-reverse;
}

.direction-column {
    flex-direction: column;
}
```

### Explanation

- `row` — items flow left to right (default).
- `row-reverse` — items flow right to left.
- `column` — items stack vertically, top to bottom.

### Practical Example

Section 3 in [02-flexbox-properties.html](02-flexbox-properties.html) demonstrates all three values present in the practice code.

### Important Points

- Changing direction swaps which axis is "main" and which is "cross".
- `column-reverse` was not included in the practice files for this lecture.

### Common Mistakes

- Forgetting that `flex-direction: column` makes `justify-content` control vertical spacing instead of horizontal.
- Assuming items always flow horizontally — direction must be checked first.

---

## 6. gap

Adds consistent spacing between flex items.

### Syntax

```css
.gap-example {
    gap: 20px;
}
```

### Explanation

- `gap` sets space between adjacent flex items (both row and column gap in one value).
- Cleaner than using margins on each item.

### Practical Example

Section 4 in [02-flexbox-properties.html](02-flexbox-properties.html) and the `.container` in [css/flexbox-basics.css](css/flexbox-basics.css) (`gap: 15px`).

### Important Points

- `gap` applies between items, not on the outer edges of the container.
- Works well with both row and column directions.

### Common Mistakes

- Using large margins on every item when `gap` on the container is simpler.
- Confusing `gap` with `padding` (padding is inside the container edges; gap is between items).

---

## 7. flex-wrap

Controls whether flex items stay on one line or wrap to new lines.

### Syntax

```css
.wrap-example {
    width: 300px;
    flex-wrap: wrap;
    gap: 10px;
}
```

### Explanation

- By default, flex items shrink to fit on one line (`nowrap`).
- `flex-wrap: wrap` allows items to move to the next line when there is not enough space.

### Practical Example

Section 5 in [02-flexbox-properties.html](02-flexbox-properties.html) — six items in a 300px-wide container wrap to multiple rows.

### Important Points

- Wrapping requires the container to be narrower than the total width of all items.
- `gap` still applies between wrapped rows.

### Common Mistakes

- Setting `flex-wrap: wrap` but giving the container unlimited width, so items never wrap.
- Not reducing container width to see the wrap effect.

---

## 8. Centering and Combined Examples

Multiple Flexbox properties are often used together to create centered, spaced layouts.

### Syntax

```css
.combined-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 15px;
    flex-wrap: wrap;
    padding: 20px;
    min-height: 300px;
}
```

### Explanation

- Combining `justify-content: center` and `align-items: center` centers items in both directions.
- Adding `gap`, `flex-wrap`, and `padding` creates a complete, responsive-feeling layout.

### Practical Example

- Section 6 (Combined Flexbox Example) in [02-flexbox-properties.html](02-flexbox-properties.html)
- Section 2 (Flexbox with Content) in [01-flexbox-basics.html](01-flexbox-basics.html) — flex items containing paragraph text

### Important Points

- Flex items in the basics file also use `display: flex` with `justify-content` and `align-items` to center text inside each box.
- The combined example brings together properties practiced individually in earlier sections.

### Common Mistakes

- Using only one alignment property when both axes need centering.
- Omitting `min-height` on the container, making vertical centering less visible.

---

## 9. Important Points (Summary)

- Flexbox is controlled mainly through **container** properties: `display: flex`, `justify-content`, `align-items`, `flex-direction`, `gap`, and `flex-wrap`.
- The practice files cover `row`, `row-reverse`, and `column` for direction, and `wrap` for wrapping.
- Flex item properties (`flex-grow`, `flex-shrink`, `order`, etc.) were not part of the practice files for this lecture.

## 10. Common Mistakes (Summary)

- Forgetting `display: flex` on the parent container.
- Mixing up main axis (`justify-content`) and cross axis (`align-items`).
- Applying flex container properties to child items instead of the parent.
- Not adjusting container width or height to observe alignment and wrap behavior.
