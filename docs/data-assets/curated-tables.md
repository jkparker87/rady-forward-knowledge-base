---
title: Curated Tables
description: How curated analytical tables should be designed and documented.
tags:
- Data Asset/Curated Table
kb:
  id: reference.curated-tables
  type: reference
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
---


# Curated tables

Curated tables should provide a stable analytical grain and absorb recurring transformation logic.

A strong curated table usually has:

- a clearly stated row grain
- stable identifiers
- standardized dates and dimensions
- business-friendly derived fields
- explicit handling of status and history
- documented exclusions and limitations
- a predictable refresh pattern

Curated does not mean universally correct. The object should state which questions it is designed to support and which questions require another grain or source.
