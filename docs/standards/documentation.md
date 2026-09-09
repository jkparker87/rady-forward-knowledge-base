---
title: Documentation Standard
status: draft
tags:
  - documentation
  - governance
---

# Documentation Standard

Documentation should preserve the knowledge required to **understand, use, maintain, and govern** an analytical asset.

## Minimum fields for maintained pages

- purpose
- intended audience
- owner
- status
- source of truth
- related systems or assets
- assumptions or limitations
- review cycle

## Documentation by artifact type

| Artifact | Rady Forward should contain | Canonical implementation belongs in |
|---|---|---|
| Data product | Purpose, use, audience, interpretation, links | Databricks / BI platform / Alation |
| SQL standard | Human-readable standard and examples | Rady Forward + version-controlled Markdown |
| Pipeline | High-level purpose and flow | Databricks / GitHub |
| Dashboard | Intended decisions, audience, usage guidance | BI platform |
| AI workflow | Purpose, guardrails, user instructions | Rady Forward; technical config in GitHub |
| System | Role, boundaries, upstream/downstream context | Rady Forward; technical config in platform docs |

## Avoid duplicate documentation

When another platform owns a fact, link to it rather than copying it.

A duplicated fact becomes a maintenance problem as soon as one copy changes.
