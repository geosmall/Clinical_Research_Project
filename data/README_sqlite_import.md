# SQLite Import Workflow

Minimal import workflow for loading the repo's synthetic clinical trial CSVs into SQLite for Week 1 and Week 2 SQL practice.

## What it creates

- A SQLite database file, defaulting to `trial_workbench.db` in this folder
- Five tables based on the current CSV dataset in [`csv/`](./csv/):
  - `sites`
  - `subjects`
  - `visits`
  - `adverse_events`
  - `protocol_deviations`

The script replaces those tables each time it runs, which keeps the workflow simple for repeated practice.

## Local Script

- [`import_trial_csvs_to_sqlite.py`](./import_trial_csvs_to_sqlite.py)

The script reads CSVs from [`csv/`](./csv/) by default.

## Run it

From the repo root in PowerShell:

```powershell
.\.venv\Scripts\python.exe .\data\import_trial_csvs_to_sqlite.py
```

To write to a different SQLite file:

```powershell
.\.venv\Scripts\python.exe .\data\import_trial_csvs_to_sqlite.py --db .\data\trial_workbench.db
```

## Verify it worked

Open the resulting database in DB Browser for SQLite, or use the SQLite CLI:

```powershell
sqlite3 .\data\trial_workbench.db "select 'sites', count(*) from sites union all select 'subjects', count(*) from subjects union all select 'visits', count(*) from visits union all select 'adverse_events', count(*) from adverse_events union all select 'protocol_deviations', count(*) from protocol_deviations;"
```

Expected row counts with the current dataset:

- `sites`: 6
- `subjects`: 161
- `visits`: 568
- `adverse_events`: 116
- `protocol_deviations`: 72

## Notes

- This is a beginner-friendly import path, not a production ETL pipeline.
- The script adds a few indexes on common ID fields to make basic joins and filtering easier.
- If the CSV schema changes later, rerun the script to rebuild the tables from the current files.
