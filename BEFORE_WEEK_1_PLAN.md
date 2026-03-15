# Before Week 1 Plan

Repo-specific action plan aligned to the current final-pack documents in [docs/](D:/Codex/Clinical_Research_Project/docs), especially the mentor guide and roadmap.

## Purpose

This plan turns the pre-Week 1 setup into concrete, lightweight steps for this repository.

## Action Plan

1. Set up the SQL environment.
   Use SQLite for the first pass because this repo favors lightweight local tooling. Install SQLite plus DB Browser for SQLite, then create a local database file for this project, such as `trial_workbench.db`, and verify that it opens correctly.

2. Set up Python for this repo.
   Create one clean project environment and install the repo dependencies from [requirements.txt](D:/Codex/Clinical_Research_Project/requirements.txt). Follow [SETUP_ENVIRONMENT.md](D:/Codex/Clinical_Research_Project/SETUP_ENVIRONMENT.md) so the repo-local `.venv` works cleanly in PowerShell and VS Code.

3. Inspect the synthetic dataset already included in this repo.
   Review [data/README_data.md](D:/Codex/Clinical_Research_Project/data/README_data.md), [data/data_dictionary.md](D:/Codex/Clinical_Research_Project/data/data_dictionary.md), and the CSV files in [data/](D:/Codex/Clinical_Research_Project/data) so the schema is clear before import.

4. Load the current repo dataset into SQLite.
   Import `sites.csv`, `subjects.csv`, `visits.csv`, `adverse_events.csv`, and `protocol_deviations.csv` from [data/](D:/Codex/Clinical_Research_Project/data) into your SQLite database. The immediate goal is to be query-ready for Weeks 1-2, not to build a perfect pipeline yet.
   A minimal import script is available at [import_trial_csvs_to_sqlite.py](D:/Codex/Clinical_Research_Project/Dad_Stuff/sqlite_import/import_trial_csvs_to_sqlite.py), with a short walkthrough in [README_sqlite_import.md](D:/Codex/Clinical_Research_Project/Dad_Stuff/sqlite_import/README_sqlite_import.md).

5. Verify Tableau Public can read the project outputs.
   Install Tableau Public, then open one of the CSVs from [data/](D:/Codex/Clinical_Research_Project/data) to confirm the tool launches and can read the dataset. You do not need a polished dashboard yet.

6. Do the first 10 SQLBolt exercises yourself.
   This is not repo work, but it directly supports the repo's Week 1-2 SQL tasks. The target is enough SQL fluency to help with `SELECT`, `JOIN`, grouping, and filtering against this dataset.

7. Review HIPAA and privacy boundaries before any build work.
   For this repo, the key rule is simple: only synthetic or public data goes into local tools, GitHub, or AI tools. Cross-check that understanding against the safety rules in [AGENTS.md](D:/Codex/Clinical_Research_Project/AGENTS.md).

8. Stretch option: download a public Synthea dataset and write a SQLite import script.
   If you want an extra data-engineering exercise, download a small public dataset from `synthea.mitre.org`, inspect the CSV layout, and write a simple import script that loads selected CSVs into SQLite tables. Treat this as a secondary exercise after the repo dataset is already working, not as a blocker for Week 1 startup.

9. Regenerate the synthetic dataset only if needed.
   The CSVs already in [data/](D:/Codex/Clinical_Research_Project/data) are sufficient for Week 1 startup. If you intentionally change the generator or want a fresh synthetic snapshot, run [make_synthetic_trial_data.py](D:/Codex/Clinical_Research_Project/Dad_Stuff/synthetic_trial_data_generator/make_synthetic_trial_data.py) from the repo root:

   ```powershell
   .\.venv\Scripts\python.exe Dad_Stuff\synthetic_trial_data_generator\make_synthetic_trial_data.py
   ```

   Then review [data/README_data.md](D:/Codex/Clinical_Research_Project/data/README_data.md) and `git status --short` before committing any regenerated outputs.

10. Clean up the repo entry point before Week 1 starts.
   Keep [README.md](D:/Codex/Clinical_Research_Project/README.md) aligned to the final-pack `.docx` documents, the current generator path, the setup guide, and the repo's privacy-safe project framing.

## Already Present In This Repo

- The current source-of-truth docs are the final-pack `.docx` files in [docs/](D:/Codex/Clinical_Research_Project/docs).
- The synthetic data generator exists at [make_synthetic_trial_data.py](D:/Codex/Clinical_Research_Project/Dad_Stuff/synthetic_trial_data_generator/make_synthetic_trial_data.py).
- The current dataset and counts are documented in [data/README_data.md](D:/Codex/Clinical_Research_Project/data/README_data.md).
- A repo-local Python setup guide exists at [SETUP_ENVIRONMENT.md](D:/Codex/Clinical_Research_Project/SETUP_ENVIRONMENT.md).

## Recommended Order

1. SQLite + DB Browser
2. Python environment check
3. Inspect current CSVs and data docs
4. Import CSVs into SQLite
5. Tableau Public check
6. SQLBolt 1-10
7. Privacy boundary review
8. Optional Synthea import exercise
9. README cleanup
10. Regenerate data only if needed
