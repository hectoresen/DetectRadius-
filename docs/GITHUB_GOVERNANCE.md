# GitHub governance

## Implemented in repository (pending owner merge)
- `.github/CODEOWNERS` lists @hectoresen.
- CI provides structural repository and documentation checks.
- SDD Compliance workflow, `scripts/validate_sdd.py` and regression tests enforce owner-merged spec PR provenance and bounded implementation scope when executed.
- PR template requires concrete test results and owner review.

## Required GitHub settings (not configured by this PR)
Protect `main`: require pull requests and approval(s), require the two named green checks once proven, prevent force pushes/deletion and direct pushes; consider squash-only merges and delete-head-branch. Confirm whether repo plan/roles permit an actual owner-only merge restriction; standard review settings alone do not do so. No bypass actors without explicit approval.

**Do not claim these protections are active** until GitHub ruleset settings are saved and verified. This connector exposes no branch-ruleset administration action, so the maintainer must configure them in GitHub Settings or authorize an alternative admin workflow.

## Safety limits
A CI check validates syntactic evidence, not semantic specification compliance, game-client compatibility, or real-world range accuracy. Agents do not merge, publish releases, change permissions, or mark unrun checks green.
