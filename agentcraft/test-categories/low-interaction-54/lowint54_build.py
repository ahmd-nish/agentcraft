"""Assemble the low-interaction-54 panel: one folder per bug, everything we hold.

Source of truth for membership is selected-low-interaction-bugs.csv (54 rows).
Each bug folder gets the original report from the low-interaction corpus, plus any
enhancement already produced elsewhere (v7 STOR + worksheet, v5 baseline), copied in
rather than referenced so the panel stands alone.

Binary attachments are excluded corpus-wide (this corpus carries png/mp4/zip).
"""
import csv
import shutil
import sys
from pathlib import Path

SRC = Path("/Users/nish/Documents/Research - Minecraft/data_collection/test-bug-panel-low-interaction-54")
CSV_IN = SRC / "selected-low-interaction-bugs.csv"
V7 = Path("/Users/nish/Documents/agentcraft/agentcraft/test-categories/v7")
V5 = Path("/Users/nish/Documents/agentcraft/agentcraft/test-categories/v5")
PANEL = Path("/Users/nish/Documents/agentcraft/agentcraft/test-categories/low-interaction-54")

TEXT_ATTACH_EXT = {".log", ".txt", ".nbt", ".java", ".json", ".mcfunction", ".yml", ".properties"}


def copy_new(src: Path, dst: Path) -> int:
    if not src.exists() or dst.exists():
        return 0
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return 1


def main():
    rows = list(csv.DictReader(CSV_IN.open()))
    assert len({r["bug_id"] for r in rows}) == len(rows) == 54, f"expected 54 unique, got {len(rows)}"
    PANEL.mkdir(parents=True, exist_ok=True)
    copy_new(CSV_IN, PANEL / CSV_IN.name)

    v5dirs = {d.name: d for d in V5.glob("*/MC-*") if d.is_dir()}
    v7dirs = {d.name: d for d in V7.glob("*/MC-*") if d.is_dir()}

    stats = {"raw": 0, "v7": 0, "v5": 0}
    for r in rows:
        bug, cat = r["bug_id"], r["category"]
        sdir = Path(r["packaged_folder"])
        target = PANEL / bug
        target.mkdir(parents=True, exist_ok=True)

        # 1. original report from this panel's own corpus
        for f in sdir.iterdir():
            if f.is_file() and f.suffix.lower() in {".json", ".md"}:
                copy_new(f, target / f.name)
        att = sdir / "attachments"
        if att.is_dir():
            for f in att.iterdir():
                if f.is_file() and f.suffix.lower() in TEXT_ATTACH_EXT:
                    copy_new(f, target / "attachments" / f.name)
        stats["raw"] += 1

        # 2. existing v7 STOR + worksheet
        v7d = v7dirs.get(bug)
        if v7d and (v7d / f"{bug}_stor.json").exists():
            copy_new(v7d / f"{bug}_stor.json", target / f"{bug}_stor.json")
            copy_new(v7d / f"{bug}.pdf", target / f"{bug}.pdf")
            stats["v7"] += 1

        # 3. existing v5 baseline (kept even once v7 STOR lands — they differ in kind)
        v5d = v5dirs.get(bug)
        if v5d and (v5d / f"{bug}_improved.json").exists():
            copy_new(v5d / f"{bug}_improved.json", target / f"{bug}_v5_improved.json")
            copy_new(v5d / f"{bug}.pdf", target / f"{bug}_v5_improved.pdf")
            stats["v5"] += 1

    missing = [r["bug_id"] for r in rows
               if not (PANEL / r["bug_id"] / f"{r['bug_id']}_stor.json").exists()]
    print(f"panel: {PANEL}")
    print(f"  bug folders    : {len(rows)}")
    print(f"  with v7 STOR   : {stats['v7']}")
    print(f"  with v5 baseline: {stats['v5']}")
    print(f"  NEED STOR      : {len(missing)}")
    (PANEL / "_need_stor.txt").write_text("\n".join(missing) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
