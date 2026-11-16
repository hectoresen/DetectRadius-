# DetectRadius SDD compliance

This repository ports CraftAtlas's PR provenance validator with DetectRadius-specific change scopes.

## Required two-PR process
1. Proposal PR changes *only* a new `openspec/changes/<id>/` directory and contains `proposal.md`, `design.md`, `tasks.md`, `sdd-scope.json` and `specs/<capability>/spec.md`. Body: `OpenSpec-Change: <id>` and `OpenSpec-Phase: proposal`.
2. Owner @hectoresen merges proposal to main.
3. Implementation PR changes only approved `allowed_paths` in the manifest (plus tasks.md), and includes `OpenSpec-Change: <id>`, `OpenSpec-Phase: implementation`, `OpenSpec-Approval-PR: <actual merged PR number>`.
4. The validator checks GitHub PR metadata, that approved spec PR was merged by @hectoresen, that it targets main, that it includes the referenced change, and that the merge preceded implementation PR creation.
5. Documentation review evidence is separately required for functional addon changes. Run the documentation-sync skill. Automated checks are not in-game verification.

## Check names
- `SDD Compliance / traceability` from `.github/workflows/spec-compliance.yml`
- `CI / repository-validation` from `.github/workflows/ci.yml`

## Narrow exemptions
- `OpenSpec-Exemption: docs-only` for eligible non-governance text files.
- `OpenSpec-Exemption: maintenance` for permitted tiny dotfiles.
- `OpenSpec-Exemption: bootstrap` for PR #2 **only**, with an exact file allowlist in `scripts/validate_sdd.py`, to install these checks. Combined spec+code PRs are forbidden.

The repository must enforce checks via active GitHub rulesets; the CI scripts alone do **not** prevent direct pushes or merges. Owner reviews rulesets and validates settings independently. Tests and strict OpenSpec validation must be actually run before declaring gates operational.

No game functionality is included in this change.
