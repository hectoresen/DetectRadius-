# GitHub governance — requested configuration vs verified state

Adopt CraftAtlas process: separate owner-approved spec and implementation PRs, review gates, docs sync, CI evidence, no agent merges/releases.

Target settings (owner-controlled, not established merely by this file):
- Protect main against direct pushes, force pushes and deletion; require pull requests and passing checks.
- Require owner review and ideally restrict merge permissions to owner where GitHub plan and roles allow; standard required approval alone does NOT enforce owner-only merging.
- Require CI and spec-traceability checks after they first run; prefer squash merges.
- CODEOWNERS and AGENTS.md express intent but **are not server-side enforcement**.
- Verify rulesets, workflows, protections and merge permissions in repository settings and a test PR before claiming they are active.

This bootstrap does **not** change GitHub repository settings, secrets, branch protection or permissions. Applying them requires explicit owner approval and compatible administrative access.
