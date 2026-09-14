"""Generate v7 STOR + worksheet for every low-interaction-54 bug that lacks one.

Reuses v7_stor.py's prompt, schema, key rotation and SIGALRM deadline verbatim by
importing it, so this panel's records are directly comparable with v7's. Roots are
patched because the panel is flat (one folder per bug) rather than category-nested.

Resumable: a bug with <id>_stor.json is skipped. Writes after every bug, so an abort
loses at most the one in flight.
"""
import csv
import json
import sys
import time
from pathlib import Path

SCRATCH = Path("/private/tmp/claude-501/-Users-nish-Documents-minecraft-agents/27b27372-6b02-42e0-bb38-7d997ff1ffaa/scratchpad")
sys.path.insert(0, str(SCRATCH))

import v7_stor
import v7_pdf

PANEL = Path("/Users/nish/Documents/agentcraft/agentcraft/test-categories/low-interaction-54")
LOG = PANEL / "_stor_log.jsonl"


def main():
    rows = list(csv.DictReader((PANEL / "selected-low-interaction-bugs.csv").open()))
    todo = [r for r in rows if not (PANEL / r["bug_id"] / f"{r['bug_id']}_stor.json").exists()]
    print(f"{len(rows)} bugs in panel, {len(todo)} need STOR", flush=True)

    ok = failed = 0
    t_start = time.time()
    for i, r in enumerate(todo, 1):
        bug, cat = r["bug_id"], r["category"]
        target = PANEL / bug
        md = [f for f in target.glob("*.md")]
        if not md:
            print(f"  [{i}/{len(todo)}] {bug}: SKIP (no .md)", flush=True)
            failed += 1
            continue

        try:
            stor, meta = v7_stor.enhance_stor(md[0].read_text(encoding="utf-8"))
        except v7_stor.CreditsExhausted:
            print(f"\n!! ALL API KEYS OUT OF CREDIT — stopping at {bug}", flush=True)
            return 9
        except Exception as e:
            print(f"  [{i}/{len(todo)}] {bug}: ERROR {type(e).__name__}: {str(e)[:160]}", flush=True)
            failed += 1
            continue

        record = {
            "bug_id": bug,
            "category": cat,
            "panel": "low-interaction-54",
            "reproduction_method": r.get("reproduction_method", ""),
            "source_md": md[0].name,
            "source_meta": v7_stor.parse_md_meta(md[0].read_text(encoding="utf-8")),
            "stor": stor,
            "call": meta,
        }
        (target / f"{bug}_stor.json").write_text(
            json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
        with LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

        ok += 1
        el = time.time() - t_start
        eta = (el / i) * (len(todo) - i)
        print(f"  [{i}/{len(todo)}] {bug} ({cat}): {len(stor.get('steps', []))} steps  "
              f"trigger={stor.get('trigger_step')}  web={meta['web_call_count']}  "
              f"{meta['elapsed_seconds']:.0f}s   eta {eta/60:.0f}m", flush=True)

    print(f"\nSTOR done: ok={ok} failed={failed}", flush=True)

    # Worksheets. v7_pdf globs <root>/<category>/*/*_stor.json, so point it one level up.
    v7_pdf.V7_ROOT = PANEL.parent
    v7_pdf.process_category(PANEL.name)

    n_stor = len(list(PANEL.glob("*/*_stor.json")))
    n_pdf = len([p for p in PANEL.glob("*/*.pdf") if not p.name.endswith("_v5_improved.pdf")])
    print(f"coverage: stor={n_stor} pdf={n_pdf}")
    return 0 if n_stor == n_pdf else 1


if __name__ == "__main__":
    sys.exit(main())
