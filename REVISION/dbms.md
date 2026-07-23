# DBMS Master Revision Notes

## DBMS and RDBMS

**DBMS (Database Management System)** → software that stores, manages, and retrieves data.

```text
User / Application
       ↓
     DBMS
       ↓
   Database (actual data on disk)
```

**RDBMS (Relational DBMS)** → stores data in **tables** (rows and columns) with relationships between them.

| DBMS | RDBMS |
| ---- | ----- |
| Stores data as files | Stores data as tables |
| No relationships | Tables related via keys |
| No SQL standard | Uses SQL |
| Example: file system | Example: MySQL, PostgreSQL, Oracle |

### Why DBMS over files?

* **Data Integrity** → enforce rules (no duplicate IDs, valid data types)
* **Concurrency** → multiple users access data safely at the same time
* **Security** → access control per user/role
* **ACID** → transactions are safe and reliable
* **Query Language** → powerful SQL instead of manual file parsing

---

## SQL Fundamentals

**SQL (Structured Query Language)** → language used to interact with an RDBMS.

### SQL Categories

```text
DDL → Data Definition Language   → structure of tables
DML → Data Manipulation Language → data inside tables
DQL → Data Query Language        → retrieve data
DCL → Data Control Language      → permissions
TCL → Transaction Control Language → transactions
```

| Category | Commands |
| -------- | -------- |
| DDL | CREATE, ALTER, DROP, TRUNCATE |
| DML | INSERT, UPDATE, DELETE |
| DQL | SELECT |
| DCL | GRANT, REVOKE |
| TCL | COMMIT, ROLLBACK, SAVEPOINT |

---

## Tables, Keys, and Relationships

### Table

A table stores data in **rows (records)** and **columns (attributes)**.

```sql
CREATE TABLE Student (
    id   INT,
    name VARCHAR(50),
    age  INT
);
```

### Keys

| Key | Definition |
| --- | ---------- |
| **Primary Key** | Uniquely identifies each row; NOT NULL, unique |
| **Foreign Key** | References the primary key of another table; links tables |
| **Candidate Key** | Any column(s) that could be a primary key |
| **Composite Key** | Primary key made of two or more columns |
| **Unique Key** | Enforces uniqueness but allows one NULL |
| **Super Key** | Any set of columns that uniquely identifies a row |

```sql
CREATE TABLE Orders (
    order_id   INT PRIMARY KEY,
    student_id INT,
    FOREIGN KEY (student_id) REFERENCES Student(id)
);
```

### Relationships

| Type | Meaning | Example |
| ---- | ------- | ------- |
| One-to-One | One row in A → one row in B | Person ↔ Passport |
| One-to-Many | One row in A → many rows in B | Student → Orders |
| Many-to-Many | Many in A ↔ many in B | Students ↔ Courses (via junction table) |

**Junction Table** → resolves many-to-many using two foreign keys.

```sql
CREATE TABLE Enrollment (
    student_id INT,
    course_id  INT,
    PRIMARY KEY (student_id, course_id)
);
```

---

## CRUD Operations

**CRUD** → Create, Read, Update, Delete — the four basic data operations.

### CREATE — INSERT

```sql
INSERT INTO Student (id, name, age)
VALUES (1, 'Alice', 20);
```

### READ — SELECT

```sql
SELECT * FROM Student;
SELECT name, age FROM Student WHERE age > 18;
```

### UPDATE

```sql
UPDATE Student
SET age = 21
WHERE id = 1;
```

### DELETE

```sql
DELETE FROM Student WHERE id = 1;
```

### TRUNCATE vs DELETE vs DROP

| Command | What it does | Rollback? |
| ------- | ------------ | --------- |
| DELETE | Remove specific rows (DML) | Yes |
| TRUNCATE | Remove all rows, keep structure (DDL) | No |
| DROP | Remove entire table including structure | No |

---

## SQL Joins

Joins combine rows from two or more tables based on a related column.

```text
INNER JOIN  → only matching rows from both tables
LEFT JOIN   → all rows from left + matching from right (NULL if no match)
RIGHT JOIN  → all rows from right + matching from left (NULL if no match)
FULL JOIN   → all rows from both; NULL where no match
CROSS JOIN  → every row from A combined with every row from B (cartesian product)
SELF JOIN   → table joined with itself
```

### Example Tables

```text
Student: id, name        Orders: order_id, student_id, item
1, Alice                 101, 1, Book
2, Bob                   102, 3, Pen
3, Charlie
```

### INNER JOIN

Returns rows where both tables have a match.

```sql
SELECT Student.name, Orders.item
FROM Student
INNER JOIN Orders ON Student.id = Orders.student_id;
-- Result: Alice-Book (Bob and Charlie have no orders, excluded)
```

### LEFT JOIN

All rows from left table; NULL for right if no match.

```sql
SELECT Student.name, Orders.item
FROM Student
LEFT JOIN Orders ON Student.id = Orders.student_id;
-- Result: Alice-Book, Bob-NULL, Charlie-Pen
```

### FULL OUTER JOIN

All rows from both; NULL where no match on either side.

```sql
SELECT Student.name, Orders.item
FROM Student
FULL OUTER JOIN Orders ON Student.id = Orders.student_id;
```

### Visual Summary

```text
INNER  →  [  A ∩ B  ]
LEFT   →  [ A  +  A∩B ]
RIGHT  →  [    A∩B + B ]
FULL   →  [ A  +  A∩B + B ]
```

---

## Aggregations and Queries

### Aggregate Functions

Operate on a set of rows and return a single value.

| Function | Purpose |
| -------- | ------- |
| COUNT() | Number of rows |
| SUM() | Total of a column |
| AVG() | Average of a column |
| MAX() | Largest value |
| MIN() | Smallest value |

```sql
SELECT COUNT(*) FROM Student;
SELECT AVG(age) FROM Student;
SELECT MAX(age), MIN(age) FROM Student;
```

### GROUP BY

Groups rows with the same value, then applies aggregate per group.

```sql
SELECT department, COUNT(*) AS total
FROM Employee
GROUP BY department;
```

### HAVING

Filters **after** GROUP BY (WHERE filters before grouping).

```sql
SELECT department, COUNT(*) AS total
FROM Employee
GROUP BY department
HAVING COUNT(*) > 5;
```

```text
WHERE  → filters rows before grouping
HAVING → filters groups after grouping
```

### ORDER BY

```sql
SELECT name, age FROM Student ORDER BY age DESC;
```

### LIMIT / OFFSET

```sql
SELECT * FROM Student LIMIT 10 OFFSET 20;  -- rows 21-30
```

### SQL Query Execution Order

```text
FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

### Subqueries

A query inside another query.

```sql
SELECT name FROM Student
WHERE id IN (SELECT student_id FROM Orders WHERE item = 'Book');
```

---

## Normalization

Normalization organizes tables to **reduce redundancy** and **improve data integrity**.

```text
Redundancy → same data stored in multiple places → update anomaly, insert anomaly, delete anomaly
```

### Normal Forms

**1NF (First Normal Form)**
* Each column has atomic (indivisible) values.
* No repeating groups or arrays in a column.

```text
Bad:  Student(id, name, subjects)  → subjects = "Math, Science"
Good: separate rows for each subject
```

**2NF (Second Normal Form)**
* Must be in 1NF.
* No **partial dependency** → every non-key column must depend on the **whole** primary key (matters for composite keys).

```text
Bad:  OrderItem(order_id, product_id, product_name)
      product_name depends only on product_id, not the full key
Good: move product_name to a Product table
```

**3NF (Third Normal Form)**
* Must be in 2NF.
* No **transitive dependency** → non-key column should not depend on another non-key column.

```text
Bad:  Employee(emp_id, dept_id, dept_name)
      dept_name depends on dept_id, not emp_id
Good: move dept_name to a Department table
```

**BCNF (Boyce-Codd Normal Form)**
* Stricter version of 3NF.
* For every functional dependency X → Y, X must be a superkey.

### Summary

| Normal Form | Removes |
| ----------- | ------- |
| 1NF | Non-atomic values, repeating groups |
| 2NF | Partial dependencies |
| 3NF | Transitive dependencies |
| BCNF | All functional dependency anomalies |

**Goal → 3NF is usually enough for most real-world databases.**

---

## Indexing

An **index** is a data structure that speeds up data retrieval — like a book's index instead of reading every page.

```text
Without index → full table scan (O(n))
With index    → fast lookup (O(log n))
```

### How it works

The DB maintains a separate sorted structure (usually a B-Tree) on the indexed column, storing column value → row location.

```sql
CREATE INDEX idx_name ON Student(name);
```

### Types of Indexes

| Type | Description |
| ---- | ----------- |
| **Primary Index** | Auto-created on primary key |
| **Unique Index** | Enforces uniqueness + fast lookup |
| **Composite Index** | Index on multiple columns |
| **Full-Text Index** | For searching text content |

### Tradeoffs

| Pros | Cons |
| ---- | ---- |
| Faster SELECT queries | Slower INSERT / UPDATE / DELETE |
| Efficient ORDER BY, WHERE | Extra disk space |
| Good for frequently filtered columns | Too many indexes = overhead |

**Index on columns you filter, sort, or join on often. Avoid indexing columns that change frequently.**

---

## Transactions and ACID Properties

A **transaction** is a sequence of operations treated as a single unit — either all succeed or all fail.

```sql
BEGIN;
    UPDATE Account SET balance = balance - 500 WHERE id = 1;
    UPDATE Account SET balance = balance + 500 WHERE id = 2;
COMMIT;
-- if anything fails → ROLLBACK, both updates undone
```

### ACID Properties

**A — Atomicity**
All operations in a transaction complete, or none do. No partial updates.

```text
Transfer ₹500: debit A AND credit B → both happen or neither
```

**C — Consistency**
A transaction brings the database from one valid state to another. All rules and constraints are maintained.

```text
Total money before = total money after transfer
```

**I — Isolation**
Concurrent transactions do not interfere with each other. Each transaction sees a consistent snapshot.

```text
T1 and T2 run simultaneously → T1 cannot see T2's uncommitted changes
```

**D — Durability**
Once a transaction is committed, it is permanent — even if the system crashes.

```text
COMMIT → data written to disk, survives restart
```

### Transaction Control Commands

```sql
BEGIN;          -- start transaction
COMMIT;         -- save all changes permanently
ROLLBACK;       -- undo all changes since BEGIN
SAVEPOINT sp1;  -- mark a point to rollback to
ROLLBACK TO sp1;
```

### Isolation Problems (when isolation is weak)

| Problem | Description |
| ------- | ----------- |
| **Dirty Read** | Read uncommitted data from another transaction |
| **Non-Repeatable Read** | Same row read twice gives different values (another tx updated it) |
| **Phantom Read** | Same query returns different rows (another tx inserted/deleted) |

### Isolation Levels

| Level | Dirty Read | Non-Repeatable | Phantom |
| ----- | ---------- | -------------- | ------- |
| Read Uncommitted | ✅ possible | ✅ possible | ✅ possible |
| Read Committed | ❌ | ✅ possible | ✅ possible |
| Repeatable Read | ❌ | ❌ | ✅ possible |
| Serializable | ❌ | ❌ | ❌ |

**Higher isolation = safer but slower. Serializable = fully safe, most overhead.**

---

## MongoDB vs MySQL — When to Use Which

**MySQL** = RDBMS, stores data in **tables** with a fixed schema. **MongoDB** = NoSQL (document store), stores data as flexible **JSON-like documents**.

```text
MySQL   → tables, rows, columns, fixed schema
MongoDB → collections, documents, flexible schema
```

### Structure Comparison

| MySQL (SQL) | MongoDB (NoSQL) |
| ----------- | ---------------- |
| Database | Database |
| Table | Collection |
| Row | Document |
| Column | Field |
| Primary Key | `_id` |
| JOIN | Embedding / `$lookup` |

```sql
-- MySQL row
SELECT * FROM Student WHERE id = 1;
```

```js
// MongoDB document
db.students.findOne({ _id: 1 })
// { _id: 1, name: "Alice", age: 20, hobbies: ["chess", "reading"] }
```

### Schema

```text
MySQL   → schema defined upfront, every row must match (rigid)
MongoDB → schema-less, each document can have different fields (flexible)
```

* MySQL → good when data structure is stable and well-known in advance.
* MongoDB → good when data is evolving, varied, or nested/hierarchical.

### Relationships

```text
MySQL   → normalized, related via foreign keys + JOINs
MongoDB → denormalized, related data often embedded in one document
```

```js
// MongoDB — embed instead of join
{
  _id: 1,
  name: "Alice",
  orders: [
    { item: "Book", price: 200 },
    { item: "Pen",  price: 20 }
  ]
}
```

### ACID & Consistency

| MySQL | MongoDB |
| ----- | ------- |
| Full ACID across multi-row/table transactions | ACID at single-document level (multi-document transactions supported but costlier) |
| Strong consistency by default | Tunable consistency (can favor availability) |

### Scaling

```text
MySQL   → scales vertically (bigger server); horizontal scaling (sharding) is harder
MongoDB → built for horizontal scaling (sharding) across many servers
```

### When to use MySQL

* Data is structured, relational, and unlikely to change shape (e.g., banking, ERP, inventory).
* Strong ACID transactions across multiple tables are required (e.g., financial transfers).
* Complex queries with JOINs, aggregations across many related tables.
* Reporting / BI tools that expect SQL.

### When to use MongoDB

* Data is unstructured or evolving (e.g., product catalogs with varying attributes, user-generated content).
* Need to scale horizontally across many servers (huge write/read volume).
* Data is naturally hierarchical/nested (e.g., a single "profile" document with nested arrays).
* Rapid development where schema changes frequently (startups, prototypes).
* Read-heavy workloads where embedding avoids expensive JOINs.

### Summary Table

| Need | Choice |
| ---- | ------ |
| Strict schema + relationships | MySQL |
| Multi-table ACID transactions | MySQL |
| Flexible/evolving schema | MongoDB |
| Massive horizontal scale | MongoDB |
| Nested/hierarchical data | MongoDB |
| Heavy JOIN-based reporting | MySQL |

**Trick:** MySQL = filing cabinet with labeled folders (fixed structure). MongoDB = a box where each item can be wrapped differently (flexible structure).

---

## One-Line Definitions

* **DBMS** → software to store, manage, and retrieve data.
* **RDBMS** → DBMS that stores data in related tables.
* **SQL** → language to interact with a relational database.
* **DDL** → defines structure (CREATE, ALTER, DROP).
* **DML** → manipulates data (INSERT, UPDATE, DELETE).
* **Primary Key** → uniquely identifies a row; not null.
* **Foreign Key** → references primary key of another table.
* **INNER JOIN** → returns only matching rows from both tables.
* **LEFT JOIN** → all rows from left, matching from right (NULL if none).
* **GROUP BY** → group rows by a column for aggregation.
* **HAVING** → filter groups after GROUP BY.
* **Normalization** → organize tables to remove redundancy.
* **1NF** → atomic values, no repeating groups.
* **2NF** → no partial dependency on composite key.
* **3NF** → no transitive dependency between non-key columns.
* **Index** → data structure for fast row lookup.
* **Transaction** → group of operations that succeed or fail together.
* **Atomicity** → all or nothing.
* **Consistency** → valid state before and after transaction.
* **Isolation** → transactions don't interfere with each other.
* **Durability** → committed data survives crashes.
* **Dirty Read** → reading another transaction's uncommitted data.
* **Serializable** → highest isolation; transactions run as if sequential.
* **NoSQL** → non-relational database (e.g., MongoDB); flexible schema, document/key-value/graph based.
* **Document** → MongoDB's equivalent of a row; a JSON-like record with a `_id`.
* **Embedding** → storing related data inside one document instead of joining tables.
* **Sharding** → splitting data across multiple servers for horizontal scaling.
