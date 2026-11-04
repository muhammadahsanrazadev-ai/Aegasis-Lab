# Aegasis Lab

Architecture phase. Do not write the contacts application until the user approves the decision that covers that work.

## Source of truth

- Process gate: `.cursor/rules/foundation-gate.mdc`
- How to judge a design: `.cursor/rules/engineering-standards.mdc`
- What the exercise brief requires: `.cursor/rules/exercise-scope.mdc` and `.cursor/skills/contacts-dashboard/reference.md`
- What is actually approved: `docs/architecture/DECISIONS.md`

If an older note describes a Flask-RESTX app, an in-memory repository, or an Angular scaffold, that note is the withdrawn draft. It is not a decision.

## How to change the design

1. Read the decision log.
2. Propose one concern. Name the principle it serves and one alternative you are not taking.
3. Stop. The user approves, rejects, or edits it.
4. Only then mark it approved in the decision log.
5. Application code starts after that approval, and only for the approved slice.
