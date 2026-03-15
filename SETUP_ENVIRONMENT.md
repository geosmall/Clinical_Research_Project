# Setup Environment

This repository uses a local Python virtual environment at `.venv`.

## Create the Virtual Environment

From the repo root:

```powershell
python -m venv .venv
```

## Activate the Virtual Environment

In PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can still run commands directly with:

```powershell
.\.venv\Scripts\python.exe --version
```

## Install Python Dependencies

From the repo root:

```powershell
python -m pip install -r requirements.txt
```

Or without activating the environment:

```powershell
python -m pip --python .venv\Scripts\python.exe install -r requirements.txt
```

## Current Dependency Set

The current `requirements.txt` supports the repo-local document and spreadsheet skills:

- `python-docx`
- `pdf2image`
- `openpyxl`
- `pandas`
- `matplotlib`

## Matplotlib Cache Note

In this environment, `matplotlib` may try to write to a blocked user cache path. Set `MPLCONFIGDIR` to a writable repo-local folder before using scripts that import `matplotlib`.

```powershell
New-Item -ItemType Directory -Force tmp\mpl | Out-Null
$env:MPLCONFIGDIR = (Resolve-Path tmp\mpl).Path
```

## DOCX Rendering Note

The repo-local `doc` skill can read `.docx` content with Python now, but full page rendering still requires system tools that are not part of `requirements.txt`:

- LibreOffice (`soffice`)
- Poppler (`pdftoppm`)

Without those tools, `.docx` inspection works for structured text extraction and editing, but not for full visual page rendering.

## Recommended Usage

Run Python scripts with the repo-local environment:

```powershell
.\.venv\Scripts\python.exe Dad_Stuff\synthetic_trial_data_generator\make_synthetic_trial_data.py
```

Use the same pattern for repo-local scripts and skill helpers when possible.
