# OOP Day 2 Notes

## Encapsulation

### What is Encapsulation?

Encapsulation is the process of:

* Wrapping data and methods together into a single unit (Class)
* Restricting direct access to data
* Allowing controlled access through methods

### Simple Meaning

```text
Hide Data
+
Control Access
=
Encapsulation
```

### Real Life Example

ATM Machine

```text
You Can:
✓ Withdraw Money
✓ Deposit Money

You Cannot:
✗ Access Bank Database Directly
```

Same concept is used in OOP.

---

## Why Do We Need Encapsulation?

Without Encapsulation:

```java
class Player {
    public int age;
}
```

Anyone can do:

```java
Player p = new Player();

p.age = -100;
p.age = 1000;
```

This creates invalid data.

Encapsulation protects data from direct modification.

---

## Data Hiding

Data Hiding is achieved using the `private` keyword.

```java
class Player {

    private int age;
}
```

Now:

```java
p.age = 25;
```

❌ Not Allowed

Only methods inside the class can directly access `age`.

---

# Getters and Setters

When variables are private, we need methods to access them.

---

## Setter

Used to update data.

```java
class Player {

    private int age;

    public void setAge(int age) {
        this.age = age;
    }
}
```

Usage:

```java
p.setAge(25);
```

---

## Getter

Used to read data.

```java
class Player {

    private int age;

    public int getAge() {
        return age;
    }
}
```

Usage:

```java
System.out.println(p.getAge());
```

---

## Validation Using Setter

```java
class Player {

    private int age;

    public void setAge(int age) {

        if(age > 0) {
            this.age = age;
        }
    }
}
```

Now:

```java
p.setAge(-10);
```

Invalid value is rejected.

### Why Setter is Better?

Instead of:

```java
p.age = -10;
```

Use:

```java
p.setAge(-10);
```

Because validation can be applied.

---

# Access Modifiers

Access Modifiers control who can access variables and methods.

---

## Private

Accessible only inside the same class.

```java
private int age;
```

### Usage

* Attributes
* Sensitive Data
* Encapsulation

---

## Protected

Accessible in:

* Same Class
* Child Classes
* Same Package

```java
protected int age;
```

Used mostly with Inheritance.

---

## Public

Accessible from anywhere.

```java
public int age;
```

Least restrictive modifier.

---

## Access Modifier Table

| Modifier  | Same Class | Child Class | Everywhere |
| --------- | ---------- | ----------- | ---------- |
| private   | ✅          | ❌           | ❌          |
| protected | ✅          | ✅           | ❌          |
| public    | ✅          | ✅           | ✅          |

---

# Static Keyword

## What is Static?

A static member belongs to the **Class**, not to individual objects.

---

## Non-Static Example

```java
class Student {

    String name;
}
```

```java
Student s1 = new Student();
Student s2 = new Student();
```

Memory:

```text
s1.name

s2.name
```

Each object gets its own copy.

---

## Static Example

```java
class Student {

    static String school = "NST";
}
```

All students belong to the same school.

Creating 1000 students:

```java
Student s1 = new Student();
Student s2 = new Student();
...
```

Still only one copy exists:

```text
school = NST
```

Shared by all objects.

---

## Accessing Static Variables

```java
System.out.println(Student.school);
```

Notice:

No object required.

Access directly through class name.

---

## Static vs Non-Static

| Static                | Non-Static                |
| --------------------- | ------------------------- |
| Belongs to Class      | Belongs to Object         |
| One Copy              | Multiple Copies           |
| Shared by All Objects | Separate for Every Object |
| Accessed via Class    | Accessed via Object       |

---

# Interview Definitions

### Encapsulation

> Encapsulation is the process of wrapping data and methods together while restricting direct access to data.

---

### Data Hiding

> Preventing direct access to class data using private variables.

---

### Getter

> A method used to read private data.

---

### Setter

> A method used to update private data.

---

### Access Modifier

> Controls the visibility and accessibility of variables and methods.

---

### Static

> A static member belongs to the class rather than individual objects.

---

# Quick Revision

```text
Encapsulation
=
private variables
+
public getters
+
public setters
```

```text
private
→ Same Class Only
```

```text
protected
→ Same Class + Child Class
```

```text
public
→ Accessible Everywhere
```

```text
Getter
→ Read Data
```

```text
Setter
→ Update Data
```

```text
Static
→ Belongs To Class
→ One Shared Copy
→ Access Through Class Name
```

# Formula to Remember

```text
Class        → Blueprint
Object       → Instance
Attributes   → Data
Methods      → Behavior
Constructor  → Initialize Object

Encapsulation → Hide Data + Control Access

Static → Shared By All Objects
```
