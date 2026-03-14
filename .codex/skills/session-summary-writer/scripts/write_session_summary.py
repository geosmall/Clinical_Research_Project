import argparse
import subprocess
from datetime import datetime
from pathlib import Path


OWNER_DIRS = {
    "dad": Path("Dad_Stuff") / "session_summaries",
    "hannah": Path("Hannah_Stuff") / "session_summaries",
}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Write a timestamped session summary with repository metadata."
    )
    parser.add_argument("--summary", required=True, help="Short paragraph summarizing the session.")
    parser.add_argument(
        "--accomplishment",
        action="append",
        default=[],
        help="Repeatable bullet for what was accomplished.",
    )
    parser.add_argument(
        "--approach",
        action="append",
        default=[],
        help="Repeatable bullet for how the work was done.",
    )
    parser.add_argument(
        "--next-step",
        action="append",
        default=[],
        help="Repeatable bullet for likely follow-up work.",
    )
    parser.add_argument(
        "--repo-note",
        action="append",
        default=[],
        help="Repeatable bullet for manual repo-state notes.",
    )
    parser.add_argument(
        "--title",
        default="Session Summary",
        help="Optional title prefix used in the document heading.",
    )
    return parser.parse_args()


def find_repo_root():
    current = Path.cwd().resolve()
    for candidate in [current, *current.parents]:
        if (candidate / ".git").exists():
            return candidate
    raise SystemExit("Could not find repository root from current working directory.")


def run_git(repo_root, *args):
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=repo_root,
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return ""


def resolve_owner(repo_root):
    remote_url = run_git(repo_root, "remote", "get-url", "origin")
    if not remote_url:
        raise SystemExit("Could not determine owner because origin remote is missing.")

    remote_url = remote_url.strip()
    owner_token = ""
    if remote_url.startswith("git@github.com:"):
        owner_token = remote_url.split(":", 1)[1].split("/", 1)[0]
    elif "github.com/" in remote_url:
        owner_token = remote_url.split("github.com/", 1)[1].split("/", 1)[0]

    if not owner_token:
        raise SystemExit(f"Could not parse GitHub owner from origin URL: {remote_url}")

    return "dad" if owner_token.lower() == "geosmall" else "hannah"


def bullet_lines(items):
    if not items:
        return ["- None recorded"]
    return [f"- {item}" for item in items]


def main():
    args = parse_args()
    repo_root = find_repo_root()
    owner = resolve_owner(repo_root)
    now = datetime.now()
    timestamp_display = now.strftime("%Y-%m-%d %H:%M:%S")
    date_slug = now.strftime("%Y-%m-%d")

    branch = run_git(repo_root, "branch", "--show-current") or "(unknown branch)"
    origin_url = run_git(repo_root, "remote", "get-url", "origin") or "(unknown remote)"
    head_full = run_git(repo_root, "rev-parse", "HEAD") or "(unknown commit)"
    head_short = run_git(repo_root, "rev-parse", "--short", "HEAD") or "(unknown commit)"
    last_commit = run_git(repo_root, "log", "-1", "--format=%h %ad %s", "--date=iso-local") or "(unknown)"
    status_output = run_git(repo_root, "status", "--short")
    status_lines = status_output.splitlines() if status_output else ["Working tree clean"]

    output_dir = repo_root / OWNER_DIRS[owner]
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{date_slug}_{owner}_session_summary.md"

    content_lines = [
        f"# {args.title}",
        "",
        f"- Owner: {owner.title()}",
        f"- Timestamp: {timestamp_display}",
        f"- Repository: `{repo_root}`",
        "",
        "## Summary",
        "",
        args.summary.strip(),
        "",
        "## Accomplishments",
        "",
        *bullet_lines(args.accomplishment),
        "",
        "## How It Was Done",
        "",
        *bullet_lines(args.approach),
        "",
        "## Repo State",
        "",
        f"- Branch: `{branch}`",
        f"- Origin: `{origin_url}`",
        f"- HEAD: `{head_short}` (`{head_full}`)",
        f"- Latest commit: `{last_commit}`",
        f"- Summary file: `{output_path}`",
        *bullet_lines(args.repo_note),
        "",
        "### Working Tree Status",
        "",
        *[f"- `{line}`" for line in status_lines],
        "",
        "## Next Steps",
        "",
        *bullet_lines(args.next_step),
        "",
    ]

    output_path.write_text("\n".join(content_lines), encoding="utf-8")
    print(output_path)


if __name__ == "__main__":
    main()
