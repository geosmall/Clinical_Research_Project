# Environment Notes

Practical environment and sandbox notes for this repository. Use this file for repeatable local setup tips, runtime workarounds, and tool-specific gotchas that do not belong in the main README.

## Matplotlib in the sandbox

- `matplotlib` is available in the repo `.venv`, not in the system Python.
- In this sandbox, `matplotlib` may fail or emit permission warnings if it tries to use the default user cache directory.
- Before running scripts that import `matplotlib`, set `MPLCONFIGDIR` to a writable repo-local folder:

```powershell
New-Item -ItemType Directory -Force tmp\mpl | Out-Null
$env:MPLCONFIGDIR = (Resolve-Path tmp\mpl).Path
.\.venv\Scripts\python.exe your_script.py
```

- Non-GUI rendering works with the `Agg` backend in this environment.

## Git pushes from this environment

- `git push` requires escalated permissions in this sandbox because normal network access is blocked.
- Use a longer timeout for push commands because the operation may wait for user approval before the network call starts.
- A very short timeout like `1000 ms` is not reliable for push commands in this environment.
