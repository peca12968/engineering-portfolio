"""Verify that every portfolio row points to files from its successful CI run."""
from pathlib import Path
import json
import re
import subprocess

BASE = r"https://github\.com/peca12968/"
REPO = re.compile(BASE + r"([a-z0-9-]+)\)")
BLOB = re.compile(BASE + r"([a-z0-9-]+)/blob/([a-f0-9]{40})/([^\s)]+)\)")
RUN = re.compile(BASE + r"([a-z0-9-]+)/actions/runs/(\d+)\)")


def api(path):
    return json.loads(subprocess.check_output(["gh", "api", path], encoding="utf-8"))


def verify(row):
    names, files, runs = REPO.findall(row), BLOB.findall(row), RUN.findall(row)
    if len(names) != 1 or len(files) != 2 or len(runs) != 1:
        raise ValueError(f"Expected a project, two files and a CI run: {row}")
    repo = names[0]
    if runs[0][0] != repo or any(owner != repo for owner, _, _ in files):
        raise ValueError(f"{repo}: evidence must belong to the same project")
    prefix = f"repos/peca12968/{repo}"
    run = api(f"{prefix}/actions/runs/{runs[0][1]}")
    sha = run["head_sha"]
    if run["conclusion"] != "success" or any(rev != sha for _, rev, _ in files):
        raise ValueError(f"{repo}: the linked revision must match a successful run")
    tree = api(f"{prefix}/git/trees/{sha}?recursive=1")
    paths = {entry["path"] for entry in tree["tree"] if entry["type"] == "blob"}
    if any(path not in paths for _, _, path in files):
        raise ValueError(f"{repo}: source or test file missing at {sha}")
    print(f"{repo} {sha[:7]} verified")
    return repo


def main():
    text = Path(__file__).with_name("README.md").read_text(encoding="utf-8")
    header = "| 作品 | 使用技術 | 可重現的情境 | 驗證 |"
    table = text.split(header, 1)[1].strip().split("\n\n", 1)[0].splitlines()
    rows = table[1:]  # The first line contains Markdown column separators.
    if not rows:
        raise ValueError("No portfolio rows found")
    count = re.search(r"目前收錄 \*\*(\d+)\*\* 個", text)
    if count and int(count[1]) != len(rows):
        raise ValueError(f"Introduction says {count[1]} projects but the table contains {len(rows)}")
    projects = [verify(row) for row in rows]
    if len(set(projects)) != len(projects):
        raise ValueError("Duplicate project row")
    unlisted = set(REPO.findall(text)) - set(projects)
    if unlisted:
        raise ValueError(f"Project links without a verified portfolio row: {sorted(unlisted)}")


if __name__ == "__main__":
    main()
