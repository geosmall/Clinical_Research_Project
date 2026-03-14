# Clinical_Research_Project
Skill-building road-map for clinical research data analysis covering SQL, Tableau, Python, REDCap, AI tools, and GitHub

# What we're building:
An 8-week self-paced learning plan for the daughter to become a more competitive clinical research data analyst, with the dad serving as engineering mentor and technical pair-programmer (not teacher).

# Documents created so far:

READ_THIS_FIRST_Overview.docx — A friendly, non-intimidating one-pager introducing the plan
Clinical_Research_Skill_Building_Roadmap_REVISED.docx — The full 8-week plan covering SQL (Weeks 1–2), Tableau + Statistics (Weeks 3–4), Python + REDCap (Week 5), AI Tools & Agents (Week 6), GitHub & Portfolio (Week 7), and Integration Capstone (Week 8). Includes parallel tracks for Advanced Excel, SAS Awareness, and CDISC Standards. Has HIPAA guardrails section and Job Market Competitiveness Map.
Dads_Guide_Engineer_Edition.docx — Companion guide for Dad covering: where his skills transfer vs. where he'll learn alongside her, his specific role each week, Claude Code as a teaching weapon, Engineer-Dad Traps to avoid, pre-work checklist, and a Claude Desktop/Cowork safety guide with VM sandbox instructions (UTM for Mac, Hyper-V for Win11).

# Key principles:

All learning projects use only synthetic or public data (Synthea, ClinicalTrials.gov, CMS public files) — never real patient data
HIPAA compliance and data privacy are woven throughout, not treated as an afterthought
She drives the learning; Dad helps with environment setup, debugging, Git, code review, and AI workflow modeling
Her clinical research domain knowledge is the career advantage — the technical tools layer on top
Everything goes into a GitHub portfolio that demonstrates skills to employers
Claude Desktop/Cowork use requires safety precautions: dedicated workspace folders, current backups, and optionally VM isolation

# Goals for this project space:

Iterate on and update the three documents as needed
Develop supplementary materials (practice exercises, challenge problems, weekly checklists)
Track progress and adjust the plan based on what's working
Answer questions about SQL, Tableau, Python, REDCap, AI tools, GitHub, HIPAA, and clinical research data workflows as they come up during the learning journey

# Regenerating synthetic data

Run the generator from the repo root:

`python Dad_Stuff\synthetic_trial_data\make_synthetic_trial_data.py`

Then review and publish changes:

`git status --short`

`git add Dad_Stuff\synthetic_trial_data\make_synthetic_trial_data.py data\`

`git commit -m "Update synthetic trial dataset"`

`git push origin main`

Note: [`data/README_data.md`](D:/Codex/Clinical_Research_Project/data/README_data.md) records the git commit used to generate the dataset, so it typically refers to the revision just before the commit that publishes the regenerated files.
