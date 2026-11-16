## ADDED Requirements

### Requirement: Explicit non-invasive enemy range diagnostics
The addon SHALL expose an on-demand command that probes only the currently selected hostile non-player NPC using APIs available on the running Forever client, and SHALL display the API source and only validated range conclusions.

#### Scenario: API absent or invalid
- **WHEN** an API is absent, errors, returns nil, or cannot be applied to the target
- **THEN** that check SHALL be marked unavailable/unknown and SHALL NOT imply distance

#### Scenario: Eligible range checker
- **WHEN** a documented checker with a verified numerical threshold yields a supported boolean on a hostile target
- **THEN** the addon SHALL report its source, threshold and in/out status with a clear approximation disclaimer

#### Scenario: Combining checks
- **WHEN** compatible monotonic validated checks bound the same selected target
- **THEN** the addon MAY report a distance interval with justified lower/upper bounds
- **WHEN** evidence conflicts or a checker lacks reliable range semantics
- **THEN** the addon SHALL report unknown/conflict instead of a fabricated interval

#### Scenario: No target or friend
- **WHEN** no hostile NPC is targeted or diagnostics are disabled
- **THEN** no proximity estimate SHALL be made

### Requirement: No misleading safe perimeter
The A3 implementation SHALL NOT reactivate B1, draw a 3D/2D danger ring, call a measured spell range an aggro radius, or assert a safe path.

#### Scenario: Target inside a spell range
- **WHEN** the target is inside a 30-yard applicable spell checker
- **THEN** the output SHALL NOT assert its detection range is 30 yards

### Requirement: Manual Forever verification
Before any A3 verdict is accepted, the maintainer SHALL record build, class/character constraints, NPC, outcomes, relevant errors and evidence. Offline CI success SHALL NOT substitute for in-game evidence.

#### Scenario: Evidence required before acceptance
- **WHEN** the maintainer evaluates an A3 range-check result in the Forever game client
- **THEN** the test record SHALL include the actual client build, character class, selected NPC, observed check outputs, relevant Lua errors and supporting evidence, and SHALL distinguish in-game observations from offline CI results
