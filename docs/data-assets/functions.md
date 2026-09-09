---
title: Functions
description: How reusable SQL functions should be documented when they encode analytical
  logic.
tags:
- Data Asset/Function
kb:
  id: reference.functions
  type: reference
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
---


# Functions

Functions are appropriate when a calculation or transformation is reused across many queries and can be safely expressed as a deterministic interface.

Document:

- inputs and expected types
- returned value
- null behavior
- calendar / timezone assumptions
- edge cases
- performance considerations
- examples of intended use

A function that encodes business logic should link back to the concept or metric whose definition it implements.
