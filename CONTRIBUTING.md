# Contributing to DetectRadius

Use English in code, docs, specs, issues and PRs. Client-visible text should support enUS/esES when implemented. Read AGENTS.md and docs/EXPERIMENTS.md.

1. Branch from main; never push directly to main.
2. For gameplay, compatibility, nontrivial refactors or new rendering/distance techniques: propose an OpenSpec change in a spec-only PR; wait for @hectoresen to merge.
3. Implement only the approved sdd-scope.json paths in another PR, one experiment at a time.
4. Validate offline tests and perform the manual trial in docs/TESTING.md. No client tests are presumed complete.
5. Read skills/documentation-sync/SKILL.md and reconcile documentation before any functional PR.
6. Submit PR with exact experiment ID, what changed, tests/results, actual client build, screenshots/video if available, rollback, limitations and human approval request. No merges or releases by agents.

Spec PR metadata:
```
OpenSpec-Change: <id>
OpenSpec-Phase: proposal
```
Implementation PR metadata:
```
OpenSpec-Change: <id>
OpenSpec-Phase: implementation
OpenSpec-Approval-PR: <merged owner spec PR number>
Documentation-Review: updated
Documentation-Evidence: <specific files and executed validation>
```

Never claim branch protections are enabled without verifying actual GitHub settings.
