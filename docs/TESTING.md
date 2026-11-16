# DetectRadius testing

## Offline (repeat and record executed results)
```sh
python3 scripts/validate_repo.py
texlua tests/test_detection_estimate.lua
texlua tests/test_unit_api.lua
texlua tests/test_nameplate_api.lua
```
These test pure math and guarded API stubs. They do not test actual Forever APIs. Report any missing `texlua` interpreter as NOT RUN.

## Owner-only in-game acceptance checklist (one screenshot received, most checks NOT RUN)
- [ ] Record Forever game build/interface number, locale, client version.
- [ ] Copy addon folder, enable, `/console scriptErrors 1`, `/reload`.
- [ ] `/dr on` and `/dr off` activate/hide reliably; reload preserves state.
- [ ] At least two hostile NPCs with different level deltas: observe `~Y yd (est.)`, compare with formula (not actual aggro).
- [ ] Friendly, player, unknown/skull level, no target: ring hidden.
- [ ] Target nameplate visible/hidden, target switch, target leaves view or despawns.
- [ ] Camera zoom, UI scale, resolution and combat/noncombat show no stuck/misleading ring or Lua errors.
- [x] Initial screenshot received: visible B1 ellipse underneath Basilisco Ojogélido nameplate and ~32 yd estimate; initial vertical position too high. No true detection threshold measured.\n- [ ] Re-test new B1 -100 UI unit offset using the same NPC, camera movement and closer/farther targets; record screenshot and whether it is actually near its feet.\n- [ ] Record additional screenshot/video and observed detection threshold separately, no invented exact range.
- [ ] Explicitly mark B1 PASS/FAIL/INCONCLUSIVE and whether candidate B2 is warranted.

Important: illustrative ring radius is fixed in screen pixels and **cannot tell the player where the safe ground boundary lies**. Misleading visuals should FAIL B1.

Use report template in `docs/EXPERIMENTS.md`. One screenshot has been supplied; the updated offset is **NOT RUN** in-game.
