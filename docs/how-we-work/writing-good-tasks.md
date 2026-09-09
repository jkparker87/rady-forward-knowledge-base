---
title: Writing Good Tasks
status: active
---

## What Makes a Good vs. Bad Task?

As we continue to mature how we manage work on our GitHub Kanban board, one of the most important habits we can build is writing **clear, actionable issues**. A well-written issue doesn’t just document work—it enables better collaboration, faster execution, and higher-quality outputs.

We’ve standardized on the **General Task** issue template, which includes three required sections:

- **Background and Purpose**
- **Explain the Task**
- **Desired Output**

## ✅ What a Good Issue Looks Like

A strong issue answers three key questions:

1. Why are we doing this? (Context)
2. What exactly needs to be done? (Execution plan)
3. What does success look like? (Deliverable)

### Example of a Good Issue

**Background and Purpose**  
The MPF leadership team has requested a breakdown of no-show rates by clinic location to identify areas where appointment adherence may be an issue. This will be used to inform targeted interventions by clinic managers.

**Explain the Task**  
- Pull appointment data for all ambulatory clinics for the past 3 months
- Identify completed vs. no-show appointments using the appropriate appointment status field
- Calculate no-show rate by clinic location
- Summarize findings and highlight any clinics with notably high no-show rates 

**Desired Output**  
An R markdown report that includes:
- No-show counts and rates by clinic location
- Supporting appointment volume for context
- Brief written summary (1–2 paragraphs) highlighting key findings and any notable trends 

## 🚫 What a Bad Issue Looks Like

A bad issue lacks context and justification for the work and/or does not define what "done" looks like.

### Example of a Bad Issue

**Background and Purpose**  
MPF No-show data

**Explain the Task**  
Pull no show rates

**Desired Output**  
Excel

### What’s Missing
- No context (Who needs this? Why?)
- No clarity on scope (Which units? What timeframe?)
- No direction (What analysis?)
- No definition of “done”

## 🤷‍♂️ A Common “In-Between” Example

**Background and Purpose**  
Leadership wants to better understand ED volume trends.

**Explain the Task**  
Pull ED visit data and create a report.

**Desired Output**  
Dashboard or report.

### What’s Missing?
- Still too vague
- Leaves too many decisions to the assignee
- Results in inconsistent outputs

## 🗝️ Key Principles for Writing Strong Issues

### 1. Be Specific (but not bloated)
Instead of saying (not specific):
> *Pull appointments data*

Don't be overly verbose:
> *Pull `pat_id`, `pat_mrn_id`, `appt_dttm`, `contact_date`, `month_begin_dt`, `appt_prc_id`, `prc_name`, `prov_id`, `prov_name`, `department_id`, `department_name`, `dep_specialty`, `division_grouping` from `f_sched_appt`, `clarity_dep` for MPF departments and where the contact date is between 1/1/2025 and 12/31/2025*

An appropriate level of detail would be:
> *Pull daily completed visits for the last 12 months by clinic location (Main, Escondido, Encinitas, Oceanside, Murrieta)*

### 2. Think in Terms of Weekly Deliverables
Avoid creating issues that represent entire projects.

**Bad**: Something that requires multiple smaller tasks represented as a single task
-  Build access Qlik app

**Better**: Define each task required to complete the overall project
-  Create SQL stored procedure for access data mart (task 1)
-  Document access data mart tech specs (task 2)
-  Develop summary sheet/landing page with core access KPI's (task 3)
-  Develop block utilization page with block utilization drill down charts by specialty & provider (task 4)

### 3. Define the Output Clearly
Ask yourself:
> *If I completed this task perfectly, what would I hand to the requestor?*

### 4. Make It Transferable
A good issue should allow someone else to pick it up with minimal confusion.

## 🔄️ Real-World Workflow: Analysis is Iterative
A common pattern in analytics work:
1. An analyst completes a task and delivers the requested output
2. The analyst meets with the requestor to review findings
3. The findings prompt new questions, refinements, or follow-up analysis

This is completely normal—analysis is inherently iterative. Answering one question often uncovers new areas of interest, data quality considerations, requests for deeper segmentation, or additional context

### How We Should Handle This
- Treat the original issue as complete once the initial request has been delivered
- Capture any new or refined requests as new GitHub issues
- Link the new issue to the original for context (e.g., “Follow-up to #123”)

### Why This Matters
- Keeps each task clearly scoped and measurable
- Prevents issues from staying “Active” indefinitely
- Creates a transparent record of how analysis evolves over time
- Makes it easier to prioritize and manage follow-up work

## 🗝️ Key Mindset

Finishing a task doesn’t mean the work is over—it means we’ve answered that specific question. In analytics, that answer is often just the starting point for the next one.

A well-written GitHub issue is a **contract for execution**.

The better we get at writing issues:
- The faster we move  
- The less confusion we have  
- The more consistent our outputs become  

