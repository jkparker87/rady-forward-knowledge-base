---
title: Analytics Methods
status: draft
tags:
  - analytics
  - standardization
  - methods
---

# Analytics Methods

The analytics-methods framework is intended to improve the consistency, efficiency, reproducibility, and accessibility of analysis while preserving analytical judgment.

## Guiding principles

- Practical over perfect
- Consistency with flexibility
- Accessibility by design
- Continuous improvement

## Standardization targets

### Standardized and validated methods
Define recommended approaches for common descriptive, diagnostic, exploratory, and improvement-oriented analyses.

### Reusable analytical logic
Move stable, validated calculations into reusable functions, packages, templates, or curated datasets.

### Reproducible project structure
Use consistent project structures, dependencies, documentation, and version control.

### Guided analytics workflow
Structure work from business question through interpretation and decision-making rather than beginning with a tool or statistical method.

### Review and validation
Use peer review and validation mechanisms appropriate to the impact and complexity of the analysis.

## What should remain flexible

Standardization should not force:

- the same statistical method onto different questions
- the same visualization for different audiences
- unnecessary tooling complexity
- rigid workflows when the analytical context requires judgment

## Initial operating model

```mermaid
flowchart LR
    Q["Business question"] --> D["Define data & decision"]
    D --> M["Select method"]
    M --> V["Validate"]
    V --> I["Interpret"]
    I --> C["Communicate"]
    C --> A["Action / next question"]
```
