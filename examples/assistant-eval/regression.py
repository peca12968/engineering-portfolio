"""Check whether two verified assistant evaluations meet a criterion-level regression gate."""

import argparse
import importlib
import json
from pathlib import Path
import sys


def upstream(root):
    root = root.resolve(strict=True)
    if not (root / "scripts/review_understanding.py").is_file():
        raise ValueError("找不到助理的離線評讀程式")
    sys.path.insert(0, str(root))
    return importlib.import_module("scripts.review_understanding")


def evaluate(before, after, suite, reviewer):
    checked = reviewer.compare(before, after, suite_bytes=suite)
    pairs = {row["id"]: row for row in checked["transitions"]}
    recorded = [{row["id"]: row.get("reviews", []) for row in report["results"]}
                for report in (before, after)]
    cases = []
    for name in before["case_ids"]:
        earlier, later = [reviews[name][-1]["result"] if reviews.get(name) else "pending"
                          for reviews in recorded]
        pair = pairs.get(name)
        lost = [] if pair is None else [
            index for index, (old, new) in enumerate(zip(pair["before_criteria_pass"],
                                                       pair["after_criteria_pass"], strict=True), 1)
            if old and not new
        ]
        cases.append({"id": name, "before": earlier, "after": later, "lost_criteria": lost})

    missing = set(checked["missing_source_fingerprint_ids"]) | set(checked["missing_prompt_ids"])
    groups = {
        "pending_review": checked["pending_ids"],
        "missing_source": [case["id"] for case in cases if case["id"] in missing],
        "unbound_review": [pair["id"] for pair in pairs.values()
                           if not (pair["before_evidence_bound"] and pair["after_evidence_bound"])],
        "reviewer_changed": checked["reviewer_changed_ids"],
        "criterion_regressed": [case["id"] for case in cases if case["lost_criteria"]],
    }
    reasons = [{"code": code, "ids": ids} for code, ids in groups.items() if ids]
    if not checked["suite_verified"] or not checked["runner_fingerprint_recorded"]:
        reasons.append({"code": "unverified_suite_or_runner", "ids": []})
    return {
        "verdict": "blocked" if reasons else "pass",
        "before_pass": sum(case["before"] == "pass" for case in cases),
        "after_pass": sum(case["after"] == "pass" for case in cases),
        "paired": checked["compared"],
        "cases": cases,
        "reasons": reasons,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--assistant-root", type=Path, required=True)
    parser.add_argument("--suite", type=Path, required=True)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    args = parser.parse_args()
    try:
        validator = upstream(args.assistant_root)
        with args.suite.open("rb") as stream:
            suite = stream.read(validator.MAX_JSON_BYTES + 1)
        result = evaluate(validator.load_json(args.baseline), validator.load_json(args.candidate), suite, validator)
    except (OSError, ImportError, ValueError, KeyError) as error:
        print(str(error), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
