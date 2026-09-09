---
title: Task Management
status: active
---

This guide defines how we manage work on our GitHub Kanban board. The goal is to improve clarity, accountability, and delivery of high-quality data products.

---

#  Status Definitions

## 🗂️ Backlog
**Purpose:** Capture all known work not yet ready for execution. Content in this bucket might have _some or all_ of the following characteristics:
- Vague, incomplete, or exploratory  
- Not yet fully scoped  
- No commitment to timeline  
- Includes ideas, requests, documentation, future enhancements, etc.

**Move to Next Up when...**
- Problem/request is clearly defined  
- Acceptance criteria are documented (what is the actual thing you need to do)
- Priority is established 

## ⏭️ Next Up
**Purpose:** Work that is ready to start. This is the only bucket that team members should pull work from. Content in this bucket should meet _all_ of the following characteristics:
- Clear problem statement/purpose
- Acceptance criteria are documented (an actionable plan is defined - the "Explain the task" and "Desired Product/Output" section of the task template)
- Dependencies identified  
- Task has been scoped (estimated work effort)

**Move to Active when...**
- You have actively commenced work on the task

## 🚧 Active
**Purpose:** Tasks that are currently in progress. Content in this bucket should meet _all_ of the following characteristics: 
- Task has an assigned owner
- Actively being worked on **RIGHT NOW**
- Updated regularly through commits and or notes. Active tasks should have evidence of progress nearly _every day_ they are active.

**If a task is not immediately being worked on, it should be moved to On Hold or Next Up as appropriate.**

## ⏸️ On Hold
**Purpose:** Work that cannot proceed due to some block. Blocks could include approvals, stakeholder feedback, migrations (e.g. Qlik app moves), etc. Content in this bucket should...
- Have a **Hold Reason** documented  
- The next step(s) should be indicated in the notes of the task

Once the block has been removed, the task should be moved back into Active or Completed as appropriate.

## ✅ Complete
**Purpose:** The task, as scoped, has been completed.

**Definition of Done:**
- The defined task/acceptance criteria have been met  
- Output validated  
- Deliverable has been generated

---

# Task Sizing & Granularity

Tasks represent **small, deliverable units**, not entire projects. They should generally meet the following guidelines:
- Represent something that can be accomplished in ≤ 1 week of work  
- Single owner. Multiple people should very rarely work on the exact same task, generally each person has their own scope of responsibility.
- There should be a clear deliverable  and reviewable outcome (how do we know the task is done or accomplished the intended objective)

## Things to Avoid
- Tasks lasting > 1 week
- Vague task names
- No clear definition of “done”  



# 🚧 Work in Progress (WIP) Discipline

> **Active is what you are working on RIGHT NOW (not everything you’ve started).**

## 🚫 What We Don’t Do
- Do not place 5–10 tasks in Active  
- Do not use Active as a “working list”  
- Do not leave idle tasks in Active  

## ✅ What We Do Instead

Each team member should typically have:

- **1–2 Active tasks (primary focus)**
- Occasionally 3 if truly necessary

Everything else should remain in:
- **Next Up** (ready but not started)
- **On Hold** (blocked)

## Why This Matters

Too many Active tasks leads to:
- Context switching (reduced efficiency)
- Slower delivery
- Poor visibility into true progress
- Work appearing “stuck”

## How to Decide What Belongs in Active

A task belongs in Active ONLY if:
- You are actively working on it **today or tomorrow**
- It is your current priority
- You are making measurable progress

If not → move it out to either on hold or next up.

## Managing Overflow

If you have too many tasks:
1. Keep only current work in Active  
2. Move the rest to Next Up  
3. Reprioritize if needed  

## 🚨 Things to Watch For

- Tasks sitting in Active for days without updates  
- More than 3 Active tasks per person  
- “I’m working on everything”  

# Team Operating Principles

- **Start Less, Finish More**. Focus on completing work before starting new work.
- **Next Up is Sacred**. Only ready work belongs there.
- **Make Blockers Visible**. Use On Hold correctly.
- **Done = Delivered Value**. Completion means usable output.

# 🔄 Handling Iterative Work (Analysis, Feedback, Revisions)

Analytical work is naturally iterative. However, **iterations should still be represented as discrete tasks**, not one long-running item that stays in *Active* indefinitely.

## 🎯 Core Principle

> Each task should represent a **complete, reviewable unit of work**—even if additional iterations are expected.

## Scenario
A stakeholder requests an analysis of inpatient census trends. The task is completed as it was initially scoped, but upon meeting with the stakeholder, they request additional changes and modifications. The following explains this flow and how it would be managed in our GitHub Kanban board.

### Step 1: Initial Task Creation/Scoping

Using the **General Data Task** task template, the task has been defined as follows and is in the "Next Up" bucket.

**Task Title**
Analysis of Inpatient Census Trends

**Background and purpose**
We need to better understand recent inpatient census trends to support operational planning. Leadership is specifically interested in identifying patterns over time and any notable increases or decreases in volume.

**Explain the task**
- Pull inpatient census data by day for the past 24 months from SQL data mart
- Analyze overall trends over time
- Identify any notable patterns or anomalies
- Summarize findings in a simple, stakeholder-friendly format

**What is the desired product or output?**
The final output should be an R markdown document summarizing inpatient trends that includes the following:
- A time series visualization of daily census
- Narrative summary of key insights

The output should be published through Posit Connect and shared with the requestor.

---

### Step 2: Task Completion

Once the team member completes the analysis and shares results with the stakeholder the will ➡️ move the task to **Complete**

---

### Step 3: Feedback Loop

After review, the stakeholder may request:
- Breakdowns (e.g., by unit)  
- Additional analysis (e.g., seasonality)  
- New formats (e.g., dashboard)  

---

### Step 4: Create Follow-Up Task(s)

Instead of reopening the original task:

Create **new task(s)**:

Examples:
- “Enhance census analysis with unit-level breakdown”
- “Add seasonal decomposition to census trends”
- “Convert analysis into dashboard prototype”

➡️ Place in **Backlog** or **Next Up**

## Takeaways

### 🚫 What We Avoid

- Keeping the original task in Active for weeks  
- Reopening the same task repeatedly  
- Continuously expanding scope within a single task 
- Treating recurring work as one ongoing task
- Leaving “routine” work undefined or undocumented 

### ✅ What This Looks Like

| Task | Status |
|------|--------|
| Initial census analysis | Complete |
| Unit-level breakdown enhancement | Next Up |
| Dashboard version | Backlog |

### 🎯 Why This Matters

- Preserves clear definitions of done  
- Improves visibility into progress  
- Prevents long-running Active tasks  
- Encourages incremental delivery  

### 👍 Rule of Thumb

> If new work is required after feedback, it is **a new task—not a continuation of the old one**.

If feedback is minor (e.g. typos, colors, labels, etc.) and can be completed within 1 day, then it may be appropriate to move back to an Active status. Otherwise, create a new task.

### 💡 Consider

Consider framing tasks as “Deliver version 1 of X”. This will:
- Set the expectation of iteration  
- Encourage task completion  
- Support clean follow-up work  

# 🔁 Handling Recurring Tasks

Recurring work (e.g., weekly reports, monthly extracts, routine data refreshes) should be managed in a way that preserves visibility, accountability, and task-level clarity.

## 🎯 Core Principle
Recurring work should be tracked as repeatable, clearly defined tasks — not one long-running task or a task that is perpetually active.

## 🏷️ Identification
- Prefix with: **Recurring - [Task Name]**
- Add the time period of the recurrence to the end of the name (Ex. "Recurring - NRC Comments Report - July 2026")
- Use the **Recurring Task** field to define frequency (Daily, Weekly, Monthly, Quarterly)

## 🧩 Definition
Recurring tasks should include the same level of detail as other tasks and should include:
- Background and Purpose  
- Explain the Task  
- Desired Output  
- Estimated Effort  

## 🚧 Execution Process
Recurring tasks should live in the backlog and can be copied for each recurring instance.

1. Duplicate the task from the backlog
2. Move new instance to Next Up when you need to integrate into your next sprint
3. Move to Active once you begin work
4. Assign owner, start date, target date  
5. Complete and close task  

## 🚫 Avoid
- Keeping recurring tasks permanently active  
- Reusing the same task repeatedly  
- Skipping task definition  

## ✅ Example

| Task | Status |
|------|--------|
| Recurring – Weekly ED Volume Extract (Template) | Backlog |
| Weekly ED Volume Extract (Week of May 5) | Complete |
| Weekly ED Volume Extract (Week of May 12) | Active |

## 👍 Rule of Thumb
A recurring task is a template. The work is tracked through individual task instances.
