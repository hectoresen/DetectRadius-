# Tasks (source implementation in progress; client tests NOT RUN)

## Proposal
- [x] Owner reviews and merges this spec-only PR (#3; proposal files present on main).
- [ ] Confirm CI/OpenSpec requirements and actual Forever addon interface/build before code.

## A1
- [x] Add pure estimate function, guarded unknown-level and invalid-target behavior.
- [x] Add offline regression test file for equal level, positive/negative delta, min/max clamp and invalid inputs (local reproduced calculation test PASS; committed suite execution still pending).
- [ ] Check whether real client returns NPC level and whether no-target/friendly logic behaves as assumed.
- [ ] Record observed in-game evidence; do not claim empirical detection accuracy.

## B1
- [ ] Probe full nameplate API and game event support in client, recording failures (first screenshot confirms only that the ring rendered for one selected target).
- [x] Implement one cached optional 2D semitransparent ring anchored to target nameplate when permitted (client NOT RUN).
- [x] Add /dr on and /dr off, hidden invalid/friendly/unselected, cleanup and re-target behavior (code only; client NOT RUN).
- [ ] Check nameplate visibility changes, target switches, zoom, scale, combat and UI restrictions.
- [x] Record owner B1 **FAIL** and screenshots in docs/EXPERIMENTS.md (client build still not supplied; disabled visual retest NOT RUN).

## QA/release
- [ ] Run offline validation/lint if available and report actual command/results.
- [x] Read documentation-sync skill and reconcile README, ARCHITECTURE, TESTING and EXPERIMENTS; CHANGELOG not yet present. Client NOT RUN.
- [ ] Open separate implementation PR with real owner-merged spec PR number and documented results.
- [x] Owner reported B1 unsuitable; second screenshot and attack outside drawn ellipse establish failure for safe-boundary use. Ring disabled in PR #4; A1 only chat diagnostic. New strategies require separate spec approval.
