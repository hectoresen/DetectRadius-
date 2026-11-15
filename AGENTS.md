# DetectRadius — agent contract

Read README.md, CONTRIBUTING.md, docs/ARCHITECTURE.md, docs/EXPERIMENTS.md, docs/TESTING.md, docs/GITHUB_GOVERNANCE.md and openspec/README.md before changes. Inspect main, relevant PRs and source before claiming functionality. English for source, specs, documentation and PRs; localize user-facing text in enUS/esES.

## Boundaries
- Lightweight offline Lua addon for WoW Forever. No network dependency, telemetry, prohibited client modification or automation.
- Code eventually lives in addon/DetectRadius/: Core lifecycle; Domain pure detection estimates; Infrastructure guarded WoW API adapters; Features presentation; Localization.
- Never advertise an estimated ring as a guaranteed safe boundary. Distinguish detection radius, hostile NPC distance, spell range, screen coordinates and world geometry.
- Document a precise API name, client build, test observations and limits for every experiment. No invented Lua API support or in-game PASS.
- Only one experimental technique/variable changes per trial; prefer feature-flagged and reversible implementations.

## Required spec-first lifecycle (mirrors CraftAtlas)
1. Create openspec/changes/<id>/proposal.md, design.md, tasks.md, specs/<capability>/spec.md and sdd-scope.json. Submit SPEC-ONLY PR with OpenSpec-Change and OpenSpec-Phase: proposal. Stop for @hectoresen to merge.
2. Only after owner-merged proposal, create a separate implementation branch/PR with OpenSpec-Change, OpenSpec-Phase: implementation, OpenSpec-Approval-PR: <real PR number>. Do not modify accepted proposal/spec/design/scope in implementation PR; only tasks.md may advance.
3. Before functional PR, explicitly read and execute skills/documentation-sync/SKILL.md, reconcile README, architecture, testing, experiments, changelog and evidence. Record Documentation-Review and Documentation-Evidence in PR.
4. Run relevant automated checks; record actual WoW Forever client build and results as PASS/FAIL/INCONCLUSIVE/NOT RUN. Present owner handoff. Never merge, release, or direct-push main without separate explicit owner authorization.

Code changes need approved OpenSpec. Documentation-only bootstrapping can proceed through PR without gameplay changes. No silent scope expansion. Repository policies documented in Markdown do not equal enforced GitHub branch protections. Do not alter settings/rulesets/secrets/permissions without separate owner approval.
