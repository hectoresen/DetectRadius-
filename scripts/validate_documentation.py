#!/usr/bin/env python3
"""PR documentation review gate: structural evidence, not semantic verification."""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

AUDIT_RE = re.compile(r"^Documentation-Review:\s*(updated|not-applicable)\s*$", re.M)
EVIDENCE_RE = re.compile(r"^Documentation-Evidence:\s*(.+?)\s*$", re.M)
DOCS = {
    "README.md", "CHANGELOG.md", "CONTRIBUTING.md", "AGENTS.md",
    "docs/ARCHITECTURE.md", "docs/DATA_MODEL.md", "docs/INSTALLATION.md",
    "docs/TESTING.md", "docs/ROADMAP.md", "docs/DEVELOPMENT.md",
    "docs/AGENT_WORKFLOW.md", "docs/DOCUMENTATION_PROTOCOL.md",
}
SCOPE_ROOTS = ("addon/", "scripts/build_materials.py", "scripts/package_release.py")
MIN_EVIDENCE_LENGTH = 55


def _unfenced(body):
    # An example declaration within a fenced code block is never evidence.
    return re.sub(r"(?ms)^(`{3,}|~{3,})[^\n]*\n.*?^\1[^\n]*$", "", body)


def validate(changed_paths, body):
    paths = set(changed_paths)
    functional = any(p.startswith("addon/") or p in (
        "scripts/build_materials.py", "scripts/package_release.py"
    ) for p in paths)
    if not functional:
        # Spec-only and documentation-only PRs are not obligated to pretend to
        # introduce new features. They remain governed by existing SDD rules.
        return []

    body = _unfenced(body or "")
    reviews = AUDIT_RE.findall(body)
    evidences = EVIDENCE_RE.findall(body)
    errors = []
    if len(reviews) != 1:
        errors.append("Functional PR requires exactly one Documentation-Review: updated|not-applicable")
    if len(evidences) != 1 or len(evidences[0].strip()) < MIN_EVIDENCE_LENGTH:
        errors.append("Functional PR requires substantive Documentation-Evidence: explanation (55+ characters)")
    if errors:
        return errors

    review, evidence = reviews[0], evidences[0].strip()
    changed_docs = paths & DOCS
    if review == "updated":
        if not changed_docs:
            errors.append("Documentation-Review: updated requires a changed documentation file")
        if "README.md" not in changed_docs and not re.search(
            r"README(?:\.md)?.{5,}(?:unchanged|no change|no update|still accurate|already accurate)",
            evidence, re.I
        ):
            errors.append("README not updated: provide a specific README no-change rationale")
    else:
        # An exemption is a documented decision, not a way to avoid reviewing README.
        if not re.search(r"README(?:\.md)?", evidence, re.I):
            errors.append("not-applicable requires an explicit README review and rationale")
        if not re.search(r"(because|since|unchanged|no user.visible|no feature|still accurate|does not change|only)", evidence, re.I):
            errors.append("not-applicable needs a meaningful reason, not merely a label")
        if changed_docs:
            errors.append("Documentation files changed: use Documentation-Review: updated")

    if re.fullmatch(r"(?i)(updated|reviewed|done|n/a|none|no changes)[.! ]*", evidence):
        errors.append("Documentation evidence must specify reviewed behavior and affected docs")
    return errors


def changed_files(base, head):
    result = subprocess.check_output(
        ["git", "diff", "--name-only", "--diff-filter=ACDMRT", f"{base}...{head}"],
        text=True
    )
    return [p for p in result.splitlines() if p]


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--event", required=True)
    args = parser.parse_args(argv)
    event = json.loads(Path(args.event).read_text(encoding="utf-8"))
    body = (event.get("pull_request") or {}).get("body") or ""
    errors = validate(changed_files(args.base, args.head), body)
    for error in errors:
        print("::error::" + error)
    print("Documentation review: " + ("FAIL" if errors else "PASS") +
          " (structural attestation only; owner verifies semantic accuracy)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
