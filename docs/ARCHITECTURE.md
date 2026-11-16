# DetectRadius architecture — A1/B1 experimental prototype

- `addon/DetectRadius/DetectRadius.toc`: addon load order. Interface 16001 is **provisional** pending client verification.
- `Domain/DetectionEstimate.lua`: pure, bounded level-delta heuristic, **not empirical Forever detection**.
- `Infrastructure/UnitApi.lua`: guarded hostile/valid target and levels.
- `Infrastructure/NameplateApi.lua`: safely query visible target nameplate through guarded `C_NamePlate.GetNamePlateForUnit`.
- `Features/Ring.lua`: cached screen-space red ellipse assembled from UI textures. Fixed pixel geometry, no conversion from estimate to accurate ground radius.
- `Core/Init.lua`: events, enable state persistence and `/dr on|off`.

**B1 has failed player testing and is no longer invoked.** The frame implementation remains isolated for historical review; the active addon only exposes the A1 estimate via `/dr estimate`. The previous UI frame anchored to a visible target nameplate, not to coordinates in the 3D world. Its offset does not vary with actual ground depth or yard distance. A target moving or the camera zooming may make the ellipse visually inaccurate or unavailable. It hides if the plate API is missing or attachment fails. Combat restrictions and actual API behavior remain **unverified**.

Keep this experiment isolated: no LibRangeCheck, ground decals, world coordinates, telemetry, all-NPC scanning or prohibited client APIs. SavedVariables only stores enabled state.

Specifications: `openspec/changes/estimate-level-and-nameplate-ring/`. The owner tests A1 and B1 separately and logs results. CI only checks structure/provenance; it does not prove visual accuracy.
