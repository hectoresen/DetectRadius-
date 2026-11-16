local addonName, ns = ...
ns = ns or {}
local adapter = {}
ns.UnitApi = adapter

local function safeBoolean(api, ...)
    if type(api) ~= "function" then return false end
    local ok, value = pcall(api, ...)
    return ok and value == true
end

function adapter.GetHostileLevels()
    if not safeBoolean(UnitExists, "target") then return nil end
    if not safeBoolean(UnitExists, "player") then return nil end
    if not safeBoolean(UnitCanAttack, "player", "target") then return nil end
    if safeBoolean(UnitIsPlayer, "target") then return nil end
    if type(UnitLevel) ~= "function" then return nil end

    local playerOK, playerLevel = pcall(UnitLevel, "player")
    local targetOK, targetLevel = pcall(UnitLevel, "target")
    if not playerOK or not targetOK then return nil end
    return playerLevel, targetLevel
end
