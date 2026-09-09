---
title: SQL Style Guide
status: active
---

# SQL Style Guide

## Overview

These guidelines define the standard SQL style for individuals and teams, including analytics, quality management, industrial engineering, research, and population health. A consistent, shared approach to SQL improves readability, eases peer review, and makes analytical work more portable and maintainable across projects, environments, and team members. While this guidance is written for internal use, it aligns with broadly accepted industry practices to promote clarity, reliability, and long-term supportability of code.

SQL should always be written with the understanding that it will be reused, reviewed, and relied upon by others. The goal is not only to produce correct results, but to ensure those results are understandable, reproducible, and maintainable over time.

A strong SQL standard improves collaboration, reduces errors, and ensures long-term sustainability of analytical work.

## Key Takeaways
- Prioritize readability over brevity.
- Always write explicit and deterministic logic.
- Use consistent naming and formatting standards.
- Treat SQL as a shared, long-term asset.

# General Concepts

## Details

These principles define the baseline expectations for all SQL developed for shared and production use.

SQL should be treated as a shared asset, not an individual artifact. Queries are frequently reused, modified, and incorporated into downstream reporting, dashboards, and data pipelines. As a result, clarity and consistency are more important than brevity or personal preference.

SQL is often used in:
- Cross-functional reporting
- Long-lived data marts and stored procedures
- Regulatory or audit-sensitive outputs

Poorly structured SQL introduces risk such as:
- Misinterpretation of business logic
- Incorrect joins leading to duplication or data loss
- Inconsistent outputs across teams
- Increased onboarding time for new analysts

These standards help ensure that any reviewer can quickly determine:
- What the query is doing
- Why the logic exists
- What assumptions are being made
- What the output represents

## Best Practice

- Use consistent and descriptive identifiers and names. Descriptive naming reduces ambiguity and helps reviewers understand the role of a table, column, or variable without needing additional explanation.
- Use quotes to alias column names. Quoted aliases are broadly recognized across SQL platforms and improve portability.
- Use `lower_snake_case` formatting for column names, table names, procedure names, file names, and related objects. This creates a predictable, readable naming pattern.
- Use uppercase for reserved keywords such as `WHERE`, `SELECT`, and `JOIN`. This visually separates SQL syntax from business-specific identifiers and improves scanability.
- Make judicious use of white space and indentation to make code easier to read. Readable formatting lowers the risk of logical mistakes and simplifies maintenance.
- When possible, use standard SQL functions instead of vendor-specific functions for portability. Standard functions reduce lock-in and make code easier to move across environments.
- Keep code succinct and devoid of redundant SQL. Unnecessary quoting, parentheses, or repeated conditions make queries harder to review and maintain.
- Include comments where necessary, especially when business logic or IDs would otherwise be unclear. Comments preserve intent over time.
- Join and filter data on indexes where possible to improve performance. Good query structure should support both readability and execution efficiency.
- Use temporary tables and CTEs to improve performance and readability where appropriate. Separating logical steps makes transformations easier to follow.
- Use a clear and explicit method of de-duplication. Methods such as `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)` make retained-record logic deterministic and reviewable.
- Be deliberate with `NULL` handling. Functions such as `COALESCE` and `ISNULL` should be used intentionally to avoid unintended row loss or incorrect results.
- Note that custom functions can and should be created and used to optimize and simplify code where appropriate. Reusable logic belongs in governed, reusable objects when justified.

## Avoid

- Avoid CamelCase unless referencing the Caboodle database. Inconsistent case patterns can be harder to scan quickly.
- Avoid writing code exclusively in lowercase or uppercase text. This reduces visual separation between syntax and data elements.
- Avoid assuming that others will know what the query is doing or is intended to accomplish. Hidden assumptions make code fragile and difficult to maintain.
- Avoid `SELECT *` in production code. Explicit column lists improve clarity, schema stability, and downstream reliability.
- Avoid `SELECT DISTINCT` as a method of deduplication. It often hides root-cause data issues rather than resolving them explicitly.
- Avoid implicit joins instead of listing tables in the `FROM` clause with explicit join types. Implicit joins reduce readability and increase the risk of incorrect conditions.

## Good Example

```sql
SELECT  a.id,
        b.name
FROM    table_a AS a
        INNER JOIN table_b AS b
        ON a.id = b.id;
```

## Bad Example

```sql
select * from table_a, table_b where table_a.id = table_b.id;
```

# Content Preface

## Details

Every SQL file should be prefaced with a comment box that includes the **Purpose**, **Author**, and **Requestor**. A standardized preface provides immediate context and reduces the need for a reviewer to infer intent from raw SQL.

A strong preface helps readers understand:
- What the query is intended to answer
- Why the data is needed
- Who originated the work
- Who requested the work

Revision history does not need to be maintained inside the query file when version control is already in place. Changes should be tracked through Git history and commit messages instead.

## Best Practice

- Include a standardized preface at the beginning of every SQL file. This ensures consistency across all shared analytical assets.
- Clearly describe the purpose in plain language. The purpose should be understandable even to someone who is not proficient in SQL.
- Include the original author. This identifies where the work originated and provides useful context for future updates.
- Include the requestor. This ties the SQL to the business question and helps preserve downstream context.
- Use the standard template consistently. A predictable structure reduces manual errors and makes files easier to review.

## Avoid

- Avoid omitting the preface. Missing context forces reviewers to infer intent from implementation details.
- Avoid vague purpose statements. A purpose that is too general is not useful for reviewers or future maintainers.
- Avoid including redundant revision history inside the SQL file when source control already captures changes.
- Avoid purpose statements that describe only the mechanics of the query without explaining the business question or target dataset.
- Avoid leaving out the requestor or author when the information is known. Ownership and context matter.

## Standard Preface Template

To ensure consistency across all SQL content, the following preface block should be included at the beginning of every SQL file. Users of the `analytics_performance_improvement` repository can utilize VS Code snippets to simplify this task. Typing `.preface` can automatically expand to the standardized comment-box template.

```sql
/*****************************************************************************************
PURPOSE:    This query identifies admissions to the Scripps Mercy NICU and includes
            information needed to identify encounters meeting certain criteria needed for
            CCS certification.
            CTE 'a' includes all of the admission and patient information.
            CTE 'b' includes all of the diagnoses for the admission.
            The main query combines the admission information of CTE 'a' and summarizes
            diagnosis information into a format more consumable to the requesting stakeholder.
AUTHOR:     Jacob Parker
REQUESTOR:  Kendall Sanderson (primary), Isabel Garcia
******************************************************************************************/
```

## Purpose

The **Purpose** statement should be clear enough so that anyone, including someone who is not proficient in SQL, can understand what the query does and what question the resulting dataset is intended to answer. It should provide a high-level overview without requiring interpretation of the implementation details.

### Good Example

```sql
/*****************************************************************************************
PURPOSE:    This query identifies admissions to the Scripps Mercy NICU and includes
            information needed to identify encounters meeting certain criteria
            needed for CCS certification.
            CTE 'a' includes all of the admission and patient information.
            CTE 'b' includes all of the diagnoses for the admission.
            The main query combines the admission information of CTE 'a' and
            summarizes diagnosis information into a format more consumable to
            the requesting stakeholder.
******************************************************************************************/
```

This example demonstrates good styling because:
1. It clearly explains the subset of admissions that are of interest.
2. It provides a reason for why the data is needed.
3. It explains, at a high level, what is happening in the query and CTEs.

### Bad Example

```sql
/*****************************************************************************************
PURPOSE:    Retrieve information about admissions
******************************************************************************************/
```

This example demonstrates bad styling because:
1. It does not explain how the data is intended to be used.
2. It does not provide enough specificity about the target data.
3. It does not help a reviewer distinguish between a broad query and a highly scoped one.

## Author

The **Author** field should indicate the original author of the query. If a query was written by a vendor, the vendor name should be included along with the specific individual if available. This field identifies where the work originated.

## Requestor

The **Requestor** field should contain the individual or individuals requesting the query. When there are multiple requestors, it can be helpful, though not required, to identify the primary stakeholder or requesting group.

# Variables

## Details

Variables are useful when defining objects of interest, particularly when the same value is referenced multiple times within a query. Declaring variables at the top of a query improves readability and makes updates easier because a change only needs to be made once.

In SQL Server, local variables can be created for different data types and assigned values that may change during execution.

## Best Practice

- Variables should use `lower_snake_case` naming, consistent with column and table naming conventions. Consistent naming improves readability and reduces confusion.
- Variables should be `DECLARE`d and `SET` on the same line using inline assignment whenever possible. This keeps code concise and reduces unnecessary separation of related logic.
- Date references should generally be declared and set with variables. This makes time windows easier to review and modify.
- Variables should be declared at the top of the query, before any CTEs or `SELECT` statements. Centralized declarations make parameters immediately visible.
- Always use the most specific and appropriate data type, such as `INT`, `DATE`, `VARCHAR(n)`, or `BIT`, rather than a generic type. Specific types reduce ambiguity and conversion errors.
- In cases such as stored procedures, variables may need to be set using dynamic data. In those situations, setting values in a separate statement is appropriate.

## Avoid

- Avoid declaring a variable and setting it on separate lines when inline assignment would suffice. This adds noise without adding clarity.
- Avoid hardcoding repeated date or identifier values throughout a query. Repetition increases maintenance burden and the likelihood of inconsistent updates.
- Avoid placing variable declarations deep in the query body. Hidden parameters are harder to review and troubleshoot.
- Avoid using overly generic or inappropriate data types. Poor type selection can create implicit conversion issues.
- Avoid using unclear variable names that do not communicate intent.

## Good Example

```sql
DECLARE @start_date DATE = '2026-02-25';
DECLARE @end_date DATE = '2026-02-26';
DECLARE @department_id1 INT = 01010100;
DECLARE @department_id2 INT = 01000010;

SELECT  pat_id,
        enc_date,
        dep_id
FROM    clarity.dbo.pat_enc
WHERE   enc_date BETWEEN @start_date AND @end_date
        AND dep_id IN (@department_id1,
                       @department_id2);
```

## Bad Example

```sql
DECLARE @start_date DATE
SET @start_date = '2026-02-25'
```

# Comments

## Details

Comments are required to ensure SQL code is understandable, maintainable, and reviewable across teams. They should provide context about **why** logic exists, not merely restate what the code is doing.

Well-written comments reduce onboarding time, prevent misinterpretation, and support long-term sustainability of analytical assets. They are especially useful when documenting:
- Business rules
- Filtering decisions
- Non-obvious joins
- System constraints or workarounds
- Assumptions, edge cases, and limitations

## Best Practice

- Use comments to explain why logic exists. Intent is often more important than the syntax itself.
- Include a comment block before every CTE, subquery, or major transformation step. This helps reviewers understand the purpose of each stage.
- Document assumptions, edge cases, and known limitations. Important caveats should not be hidden in implementation.
- Annotate ID-based filters with meaningful descriptions. Numeric codes without context are not self-explanatory.
- Keep comments clear, concise, and intentional. Good comments preserve context without cluttering the query.
- Update comments when modifying logic. Documentation should evolve with the code.

## Avoid

- Avoid comments that simply restate obvious SQL logic. They add noise without improving understanding.
- Avoid leaving outdated or incorrect comments in code. Stale documentation is more harmful than no documentation.
- Avoid over-commenting trivial or self-explanatory logic. Excessive commentary can bury the information that matters.
- Avoid vague placeholders such as "fix this later" or "temporary" without context. These do not help future reviewers make decisions.
- Avoid embedding commented-out legacy code instead of removing it. Version control should preserve old code, not the SQL file itself.

## Standard Comment Block (for Sections)

Use comment blocks to clearly define major sections of logic.

## Good Example

```sql
DECLARE @start_date DATE = '2022-07-01';
DECLARE @end_date DATE = '2022-07-10';
DECLARE @enc_type NUMERIC = 76; -- EPT 30 = Telephone Encounters
DECLARE @appt_status NUMERIC = 2; -- EPT 7020 = Completed

/*******************************************************************************
The following query retrieves the date of the last completed telephone encounter
within the defined time period for each patient
*******************************************************************************/

WITH enc AS
(
    SELECT  appt.pat_id,
            CAST(MAX(appt.contact_date) AS DATE) "last_enc"
    FROM    f_sched_appt AS appt
            INNER JOIN pat_enc AS pe
            ON appt.pat_enc_csn_id = pe.pat_enc_csn_id
            AND pe.enc_type_c = @enc_type
    WHERE   appt.appt_status_c = @appt_status
            AND appt.contact_date >= @start_date
            AND appt.contact_date <= @end_date
    GROUP BY appt.pat_id
)

/*******************************************************************************
The following query retrieves patient information for patients with encounters
identified in CTE 'enc' and classifies patients into age groups based on their
age in years at the time of the encounter
*******************************************************************************/

SELECT  p.pat_mrn_id,
        CAST(p.birth_date AS DATE) "birth_date",
        enc.last_enc,
        DATEDIFF(YEAR, p.birth_date, enc.last_enc) "age_years",
        -- Classify patient into age groups based on age at the last encounter
        CASE
            WHEN DATEDIFF(YEAR, p.birth_date, enc.last_enc) < 2 THEN 'Infant'
            WHEN DATEDIFF(YEAR, p.birth_date, enc.last_enc) < 12 THEN 'Child'
            WHEN DATEDIFF(YEAR, p.birth_date, enc.last_enc) < 18 THEN 'Adolescent'
            WHEN DATEDIFF(YEAR, p.birth_date, enc.last_enc) > 17 THEN 'Adult'
        END "age_group"
FROM    patient AS p
        INNER JOIN enc
        ON p.pat_id = enc.pat_id
ORDER BY enc.last_enc DESC;
```

## Bad Example

```sql
SELECT  pe.pat_enc_csn_id,
        p.pat_mrn_id,
        p.pat_name,
        pe.contact_date,
        dep.department_name
FROM    pat_enc pe
        INNER JOIN clarity_dep dep
        ON pe.department_id = dep.department_id;
```

This example is not wrong SQL, but it is a poor commenting example because there is no contextual explanation of why the query exists, what business question it answers, or what the join is intended to accomplish.

# Naming Conventions

## Details

Naming conventions should allow a reviewer to understand where a file is used, what domain it covers, and what the output represents. Consistent naming improves readability, reduces ambiguity, and makes assets easier to find and reuse.

These conventions apply to:
- File names
- Tables
- Views
- Columns
- Common suffixes

## File Names

SQL query files should be named in a way that communicates:
- Where the file is used or what type of SQL object it is
- The content area or application
- A concise descriptor of the specific content

File names should always be written in `lower_snake_case` and should follow the format:

`<file_type>_<content_area>_<descriptor>`

### File Type

`file_type` refers to the type of SQL file or where the SQL will be used. Common examples include:
- `query` for any standalone query
- `sp` for any stored procedure
- `fn` for any function
- `rw` for SQL used in Epic Reporting Workbench reports
- `radar` for SQL used to populate Epic Radar metrics

### Content Area

`content_area` refers to the application or primary content domain of the data retrieved. Examples include:
- `amb` for clinical content based on EpicCare ambulatory workflows or tools
- `cad` for content related to scheduling
- `ed` for content related to ASAP or the emergency department
- `ip` for content related to inpatient admissions
- `myc` for content related to MyChart
- `ref` for content related to referrals
- `hb` for content related to hospital billing
- `pb` for content related to professional billing
- `qm` for content related to quality management or quality measures

### Descriptor

`descriptor` refers to the specific content of the query. It should be concise yet descriptive. Reviewers can gain additional detail from the purpose statement, but the descriptor should still provide a meaningful summary.

### Best Practice

- File names should use underscores instead of spaces and avoid special characters. This ensures compatibility and consistency.
- File names should not contain dates or version numbers. Version control should manage revisions.
- File names should not contain the name or initials of the author. Ownership belongs in the preface, not the filename.
- Scripts used to create stored procedures should have the same name as the stored procedure. This keeps artifacts aligned and easy to locate.
- File names should be descriptive enough to be interpretable in a repository listing without additional context.

### Avoid

- Avoid generic file names that do not communicate purpose.
- Avoid dates and version numbers in file names.
- Avoid author-specific naming conventions.
- Avoid spaces or special characters.
- Avoid vague descriptors that add no meaningful context.

### Good Example

```text
query_ref_referral_volume.sql
sp_ip_admissions_summary.sql
```

### Bad Example

```text
query_v2.sql
john_query.sql
data.sql
```

## Tables

Tables are physical database objects that store persisted data. Naming and structure should prioritize clarity, stability, and long-term maintainability. Data marts are also physical tables, but they often represent curated datasets focused on a specific content area.

### Best Practice

- Use descriptive, domain-specific names that clearly reflect the content of the table.
- Use lowercase letters and underscores for table names, such as `inpatient_dx` or `encounter_details`.
- Prefix data marts with `dm_` to indicate curated datasets for specific content areas.
- Ensure primary keys are clearly defined and follow naming conventions such as `patient_id` or `encounter_id`.
- Use table names that reflect the grain of the data, such as `daily_patient_visits` for one row per patient per day.
- Use consistent naming conventions across all tables in the database.
- Document the purpose and intended use of the table in comments at the top of the script.
- Use singular nouns for table names unless the table truly represents a collection.

### Avoid

- Avoid CamelCase for table names unless referencing the Caboodle database.
- Avoid generic prefixes like `tbl_` or `table_`.
- Avoid aliasing a table with the same name as one of its columns.
- Avoid concatenating two table names together into a single unreadable name such as `patientencounter`.
- Avoid reserved keywords or special characters in table names.
- Avoid abbreviations that are not widely understood or documented.
- Avoid using prefixes like `vw_` for physical tables.
- Avoid overly generic names such as `data`, `info`, or `table1`.

### Good Example

```text
patient
daily_patient_visits
dm_referral_summary
```

### Bad Example

```text
table1
tbl_patient
patientencounter
```

## Views

Views are logical database objects used to standardize reusable business logic, simplify downstream queries, and enforce consistent semantics. They provide an abstraction layer over base tables and can reduce duplication of complex joins while presenting a stable interface to analysts and reporting tools.

Because views may be referenced broadly and executed frequently, they must be treated as production assets with clear ownership, documentation, and performance considerations.

### Best Practice

- Prefix all views with `vw_` to distinguish them from physical tables.
- Explicitly define and document the grain of the view, such as one row per patient, encounter, or referral.
- Use views to encapsulate reusable business logic so it is defined once and applied consistently.
- Explicitly list all columns in the `SELECT` clause.
- Use `lower_snake_case` naming conventions for all columns.
- Alias columns using double quotes for portability.
- Include a standardized comment preface at the top of every view definition.
- Clearly document any deduplication logic.
- Join and filter on indexed columns where possible to improve performance.
- Use views as a controlled access layer instead of exposing base tables directly.

### Avoid

- Avoid creating views for ad hoc or one-time use cases.
- Avoid using `SELECT *` in view definitions.
- Avoid embedding volatile filters such as "last 30 days" unless explicitly required.
- Avoid introducing ambiguous grain or hidden duplication.
- Avoid excessive nesting of views without clear justification.
- Avoid using `ORDER BY` in view definitions unless required with `TOP`.

### Good Example

```sql
CREATE VIEW vw_patient_latest_encounter AS
SELECT  patient_id,
        contact_date
FROM    encounter;
```

### Bad Example

```sql
CREATE VIEW my_view AS
SELECT * FROM encounter;
```

## Columns

Column naming should make field meaning immediately clear and consistent across datasets.

### Best Practice

- Use `lower_snake_case` formatting for column names when referencing data from the Clarity database.
- Alias column names in double quotes for portability.
- Always include the table name or alias when referencing a column in SQL.
- Use descriptive names that indicate content and purpose.
- Avoid using a bare `id` when a more specific identifier is possible.

### Avoid

- Avoid CamelCase unless referencing the Caboodle database.
- Avoid aliasing a column with the same name as a table.
- Avoid generic identifiers when a more descriptive name is available.
- Avoid unqualified columns in multi-table queries.
- Avoid inconsistent suffix usage.

### Good Example

```sql
SELECT  p.patient_id,
        p.patient_name
FROM    patient AS p;
```

### Bad Example

```sql
SELECT  id,
        name
FROM    patient;
```

## Uniform Suffixes

The following suffixes have universal meanings and should be used consistently where appropriate:

- `_count`: a count or tally of something, e.g. `patient_count`
- `_date`: denotes a date value, e.g. `appt_date`
- `_dttm`: denotes a datetime or instant, e.g. `roomed_dttm`
- `_id`: a unique identifier, e.g. `pat_enc_csn_id`
- `_name`: signifies a name, e.g. `patient_name`
- `_status`: indicates state or classification, e.g. `appt_status`
- `_total`: denotes a sum or total, e.g. `rvu_total`

### Best Practice

- Use standard suffixes consistently so that field meaning is immediately recognizable.
- Match suffixes to actual data type and meaning.
- Prefer descriptive base names combined with standard suffixes.

### Avoid

- Avoid inventing inconsistent suffix patterns.
- Avoid using a suffix that does not match the data.
- Avoid leaving semantic meaning ambiguous when a standard suffix would clarify it.

### Good Example

```text
patient_id
contact_date
appt_status
rvu_total
```

### Bad Example

```text
patient_identifier
dt_contact
status_value
total_rvu_amount
```

# Query Syntax

## Details

Query syntax standards improve readability, reduce cognitive load, and make code easier to review and troubleshoot. Consistency in formatting helps separate logic from implementation details and makes structural issues easier to spot.

## Reserved Words

### Best Practice

- Always use uppercase for reserved keywords like `SELECT` and `WHERE`. This makes SQL syntax visually distinct from identifiers.
- Prefer ANSI-standard keywords and functions when the same outcome can be achieved without vendor-specific syntax.
- Keep keyword casing consistent throughout the query.

### Avoid

- Avoid mixing keyword casing inconsistently.
- Avoid using vendor-specific syntax when a widely supported alternative is reasonable.
- Avoid styling that makes syntax hard to distinguish from column names and aliases.

### Good Example

```sql
SELECT  p.pat_name "patient_name"
FROM    patient AS p
WHERE   p.birth_date >= '2019-01-01';
```

### Bad Example

```sql
select p.pat_name "patient_name" from patient p where p.birth_date >= '2019-01-01';
```

## White Space

To make code easier to read, the correct amount of spacing should be used. Avoid crowding code or removing natural-language spacing.

### Spaces

Spaces should be used to line up code so that root keywords align visually. This creates a "river" down the middle, making queries easier to scan.

### Best Practice

- Put each selected column on its own line.
- Keep commas at the end of the line rather than beginning the next line with a comma.
- Use spaces before and after `=`.
- Use spaces after commas.
- Use natural spacing around quoted strings and expressions.

### Avoid

- Avoid compressed formatting that forces the reader to parse too much at once.
- Avoid leading commas.
- Avoid omitting spaces around operators.
- Avoid inconsistent alignment.
- Avoid formatting that obscures logical structure.

### Good Example

```sql
(
SELECT  f.species_name,
        AVG(f.height) "average_height",
        AVG(f.diameter) "average_diameter"
FROM    flora AS f
WHERE   f.species_name = 'Banksia'
OR      f.species_name = 'Sheoak'
OR      f.species_name = 'Wattle'
        
        GROUP BY 
        f.species_name,
        f.observation_date
)

UNION ALL

(
SELECT  b.species_name,
        AVG(b.height) "average_height",
        AVG(b.diameter) "average_diameter"
FROM    botanic_garden_flora AS b
WHERE   b.species_name = 'Banksia'
OR      b.species_name = 'Sheoak'
OR      b.species_name = 'Wattle'
        
        GROUP BY 
        b.species_name,
        b.observation_date
);
```

### Bad Example

```sql
(select f.species_name,AVG(f.height)"average_height",AVG(f.diameter)"average_diameter" from flora f where f.species_name='Banksia' or f.species_name='Sheoak' or f.species_name='Wattle' group by f.species_name,f.observation_date)
UNION ALL
(select b.species_name,AVG(b.height)"average_height",AVG(b.diameter)"average_diameter" from botanic_garden_flora b where b.species_name='Banksia' or b.species_name='Sheoak' or b.species_name='Wattle' group by b.species_name,b.observation_date);
```

## Line Spacing

### Best Practice

- Insert new lines before `AND` and `OR`.
- Use blank lines to separate logical sections of code.
- Separate multiple statements with vertical space after semicolons.
- Use line breaks to organize large column lists into meaningful groups.

### Avoid

- Avoid writing long, uninterrupted blocks of SQL.
- Avoid stacking all conditions onto one line.
- Avoid removing blank lines where they improve readability.
- Avoid mixing multiple unrelated logical sections without separation.
- Avoid formatting that forces the reader to hunt for clause boundaries.

### Good Example

```sql
INSERT INTO albums (title, release_date, recording_date)

VALUES  ('Charcoal Lane', '1990-01-01 01:01:01.00000', '1990-01-01 01:01:01.00000'),
        ('The New Danger', '2008-01-01 01:01:01.00000', '1990-01-01 01:01:01.00000');

UPDATE  albums

SET     release_date = '1990-01-01 01:01:01.00000'

WHERE   title = 'The New Danger';

SELECT  a.title,
        a.release_date,
        a.recording_date,
        a.production_date

FROM    albums AS a

WHERE   a.title = 'Charcoal Lane'
OR      a.title = 'The New Danger';
```

### Bad Example

```sql
INSERT INTO albums (title, release_date, recording_date) VALUES ('Charcoal Lane','1990-01-01 01:01:01.00000','1990-01-01 01:01:01.00000'),('The New Danger','2008-01-01 01:01:01.00000','1990-01-01 01:01:01.00000'); UPDATE albums SET release_date='1990-01-01 01:01:01.00000' WHERE title='The New Danger'; SELECT a.title,a.release_date,a.recording_date,a.production_date FROM albums a WHERE a.title='Charcoal Lane' OR a.title='The New Danger';
```

## Indentation

To ensure readability, proper indentation standards should be followed.

### Joins

Joins should be indented consistently and grouped clearly.

### Best Practice

- Indent joins so they are visually separated from the `FROM` clause.
- Place join conditions on their own lines.
- Keep multi-condition joins aligned and easy to scan.

### Avoid

- Avoid inconsistent indentation.
- Avoid crowding join conditions onto one line.
- Avoid formatting that hides relationship logic.
- Avoid placing complex join conditions where they are hard to distinguish from filters.
- Avoid inconsistent aliasing style within joins.

### Good Example

```sql
SELECT  p.pat_name

FROM    pat_enc AS pe

        INNER JOIN patient AS p
        ON pe.pat_id = p.pat_id
        AND p.birth_date >= '2022-01-01'

        INNER JOIN zc_tax_state AS state
        ON p.state_c = state.state_c;
```

### Bad Example

```sql
SELECT p.pat_name FROM pat_enc pe INNER JOIN patient p ON pe.pat_id = p.pat_id AND p.birth_date >= '2022-01-01' INNER JOIN zc_tax_state state ON p.state_c = state.state_c;
```

### Subqueries

Subqueries should be aligned using the same structure as any other query. Closing parentheses should be positioned clearly, especially when nesting is involved.

### Best Practice

- Format subqueries with the same clause alignment standards as top-level queries.
- Place nested logic on separate lines.
- Use indentation to clearly show scope and nesting depth.

### Avoid

- Avoid embedding dense subqueries inline without formatting.
- Avoid ambiguous parenthesis placement.
- Avoid nested queries that are hard to visually parse.
- Avoid mixing multiple nested scopes on one line.
- Avoid formatting that obscures where a subquery begins or ends.

### Good Example

```sql
SELECT  r.last_name,
        (
            SELECT  MAX(YEAR(championship_date))
            FROM    champions AS c
            WHERE   c.last_name = r.last_name
            AND     c.confirmed = 'Y'
        ) AS last_championship_year

FROM    riders AS r

WHERE   r.last_name IN
        (
            SELECT  c.last_name
            FROM    champions AS c
            WHERE   YEAR(championship_date) > '2008'
            AND     c.confirmed = 'Y'
        );
```

### Bad Example

```sql
SELECT r.last_name,(SELECT MAX(YEAR(championship_date)) FROM champions c WHERE c.last_name=r.last_name AND c.confirmed='Y') AS last_championship_year FROM riders r WHERE r.last_name IN (SELECT c.last_name FROM champions c WHERE YEAR(championship_date)>'2008' AND c.confirmed='Y');
```

# Stored Procedures

## Details

Stored procedures should follow all guidelines for regular queries, with additional considerations for repeatability, operational safety, and production maintenance. Stored procedures often serve as production data pipelines, and their structure must support reliable execution over time.

## Best Practice

- Define the stored procedure and destination table clearly at the top. This makes ownership and target objects explicit.
- Use `CREATE OR ALTER PROCEDURE` so deployments are idempotent and safer across environments.
- Create the destination table if it does not already exist. This supports repeatable deployment.
- Define data types for every column and identify a primary key. Correct table design is foundational to reliable stored procedures.
- Use variable-driven incremental or full-load logic. This makes load patterns transparent and maintainable.
- Delete and replace only the records being refreshed. This limits unnecessary churn and supports incremental processing.
- Use clear comment blocks to separate major procedural steps.

## Avoid

- Avoid creating unstructured stored procedures that mix unrelated logic together.
- Avoid hardcoding date ranges when incremental logic is required.
- Avoid relying on implicit assumptions about target table schema.
- Avoid omitting deletion logic when replacing existing records.
- Avoid full reloads when incremental logic is sufficient.
- Avoid leaving procedural sections undocumented.

## Good Example

```sql
USE EPIC_MPFQM;
GO

CREATE OR ALTER PROCEDURE [dbo].[stored_proc_name] (@full_indicator INT = 0)
AS
BEGIN

/*******************************************************************************
This section creates the final table if it does not already exist
*******************************************************************************/

IF NOT EXISTS
(
    SELECT *
      FROM sys.objects
     WHERE object_id = OBJECT_ID(N'[dbo].[destination_table]')
       AND type IN (N'U')
)
BEGIN
    CREATE TABLE [dbo].[destination_table]
    (
        Insert_Columns
    );
END;
```

### Set the Date Range

Next, identify the date range of record to add or replace each time the stored procedure runs.

```sql
/*******************************************************************************
This section identifies the time period for records we are adding/replacing.
If the full indicator is set to 0, the procedure performs an incremental load.
If the full indicator is set to 1, the procedure performs a full load.
*******************************************************************************/

DECLARE @start_date DATE;
DECLARE @end_date DATE;

IF @full_indicator = 0
BEGIN
    SET @start_date =
        (
            SELECT COALESCE(DATEADD(DAY, -7, MAX(date_field)), 'full_start_date')
              FROM Epic_MPFQM.dbo.destination_table
        );
    SET @end_date = GETDATE();
END
ELSE
BEGIN
    SET @start_date = 'full_start_date';
    SET @end_date = GETDATE();
END;

/*******************************************************************************
Delete records that are being replaced
*******************************************************************************/
DELETE FROM [dbo].[destination_table]
WHERE date_field BETWEEN @start_date AND @end_date;
```

Important notes:
- The default value for `@full_indicator` is `0`, which loads the data incrementally.
- To load the full range of dates, change the `@full_indicator` variable when executing the procedure.
- The `date_field` variable needs to be a column in the final table.
- The `date_field` variable cannot be defined using a `COALESCE` statement.

### Close

Use `INSERT INTO` to update the table with new rows of data.

Close with an `END;` statement to complete the `AS BEGIN` block that defines the stored procedure.

## Bad Example

```sql
CREATE PROC test AS SELECT * FROM table;
```

This example is problematic because it lacks structure, does not define load strategy, uses `SELECT *`, and is not designed for production maintenance.

## Reporting Universes

A reporting universe consists of a single stored procedure that updates multiple data marts. Create multiple data marts in one stored procedure by defining each final table clearly.

### Good Example

```sql
USE EPIC_MPFQM;
GO

CREATE OR ALTER PROCEDURE [dbo].[stored_proc_name] (@full_indicator INT = 0)
AS
BEGIN

/*******************************************************************************
This section creates the final table if it does not already exist
*******************************************************************************/

-- Table 1
IF NOT EXISTS
(
    SELECT *
      FROM sys.objects
     WHERE object_id = OBJECT_ID(N'[dbo].[destination_table_01]')
       AND type IN (N'U')
)
BEGIN
    CREATE TABLE [dbo].[destination_table_01]
    (
        Insert_Columns
    );
END;

-- Table 2
IF NOT EXISTS
(
    SELECT *
      FROM sys.objects
     WHERE object_id = OBJECT_ID(N'[dbo].[destination_table_02]')
       AND type IN (N'U')
)
BEGIN
    CREATE TABLE [dbo].[destination_table_02]
    (
        Insert_Columns
    );
END;
```

It is possible to use the same date field to update multiple data marts at once.

```sql
/*******************************************************************************
This section creates the final table if it does not already exist
*******************************************************************************/

-- Sales History
IF NOT EXISTS
(
    SELECT *
      FROM sys.objects
     WHERE object_id = OBJECT_ID(N'[dbo].[dm_sales_hx]')
       AND type IN (N'U')
)
BEGIN
    CREATE TABLE [dbo].[dm_sales_hx]
    (
        sale_id NUMERIC,
        date_sold DATE
        -- ...
    );
END;

-- Sale Details
IF NOT EXISTS
(
    SELECT *
      FROM sys.objects
     WHERE object_id = OBJECT_ID(N'[dbo].[dm_sale_details]')
       AND type IN (N'U')
)
BEGIN
    CREATE TABLE [dbo].[dm_sale_details]
    (
        sale_id NUMERIC,
        customer_id NUMERIC,
        item_id NUMERIC
        -- ...
    );
END;

/*******************************************************************************
Delete records that are being replaced
*******************************************************************************/
DELETE FROM [dbo].[dm_sales_hx]
WHERE date_sold BETWEEN @start_date AND @end_date;

DELETE FROM [dbo].[dm_sale_details]
WHERE sale_id IN
      (
          SELECT sale_id
            FROM dm_sale_hx
           WHERE date_sold BETWEEN @start_date AND @end_date
      );
```

Clearly delineate sections for each table, for example:

```sql
/*
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
The next section addresses content in the table table_01.
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
*/
```

### Bad Example

```sql
CREATE PROC universe AS
BEGIN
SELECT * FROM a;
SELECT * FROM b;
END;
```

This example is problematic because it lacks table creation safeguards, load-window logic, deletion logic, clear sectioning, and explicit column lists.

# Code Review Considerations

## Details

Before SQL is submitted for review, it must meet all style guide standards. This ensures reviewers focus on business logic rather than formatting or structural issues. 

- SQL should be fully formatted and aligned with style standards before submission so reviewers can focus on validating logic rather than correcting formatting.
- Developers should review the (https://github.com/rchsd/analytics_performance_improvement/wiki/SQL-Development-Guide#code-review-checklist) prior to submission to ensure all required standards are met.
- All queries should include a standardized preface and appropriate comments to clearly communicate the purpose of the query, the business context, and any key assumptions.
- Developers should validate joins, data grain, and deduplication logic prior to review to ensure the query produces accurate and reliable results.
- The Copilot workflow or equivalent tooling should be used to enforce consistency and ensure compliance with style standards before submission.
- Queries should be tested and validated against expected results to confirm correctness before requesting review.


