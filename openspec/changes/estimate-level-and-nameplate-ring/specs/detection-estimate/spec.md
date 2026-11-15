## ADDED Requirements

### Requirement: Hostile NPC estimate is explicitly approximate
DetectRadius SHALL calculate a deterministic illustrative detection-radius estimate from validated player and hostile NPC levels using `clamp(20 + npcLevel - playerLevel, 5, 45)` yards as a provisional model. It SHALL NOT claim exact or guaranteed detection safety.

#### Scenario: Equal levels
- **WHEN** player and selected hostile NPC are both level 30
- **THEN** the provisional estimate is 20 yards and is identified as approximate

#### Scenario: Different levels and clamping
- **WHEN** player level is 30 and hostile NPC is level 35
- **THEN** the provisional estimate is 25 yards
- **WHEN** the level difference exceeds the configured bounds
- **THEN** the estimate is clamped between 5 and 45 yards

#### Scenario: Unknown or inappropriate target
- **WHEN** the target is absent, friendly, a player, has unknown/skull level or an unavailable API value
- **THEN** the addon SHALL hide the estimate rather than invent a value

### Requirement: Disabled addon does no presentation work
DetectRadius SHALL provide explicit enable and disable slash commands and hide any visual instantly on disable.

#### Scenario: Toggle
- **WHEN** a player executes `/dr off`
- **THEN** the current ring disappears and no other units are scanned
