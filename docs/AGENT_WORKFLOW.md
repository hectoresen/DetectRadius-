# Agent workflow

1. Discover: read AGENTS.md, current main, approved OpenSpec, active experiments and open PRs.
2. Explore: choose a single pending A/B candidate from docs/EXPERIMENTS.md; document falsifiable expected outcome and rollback.
3. Propose: spec-only PR with full artifacts and bounded sdd-scope.json; owner merges before code starts.
4. Implement: one experiment only on a new branch and PR referring to real merged proposal. Keep pure estimate isolated from UI and all APIs guarded.
5. Verify: automated checks (exact commands), explicit NOT RUN where applicable, owner in-game evidence using the report template.
6. Documentation-sync skill before PR; return results and next experiment recommendation.
7. Owner reviews/merges. No speculative PASS, direct main pushes, settings changes or release publication.
