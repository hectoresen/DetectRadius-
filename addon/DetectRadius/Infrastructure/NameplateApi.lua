local addonName, ns = ...
ns = ns or {}
local adapter = {}
ns.NameplateApi = adapter

function adapter.GetTargetNameplate()
    if not C_NamePlate or type(C_NamePlate.GetNamePlateForUnit) ~= "function" then
        return nil
    end
    local ok, frame = pcall(C_NamePlate.GetNamePlateForUnit, "target")
    if not ok or not frame or type(frame.IsShown) ~= "function" then return nil end
    local shownOK, shown = pcall(frame.IsShown, frame)
    if not shownOK or not shown then return nil end
    return frame
end
