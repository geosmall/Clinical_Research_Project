# Before Week 1 Plan

Repo-specific action plan aligned to the current final-pack documents in [docs/](./docs/), especially the mentor guide and roadmap.

## Purpose

This plan turns the pre-Week 1 setup into concrete, lightweight steps for this repository.

## Action Plan

1. Review privacy boundaries before any build work.
   For this repo, the key rule is simple: only synthetic or public data goes into local tools, GitHub, or AI tools. Cross-check that understanding against the safety rules in [AGENTS.md](./AGENTS.md).

2. Set up the SQL environment.
   Use SQLite for the first pass because this repo favors lightweight local tooling. Install SQLite plus DB Browser for SQLite, then create a local database file for this project, such as `trial_workbench.db`, and verify that it opens correctly.

3. Set up Python for this repo.
   Create one clean project environment and install the repo dependencies from [requirements.txt](./requirements.txt). Follow [SETUP_ENVIRONMENT.md](./SETUP_ENVIRONMENT.md) to verify that `python` is a normal installed interpreter rather than the Microsoft Store alias, then create and verify the repo-local `.venv`. Use [ENVIRONMENT_NOTES.md](./ENVIRONMENT_NOTES.md) only if you hit environment-specific issues.

4. Inspect the synthetic dataset already included in this repo.
   Review [data/README_data.md](./data/README_data.md), [data/data_dictionary.md](./data/data_dictionary.md), and the CSV files in [data/csv/](./data/csv/) so the schema is clear before import.

5. Load the current repo dataset into SQLite.
   Import `sites.csv`, `subjects.csv`, `visits.csv`, `adverse_events.csv`, and `protocol_deviations.csv` from [data/csv/](./data/csv/) into your SQLite database. The immediate goal is to be query-ready for Weeks 1-2, not to build a perfect pipeline yet.
   A minimal import script is available at [import_trial_csvs_to_sqlite.py](./data/import_trial_csvs_to_sqlite.py), with a short walkthrough in [README_sqlite_import.md](./data/README_sqlite_import.md).

6. Verify Tableau Public can read the project outputs.
   Install Tableau Public, then open one of the CSVs from [data/csv/](./data/csv/) to confirm the tool launches and can read the dataset. You do not need a polished dashboard yet.

7. Do the first 10 SQLBolt exercises yourself.
   This is not repo work, but it directly supports the repo's Week 1-2 SQL tasks. The target is enough SQL fluency to help with `SELECT`, `JOIN`, grouping, and filtering against this dataset.

8. Stretch option: download a public Synthea dataset and write a SQLite import script.
   If you want an extra data-engineering exercise, download a small public dataset from `synthea.mitre.org`, inspect the CSV layout, and write a simple import script that loads selected CSVs into SQLite tables. Treat this as a secondary exercise after the repo dataset is already working, not as a blocker for Week 1 startup.

9. Regenerate the synthetic dataset only if needed.
   The CSVs already in [data/](./data/) are sufficient for Week 1 startup. If you intentionally change the generator or want a fresh synthetic snapshot, run [make_synthetic_trial_data.py](./data/make_synthetic_trial_data.py) from the repo root:

   ```powershell
   .\.venv\Scripts\python.exe data\make_synthetic_trial_data.py
   ```

   Then review [data/README_data.md](./data/README_data.md) and `git status --short` before committing any regenerated outputs.

10. Clean up the repo entry point before Week 1 starts.
   Keep [README.md](./README.md) aligned to the final-pack `.docx` documents, the current generator path, the setup guide, and the repo's privacy-safe project framing.

## Already Present In This Repo

- The current source-of-truth docs are the final-pack `.docx` files in [docs/](./docs/).
- The synthetic data generator exists at [make_synthetic_trial_data.py](./data/make_synthetic_trial_data.py).
- The current dataset and counts are documented in [data/README_data.md](./data/README_data.md).
- A repo-local Python setup guide exists at [SETUP_ENVIRONMENT.md](./SETUP_ENVIRONMENT.md).

## Recommended Order

1. Privacy boundary review
2. SQLite + DB Browser
3. Python environment check
4. Inspect current CSVs and data docs
5. Import CSVs into SQLite
6. Tableau Public check
7. SQLBolt 1-10
8. README cleanup
9. Regenerate data only if needed
10. Optional Synthea import exercise
