---
name: session-summary-writer
description: Save an end-of-session summary for this repository, including timestamp, accomplishments, approach, repo state, and next steps. Use when the user asks to save, capture, log, or summarize the current session, especially at the end of a working session. The owner is resolved automatically from `git remote get-url origin`.
---

# Session Summary Writer

Write a concise Markdown session record for either Dad or Hannah.

If the user appears to be wrapping up the session, proactively remind them that this skill can save the session summary.

## Output locations

- Dad summaries go in `Dad_Stuff/session_summaries/`
- Hannah summaries go in `Hannah_Stuff/session_summaries/`

## Owner resolution

- Read `git remote get-url origin`
- If the GitHub owner is `geosmall`, write to Dad's summary folder
- Otherwise, write to Hannah's summary folder
- This assumes Dad owns the parent repo and Hannah is the only other fork user

## Workflow

1. Resolve the owner from `git remote get-url origin`.
2. Summarize the session in four parts:
   - short summary paragraph
   - accomplishments
   - how the work was done
   - next steps
3. Run `scripts/write_session_summary.py` from the repo root.
4. Let the script collect repository metadata automatically:
   - local timestamp
   - repo root
   - current branch
   - HEAD commit
   - latest commit subject
   - working tree status
5. Tell the user where the summary file was written.

## Command pattern

Use repeatable flags for bullet lists.

```powershell
python .codex\skills\session-summary-writer\scripts\write_session_summary.py `
  --summary "Short summary of the session." `
  --accomplishment "Built or changed X" `
  --approach "How the work was done at a high level" `
  --next-step "What to do next"
```

## Writing rules

- Keep summaries concise and factual.
- Prefer repository-relative paths when mentioning files in bullet text.
- Do not include secrets, tokens, or sensitive real-world data.
- If the working tree is dirty, keep that visible in the repo state section instead of hiding it.
