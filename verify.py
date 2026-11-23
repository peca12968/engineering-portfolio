"""Verify that every portfolio row points to files from its successful CI run."""
from pathlib import Path
import json
import re
import subprocess
import time

BASE = r"https://github\.com/peca12968/"
REPO = re.compile(BASE + r"([a-z0-9-]+)\)")
BLOB = re.compile(BASE + r"([a-z0-9-]+)/blob/([a-f0-9]{40})/([^\s)]+)\)")
RUN = re.compile(BASE + r"([a-z0-9-]+)/actions/runs/(\d+)\)")


def api(path):
    for attempt in range(3):
        result = subprocess.run(["gh", "api", path], capture_output=True, encoding="utf-8")
        if result.returncode == 0:
            return json.loads(result.stdout)
        transient = re.search(r"i/o timeout|connection reset|TLS handshake timeout|HTTP 50[234]", result.stderr, re.I)
        if not transient or attempt == 2:
            raise RuntimeError(f"{path}: {result.stderr.strip()}")
        time.sleep(2 ** attempt)


def verify_highlights(text, rows):
    sections = re.split(r"^### ", text, flags=re.M)[1:]
    if not sections:
        raise ValueError("Missing resume project sections")
    for section in sections:
        files, runs = BLOB.findall(section), RUN.findall(section)
        if not files or not runs:
            raise ValueError(f"Missing resume evidence: {section.splitlines()[0]}")
        for file in files:
            if not any(file in BLOB.findall(row) and set(runs).intersection(RUN.findall(row)) for row in rows):
                raise ValueError(f"Resume evidence must match its verified portfolio row: {file}")
        if any(not any(run in RUN.findall(row) and set(files).intersection(BLOB.findall(row)) for row in rows)
               for run in runs):
            raise ValueError("Resume CI link has no matching evidence")


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
    highlights = Path(__file__).with_name("resume-projects.md").read_text(encoding="utf-8")
    verify_highlights(highlights, rows)


if __name__ == "__main__":
    main()
