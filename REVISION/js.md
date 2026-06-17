# JavaScript Revision Notes

### 1. `let`, `const`, and `var`:

- `var`: Function-scoped, can be redeclared, hoisted to the top of the scope.
- `let`: Block-scoped, cannot be redeclared in the same scope, not hoisted like `var`.
- `const`: Block-scoped, must be initialized when declared, cannot be reassigned, but objects/arrays are still mutable.

### 2. Variable Hoisting:

- JavaScript moves declarations to the top of their scope before code execution. `var` is hoisted and initialized as `undefined`, while `let` and `const` are hoisted but not initialized.

### 3. Lexical Scoping:

- Variables are resolved by the scope in which they were defined, not the scope where they are called.

Example:

```js
function outer() {
  let x = 10;
  function inner() {
    console.log(x); // 10
  }
  inner();
}
```

### 4. JavaScript:

- A high-level, interpreted programming language used primarily for web development to create interactive effects within web browsers.

### 5. Events in JavaScript:

- Events are user or system actions (e.g., clicks, key presses) that JavaScript can respond to.

### 6. `==` vs `===`:

- `==`: Loose equality, compares values after type coercion.
- `===`: Strict equality, compares values and types without coercion.

### 7. `null` vs `undefined`:

- `null`: Explicitly set by the developer, meaning "no value".
- `undefined`: A variable that has been declared but not assigned a value.

### 8. Arrow Functions:

- Shorter syntax for functions, do not have their own `this`, and cannot be used as constructors.

Example:

```js
const add = (a, b) => a + b;
```

### 9. Spread Operator (`...`):

- Expands arrays or objects into individual elements. Used in array concatenation, shallow copying, etc.

Example:

```js
const arr1 = [1, 2];
const arr2 = [...arr1, 3, 4]; // [1, 2, 3, 4]
```

### 10. Rest Operator (`...`):

- Collects all remaining elements into an array. Commonly used in function parameters to accept an arbitrary number of arguments.

Example:

```js
function sum(...nums) {
  return nums.reduce((acc, val) => acc + val, 0);
}
```

### 11. `map()`, `filter()`, `reduce()` Array Methods:

- `map()`: Transforms each element in an array and returns a new array.
- `filter()`: Filters elements based on a condition and returns a new array.
- `reduce()`: Reduces an array to a single value by applying a function to each element.

Examples:

```js
[1, 2, 3].map(x => x * 2); // [2, 4, 6]
[1, 2, 3].filter(x => x > 1); // [2, 3]
[1, 2, 3].reduce((acc, x) => acc + x, 0); // 6
```

### 12. Synchronous vs Asynchronous Code:

- Synchronous: Code that runs sequentially, one task at a time.
- Asynchronous: Code that runs in parallel or is deferred, allowing other tasks to continue executing.

### 13. `call()`, `apply()`, `bind()`:

- `call()`: Invokes a function with a specific `this` value and arguments individually.
- `apply()`: Same as `call()`, but arguments are passed as an array.
- `bind()`: Returns a new function that permanently binds `this`.

### 14. `localStorage` and `sessionStorage`:

- `localStorage`: Stores data with no expiration, even after browser is closed.
- `sessionStorage`: Stores data for the current session, cleared when the tab is closed.

### 15. `JSON.parse()` and `JSON.stringify()`:

- `JSON.parse()`: Converts a JSON string into a JavaScript object.
- `JSON.stringify()`: Converts a JavaScript object into a JSON string.

### 16. Global Scope vs Function Scope:

- Global: Variables accessible everywhere in the code.
- Function: Variables accessible only within the function they are defined.

### 17. Variable Shadowing:

- When a variable declared in a local scope has the same name as a variable in an outer scope, the local variable shadows the outer one.

### 18. Execution Context:

- The environment where JavaScript code is executed. Created during the execution phase and consists of the variable environment, scope chain, and `this`.

### 19. `async` and `await`:

- `async`: Declares a function that returns a Promise.
- `await`: Pauses the execution of an `async` function until the Promise is resolved.

### 20. Closures:

- A function that retains access to variables in its lexical scope even when called outside that scope.

Example:

```js
function outer() {
  let x = 10;
  return function inner() {
    return x;
  };
}
```

### 21. Promises:

- Objects representing the eventual completion (or failure) of an asynchronous operation.

Example:

```js
const promise = new Promise((resolve, reject) => {
  resolve('Success');
});
```

### 22. `this` Keyword:

- Refers to the object that is currently executing the function. In strict mode, `this` is `undefined` if not explicitly bound.

### 23. IIFE (Immediately Invoked Function Expressions):

- Functions that are executed immediately after they are defined. Useful for creating private scopes.

Example:

```js
(function() {
  console.log('IIFE');
})();
```

### 24. Event Delegation:

- A technique in which a single event listener is attached to a parent element, which listens for events on its children via event bubbling.

### 25. JavaScript Modules:

- Code organization patterns that allow exporting and importing pieces of code across different files, helping modularity.

### 26. JavaScript's Event Loop:

- A mechanism that handles asynchronous code by pushing tasks from the callback queue to the call stack when the stack is empty.

### 27. Destructuring Assignment:

- Allows unpacking values from arrays or properties from objects into variables.

Example:

```js
const [a, b] = [1, 2];
const {name, age} = {name: 'John', age: 25};
```

### 28. `Object.create()`:

- Creates a new object with the specified prototype object. Different from regular instantiation where you create an object directly.

### 29. Deep Copy vs Shallow Copy:

- Shallow copy copies reference types, not the actual values.
- Deep copy creates a new object and copies all values recursively.

Example (Shallow copy):

```js
let arr = [1, 2, {a: 3}];
let copy = [...arr]; // Only top-level copy
```

### 30. Error Handling (`try`, `catch`, `finally`, `throw`):

- `try`: Defines a block of code to test.
- `catch`: Handles the error if thrown.
- `finally`: Executes code after `try`/`catch` blocks.
- `throw`: Manually throws an error.

### 31. `Promise.all()` and `Promise.race()`:

- `Promise.all()`: Resolves when all promises resolve, or rejects if any promise rejects.
- `Promise.race()`: Resolves/rejects as soon as one promise resolves/rejects.

### 32. Memory Management and Garbage Collection:

- JavaScript automatically handles memory allocation and frees memory when objects are no longer used, using garbage collection.

### 33. `setTimeout()` Function:

- Executes a function after a specified delay. If set to zero, it still defers execution until the current call stack is cleared.

### 34. Mutable vs Immutable Data Structures:

- Mutable: Can be changed (e.g., arrays, objects).
- Immutable: Cannot be changed once created (e.g., strings, numbers).

### 35. `WeakMap` vs `Map`:

- `WeakMap`: Holds key-value pairs where keys are objects, and the keys can be garbage collected if there are no other references.
- `Map`: Holds key-value pairs, including any type of keys, without automatic garbage collection.

### 36. Closures:

- A closure is created when an inner function retains access to variables from its outer function, even after the outer function has executed.

### 37. Lexical Environment:

- Refers to the environment where variables and functions are declared. Closures are based on lexical environments.

### 38. Execution Context Lifecycle:

- Consists of the creation and execution phases. Memory for variables and functions is allocated during creation, and code execution happens in the execution phase.

### 39. Lexical Scoping vs Block Scoping:

- Lexical Scoping: Scope determined by the structure of the code.
- Block Scoping: Scope confined to `{}` blocks (e.g., with `let` and `const`).

### 40. Event Bubbling and Capturing:

- Bubbling: Events propagate from the target element up to the root.
- Capturing: Events propagate from the root to the target.

### 41. Hoisting:

- Variable and function declarations are moved to the top of their scope during the creation phase of the execution context.

### 42. Prototypal Inheritance:

- Objects inherit properties and methods from other objects (prototypes) rather than classes.

### 43. Proxy Object:

- Allows customizing operations on objects like property lookup, assignment, and function invocation.

### 44. Generators and `yield`:

- Generators are functions that can pause execution and later resume. `yield` pauses the function execution and returns a value.

### 45. Symbols:

- Unique and immutable data types, often used to create unique property keys.

### 46. Function Currying:

- A technique where a function with multiple arguments is transformed into a series of functions that take one argument at a time.

Example:

```js
const add = a => b => a + b;
```

### 47. Debouncing and Throttling:

- **Debouncing**: Delays execution of a function until a period of inactivity.
- **Throttling**: Ensures a function is executed at most once in a given time period.

### 48. JavaScript Modules:

- Helps in organizing code by splitting it into multiple files that can export and import functionality, improving reusability and maintainability.

### 49. `Promise.all()` vs `Promise.race()`:

- **Promise.all()** waits for all promises to resolve or any to reject.
- **Promise.race()** resolves/rejects as soon as one of the promises resolves/rejects.

---

## One-Line Definitions

* **JavaScript** → high-level, interpreted language for interactive web effects.
* **var** → function-scoped variable, hoisted.
* **let** → block-scoped variable, can be reassigned.
* **const** → block-scoped variable, cannot be reassigned.
* **Hoisting** → moving declarations to the top of their scope before execution.
* **Lexical Scoping** → variables resolved by their defined scope, not calling scope.
* **== vs ===** → loose equality (with coercion) vs strict equality (no coercion).
* **Arrow Functions** → shorter syntax, do not have their own `this`.
* **Spread Operator (...)** → expands arrays/objects into individual elements.
* **Rest Operator (...)** → collects remaining elements into an array.
* **Synchronous** → runs sequentially, one task at a time.
* **Asynchronous** → runs in parallel or deferred, allowing other tasks to continue.
* **Closures** → inner function retains access to outer function's scope.
* **Promises** → represent eventual completion/failure of an async operation.
* **this** → refers to the object currently executing the function.
* **Event Delegation** → single listener on parent handles events for children.
* **Event Loop** → handles async code by pushing tasks from callback queue to call stack.
