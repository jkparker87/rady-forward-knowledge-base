---
title: User Stories & Acceptance Criteria
status: active
---

# User Story Framework

## Overview

A user story is an informal description of one or more features of a data product, written from the perspective of the end user.

User stories should focus on the **value derived from data** rather than the technical implementation. They help guide development efforts and ensure data products remain aligned with the needs of their intended users.

# User Story Format

Every user story should follow the following template:

> **As a [user], I want to [goal], so that [reason].**

This structure captures:

- **Who** is using the product
- **What** they need to do
- **Why** it provides value

# Components of a User Story

## Who

The **Who** identifies the user or role performing the function.

User stories should be written with a specific persona in mind. The scope and detail of the story should align with both the user's role and their level of data literacy.

| Persona | Typical Focus | Key Data Needs | Story Detail Level |
|----------|----------|----------|----------|
| **Executive** | Strategic, financial, regulatory, compliance | High-level KPIs, multiple levels of time aggregation, drill-down by organizational area | Broad, value-driven, outcome-focused |
| **Director** | Operational performance, resource allocation, quality improvement | Trend analysis, target comparisons, department comparisons | Goal-oriented, focused on decisions |
| **Manager** | Day-to-day operations, process adherence | Near real-time information, detailed staff-level data | Tactical and action-oriented |
| **Data Practitioner / Explorer** | Ad hoc analysis, investigation, research | Raw data access, flexible data models | Technical and function-oriented |

## What

The **What** describes the action, feature, or capability the user needs.

### Examples

- I want to view OR block utilization by service
- I want to filter readmission rates by discharge provider
- I want to analyze appointment no-show rates by week
- I want to export a list of inpatient discharges
- I want to compare department performance against organizational targets

## Why

The **Why** is the most important part of the user story.

It explains the business value of the feature and helps prioritize development efforts.

### Examples

- So that I can understand which services are effectively utilizing operating room capacity
- So that I can identify physicians who may need quality improvement coaching
- So that I can determine whether interventions are reducing appointment no-show rates
- So that I can submit required data to regulatory agencies

# User Story Examples

## Executive

> As an **Executive (Chief Operating Officer)**, I want to **view a quarterly summary of operating room utilization rates compared to peer hospitals** so that I can **determine whether investment in additional OR capacity or scheduling optimization is needed**.

## Director

> As a **Director of Emergency Medicine**, I want to **analyze average throughput time for admitted patients by time of day** so that I can **adjust staffing schedules to reduce bottlenecks**.

## Manager

> As a **Clinic Manager**, I want to **view a weekly list of encounters that remain open more than 14 days after the encounter date** so that I can **follow up with staff to ensure documentation and charges are completed promptly**.

## Data Practitioner

> As a **Data Analyst**, I want to **export filtered subsets of inpatient discharges** so that I can **submit supporting data to regulatory agencies**.



# Acceptance Criteria

Acceptance criteria transform a high-level user story into a clear, testable, and actionable requirement.

A user story should not be considered complete until all acceptance criteria have been met.

Acceptance criteria generally fall into two categories:

1. **Data & Logic Accuracy**
2. **Visualization & User Experience (UX)**


# Data & Logic Accuracy

This section ensures that measures, dimensions, filters, and calculations accurately represent the intended business process.

## Areas to Define

### Data Source

Identify:

- Where the data originates
- What the data represents
- Refresh frequency
- Ownership and governance

### Calculation Logic

Document:

- Measure definitions
- Numerators and denominators
- Aggregation methods
- Rounding rules
- Display formatting

### Exclusions

Document:

- Excluded populations
- Excluded encounter types
- Excluded facilities
- Timeframe restrictions
- Operational exceptions

# Visualization & User Experience (UX)

This section defines how information is presented and how users interact with it.

The goal is to ensure the data is intuitive, actionable, and aligned with user needs.

## Areas to Define

### Interactivity

Examples:

- Filters
- Drill-down capabilities
- Alternate dimensions
- Alternate measures
- Export functionality

### Visual Indicators

Examples:

- Target lines
- Threshold alerts
- Exception highlighting
- Conditional formatting
- Trend indicators

### Labels & Tooltips

Examples:

- KPI definitions
- Measure descriptions
- Data source explanations
- Calculation details
- Hover-over help text

# User Story Example with Acceptance Criteria

## User Story

> As a **Clinic Manager**, I want to **view a weekly list of patients who no-showed or same-day canceled appointments during the previous week** so that I can **assign staff to follow up and reschedule those patients**.

---

## Acceptance Criteria

### Data & Logic Accuracy

**Encounter Status**

Include encounters with:

- Status = "No Show"
- Status = "Canceled"

**Cancellation Logic**

- Cancellation date must equal appointment date

**Exclusions**

Exclude patients who:

- Completed a subsequent appointment after the no-show/cancellation
- Already have a future appointment scheduled

---

### Visualization & User Experience

**Filtering**

The list must be filterable by department or clinic location.

**Data Table Columns**

The table should include:

- Patient MRN
- Patient Name
- Primary Guardian Name
- Primary Guardian Phone Number
- Appointment Date/Time
- Appointment Status
- Visit Type
- Provider

**Sorting**

- Sort by Appointment Date/Time ascending

**Exporting**

- Export to Excel/CSV must be supported

**Workflow Support**

- Output should be easily shared with designated follow-up staff members.

# Best Practices

✅ Focus on value, not implementation

✅ Keep stories user-centered

✅ Make stories measurable and testable

✅ Tie every visualization to a decision or action

✅ Define acceptance criteria before development begins

✅ Ensure data definitions and calculation logic are documented

✅ Design for the intended persona and literacy level

# Quick Reference

### Template

> As a **[user]**, I want to **[goal]** so that **[reason]**.

### Questions to Ask

1. Who is the user?
2. What decision are they trying to make?
3. What action do they need to perform?
4. Why does this information matter?
5. How will they know they have succeeded?
6. What acceptance criteria must be met?
