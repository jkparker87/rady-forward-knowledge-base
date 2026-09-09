---
title: Automation Patterns
status: draft
tags:
  - automation
  - github-actions
---

# Automation Patterns

Automation is most valuable when it removes repetitive enforcement or publishing work.

## High-value patterns

### Documentation build validation
Build the MkDocs site on every pull request and fail when navigation or required pages are broken.

### Metadata checks
Require fields such as owner, status, or review cycle for governed pages.

### Link validation
Detect broken internal links before merge.

### Site deployment
Publish the site automatically after approved changes merge to the default branch.

### Documentation generation
Generate or update human-readable documentation from stable technical metadata when the generated content can be reviewed before publication.

### Change summaries
Create release notes or summaries of changed standards and workflows.

## Principle

Automate **mechanical consistency**. Keep judgment-heavy decisions reviewable by people.
