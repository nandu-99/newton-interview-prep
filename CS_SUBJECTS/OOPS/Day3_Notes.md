# OOP Day 3 Notes

# Inheritance

## What is Inheritance?

Inheritance is a mechanism where one class acquires the properties and behaviors of another class.

### Interview Definition

> Inheritance is a mechanism by which one class acquires the properties and methods of another class.

---

# Why Do We Need Inheritance?

Without Inheritance:

```java
class Batsman {

    String name;
    int age;

    void play() {
        System.out.println("Playing");
    }

    int runs;
}
```

```java
class Bowler {

    String name;
    int age;

    void play() {
        System.out.println("Playing");
    }

    int wickets;
}
```

Common code is repeated.

### Problem

```text
name
age
play()
```

are duplicated.

---

## Solution

Put common properties in a Parent Class.

```java
class Player {

    String name;
    int age;

    void play() {
        System.out.println("Playing");
    }
}
```

```java
class Batsman extends Player {

    int runs;
}
```

```java
class Bowler extends Player {

    int wickets;
}
```

Now no duplication exists.

---

# Parent Class

The class whose properties and methods are inherited.

```java
class Player {

}
```

Also called:

```text
Parent Class
Super Class
Base Class
```

---

# Child Class

The class that inherits from another class.

```java
class Batsman extends Player {

}
```

Also called:

```text
Child Class
Sub Class
Derived Class
```

---

# extends Keyword

Used to create inheritance.

```java
class Batsman extends Player {

}
```

Meaning:

```text
Batsman inherits from Player
```

---

# IS-A Relationship

Inheritance follows an IS-A relationship.

Examples:

```text
Dog IS A Animal

Student IS A Person

Car IS A Vehicle

Batsman IS A Player
```

If the sentence sounds natural, inheritance is usually valid.

---

# What Does a Child Class Get?

Parent:

```java
class Player {

    String name;
    int age;

    void play() {
        System.out.println("Playing");
    }
}
```

Child:

```java
class Batsman extends Player {

    int runs;
}
```

Usage:

```java
Batsman b = new Batsman();

b.name = "Virat";
b.age = 36;
b.runs = 150;
```

The child class can use parent properties and methods.

---

# Visual Representation

```text
Player
│
├── name
├── age
└── play()

      ↑

Batsman
│
└── runs
```

---

# Constructor Inheritance

Parent:

```java
class Player {

    Player() {
        System.out.println("Player Constructor");
    }
}
```

Child:

```java
class Batsman extends Player {

    Batsman() {
        System.out.println("Batsman Constructor");
    }
}
```

```java
new Batsman();
```

Output:

```text
Player Constructor
Batsman Constructor
```

### Rule

```text
Parent Constructor Runs First
Child Constructor Runs Second
```

---

# super Keyword

Used to access Parent Class members.

### Access Parent Variable

```java
class Player {

    String name = "Player";
}
```

```java
class Batsman extends Player {

    String name = "Virat";

    void show() {
        System.out.println(super.name);
    }
}
```

Output:

```text
Player
```

---

### Access Parent Method

```java
class Player {

    void play() {
        System.out.println("Player Playing");
    }
}
```

```java
class Batsman extends Player {

    void show() {
        super.play();
    }
}
```

Output:

```text
Player Playing
```

---

# Advantages of Inheritance

### Code Reusability

Write code once and reuse it.

---

### Less Duplication

Avoid repeated code.

---

### Easier Maintenance

Changes in parent class automatically benefit child classes.

---

### Better Organization

Creates a natural hierarchy.

Example:

```text
Player
│
├── Batsman
├── Bowler
└── WicketKeeper
```

---

# Types of Inheritance

## Single Inheritance

```text
Player
   ↑
Batsman
```

One Parent → One Child

---

## Multilevel Inheritance

```text
Person
   ↑
Player
   ↑
Batsman
```

Chain of inheritance.

---

## Hierarchical Inheritance

```text
         Player
       /    |    \
Batsman  Bowler  Keeper
```

One Parent → Multiple Children

---

## Multiple Inheritance

```text
Parent1
    \
     Child
    /
Parent2
```

Java classes do not support this directly.

---

# What Cannot Be Inherited?

Private members.

```java
class Player {

    private int salary;
}
```

```java
class Batsman extends Player {

    void show() {
        System.out.println(salary);
    }
}
```

❌ Error

Because private members belong only to the class where they are declared.

---

# Interview Definitions

### Inheritance

> A mechanism by which one class acquires the properties and methods of another class.

### Parent Class

> The class whose members are inherited.

### Child Class

> The class that inherits from another class.

### extends

> Keyword used to establish inheritance.

### super

> Keyword used to access parent class variables, methods, and constructors.

---

# Quick Revision

```text
Inheritance
→ Code Reuse
```

```text
Child IS A Parent
```

```java
class Child extends Parent
```

```text
Parent Constructor
Runs First
```

```java
super
```

```text
Access Parent Members
```

```text
Private Members
Cannot Be Inherited
```

# Formula to Remember

```text
Inheritance
=
Parent Class
+
Child Class
+
extends

super
=
Access Parent

Child IS A Parent
```
