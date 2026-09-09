---
title: How We Work
tags:
  - workflow
---

# How We Work

This section describes the operating model for analytics work from initial request through delivery and maintenance.

## Core workflow

```mermaid
flowchart LR
    A["Understand the problem"] --> B["Scope the work"]
    B --> C["Design / reuse"]
    C --> D["Build"]
    D --> E["Validate"]
    E --> F["Peer review"]
    F --> G["Release"]
    G --> H["Document & maintain"]
```

## Core principles

- **Start with the business question.**
- **Reuse before rebuilding.**
- **Keep work small enough to deliver.**
- **Validate before release.**
- **Make review and documentation part of development.**
- **Finish work before starting excessive new work.**
- **Treat follow-up analysis as new, explicitly scoped work when scope materially changes.**
