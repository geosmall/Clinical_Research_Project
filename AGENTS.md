# AGENTS.md

## Purpose
Maintain this repository as an execution-ready clinical research analytics learning workspace.

The project is an 8-week, self-paced plan for an early-career clinical research professional to build stronger skills in:
- SQL
- Tableau
- Python
- AI-assisted workflows
- GitHub and portfolio development
- Light REDCap familiarity

The through-line project is a privacy-safe portfolio artifact: a Synthetic Clinical Trial Monitoring Workbench.

## Primary Source Documents
The current project definition lives in [`docs/`](./docs/).

Core final-pack documents:
- [`Clinical_Research_Learning_Final_Pack_Overview.docx`](./docs/Clinical_Research_Learning_Final_Pack_Overview.docx)
- [`Clinical_Research_Learning_Final_Pack_Roadmap.docx`](./docs/Clinical_Research_Learning_Final_Pack_Roadmap.docx)
- [`Clinical_Research_Learning_Final_Pack_Execution_Checklist.docx`](./docs/Clinical_Research_Learning_Final_Pack_Execution_Checklist.docx)
- [`Clinical_Research_Learning_Final_Pack_Dads_Guide.docx`](./docs/Clinical_Research_Learning_Final_Pack_Dads_Guide.docx)

Document handling rules:
- Treat the final-pack `.docx` documents above as the current source of truth over older document names
- Prefer `.docx` for polished learner-facing curriculum documents and companion handouts where Word-style formatting matters
- Prefer `.md` for supplementary references, technical explainers, workflow notes, and documents where GitHub readability matters more than Word formatting
- `docs/` may contain both `.docx` and `.md` when that split improves usability, but do not create markdown duplicates of the final-pack source documents unless explicitly requested

## Repository Shape
- [`docs/`](./docs/): polished learner-facing guides, roadmap, checklist, and mentor guide
- [`data/`](./data/): synthetic trial-style CSVs and dataset notes
- [`Dad_Stuff/`](./Dad_Stuff/): helper scripts and supporting working materials
- [`ENVIRONMENT_NOTES.md`](./ENVIRONMENT_NOTES.md): accumulated practical setup, sandbox, and runtime notes for this repo
- [`.codex/`](./.codex/): Codex configuration and repo-local safety rules

## Project Outcomes
Work in this repo should support one or more of these outcomes:
- Clear, beginner-friendly learning materials
- Portfolio-ready analytics artifacts
- Synthetic study datasets and supporting documentation
- Reusable practice exercises, challenge problems, or weekly checklists
- Repo hygiene and AI-safety guardrails for home learning

Expected capstone components:
- SQL queries for enrollment, visit progress, safety, or site performance
- A small Python data-quality or reporting script
- A Tableau dashboard
- An AI-assisted weekly study-status memo
- A strong README, data dictionary, limitations note, and privacy-safe design statement

## Non-Negotiable Safety Rules
- Use only synthetic, public, or clearly representative non-work data
- Do not add real patient data, PHI, screenshots from work systems, internal reports, credentials, or confidential material
- Do not paste work content into consumer AI tools
- Document data source, assumptions, and verification steps for every mini-project or major deliverable
- Keep public-facing outputs clean: no secrets, internal filenames, accidental local paths, or copied employer material

## Working Style
- Treat this as a mixed content repo where documents, datasets, and scripts all matter
- Prefer practical, lightweight solutions over over-engineered ones
- Preserve the repo's instructional tone: supportive, clear, non-intimidating, and execution-focused
- Optimize for visible progress and reusable artifacts rather than perfect coverage
- Prefer minimal targeted edits unless the task specifically asks for restructuring

## Learner and Mentor Roles
This repo assumes a paired workflow:
- The learner owns clinical framing, interpretation, and final storytelling
- Dad acts as engineering mentor and technical pair-programmer, not the primary author of the learning

Mentor contributions should center on:
- environment setup
- Git and GitHub hygiene
- debugging workflow
- Python pairing
- repo cleanup and security review
- modeling careful AI-assisted work

Avoid steering the work toward unnecessary engineering complexity.

## Weekly Execution Rules
The roadmap defines a weekly cadence. When adding or revising materials, stay aligned with:
- two learning sessions per week
- one build session
- one review, debug, or documentation session

Standing deliverable rules:
- Every deliverable should have a README or short lab note
- Keep a simple data dictionary and update it when fields change
- State the data source and confirm no real work data was used
- Treat AI output as a draft that must be reviewed and verified

## Data and Scripts
- Keep synthetic CSV schemas stable unless a deliberate change is required
- If datasets are regenerated, note the generator or workflow used
- Favor realistic clinical research entities such as sites, subjects, visits, adverse events, and protocol deviations
- Keep scripts simple, reproducible, and easy for a learner to inspect
- When changing datasets, update [`data/README_data.md`](./data/README_data.md) if row counts, schema, or dataset purpose changed

Synthetic data regeneration workflow:
- Run [`make_synthetic_trial_data.py`](./data/make_synthetic_trial_data.py) from the repo root: `python data\make_synthetic_trial_data.py`
- Review changes with `git status --short`
- Stage the generator and generated outputs: `git add data\make_synthetic_trial_data.py data\`
- Commit and push after verifying the regenerated files
- [`data/README_data.md`](./data/README_data.md) records the git commit that generated the dataset, so it normally points to the pre-commit revision used to create the files

## Git and Repo Safety
- Follow repo-local rules in [`.codex/rules/`](./.codex/rules/)
- Do not force-push, including `--force-with-lease`
- Ask before destructive cleanup or broad repository reorganization
- Maintain a clean, portfolio-appropriate repository structure and documentation set

## Repo-Local Skills
- [`session-summary-writer`](./.codex/skills/session-summary-writer/SKILL.md): use at the end of a work session to save a timestamped summary for Dad or Hannah, including accomplishments, approach, repo state, and next steps
- [`doc`](./.codex/skills/doc/SKILL.md): use when working with `.docx` documents, including inspection, extraction, comparison, and rendering workflows for Word files
- [`spreadsheet`](./.codex/skills/spreadsheet/SKILL.md): use when working with spreadsheets or workbook-style tabular data, including inspection of sheets, structure, and content
- Owner resolution for session summaries comes from `git remote get-url origin`: `geosmall` maps to Dad; any other GitHub owner maps to Hannah
- When the user appears to be ending a work session, remind them that a session summary can be saved with `session-summary-writer`
