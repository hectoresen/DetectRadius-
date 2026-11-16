-- Safe failure and visibility stubs; run: texlua tests/test_nameplate_api.lua
local ns = {}
local f = assert(loadfile("addon/DetectRadius/Infrastructure/NameplateApi.lua"))
C_NamePlate = nil
f("DetectRadius", ns)
assert(ns.NameplateApi.GetTargetNameplate() == nil)
local plate = {IsShown=function() return true end}
C_NamePlate = {GetNamePlateForUnit=function(unit) assert(unit=="target"); return plate end}
assert(ns.NameplateApi.GetTargetNameplate() == plate)
plate.IsShown=function() return false end
assert(ns.NameplateApi.GetTargetNameplate() == nil)
C_NamePlate.GetNamePlateForUnit=function() error("restricted") end
assert(ns.NameplateApi.GetTargetNameplate() == nil)
print("PASS: guarded nameplate API stub test (not in-game validation)")
