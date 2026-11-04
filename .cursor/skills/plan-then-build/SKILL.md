---
name: plan-then-build
description: >-
  Defines state A and state B and stops for approval before application code.
  Use when the user discusses a feature, a fix, live coding, or the contacts
  exercise. Do not use it to start coding while the foundation gate is closed.
---

# Plan, then wait, then build

## 1. Define the ends

- **A** — what is true in the repo right now.
- **B** — what a reviewer can observe when this step is done.

If B needs an interpretation, say so. Do not bury it in code that was not approved.

## 2. Check the gate

Read `docs/architecture/DECISIONS.md`.

- The decision this step depends on is missing or still marked proposed: write the proposal, name one rejected alternative, and stop. Do not add application files.
- The decision is marked approved: build only that slice.

## 3. Pick a path

Two real options. One recommendation. One sentence on why the other loses. Reject a path that adds a second pattern for the same responsibility, or that uses a library the exercise brief forbids.

## 4. After approval

One behavior, one check, then the next behavior. Read the diff before the check. Do not recreate the withdrawn draft unless the user approved that design.
