# Synthea Sample Data Notes

This folder contains a public Synthea sample dataset downloaded for optional practice work outside the main synthetic clinical trial dataset in [`../data/`](../data/).

## Source

- Source project: Synthea by The MITRE Corporation / Synthetic Health
- Official project page: https://synthetichealth.github.io/synthea/
- Public sample-data repository: https://github.com/synthetichealth/synthea-sample-data
- Downloaded artifact: `synthea_sample_data_csv_apr2020.zip`

This dataset is public synthetic data, not real patient data.

## Local Layout

- Downloaded zip: `synthea_sample_data_csv_apr2020.zip`
- Extracted CSV folder: [`csv/`](./csv/)

## Included CSV Files

The extracted `csv/` folder currently contains:

- `allergies.csv`
- `careplans.csv`
- `conditions.csv`
- `devices.csv`
- `encounters.csv`
- `imaging_studies.csv`
- `immunizations.csv`
- `medications.csv`
- `observations.csv`
- `organizations.csv`
- `patients.csv`
- `payer_transitions.csv`
- `payers.csv`
- `procedures.csv`
- `providers.csv`
- `supplies.csv`

## Good Starter Tables

For a first SQLite import exercise, start with:

- `patients.csv`
- `encounters.csv`
- `conditions.csv`
- `medications.csv`
- `observations.csv`

These are enough for basic joins and beginner SQL practice.

Current starter row counts from the downloaded sample:

- `patients.csv`: 1,171 rows
- `encounters.csv`: 53,346 rows
- `conditions.csv`: 8,376 rows
- `medications.csv`: 42,989 rows
- `observations.csv`: 299,697 rows

## Local SQLite Import Script

A beginner-friendly import script for the starter tables lives here:

- [`import_synthea_starter_csvs_to_sqlite.py`](./import_synthea_starter_csvs_to_sqlite.py)

Run it from the repo root:

```powershell
.\.venv\Scripts\python.exe .\data_synthea\import_synthea_starter_csvs_to_sqlite.py
```

This creates:

- `synthea_starter.db`

`synthea_starter.db` is a local generated file for practice use. It is not committed to git, so after a fresh clone you should rerun the import script if you want the SQLite database locally.

Then verify the import:

```powershell
sqlite3 .\data_synthea\synthea_starter.db ".tables"
sqlite3 .\data_synthea\synthea_starter.db "select count(*) from patients;"
```

## Usage Notes

- Synthea field names often use uppercase or mixed-case column names such as `Id`, `PATIENT`, and `ENCOUNTER`.
- Inspect headers before creating indexes or writing joins.
- Keep this folder separate from the main repo capstone dataset in [`../data/`](../data/), since this sample reflects general healthcare/event-style data rather than the repo's trial-monitoring structure.
