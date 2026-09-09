---
title: Choose the Right Date
description: How to select the timestamp that matches the business event being measured.
tags:
- Topic/Dates
kb:
  id: guide.dates
  type: guide
  status: approved
  render_connections: true
  review:
    last_reviewed: '2026-09-08'
---

# Choose the right date

Healthcare operational data contains many valid dates. The right one depends on the question.

| Question | Likely time basis |
| --- | --- |
| When was demand created? | order / referral / appointment creation |
| When was care expected? | scheduled service date |
| When did the patient arrive? | arrival / check-in |
| When did an inpatient stay begin? | defined admission timestamp |
| When did care end? | discharge / departure / completion |
| What occupied capacity on a day? | census snapshot date |

## Name the event, not just the field

Avoid documentation such as “use `DATE_1`.” Prefer “use the **scheduled appointment date** when grouping no-show outcomes by service period.”

Timezones, daylight-saving transitions, and date truncation can also matter when timestamps are stored differently across systems.
