# Node.js Master Revision Notes

## What is Node.js

**Node.js** is a JavaScript runtime built on Chrome's **V8 engine** that lets you run JavaScript outside the browser.

```text
Browser → JavaScript runs in V8 inside the browser
Node.js → JavaScript runs in V8 on your machine / server
```

* **Single-threaded** → one thread handles all requests.
* **Non-blocking I/O** → while waiting for a file/DB/network, it handles other requests.
* **Event-driven** → responds to events (requests, file reads, timers).

```text
Good for  → I/O-heavy apps (APIs, real-time, chat)
Not ideal → CPU-heavy tasks (video encoding, ML) — blocks the single thread
```

---

## Event Loop

Node.js is single-threaded but handles concurrency via the **event loop** — a mechanism that offloads I/O operations and picks up results when ready.

### Components

```text
Call Stack        → where JS code executes (one at a time)
Web APIs / libuv  → handles async tasks (setTimeout, file I/O, network)
Microtask Queue   → resolved Promises, queueMicrotask
Callback Queue    → setTimeout, setInterval callbacks
```

### Execution Order

```text
1. Run all synchronous code (Call Stack)
2. Process all Microtasks (Promises)
3. Process one Macrotask (setTimeout / setInterval)
4. Repeat
```

```js
console.log('1');

setTimeout(() => console.log('2'), 0);

Promise.resolve().then(() => console.log('3'));

console.log('4');

// Output: 1, 4, 3, 2
// Sync first → microtask (Promise) → macrotask (setTimeout)
```

### Visual

```text
   Code
    ↓
[Call Stack] → sync code runs here
    ↓ (async task handed off)
[libuv / Web APIs] → file read, timer, network
    ↓ (done)
[Microtask Queue] ← Promises resolve here  (checked first)
[Callback Queue]  ← setTimeout lands here  (checked after)
    ↓
Event Loop picks next task → pushes to Call Stack
```

---

## async / await

**Promises** represent a value that will be available in the future.

```js
fetch('/api/user')
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));
```

**async/await** is cleaner syntax over Promises — same thing, easier to read.

```js
async function getUser() {
  try {
    const res = await fetch('/api/user');
    const data = await res.json();
    console.log(data);
  } catch (err) {
    console.error(err);
  }
}
```

* `async` → marks a function as asynchronous; it always returns a Promise.
* `await` → pauses execution inside the async function until the Promise resolves.
* Errors are caught with `try/catch`.

### Sequential vs Parallel

```js
// Sequential — second waits for first to finish
const user = await getUser();
const orders = await getOrders();

// Parallel — both run at the same time (faster)
const [user, orders] = await Promise.all([getUser(), getOrders()]);
```

**Use `Promise.all` when tasks are independent.**

---

## Middleware

**Middleware** is a function that runs between the incoming request and the final route handler.

```text
Request → middleware 1 → middleware 2 → route handler → Response
```

Every middleware has access to `req`, `res`, and `next`.

```js
function logger(req, res, next) {
  console.log(`${req.method} ${req.url}`);
  next(); // pass control to the next middleware
}
```

* Call `next()` → moves to the next middleware.
* Don't call `next()` → request stops here (must send a response or it hangs).

### Types of Middleware

| Type | Example | Purpose |
| ---- | ------- | ------- |
| Built-in | `express.json()` | Parse JSON request bodies |
| Third-party | `morgan`, `cors` | Logging, CORS headers |
| Custom | your own function | Auth checks, validation |
| Error-handling | `(err, req, res, next)` | Catch and respond to errors |

```js
app.use(express.json());          // parse JSON body
app.use(logger);                  // custom middleware
app.get('/users', getUsers);      // route handler
app.use((err, req, res, next) => { // error handler (4 params)
  res.status(500).json({ error: err.message });
});
```

---

## How Express Handles a Request

```text
Incoming HTTP Request
        ↓
Express receives it (http.createServer under the hood)
        ↓
Global middleware runs (express.json, cors, morgan...)
        ↓
Router matches method + path (GET /users/:id)
        ↓
Route-level middleware runs (auth check, validation...)
        ↓
Route handler runs → builds response
        ↓
res.json() / res.send() → Response sent back to client
```

### What if nothing matches?

Express falls through all routes — if no route matches, you need a catch-all:

```js
app.use((req, res) => {
  res.status(404).json({ error: 'Not found' });
});
```

### Quick Example

```js
const express = require('express');
const app = express();

app.use(express.json());                        // middleware

app.get('/users/:id', (req, res) => {           // route
  const { id } = req.params;
  res.json({ id, name: 'Alice' });
});

app.listen(3000);
```

---

## REST APIs

**REST (Representational State Transfer)** is an architectural style for building APIs using HTTP.

### REST Principles

* **Stateless** → server stores no session state; each request is self-contained.
* **Resource-based URLs** → URLs represent things, not actions.
* **HTTP methods** → the method defines the action.

```text
Good: GET /users/1
Bad:  GET /getUser?id=1
```

### HTTP Methods

| Method | Action | Body? |
| ------ | ------ | ----- |
| GET | Read | No |
| POST | Create | Yes |
| PUT | Replace (full update) | Yes |
| PATCH | Partial update | Yes |
| DELETE | Delete | No |

### Status Codes (key ones)

| Code | Meaning |
| ---- | ------- |
| 200 | OK |
| 201 | Created |
| 204 | No Content (success, nothing to return) |
| 400 | Bad Request |
| 401 | Unauthorized (not logged in) |
| 403 | Forbidden (logged in but no permission) |
| 404 | Not Found |
| 500 | Internal Server Error |

### Headers

| Header | Purpose |
| ------ | ------- |
| `Content-Type: application/json` | Body is JSON |
| `Authorization: Bearer <token>` | Pass auth token |
| `Accept: application/json` | Client expects JSON |
| `Access-Control-Allow-Origin: *` | CORS — allow cross-origin requests |

---

## Design a Simple API Endpoint (Verbal)

**Question:** "Design an endpoint to get a user by ID."

**How to answer:**

```text
1. Method + URL
   GET /users/:id
   GET because we're reading data. URL uses a resource noun, ID as a path param.

2. Request
   No body needed for GET.
   May need Authorization header if the route is protected.

3. Happy path response — 200 OK
   { "id": 1, "name": "Alice", "email": "alice@example.com" }

4. Error cases
   User not found     → 404 Not Found  { "error": "User not found" }
   Not authenticated  → 401 Unauthorized
   Server crash       → 500 Internal Server Error

5. Middleware involved
   Auth middleware verifies token before the handler runs.
```

**Reusable template for any endpoint:**

```text
→ What method and URL?
→ What goes in the request (params, body, headers)?
→ What does the happy path return (status + shape)?
→ What are the error cases and their status codes?
→ Any middleware needed (auth, validation)?
```

---

## One-Line Definitions

* **Node.js** → JavaScript runtime on V8; single-threaded, non-blocking.
* **Event Loop** → mechanism that offloads async work and processes results when ready.
* **Call Stack** → where synchronous JS executes, one frame at a time.
* **Microtask Queue** → where resolved Promises queue (runs before macrotasks).
* **Callback Queue** → where setTimeout/setInterval callbacks queue.
* **async** → marks a function as asynchronous; returns a Promise.
* **await** → pauses async function until a Promise resolves.
* **Promise.all** → runs multiple async tasks in parallel, waits for all.
* **Middleware** → function that runs between request and response; has req, res, next.
* **next()** → passes control to the next middleware in the chain.
* **Express** → minimal Node.js web framework for routing and middleware.
* **REST** → stateless, resource-based API design using HTTP methods.
* **Stateless** → server holds no session; every request is self-contained.
* **401** → not authenticated. **403** → authenticated but not authorized.
* **204** → success with no content to return.
