# A3 design — read-only target range capability probes

## Modules
- `Infrastructure/RangeProbe.lua`: guarded feature detection and individually named probes. All API invocations in `pcall`; never coerce nil/secret/invalid into in/out of range. Skip units that are absent, friendly or players.
- `Domain/RangeBracket.lua`: pure logic for combining independently validated yes/no threshold checks into **lower/upper limits**; unknown values stay unknown. If checks disagree or lack credible semantic range definitions, reject bracket.
- `Core/Init.lua`: explicit `/dr probe` (or `/dr range`), one on-demand query. Do not add a frame loop or spam chat. Do not turn ring back on.
- `tests/`: stubs covering no API, known spell false/true/nil, conflicting probes, bounds, unsupported client, errors and invalid target.

## Order of investigation
1. Report `GetBuildInfo()` and capability presence (functions, not results). WoW Forever interface version must be recorded.
2. For the player's character, identify usable **known harmful spell** with a trustworthy max-range definition. Probe `C_Spell.IsSpellInRange(spellIdentifier,"target")`. A true answer states the spell can reach the target under its own conditions; this is not a universally valid yard threshold.
3. Check `CheckInteractDistance("target", index)` or `UnitIsInInteractRange("target")` only if range semantics are documented and observed. Preserve raw outcomes if numeric bound unavailable.
4. Try preverified eligible `C_Item.IsItemInRange(itemID,"target")` checkers with recorded item IDs and known ranges (not invented). Avoid item casts, inventory consumption or assumptions about possession.
5. Consider `LibRangeCheck-3.0` only if a compatible lawful license/build is established and actual output improves confidence. Vendor source requires source/licence attribution and own spec approval if added.
6. Derive bracket only from validated thresholds; capture changes when player moves, different level deltas, combat and target swaps. Report unknown otherwise.

## Risks / security
Modern API can have restricted/secret return values in some contexts. Do not serialize them or try to bypass protections. Handle Lua errors and nil without spam. Only request results upon explicit slash command. No ground ring, no safety status. Changing gameplay estimation/ring logic beyond diagnostics requires a new OpenSpec.

## Evidence
Owner will post exact client version, available checker IDs/spells, screenshots/chat lines, target name/level and relative distance, and any error. Mark API candidate PASS, FAIL or INCONCLUSIVE separately. Distinguish `API available`, `check returned value`, `validated distance bracket` and `actual detection range`.
