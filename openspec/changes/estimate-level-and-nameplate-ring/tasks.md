# Tasks (all NOT RUN)

## Proposal
- [ ] Owner reviews and merges this spec-only PR.
- [ ] Confirm CI/OpenSpec requirements and actual Forever addon interface/build before code.

## A1
- [ ] Add pure estimate function, guarded unknown-level and invalid-target behavior.
- [ ] Add offline tests for equal level, positive/negative delta, min/max clamp and invalid inputs.
- [ ] Check whether real client returns NPC level and whether no-target/friendly logic behaves as assumed.
- [ ] Record observed in-game evidence; do not claim empirical detection accuracy.

## B1
- [ ] Probe nameplate API and game event support in client, recording failures.
- [ ] Implement one cached optional 2D semitransparent ring anchored to target nameplate when permitted.
- [ ] Add /dr on and /dr off, hidden invalid/friendly/unselected, cleanup and re-target behavior.
- [ ] Check nameplate visibility changes, target switches, zoom, scale, combat and UI restrictions.
- [ ] Record screenshots, client build and PASS/FAIL/INCONCLUSIVE in docs/EXPERIMENTS.md.

## QA/release
- [ ] Run offline validation/lint if available and report actual command/results.
- [ ] Explicitly execute skills/documentation-sync/SKILL.md and reconcile README, ARCHITECTURE, TESTING, EXPERIMENTS and CHANGELOG as relevant.
- [ ] Open separate implementation PR with real owner-merged spec PR number and documented results.
- [ ] Owner decides whether B1 is viable; if rejected, leave next candidates untouched until a separate proposal.
