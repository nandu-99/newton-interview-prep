# Git Master Revision Notes

## Introduction to Git

**Git** is a distributed version control system (VCS) — it tracks changes to files over time so multiple people can collaborate without overwriting each other's work.

```text
Working Directory → files you edit
Staging Area      → files marked ready to commit (git add)
Local Repository  → committed history (git commit)
Remote Repository → shared copy (GitHub, GitLab)
```

```text
git add    → Working Dir  → Staging Area
git commit → Staging Area → Local Repo
git push   → Local Repo   → Remote Repo
git pull   → Remote Repo  → Local Repo
```

### Why Git?

* **History** → every change is tracked, can revert to any point.
* **Collaboration** → multiple people work on the same codebase without conflict.
* **Branching** → isolate work-in-progress from stable code.
* **Distributed** → every clone has the full history (unlike centralized VCS like SVN).

---

## Basic Workflow

```bash
git init                     # start a new repo
git clone <url>               # copy a remote repo locally
git status                    # see changed/staged files
git add file.txt               # stage a file
git add .                      # stage everything
git commit -m "message"       # save staged changes to history
git push origin main          # send commits to remote
git pull origin main          # fetch + merge remote changes
```

```text
git fetch → downloads remote changes, does NOT merge
git pull  → fetch + merge in one step
```

---

## Branching

A **branch** is an independent line of development — a movable pointer to a commit.

```text
main  → o---o---o---o
                 \
feature           o---o   (isolated work, doesn't affect main)
```

```bash
git branch                    # list branches
git branch feature-x          # create a branch
git checkout feature-x        # switch to it
git checkout -b feature-x     # create + switch in one step
git switch feature-x          # modern alternative to checkout
git branch -d feature-x       # delete a merged branch
```

### Why branch?

* Work on a new feature/bugfix without breaking `main`.
* Multiple people work in parallel on separate branches.
* `main`/`master` stays stable and deployable at all times.

```text
main       → always stable, deployable
feature/*  → new work, isolated
hotfix/*   → urgent production fixes
```

---

## Merge vs Rebase

Both **combine changes from one branch into another** — but they rewrite history differently.

### Merge

Creates a **new merge commit** that joins two histories. Original commits are untouched.

```bash
git checkout main
git merge feature-x
```

```text
main     → A---B---C-------M   (M = merge commit)
                \         /
feature-x        D---E---/
```

* Preserves full, true history (including branch structure).
* Non-destructive — safe for shared/public branches.
* History can get cluttered with many merge commits.

### Rebase

**Replays** your branch's commits on top of another branch — rewrites commit history, no merge commit.

```bash
git checkout feature-x
git rebase main
```

```text
Before:
main     → A---B---C
feature-x → A---D---E   (branched from A)

After rebase:
main     → A---B---C
feature-x →         D'---E'   (D, E replayed on top of C)
```

* Produces a **clean, linear history**.
* Rewrites commit hashes (D → D', E → E') — **never rebase commits already pushed/shared** with others.
* Easier to read `git log`, but loses the record of when branches diverged.

### Merge vs Rebase — Summary

| Merge | Rebase |
| ----- | ------ |
| Creates a merge commit | Replays commits, no merge commit |
| Preserves true history | Linear, rewritten history |
| Safe on shared branches | Risky on shared/pushed branches |
| History shows when branches diverged | History looks like work happened sequentially |
| Can get cluttered | Clean and easy to follow |

**Golden rule:** *Never rebase a branch others are already working on / that's already pushed publicly.* Rebase local/private branches before opening a PR; merge to bring shared branches together.

**Trick:** Merge = stapling two timelines together (keeps both intact). Rebase = tearing off your pages and re-gluing them at the end of the other book (rewrites your pages).

### Merge Conflicts

Happen when the same lines are changed differently in both branches — Git can't auto-merge.

```text
<<<<<<< HEAD
your changes (current branch)
=======
their changes (incoming branch)
>>>>>>> feature-x
```

```bash
# resolve manually, then:
git add <resolved-file>
git commit          # for a merge conflict
git rebase --continue  # for a rebase conflict
```

---

## Pull Requests (PRs)

A **Pull Request** is a request to merge changes from one branch (usually a feature branch) into another (usually `main`) — reviewed before merging. (GitLab calls it a **Merge Request**.)

```text
1. Create feature branch
2. Commit + push changes
3. Open PR: feature-x → main
4. Team reviews, comments, requests changes
5. CI runs tests/checks
6. Approve → merge into main
```

```bash
git checkout -b feature-x
# ... make changes, commit ...
git push origin feature-x
# open PR on GitHub/GitLab from feature-x → main
```

### Why PRs?

* **Code review** → catch bugs, enforce standards before merging.
* **CI/CD gate** → tests must pass before merge is allowed.
* **Discussion** → comments, suggestions, context recorded against the change.
* **Audit trail** → clear record of what changed, why, and who approved it.

### PR Merge Strategies

| Strategy | Effect |
| -------- | ------ |
| **Merge commit** | Keeps all commits + adds a merge commit |
| **Squash and merge** | Combines all PR commits into one clean commit on `main` |
| **Rebase and merge** | Replays PR commits onto `main`, linear history, no merge commit |

```text
Squash → best for messy WIP commit history ("fix typo", "oops", "wip")
Merge commit → best when individual commits are meaningful and worth preserving
Rebase → best for a clean linear history without a merge commit
```

### Good PR Practices

* Small, focused PRs — easier and faster to review.
* Descriptive title + summary of *why*, not just *what*.
* Link related issue/ticket.
* Keep the branch up to date with `main` (merge or rebase) before requesting review.
* Resolve conflicts before requesting review, not after.

---

## Undoing Changes

| Command | Effect |
| ------- | ------ |
| `git checkout -- file` | Discard unstaged changes to a file |
| `git restore file` | Modern alternative to discard unstaged changes |
| `git reset HEAD file` | Unstage a file (keep changes) |
| `git reset --soft HEAD~1` | Undo last commit, keep changes staged |
| `git reset --mixed HEAD~1` | Undo last commit, keep changes unstaged (default) |
| `git reset --hard HEAD~1` | Undo last commit, **discard changes entirely** |
| `git revert <commit>` | Create a new commit that undoes a previous commit (safe on shared history) |

```text
reset  → moves the branch pointer, rewrites history (dangerous if pushed)
revert → adds a new commit that undoes changes, preserves history (safe if pushed)
```

**Rule of thumb:** use `revert` on shared/pushed commits, `reset` only on local/unpushed commits.

---

## One-Line Definitions

* **Git** → distributed version control system tracking file history.
* **Repository** → a project tracked by Git (local or remote).
* **Commit** → a saved snapshot of staged changes.
* **Branch** → an independent, movable line of development.
* **Merge** → combine two branches via a new merge commit, preserving history.
* **Rebase** → replay commits from one branch onto another, rewriting history for a linear log.
* **Merge Conflict** → Git can't auto-resolve overlapping changes; needs manual fix.
* **Pull Request (PR)** → request to review and merge one branch into another.
* **Squash and Merge** → combine all PR commits into a single commit on the target branch.
* **Fast-Forward Merge** → merge with no divergent commits; branch pointer just moves forward.
* **Fetch** → download remote changes without merging.
* **Pull** → fetch + merge in one step.
* **Reset** → move branch pointer backward, optionally discarding changes; rewrites history.
* **Revert** → new commit that undoes a previous commit; safe on shared history.
* **HEAD** → pointer to the current commit/branch you're on.
* **Detached HEAD** → checked out to a specific commit, not a branch.
