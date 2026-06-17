# HTML Revision Notes

### 1. What is the purpose of `<!DOCTYPE html>` in an HTML document?

- The `<!DOCTYPE html>` declaration defines the document type and version of HTML. It helps the browser to render the page correctly by triggering standards mode. Without it, the browser may enter quirks mode, rendering pages inconsistently.

Example:

```html
<!DOCTYPE html>
<html>
</html>
```

### 2. Define a markup language. How does it differ from a programming language?

- A markup language, like HTML, uses tags to structure and present content. Unlike programming languages, it doesn't handle logic or dynamic behaviors but is focused on presentation and structure.

Example:

```html
<p>This is a paragraph.</p>
```

### 3. What is the difference between HTML tags and attributes?

- Tags define elements, while attributes provide additional information about elements. Attributes are written inside the opening tag.

Example:

```html
<a href="https://example.com">Link</a>
```

### 4. Define the purpose of the `<title>` tag in HTML.

- The `<title>` tag sets the title of the web page, which appears in the browser tab and is used by search engines.

Example:

```html
<title>My Website</title>
```

### 5. What is a `<div>` element and when is it used?

- The `<div>` element is a block-level container used to group content for styling or layout purposes.

Example:

```html
<div class="container">
  <p>Some content here</p>
</div>
```

### 6. What is HTML and why is it important?

- HTML (HyperText Markup Language) is the standard markup language for creating web pages. It's essential for structuring web content.

Example:

```html
<h1>HTML Basics</h1>
<p>This is important because it structures web pages.</p>
```

### 7. How do HTML comments work, and why are they useful in development?

- HTML comments are used to add notes or explanations that are not visible on the web page.

Example:

```html
<!-- This is a comment -->
<p>Visible text</p>
```

### 8. What is the function of the `<code>`, `<kbd>`, and `<pre>` tags, and when would you use each?

- `<code>`: Displays inline code.
- `<kbd>`: Represents user input from a keyboard.
- `<pre>`: Displays preformatted text.

Example:

```html
<code>const a = 5;</code>
<kbd>Ctrl + S</kbd>
<pre>
  Line 1
  Line 2
</pre>
```

### 9. Explain the difference between absolute and relative URLs in HTML.

- Absolute URLs contain the full path, including the domain. Relative URLs are based on the current location of the document.

Example:

```html
<a href="https://example.com/page.html">Absolute URL</a>
<a href="/page.html">Relative URL</a>
```

### 10. What are HTML entities, and why are they used? Provide examples.

- HTML entities are used to display reserved characters. For example, `&lt;` displays `<` and `&amp;` displays `&`.

Example:

```html
&lt;div&gt;
```

### 11. What are the `<header>`, `<footer>`, and `<main>` elements, and how do they contribute to HTML structure?

- `<header>`: Represents the introductory content of a page or section.
- `<footer>`: Represents the footer content.
- `<main>`: Represents the main content of the page.

Example:

```html
<header>Page Header</header>
<main>Main Content</main>
<footer>Footer Information</footer>
```

### 12. Explain the purpose of the `lang` attribute in the `<html>` tag and how it affects accessibility and SEO.

- The `lang` attribute specifies the language of the document. It helps screen readers and improves SEO by indicating the page's language.

Example:

```html
<html lang="en">
```

### 13. What is the purpose of the `<noscript>` tag, and when should it be used?

- The `<noscript>` tag provides content for users with JavaScript disabled.

Example:

```html
<noscript>Please enable JavaScript to view this content.</noscript>
```

### 14. How does the `<link>` tag work, and in which situations is it typically used?

- The `<link>` tag links external resources to the HTML document, such as stylesheets.

Example:

```html
<link rel="stylesheet" href="styles.css">
```

### 15. Describe the function of the `tabindex` attribute and its impact on keyboard navigation.

- The `tabindex` attribute controls the tab order of elements for keyboard navigation.

Example:

```html
<button tabindex="1">First Button</button>
```

### 16. Explain the role of the `<head>` tag in an HTML document and list at least two elements commonly placed within it.

- The `<head>` contains metadata about the document, such as `<title>` and `<meta>` tags.

Example:

```html
<head>
  <title>Website Title</title>
  <meta charset="UTF-8">
</head>
```

### 17. Describe the difference between semantic and non-semantic tags, providing two examples of each.

- Semantic tags clearly describe their meaning (e.g., `<article>`, `<footer>`), while non-semantic tags do not (e.g., `<div>`, `<span>`).

Example:

```html
<article>Article content</article>
<div>Non-semantic content</div>
```

### 18. How do metadata elements in the head section affect an HTML document?

- Metadata elements like `<meta charset>` or `<meta description>` provide information about the page to browsers and search engines.

Example:

```html
<meta charset="UTF-8">
<meta name="description" content="An example website">
```

### 19. What are semantic elements in HTML?

- Semantic elements provide meaning to the content, such as `<header>`, `<section>`, and `<footer>`, which improve readability and accessibility.

Example:

```html
<header>Page Header</header>
```

### 20. Explain the difference between inline and block elements in HTML.

- Inline elements do not start on a new line and only take up as much space as needed. Block elements start on a new line and take up the full width.

Example:

```html
<span>Inline element</span>
<div>Block element</div>
```

### 21. How does the `<meta>` tag work in an HTML document?

- The `<meta>` tag provides metadata about the document, like character set, description, or keywords.

Example:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### 22. Explain the difference between `<section>` and `<article>` tags in HTML.

- `<section>` groups related content, while `<article>` represents a standalone piece of content.

Example:

```html
<section>
  <h2>About Us</h2>
</section>
<article>
  <h2>News Article</h2>
</article>
```

### 23. What is the purpose of the `<base>` tag, and how does it affect links and resources on a page?

- The `<base>` tag sets the base URL for all relative links and resources in the document.

Example:

```html
<base href="https://example.com/">
```

### 24. Describe how `<iframe>` is used in HTML and give a use case for when you might use it.

- The `<iframe>` element embeds another webpage inside the current page.

Example:

```html
<iframe src="https://example.com" width="600" height="400"></iframe>
```

Use case: Embedding a YouTube video or external content.

### 25. Describe how `<picture>` and `<source>` elements work together for responsive images.

- The `<picture>` element allows you to specify multiple sources for an image, adjusting based on screen size or resolution.

Example:

```html
<picture>
  <source media="(min-width: 800px)" srcset="large.jpg">
  <source media="(max-width: 799px)" srcset="small.jpg">
  <img src="default.jpg" alt="Responsive image">
</picture>
```

### 26. How does the `data-*` attribute work, and how can it be used in conjunction with JavaScript?

- The `data-*` attribute stores custom data in HTML elements, which can be accessed via JavaScript.

Example:

```html
<div data-user-id="123">User Info</div>
<script>
  let userId = document.querySelector('div').dataset.userId;
</script>
```

### 27. Describe the `<canvas>` element and how it's typically used in HTML.

- The `<canvas>` element is used for drawing graphics using JavaScript, such as charts or games.

Example:

```html
<canvas id="myCanvas" width="200" height="100"></canvas>
<script>
  var canvas = document.getElementById("myCanvas");
  var ctx = canvas.getContext("2d");
  ctx.fillRect(50, 50, 100, 50);
</script>
```

### 28. What is the purpose of the `<fieldset>` and `<legend>` tags in a form, and how do they improve accessibility?

- `<fieldset>` groups form elements, and `<legend>` provides a label for the group, improving readability and accessibility.

Example:

```html
<fieldset>
  <legend>Personal Information</legend>
  <label for="name">Name:</label>
  <input type="text" id="name">
</fieldset>
```

### 29. How does the `<form>` element work, and what are some best practices when creating forms?

- The `<form>` element collects user input and sends it to a server. Best practices include proper validation, labels for inputs, and using `method="post"` for sensitive data.

Example:

```html
<form action="/submit" method="post">
  <label for="email">Email:</label>
  <input type="email" id="email">
  <button type="submit">Submit</button>
</form>
```

### 30. Explain the role of the `enctype` attribute in an HTML form.

- The `enctype` attribute specifies how the form data should be encoded when submitted, typically used with file uploads (`multipart/form-data`).

Example:

```html
<form action="/upload" method="post" enctype="multipart/form-data">
  <input type="file" name="file">
</form>
```

### 31. What are the roles of `<b>` and `<strong>` tags, and how do they differ semantically?

- `<b>` is used for bold text without adding importance, while `<strong>` indicates text of higher importance semantically.

Example:

```html
<b>Bold Text</b>
<strong>Important Text</strong>
```

### 32. What are the main advantages of using semantic tags in HTML? How do they impact SEO and accessibility?

- Semantic tags provide meaning to the content, improving accessibility for screen readers and helping search engines understand the content structure, which can improve SEO.

Example:

```html
<nav>Main navigation</nav>
```

### 33. Describe the differences between CSS properties and HTML attributes. Provide examples where both might be used to achieve similar styling outcomes.

- HTML attributes are used for behavior (e.g., `href`, `src`), while CSS properties are used for styling (e.g., `color`, `font-size`). Both can affect the appearance, but CSS provides more flexibility.

Example:

```html
<a href="#" style="color: blue;">Link</a>
```

### 34. How does the browser interpret a missing `<!DOCTYPE html>` declaration?

- Without `<!DOCTYPE html>`, the browser may enter quirks mode, leading to inconsistent rendering of the page.

### 35. In the context of an interview, how would you explain the term 'markup' in a concise and understandable way?

- Markup refers to the use of tags in a language like HTML to define and structure content, making it interpretable by browsers.

### 36. What is the purpose of ARIA attributes in HTML?

- ARIA (Accessible Rich Internet Applications) attributes make web content more accessible by providing additional information to assistive technologies.

Example:

```html
<button aria-label="Close">X</button>
```

### 37. Describe the DOM structure of an HTML document.

- The DOM (Document Object Model) represents the structure of an HTML document as a tree of objects, where each node is an element, attribute, or text.

Example:

```html
<html>
  <body>
    <div>Example</div>
  </body>
</html>
```

### 38. What is the purpose of the `async` and `defer` attributes in the `<script>` tag, and how do they affect page loading?

- `async`: Loads the script asynchronously and executes it immediately once loaded.
- `defer`: Delays script execution until the HTML document is fully parsed.

Example:

```html
<script src="script.js" async></script>
```

### 39. How would you optimize an HTML page for better SEO?

- Use semantic tags, optimize images with alt attributes, provide meaningful meta descriptions, and use proper heading structures.

Example:

```html
<meta name="description" content="High-quality HTML content">
```

### 40. What are the different types of lists available in HTML?

1. **Ordered List (`<ol>`)**: Displays items in a numbered list.

```html
<ol>
    <li>Item 1</li>
    <li>Item 2</li>
</ol>
```

2. **Unordered List (`<ul>`)**: Displays items with bullet points.

```html
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>
```

3. **Definition List (`<dl>`)**: Displays terms and their definitions.

```html
<dl>
    <dt>Term 1</dt>
    <dd>Definition 1</dd>
</dl>
```

### 41. What is form validation, and how can it be implemented in HTML?

Form validation is the process of checking user input for correctness before submission. HTML provides attributes for basic validation, such as:

- `required`: Ensures that a field must be filled out before submission.
- `minlength` and `maxlength`: Sets minimum and maximum lengths for input.
- `pattern`: Specifies a regular expression that input must match.
- `type`: Defines the expected input type (e.g., `email`, `url`).

Example:

```html
<input type="email" required>
```

### 42. What is the difference between id and class attributes in HTML?

**id**: A unique identifier for a single HTML element. Each ID must be unique within the document and is used to style or manipulate that specific element.

**class**: A reusable identifier that can be assigned to multiple elements. Classes are used to apply styles or behaviors to groups of elements.

Example:

```html
<div id="uniqueElement">Content</div>
<div class="commonClass">Content 1</div>
<div class="commonClass">Content 2</div>
```

### 43. What are void elements?

- Void elements, also known as self-closing tags or empty elements, are HTML elements that do not require a closing tag.

### 44. What are the main features of HTML5?

1. **Semantic Elements**: Introduces new semantic elements (e.g., `<article>`, `<section>`, `<nav>`, `<header>`, `<footer>`) that improve document structure and enhance accessibility.
2. **Multimedia Support**: Native support for audio and video playback with `<audio>` and `<video>` tags, eliminating the need for third-party plugins.
3. **Form Enhancements**: New input types (e.g., `email`, `date`, `number`) and attributes (e.g., `placeholder`, `required`, `pattern`) improve form validation and user experience.
4. **Canvas and Graphics**: The `<canvas>` element allows for dynamic rendering of 2D graphics and animations directly in the browser using JavaScript.
5. **Local Storage**: Introduces Web Storage APIs (localStorage and sessionStorage) for storing data on the client side, enabling offline capabilities and persistent storage.

---

## One-Line Definitions

* **HTML** → standard markup language for creating web pages.
* **Markup Language** → uses tags to structure and present content.
* **<!DOCTYPE html>** → defines document type and triggers standards mode.
* **Tags vs Attributes** → tags define elements, attributes provide additional info.
* **<title>** → sets the title of the web page in the browser tab.
* **<div>** → block-level container for grouping content.
* **Comments** → `<!-- -->` used to add non-visible notes.
* **Absolute vs Relative URL** → absolute includes domain, relative is based on current location.
* **Semantic Tags** → clearly describe their meaning (e.g., `<article>`).
* **Non-semantic Tags** → do not describe their meaning (e.g., `<div>`).
* **Inline Elements** → take only needed space, don't start a new line.
* **Block Elements** → take full width, start on a new line.
* **<meta>** → provides metadata like charset and description.
* **<iframe>** → embeds another webpage inside the current page.
* **Void Elements** → self-closing tags that do not require a closing tag.
* **DOM** → Document Object Model representing HTML as a tree.
