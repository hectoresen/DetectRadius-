# DetectRadius

Experimental World of Warcraft: Forever addon for a **selected hostile NPC**. A1 uses a Classic-inspired *unverified* detection estimate based on player vs NPC levels; B1 places a **screen-space** red translucent ellipse beside the selected target's visible nameplate. The ring is illustrative, **not** a world-space ground circle or a safe distance boundary.

## Install experimental source

Copy **only** `addon/DetectRadius/` to `World of Warcraft/Interface/AddOns/DetectRadius/` so the file exists at `Interface/AddOns/DetectRadius/DetectRadius.toc`. On login check the AddOns menu. The TOC currently declares **Interface 16001 provisionally**; confirm the interface/build in your actual Forever client and enable "Load out of date AddOns" if appropriate. Do not interpret an addon loading as proof that the API works. To inspect errors use `/console scriptErrors 1` and `/reload`.

Commands:
- `/dr on`: enable target-only experiment.
- `/dr off`: disable and hide.
- `/dr`: display usage.

Setting persists across sessions; default off until explicitly activated. When nameplates are hidden/target invalid, the ring hides. It does **not** mark the actual ground; an estimated value in yards does not control the pixel radius.

## Tests and experiment status

Offline test command: `texlua tests/test_detection_estimate.lua`, `texlua tests/test_unit_api.lua`, `texlua tests/test_nameplate_api.lua`. Automated tests cannot establish in-game compatibility. **Owner Forever tests NOT RUN**: see [experiments](docs/EXPERIMENTS.md) and [testing](docs/TESTING.md). Screenshot/evidence required before calling B1 successful.

Engineering workflow is inherited from CraftAtlas conventions: [agent guidance](AGENTS.md), [contribution protocol](CONTRIBUTING.md), [architecture](docs/ARCHITECTURE.md), [OpenSpec](openspec/README.md). Do not merge/release without maintainer approval.
