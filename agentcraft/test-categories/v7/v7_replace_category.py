"""Replace a v7 category with a new bug panel and regenerate STOR + worksheets.

  python v7_replace_category.py <source_dir> <v7_category> [source_panel_label]

Generalised from the Networking swap. The source dir holds one <MC-ID>/ folder per
bug; anything currently in the v7 category that is not in the new panel is removed,
and every bug in the new panel is generated from scratch (no records carried over,
so the category is internally consistent).

Panel-level provenance files (README.md, _selection.csv, _summary.json,
_attachment_manifest.csv) are copied in with a _source_ prefix so the selection
criteria travel with the data.
"""
import json
import shutil
import sys
from pathlib import Path

SCRATCH = Path("/private/tmp/claude-501/-Users-nish-Documents-minecraft-agents/27b27372-6b02-42e0-bb38-7d997ff1ffaa/scratchpad")
sys.path.insert(0, str(SCRATCH))
import v7_stor
import v7_pdf

V7 = Path("/Users/nish/Documents/agentcraft/agentcraft/test-categories/v7")
PROVENANCE = {"README.md", "_selection.csv", "_summary.json", "_attachment_manifest.csv"}


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    SRC = Path(sys.argv[1])
    CAT = sys.argv[2]
    PANEL = sys.argv[3] if len(sys.argv) > 3 else SRC.name
    DST = V7 / CAT
    if not SRC.is_dir():
        print(f"!! no such source dir: {SRC}")
        return 2
    DST.mkdir(parents=True, exist_ok=True)

    new_bugs = sorted(d for d in SRC.iterdir() if d.is_dir() and d.name.startswith("MC-"))
    keep = {d.name for d in new_bugs}
    print(f"[{CAT}] new set ({len(keep)}): {sorted(keep)}")

    # 1. drop bugs no longer in the panel
    for old in sorted(p for p in DST.iterdir() if p.is_dir()):
        if old.name not in keep:
            shutil.rmtree(old)
            print(f"  removed {old.name}")

    # 2. clear stale STOR so retained bugs regenerate too
    for b in sorted(keep):
        sp = DST / b / f"{b}_stor.json"
        if sp.exists():
            sp.unlink()
            print(f"  cleared stale STOR for {b}")
    log = DST / "_stor_log.jsonl"
    if log.exists():
        log.unlink()

    # 3. panel provenance
    for f in SRC.iterdir():
        if f.is_file() and f.name in PROVENANCE:
            shutil.copy2(f, DST / f"_source_{f.name.lstrip('_')}")

    # 4. mirror + generate
    ok = failed = 0
    for i, sdir in enumerate(new_bugs, 1):
        bug = sdir.name
        target = DST / bug
        target.mkdir(parents=True, exist_ok=True)

        md_src = None
        for f in sdir.iterdir():
            if f.is_file() and f.suffix.lower() in {".json", ".md"}:
                shutil.copy2(f, target / f.name)
                if f.suffix.lower() == ".md":
                    md_src = target / f.name
        att = sdir / "attachments"
        if att.is_dir():
            for f in att.iterdir():
                if f.is_file() and f.suffix.lower() in v7_stor.TEXT_ATTACH_EXT:
                    d = target / "attachments" / f.name
                    d.parent.mkdir(exist_ok=True)
                    shutil.copy2(f, d)

        if md_src is None:
            print(f"  [{i}/{len(new_bugs)}] {bug}: SKIP (no .md)")
            failed += 1
            continue

        label = md_src.name.split("]")[0].lstrip("[") if md_src.name.startswith("[") else ""
        md_text = md_src.read_text(encoding="utf-8")
        try:
            stor, meta = v7_stor.enhance_stor(md_text)
        except v7_stor.CreditsExhausted:
            print(f"\n!! ALL API KEYS OUT OF CREDIT — stopping at {bug}")
            return 9
        except Exception as e:
            print(f"  [{i}/{len(new_bugs)}] {bug}: ERROR {type(e).__name__}: {str(e)[:150]}")
            failed += 1
            continue

        rec = {"bug_id": bug, "category": CAT, "source_category": label,
               "source_panel": PANEL, "source_md": md_src.name,
               "source_meta": v7_stor.parse_md_meta(md_text),
               "stor": stor, "call": meta}
        (target / f"{bug}_stor.json").write_text(
            json.dumps(rec, indent=2, ensure_ascii=False), encoding="utf-8")
        with log.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        ok += 1
        print(f"  [{i}/{len(new_bugs)}] {bug} [{label}]: {len(stor.get('steps', []))} steps  "
              f"trigger={stor.get('trigger_step')}  web={meta['web_call_count']}  "
              f"{meta['elapsed_seconds']:.0f}s", flush=True)

    # 5. worksheets — clear stale first so nothing survives from the old set
    for p in DST.glob("*/*.pdf"):
        p.unlink()
    v7_pdf.V7_ROOT = V7
    v7_pdf.process_category(CAT)

    n_dir = len([p for p in DST.iterdir() if p.is_dir()])
    n_stor = len(list(DST.glob("*/*_stor.json")))
    n_pdf = len(list(DST.glob("*/*.pdf")))
    print(f"\n[{CAT}] dirs={n_dir} stor={n_stor} pdf={n_pdf} (ok={ok} failed={failed})")
    return 0 if (n_dir == n_stor == n_pdf == len(new_bugs)) else 1


if __name__ == "__main__":
    sys.exit(main())
