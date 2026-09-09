---
title: Enterprise-Enabled Copilot Initiative
status: active
tags:
  - ai
  - copilot
  - initiative
---

# Enterprise-Enabled Copilot Initiative

This initiative organizes the work required to establish consistent, governed, usable AI-assisted development.

## Current driver diagram

A [Key Driver Diagram](https://www.ihi.org/library/tools/driver-diagram) helps organize ideas and identify the primary factors that contribute to the issue being improved.

<div align="left">
<sub><b>Intervention Status Legend</b></sub><br/>
<sub>🟦 In Progress &nbsp;&nbsp; 🟩 Completed &nbsp;&nbsp; 🟥 Delayed &nbsp;&nbsp; ⬜ Not Started</sub>
</div>

```mermaid
%%{init: {
  "theme": "base",
  "htmlLabels": true,
  "themeVariables": {
    "fontSize": "12px",
    "fontFamily": "Tahoma, Arial, sans-serif",
    "primaryTextColor": "#333333",
    "lineColor": "#7A7A7A"
  },
  "flowchart": {
    "nodeSpacing": 30,
    "rankSpacing": 100,
    "padding": 15
  }
}}%%

flowchart LR

%% --- Styles ---
classDef aim fill:#FFFFFF,stroke:#0077A3,stroke-width:2px,color:#333333;
classDef driver fill:#FFFFFF,stroke:#0077A3,stroke-width:1.5px,color:#333333;
classDef intervention fill:#FFFFFF,stroke:#0077A3,stroke-width:1.5px,color:#333333;

%% STATUS COLORS
classDef inprogress fill:#DCEBFF,stroke:#0077A3,stroke-width:1.5px,color:#333333;
classDef completed fill:#E6F3EA,stroke:#0077A3,stroke-width:1.5px,color:#333333;
classDef delayed fill:#FCE8E8,stroke:#0077A3,stroke-width:1.5px,color:#333333;
classDef notstarted fill:#F2F2F2,stroke:#0077A3,stroke-width:1.5px,color:#333333;

%% --- SMART AIM ---
subgraph SMART["Smart Aim"]
direction TB
SA["By December 2026, >=75% of new or updated analytics solutions will use enterprise-enabled GitHub Copilot with standardized, governed templates, data definitions, and approved repositories."]
end

%% --- DRIVERS ---
subgraph DRIVERS["Drivers"]
direction TB
KD1["Consistent and Effective Copilot Use for Analytics Development"]
KD2["Standardized Development Framework"]
KD3["Team Enablement and Confidence in Using Copilot"]
KD4["Reliable, Governed and High Quality Output"]
end

%% --- INTERVENTIONS ---
subgraph INTERVENTIONS["Interventions"]
direction TB
I1["Develop and implement a standardized set of SQL prompt instructions for GitHub Copilot that embed enterprise standards"]
I2["Build a standard analytics repository template (folders, naming conventions, documentation) that Copilot can reference"]
I3["Embed structured comments and guidance within templates to improve Copilot-generated outputs"]
I4["Get enterprise level access to Copilot"]
I5["Integrate data context into repositories to guide accurate query generation"]
I6["Create a consumable learning series on data governance and responsible Copilot usage"]
I7["Define standards for reviewing and validating Copilot-generated code"]
I8["Monitor adoption, usage patterns, and quality outcomes to continuously refine standards"]
end

%% --- Apply base styles ---
class SA aim;
class KD1,KD2,KD3,KD4 driver;

%% --- STATUS ASSIGNMENT ---
class I1 inprogress;
class I2 inprogress;
class I3 notstarted;
class I4 delayed;
class I5 inprogress;
class I6 notstarted;
class I7 notstarted;
class I8 notstarted;

%% --- Clean layout ---
style SMART fill:#FFFFFF,stroke:#FFFFFF,color:#0077A3
style DRIVERS fill:#FFFFFF,stroke:#FFFFFF,color:#0077A3
style INTERVENTIONS fill:#FFFFFF,stroke:#FFFFFF,color:#0077A3

%% --- Flow ---
SA --> KD1
SA --> KD2
SA --> KD3
SA --> KD4

KD1 --> I1
KD1 --> I3
KD1 --> I4
KD1 --> I5

KD2 --> I1
KD2 --> I2
KD2 --> I3
KD2 --> I5

KD3 --> I1
KD3 --> I4
KD3 --> I6
KD3 --> I8

KD4 --> I3
KD4 --> I5
KD4 --> I7
KD4 --> I8
```
