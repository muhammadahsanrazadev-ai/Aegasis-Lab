---
name: review-generated-code
description: >-
  Reviews a proposal or a fresh edit against the approved decision log and the
  exercise brief. Use when the user asks to review, or before calling any
  approved implementation step done.
---

# Review before accepting

## If the foundation gate is closed

Application code is a finding, not progress. Say which file appeared and that it should not stay. Do not "finish" it.

## If a decision was approved and code followed

- [ ] The change matches that decision and does not sneak in the next decision.
- [ ] You can explain why the rejected alternative lost.
- [ ] The exercise brief is still satisfied: Flask resource classes, the two named endpoints, `contact-list`, `contact-details`.
- [ ] No banned UI kit or third-party table or pagination module.
- [ ] A business rule does not import the web framework or a database driver.
- [ ] Errors are visible. There is no empty catch.
- [ ] Assumptions sit in a source comment.
- [ ] The check for this step was run.

## Report

State the finding, the file or the decision, and the correction. Apply the correction only when the user has already approved that kind of edit. Do not invent a new pattern while fixing a review note.
