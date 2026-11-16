"""Documentation PR readiness policy, independent of any AI runtime."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/validate_documentation.py"
spec = importlib.util.spec_from_file_location("docs_gate", SCRIPT)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

FUNCTIONAL = {"addon/DetectRadius/Features/Ring.lua"}
EVIDENCE = ("README.md current behavior was compared to Lua view changes; "
            "CHANGELOG.md documents the new tab, TESTING.md preserves NOT RUN client tests.")

class DocumentationReviewTests(unittest.TestCase):
    def test_updated_with_readme_passes(self):
        self.assertEqual(gate.validate(FUNCTIONAL | {"README.md", "CHANGELOG.md"},
            "Documentation-Review: updated\nDocumentation-Evidence: " + EVIDENCE), [])

    def test_missing_review_fails(self):
        self.assertTrue(gate.validate(FUNCTIONAL | {"README.md"},
            "Documentation-Evidence: " + EVIDENCE))

    def test_missing_evidence_fails(self):
        self.assertTrue(gate.validate(FUNCTIONAL | {"README.md"},
            "Documentation-Review: updated"))

    def test_duplicate_attestations_fail(self):
        body = "Documentation-Review: updated\nDocumentation-Review: updated\nDocumentation-Evidence: " + EVIDENCE
        self.assertTrue(gate.validate(FUNCTIONAL | {"README.md"}, body))

    def test_updated_without_docs_fails(self):
        self.assertTrue(gate.validate(FUNCTIONAL,
            "Documentation-Review: updated\nDocumentation-Evidence: " + EVIDENCE))

    def test_updated_with_other_docs_needs_readme_rationale(self):
        self.assertTrue(gate.validate(FUNCTIONAL | {"CHANGELOG.md"},
            "Documentation-Review: updated\nDocumentation-Evidence: " +
            "Only changelog has changes since source behavior was updated and tested elsewhere."))
        self.assertEqual(gate.validate(FUNCTIONAL | {"CHANGELOG.md"},
            "Documentation-Review: updated\nDocumentation-Evidence: " +
            "README.md remains unchanged because the client behavior stays identical; "
            "CHANGELOG.md documents a new internal test scenario."), [])

    def test_not_applicable_requires_specific_reason(self):
        self.assertTrue(gate.validate(FUNCTIONAL,
            "Documentation-Review: not-applicable\nDocumentation-Evidence: " +
            "No content requires changes and all seems fine after review of all areas."))
        self.assertEqual(gate.validate(FUNCTIONAL,
            "Documentation-Review: not-applicable\nDocumentation-Evidence: " +
            "README.md remains unchanged because this only adjusts guarded error "
            "handling without user-visible behavior; architecture and testing docs audited."), [])

    def test_not_applicable_with_docs_changed_fails(self):
        self.assertTrue(gate.validate(FUNCTIONAL | {"README.md"},
            "Documentation-Review: not-applicable\nDocumentation-Evidence: " + EVIDENCE +
            " Since README remains correct, no behavioral changes are needed."))

    def test_spec_proposal_only_passes_without_metadata(self):
        self.assertEqual(gate.validate({"openspec/changes/a/proposal.md"}, ""), [])

    def test_docs_only_passes_without_metadata(self):
        self.assertEqual(gate.validate({"README.md", "docs/TESTING.md"}, ""), [])

    def test_governance_only_passes_without_metadata(self):
        self.assertEqual(gate.validate({"AGENTS.md", "scripts/validate_sdd.py"}, ""), [])

    def test_fenced_example_does_not_satisfy_attestation(self):
        body = "```\nDocumentation-Review: updated\nDocumentation-Evidence: " + EVIDENCE + "\n```"
        self.assertTrue(gate.validate(FUNCTIONAL | {"README.md"}, body))

    def test_source_data_changes_require_docs(self):
        self.assertTrue(gate.validate({"addon/DetectRadius/Data/Recipes.lua"}, ""))

    def test_empty_repetitive_evidence_rejected(self):
        self.assertTrue(gate.validate(FUNCTIONAL | {"README.md"},
            "Documentation-Review: updated\nDocumentation-Evidence: reviewed"))

if __name__ == "__main__":
    unittest.main()
