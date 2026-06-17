# OOP Day 6 Notes

# Relationships Between Classes

Until now, we learned:

```text
Inheritance
=
IS-A Relationship
```

Example:

```text
Dog IS A Animal

Batsman IS A Player
```

Today we learn:

```text
Association
Aggregation
Composition

=
HAS-A Relationship
```

Examples:

```text
College HAS-A Students

Company HAS-A Employees

Car HAS-A Engine
```

---

# Association

## What is Association?

Association is a relationship where two classes are connected and can interact with each other.

### Example

```text
Teacher ↔ Student

Doctor ↔ Patient

Player ↔ Team
```

Both objects can exist independently.

---

## Key Point

```text
Both objects can exist without each other.
```

Example:

```text
Team removed
→ Player still exists

Player leaves
→ Team still exists
```

---

## Interview Definition

> Association is a relationship where two classes are connected and interact with each other.

---

# Aggregation

## What is Aggregation?

Aggregation is a weak HAS-A relationship.

The child object can exist independently of the parent object.

### Example

```text
College HAS-A Student
```

If College is removed:

```text
Student still exists
```

Student can join another college.

---

## More Examples

```text
Company HAS-A Employee

Library HAS-A Books

Tournament HAS-A Teams
```

Destroy Parent:

```text
Child survives
```

---

## Key Point

```text
Parent and Child have independent lifecycles.
```

---

## Interview Definition

> Aggregation is a HAS-A relationship where the child object can exist independently of the parent.

---

# Composition

## What is Composition?

Composition is a strong HAS-A relationship.

The child object cannot exist without the parent.

### Example

```text
Car HAS-A Engine
```

If Car is destroyed:

```text
Engine is also destroyed
```

---

## More Examples

```text
Human HAS-A Heart

House HAS-A Room

Computer HAS-A Motherboard
```

Destroy Parent:

```text
Child also gets destroyed
```

---

## Key Point

```text
Parent and Child have dependent lifecycles.
```

---

## Interview Definition

> Composition is a HAS-A relationship where the child object's lifecycle depends on the parent.

---

# Aggregation vs Composition

## Aggregation

```text
College HAS-A Student
```

Remove College:

```text
Student survives
```

Independent lifecycle.

---

## Composition

```text
Car HAS-A Engine
```

Remove Car:

```text
Engine destroyed
```

Dependent lifecycle.

---

# Easiest Memory Trick

Ask yourself:

## Can the Child Exist Alone?

### YES

```text
Aggregation
```

Examples:

```text
Student without College

Employee without Company

Player without Team
```

---

### NO

```text
Composition
```

Examples:

```text
Heart without Human

Engine without Car

Room without House
```

---

# Association vs Aggregation vs Composition

| Relationship | Meaning      | Child Exists Without Parent? |
| ------------ | ------------ | ---------------------------- |
| Association  | Connected To | Yes                          |
| Aggregation  | Weak HAS-A   | Yes                          |
| Composition  | Strong HAS-A | No                           |

---

# Inheritance vs Aggregation vs Composition

## Inheritance

```text
Dog IS A Animal
```

Relationship:

```text
IS-A
```

---

## Aggregation

```text
College HAS-A Student
```

Relationship:

```text
Weak HAS-A
```

---

## Composition

```text
Car HAS-A Engine
```

Relationship:

```text
Strong HAS-A
```

---

# Interview Examples

### Association

```text
Teacher ↔ Student

Doctor ↔ Patient
```

---

### Aggregation

```text
College HAS-A Student

Company HAS-A Employee

Tournament HAS-A Team
```

---

### Composition

```text
Car HAS-A Engine

Human HAS-A Heart

House HAS-A Room
```

---

# Quick Revision

```text
Inheritance
=
IS-A
```

```text
Dog IS A Animal
```

---

```text
Association
=
Connected Relationship
```

```text
Teacher ↔ Student
```

---

```text
Aggregation
=
Weak HAS-A
```

```text
College HAS-A Student
```

Student survives.

---

```text
Composition
=
Strong HAS-A
```

```text
Car HAS-A Engine
```

Engine does not survive.

---

# Formula to Remember

```text
Inheritance
=
IS-A

Association
=
Connected To

Aggregation
=
Weak HAS-A
+
Child Survives

Composition
=
Strong HAS-A
+
Child Does Not Survive
```
