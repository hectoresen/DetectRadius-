#!/usr/bin/env python3
"""Basic repository-doc scaffold validation; does not establish client compatibility."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "AGENTS.md", "CONTRIBUTING.md",
    "docs/ARCHITECTURE.md", "docs/EXPERIMENTS.md",
    "docs/TESTING.md", "docs/GITHUB_GOVERNANCE.md",
    "docs/AGENT_WORKFLOW.md", "docs/CODE_QUALITY.md",
    "openspec/README.md", "openspec/config.yaml",
    "skills/documentation-sync/SKILL.md",
    ".github/CODEOWNERS", ".github/pull_request_template.md",
]
def check():
    missing = [p for p in REQUIRED if not (ROOT / p).is_file()]
    checklist = (ROOT / "docs/EXPERIMENTS.md").read_text(encoding="utf-8") if not missing else ""
    for marker in ("A1:", "A2:", "A3:", "A4:", "A5:", "B1:", "B2:", "B3:", "B4:", "B5:", "B6:", "Decision log", "NOT RUN"):
        if marker not in checklist:
            missing.append("docs/EXPERIMENTS.md marker " + marker)
    return missing
if __name__ == "__main__":
    issues = check()
    if issues:
        print("Repository validation failed:", *issues, sep="\n- ")
        sys.exit(1)
    print("PASS: documentation scaffold and experiment identifiers (NOT game validation)")
