# CSS Revision Notes

### 1. What is the CSS Box Model, and why is it important in web design?

- The CSS Box Model defines how elements are structured and spaced, consisting of `content`, `padding`, `border`, and `margin`. It's crucial for accurately spacing and aligning elements on a page.

Example:

```css
div {
  width: 100px;
  padding: 10px;
  border: 5px solid black;
  margin: 20px;
}
```

### 2. Explain the difference between block and inline display properties.

- **Block** elements take up the full width available and begin on a new line (e.g., `<div>`, `<p>`). **Inline** elements take only as much width as needed and do not break the flow of text (e.g., `<span>`, `<a>`).

Example:

```css
div {
  display: block;
}
span {
  display: inline;
}
```

### 3. What is the purpose of the `box-sizing` property, and what does the `border-box` value do?

- `box-sizing` determines how the width and height of an element are calculated. `border-box` includes `padding` and `border` in the element's total width and height, making layout easier to manage.

Example:

```css
div {
  box-sizing: border-box;
}
```

### 4. What is CSS and how is it applied to HTML?

- CSS (Cascading Style Sheets) styles HTML elements by controlling layout, colors, fonts, etc. It can be applied via inline styles, `<style>` tags, or external stylesheets.

Example:

```html
<style>
  p {
    color: blue;
  }
</style>
```

### 5. Define the purpose of the box model in CSS.

- The box model defines how elements are sized and spaced, including `content`, `padding`, `border`, and `margin`, which are essential for layout design.

### 6. Explain the difference between padding and margin.

- **Padding** is the space between the content and the element's border, while **margin** is the space outside the border between the element and others.

Example:

```css
div {
  padding: 20px;
  margin: 10px;
}
```

### 7. What is the purpose of the `z-index` property, and how does it work with positioned elements?

- `z-index` controls the stack order of positioned elements. Higher `z-index` values appear in front of elements with lower values.

Example:

```css
div {
  position: absolute;
  z-index: 10;
}
```

### 8. How do you implement a hover effect in CSS, and why is it commonly used?

- Hover effects are implemented using the `:hover` pseudo-class and are commonly used for interactive elements like buttons.

Example:

```css
button:hover {
  background-color: green;
}
```

### 9. What is the difference between `visibility: hidden` and `display: none`, and how do they affect layout?

- `visibility: hidden` hides the element but keeps its space, while `display: none` removes it entirely from the layout.

Example:

```css
div.hidden {
  visibility: hidden;
}
div.none {
  display: none;
}
```

### 10. Describe the differences between `em`, `rem`, `px`, and `%` units in CSS and when each should be used.

- `px`: Absolute unit, fixed size.
- `em`: Relative to the font size of the element.
- `rem`: Relative to the root element's font size.
- `%`: Relative to the parent element.

Example:

```css
div {
  font-size: 1.5em; /* Relative to parent */
  width: 50%; /* Relative to parent */
}
```

### 11. Explain how CSS variables (custom properties) work and give an example of how they can be used.

- CSS variables are reusable values defined with `--` and accessed with `var()`. They help maintain consistent design.

Example:

```css
:root {
  --main-color: blue;
}
p {
  color: var(--main-color);
}
```

### 12. Explain the `overflow` property and the different values it can take.

- `overflow` controls what happens when content overflows an element's box. Values: `visible`, `hidden`, `scroll`, `auto`.

Example:

```css
div {
  overflow: hidden;
}
```

### 13. What is the `calc()` function in CSS, and when might you use it?

- `calc()` allows calculations within CSS, combining units like `px`, `%`, and `em`. Useful for dynamic sizing.

Example:

```css
div {
  width: calc(100% - 20px);
}
```

### 14. Describe how `justify-content` and `align-items` work in Flexbox and how they differ.

- `justify-content` aligns items horizontally along the main axis. `align-items` aligns items vertically along the cross axis.

Example:

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

### 15. Explain the difference between `inline`, `block`, and `inline-block` display values and give an example of when each might be used.

- `inline`: Elements flow in line (e.g., `<span>`).
- `block`: Elements take up full width (e.g., `<div>`).
- `inline-block`: Elements flow inline but respect width and height.

Example:

```css
span {
  display: inline-block;
  width: 100px;
}
```

### 16. How does position affect element layout in CSS, and which positioning type would you use to overlay an element?

- Positioning (`relative`, `absolute`, `fixed`, `sticky`) affects how an element is placed in the layout. Use `absolute` or `fixed` to overlay elements.

Example:

```css
.overlay {
  position: absolute;
  top: 0;
  left: 0;
}
```

### 17. Describe the role of pseudo-classes in CSS.

- Pseudo-classes target elements based on their state (e.g., `:hover`, `:focus`) or their position in the DOM (e.g., `:nth-child`).

Example:

```css
a:hover {
  color: red;
}
```

### 18. How do media queries work in responsive design?

- Media queries apply styles based on screen size or device type, enabling responsive design.

Example:

```css
@media (max-width: 600px) {
  body {
    background-color: lightblue;
  }
}
```

### 19. How would you create a flexbox layout?

- Use `display: flex` to enable Flexbox. Control alignment with properties like `justify-content` and `align-items`.

Example:

```css
.container {
  display: flex;
  justify-content: space-between;
}
```

### 20. Describe the role of pseudo-classes in CSS.

- Pseudo-classes style elements based on dynamic states like `:hover`, `:focus`, or positional ones like `:nth-child`.

Example:

```css
button:hover {
  background-color: yellow;
}
```

### 21. How do `min-width`, `max-width`, `min-height`, and `max-height` properties affect an element's size?

- These properties restrict the size of elements by defining minimum and maximum width/height limits.

Example:

```css
div {
  min-width: 100px;
  max-width: 500px;
}
```

### 22. Describe how the `transition` property works in CSS and provide an example of its use.

- The `transition` property enables smooth changes of properties over time (e.g., color, width).

Example:

```css
button {
  transition: background-color 0.5s ease;
}
```

### 23. Explain how to center an element horizontally and vertically in CSS using Flexbox.

- Use `justify-content: center` and `align-items: center` on a Flexbox container to center the content.

Example:

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
```

### 24. Describe the difference between `nth-child` and `nth-of-type` pseudo-classes in CSS.

- `nth-child` selects based on position among all siblings, while `nth-of-type` selects based on type.

Example:

```css
div:nth-child(2) { /* second child */ }
p:nth-of-type(2) { /* second paragraph */ }
```

### 25. Explain the purpose of the `filter` property in CSS and give an example of how it can be used.

- `filter` applies visual effects (blur, brightness, etc.) to elements.

Example:

```css
img {
  filter: grayscale(100%);
}
```

### 26. What is the `display: grid` property, and how does it differ from Flexbox?

- `display: grid` creates a two-dimensional grid layout, whereas Flexbox is one-dimensional (row or column).

Example:

```css
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}
```

### 27. How do the `gap`, `row-gap`, and `column-gap` properties work, and where are they used?

- These properties define the space between elements in CSS Grid and Flexbox layouts.

Example:

```css
.container {
  display: grid;
  gap: 10px;
}
```

### 28. Describe the differences between `opacity` and `rgba` for controlling transparency in CSS.

- `opacity` affects the entire element's transparency, while `rgba` applies transparency only to color values.

Example:

```css
div {
  opacity: 0.5; /* entire element is transparent */
  background-color: rgba(255, 0, 0, 0.5); /* only color is transparent */
}
```

### 29. Explain how media queries enable responsive design, and provide a basic example.

- Media queries apply different styles based on the device or screen size, making designs responsive.

Example:

```css
@media (max-width: 600px) {
  body {
    font-size: 14px;
  }
}
```

### 30. Describe the process and syntax of creating a CSS animation using `@keyframes`.

- Use `@keyframes` to define animations and `animation` to apply them to elements.

Example:

```css
@keyframes slide {
  from {
    transform: translateX(0);
  }
  to {
    transform: translateX(100px);
  }
}

div {
  animation: slide 2s ease;
}
```

### 31. How do `flex-direction` and the concept of main axis and cross axis work in Flexbox?

- `flex-direction` controls the direction of the main axis (row or column), while the cross axis is perpendicular to the main axis.

Example:

```css
.container {
  display: flex;
  flex-direction: column;
}
```

### 32. How would you create a responsive layout for a webpage header without using a CSS framework? Describe the key steps.

- Use media queries to adjust the layout at different screen sizes. Flexbox or Grid can create responsive navigation and content arrangement.

Example:

```css
header {
  display: flex;
  justify-content: space-between;
}

@media (max-width: 600px) {
  header {
    flex-direction: column;
  }
}
```

### 33. How would you implement grid layouts using CSS Grid?

- Use `display: grid` and define columns and rows with properties like `grid-template-columns`.

Example:

```css
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}
```

### 34. Explain the concept of CSS specificity and how it works.

- CSS specificity determines which styles take precedence. It's calculated based on the selectors (inline styles > IDs > classes > elements).

Example:

```css
/* More specific */
#id {
  color: red;
}
```

### 35. What are CSS preprocessors and why use them?

- CSS preprocessors (e.g., SASS, LESS) add programming features like variables and functions to CSS, simplifying complex stylesheets.

Example (SASS):

```scss
$primary-color: blue;

body {
  background-color: $primary-color;
}
```

### 36. What are CSS combinators, and how do they work? Provide examples.

- CSS combinators (e.g., descendant, child, adjacent sibling) define the relationship between elements.

Example:

```css
div > p { /* Direct child */
  color: red;
}

div + p { /* Adjacent sibling */
  color: blue;
}
```

---

## One-Line Definitions

* **CSS** → styles HTML elements by controlling layout, colors, and fonts.
* **Box Model** → defines element structure: content, padding, border, margin.
* **Block Display** → element takes full width and starts on a new line.
* **Inline Display** → element takes only needed width and stays in flow.
* **box-sizing: border-box** → includes padding and border in element's total size.
* **Padding** → space between content and border.
* **Margin** → space outside the border.
* **z-index** → controls the stack order of positioned elements.
* **display: none** → removes element entirely from layout.
* **visibility: hidden** → hides element but keeps its space.
* **Flexbox** → one-dimensional layout module for rows or columns.
* **Grid** → two-dimensional layout module for rows and columns.
* **Media Queries** → apply styles based on screen size for responsive design.
* **Pseudo-classes** → target elements based on state (e.g., `:hover`).
* **Specificity** → determines which CSS rules take precedence.
* **CSS Combinators** → define relationships between elements (e.g., child, adjacent).
