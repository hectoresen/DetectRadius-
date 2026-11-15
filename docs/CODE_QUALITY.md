# Code quality expectations (planned)

Prefer small Lua modules, pure domain math, explicit nil/unknown handling, no leaking WoW globals into pure tests, guarded client APIs and robust target-state changes. Throttle updates and allocate UI widgets once. Only reuse correctly licensed assets. Avoid external dependencies unless benchmarked. Each function should have one responsibility; tests should cover boundary levels and UI cleanup. Fail closed on unsafe or misleading display.

Source code does not exist yet; this is the standard for future approved implementation.
