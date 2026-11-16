# DetectRadius

Experimental World of Warcraft: Forever addon. A1 computes a **provisional, unverified** level-based estimate. **B1 red ring was disabled following real-game failure:** it remained a small screen-space shape and the user was attacked outside it. No ground-space safe perimeter is available.

## Install experimental source

Copy **only** `addon/DetectRadius/` to `World of Warcraft/Interface/AddOns/DetectRadius/` so the file exists at `Interface/AddOns/DetectRadius/DetectRadius.toc`. On login check the AddOns menu. The TOC currently declares **Interface 16001 provisionally**; confirm the interface/build in your actual Forever client and enable "Load out of date AddOns" if appropriate. Do not interpret an addon loading as proof that the API works. To inspect errors use `/console scriptErrors 1` and `/reload`.

Commands:
- `/dr on`: enable target-only experiment.
- `/dr off`: disable and hide.
- `/dr estimate`: chat-only estimate for selected hostile NPC; **not a safe range**.\n- `/dr`: display usage.

Setting persists across sessions; default off until explicitly activated. No ring is displayed, even when enabled. The previous fixed-pixel visual was rejected; this build is diagnostic-only.

## Tests and experiment status

Offline test command: `texlua tests/test_detection_estimate.lua`, `texlua tests/test_unit_api.lua`, `texlua tests/test_nameplate_api.lua`. Automated tests cannot establish in-game compatibility. **B1 visual test FAILED in-game; new diagnostic-only revision NOT RUN**: see [experiments](docs/EXPERIMENTS.md) and [testing](docs/TESTING.md). Screenshot/evidence required before calling B1 successful.

Engineering workflow is inherited from CraftAtlas conventions: [agent guidance](AGENTS.md), [contribution protocol](CONTRIBUTING.md), [architecture](docs/ARCHITECTURE.md), [OpenSpec](openspec/README.md). Do not merge/release without maintainer approval.
