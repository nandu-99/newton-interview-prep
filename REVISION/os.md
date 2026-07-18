# OS Master Revision Notes

## Introduction to Operating Systems (OS)

An **Operating System** is system software that acts as an intermediary between the user and hardware. It manages hardware resources and provides services to programs.

```text
User / Applications
      ↓
Operating System
      ↓
Hardware (CPU, RAM, Disk, I/O)
```

### What does an OS do?

* **Process Management** → create, schedule, terminate processes
* **Memory Management** → allocate and free RAM
* **File System** → organize and access data on disk
* **I/O Management** → manage devices (keyboard, disk, network)
* **Security & Access Control** → protect resources

### Types of OS

| Type | Description | Example |
| ---- | ----------- | ------- |
| Batch | Jobs grouped and processed together | Early mainframes |
| Time-Sharing | Multiple users share CPU via time slices | Unix |
| Real-Time | Strict time guarantees | Embedded systems |
| Distributed | Multiple machines work as one | Cloud OS |
| Multitasking | Multiple processes run concurrently | Windows, Linux |

### Kernel

The **core of the OS** — always running in memory. Manages CPU, memory, and devices directly.

```text
Kernel Mode  → full hardware access (OS code)
User Mode    → restricted access (application code)
```

* A **system call** is how user programs ask the kernel to do privileged operations (read file, allocate memory).

---

## Process

A **program in execution**. A program is passive (just code on disk); a process is active (loaded in memory, running).

```text
Program  → passive, code on disk
Process  → active, program running in memory
```

Each process gets its own memory space:

```text
Text    → compiled code
Data    → global / static variables
Heap    → dynamic memory (new, malloc)
Stack   → function calls, local variables
```

### Process States

```text
New       → being created
Ready     → waiting for CPU
Running   → executing on CPU
Waiting   → waiting for I/O or event
Terminated→ finished
```

```text
New → Ready → Running → Terminated
        ↑        ↓
      Waiting ← (I/O)
```

### PCB (Process Control Block)

Data structure the OS keeps for each process. Stores everything needed to manage and resume it.

* Process ID (PID)
* Process state
* Program counter (next instruction)
* CPU registers
* Memory info
* I/O and open files

---

## Thread

A **lightweight unit of execution inside a process**. A process can have many threads that share the same memory.

```text
Process → own memory
Thread  → shares process memory, own stack + registers
```

Threads share: **code, data, heap, files.**
Threads have their own: **stack, registers, program counter.**

### Why Threads?

* Parallel work inside one process
* Faster than creating new processes
* Cheaper context switch
* Better resource sharing

```text
Multithreading → many threads run inside one process
```

---

## Process vs Thread

| Process | Thread |
| ------- | ------ |
| Own memory space | Shares process memory |
| Heavy | Lightweight |
| Slow creation | Fast creation |
| Costly context switch | Cheap context switch |
| Communication via IPC | Communication via shared memory |
| Crash isolated | One thread crash can kill process |

**Trick:** Process = separate house, Thread = rooms sharing the same house.

---

## Context Switching

Saving the state of one process/thread and loading the state of another so the CPU can switch between them.

```text
Save current state (PCB) → Load next state (PCB) → Resume
```

* Triggered by: time slice ends, interrupt, I/O wait, higher priority task.
* **Pure overhead** — no useful work happens during the switch.
* Thread switch is cheaper than process switch (shared memory, less to save).

---

## CPU Burst

Time a process spends **using the CPU** before it needs I/O.

```text
CPU Burst → CPU work
I/O Burst → waiting for I/O
```

* A process alternates: CPU burst → I/O burst → CPU burst...
* **CPU-bound** → long CPU bursts (calculations).
* **I/O-bound** → short CPU bursts, frequent I/O (reading files).
* Scheduling algorithms often use burst length to decide order.

---

## Scheduling — Key Terms

| Term | Meaning |
| ---- | ------- |
| Arrival Time (AT) | when process enters ready queue |
| Burst Time (BT) | CPU time needed |
| Completion Time (CT) | when process finishes |
| Turnaround Time (TAT) | CT − AT (total time in system) |
| Waiting Time (WT) | TAT − BT (time spent waiting) |
| Response Time (RT) | first CPU time − AT |

```text
Turnaround Time = Completion − Arrival
Waiting Time    = Turnaround − Burst
```

### Throughput

Number of processes **completed per unit time**. Higher = better.

```text
Throughput = processes completed / total time
```

### Goals of Scheduling

* Maximize: CPU utilization, throughput
* Minimize: waiting time, turnaround time, response time

### Preemptive vs Non-Preemptive

| Preemptive | Non-Preemptive |
| ---------- | -------------- |
| CPU can be taken away | Runs till finish/block |
| SRTF, RR, Priority(P) | FCFS, SJF |
| Better response | Simple, less overhead |

---

## 1. FCFS (First Come First Serve)

Runs processes in **order of arrival**. Non-preemptive.

```text
Queue → first in, first served
```

* Simple, fair by arrival.
* **Convoy Effect** → one long process blocks all short ones behind it.
* High average waiting time.

---

## 2. SJF (Shortest Job First)

Picks the process with the **smallest burst time**. Non-preemptive.

* Gives **minimum average waiting time** (optimal).
* Problem: need to know burst time in advance.
* **Starvation** → long jobs may wait forever if short jobs keep arriving.

---

## 3. SRTF (Shortest Remaining Time First)

**Preemptive version of SJF.** Picks the process with the smallest *remaining* burst.

* If a new process arrives with a shorter remaining time, it preempts the current one.
* Lower average waiting time than SJF.
* More context switches + starvation of long jobs.

---

## 4. RR (Round Robin)

Each process gets a fixed **time quantum**; after it expires, it goes to the back of the queue. Preemptive.

```text
P1 → P2 → P3 → P1 → P2 ... (each gets quantum)
```

* Fair — everyone gets a turn.
* Best **response time** → good for time-sharing systems.
* Quantum too large → behaves like FCFS.
* Quantum too small → too many context switches (overhead).

---

## 5. Priority Scheduling

Each process has a **priority**; CPU goes to the highest priority. Can be preemptive or non-preemptive.

* **Starvation** → low-priority processes may never run.
* **Aging** → gradually increase priority of waiting processes to fix starvation.

---

## 6. MLFQ (Multi-Level Feedback Queue)

Multiple queues with different priorities; processes **move between queues** based on behavior.

```text
Q0 → high priority, small quantum
Q1 → medium priority, larger quantum
Q2 → low priority (FCFS)
```

Rules:

* New process starts in the top queue.
* Uses full quantum → **demoted** (likely CPU-bound).
* Gives up CPU for I/O → **stays / promoted** (likely I/O-bound).
* Aging moves starved processes up.

* Favors short and I/O-bound jobs, still serves long jobs.
* Most flexible, adapts automatically. Used in real OSes.

---

## Scheduling Algorithms — Summary

| Algorithm | Preemptive | Basis | Problem |
| --------- | ---------- | ----- | ------- |
| FCFS | No | Arrival order | Convoy effect |
| SJF | No | Shortest burst | Starvation |
| SRTF | Yes | Shortest remaining | Starvation, overhead |
| RR | Yes | Time quantum | Quantum tuning |
| Priority | Both | Priority value | Starvation |
| MLFQ | Yes | Feedback / behavior | Complex to tune |

---

## Synchronization

When multiple threads/processes share data, simultaneous access can cause inconsistent results — this is a **race condition**.

```text
Race Condition → two threads read-modify-write the same data at the same time → wrong result
```

### Critical Section

A piece of code that accesses shared data. Only **one thread should be in it at a time**.

```text
Requirements:
1. Mutual Exclusion  → only one thread inside at a time
2. Progress          → if no one is inside, a waiting thread must be allowed in
3. Bounded Waiting   → a thread must not wait forever
```

### Mutex (Mutual Exclusion Lock)

A lock that only **one thread can hold at a time**. Others wait until it is released.

```java
mutex.lock();
// critical section — only one thread here at a time
mutex.unlock();
```

* Binary: locked or unlocked.
* The thread that locks it must unlock it.
* Prevents race conditions on shared data.

### Semaphore

A signaling mechanism using an **integer counter**. Controls how many threads can access a resource.

```text
wait(S)   → S-- ; if S < 0, block (P operation)
signal(S) → S++ ; wake a blocked thread (V operation)
```

* **Binary Semaphore (0 or 1)** → works like a mutex.
* **Counting Semaphore** → allows N threads simultaneously (e.g., 3 printers → S = 3).

| Mutex | Semaphore |
| ----- | --------- |
| Only locking thread can unlock | Any thread can signal |
| Binary only | Binary or counting |
| Ownership concept | No ownership |
| Protects critical section | Controls resource count |

### Deadlock vs Starvation vs Race Condition

| Problem | Cause |
| ------- | ----- |
| Race Condition | Uncontrolled concurrent access |
| Deadlock | Circular wait for locked resources |
| Starvation | Low-priority process never scheduled |

---

## Deadlocks

A **deadlock** occurs when two or more processes are waiting for each other to release resources — none can proceed.

```text
P1 holds R1, waits for R2
P2 holds R2, waits for R1
→ both wait forever
```

### 4 Necessary Conditions (Coffman Conditions)

All four must hold simultaneously for a deadlock to occur:

| Condition | Meaning |
| --------- | ------- |
| Mutual Exclusion | Resource held by only one process at a time |
| Hold and Wait | Process holds a resource while waiting for another |
| No Preemption | Resource cannot be forcibly taken away |
| Circular Wait | P1 waits for P2, P2 waits for P1 (cycle) |

**Break any one → deadlock cannot occur.**

### Deadlock Handling Strategies

**1. Prevention** → ensure at least one Coffman condition can never hold.
* No Hold & Wait → request all resources at once upfront.
* Allow Preemption → forcibly take resources if needed.
* Eliminate Circular Wait → assign a global order to resources, always request in order.

**2. Avoidance** → dynamically check before granting a resource if the system stays in a safe state.
* **Banker's Algorithm** → before allocating, simulate if remaining processes can still finish. Grant only if safe.

```text
Safe State → there exists a sequence where every process can finish
```

**3. Detection & Recovery** → allow deadlocks to happen, detect them, then recover.
* Detection: check for cycles in the resource allocation graph.
* Recovery: kill a process, or preempt and roll back resources.

**4. Ignorance (Ostrich Algorithm)** → pretend deadlocks don't happen. Used when they are rare and the cost of handling is high (e.g., Windows, Linux for some cases).

| Strategy | Approach | Cost |
| -------- | -------- | ---- |
| Prevention | Break Coffman conditions | Low performance |
| Avoidance | Banker's algorithm | Overhead per request |
| Detection | Detect cycles + recover | Recovery cost |
| Ignorance | Do nothing | Risk of deadlock |

---

## Memory Management

The OS manages RAM — deciding which process gets memory, how much, and where.

### Goals

* Allocate memory to processes
* Isolate processes (one process can't read another's memory)
* Maximize utilization, minimize waste

### Address Types

```text
Logical Address  → generated by CPU (what program sees)
Physical Address → actual location in RAM
```

**MMU (Memory Management Unit)** → hardware that translates logical → physical address.

### Contiguous Allocation

Each process gets one continuous block of RAM.

* **Fixed Partitioning** → RAM divided into fixed slots. Simple but causes **internal fragmentation** (wasted space inside a slot).
* **Dynamic Partitioning** → slots sized to process. Causes **external fragmentation** (free gaps too small to use).

```text
Internal Fragmentation → wasted space inside allocated block
External Fragmentation → free memory exists but scattered in small pieces
```

### Paging

Divide memory into fixed-size blocks:

```text
Physical RAM → frames (fixed size, e.g. 4KB)
Process      → pages (same size as frames)
```

* OS maps pages to frames using a **page table**.
* Eliminates external fragmentation.
* May cause internal fragmentation (last page may not be full).

### Segmentation

Divide process memory into logical segments (code, stack, heap) of variable size.

* More natural — matches how programs think about memory.
* Can cause external fragmentation.

### Virtual Memory

Allows a process to use **more memory than physically available** by storing some pages on disk.

```text
RAM (fast) + Disk (slow) = Virtual Memory space
```

* **Page Fault** → process accesses a page not in RAM → OS loads it from disk.
* **Swapping** → moving an entire process out of RAM to disk to free space.
* **Thrashing** → too many page faults; CPU spends more time swapping than executing.

### Page Replacement Algorithms

When RAM is full and a new page is needed, the OS must evict a page:

| Algorithm | Policy | Problem |
| --------- | ------ | ------- |
| FIFO | Evict oldest page | Belady's anomaly |
| LRU | Evict least recently used | Implementation overhead |
| Optimal | Evict page used farthest in future | Theoretical only |

**LRU is the most commonly used in practice.**

---



* **Process** → a program in execution.
* **Thread** → lightweight unit of execution sharing process memory.
* **PCB** → structure storing all info about a process.
* **Context Switch** → save one process state, load another's.
* **CPU Burst** → time a process uses the CPU before I/O.
* **Turnaround Time** → completion − arrival.
* **Waiting Time** → turnaround − burst.
* **Response Time** → first CPU access − arrival.
* **Throughput** → processes completed per unit time.
* **FCFS** → run in arrival order (non-preemptive).
* **SJF** → run shortest burst first (non-preemptive).
* **SRTF** → preemptive SJF, shortest remaining first.
* **RR** → fixed time quantum per process, cyclic.
* **Priority** → highest priority runs first.
* **MLFQ** → multiple queues, processes move by behavior.
* **Starvation** → a process never gets the CPU.
* **Aging** → raise priority of waiting processes to prevent starvation.
* **OS** → software that manages hardware and provides services to programs.
* **Kernel** → core of the OS, runs in privileged mode.
* **System Call** → how user programs request OS services.
* **Race Condition** → uncontrolled concurrent access leads to wrong results.
* **Critical Section** → code accessing shared data; needs mutual exclusion.
* **Mutex** → binary lock; only one thread enters critical section at a time.
* **Semaphore** → integer counter controlling access to a resource.
* **Deadlock** → circular wait where processes block each other forever.
* **Coffman Conditions** → mutual exclusion, hold & wait, no preemption, circular wait.
* **Banker's Algorithm** → avoidance algorithm; grants resources only if safe state remains.
* **Logical Address** → address generated by CPU (what the program sees).
* **Physical Address** → actual RAM location.
* **Paging** → divide memory into fixed-size pages/frames to avoid external fragmentation.
* **Virtual Memory** → use disk to extend RAM; allows programs larger than physical RAM.
* **Page Fault** → accessed page not in RAM; OS loads it from disk.
* **Thrashing** → too many page faults; system spends more time swapping than executing.
* **LRU** → evict the least recently used page when RAM is full.
