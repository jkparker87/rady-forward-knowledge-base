---
title: Null, Zero & Unknown
description: Why missing, zero, unknown, not applicable, and not yet observed must
  not be treated as the same thing.
tags:
- Topic/Missing Data
kb:
  id: guide.null-zero
  type: guide
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
---

# Null, zero, and unknown

These values are not interchangeable.

- **Zero**: the quantity is known and equals zero.
- **Null / missing**: no value is stored.
- **Unknown**: the workflow explicitly records that the value is not known.
- **Not applicable**: the concept does not apply.
- **Not yet observed**: the value may become available later.

Converting all missing values to zero is often analytically destructive because it turns uncertainty into a measured absence.

## Example

A missing cancellation reason does not mean “no reason.” It may mean the user did not enter one, the workflow did not require one, or the source did not carry the field.
