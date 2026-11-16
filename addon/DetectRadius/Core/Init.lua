local addonName, ns = ...
ns = ns or {}

local enabled = false
local tracker
local events
local function printMessage(message)
    if DEFAULT_CHAT_FRAME and DEFAULT_CHAT_FRAME.AddMessage then
        DEFAULT_CHAT_FRAME:AddMessage("|cffff5555DetectRadius:|r " .. message)
    end
end

local function refresh()
    if not enabled then ns.Ring.Hide(); return end
    local playerLevel, npcLevel = ns.UnitApi.GetHostileLevels()
    local radius = ns.DetectionEstimate.Calculate(playerLevel, npcLevel)
    if not radius then ns.Ring.Hide(); return end
    local nameplate = ns.NameplateApi.GetTargetNameplate()
    if not nameplate then ns.Ring.Hide(); return end
    if not ns.Ring.ShowAt(nameplate, radius) then
        ns.Ring.Hide()
    end
end

local function setEnabled(value)
    enabled = value == true
    if DetectRadiusDB then DetectRadiusDB.enabled = enabled end
    if enabled then refresh() else ns.Ring.Hide() end
    printMessage(enabled and "ON (experimental, approximate)" or "OFF")
end

local function init()
    DetectRadiusDB = type(DetectRadiusDB) == "table" and DetectRadiusDB or {}
    enabled = DetectRadiusDB.enabled == true
    if type(SlashCmdList) == "table" then
        SLASH_DETECTRADIUS1 = "/dr"
        SLASH_DETECTRADIUS2 = "/detectradius"
        SlashCmdList.DETECTRADIUS = function(message)
            local cmd = (message or ""):match("^%s*(%S*)")
            cmd = (cmd or ""):lower()
            if cmd == "on" then setEnabled(true)
            elseif cmd == "off" then setEnabled(false)
            else printMessage("Use /dr on or /dr off") end
        end
    end
    refresh()
end

if type(CreateFrame) == "function" then
    events = CreateFrame("Frame")
    events:RegisterEvent("ADDON_LOADED")
    events:RegisterEvent("PLAYER_TARGET_CHANGED")
    events:RegisterEvent("NAME_PLATE_UNIT_ADDED")
    events:RegisterEvent("NAME_PLATE_UNIT_REMOVED")
    events:RegisterEvent("PLAYER_LEVEL_UP")
    events:SetScript("OnEvent", function(self, event, arg1)
        if event == "ADDON_LOADED" then
            if arg1 == addonName then init() end
        elseif enabled then
            refresh()
        end
    end)
end
