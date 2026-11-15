# DetectRadius OpenSpec / SDD

Intended workflow mirrors CraftAtlas. Required for every gameplay or nontrivial technical change: **two separate PRs**.

1. PROPOSE: new openspec/changes/<id>/ with proposal.md (why/scope/risks), design.md (API/architecture/fallbacks), specs/<capability>/spec.md (SHALL/WHEN/THEN), tasks.md (verifiable checks), and sdd-scope.json (bounded authorized implementation paths). Submit spec-only PR with OpenSpec-Change: <id> and OpenSpec-Phase: proposal. Wait for @hectoresen to merge.
2. IMPLEMENT: separate branch and PR only after spec PR owner-merged. Include OpenSpec-Change: <id>, OpenSpec-Phase: implementation, OpenSpec-Approval-PR: <real number>. Only modify approved implementation paths; in OpenSpec only tasks.md may be advanced. Stop for review and real game testing.
3. VERIFY / SYNC / ARCHIVE: do so after real approval and acceptance; do not claim in-game PASS from CI.

Official OpenSpec CLI package: @fission-ai/openspec. Consult current CLI help and generated profile rather than inventing commands. This repository does **not** yet have CraftAtlas's custom server-backed SDD validator reproduced or configured; manual source/PR reviews are mandatory until gate is ported and proven. No combined spec+implementation shortcuts.

First proposed experiment should cover A1 and B1 independently (or separate proposals) and reference docs/EXPERIMENTS.md.
