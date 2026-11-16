# Proposal: estimated hostile detection + visual nameplate ring (A1/B1)

## Why
Players want an optional translucent red ring around a targeted hostile NPC to estimate its detection radius from the level difference. WoW Lua cannot be assumed to project a true ground-space circle. We must validate each component separately to avoid offering falsely precise navigation guidance.

## Scope
- A1: level-delta heuristic as pure Lua domain function, guarded player/target level reads and invalid-target handling.
- B1: one red semitransparent **screen-space** ring/ellipse anchored to the *selected hostile NPC's nameplate*, only if client permits.
- Toggle via slash commands `/dr on` and `/dr off`, default off until explicitly enabled (final persistence behavior subject to test).
- Probing and logging of relevant WoW Forever APIs, safe hide/show, cleanup, efficiency and documentation.
- Owner-run in-game tests with exact build, screenshots, errors, zoom/UI scale/target changes.

## Explicitly out of scope
World-locked / 3D ground decal, exact danger perimeter, guarantees of aggro avoidance, cross-target scanners, automatic combat actions, telemetry, external network services, calibration (A2), range checking (A3), special-case tuning (A4), alternative visual anchors B2–B6 and shipping a production release.

## Risks
- Formula `clamp(20 + targetLevel - playerLevel, 5, 45)` is a **hypothesis**, not confirmed Forever detection data; mobs have exceptions.
- Nameplate access, attachment, 2D sizing, combat state and zoom may make B1 unusable.
- Anchored ring is screen-space and cannot encode world yardage reliably; it must be labeled indicative, never safe.
- Release must be blocked if UX implies precise world-space safety.

## Rollback
Disable by slash command or revert this feature PR; no saved game state or network side effects.

## Acceptance
Pure tests pass; client test record indicates supported/unsupported APIs with actual evidence. If B1 cannot render consistently, record FAIL/INCONCLUSIVE and retain no misleading overlay; propose B2 separately.
