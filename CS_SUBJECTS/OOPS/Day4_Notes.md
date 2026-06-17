# OOP Day 4 Notes

# Polymorphism

## What is Polymorphism?

The word Polymorphism comes from:

```text
Poly  = Many

Morph = Forms
```

Meaning:

```text
One thing can have multiple forms or behaviors
```

### Interview Definition

> Polymorphism is the ability of an object to take multiple forms.

---

# Why Do We Need Polymorphism?

Suppose all players can:

```java
play()
```

But their behavior is different.

```text
Batsman → Batting

Bowler → Bowling

Keeper → Keeping
```

Same method.

Different behavior.

This is Polymorphism.

---

# Types of Polymorphism

```text
1. Compile-Time Polymorphism
2. Run-Time Polymorphism
```

---

# Method Overloading

## What is Overloading?

Defining multiple methods with the same name but different parameters.

Example:

```java
class Calculator {

    int add(int a, int b) {
        return a + b;
    }

    int add(int a, int b, int c) {
        return a + b + c;
    }
}
```

Usage:

```java
Calculator c = new Calculator();

c.add(10, 20);

c.add(10, 20, 30);
```

---

## Why Overloading?

Without Overloading:

```java
add2Numbers()

add3Numbers()

add4Numbers()
```

With Overloading:

```java
add()
```

Cleaner and easier to use.

---

## Rules for Overloading

Must change:

### Number of Parameters

```java
add(int a, int b)

add(int a, int b, int c)
```

---

### Type of Parameters

```java
add(int a, int b)

add(double a, double b)
```

---

## Invalid Overloading

Only changing return type:

```java
int add(int a, int b)

double add(int a, int b)
```

❌ Not Allowed

Because parameter list is identical.

---

# Compile-Time Polymorphism

Method Overloading is called:

```text
Compile-Time Polymorphism
```

Reason:

```text
Compiler decides which method to call
```

before the program runs.

---

# Method Overriding

## What is Overriding?

When a Child Class provides its own implementation of a Parent Class method.

Parent:

```java
class Player {

    void play() {
        System.out.println("Playing");
    }
}
```

Child:

```java
class Batsman extends Player {

    @Override
    void play() {
        System.out.println("Batting");
    }
}
```

Usage:

```java
Batsman b = new Batsman();

b.play();
```

Output:

```text
Batting
```

---

# Why Overriding?

Parent class provides generic behavior.

```text
Player → Playing
```

Child class provides specific behavior.

```text
Batsman → Batting

Bowler → Bowling

Keeper → Keeping
```

---

# Runtime Polymorphism

Example:

```java
Player p = new Batsman();

p.play();
```

Output:

```text
Batting
```

Even though reference type is Player.

Reason:

```text
Actual Object = Batsman
```

Java executes the Child's overridden method.

---

## Why Called Runtime Polymorphism?

Because Java decides which method to execute while the program is running.

```text
Decision happens at Runtime
```

---

# Visual Representation

```text
            Player
               |
      -------------------
      |                 |
   Batsman          Bowler

 play()            play()

 Batting           Bowling
```

Same method.

Different behavior.

---

# Overloading vs Overriding

| Overloading              | Overriding               |
| ------------------------ | ------------------------ |
| Same Class               | Parent & Child Classes   |
| Different Parameters     | Same Parameters          |
| Inheritance Not Required | Inheritance Required     |
| Compile-Time             | Run-Time                 |
| Multiple Methods         | Replaces Existing Method |

---

# Example of Overloading

```java
class Calculator {

    int add(int a, int b) {
        return a + b;
    }

    int add(int a, int b, int c) {
        return a + b + c;
    }
}
```

---

# Example of Overriding

```java
class Animal {

    void sound() {
        System.out.println("Animal Sound");
    }
}

class Dog extends Animal {

    @Override
    void sound() {
        System.out.println("Bark");
    }
}
```

---

# Advantages of Polymorphism

### Flexibility

Same method can behave differently.

---

### Reusability

Common parent code can be reused.

---

### Cleaner Code

Instead of:

```java
bat()

bowl()

keep()
```

Use:

```java
play()
```

with different implementations.

---

# Interview Definitions

### Polymorphism

> Polymorphism is the ability of an object to take multiple forms.

---

### Method Overloading

> Defining multiple methods with the same name but different parameters.

---

### Method Overriding

> Providing a new implementation of a parent class method in a child class.

---

### Compile-Time Polymorphism

> Polymorphism achieved through Method Overloading.

---

### Runtime Polymorphism

> Polymorphism achieved through Method Overriding.

---

# Quick Revision

```text
Polymorphism
=
Many Forms
```

```text
Overloading
=
Same Method Name
+
Different Parameters
```

```text
Overriding
=
Same Method Name
+
Same Parameters
+
Different Implementation
```

```text
Overloading
→ Compile-Time
```

```text
Overriding
→ Runtime
```

```text
Overloading
→ Inheritance Not Required
```

```text
Overriding
→ Inheritance Required
```

# Formula to Remember

```text
Polymorphism
=
Overloading
+
Overriding

Overloading
=
Same Method
Different Parameters

Overriding
=
Same Method
Different Behavior
```
