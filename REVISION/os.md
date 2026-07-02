# OS Master Revision Notes

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

## One-Line Definitions

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
