"""Offline checks for preserving personal data and evidence/state boundaries."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

import job_search as js


class StarterTests(unittest.TestCase):
    def test_init_is_blank_and_refuses_to_overwrite_personal_records(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "workspace"
            js.initialize(root)
            candidate = root / "profile/candidate.md"
            self.assertNotIn("Riley Morgan", candidate.read_text())
            self.assertEqual(js.inspect(root)[0], [])
            candidate.write_text("My actual personal record\n")
            with self.assertRaises(ValueError):
                js.initialize(root)
            self.assertEqual(candidate.read_text(), "My actual personal record\n")

    def test_demo_checks_read_only_and_does_not_create_personal_workspace(self):
        root = js.REPO / "examples"
        personal_existed = (js.REPO / "workspace").exists()
        before = {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()}
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(js.main(["demo"]), 0)
            self.assertEqual(js.main(["check", "--root", str(root)]), 0)
        after = {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)
        self.assertEqual((js.REPO / "workspace").exists(), personal_existed)

    def test_crm_preview_allowlist_preserves_stage_and_lock(self):
        roles, _, _, errors = js.inspect(js.REPO / "examples")
        self.assertEqual(errors, [])
        preview = js.crm_preview(roles)
        cedar = next(item for item in preview if item["company"] == "Cedarline Labs")
        self.assertEqual(cedar["local_stage"], "Informational interview")
        self.assertTrue(cedar["board_lock"])
        self.assertTrue(cedar["fictional"])
        self.assertEqual(set(cedar), {"company", "role", "requisition", "decision", "local_stage",
                                      "verification_status", "fictional", "source_file", "board_lock"})

    def test_populated_paths_do_not_establish_research_completion(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "workspace"
            js.initialize(root)
            (root / "opportunities/company-list.csv").write_text(
                "List,Advocacy,Networking path 1,Networking path 2,Motivation,Posting\n"
                "Some Company,Yes,Known route,,3,\n"
            )
            _, rows, checkpoints, errors = js.inspect(root)
            self.assertEqual(errors, [])
            self.assertEqual(rows[0]["Advocacy"], "Yes")
            self.assertEqual(checkpoints, {})

    def test_research_requires_in_root_evidence_and_real_roles_reject_example_urls(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "workspace"
            js.initialize(root)
            outside = Path(temp) / "outside.md"
            outside.write_text("Not in this data root\n")
            (root / "research/company-status.json").write_text(json.dumps({
                "schema_version": 1, "companies": {"some company": {
                    "networking": {"status": "researched", "date": "2025-04-10", "evidence": "../outside.md"}
                }}
            }))
            (root / "opportunities/roles/example.md").write_text(
                "# Role\n- Company: Example\n- Role: Product\n- Decision: Watch\n"
                "- Pipeline: Research\n- Verification status: Active\n"
                "- Last verified: 2025-04-10\n- Official posting: https://company.example/jobs\n"
            )
            issues = js.inspect(root)[3]
            self.assertTrue(any("outside data root" in issue for issue in issues))
            self.assertTrue(any("cannot verify a real role" in issue for issue in issues))

    def test_invalid_inputs_fail_without_rewriting(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "workspace"
            js.initialize(root)
            path = root / "opportunities/roles/invalid.md"
            text = ("# Invalid\n- Company: Example\n- Role: Product\n- Decision: Sure\n"
                    "- Pipeline: Unlisted\n- Verification status: Unverified\n- CRM board lock: maybe\n")
            path.write_text(text)
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(js.main(["check", "--root", str(root)]), 1)
            self.assertEqual(path.read_text(), text)


if __name__ == "__main__":
    unittest.main()
