"""Enhance four v7 categories, pushing after each one completes.

Order: Debug, Data Packs, Datafixer, Save Data.

Bugs whose STOR already exists in the low-interaction-54 panel are copied across
instead of regenerated -- same model, same prompt, same schema, so the record is
identical and the API call is wasted work. The copy is re-keyed to its v7 category.

Push happens only after a category reaches full stor==pdf coverage, so a category is
never pushed half-rendered.
"""
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

SCRATCH = Path("/private/tmp/claude-501/-Users-nish-Documents-minecraft-agents/27b27372-6b02-42e0-bb38-7d997ff1ffaa/scratchpad")
sys.path.insert(0, str(SCRATCH))
import v7_stor
import v7_pdf

REPO = Path("/Users/nish/Documents/agentcraft")
SRC = v7_stor.SRC_ROOT
V7 = v7_stor.V7_ROOT
PANEL = REPO / "agentcraft/test-categories/low-interaction-54"
CATS = ["Debug", "Data Packs", "Datafixer", "Save Data"]


def sh(*a):
    return subprocess.run(a, cwd=REPO, capture_output=True, text=True)


def push(cat, note):
    rel = f"agentcraft/test-categories/v7/{cat}"
    sh("git", "add", "--", rel)
    if sh("git", "diff", "--cached", "--quiet").returncode == 0:
        print(f"    (nothing to push for {cat})", flush=True)
        return
    sh("git", "commit", "-q", "-m", f"v7: STOR + worksheets for '{cat}' ({note})")
    sh("git", "pull", "--rebase", "-q", "origin", "main")
    r = sh("git", "push", "-q")
    print(f"    {'pushed' if r.returncode == 0 else '!! PUSH FAILED'}: {cat} ({note})", flush=True)
    if r.returncode != 0:
        print((r.stderr or r.stdout)[:400], flush=True)


def reuse_from_panel(bug, cat, target):
    """Copy an existing panel STOR record into the v7 tree, re-keyed to this category."""
    sp = PANEL / bug / f"{bug}_stor.json"
    if not sp.exists():
        return False
    rec = json.loads(sp.read_text())
    rec["category"] = cat
    rec["reused_from"] = "low-interaction-54"
    rec.pop("panel", None)
    target.mkdir(parents=True, exist_ok=True)
    (target / f"{bug}_stor.json").write_text(
        json.dumps(rec, indent=2, ensure_ascii=False), encoding="utf-8")
    return True


def main():
    for ci, cat in enumerate(CATS, 1):
        src_cat = SRC / cat
        dst_cat = V7 / cat
        dst_cat.mkdir(parents=True, exist_ok=True)
        bugs = sorted(p for p in src_cat.iterdir() if p.is_dir())
        print(f"\n== [{ci}/{len(CATS)}] {cat} — {len(bugs)} bugs ==", flush=True)

        gen = reused = skipped = failed = 0
        t0 = time.time()

        for i, bdir in enumerate(bugs, 1):
            bug = bdir.name
            target = dst_cat / bug
            if (target / f"{bug}_stor.json").exists():
                print(f"  [{i}/{len(bugs)}] {bug}: skip (exists)", flush=True)
                skipped += 1
                continue

            # preserve originals (text only) regardless of how STOR arrives
            target.mkdir(parents=True, exist_ok=True)
            for f in bdir.iterdir():
                if f.is_file() and f.suffix.lower() in {".json", ".md"}:
                    if not (target / f.name).exists():
                        shutil.copy2(f, target / f.name)
            att = bdir / "attachments"
            if att.is_dir():
                for f in att.iterdir():
                    if f.is_file() and f.suffix.lower() in v7_stor.TEXT_ATTACH_EXT:
                        d = target / "attachments" / f.name
                        if not d.exists():
                            d.parent.mkdir(exist_ok=True)
                            shutil.copy2(f, d)

            if reuse_from_panel(bug, cat, target):
                print(f"  [{i}/{len(bugs)}] {bug}: reused from panel", flush=True)
                reused += 1
                continue

            md = list(bdir.glob("*.md"))
            if not md:
                print(f"  [{i}/{len(bugs)}] {bug}: SKIP (no .md)", flush=True)
                failed += 1
                continue
            try:
                stor, meta = v7_stor.enhance_stor(md[0].read_text(encoding="utf-8"))
            except v7_stor.CreditsExhausted:
                print(f"\n!! ALL API KEYS OUT OF CREDIT — stopping at {cat}/{bug}", flush=True)
                return 9
            except Exception as e:
                print(f"  [{i}/{len(bugs)}] {bug}: ERROR {type(e).__name__}: {str(e)[:150]}", flush=True)
                failed += 1
                continue

            rec = {"bug_id": bug, "category": cat, "source_md": md[0].name,
                   "source_meta": v7_stor.parse_md_meta(md[0].read_text(encoding="utf-8")),
                   "stor": stor, "call": meta}
            (target / f"{bug}_stor.json").write_text(
                json.dumps(rec, indent=2, ensure_ascii=False), encoding="utf-8")
            with (dst_cat / "_stor_log.jsonl").open("a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            gen += 1
            print(f"  [{i}/{len(bugs)}] {bug}: {len(stor.get('steps', []))} steps  "
                  f"trigger={stor.get('trigger_step')}  web={meta['web_call_count']}  "
                  f"{meta['elapsed_seconds']:.0f}s", flush=True)

        # worksheets
        v7_pdf.V7_ROOT = V7
        v7_pdf.process_category(cat)

        n_stor = len(list(dst_cat.glob("*/*_stor.json")))
        n_pdf = len([p for p in dst_cat.glob("*/*.pdf") if not p.name.endswith("_v5_improved.pdf")])
        print(f"  coverage: stor={n_stor} pdf={n_pdf}  "
              f"(gen={gen} reused={reused} skip={skipped} fail={failed}) "
              f"{time.time()-t0:.0f}s", flush=True)
        if n_stor != n_pdf:
            print(f"  !! COVERAGE GAP in {cat} — not pushing", flush=True)
            continue
        push(cat, f"{n_stor} bugs; gen={gen} reused={reused}")

    print("\n== all four categories done ==", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
