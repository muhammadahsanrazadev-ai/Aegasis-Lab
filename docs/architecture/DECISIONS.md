# Architecture decision log

**Status: no technical design is approved.** Application code stays out of the repo until the user approves the decision that covers it.

Approved entries below are process rules the user stated. Proposed entries are not decisions. Do not implement them.

## Approved — process (user, 4 Nov 2026)

- Cleanup of the unapproved draft comes before any new design is treated as real.
- Frontend and backend will be designed separately, with one defined way they meet. That shape is not chosen yet.
- Patterns are picked only after a purpose is stated. One responsibility does not get two patterns.
- Decisions are discussed, then approved, then written here as approved. One concern at a time.
- An approved decision changes only with a stated impact and a new approval.
- No database or operational data is deleted, reset, or modified without an explicit approval. This repo has no database. The cleanup did not touch one.

## Withdrawn — not a decision

A draft app was written before this process: Flask resources, an in-memory store, an Angular scaffold, and `PLAN.md`. The user rejected that start. Those files are removed. Nothing in that draft is approved, including Flask-RESTX, the repository class, the JSON fields, and the screen behavior beyond the brief.

## Proposed — not approved

### P1. What "deep architecture" means in this project

**Purpose.** Give every later folder and pattern one rule for dependencies, so a change in storage or HTTP does not rewrite the contact rules. This is separation of concerns and dependency inversion, sized for two endpoints and one screen (KISS).

**Proposal.** Four responsibilities, dependencies in one direction only:

1. Domain holds the contact and email rules. It imports no framework and no database driver.
2. Application holds the use-cases. It uses the domain and a port (an interface). It does not import Flask, Angular, or a driver.
3. A port is the small interface the application owns. An adapter implements it. The application does not import the adapter.
4. Delivery is the Flask resource or the Angular component. It calls the application and does not contain the business rule.

**Alternative rejected by this proposal, pending the user's call.** A single module that loads data, applies rules, and writes the HTTP body. It is shorter, and it makes the rule untestable without the framework. A larger set of rings (CQRS, an event bus, a use-case class per read) adds a second structure for the same two reads.

**Not in this proposal.** Folder names, package choice, JSON fields, Figma regions, auth, and persistence. Those stay on the open list.

## Next

Wait for approval, rejection, or a change to P1. Do not open P2 in the same step.
