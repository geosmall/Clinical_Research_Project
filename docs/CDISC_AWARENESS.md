# CDISC Awareness Companion

This note explains how the repo's learner-friendly synthetic dataset relates to common CDISC concepts without turning the project into a full SDTM or submission-model exercise.

## Purpose

The current dataset is designed for:

- SQL practice
- Tableau dashboarding
- Python data checks and reporting
- portfolio-ready clinical operations storytelling

It is intentionally simpler than a production clinical data model. The goal here is CDISC awareness, not CDISC compliance.

## Why CDISC matters for you (Hannah)

CDISC matters because it is part of the language of clinical research data work, even when your day-to-day job is not building regulatory submission datasets yourself.

For this learning plan, CDISC awareness can help you:

- recognize how clinical operations, data management, and biostatistics teams often organize study data
- speak more confidently about standardization in interviews and portfolio discussions
- understand why consistent naming, controlled values, and traceable derivations matter
- connect learner-friendly analytics work to the more formal data structures used in industry

You do not need to master SDTM (Study Data Tabulation Model, a standard structure for organizing clinical study data) or ADaM (Analysis Data Model, a standard structure for analysis-ready datasets) to get value from this repo. The practical goal is to build enough familiarity that CDISC concepts feel recognizable rather than opaque.

## What "CDISC-aware" means in this repo

For this project, CDISC-aware means:

- using consistent identifiers and controlled values where practical
- understanding which learner-friendly tables are closest to real clinical data domains
- documenting likely mappings to standard concepts
- avoiding unnecessary production-level complexity too early

It does not mean:

- building a full SDTM package
- using complete submission-ready variable naming
- implementing audit-trail, traceability, and standards-governance requirements
- replacing readable learner-facing columns with opaque production abbreviations

## Approximate mapping from this dataset to CDISC concepts

### `subjects.csv`

Closest concepts:

- `DM`-like subject-level demographics and identifiers
- `DS`-like disposition concepts for screen failure, completion, or discontinuation

Examples:

- `subject_id` is the learner-friendly subject key
- `screen_fail_flag`, `subject_status`, `completion_date`, and `discontinuation_reason` cover ideas that would often be represented more formally across standard disposition structures
- `sex`, `age`, and `race` are demographic variables in a simplified form

### `visits.csv`

Closest concepts:

- `SV`-like actual subject visit tracking
- `TV`-like scheduled visit structure, though the current repo combines planned and actual information in one table

Examples:

- `planned_date` represents protocol target timing
- `actual_date` represents observed visit timing
- `visit_status` and `protocol_window_ok` capture simplified execution outcomes that would be more formally modeled in production data

### `adverse_events.csv`

Closest concept:

- `AE`

Examples:

- `ae_term`, `severity`, `serious_flag`, `relatedness`, `action_taken`, and `outcome` are a simplified adverse-event structure
- `study_day_onset` is a learner-friendly derivation similar in spirit to study-day calculations used in standard clinical datasets

### `protocol_deviations.csv`

Closest concept:

- operational protocol deviation tracking rather than a single universal CDISC submission domain

Examples:

- this table is useful for monitoring and training work, even though it is simpler than how deviations may be handled across sponsor or CRO systems
- `deviation_type`, `severity`, and `resolved_flag` support monitoring-style analysis

### `sites.csv`

Closest concept:

- operational site-management metadata rather than a standard SDTM subject domain

Examples:

- `site_activation_date`, `enrollment_target`, and `monitoring_risk_level` are operational planning and oversight fields
- this table is intentionally analytics-friendly for site performance work, not modeled as a regulatory submission dataset

## Why the repo does not use a full CDISC model

A full CDISC-style model would add a lot of complexity too early:

- more domains
- stricter variable naming
- more controlled terminology
- more derivations and metadata
- less readable tables for beginner SQL and Python work

That would make the learning curve steeper without clearly improving the Week 1 to Week 8 outcomes.

## Practical ways to make the dataset more CDISC-aware later

If the repo grows, these are sensible incremental upgrades:

1. Add a `study_id` field across tables.
2. Add a documented `usubjid`-style derived identifier while keeping `subject_id` for readability.
3. Standardize controlled values more explicitly for statuses, flags, severity, relatedness, and outcomes.
4. Expand the data dictionary with allowed values, derivation notes, and "closest CDISC concept" annotations.
5. Add a small metadata/spec file that lists each variable, meaning, origin, and expected values.

## Recommended learner mindset

Use this dataset to learn the operational questions first:

- How many subjects screened and randomized?
- Which sites are underperforming?
- Which visits were missed or out of window?
- What safety or deviation patterns need monitoring attention?

Then use this companion note to understand how those same ideas would appear in a more standardized clinical data environment.
