# Clinical_Research_Project

Execution-ready clinical research analytics learning workspace centered on a privacy-safe portfolio project: a Synthetic Clinical Trial Monitoring Workbench.

## What this repo is for

This project supports an 8-week, self-paced learning plan for an early-career clinical research professional building practical skills in:

- SQL
- Tableau
- Python
- AI-assisted workflows
- GitHub and portfolio development
- Light REDCap familiarity

The learner owns the clinical framing and interpretation. Dad acts as engineering mentor and technical pair-programmer for setup, debugging, Git hygiene, Python pairing, and careful AI-assisted workflow habits.

## Current source documents

The current source of truth lives in [docs/](./docs/):

- [Clinical_Research_Learning_Final_Pack_Overview.docx](./docs/Clinical_Research_Learning_Final_Pack_Overview.docx)
- [Clinical_Research_Learning_Final_Pack_Roadmap.docx](./docs/Clinical_Research_Learning_Final_Pack_Roadmap.docx)
- [Clinical_Research_Learning_Final_Pack_Execution_Checklist.docx](./docs/Clinical_Research_Learning_Final_Pack_Execution_Checklist.docx)
- [Clinical_Research_Learning_Final_Pack_Dads_Guide.docx](./docs/Clinical_Research_Learning_Final_Pack_Dads_Guide.docx)

Older document names may still appear in repo history, but the final-pack files above are the active versions.

## Repo layout

- [docs/](./docs/): learner-facing guides, roadmap, checklist, and mentor guide
- [data/](./data/): synthetic clinical trial CSVs plus dataset notes and data dictionary
- [Dad_Stuff/](./Dad_Stuff/): helper scripts and working materials
- [.codex/](./.codex/): repo-local rules and skills

## First steps before Week 1

- Follow [BEFORE_WEEK_1_PLAN.md](./BEFORE_WEEK_1_PLAN.md)
- Set up the repo-local Python environment with [SETUP_ENVIRONMENT.md](./SETUP_ENVIRONMENT.md), including the Windows check to avoid Microsoft Store Python aliases
- Use [ENVIRONMENT_NOTES.md](./ENVIRONMENT_NOTES.md) only for environment-specific issues and sandbox notes
- Review the current synthetic dataset in [data/README_data.md](./data/README_data.md), [data/data_dictionary.md](./data/data_dictionary.md), and [data/csv/](./data/csv/)

## Synthetic data and safety rules

This repo is intentionally restricted to synthetic, public, or clearly representative non-work data.

- Never add real patient data, PHI, employer reports, screenshots from work systems, credentials, or confidential material
- Document data source, assumptions, and verification steps for each meaningful deliverable
- Treat AI output as a draft that must be reviewed and verified

## Regenerating synthetic data

Use the current generator from the repo root:

```powershell
.\.venv\Scripts\python.exe data\make_synthetic_trial_data.py
```

Then review and publish changes:

```powershell
git status --short
git add data\make_synthetic_trial_data.py data\
git commit -m "Update synthetic trial dataset"
git push origin main
```

[`data/README_data.md`](./data/README_data.md) records the git commit used to generate the dataset, so it normally refers to the pre-commit revision that produced the files.

## Future considerations

- Add an optional `dirty` dataset export with intentional, documented QA issues for Week 5 data-quality exercises while keeping the current output as the clean canonical dataset.
- Make the synthetic dataset more CDISC-aware without turning it into a full production-model training burden.
- Improve the generator's statefulness further where that adds learning value, especially around operational timelines and trial-conduct logic.
- Expand the data dictionary into a richer metadata/spec reference if the capstone grows beyond the current learner-friendly scope.

Related reference:

- [CDISC_AWARENESS.md](./docs/CDISC_AWARENESS.md)
