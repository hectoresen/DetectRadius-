"""Tests for PR-to-OpenSpec policy. Python standard library only."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/validate_sdd.py"
spec = importlib.util.spec_from_file_location("sdd_gate", SCRIPT)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class SddPolicyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.change = "detect-radius-ring"
        self.prefix = "openspec/changes/" + self.change + "/"
        directory = self.root / self.prefix
        (directory / "specs" / "material-tooltip").mkdir(parents=True)
        for name in ("proposal.md", "design.md", "tasks.md"):
            (directory / name).write_text("# Example\n", encoding="utf-8")
        (directory / "specs/material-tooltip/spec.md").write_text(
            "## ADDED Requirements\n### Requirement: Example\n", encoding="utf-8")
        (directory / "sdd-scope.json").write_text(
            json.dumps({"allowed_paths": ["addon/DetectRadius/**", "tests/**"]}))
        self.proposal = "OpenSpec-Change: " + self.change + "\nOpenSpec-Phase: proposal\n"
        self.implementation = (
            "OpenSpec-Change: " + self.change + "\n"
            "OpenSpec-Phase: implementation\nOpenSpec-Approval-PR: 9\n")

    @staticmethod
    def api(path, token):
        if path == "pulls/9":
            return {"merged_at": "2026-11-01T00:00:00Z",
                    "merged_by": {"login": "hectoresen"}, "base": {"ref": "main"}}
        if path.startswith("pulls/9/files"):
            return [{"filename": "openspec/changes/detect-radius-ring/proposal.md"}]
        raise AssertionError(path)

    def check(self, paths, body, number=42, present=False, api=None, created=None):
        return gate.validate(set(paths), body, number, root=self.root,
                             token="mock-token", api=api or self.api,
                             exists_in_base=lambda path: present, implementation_created=created)

    def test_new_proposal_passes(self):
        self.assertEqual(self.check({self.prefix + "proposal.md"}, self.proposal), [])

    def test_proposal_with_lua_fails(self):
        self.assertTrue(self.check({self.prefix + "proposal.md", "addon/DetectRadius/Core/Init.lua"},
                                   self.proposal))

    def test_proposal_reusing_old_id_fails(self):
        self.assertTrue(self.check({self.prefix + "proposal.md"}, self.proposal, present=True))

    def test_implementation_with_existing_approved_spec_passes(self):
        self.assertEqual(self.check({"addon/DetectRadius/Core/Init.lua"},
                                    self.implementation, present=True), [])

    def test_code_without_spec_metadata_fails(self):
        self.assertTrue(self.check({"addon/DetectRadius/Core/Init.lua"}, ""))

    def test_implementation_without_approval_fails(self):
        self.assertTrue(self.check({"addon/DetectRadius/Core/Init.lua"},
                                   self.implementation.replace("OpenSpec-Approval-PR: 9", ""),
                                   present=True))

    def test_implementation_spec_must_be_in_main(self):
        self.assertTrue(self.check({"addon/DetectRadius/Core/Init.lua"},
                                   self.implementation, present=False))

    def test_implementation_cannot_modify_approved_scope(self):
        self.assertTrue(self.check({"addon/DetectRadius/Core/Init.lua",
                                    self.prefix + "sdd-scope.json"},
                                   self.implementation, present=True))

    def test_implementation_outside_scope_fails(self):
        self.assertTrue(self.check({"private/admin.lua"},
                                   self.implementation, present=True))

    def test_implementation_bad_owner_fails(self):
        def other_owner(path, token):
            if path == "pulls/9":
                return {"merged_at": "2026-11-01T00:00:00Z",
                        "merged_by": {"login": "someone-else"}, "base": {"ref": "main"}}
            return [{"filename": self.prefix + "proposal.md"}]
        self.assertTrue(self.check({"addon/DetectRadius/Core/Init.lua"},
                                   self.implementation, present=True, api=other_owner))

    def test_implementation_unrelated_approval_fails(self):
        def unrelated(path, token):
            if path == "pulls/9":
                return {"merged_at": "2026-11-01T00:00:00Z",
                        "merged_by": {"login": "hectoresen"}, "base": {"ref": "main"}}
            return [{"filename": "openspec/changes/unrelated/proposal.md"}]
        self.assertTrue(self.check({"addon/DetectRadius/Core/Init.lua"},
                                   self.implementation, present=True, api=unrelated))

    def test_docs_exemption_passes_for_readme(self):
        self.assertEqual(self.check({"README.md"},
                                    "OpenSpec-Exemption: docs-only\n"), [])

    def test_docs_exemption_fails_for_policy(self):
        self.assertTrue(self.check({"AGENTS.md"}, "OpenSpec-Exemption: docs-only\n"))

    def test_maintenance_cannot_modify_lua(self):
        self.assertTrue(self.check({"addon/DetectRadius/Core/Init.lua"},
                                   "OpenSpec-Exemption: maintenance\n"))

    def test_bootstrap_only_pr2_with_allowlist(self):
        exemption = "OpenSpec-Exemption: bootstrap\n"
        self.assertEqual(self.check({"scripts/validate_sdd.py"}, exemption, number=2), [])
        self.assertTrue(self.check({"scripts/validate_sdd.py"}, exemption, number=3))
        self.assertTrue(self.check({"addon/DetectRadius/Core/Init.lua"}, exemption, number=2))

    def test_fenced_metadata_does_not_count(self):
        fields = gate.parse_metadata(
            "~~~\nOpenSpec-Change: fake\n~~~\nOpenSpec-Exemption: docs-only\n")
        self.assertEqual(fields["change"], [])
        self.assertEqual(fields["exemption"], ["docs-only"])

    def test_unsafe_wildcard_scope_fails(self):
        (self.root / self.prefix / "sdd-scope.json").write_text(
            '{"allowed_paths": ["**"]}')
        self.assertTrue(self.check({self.prefix + "proposal.md"}, self.proposal))

    def test_missing_artifact_fails(self):
        (self.root / self.prefix / "design.md").unlink()
        self.assertTrue(self.check({self.prefix + "proposal.md"}, self.proposal))

    def test_duplicate_declarations_fail(self):
        self.assertTrue(self.check({"README.md"},
                                   "OpenSpec-Exemption: docs-only\n"
                                   "OpenSpec-Exemption: docs-only\n"))


    def test_docs_exception_cannot_edit_openspec(self):
        self.assertTrue(self.check({"openspec/changes/a/proposal.md"},
                                   "OpenSpec-Exemption: docs-only\n"))

    def test_docs_exception_cannot_edit_code_quality(self):
        self.assertTrue(self.check({"docs/CODE_QUALITY.md"},
                                   "OpenSpec-Exemption: docs-only\n"))

    def test_combined_only_authorized_pr_and_change(self):
        body = "OpenSpec-Change: improve-material-explorer-ui\nOpenSpec-Phase: combined\n"
        files = {self.prefix + "proposal.md", "addon/DetectRadius/Core/Init.lua"}
        self.assertTrue(self.check(files, body, number=14))
        self.assertTrue(self.check(files, body, number=15))

    def test_combined_valid_authorization(self):
        change = "improve-material-explorer-ui"
        prefix = "openspec/changes/" + change + "/"
        folder = self.root / prefix
        (folder / "specs" / "material-explorer").mkdir(parents=True)
        for name in ("proposal.md", "design.md", "tasks.md", "sdd-scope.json"):
            (folder / name).write_text("# example" if name.endswith(".md")
                else '{"allowed_paths":["addon/DetectRadius/**","tests/**"]}', encoding="utf-8")
        (folder / "specs/material-explorer/spec.md").write_text("## ADDED Requirements\n")
        body = "OpenSpec-Change: " + change + "\nOpenSpec-Phase: combined\n"
        paths = {prefix + "proposal.md", "addon/DetectRadius/Core/Init.lua"}
        self.assertTrue(self.check(paths, body, number=14))
        self.assertTrue(self.check(paths, body, number=16))
        self.assertTrue(self.check(paths | {"private/secret"}, body, number=14))
        self.assertTrue(self.check(paths | {".github/workflows/ci.yml"}, body, number=14))
        self.assertTrue(self.check(paths, body + "OpenSpec-Approval-PR: 9\n", number=14))

    def test_implementation_cannot_precede_spec_approval(self):
        self.assertTrue(self.check({"addon/DetectRadius/Core/Init.lua"},
                                   self.implementation, present=True,
                                   created="2026-10-01T00:00:00Z"))

    def set_scope(self, paths):
        (self.root / self.prefix / "sdd-scope.json").write_text(
            json.dumps({"allowed_paths": paths}), encoding="utf-8")

    def test_explicit_workflow_scope_is_accepted(self):
        self.set_scope([".github/workflows/publish-release.yml"])
        self.assertEqual(self.check({self.prefix + "proposal.md"}, self.proposal), [])
        self.assertEqual(
            self.check({".github/workflows/publish-release.yml"},
                       self.implementation, present=True), [])

    def test_unapproved_workflow_is_rejected(self):
        self.set_scope(["README.md"])
        self.assertTrue(self.check({".github/workflows/publish-release.yml"},
                                   self.implementation, present=True))

    def test_other_workflow_is_rejected_even_if_one_is_approved(self):
        self.set_scope([".github/workflows/publish-release.yml"])
        self.assertTrue(self.check({".github/workflows/ci.yml"},
                                   self.implementation, present=True))

    def test_workflow_wildcards_are_rejected(self):
        for unsafe in (".github/workflows/**", ".github/**",
                       ".github/workflows/*.yml",
                       ".github/workflows/../ci.yml",
                       ".github/CODEOWNERS"):
            with self.subTest(path=unsafe):
                self.set_scope([unsafe])
                self.assertTrue(self.check({self.prefix + "proposal.md"}, self.proposal))

    def test_hidden_file_cannot_be_whitelisted_via_broad_scope(self):
        self.set_scope([".github/workflows/publish-release.yml", "docs/**"])
        self.assertTrue(self.check({".github/CODEOWNERS"}, self.implementation, present=True))

    def test_approval_gates_apply_to_workflow_changes(self):
        self.set_scope([".github/workflows/publish-release.yaml"])
        self.assertTrue(self.check({".github/workflows/publish-release.yaml"},
                                   self.implementation, present=False))
        self.assertTrue(self.check({".github/workflows/publish-release.yaml"},
                                   self.implementation, present=True,
                                   created="2026-10-01T00:00:00Z"))

    def test_only_approved_documentation_gate_may_update_agents(self):
        change = "mandatory-multiagent-documentation-gate"
        prefix = "openspec/changes/" + change + "/"
        folder = self.root / prefix
        (folder / "specs" / "documentation-gate").mkdir(parents=True)
        for name in ("proposal.md", "design.md", "tasks.md"):
            (folder / name).write_text("# approved\n", encoding="utf-8")
        (folder / "specs/documentation-gate/spec.md").write_text(
            "## ADDED Requirements\n", encoding="utf-8")
        (folder / "sdd-scope.json").write_text(json.dumps({
            "allowed_paths": ["AGENTS.md", ".github/workflows/ci.yml",
                "skills/documentation-sync/**", "scripts/validate_sdd.py"]
        }))
        body = ("OpenSpec-Change: " + change +
                "\nOpenSpec-Phase: implementation\nOpenSpec-Approval-PR: 9\n")

        def approved_api(path, token):
            if path == "pulls/9":
                return {"merged_at": "2026-11-01T00:00:00Z",
                        "merged_by": {"login": "hectoresen"}, "base": {"ref": "main"}}
            return [{"filename": prefix + "proposal.md"}]

        self.assertTrue(self.check({"AGENTS.md", "skills/documentation-sync/SKILL.md"},
                                    body, present=True, api=approved_api))
        # A different change claiming AGENTS in scope still fails.
        self.set_scope(["AGENTS.md", "addon/DetectRadius/**"])
        self.assertTrue(self.check({"AGENTS.md"}, self.implementation, present=True))
        # SDD rules remain strict: an unrelated spec approval cannot bless AGENTS.
        self.assertTrue(self.check({"AGENTS.md"}, body, present=True, api=self.api))
        self.assertTrue(self.check({"AGENTS.md"}, body, present=False, api=approved_api))
        self.assertTrue(self.check({"AGENTS.md"}, body, present=True,
                                   created="2026-10-01T00:00:00Z", api=approved_api))

    def test_governance_scope_cannot_glob_hidden_paths(self):
        self.set_scope([".github/**", "AGENTS.md"])
        self.assertTrue(self.check({self.prefix + "proposal.md"}, self.proposal))

if __name__ == "__main__":
    unittest.main()
