-- Pure logic regression; run: texlua tests/test_detection_estimate.lua
local ns = {}
local f = assert(loadfile("addon/DetectRadius/Domain/DetectionEstimate.lua"))
f("DetectRadius", ns)
local calc = ns.DetectionEstimate.Calculate
local function equal(actual, expected)
    assert(actual == expected, tostring(actual) .. " ~= " .. tostring(expected))
end
equal(calc(30,30), 20)
equal(calc(30,35), 25)
equal(calc(30,20), 10)
equal(calc(60,1), 5)
equal(calc(1,60), 45)
equal(calc(nil,30), nil)
equal(calc(30,-1), nil)
equal(calc(30,0), nil)
equal(calc(30,30.5), nil)
equal(calc("30",30), nil)
equal(calc(30,math.huge), nil)
print("PASS: detection estimate A1 (not in-game validation)")
