---
title: Source of Truth
description: How to think about authoritative definitions and curated entry points
  without oversimplifying.
tags:
- Governance/Trust
kb:
  id: governance.source-of-truth
  type: governance
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
---

# Source of truth

“Source of truth” should not mean “the table closest to the source system.”

An authoritative analytical source is the source that best matches:

- the business question
- the intended grain
- the approved definition
- the required history
- the expected refresh cadence

A raw source table can be operationally authoritative while a curated analytical table is the correct source for a recurring metric.

--8<-- "includes/snippets/source-of-truth-note.md"

As Alation matures, catalog certification should be treated as the technical discovery signal. This site should explain **why** an asset is appropriate, not duplicate every catalog control.
