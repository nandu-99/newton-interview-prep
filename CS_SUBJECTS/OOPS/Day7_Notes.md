# OOP Day 7 Notes

# Stack, Heap, References, Object Lifecycle & Garbage Collection

## Memory in Java

Java memory is mainly divided into:

```text
Memory
│
├── Stack
│
└── Heap
```

---

# Stack Memory

Stack stores:

* Local Variables
* Reference Variables
* Method Calls

Example:

```java
int age = 22;
```

Stored in Stack.

---

# Heap Memory

Heap stores:

* Objects
* Arrays

Example:

```java
Student s = new Student();
```

The actual Student object is stored in Heap.

---

# What Happens Here?

```java
Student s = new Student();
```

### Step 1

```java
new Student()
```

Creates an object in Heap.

---

### Step 2

```java
Student s
```

Creates a reference variable in Stack.

---

### Step 3

```java
s = ...
```

Stores the address of the object.

---

## Memory Representation

```text
STACK                    HEAP

s  ------------->      Student Object
```

---

# Reference

A Reference stores the address of an object.

Example:

```java
Student s = new Student();
```

Important:

```text
s is NOT the object.
s stores the address of the object.
```

### Real Life Analogy

```text
House           → Object

House Address   → Reference
```

You carry the address, not the house.

---

# Multiple References

Example:

```java
Student s1 = new Student();

Student s2 = s1;
```

Memory:

```text
STACK

s1 --------\
            \
             ---> Student Object
            /
s2 --------/

HEAP

Student Object
```

---

## Result

Objects:

```text
1
```

References:

```text
2
```

Both references point to the same object.

---

# Shared Object Example

```java
Student s1 = new Student();

Student s2 = s1;

s2.name = "Vivek";
```

Now:

```java
System.out.println(s1.name);
```

Output:

```text
Vivek
```

Because both references point to the same object.

---

# Object Lifecycle

Every object follows:

```text
Created
↓
Used
↓
Unreachable
↓
Garbage Collected
```

---

## Object Creation

```java
Student s = new Student();
```

Object created in Heap.

---

## Object Usage

```java
s.name = "Vivek";
```

Object is actively used.

---

## Object Becomes Unreachable

```java
Student s = new Student();

s = null;
```

Memory:

```text
STACK               HEAP

s = null          Student Object
```

No reference points to the object.

The object becomes unreachable.

---

# Garbage Collection (GC)

Java automatically removes unreachable objects.

Example:

```java
Student s = new Student();

s = null;
```

Now the object becomes eligible for Garbage Collection.

---

## Responsibilities of Garbage Collector

```text
Find Unused Objects

Free Memory

Prevent Memory Waste
```

---

# Why Garbage Collection?

Without GC:

```text
Unused objects stay in memory forever.
```

This can eventually cause:

```text
OutOfMemoryError
```

---

# Important Point

Garbage Collection is:

```text
Automatic
```

You cannot force it.

You can only request it:

```java
System.gc();
```

JVM may or may not run GC immediately.

---

# Null Reference

Example:

```java
Student s = null;
```

Now:

```java
s.name = "Vivek";
```

❌ Error

Because:

```text
s points to nothing.
```

Runtime Error:

```text
NullPointerException
```

---

# Stack vs Heap

| Stack             | Heap                   |
| ----------------- | ---------------------- |
| Stores Variables  | Stores Objects         |
| Stores References | Stores Arrays          |
| Faster Access     | Larger Memory Area     |
| Automatic Cleanup | Uses Garbage Collector |
| Method Calls      | Object Data            |

---

# Memory Example 1

```java
Student s1 = new Student();

Student s2 = new Student();
```

Result:

```text
Objects = 2

References = 2
```

---

# Memory Example 2

```java
Student s1 = new Student();

Student s2 = s1;
```

Result:

```text
Objects = 1

References = 2
```

---

# Interview Definitions

### Stack Memory

> Memory area that stores local variables, references, and method calls.

---

### Heap Memory

> Memory area where objects and arrays are stored.

---

### Reference

> A variable that stores the address of an object.

---

### Garbage Collection

> The automatic process of removing unreachable objects from memory.

---

### Object Lifecycle

> The journey of an object from creation to garbage collection.

---

# Quick Revision

```text
Stack
=
Variables
References
Method Calls
```

```text
Heap
=
Objects
Arrays
```

```java
Student s = new Student();
```

```text
Reference → Stack

Object → Heap
```

```java
Student s2 = s1;
```

```text
1 Object

2 References
```

```java
s = null;
```

```text
Object becomes unreachable
```

```text
Garbage Collector
=
Removes Unused Objects
```

# Formula to Remember

```text
Stack
=
References + Variables

Heap
=
Objects

Reference
=
Address of Object

Object Lifecycle
=
Create
↓
Use
↓
Unreachable
↓
Garbage Collection
```
