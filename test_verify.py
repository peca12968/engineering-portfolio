import unittest

from verify import report, verify


SHA = "a" * 40
OTHER = "b" * 40
PREFIX = "repos/peca12968/food"
URL = "https://github.com/peca12968/food"
ROW = (
    f"| [作品]({URL}) | Python | 說明 | "
    f"[實作]({URL}/blob/{SHA}/docs/README.md) · "
    f"[測試]({URL}/blob/{SHA}/docs/test%20suite.py) · [CI]({URL}/actions/runs/42) |"
)
RUN = {
    "head_sha": SHA,
    "status": "completed",
    "conclusion": "success",
    "repository": {"full_name": "peca12968/food"},
    "head_repository": {"full_name": "peca12968/food"},
}


class VerifyTest(unittest.TestCase):
    def fixture(self, run=RUN, trees=None):
        self.calls = []
        responses = {f"{PREFIX}/actions/runs/42": run, **(trees or {})}

        def fetch(path):
            self.calls.append(path)
            return responses[path]

        return fetch

    def test_truncated_tree_checks_only_target_subtrees(self):
        lookup = self.fixture(trees={
            f"{PREFIX}/git/trees/{SHA}?recursive=1": {"sha": "root", "truncated": True, "tree": []},
            f"{PREFIX}/git/trees/root": {
                "truncated": False, "tree": [
                    {"path": "docs", "type": "tree", "sha": "docs"},
                    {"path": "unrelated", "type": "tree", "sha": "unrelated"},
                ],
            },
            f"{PREFIX}/git/trees/docs": {
                "truncated": False, "tree": [
                    {"path": "README.md", "type": "blob"},
                    {"path": "test suite.py", "type": "blob"},
                ],
            },
        })
        result = verify(ROW, lookup)
        self.assertEqual(result["issues"], [])
        self.assertEqual(result["files"][1], {"sha": SHA, "path": "docs/test suite.py", "exists": True})
        self.assertEqual(self.calls.count(f"{PREFIX}/git/trees/docs"), 1)
        self.assertNotIn(f"{PREFIX}/git/trees/unrelated", self.calls)

    def test_absent_test_path_is_distinct_from_unchecked(self):
        lookup = self.fixture(trees={
            f"{PREFIX}/git/trees/{SHA}?recursive=1": {"truncated": False, "tree": [
                {"path": "docs/README.md", "type": "blob"},
                {"path": "docs/test suite.py", "type": "tree"},
            ]},
        })
        result = verify(ROW, lookup)
        self.assertEqual(result["issues"], ["file_missing"])
        self.assertEqual([e["exists"] for e in result["files"]], [True, False])

    def test_ci_for_the_wrong_commit_or_fork_never_checks_files(self):
        for run, issue in [
            ({**RUN, "head_sha": OTHER}, "revision_mismatch"),
            ({**RUN, "conclusion": None, "status": "queued"}, "ci_not_successful"),
            ({**RUN, "head_repository": {"full_name": "fork/food"}}, "repository_mismatch"),
        ]:
            with self.subTest(issue=issue):
                result = verify(ROW, self.fixture(run))
                self.assertEqual(result["issues"], [issue])
                self.assertEqual([e["exists"] for e in result["files"]], [None, None])
                self.assertEqual(self.calls, [f"{PREFIX}/actions/runs/42"])

    def test_report_checks_resume_correspondence_and_retains_failed_ci(self):
        text = "目前收錄 **1** 個\n\n| 作品 | 使用技術 | 可重現的情境 | 驗證 |\n| --- | --- | --- | --- |\n" + ROW
        resume = f"### 作品\n[實作]({URL}/blob/{SHA}/docs/README.md) [CI]({URL}/actions/runs/42)"
        result = report(text, resume, self.fixture({**RUN, "conclusion": "failure"}))
        self.assertEqual(result["format"], "peca12968.portfolio-evidence.v1")
        self.assertFalse(result["ok"])
        self.assertEqual(result["projects"][0]["issues"], ["ci_not_successful"])
        with self.assertRaisesRegex(ValueError, "Resume evidence"):
            report(text, resume.replace("runs/42", "runs/18"), self.fixture())


if __name__ == "__main__":
    unittest.main()
