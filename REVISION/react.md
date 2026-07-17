# React Revision Notes

### 1. What is React and why is it used?

- React is a JavaScript library for building user interfaces, developed by Meta. It uses a component-based architecture and a virtual DOM to efficiently update and render UI.

### 2. JSX (JavaScript XML):

- JSX is a syntax extension that lets you write HTML-like code inside JavaScript. It gets compiled to `React.createElement()` calls by Babel.

Example:

```jsx
const element = <h1>Hello, World!</h1>;
// compiles to:
const element = React.createElement('h1', null, 'Hello, World!');
```

### 3. Functional vs Class Components:

- **Functional**: JavaScript functions that return JSX. Simpler, support hooks, and are the modern standard.
- **Class**: ES6 classes that extend `React.Component`. Use `this.state` and lifecycle methods. Mostly legacy now.

Example:

```jsx
// Functional
function Greeting({ name }) {
  return <h1>Hiii, {name}</h1>;
}

// Class
class Greeting extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

### 4. Props (Properties):

- Props are read-only inputs passed from a parent component to a child. They allow data to flow down the component tree.

Example:

```jsx
function Button({ label, onClick }) {
  return <button onClick={onClick}>{label}</button>;
}

// Usage
<Button label="Click me" onClick={() => alert('clicked')} />
```

### 5. State vs Props:

- **Props**: Passed in from the parent, read-only inside the component.
- **State**: Managed internally by the component, can change over time and triggers a re-render when updated.

### 6. `useState` Hook:

- Declares a state variable inside a functional component. Returns the current value and a setter function.

Example:

```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>Count: {count}</button>;
}
```

### 7. `useEffect` Hook:

- Runs side effects (API calls, subscriptions, DOM manipulation) after the component renders. Replaces lifecycle methods like `componentDidMount` and `componentDidUpdate`.

Example:

```jsx
import { useEffect } from 'react';

function App() {
  useEffect(() => {
    console.log('Component mounted or updated');
  });
}
```

### 8. Dependency Array and Cleanup in `useEffect`:

- The dependency array controls when the effect re-runs. Returning a function from `useEffect` acts as a cleanup (like `componentWillUnmount`).

Example:

```jsx
useEffect(() => {
  const timer = setInterval(() => console.log('tick'), 1000);

  return () => clearInterval(timer); // cleanup on unmount
}, []); // [] = run only once on mount
```

- `[]` → runs once on mount.
- `[value]` → runs when `value` changes.
- No array → runs after every render.

### 9. `useRef` Hook:

- Returns a mutable ref object whose `.current` property persists across renders without causing re-renders. Commonly used to access DOM elements directly.

Example:

```jsx
import { useRef } from 'react';

function InputFocus() {
  const inputRef = useRef(null);
  return (
    <>
      <input ref={inputRef} />
      <button onClick={() => inputRef.current.focus()}>Focus</button>
    </>
  );
}
```

### 10. `useContext` Hook:

- Lets you read a context value without prop drilling. The provider wraps the component tree and the consumer reads the value anywhere below it.

Example:

```jsx
const ThemeContext = React.createContext('light');

function App() {
  return (
    <ThemeContext.Provider value="dark">
      <Child />
    </ThemeContext.Provider>
  );
}

function Child() {
  const theme = useContext(ThemeContext);
  return <p>Theme: {theme}</p>;
}
```

### 11. `useMemo` and `useCallback`:

- **`useMemo`**: Memoizes the result of an expensive calculation, recomputing only when dependencies change.
- **`useCallback`**: Memoizes a function reference so it doesn't get recreated on every render.

Example:

```jsx
const expensiveValue = useMemo(() => computeHeavy(data), [data]);

const handleClick = useCallback(() => {
  doSomething(id);
}, [id]);
```

### 12. Custom Hooks:

- A JavaScript function whose name starts with `use` that can call other hooks. Used to extract and reuse stateful logic across components.

Example:

```jsx
function useWindowWidth() {
  const [width, setWidth] = useState(window.innerWidth);
  useEffect(() => {
    const handler = () => setWidth(window.innerWidth);
    window.addEventListener('resize', handler);
    return () => window.removeEventListener('resize', handler);
  }, []);
  return width;
}
```

### 13. Virtual DOM:

- React keeps a lightweight in-memory copy of the real DOM (the virtual DOM). When state or props change, React creates a new virtual DOM tree and compares it to the previous one.

### 14. Reconciliation and Diffing:

- React's algorithm for comparing the old and new virtual DOM trees to find the minimum set of changes needed. It then batches and applies only those changes to the real DOM.

### 15. Keys in Lists:

- Keys help React identify which items in a list have changed, been added, or removed. They must be unique among siblings.

Example:

```jsx
const items = ['a', 'b', 'c'];
return (
  <ul>
    {items.map((item) => (
      <li key={item}>{item}</li>
    ))}
  </ul>
);
```

- Avoid using array index as a key if the list order can change — it breaks reconciliation.

### 16. Conditional Rendering:

- Render different UI based on a condition. Common patterns: `&&`, ternary `? :`, or early `return`.

Example:

```jsx
function Alert({ isError }) {
  return isError ? <p>Error occurred</p> : <p>All good</p>;
}

// Short-circuit
function Badge({ count }) {
  return count > 0 && <span>{count}</span>;
}
```

### 17. Event Handling in React:

- React uses camelCase event names and passes a function reference (not a string). Synthetic events wrap native events for cross-browser compatibility.

Example:

```jsx
function Form() {
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('submitted');
  };
  return <form onSubmit={handleSubmit}>...</form>;
}
```

### 18. Controlled vs Uncontrolled Components:

- **Controlled**: Form input value is driven by React state. Single source of truth.
- **Uncontrolled**: Input manages its own state internally; accessed via `ref`.

Example:

```jsx
// Controlled
function Controlled() {
  const [value, setValue] = useState('');
  return <input value={value} onChange={(e) => setValue(e.target.value)} />;
}

// Uncontrolled
function Uncontrolled() {
  const inputRef = useRef();
  return <input ref={inputRef} />;
}
```

### 19. Lifting State Up:

- When multiple components need to share state, move the state to their closest common ancestor and pass it down as props.

Example:

```jsx
function Parent() {
  const [value, setValue] = useState('');
  return (
    <>
      <InputChild value={value} onChange={setValue} />
      <DisplayChild value={value} />
    </>
  );
}
```

### 20. `React.Fragment`:

- A wrapper that groups multiple elements without adding an extra DOM node.

Example:

```jsx
return (
  <>
    <h1>Title</h1>
    <p>Paragraph</p>
  </>
);
// shorthand for <React.Fragment>...</React.Fragment>
```

---

## One-Line Definitions

* **React** → JavaScript library for building component-based UIs with a virtual DOM.
* **JSX** → HTML-like syntax in JS that compiles to `React.createElement()` calls.
* **Functional Component** → a plain function that returns JSX; supports hooks.
* **Class Component** → ES6 class extending `React.Component`; uses lifecycle methods.
* **Props** → read-only data passed from parent to child component.
* **State** → internal, mutable data that triggers a re-render when updated.
* **useState** → hook to declare and update state in a functional component.
* **useEffect** → hook to run side effects after render; replaces lifecycle methods.
* **Dependency Array** → controls when `useEffect` re-runs; `[]` means mount only.
* **Cleanup Function** → returned from `useEffect`; runs before unmount or re-run.
* **useRef** → hook that holds a mutable value or DOM reference without re-rendering.
* **useContext** → hook to consume a context value without prop drilling.
* **useMemo** → memoizes a computed value, recomputes only when dependencies change.
* **useCallback** → memoizes a function reference to prevent unnecessary re-creation.
* **Custom Hook** → a `use`-prefixed function that reuses stateful logic across components.
* **Virtual DOM** → in-memory copy of the real DOM that React uses to compute updates.
* **Reconciliation** → React's diffing algorithm to find and apply minimal DOM changes.
* **Keys** → unique identifiers on list items to help React track changes efficiently.
* **Conditional Rendering** → showing different UI based on a condition (`&&`, ternary).
* **Controlled Component** → form element whose value is fully managed by React state.
* **Uncontrolled Component** → form element that manages its own state via a ref.
* **Lifting State Up** → moving shared state to the nearest common ancestor component.
* **React.Fragment** → groups elements without adding an extra DOM node.
