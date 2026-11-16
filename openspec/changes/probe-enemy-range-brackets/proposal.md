# A3 — Probe enemy distance brackets in WoW Forever

## Why
Two owner in-game screenshots of B1's nameplate ellipse showed it does not correspond to actual ground distance, and the owner reported an enemy attack outside the ring. A1's level-based estimate is unverified. Before visualizing a safe/unsafe boundary we must determine which lawful client APIs can report **distance brackets** to a targeted hostile NPC.

## Scope
- Build a strictly opt-in chat diagnostic `/dr range` or `/dr probe`, without a ring.
- Probe native range APIs only when present, with validity handling and explicit source / min-max bounds or individual check outcomes.
- Prioritize documented APIs supported by WoW Forever: `C_Spell.IsSpellInRange` for actually-known harmful player spells, `CheckInteractDistance` / `UnitIsInInteractRange` when appropriate, and `C_Item.IsItemInRange` using **validated applicable item IDs** rather than guesses. Check each against the real client; maintain non-invasive, read-only behavior.
- Evaluate a compatible licensed `LibRangeCheck-3.0` **as optional research only**, no mandatory dependency.
- Log exact client/build, character class, known spells/items, results, approximate reference position and failure states.
- Use `/dr off` to disable probes; target only; no scanning around.

## Out of scope
A2 empirical aggro threshold calibration, modifying the rejected B1 ring, 3D ground effects, automatic movement/attack, data collection/telemetry, hidden APIs, and pretending these range brackets are actual hostile detection thresholds.

## Hypotheses, not verified facts
WoW Forever documentation indicates `C_Spell.IsSpellInRange` can return true/false/nil for known spells; a third-party Forever beta experiment observed some interact and item checks against hostile targets. These **must be re-tested for this character/build**. `UnitInRange` and `UnitDistanceSquared` are not general hostile-target distance sources. Do not equate spell max range with detection radius.

## Acceptance / fallback
A diagnostic may report known comparisons (e.g. within/outside a real 30-yard item checker) or a bounded interval only when its checkers are validated and monotonic/consistent. Otherwise report `unknown` with reasons, no numeric point distance. No ring resumes until a separate visual approach is proven safe and approved. Rollback: remove diagnostics or `/dr off`.
