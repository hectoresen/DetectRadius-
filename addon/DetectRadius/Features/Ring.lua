local addonName, ns = ...
ns = ns or {}
local ring = {}
ns.Ring = ring

local overlay
local slices = 32
local width, height = 64, 23
local TWO_PI = math.pi * 2

local function atan2(y, x)
    if math.atan2 then return math.atan2(y, x) end
    if x > 0 then return math.atan(y / x) end
    if x < 0 then return math.atan(y / x) + (y >= 0 and math.pi or -math.pi) end
    if y > 0 then return math.pi / 2 end
    if y < 0 then return -math.pi / 2 end
    return 0
end

local function build()
    if overlay then return overlay end
    if type(CreateFrame) ~= "function" then return nil end
    local ok, result = pcall(CreateFrame, "Frame", nil, UIParent)
    if not ok or not result then return nil end
    overlay = result
    overlay:SetSize(width * 2 + 22, height * 2 + 22)
    overlay:SetFrameStrata("HIGH")
    overlay:Hide()
    -- Intentionally screen-space. This ellipse is NOT a yard-calibrated ground decal.
    for i = 1, slices do
        local a = TWO_PI * (i - 1) / slices
        local b = TWO_PI * i / slices
        local x1, y1 = width * math.cos(a), height * math.sin(a)
        local x2, y2 = width * math.cos(b), height * math.sin(b)
        local midX, midY = (x1 + x2) / 2, (y1 + y2) / 2
        local seg = overlay:CreateTexture(nil, "ARTWORK")
        seg:SetTexture("Interface\\Buttons\\WHITE8X8")
        seg:SetVertexColor(1, 0.12, 0.12, 0.70)
        seg:SetSize(math.sqrt((x2 - x1)^2 + (y2 - y1)^2) + 1, 3)
        seg:SetPoint("CENTER", overlay, "CENTER", midX, midY)
        if type(seg.SetRotation) == "function" then
            seg:SetRotation(atan2(y2 - y1, x2 - x1))
        end
    end

    local label = overlay:CreateFontString(nil, "OVERLAY", "GameFontNormalSmall")
    label:SetPoint("TOP", overlay, "BOTTOM", 0, -2)
    label:SetTextColor(1, 0.4, 0.4)
    overlay.label = label
    return overlay
end

function ring.Hide()
    if overlay then overlay:Hide() end
end

function ring.ShowAt(nameplate, radius)
    local frame = build()
    if not frame or not nameplate then return false end
    -- A forbidden/protected anchor can fail in combat. Hide on error.
    local ok = pcall(function()
        frame:Hide()
        frame:ClearAllPoints()
        frame:SetPoint("CENTER", nameplate, "CENTER", 0, -35)
        frame.label:SetText("~" .. tostring(radius) .. " yd (est.)")
        frame:Show()
    end)
    if not ok then ring.Hide() end
    return ok
end
