# Maps — v5 baseline (awaiting v7 STOR)

These 5 bugs are present in **both** the v5 corpus (`test-bug-panel`) and the v7 corpus (`test-bug-panel-five-year-refresh`).

v7 has not processed this category yet, so each bug carries the original report plus v5's enhanced output as a baseline:

| file | produced by |
|---|---|
| `MC-XXX_v5_improved.json` | v5 — gpt-5.6-luna, full report (S2R + Environment + Observed + Expected) |
| `MC-XXX_v5_improved.pdf` | v5 worksheet |

**No `_stor.json` is present.** These are not v7 output. When v7 reaches this category it will generate `MC-XXX_stor.json` + `MC-XXX.pdf` alongside these files — the resume check keys on `_stor.json`, so nothing here causes a bug to be skipped.

## Bugs

- MC-124331
- MC-179858
- MC-236740
- MC-249171
- MC-249172
