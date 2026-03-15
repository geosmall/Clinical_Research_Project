# Setup Environment

Use a repo-local Python virtual environment at `.venv` so scripts and skills run consistently in PowerShell and VS Code.

## Windows Python Requirement

Use a standard Python installation from `python.org`, not the Microsoft Store alias or Store-managed shim.

Before creating `.venv`, verify that `python` resolves to a real Python install:

```powershell
Get-Command python
python --version
```

The command should point to a normal Python install path such as `C:\Users\<you>\AppData\Local\Programs\Python\Python313\python.exe`.

If `python` points to `...\Microsoft\WindowsApps\python.exe`, opens the Microsoft Store, or resolves to the Store stub:

1. Open `Settings` -> `Apps` -> `Advanced app settings` -> `App execution aliases`
2. Turn off the aliases for `python.exe` and `python3.exe`
3. Make sure the real Python install path is ahead of `WindowsApps` in your user `Path`
4. Open a new PowerShell window and rerun:

```powershell
Get-Command python
python --version
```

## Standard Setup

From the repo root:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

This is the preferred setup path for a fresh clone.

## Verify `.venv` Creation

After creation, confirm the environment Python is the repo-local one:

```powershell
.\.venv\Scripts\python.exe --version
Get-Command .\.venv\Scripts\python.exe
```

Then install dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

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
.\.venv\Scripts\python.exe data\make_synthetic_trial_data.py
```

Use the same pattern for the SQLite import script and other repo-local helpers.

## Environment Notes

See [ENVIRONMENT_NOTES.md](./ENVIRONMENT_NOTES.md) for sandbox-specific notes such as:

- `matplotlib` cache configuration with `MPLCONFIGDIR`
- `.docx` rendering tool requirements beyond `requirements.txt`
- Git push behavior in this environment
