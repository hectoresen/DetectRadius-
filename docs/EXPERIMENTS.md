# DetectRadius — ordered experiment plan (source of truth)

Status: **B1 FAILED in real-client visual testing; A1 empirical accuracy NOT VERIFIED**. Other candidates NOT RUN. Owner @hectoresen tests each candidate in the real WoW Forever client. Engineering assumptions below are hypotheses until observed. Goal: visually communicate an *estimated* hostile NPC detection radius, ideally as a red translucent ground-like ring; never promise an actual safe boundary.

## Experimental rules

- Implement **one candidate per PR/test build**, behind a temporary flag when possible. Owner tests and posts PASS, FAIL, INCONCLUSIVE or NOT RUN with evidence before proceeding.
- Keep screenshot/video, player/NPC level, NPC name/ID when known, distance/range clues, zone, combat status, UI scale, display resolution, client interface/build, locale, date and Lua error text.
- For each trial note feasibility, correctness, UX, frame cost, API restrictions, known failure modes and verdict. A visually attractive but physically misleading circle FAILS the accuracy criterion.
- Stop escalating the list once an accepted, honest presentation is found. Never deploy memory reading, DLL injection, client tampering or prohibited automation.

## Track A — detection range estimate (test in priority order)

- [ ] **A1: level-difference estimate (highest feasibility).** Read UnitLevel("player") and UnitLevel("target") on a valid target; isolate a configurable Classic-inspired heuristic R = clamp(20 + NPC_level - player_level, 5, 45) *in yards*, as an **unverified baseline**, not confirmed Forever behavior. Reject unknown/skull levels, pets/players where inappropriate and special cases. Unit level is available but real NPC detection is not guaranteed by this formula. Unit test boundaries and level changes.
- [ ] **A2: controlled observed pull threshold / calibration.** For same NPC type/levels, approach carefully and record first engagement at multiple attempts. Use screenshots plus independently verified reference distances where available. Derive correction/uncertainty and test repeated consistency; do not represent the observation as game-provided aggro radius.
- [ ] **A3: range-bracket API probes.** Test available spell/interact/range checks and/or a compatible LibRangeCheck alternative for enemy target. Record function names and actual bracket granularity, missing values and combat restrictions. Only use intervals; do not call them meters or precise radii.
- [ ] **A4: special-case classifications.** Evaluate elite, hostile-but-passive, neutral, stealth/invisibility, detection buffs, vertical separation and nonstandard NPCs. Exclude/label unsupported cases rather than extrapolating.
- [ ] **A5: alternate client APIs (low confidence).** With explicit API availability checks, assess exposed tracking/position/map functions for enemy units. No unsafe API assumptions; accept INCONCLUSIVE if coordinates unavailable.

## Track B — visual representation (test in priority order)

- [x] **B1: FAILED (not suitable as a safe radius): target nameplate-anchored 2D ellipse/ring (highest plausible usable visual).** Probe C_NamePlate.GetNamePlateForUnit("target"), nameplate visibility and permitted anchoring outside/inside combat. Draw cached WoW UI texture(s), hollow center, red alpha; show/hide with target/enable state. It follows nameplate *on screen*, not ground, and size is illustrative only. Check no nameplate, camera rotation, zoom, occlusion, combat and UI scaling.
- [ ] **B2: target-frame-anchored 2D ring.** Same geometry attached to target frame; robust when nameplate unavailable but less spatially meaningful. Trial only if B1 insufficient.
- [ ] **B3: screen-space ground-like illusion anchored to nameplate offset.** Try a projected ellipse below nameplate using fixed/heuristic offsets and camera cases. This cannot remain a calibrated world-space radius; reject if it induces false safe-path decisions.
- [ ] **B4: map/minimap indication.** Assess whether legitimate APIs provide current target position and compatible map frame rendering. Reject rather than invent world coordinates.
- [ ] **B5: HUD ring or perimeter warning fallback.** Screen overlay showing calculated estimate/risk status, clearly not world-space. Prefer truthful UX if B1–B4 are inaccurate.
- [ ] **B6: genuine ground-locked 3D decal (expected unavailable).** Treat as research-only; do not implement absent a documented, permitted native client API and successful in-game demonstration. Normal addon Lua 2D textures do not produce a physically accurate 3D ground circle.

## Current prototype notes (A1/B1)

The prototype originally displayed a fixed-pixel nameplate ellipse and a provisional level-delta estimate. **The visual has been disabled following two owner screenshots and a reported hostile NPC attack outside the drawn circle.** The A1 provisional calculation remains accessible as a chat diagnostic via `/dr estimate`. This is **not** a world-calibrated detection circle. B1 is **FAILED as a safety representation**; A1 empirical accuracy is **NOT VERIFIED**. The first owner screenshot confirms the overlay is visible in one target scenario, not that it follows movement, works in combat or represents safe yardage. Start with `/dr on`, a visible hostile target nameplate, and `/console scriptErrors 1`. The TOC interface `16001` is provisional and must be checked in the real client. A1 initial pure calculation regression passed using a local texlua reproduction; the nameplate ring render has been observed in one Forever screenshot; exact API behavior beyond that and remaining tests are not established.

## Test dependency and order

1. Bootstrap addon and validate client build/API discovery; no game claims beforehand.
2. A1 establishes a deterministic estimate; B1 tests best feasible spatial visual **independently** of accurate range.
3. A2 and A3 investigate estimate credibility and physical proximity; advance B2/B3 only if B1 fails usability.
4. A4 handles known exceptions. B4/B5 are fallbacks, not proof of a 3D circle. A5/B6 need new evidence and spec approval.
5. After every attempt update the decision log below, user testing matrix and next candidate. Do not mark an item complete merely for writing code.

## Acceptance criteria (each tested explicitly)

- Toggle on/off and target change work; hidden for friendly/invalid targets; reload behaves as documented.
- Red semitransparent visual does not obstruct play; clear indication that ring is approximate.
- No Lua errors or forbidden combat/secure-frame operations in tested client; sampling/performance measured reasonably.
- Level-delta estimate has unit tests; observed thresholds are recorded without claiming guaranteed safety.
- Real player tests at multiple player-vs-NPC level deltas, elevations, camera zooms/UI scales and combat/noncombat.
- Code small, no mandatory external addon, no background scanning, no player tracking/telemetry.

## Decision log (append, never rewrite historical evidence)

| Date | Candidate | Build / PR | Result | Evidence link | Finding / next step |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | All candidates | N/A | NOT RUN | N/A | Initial plan prepared |\n| 2026-11-16 | B1 screenshot #1 | PR #4 initial build | PARTIAL — render visible | Owner screenshot shared in conversation | Red ellipse and ~32 yd (est.) appear beneath selected Basilisco Ojogélido nameplate, player level 28. Ring sits too high; not on terrain, and scale is illustrative only. A1 formula is not independently verified against real detection. |\n| 2026-11-16 | B1 visual alignment revision | PR #4 (same branch) | FAILED in subsequent client report | Owner second screenshot in conversation | Crocolisco Aguasalada shows ~28 yd (est.) and small ellipse across NPC body; owner reports NPC attacked while outside visual ellipse. This is evidence against the overlay as a safe boundary, not a precise empirical aggro distance measurement. |\n| 2026-11-16 | B1 disabled | PR #4 | IMPLEMENTED, game retest NOT RUN | Commit baa949f | Do not render fixed-pixel ring. Retain A1 as explicit unverified chat diagnostic; pursue A2/A3 via new approved OpenSpec before claiming proximity/range. |

## Next action — B1 rejected; no more arbitrary ring offsets

Do not use the previous B1 ring for navigation: the player was attacked while outside the drawn ellipse. The latest PR #4 removes the visual and limits A1 to chat diagnostics. Candidate B2 (target-frame anchor) and B3 (other screen-space offsets) cannot solve physical yard calibration on their own. Propose A2/A3 next to calibrate actual hostile range and test legitimate distance-bracket API availability separately before revisiting any world-facing overlay.

## Owner in-game report template

```text
Candidate: A1 / B1 / ...
Addon commit or PR:
Forever client version / interface:
Locale; UI scale; resolution; camera zoom:
Player class/level and target name/level/type:
Combat? nameplate visible? zone/elevation:
Steps performed:
Expected:
Observed:
Lua errors (/console scriptErrors 1):
PASS / FAIL / INCONCLUSIVE:
Screenshot/video:
Recommendation: accept / revise / try next experiment
```
