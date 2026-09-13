"""Backfill the 33 bugs shared between the v5 and v7 corpora into v7/<Category>/<MC-ID>/.

v7 cannot generate STOR right now (no API credit), so each backfilled bug gets the
original report plus v5's enhanced output as a *baseline*, named so it can never be
mistaken for — or overwritten by — v7's own STOR worksheet:

    MC-XXX_v5_improved.json   v5 enhanced report  (gpt-5.6-luna, full S2R+Env+OB+EB)
    MC-XXX_v5_improved.pdf    v5 worksheet

Bugs already present in v7 are left byte-for-byte untouched: this script never writes
into a directory that already contains a *_stor.json, and never overwrites an existing
file. When v7 later reaches these categories it will still process every one of them,
because the resume check keys on *_stor.json, which this script does not create.
"""
import json
import shutil
import sys
from pathlib import Path

SRC7 = Path("/Users/nish/Documents/Research - Minecraft/data_collection/test-bug-panel-five-year-refresh")
SRC5 = Path("/Users/nish/Documents/Research - Minecraft/data_collection/test-bug-panel")
V5 = Path("/Users/nish/Documents/agentcraft/agentcraft/test-categories/v5")
V7 = Path("/Users/nish/Documents/agentcraft/agentcraft/test-categories/v7")

TEXT_ATTACH_EXT = {".log", ".txt", ".nbt", ".java", ".json", ".mcfunction", ".yml", ".properties"}


def bug_dirs(root):
    """{MC-ID: path} for every bug directory under a corpus root."""
    return {d.name: d for d in root.glob("*/*") if d.is_dir() and d.name.startswith("MC-")}


def copy_new(src: Path, dst: Path) -> bool:
    """Copy only if absent. Returns True if written."""
    if dst.exists():
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return True


def main():
    shared = sorted(set(bug_dirs(SRC7)) & set(bug_dirs(SRC5)))
    src7 = bug_dirs(SRC7)
    print(f"shared v5/v7 corpus bugs: {len(shared)}")

    written, skipped_existing, by_cat = 0, 0, {}

    for bug_id in shared:
        sdir = src7[bug_id]
        cat = sdir.parent.name
        target = V7 / cat / bug_id

        # Already produced by v7 proper — leave completely alone.
        if list(target.glob("*_stor.json")):
            skipped_existing += 1
            continue

        n = 0
        # 1. original report (from the v7 corpus, so provenance stays consistent)
        for f in sdir.iterdir():
            if f.is_file() and f.suffix.lower() in {".json", ".md"}:
                n += copy_new(f, target / f.name)

        # 2. text attachments only — binaries are excluded corpus-wide
        att = sdir / "attachments"
        if att.is_dir():
            for f in att.iterdir():
                if f.is_file() and f.suffix.lower() in TEXT_ATTACH_EXT:
                    n += copy_new(f, target / "attachments" / f.name)

        # 3. v5 baseline, distinctly named
        v5dir = V5 / cat / bug_id
        for src, dstname in (
            (v5dir / f"{bug_id}_improved.json", f"{bug_id}_v5_improved.json"),
            (v5dir / f"{bug_id}.pdf", f"{bug_id}_v5_improved.pdf"),
        ):
            if src.exists():
                n += copy_new(src, target / dstname)
            else:
                print(f"  !! missing v5 artifact: {src}")

        if n:
            written += 1
            by_cat.setdefault(cat, []).append(bug_id)

    # Per-category provenance note so the folders are self-explaining.
    for cat, ids in sorted(by_cat.items()):
        (V7 / cat / "_V5_BASELINE.md").write_text(
            f"# {cat} — v5 baseline (awaiting v7 STOR)\n\n"
            f"These {len(ids)} bugs are present in **both** the v5 corpus "
            f"(`test-bug-panel`) and the v7 corpus (`test-bug-panel-five-year-refresh`).\n\n"
            "v7 has not processed this category yet, so each bug carries the original "
            "report plus v5's enhanced output as a baseline:\n\n"
            "| file | produced by |\n|---|---|\n"
            f"| `MC-XXX_v5_improved.json` | v5 — gpt-5.6-luna, full report (S2R + Environment + Observed + Expected) |\n"
            f"| `MC-XXX_v5_improved.pdf` | v5 worksheet |\n\n"
            "**No `_stor.json` is present.** These are not v7 output. When v7 reaches "
            "this category it will generate `MC-XXX_stor.json` + `MC-XXX.pdf` alongside "
            "these files — the resume check keys on `_stor.json`, so nothing here causes "
            "a bug to be skipped.\n\n"
            "## Bugs\n\n" + "\n".join(f"- {b}" for b in sorted(ids)) + "\n"
        )

    print(f"\nbackfilled       : {written} bugs")
    print(f"left untouched   : {skipped_existing} bugs (already have v7 STOR)")
    print(f"categories       : {len(by_cat)}")
    for cat, ids in sorted(by_cat.items()):
        print(f"  {cat:<16} {len(ids)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
