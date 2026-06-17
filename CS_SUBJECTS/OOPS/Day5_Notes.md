# OOP Day 5 Notes

# Abstraction

## What is Abstraction?

Abstraction is the process of hiding implementation details and showing only essential functionality.

### Simple Meaning

```text
Hide How

Show What
```

### Real Life Example

Car:

```text
✓ Start Car
✓ Accelerate
✓ Brake
```

You know what to do.

You don't know:

```text
How engine works
How fuel injection works
How transmission works
```

The internal implementation is hidden.

---

# Why Do We Need Abstraction?

Without abstraction, users would need to understand every internal detail.

Abstraction helps by:

* Hiding complexity
* Making systems easier to use
* Providing a simple interface
* Improving maintainability

---

# ATM Example

You perform:

```text
Insert Card
Enter PIN
Withdraw Money
```

You don't see:

```text
Database Queries
Bank Servers
Encryption
Network Calls
```

These details are hidden.

This is abstraction.

---

# Abstraction vs Encapsulation

## Encapsulation

```text
Hide Data
```

Example:

```java
private int age;
```

Purpose:

```text
Protect Data
Control Access
```

---

## Abstraction

```text
Hide Implementation
```

Example:

```java
car.start();
```

Purpose:

```text
Hide Complexity
Show Essential Features
```

---

# How Java Achieves Abstraction

Java provides two ways:

```text
1. Abstract Class
2. Interface
```

---

# Abstract Class

A class declared using the `abstract` keyword.

Example:

```java
abstract class Player {

}
```

An abstract class acts as an incomplete blueprint.

---

# Abstract Method

A method without implementation.

Example:

```java
abstract void play();
```

Notice:

```text
No method body

Ends with ;
```

---

## Why Abstract Methods?

Parent knows a method should exist.

But child classes decide how it works.

Example:

```java
abstract class Player {

    abstract void play();
}
```

Child classes:

```java
class Batsman extends Player {

    void play() {
        System.out.println("Batting");
    }
}
```

```java
class Bowler extends Player {

    void play() {
        System.out.println("Bowling");
    }
}
```

---

# Rules of Abstract Class

### Can Have Abstract Methods

```java
abstract void play();
```

---

### Can Have Normal Methods

```java
void welcome() {
    System.out.println("Welcome");
}
```

---

### Can Have Variables

```java
String name;
int age;
```

---

### Cannot Create Objects

```java
Player p = new Player();
```

❌ Not Allowed

---

# Why Can't We Create Objects?

Example:

```java
abstract class Animal {

    abstract void sound();
}
```

If Java allows:

```java
Animal a = new Animal();
```

Then:

```java
a.sound();
```

What should happen?

Java doesn't know because `sound()` has no implementation.

Therefore object creation is not allowed.

---

# Interface

An Interface defines a contract.

Example:

```java
interface Player {

    void play();
}
```

It tells classes:

```text
You must implement play()
```

---

# Implementing Interface

```java
interface Player {

    void play();
}
```

```java
class Batsman implements Player {

    public void play() {
        System.out.println("Batting");
    }
}
```

Notice:

```java
implements
```

is used with interfaces.

---

# Abstract Class vs Interface

| Abstract Class               | Interface                      |
| ---------------------------- | ------------------------------ |
| Uses `abstract class`        | Uses `interface`               |
| Uses `extends`               | Uses `implements`              |
| Can have variables           | Mainly defines contracts       |
| Can have normal methods      | Defines required behavior      |
| Represents IS-A relationship | Represents CAN-DO relationship |

---

# Relationship Types

## Abstract Class → IS-A

Example:

```text
Batsman IS A Player
```

```java
class Batsman extends Player
```

---

## Interface → CAN-DO

Example:

```text
Batsman CAN PLAY

Robot CAN PLAY
```

```java
class Batsman implements Playable
```

---

# Multiple Inheritance

Java does not allow:

```text
Parent1
    \
     Child
    /
Parent2
```

through classes.

But interfaces support it.

Example:

```java
interface A {

}

interface B {

}
```

```java
class Test implements A, B {

}
```

✅ Valid

---

# When to Use Abstract Class?

Use when classes share common data and behavior.

Example:

```text
Player
```

All players have:

```text
name
age
team
```

Use Abstract Class.

---

# When to Use Interface?

Use when you only want a contract.

Examples:

```text
Playable
Drivable
Runnable
Payable
```

Use Interface.

---

# Interview Definitions

### Abstraction

> Hiding implementation details and showing only essential functionality.

---

### Abstract Class

> A class that cannot be instantiated and may contain abstract and non-abstract methods.

---

### Abstract Method

> A method without implementation that must be implemented by child classes.

---

### Interface

> A contract that defines what a class must do.

---

# Quick Revision

```text
Abstraction
=
Hide How
Show What
```

```text
Encapsulation
=
Hide Data
```

```java
abstract class Player
```

Cannot create objects.

---

```java
abstract void play();
```

Abstract method.

No body.

---

```java
interface Playable
```

Contract only.

---

```java
extends
```

Used with Abstract Classes.

---

```java
implements
```

Used with Interfaces.

---

# Formula to Remember

```text
Abstraction
=
Hide Implementation

Abstract Class
=
Partial Blueprint

Interface
=
Contract

extends
=
Abstract Class

implements
=
Interface
```

**Day 5 Complete ✅**

Covered:

* Abstraction
* Encapsulation vs Abstraction
* Abstract Class
* Abstract Method
* Interface
* Abstract Class vs Interface
* IS-A vs CAN-DO Relationship
* Multiple Inheritance via Interfaces
* Interview Definitions and Examples
