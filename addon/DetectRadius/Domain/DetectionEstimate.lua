local addonName, ns = ...
ns = ns or {}

local estimate = {}
ns.DetectionEstimate = estimate

local function validLevel(value)
    return type(value) == "number" and value > 0
        and value == math.floor(value) and value < 1000
end

function estimate.Calculate(playerLevel, npcLevel)
    if not validLevel(playerLevel) or not validLevel(npcLevel) then
        return nil
    end

    -- A1: Classic-inspired placeholder. NOT a measured Forever pull distance.
    return math.max(5, math.min(45, 20 + npcLevel - playerLevel))
end
