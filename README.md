# DetectRadius

**Planned World of Warcraft: Forever addon.** Goal: display an estimated detection range for a targeted hostile NPC with a translucent red ring, based in part on player-vs-target level difference.

> **Status: design/research only.** This repository does **not** yet contain a playable addon. No estimate, screen-space rendering or exact ground-locked ring has been validated in-game. Do not interpret a future visual ring as a guaranteed safe path.

## Experiment-first roadmap

[Ordered experimental checklist and owner test template](docs/EXPERIMENTS.md). Candidates cover the Classic-inspired level difference heuristic, observed pull calibration, range-check APIs and handling of exceptional NPCs; separately they investigate nameplate-anchored rings, target-frame overlays, projected illusions, minimap and HUD alternatives. Each candidate will be tested and logged separately, prioritizing success likelihood.

## Engineering workflow

The architecture and agent development workflow are adapted from [CraftAtlas](https://github.com/hectoresen/CraftAtlas): lightweight Lua, separation of domain and game API, OpenSpec/spec-first proposals in an owner-merged PR, separate implementation PR, docs synchronization and explicit player acceptance in the Forever client.

Read [AGENTS.md](AGENTS.md), [CONTRIBUTING.md](CONTRIBUTING.md), [architecture](docs/ARCHITECTURE.md), [testing](docs/TESTING.md), [OpenSpec](openspec/README.md), [GitHub governance](docs/GITHUB_GOVERNANCE.md) and [agent workflow](docs/AGENT_WORKFLOW.md).

Server-side GitHub branch protections and complete CraftAtlas SDD automation must be verified/configured separately. A policy in this repository does **not** itself enforce permissions or prove gameplay functionality.

This project is independent of Blizzard and WoW Forever operators.
