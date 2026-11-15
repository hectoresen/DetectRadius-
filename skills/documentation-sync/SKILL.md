---
name: documentation-sync
description: Mandatory pre-PR documentation/evidence review for DetectRadius.
---

# Documentation sync (adapted from CraftAtlas)

Before every functional PR and after relevant revisions:
1. Read AGENTS.md, README.md, the owner-merged OpenSpec proposal/spec/design/tasks/scope, affected code, docs/ARCHITECTURE.md, docs/EXPERIMENTS.md, docs/TESTING.md, docs/GITHUB_GOVERNANCE.md and CHANGELOG.md (if present).
2. Audit user-visible reality vs claims; distinguish **implemented**, **offline-tested**, **manually tested in real Forever**, **hypothesized** and **NOT RUN**. Do not infer APIs or game build.
3. Sync README actual behavior and limitations, architecture, testing, experiment verdicts, roadmap/change history if present. Keep AGENTS.md process-only.
4. Check approved scope and links, run relevant tests, log missing commands and unrun client checks. Implementation PR may advance tasks.md but not rewrite owner-approved artifacts.
5. Report in PR:
```
Documentation-Review: updated
Documentation-Evidence: <files audited and real checks completed>
```
Or a substantive Documentation-Review: not-applicable with evidence if truly no changes. Owner is the only merge/release approver.
