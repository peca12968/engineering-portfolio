from copy import deepcopy
import json
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from make_demo import BASE_STATES, report, samples
from regression import evaluate, upstream


class ReleaseGateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = upstream(Path(os.environ["ASSISTANT_EVAL_REFERENCE"]))

    def setUp(self):
        self.runner = "a" * 64
        self.suite, self.baseline, self.variants = samples(self.validator, self.runner)

    def check(self, candidate):
        return evaluate(self.baseline, candidate, self.suite, self.validator)

    def test_champion_improves_without_any_regression(self):
        result = self.check(self.variants["improved"])
        self.assertEqual((result["verdict"], result["before_pass"], result["after_pass"]), ("pass", 2, 4))
        self.assertEqual(result["reasons"], [])

    def test_overall_gain_can_hide_a_case_regression(self):
        result = self.check(self.variants["regression"])
        self.assertEqual((result["verdict"], result["before_pass"], result["after_pass"]), ("blocked", 2, 3))
        self.assertEqual(result["reasons"], [{"code": "criterion_regressed", "ids": ["citation"]}])
        self.assertEqual(result["cases"][0]["lost_criteria"], [2])

    def test_case_that_remains_failed_can_still_lose_a_criterion(self):
        states = [*BASE_STATES[:2], (False, True), BASE_STATES[3]]
        outcome = self.check(report(self.validator, states, self.suite, self.runner))
        scope = outcome["cases"][2]
        self.assertEqual((scope["before"], scope["after"], scope["lost_criteria"]), ("fail", "fail", [1]))
        self.assertEqual(outcome["verdict"], "blocked")

    def test_pending_and_reviewer_changes_cannot_clear_the_gate(self):
        for key, reason in [("pending", "pending_review"), ("reviewer", "reviewer_changed")]:
            with self.subTest(key=key):
                outcome = self.check(self.variants[key])
                self.assertEqual(outcome["verdict"], "blocked")
                self.assertEqual(outcome["reasons"], [{"code": reason, "ids": ["citation"]}])

    def test_missing_source_or_review_binding_is_explicit(self):
        baseline, candidate = deepcopy(self.baseline), deepcopy(self.variants["improved"])
        for side in [baseline, candidate]:
            row = side["results"][0]
            del row["reviews"][-1]["evidence_sha256"]
            del row["source_sha256"]
        outcome = evaluate(baseline, candidate, self.suite, self.validator)
        self.assertEqual(outcome["reasons"], [
            {"code": "missing_source", "ids": ["citation"]},
            {"code": "unbound_review", "ids": ["citation"]},
        ])

    def test_wrong_suite_or_modified_answer_rejects_the_comparison(self):
        candidate = self.variants["improved"]
        with self.assertRaises(ValueError):
            evaluate(self.baseline, candidate, self.suite + b" ", self.validator)
        candidate["results"][0]["answer"] += "!"
        with self.assertRaises(ValueError):
            self.check(candidate)

    def test_command_reports_blocked_cases_and_returns_nonzero(self):
        with TemporaryDirectory() as folder:
            work = Path(folder)
            suite, before, after = (work / name for name in ("suite.json", "before.json", "after.json"))
            suite.write_bytes(self.suite)
            before.write_text(json.dumps(self.baseline), encoding="utf-8")
            after.write_text(json.dumps(self.variants["regression"]), encoding="utf-8")
            result = subprocess.run([sys.executable, "-X", "utf8", "-B", str(Path(__file__).with_name("regression.py")),
                                     "--assistant-root", os.environ["ASSISTANT_EVAL_REFERENCE"],
                                     "--suite", str(suite), "--baseline", str(before), "--candidate", str(after)],
                                    capture_output=True, encoding="utf-8", timeout=20)
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertEqual(json.loads(result.stdout)["cases"][0]["lost_criteria"], [2])
            self.assertNotIn("合成評讀用文字", result.stdout)


if __name__ == "__main__":
    unittest.main()
