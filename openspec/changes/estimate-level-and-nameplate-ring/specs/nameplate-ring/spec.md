## ADDED Requirements

### Requirement: Optional nameplate-anchored visual experiment
DetectRadius SHALL attempt one red semi-transparent **2D** ring for the selected valid hostile NPC, using only APIs confirmed available and permitted in the current WoW Forever client. It SHALL NOT claim to render a true in-world ground decal, nor scale the ring as a physically accurate yard radius without independent evidence.

#### Scenario: Nameplate visible and API permitted
- **WHEN** the player enables DetectRadius, selects a valid hostile NPC, and its nameplate can be safely resolved
- **THEN** one red translucent ring appears anchored to the target's visible screen-space nameplate and is clearly experimental/approximate

#### Scenario: Nameplate missing or blocked
- **WHEN** the target nameplate is absent, API is unavailable, or a protected operation is blocked
- **THEN** the addon hides the ring without throwing a Lua error or fabricating a location

#### Scenario: Target/visibility lifecycle
- **WHEN** target changes, becomes invalid or friendly, nameplate disappears, or addon is disabled
- **THEN** the old ring hides and no stale overlay remains

### Requirement: Real-game validation before accuracy claims
The implementation SHALL document the actual client build, Lua errors, screenshots and results under varying camera zoom, UI scale, nameplate visibility and combat conditions.

#### Scenario: Misleading visual
- **WHEN** the ring appears to imply a guaranteed physical safe boundary or cannot follow the intended target reliably
- **THEN** the experiment is recorded as failed or inconclusive and no accuracy claim is made
