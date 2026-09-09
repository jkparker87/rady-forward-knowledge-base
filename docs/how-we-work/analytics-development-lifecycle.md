---
title: Analytics Development Lifecycle
status: active
tags:
  - workflow
  - development
  - validation
---

# Analytics Development Lifecycle

Analytics development should move through a repeatable lifecycle that makes the work understandable, testable, reviewable, and maintainable.

## 1. Define the need

Clarify the question the requester is trying to answer, the decision the output will support, the expected audience, and what a successful deliverable looks like.

Before building anything new:

- search for an existing data product or reusable component
- determine whether an existing solution can be extended
- identify the appropriate owner and source of truth

## 2. Design the solution

Define:

- intended grain
- required measures and dimensions
- inclusion and exclusion rules
- data sources
- refresh needs
- validation strategy
- output format
- reuse potential

## 3. Develop

Use approved repositories, naming standards, style guidance, and branching practices.

Code should be:

- readable
- deterministic
- documented
- version controlled
- designed for appropriate reuse

## 4. Validate

Validation should address both **technical correctness** and **business validity**.

Examples include:

- source-system reconciliation
- row-count and grain checks
- duplicate detection
- missingness checks
- boundary-condition checks
- stakeholder review against known cases
- comparison with trusted existing reports where appropriate

## 5. Peer review

Peer review should focus on:

- correctness
- readability
- maintainability
- performance
- adherence to standards
- reuse opportunities
- risks or assumptions

## 6. Release

Release only after the agreed acceptance criteria have been met and required approvals or deployment steps are complete.

## 7. Document and maintain

Documentation should explain:

- purpose
- owner
- intended use
- source systems
- assumptions
- limitations
- dependencies
- where the implementation lives

Implementation-specific deployment instructions should remain with the implementation repository or platform when possible.
