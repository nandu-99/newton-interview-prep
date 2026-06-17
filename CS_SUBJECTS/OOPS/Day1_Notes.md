# OOP Day 1 Notes

## Why OOP?

OOP (Object-Oriented Programming) was introduced to:

- Organize code better
- Reuse code
- Reduce duplication
- Model real-world entities
- Make applications scalable and maintainable

### Problem Without OOP

```
student1_name
student1_age

student2_name
student2_age

student3_name
student3_age
```

This becomes difficult to manage as data grows.

---

## Class

A Class is a blueprint or template that defines what properties and behaviors an object should have.

**Example:**

```java
class Student {
    String name;
    int age;
}
```

A class itself is not a real object.

**Interview Definition**

A class is a blueprint used to create objects.

---

## Object

An Object is a real instance of a class.

**Example:**

```java
Student s1 = new Student();
Student s2 = new Student();
```

Here:

- s1 is an object
- s2 is an object

**Interview Definition**

An object is an instance of a class that occupies memory and contains data and behavior.

---

## Class vs Object

| Class | Object |
|-------|--------|
| Blueprint | Real Instance |
| Template | Created from template |
| No memory for instance data | Memory allocated |
| One class | Many objects |

**Example:**

```
Student Class

↓ ↓ ↓

Vivek
Rahul
Aman
```

One class can create multiple objects.

---

## Attributes (Properties)

Attributes store the state/data of an object.

**Example:**

```java
class Student {
    String name;
    int age;
}
```

name and age are attributes.

**Interview Definition**

Attributes are variables inside a class that store the state of an object.

---

## Methods

Methods define the behavior/actions of an object.

**Example:**

```java
class Student {

    void study() {
        System.out.println("Studying");
    }
}
```

**Interview Definition**

Methods define the behavior of an object.

---

## Constructor

A Constructor is a special member of a class used to initialize objects.

**Example:**

```java
class Student {

    String name;
    int age;

    Student(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```

**Usage:**

```java
Student s1 = new Student("Vivek", 22);
```

### Constructor Rules

- Same name as class
- No return type
- Called automatically when object is created
- Used to initialize object data

**Interview Definition**

A constructor is a special member of a class that is automatically called when an object is created to initialize its data.

---

## Memory Formula

```
Class      → Blueprint
Object     → Instance
Attributes → Data
Methods    → Behavior
Constructor → Object Initialization
```
