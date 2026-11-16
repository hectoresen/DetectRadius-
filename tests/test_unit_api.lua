-- Controlled WoW API test stubs; run: texlua tests/test_unit_api.lua
local ns = {}
local f = assert(loadfile("addon/DetectRadius/Infrastructure/UnitApi.lua"))
UnitExists = function(unit) return unit == "player" or unit == "target" end
UnitCanAttack = function(source, target) return source == "player" and target == "target" end
UnitIsPlayer = function() return false end
UnitLevel = function(unit) if unit == "player" then return 30 else return 35 end end
f("DetectRadius", ns)
local function check(player, target)
    local a, b = ns.UnitApi.GetHostileLevels()
    assert(a == player and b == target, "unexpected target level handling")
end
check(30,35)
UnitCanAttack = function() return false end
check(nil,nil)
UnitCanAttack = function() return true end
UnitIsPlayer = function() return true end
check(nil,nil)
UnitIsPlayer = function() return false end
UnitLevel = function() error("API missing") end
check(nil,nil)
print("PASS: guarded hostile target API stub test (not in-game validation)")
