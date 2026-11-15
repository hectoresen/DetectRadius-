# DetectRadius OpenSpec — enforced spec-first process

Read AGENTS.md, docs/EXPERIMENTS.md and docs/SDD_COMPLIANCE.md first.

For each gameplay change:
1. Create `openspec/changes/<id>/proposal.md`, `design.md`, `tasks.md`, `specs/<capability>/spec.md` and `sdd-scope.json`.
2. Open a **spec-only PR**, declaring `OpenSpec-Change: <id>` and `OpenSpec-Phase: proposal`. Owner @hectoresen merges it before implementation.
3. Implement in a separate PR limited to approved paths, with `OpenSpec-Change`, `OpenSpec-Phase: implementation`, `OpenSpec-Approval-PR: <merged proposal PR>`. Only update tasks.md within that approved change; no spec/design/scope mutations.
4. Read and run skills/documentation-sync/SKILL.md before functional PRs. Record actual test results.
5. Human verification in Forever is mandatory before a claim of game correctness.

Official CLI: `@fission-ai/openspec`. CI runs `openspec validate --all --strict --no-interactive`. Custom provenance checks are separate from the official CLI. No combined PRs, and no reuse of CraftAtlas exception numbers.

The experimental roadmap is docs/EXPERIMENTS.md. No addon functionality implemented yet.
