# DetectRadius architecture — planned, not implemented

Status: documentation-only bootstrap. No working addon exists yet.

Expected lightweight source layout after approved spec:
```
addon/DetectRadius/
  DetectRadius.toc
  Core/                 addon lifecycle and enable/disable
  Domain/               pure level-delta estimate and limits
  Infrastructure/       guarded unit, nameplate and range adapters
  Features/             2D ring, fallback HUD and settings
  Localization/         enUS / esES
openspec/               approved requirements and proposals
docs/                   experiment matrix and owner observations
scripts/                offline structural/packaging checks (when added)
tests/                  pure Lua behavior tests (when added)
skills/                  mandatory documentation sync
```

Architectural constraint: the UI layer cannot paint a genuine 3D decal on ground using ordinary WoW Lua frames; nameplate-anchored overlays are 2D approximations. Distance returned from spell range checks is generally a range/interval, not exact coordinate separation. Calculating an approximate radius does not automatically imply drawing an accurate screen-sized ring.

Guard every API for Forever client build and combat/security restrictions. Avoid frame-by-frame scans, allocate textures once, throttle sampling and skip unselected or invalid targets. No dependency unless a measured experiment proves it necessary. Keep estimates in Domain so tests can exercise edge conditions without game globals.

Do not reuse CraftAtlas's profession-specific data pipeline, catalogs, components or product claims. Reuse its *development conventions* and review gates only.
