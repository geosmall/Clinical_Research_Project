# Setup Environment

Use a repo-local Python virtual environment at `.venv` so scripts and skills run consistently in PowerShell and VS Code.

## Standard Setup

From the repo root:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

This is the preferred setup path for a fresh clone.

## Activate the Environment

In PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If activation is blocked by local PowerShell policy, run the environment Python directly instead:

```powershell
.\.venv\Scripts\python.exe --version
```

## Verify the Environment

Use these quick checks from the repo root:

```powershell
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -m pip list
```

## Current Dependency Set

The current `requirements.txt` supports the repo-local document and spreadsheet skills:

- `python-docx`
- `pdf2image`
- `openpyxl`
- `pandas`
- `matplotlib`

## Recommended Usage

Run repo scripts with the environment Python, even if the shell is not activated:

```powershell
.\.venv\Scripts\python.exe Dad_Stuff\synthetic_trial_data_generator\make_synthetic_trial_data.py
```

Use the same pattern for the SQLite import script and other repo-local helpers.

## Environment Notes

See [ENVIRONMENT_NOTES.md](D:/Codex/Clinical_Research_Project/ENVIRONMENT_NOTES.md) for sandbox-specific notes such as:

- `matplotlib` cache configuration with `MPLCONFIGDIR`
- `.docx` rendering tool requirements beyond `requirements.txt`
- Git push behavior in this environment
