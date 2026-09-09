---
title: Historical Changes
description: How changing attributes and organizational structures affect historical
  analysis.
tags:
- Topic/History
kb:
  id: guide.historical-changes
  type: guide
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
---

# Historical changes

Data values that look descriptive can change over time:

- provider specialty
- department name
- service-line mapping
- patient demographics
- status classifications
- business rules

The analytical question determines whether you want the **current value** or the **value as of the historical event**.

## Example

If a department was renamed in 2025, a current-state dimension may show the new name for encounters from 2023. That can be desirable for current organizational reporting, but wrong for a historical “what did the organization look like then?” analysis.

Document whether curated dimensions are current-state or effective-dated.
