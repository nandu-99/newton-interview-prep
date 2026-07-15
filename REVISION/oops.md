# OOP Master Revision Notes

## Why OOP?

* Organize code better
* Reuse code
* Reduce duplication
* Model real-world entities
* Scalable and maintainable

---

## Class & Object

**Class** → blueprint used to create objects.

**Object** → instance of a class that occupies memory and contains data and behavior.

```java
class Student {
    String name;
    int age;
}

Student s1 = new Student();
```

| Class | Object |
| ----- | ------ |
| Blueprint | Real Instance |
| No memory for instance data | Memory allocated |
| One class | Many objects |

**Attributes** → variables that store the state of an object.

**Methods** → define the behavior of an object.

---

## Constructor

Special member, automatically called when an object is created, to initialize its data.

```java
Student(String name, int age) {
    this.name = name;
    this.age = age;
}
```

Rules:

* Same name as class
* No return type
* Called automatically on object creation

---

## The 4 Pillars

```text
Encapsulation
Abstraction
Inheritance
Polymorphism
```

---

## 1. Encapsulation

Wrapping data and methods together, restricting direct access to data, allowing controlled access through methods.

```text
Hide Data + Control Access = Encapsulation
```

* **Data Hiding** → make fields `private`.
* **Getter** → read private data.
* **Setter** → update private data (allows validation).

```java
class Player {
    private int age;

    public void setAge(int age) {
        if (age > 0) this.age = age;
    }

    public int getAge() {
        return age;
    }
}
```

### Access Modifiers

| Modifier  | Same Class | Child Class | Everywhere |
| --------- | ---------- | ----------- | ---------- |
| private   | ✅ | ❌ | ❌ |
| protected | ✅ | ✅ | ❌ |
| public    | ✅ | ✅ | ✅ |

### Static

A static member belongs to the **class**, not individual objects. One shared copy, accessed via class name.

```java
class Student {
    static String school = "NST";
}

System.out.println(Student.school);
```

| Static | Non-Static |
| ------ | ---------- |
| Belongs to Class | Belongs to Object |
| One Copy | Multiple Copies |
| Accessed via Class | Accessed via Object |

---

## 2. Abstraction

Hiding implementation details and showing only essential functionality.

```text
Hide How + Show What
```

Java achieves abstraction via **Abstract Class** and **Interface**.

| Encapsulation | Abstraction |
| ------------- | ----------- |
| Hide Data | Hide Implementation |
| Protect Data | Hide Complexity |

### Abstract Class

* Declared with `abstract`
* Can have abstract methods, normal methods, and variables
* **Cannot create objects**

```java
abstract class Player {
    abstract void play();   // no body
}

class Batsman extends Player {
    void play() { System.out.println("Batting"); }
}
```

### Interface

Defines a contract — what a class must do.

```java
interface Player {
    void play();
}

class Batsman implements Player {
    public void play() { System.out.println("Batting"); }
}
```

| Abstract Class | Interface |
| -------------- | --------- |
| `abstract class` | `interface` |
| `extends` | `implements` |
| Can have variables | Mainly contracts |
| IS-A relationship | CAN-DO relationship |

* Use **Abstract Class** when classes share common data and behavior.
* Use **Interface** when you only want a contract.
* Multiple inheritance → not allowed via classes, allowed via interfaces (`implements A, B`).

---

## 3. Inheritance

One class acquires the properties and methods of another class.

```java
class Player {              // Parent / Super / Base
    String name;
    void play() {}
}

class Batsman extends Player {   // Child / Sub / Derived
    int runs;
}
```

* `extends` → creates inheritance.
* Follows **IS-A** relationship (Batsman IS A Player).
* Parent constructor runs first, then child.
* `super` → access parent variables, methods, constructor.
* **Private members cannot be inherited.**

### Types

```text
Single        → Player → Batsman
Multilevel    → Person → Player → Batsman
Hierarchical  → Player → Batsman, Bowler, Keeper
Multiple      → not supported via classes
```

---

## 4. Polymorphism

Ability of an object to take multiple forms. Same method, different behavior.

### Method Overloading (Compile-Time)

Same method name, different parameters. Compiler decides which to call.

```java
int add(int a, int b);
int add(int a, int b, int c);
```

* Must change number or type of parameters.
* Changing only return type → ❌ not allowed.
* Inheritance not required.

### Method Overriding (Runtime)

Child provides its own implementation of a parent method. JVM decides at runtime.

```java
Player p = new Batsman();
p.play();   // runs Batsman's play() — Batting
```

* Same method name, same parameters, different implementation.
* Inheritance required.

| Overloading | Overriding |
| ----------- | ---------- |
| Same Class | Parent & Child |
| Different Parameters | Same Parameters |
| Inheritance Not Required | Inheritance Required |
| Compile-Time | Run-Time |

---

## Class Relationships

```text
Inheritance  → IS-A
Association  → Connected To
Aggregation  → Weak HAS-A
Composition  → Strong HAS-A
```

* **Association** → two classes connected and interact; both exist independently (Teacher ↔ Student).
* **Aggregation** → weak HAS-A, child survives without parent (College HAS-A Student).
* **Composition** → strong HAS-A, child dies with parent (Car HAS-A Engine).

| Relationship | Meaning | Child Exists Without Parent? |
| ------------ | ------- | ---------------------------- |
| Association | Connected To | Yes |
| Aggregation | Weak HAS-A | Yes |
| Composition | Strong HAS-A | No |

**Trick:** Can the child exist alone? Yes → Aggregation. No → Composition.

---

## Memory: Stack, Heap, GC

```text
Stack → Variables, References, Method Calls
Heap  → Objects, Arrays
```

```java
Student s = new Student();
// object → Heap, reference s → Stack (stores address)
```

* **Reference** → stores the address of an object, not the object itself.
* `Student s2 = s1;` → 1 object, 2 references (both point to same object).

| Stack | Heap |
| ----- | ---- |
| Variables, References | Objects, Arrays |
| Faster Access | Larger Memory |
| Automatic Cleanup | Garbage Collector |

### Object Lifecycle

```text
Create → Use → Unreachable → Garbage Collected
```

* `s = null;` → object becomes unreachable → eligible for GC.
* **Garbage Collection** → automatic removal of unreachable objects. Cannot force, only request via `System.gc()`.
* Accessing a null reference → `NullPointerException`.

---

## Object-Oriented Design Concepts

### SOLID Principles

```text
S → Single Responsibility Principle
O → Open/Closed Principle
L → Liskov Substitution Principle
I → Interface Segregation Principle
D → Dependency Inversion Principle
```

* **SRP** → A class should have only one reason to change. One class = one job.
  ```java
  // Bad: Invoice class handles both calculation AND printing
  // Good: InvoiceCalculator + InvoicePrinter — separate classes
  ```

* **OCP** → Open for extension, closed for modification. Add new behavior by adding new code, not changing existing code.
  ```java
  // Add new shapes by creating new classes, not editing existing ones
  ```

* **LSP** → A child class must be substitutable for its parent without breaking behavior.
  ```java
  Player p = new Batsman();   // Batsman should behave correctly as a Player
  ```

* **ISP** → Don't force a class to implement methods it doesn't need. Prefer small, specific interfaces over one large one.
  ```java
  // Bad: one fat Athlete interface with swim(), run(), shoot()
  // Good: Swimmer, Runner, Shooter — separate interfaces
  ```

* **DIP** → Depend on abstractions, not concrete classes.
  ```java
  // Bad: Engine e = new PetrolEngine();
  // Good: Engine e = new ElectricEngine();  // Engine is an interface
  ```

---

### Cohesion and Coupling

```text
High Cohesion  → good (class does one focused thing)
Low Coupling   → good (classes depend on each other as little as possible)
```

* **Cohesion** → how focused a class is. A `Player` class that only manages player data = high cohesion.
* **Coupling** → how much one class depends on another. Tightly coupled classes break together; loosely coupled classes change independently.

**Goal → High Cohesion + Low Coupling**

---

### Design Principles (DRY, KISS, YAGNI)

* **DRY** (Don't Repeat Yourself) → one piece of logic in one place; avoid copy-paste code.
* **KISS** (Keep It Simple, Stupid) → prefer the simplest solution that works.
* **YAGNI** (You Aren't Gonna Need It) → don't add features until they are actually needed.

---

### Common Design Patterns

Patterns are reusable solutions to common design problems.

```text
Creational  → how objects are created
Structural  → how classes/objects are composed
Behavioral  → how objects communicate
```

**Creational**

* **Singleton** → only one instance of a class exists.
  ```java
  class Config {
      private static Config instance;
      private Config() {}
      public static Config getInstance() {
          if (instance == null) instance = new Config();
          return instance;
      }
  }
  ```

* **Factory** → a method/class creates objects without exposing creation logic.
  ```java
  Player p = PlayerFactory.create("batsman");
  ```

**Structural**

* **Decorator** → add behavior to an object at runtime without changing its class.
* **Adapter** → makes incompatible interfaces work together (like a power plug adapter).

**Behavioral**

* **Observer** → one object (subject) notifies many objects (observers) when its state changes. Example: event listeners.
* **Strategy** → define a family of algorithms, encapsulate each one, and make them interchangeable at runtime.
  ```java
  // SortStrategy can be BubbleSort or QuickSort — swap without changing the calling code
  ```

---



* **Class** → blueprint used to create objects.
* **Object** → instance of a class with data and behavior.
* **Constructor** → special member auto-called to initialize an object.
* **Encapsulation** → wrap data + methods, restrict direct access.
* **Abstraction** → hide implementation, show essential functionality.
* **Inheritance** → one class acquires properties/methods of another.
* **Polymorphism** → object takes multiple forms.
* **Overloading** → same name, different parameters (compile-time).
* **Overriding** → new implementation in child class (runtime).
* **Association** → connected classes that interact.
* **Aggregation** → weak HAS-A, child survives.
* **Composition** → strong HAS-A, child does not survive.
* **Stack** → stores variables, references, method calls.
* **Heap** → stores objects and arrays.
* **Reference** → stores address of an object.
* **Garbage Collection** → automatic removal of unreachable objects.
