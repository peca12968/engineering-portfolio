"""Verify that every portfolio row points to files from its successful CI run."""
import argparse
from pathlib import Path
import json
import re
import subprocess
import sys
import time
from urllib.parse import unquote

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


def file_presence(prefix, sha, paths, lookup):
    root = lookup(f"{prefix}/git/trees/{sha}?recursive=1")
    blobs = {entry["path"] for entry in root["tree"] if entry["type"] == "blob"}
    if not root["truncated"]:
        return [path in blobs for path in paths]

    subtrees = {}

    def find(path):
        if path in blobs:
            return True
        revision = root["sha"]
        pieces = path.split("/")
        for index, piece in enumerate(pieces):
            if revision not in subtrees:
                tree = lookup(f"{prefix}/git/trees/{revision}")
                if tree["truncated"]:
                    raise RuntimeError(f"Cannot verify {path} in a truncated Git subtree")
                subtrees[revision] = {entry["path"]: entry for entry in tree["tree"]}
            entry = subtrees[revision].get(piece)
            if index == len(pieces) - 1:
                return entry is not None and entry["type"] == "blob"
            if not entry or entry["type"] != "tree":
                return False
            revision = entry["sha"]
        return False

    return [find(path) for path in paths]


def verify(row, lookup=api):
    names, files, runs = REPO.findall(row), BLOB.findall(row), RUN.findall(row)
    if len(names) != 1 or len(files) != 2 or len(runs) != 1:
        raise ValueError(f"Expected a project, two files and a CI run: {row}")
    repo = names[0]
    if runs[0][0] != repo or any(owner != repo for owner, _, _ in files):
        raise ValueError(f"{repo}: evidence must belong to the same project")
    evidence = [
        {"sha": rev, "path": unquote(path), "exists": None} for _, rev, path in files
    ]
    if len({file["path"] for file in evidence}) != 2:
        raise ValueError(f"{repo}: implementation and test links must point to distinct files")
    prefix = f"repos/peca12968/{repo}"
    run_id = runs[0][1]
    run = lookup(f"{prefix}/actions/runs/{run_id}")
    ci = {"id": run_id, "sha": run["head_sha"], "status": run["status"], "conclusion": run["conclusion"]}
    issues = []
    owner_repo = f"peca12968/{repo}"
    if any((run.get(key) or {}).get("full_name", "").casefold() != owner_repo.casefold()
           for key in ("repository", "head_repository")):
        issues.append("repository_mismatch")
    if ci["status"] != "completed" or ci["conclusion"] != "success":
        issues.append("ci_not_successful")
    if any(file["sha"] != ci["sha"] for file in evidence):
        issues.append("revision_mismatch")
    if not issues:
        found = file_presence(prefix, ci["sha"], [file["path"] for file in evidence], lookup)
        for file, exists in zip(evidence, found):
            file["exists"] = exists
        if not all(found):
            issues.append("file_missing")
    return {"repository": repo, "ci": ci, "files": evidence, "issues": issues}


def report(text, highlights, lookup=api):
    header = "| 作品 | 使用技術 | 可重現的情境 | 驗證 |"
    _, marker, body = text.partition(header)
    if not marker:
        raise ValueError("Missing portfolio table header")
    table = body.strip().split("\n\n", 1)[0].splitlines()
    rows = table[1:]  # The first line contains Markdown column separators.
    if not rows:
        raise ValueError("No portfolio rows found")
    count = re.search(r"目前收錄 \*\*(\d+)\*\* 個", text)
    if count and int(count[1]) != len(rows):
        raise ValueError(f"Introduction says {count[1]} projects but the table contains {len(rows)}")
    names = [REPO.findall(row) for row in rows]
    if any(len(links) != 1 for links in names):
        raise ValueError("Each portfolio row must link to exactly one project")
    projects = {links[0] for links in names}
    if len(projects) != len(rows):
        raise ValueError("Duplicate project row")
    unlisted = set(REPO.findall(text)) - set(projects)
    if unlisted:
        raise ValueError(f"Project links without a verified portfolio row: {sorted(unlisted)}")
    verify_highlights(highlights, rows)
    entries = [verify(row, lookup) for row in rows]
    return {"format": "peca12968.portfolio-evidence.v1", "ok": all(not entry["issues"] for entry in entries),
            "projects": entries}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="write a structured evidence report to stdout")
    args = parser.parse_args()
    try:
        text = Path(__file__).with_name("README.md").read_text(encoding="utf-8")
        highlights = Path(__file__).with_name("resume-projects.md").read_text(encoding="utf-8")
        result = report(text, highlights)
    except (OSError, ValueError, RuntimeError) as error:
        print(str(error), file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for entry in result["projects"]:
            name = entry["repository"]
            if entry["issues"]:
                print(f"{name}: {', '.join(entry['issues'])}", file=sys.stderr)
            else:
                print(f"{name} {entry['ci']['sha'][:7]} verified")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
