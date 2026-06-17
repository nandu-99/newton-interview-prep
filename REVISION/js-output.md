# JavaScript Output Questions

### 1.

```js
console.log(x);
var x = 10;
```

**Output:** `undefined`

**Explanation:** The variable `x` is hoisted, so its declaration is moved to the top of the scope, but its assignment happens where it is. Therefore, `console.log(x)` returns `undefined`.

---

### 2.

```js
let a = 5;
const b = 10;
a = 15;
console.log(a, b);
```

**Output:** `15 10`

**Explanation:** `let` allows reassignment, so `a` is updated to `15`. `const` cannot be reassigned, so `b` remains `10`.

---

### 3.

```js
function greet() {
    console.log("Hello, World!");
}
greet();
```

**Output:** `Hello, World!`

**Explanation:** The function `greet` is defined and then called, logging "Hello, World!" to the console.

---

### 4.

```js
let a = 1, b = 2;
[a, b] = [b, a];
console.log(a, b);
```

**Output:** `2 1`

**Explanation:** This uses destructuring assignment to swap the values of `a` and `b`.

---

### 5.

```js
var x = 10;
function showX() {
    console.log(x);
}
var x = 20;
showX();
```

**Output:** `20`

---

### 6.

```js
const arr = [1, 2, 3];
arr.push(4);
console.log(arr);
```

**Output:** `[1, 2, 3, 4]`

**Explanation:** The `const` declaration means the variable cannot be reassigned, but the contents of the array can still be modified. `push` adds `4` to the end of the array.

---

### 7.

```js
let num = 5;
console.log(num++);
console.log(num);
```

**Output:**

```
5
6
```

**Explanation:** `num++` logs `5` first (the current value), then increments `num` to `6`.

---

### 8.

```js
let a = 10;
function changeA() {
    let a = 20;
    console.log(a);
}
changeA();
console.log(a);
```

**Output:**

```
20
10
```

**Explanation:** The inner `a` shadows the outer `a` inside the function. Thus, it logs `20` from inside `changeA` and `10` from the outer scope.

---

### 9.

```js
console.log(x);
let x = 20;
```

**Output:** `ReferenceError: Cannot access 'x' before initialization`

**Explanation:** `let` does not allow access before initialization, so it throws a ReferenceError.

---

### 10.

```js
function outer() {
    var a = 10;
    function inner() {
        console.log(a);
    }
    return inner;
}
let innerFunction = outer();
innerFunction();
```

**Output:** `10`

**Explanation:** The inner function retains access to the outer function's scope, allowing it to log the value of `a`.

---

### 11.

```js
var x = 5;
(function() {
    console.log(x);
    var x = 10;
    console.log(x);
})();
```

**Output:**

```
undefined
10
```

**Explanation:** The inner `var x` is hoisted, so the first `console.log(x)` outputs `undefined`. The second logs `10`.

---

### 12.

```js
const arr = [1, 2, 3];
const [first, ...rest] = arr;
console.log(rest);
```

**Output:** `[2, 3]`

**Explanation:** The rest operator collects the remaining elements of the array into a new array `rest`.

---

### 13.

```js
let x = 10;
function outer() {
    let x = 20;
    function inner() {
        console.log(x);
    }
    return inner;
}
let innerFunc = outer();
innerFunc();
```

**Output:** `20`

**Explanation:** The inner function accesses `x` from the outer function's scope, which is `20`.

---

### 14.

```js
var a = 5;
function scopeTest() {
    if (true) {
        var a = 10;
    }
    console.log(a);
}
scopeTest();
```

**Output:** `10`

**Explanation:** `var` has function scope, so the `a` inside `scopeTest` is the same as the one declared at the beginning.

---

### 15.

```js
const a = 5;
const b = '5';
console.log(a == b);
console.log(a === b);
```

**Output:**

```
true
false
```

**Explanation:** `==` performs type coercion, while `===` checks both value and type.

---

### 16.

```js
let value = 10;
function showValue() {
    console.log(value);
    let value = 20;
}
showValue();
```

**Output:** `ReferenceError: Cannot access 'value' before initialization`

**Explanation:** The `let value` in `showValue` is hoisted, causing a ReferenceError on the first `console.log`.

---

### 17.

```js
let count = 0;
(function increment() {
    count++;
    if (count < 5) increment();
})();
console.log(count);
```

**Output:** `5`

**Explanation:** The function `increment` calls itself recursively until `count` reaches `5`.

---

### 18.

```js
const obj = {
    name: 'Alice',
    sayName: function() {
        console.log(this.name);
    }
};
const sayNameFunc = obj.sayName;
sayNameFunc();
```

**Output:** `undefined`

**Explanation:** `sayNameFunc` loses its context, so `this` is not bound to `obj`, resulting in `undefined`.

---

### 19.

```js
let foo = {
    bar: 'Hello'
};
foo = null;
console.log(foo?.bar);
```

**Output:** `undefined`

**Explanation:** The optional chaining operator (`?.`) checks if `foo` is null or undefined before accessing `bar`, preventing a TypeError.

---

### 20.

```js
function counter() {
    let count = 0;
    return function() {
        count++;
        return count;
    };
}
const increment = counter();
console.log(increment());
console.log(increment());
console.log(increment());
```

**Output:**

```
1
2
3
```

**Explanation:** The inner function maintains state (`count`) across calls, incrementing it each time.

---

### 21.

```js
console.log(a);
var a = 2;
function test() {
    console.log(a);
    var a = 5;
    console.log(a);
}
test();
console.log(a);
```

**Output:**

```
undefined
undefined
5
2
```

**Explanation:** The first `console.log(a)` outputs `undefined` due to hoisting. Inside `test`, the hoisted local `a` is `undefined` first, then logs `5`, and finally `2` from the global scope.

---

### 22.

```js
function makeCounter() {
    let count = 0;
    return {
        increment: function() { count++; return count; },
        decrement: function() { count--; return count; }
    };
}
const counter = makeCounter();
console.log(counter.increment());
console.log(counter.increment());
console.log(counter.decrement());
```

**Output:**

```
1
2
1
```

**Explanation:** The `increment` and `decrement` functions maintain and modify the `count` variable from their closure.

---

### 23.

```js
function scopeExample() {
    if (true) {
        let a = 5;
        const b = 10;
        var c = 15;
    }
    console.log(typeof a);
    console.log(typeof b);
    console.log(c);
}
scopeExample();
```

**Output:**

```
undefined
undefined
15
```

**Explanation:** `a` and `b` are block-scoped and cannot be accessed outside the `if` block, while `c` is hoisted and accessible.

---

### 24.

```js
const x = 1;
function outer() {
    const x = 2;
    function inner() {
        console.log(x);
    }
    return inner;
}
const func = outer();
func();
```

**Output:** `2`

**Explanation:** The inner function has access to the `x` defined in the `outer` function, which is `2`.

---

### 25.

```js
let a = 10;
let b = (function() {
    let a = 20;
    return function() {
        return a;
    };
})();
console.log(b());
```

**Output:** `20`

**Explanation:** The inner function returns the `a` defined in its own scope, which is `20`.

---

### 26.

```js
var x = 3;
function foo() {
    console.log(x);
    var x = 2;
}
foo();
```

**Output:** `undefined`

**Explanation:** The `var x` in `foo` is hoisted, making it `undefined` at the time of the `console.log`.

---

### 27.

```js
let total = 0;
for (let i = 0; i < 5; i++) {
    total += i;
}
console.log(total);
```

**Output:** `10`

**Explanation:** The loop sums `0` to `4`, resulting in `10`.

---

### 28.

```js
const person = {
    name: 'John',
    age: 30,
    greet: function() {
        console.log(`Hello, my name is ${this.name}`);
    }
};
person.greet();
```

**Output:** `Hello, my name is John`

**Explanation:** The `greet` method accesses the `name` property of the `person` object.

---

### 29.

```js
let a = [1, 2, 3];
let b = a;
b.push(4);
console.log(a);
```

**Output:** `[1, 2, 3, 4]`

**Explanation:** Both `a` and `b` refer to the same array in memory, so modifying `b` affects `a`.

---

### 30.

```js
const obj = { a: 1, b: 2 };
const clone = { ...obj };
clone.a = 3;
console.log(obj.a);
```

**Output:** `1`

**Explanation:** The spread operator creates a shallow copy of `obj`, so changes to `clone` do not affect `obj`.
