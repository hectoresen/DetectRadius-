# Testing / evidence

Status: documentation scaffold, addon not implemented, no in-game tests run.

## Automated checks
When implemented, separately test pure Domain estimation (bounds, level parity, invalid/skull inputs), guarded Infrastructure wrappers, state toggles, frame attachment cleanup and packaging paths. CI cannot emulate the real client. Document exact checks run, and say NOT RUN for others.

## In-game test protocol
1. Enable /console scriptErrors 1; /reload; record Forever exact client build and interface.
2. Test addon disabled/enabled, selected hostile/neutral/friendly/no target and target switching.
3. For one fixed NPC, approach from multiple positions while logging whether the actual pull happens; vary level delta only through controlled scenarios.
4. Repeat nameplate visible/hidden, zoom/UI scale, combat, occlusion, vertical differences and crowded nameplates.
5. Record each candidate from docs/EXPERIMENTS.md with PASS/FAIL/INCONCLUSIVE and screenshot/video.
6. Capture any FPS change, Lua error, inaccurate screen anchoring and misleading indication; revert invalid prototype.

No automated or documentation check establishes that an estimated ring corresponds to the actual safe in-game path.
