# Design: two independent experiments A1 and B1

## Components (planned)
- `addon/DetectRadius/DetectRadius.toc` — game load order and correct verified interface.
- `Core/Init.lua` — lifecycle, slash toggles, target-change events, minimal update policy.
- `Domain/DetectionEstimate.lua` — pure clamp and input validity, no WoW globals.
- `Infrastructure/UnitApi.lua` — guarded `UnitExists`, `UnitCanAttack`, `UnitLevel`; unknown level or non-NPC => unavailable estimate.
- `Infrastructure/NameplateApi.lua` — probe `C_NamePlate.GetNamePlateForUnit("target")` on the actual client. No secure frame mutations in combat; handle nil and transitions.
- `Features/Ring.lua` — cached UI texture ring, alpha configurable, explicitly screen-space, anchored to valid target nameplate when available. Avoid allocating on every frame.
- `Localization/Locales.lua` — English/Spanish strings; no ground-accuracy claim.

## A1 heuristic contract
`estimate(playerLevel, npcLevel)` returns an estimated number of yards only for valid positive numeric level values and normal NPC targets. `max(5, min(45, 20 + npcLevel - playerLevel))` is a starting model for experimental testing, not canonical Forever range. Isolate constants for later owner-approved calibration. Skip unknown skull/non-numeric levels, players, friendly/no targets and unsupported edge cases; don't show a fabricated estimate.

## B1 UI assumptions
Call nameplate API only if function exists; validate returned frame, visibility and secure/forbidden status where possible. Attach one 2D ring to appropriate non-protected accessible frame or an independent UIParent overlay anchored relative to nameplate if safe. Never create world coordinates; any sizing is **illustrative**. Do not interpret computed yard value as an exact pixel radius. Use clear experimental/approximate labeling. If attaching requires blocked actions or unreliable anchors, hide rather than pretending correctness.

## Event/performance
Event-driven `PLAYER_TARGET_CHANGED`, nameplate added/removed and player-level changes if API supports them; throttle any necessary refresh. No scanning other enemies. Clear on target loss, toggling off, zone transitions, unload/reload. Measure frame/update overhead in manual testing, avoid unnecessary OnUpdate.

## Validation
Offline Lua tests for domain inputs/boundaries and fake API availability; structural package check. Test B1 in actual Forever client with selected NPCs, nameplate visible/hidden, camera zoom, UI scale, combat/noncombat, target switching. Capture interface/build, slash behavior, error text, screenshots and explicit failure rationale.

## Decision boundary
If B1 cannot represent physical danger distance accurately, label as *visual-only approximation* and seek owner feedback before choosing next experiment. No escalation to B2–B6 without a new approved change.
