---
title: Data Assets
description: Human-centered documentation for curated SQL objects that serve as recommended
  analytical entry points.
tags:
- Data Asset/All
kb:
  id: collection.data-assets
  type: collection
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
---


# Data assets

This section documents **high-value curated analytical entry points**, not every physical database object.

A useful asset page explains:

- what the object represents
- its grain
- primary keys and relationship keys
- major derived fields
- refresh timing
- source systems
- common join paths
- known limitations
- business concepts and metrics it supports

--8<-- "includes/snippets/alation-boundary.md"

## What should live here?

Prefer objects that analysts are expected to use directly or that embody reusable organizational logic. Low-level staging objects, transient technical objects, and exhaustive schema inventories are better handled by the technical catalog.
