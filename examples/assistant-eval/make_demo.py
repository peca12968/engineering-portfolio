"""Replay hand-authored examples through the assistant's offline evidence validator."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import subprocess

from regression import evaluate, upstream

ROOT = Path(__file__).resolve().parent
CASE_DEFS = [
    {"id": "citation", "category": "來源", "prompt": "為採購單 A 引用來源行。",
     "criteria": ["使用採購單 A", "提供行號"]},
    {"id": "count", "category": "數量", "prompt": "總箱數是 18，只回覆數字。",
     "criteria": ["總箱數正確", "只回覆數字"]},
    {"id": "scope", "category": "範圍", "prompt": "只確認二樓的收貨口。",
     "criteria": ["維持二樓範圍", "避免引用一樓"]},
    {"id": "wait", "category": "追問", "prompt": "不知道取件日，先列待確認項目。",
     "criteria": ["標出待確認狀態", "只追問缺少的日期"]},
]
BASE_STATES = [(True, True), (True, True), (True, False), (False, True)]


def sha(value):
    return hashlib.sha256(value).hexdigest()


def report(validator, states, suite, runner):
    rows = [{**case, "source_sha256": sha(case["prompt"].encode("utf-8")),
             "answer": "合成評讀用文字 " + case["id"]} for case in CASE_DEFS]
    result = {"format_version": 1, "mode": "portfolio_synthetic",
              "case_ids": [case["id"] for case in CASE_DEFS],
              "fingerprint": {"suite_sha256": sha(suite), "runner_sha256": runner},
              "results": rows}
    reviews = [{"id": row["id"], "criteria_pass": list(state), "note": "合成的固定示範評分"}
               for row, state in zip(rows, states, strict=True) if state is not None]
    return validator.apply_reviews(result, reviews, "development_agent")


def samples(validator, runner):
    suite = json.dumps(CASE_DEFS, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    baseline = report(validator, BASE_STATES, suite, runner)
    full = report(validator, [(True, True)] * 4, suite, runner)
    regression = report(validator, [(True, False)] + [(True, True)] * 3, suite, runner)
    incomplete = report(validator, [None] + [(True, True)] * 3, suite, runner)
    changed = deepcopy(full)
    changed["results"][0]["reviews"][-1]["reviewer"] = "independent_reviewer"
    return suite, baseline, {
        "improved": full,
        "regression": regression,
        "pending": incomplete,
        "reviewer": changed,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--assistant-root", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = args.assistant_root.resolve(strict=True)
    rev = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    dirty = subprocess.check_output(["git", "-C", str(root), "status", "--porcelain", "--", "assistant", "scripts"],
                                    text=True)
    if dirty:
        raise SystemExit("重跑展示時請使用乾淨的助理工作樹")
    validator = upstream(root)
    runner = sha((root / "scripts/review_understanding.py").read_bytes())
    suite, baseline, variants = samples(validator, runner)
    result = {"format": "assistant-regression-demo.v1", "assistant_sha": rev,
              "suite_sha256": sha(suite),
              "labels": {case["id"]: case["category"] for case in CASE_DEFS},
              "scenarios": [{"scenario": name, **evaluate(baseline, candidate, suite, validator)}
                            for name, candidate in variants.items()]}
    if args.check:
        saved = json.loads((ROOT / "sample.json").read_text(encoding="utf-8"))
        if saved != result:
            raise SystemExit("合成評測輸出與已發表樣本不同")
        print("4 synthetic comparisons reproduced")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
