# Lecture 3 Notes — HTML Tables, Images & Videos

## 1. HTML Tables

Tables display data in rows and columns. They are useful for timetables, schedules, and structured information.

### Syntax

```html
<table border="1" cellpadding="10" cellspacing="8">
    <tr>
        <th>Name</th>
        <th>University</th>
    </tr>
    <tr>
        <td>Wajid Ali</td>
        <td>NUML</td>
    </tr>
</table>
```

### Explanation

- `<table>` creates the table container.
- `<tr>` defines a table row.
- `<th>` defines a header cell (bold and centered by default).
- `<td>` defines a standard data cell.
- `border="1"` adds a visible border.
- `cellpadding` adds space inside cells; `cellspacing` adds space between cells.

### Practical Example

See [table.html](table.html) — sections 1 through 7 cover basic tables, padding, spacing, colspan, rowspan, combined examples, and a class timetable.

### Important Points

- Use `<th>` for column/row headers and `<td>` for data.
- `colspan` makes a cell span multiple columns; `rowspan` spans multiple rows.

### Common Mistakes

- Confusing `colspan` and `rowspan` — colspan goes across columns (horizontal), rowspan goes down rows (vertical).
- Forgetting that the `colspan`/`rowspan` value must match the number of cells being merged.

---

## 2. Colspan and Rowspan

These attributes merge cells to create more complex table layouts.

### Syntax

```html
<!-- Colspan: header spans 3 columns -->
<tr>
    <th colspan="3">Student Information</th>
</tr>

<!-- Rowspan: cell spans 3 rows -->
<tr>
    <td rowspan="3">Morning</td>
    <td>Wajid Ali</td>
</tr>
```

### Explanation

- `colspan="3"` means one cell takes the space of three columns.
- `rowspan="3"` means one cell takes the space of three rows.
- When a cell spans multiple rows or columns, the following rows need fewer `<td>` or `<th>` elements.

### Practical Example

- **Colspan:** Section 4 in [table.html](table.html)
- **Rowspan:** Section 5 in [table.html](table.html)
- **Combined:** Sections 6 and 7 (schedule grid and class timetable)

### Important Points

- Plan the table layout before writing HTML — draw it on paper first for complex tables.
- The class timetable in section 7 combines both attributes in a realistic example.

### Common Mistakes

- Adding too many `<td>` elements in rows affected by rowspan/colspan, which breaks the table layout.
- Using colspan when rowspan is needed (or vice versa).

---

## 3. HTML Images

The `<img>` tag embeds images. It is a self-closing tag (no closing tag needed).

### Syntax

```html
<!-- Local image -->
<img src="images/profile.jpeg" alt="Profile Picture" width="250">

<!-- Online image -->
<img src="https://picsum.photos/500/300" alt="Random Image" width="500">

<!-- Clickable image -->
<a href="https://github.com" target="_blank">
    <img src="images/profile.jpeg" alt="GitHub" width="250">
</a>
```

### Explanation

- `src` specifies the image path (local file or URL).
- `alt` provides alternative text when the image cannot load — important for accessibility.
- `width` and `height` control display size.
- `title` shows a tooltip on hover.
- Wrapping `<img>` inside `<a>` makes the image clickable.

### Practical Example

See [image.html](image.html) — 10 sections cover local/online images, sizing, borders, titles, clickable images, multiple images, and missing-image alt fallback.

### Important Points

- Always include meaningful `alt` text.
- Local images use relative paths from the HTML file (e.g., `images/profile.jpeg`).
- If `src` is wrong, the browser shows the `alt` text instead (section 10).

### Common Mistakes

- Wrong file path or filename (including extension — `.jpeg` vs `.jpg`).
- Omitting `alt`, which hurts accessibility and provides no fallback when images fail to load.
- Using extremely large images without setting `width`/`height`, causing slow page loads.

---

## 4. HTML Videos

The `<video>` element embeds video content. Browsers use `<source>` tags to support different formats.

### Syntax

```html
<video width="500" controls>
    <source src="videos/sample.mp4" type="video/mp4">
    <source src="videos/sample.webm" type="video/webm">
    Your browser does not support the video tag.
</video>
```

### Explanation

- `<video>` is the container; `<source>` specifies each video file and its MIME type.
- `controls` shows play/pause, volume, and timeline controls.
- `autoplay` starts playback automatically (usually requires `muted` in modern browsers).
- `muted` silences audio; `loop` repeats the video.
- `poster` sets an image shown before playback starts.
- Text inside `<video>` is fallback content for browsers that do not support video.

### Practical Example

See [video.html](video.html) — sections cover basic video, autoplay/muted, loop, poster, sizing, multiple sources, and a combined example.

### Important Points

- Most browsers block autoplay with sound — use `autoplay muted` together.
- Multiple `<source>` tags let the browser pick the first supported format.
- The `type` attribute on `<source>` helps the browser choose efficiently.

### Common Mistakes

- Expecting autoplay to work without `muted`.
- Wrong video path or missing file in the `videos/` folder.

---

## 5. HTML Links

The `<a>` (anchor) tag creates hyperlinks that connect pages or jump to sections.

### Syntax

```html
<!-- Basic external link -->
<a href="https://www.google.com">Visit Google</a>

<!-- Open in new tab -->
<a href="https://github.com" target="_blank">Open GitHub</a>

<!-- Local page link -->
<a href="table.html">Go to HTML Tables Page</a>

<!-- Email link -->
<a href="mailto:wajid@example.com">Send Email</a>

<!-- Same-page anchor -->
<a href="#bottom">Jump to Bottom</a>
<h2 id="bottom">Bottom of Page</h2>
```

### Explanation

- `href` specifies the link destination (URL, file path, email, or `#id`).
- `target="_blank"` opens the link in a new browser tab.
- Relative paths like `table.html` link to other files in the same folder.
- `mailto:` opens the default email application.
- `href="#id"` jumps to an element on the same page with a matching `id`.
- `title` shows a tooltip when the user hovers over the link.

### Practical Example

See [links.html](links.html) — 8 sections cover basic links, external links, local pages, email links, title tooltips, same-page anchors, and simple navigation.

### Important Points

- Every link needs a valid `href` value.
- Use descriptive link text (e.g., "Visit GitHub") instead of vague text like "click here".
- Local links between lecture files use relative paths.

### Common Mistakes

- Forgetting `href` or leaving it empty (`href=""`).
- Using absolute paths when a simple relative path (e.g., `table.html`) would work.
- Mismatch between `href="#bottom"` and the target element's `id` — they must match exactly.

---

## 6. Important Points (Summary)

- Tables use `<table>`, `<tr>`, `<th>`, and `<td>` — plan colspan/rowspan carefully.
- Images require `src` and should always have descriptive `alt` text.
- Videos use `<video>` with `<source>` children and optional attributes like `controls`, `loop`, and `poster`.
- Links use `<a href="...">` for navigation between pages, external sites, and same-page sections.
- Assets (images, videos) are stored in subfolders relative to the HTML files.

## 7. Common Mistakes (Summary)

- Incorrect relative paths to images, videos, or other HTML files.
- Missing `alt` on images or fallback text inside `<video>`.
- Table layout breaks due to incorrect colspan/rowspan cell counts.
- Broken anchor links when the `id` on the target element does not match `href`.
