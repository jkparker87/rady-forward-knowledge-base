---
title: Product Design
tags:
  - product
  - ux
---

# Product Design

Data products should be designed around the **decision, action, and user**, not just the available data.

## Core artifacts

### User personas
Personas describe recurring user needs, behaviors, capabilities, and expectations.

### User stories
User stories connect a user's goal to the value the data product should provide.

### Acceptance criteria
Acceptance criteria make a story testable by defining required data logic and user experience.

## Design sequence

```mermaid
flowchart LR
    P["Persona"] --> N["Need / decision"]
    N --> S["User story"]
    S --> A["Acceptance criteria"]
    A --> D["Data product design"]
    D --> V["User validation"]
```
