"""Replace v7/Networking with the new five-bug set and regenerate STOR from scratch.

The new panel keeps MC-251889 and MC-74984, adds MC-250918 / MC-268431 / MC-299627,
and drops MC-10025 / MC-26678 / MC-4. All five are regenerated -- none are carried
over -- so the category is internally consistent.

Two of the new reports carry a different original Mojira category in their filename
([Inventory], [Projectiles]). The source filenames are preserved as-is per v7
convention; the STOR record's `category` is set to Networking (the v7 folder it lives
in) with `source_category` recording the original label.
"""
import json
import shutil
import sys
import time
from pathlib import Path

SCRATCH = Path("/private/tmp/claude-501/-Users-nish-Documents-minecraft-agents/27b27372-6b02-42e0-bb38-7d997ff1ffaa/scratchpad")
sys.path.insert(0, str(SCRATCH))
import v7_stor
import v7_pdf

NEW = Path("/Users/nish/Documents/Research - Minecraft/data_collection/outputs/networking_five_bug_reports")
V7 = Path("/Users/nish/Documents/agentcraft/agentcraft/test-categories/v7")
CAT = "Networking"
DST = V7 / CAT


def main():
    new_bugs = sorted(d for d in NEW.iterdir() if d.is_dir() and d.name.startswith("MC-"))
    keep = {d.name for d in new_bugs}
    print(f"new set: {sorted(keep)}")

    # 1. drop bugs no longer in the panel
    for old in sorted(p for p in DST.iterdir() if p.is_dir()):
        if old.name not in keep:
            shutil.rmtree(old)
            print(f"  removed {old.name}")

    # 2. clear stale STOR for the retained bugs so they regenerate
    for b in keep:
        sp = DST / b / f"{b}_stor.json"
        if sp.exists():
            sp.unlink()
            print(f"  cleared stale STOR for {b}")
    log = DST / "_stor_log.jsonl"
    if log.exists():
        log.unlink()

    # 3. mirror originals + generate
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
            print(f"  [{i}/5] {bug}: SKIP (no .md)")
            failed += 1
            continue

        src_label = md_src.name.split("]")[0].lstrip("[") if md_src.name.startswith("[") else ""
        md_text = md_src.read_text(encoding="utf-8")
        try:
            stor, meta = v7_stor.enhance_stor(md_text)
        except v7_stor.CreditsExhausted:
            print(f"\n!! ALL API KEYS OUT OF CREDIT — stopping at {bug}")
            return 9
        except Exception as e:
            print(f"  [{i}/5] {bug}: ERROR {type(e).__name__}: {str(e)[:150]}")
            failed += 1
            continue

        rec = {"bug_id": bug, "category": CAT, "source_category": src_label,
               "source_panel": "networking_five_bug_reports",
               "source_md": md_src.name,
               "source_meta": v7_stor.parse_md_meta(md_text),
               "stor": stor, "call": meta}
        (target / f"{bug}_stor.json").write_text(
            json.dumps(rec, indent=2, ensure_ascii=False), encoding="utf-8")
        with log.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        ok += 1
        print(f"  [{i}/5] {bug} [{src_label}]: {len(stor.get('steps', []))} steps  "
              f"trigger={stor.get('trigger_step')}  web={meta['web_call_count']}  "
              f"{meta['elapsed_seconds']:.0f}s", flush=True)

    # 4. worksheets — remove stale PDFs first so nothing survives from the old set
    for p in DST.glob("*/*.pdf"):
        p.unlink()
    v7_pdf.V7_ROOT = V7
    v7_pdf.process_category(CAT)

    n_stor = len(list(DST.glob("*/*_stor.json")))
    n_pdf = len(list(DST.glob("*/*.pdf")))
    n_dir = len([p for p in DST.iterdir() if p.is_dir()])
    print(f"\nNetworking: dirs={n_dir} stor={n_stor} pdf={n_pdf} (ok={ok} failed={failed})")
    return 0 if (n_dir == n_stor == n_pdf == 5) else 1


if __name__ == "__main__":
    sys.exit(main())
