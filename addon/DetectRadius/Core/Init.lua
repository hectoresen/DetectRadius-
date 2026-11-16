local addonName, ns = ...
ns = ns or {}

local enabled = false
local events

local function printMessage(message)
    if DEFAULT_CHAT_FRAME and DEFAULT_CHAT_FRAME.AddMessage then
        DEFAULT_CHAT_FRAME:AddMessage("|cffff5555DetectRadius:|r " .. message)
    end
end

-- A1 remains available as a diagnostic estimate only.
-- B1 is disabled after the owner's real-client test showed a false spatial boundary.
local function reportEstimate()
    if not enabled then return end
    local playerLevel, npcLevel = ns.UnitApi.GetHostileLevels()
    local radius = ns.DetectionEstimate.Calculate(playerLevel, npcLevel)
    if radius then
        printMessage("Target estimate: ~" .. tostring(radius) .. " yd (unverified; not a safe distance)")
    else
        printMessage("No valid hostile NPC estimate")
    end
end

local function setEnabled(value)
    enabled = value == true
    if DetectRadiusDB then DetectRadiusDB.enabled = enabled end
    if ns.Ring then ns.Ring.Hide() end
    printMessage(enabled and "ON (diagnostic only; visual ring disabled)" or "OFF")
end

local function init()
    DetectRadiusDB = type(DetectRadiusDB) == "table" and DetectRadiusDB or {}
    enabled = DetectRadiusDB.enabled == true
    if ns.Ring then ns.Ring.Hide() end
    if type(SlashCmdList) == "table" then
        SLASH_DETECTRADIUS1 = "/dr"
        SLASH_DETECTRADIUS2 = "/detectradius"
        SlashCmdList.DETECTRADIUS = function(message)
            local cmd = (message or ""):match("^%s*(%S*)")
            cmd = (cmd or ""):lower()
            if cmd == "on" then setEnabled(true)
            elseif cmd == "off" then setEnabled(false)
            elseif cmd == "estimate" then reportEstimate()
            else printMessage("Use /dr on, /dr off or /dr estimate") end
        end
    end
end

if type(CreateFrame) == "function" then
    events = CreateFrame("Frame")
    events:RegisterEvent("ADDON_LOADED")
    events:SetScript("OnEvent", function(self, event, arg1)
        if event == "ADDON_LOADED" and arg1 == addonName then
            init()
        end
    end)
end
