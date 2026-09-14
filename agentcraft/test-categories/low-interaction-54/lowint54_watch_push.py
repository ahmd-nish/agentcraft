"""Push low-interaction-54 results to GitHub in batches of 3 while generation runs.

Runs alongside lowint54_run.py rather than inside it, so the generator is never
interrupted. Every poll it looks for bugs that have a STOR record but no worksheet,
renders those, and once 3+ complete bugs are unstaged it commits and pushes.

Safety: a bug is only eligible once its <id>_stor.json parses as valid JSON and its
worksheet exists. That avoids staging a file the generator is midway through writing.
Exits when the generator process is gone and nothing is left pending.
"""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

SCRATCH = Path("/private/tmp/claude-501/-Users-nish-Documents-minecraft-agents/27b27372-6b02-42e0-bb38-7d997ff1ffaa/scratchpad")
sys.path.insert(0, str(SCRATCH))
import v7_pdf

REPO = Path("/Users/nish/Documents/agentcraft")
PANEL = REPO / "agentcraft/test-categories/low-interaction-54"
REL = "agentcraft/test-categories/low-interaction-54"
BATCH = 3
GEN_PID = int(sys.argv[1]) if len(sys.argv) > 1 else 0

v7_pdf.V7_ROOT = PANEL.parent


def sh(*args, **kw):
    return subprocess.run(args, cwd=REPO, capture_output=True, text=True, **kw)


def gen_alive():
    if not GEN_PID:
        return False
    try:
        os.kill(GEN_PID, 0)
        return True
    except OSError:
        return False


def complete_bugs():
    """Bugs with a parseable STOR record and a rendered worksheet."""
    out = []
    for sp in sorted(PANEL.glob("*/*_stor.json")):
        bug = sp.parent.name
        try:
            json.loads(sp.read_text())
        except Exception:
            continue                      # still being written
        if (sp.parent / f"{bug}.pdf").exists():
            out.append(bug)
    return out


def render_missing():
    made = 0
    for sp in sorted(PANEL.glob("*/*_stor.json")):
        bug = sp.parent.name
        if (sp.parent / f"{bug}.pdf").exists():
            continue
        try:
            json.loads(sp.read_text())
        except Exception:
            continue
        try:
            if v7_pdf.render(sp):
                made += 1
        except Exception as e:
            print(f"  pdf failed {bug}: {type(e).__name__}: {e}", flush=True)
    return made


def untracked_or_modified(bugs):
    """Subset of bugs git considers new/changed."""
    r = sh("git", "status", "--porcelain", "--", REL)
    dirty = r.stdout
    return [b for b in bugs if f"{REL}/{b}/" in dirty]


def push(bugs):
    sh("git", "add", "--", *[f"{REL}/{b}" for b in bugs])
    if sh("git", "diff", "--cached", "--quiet").returncode == 0:
        return False
    msg = (f"low-interaction-54: STOR + worksheet for {len(bugs)} bugs "
           f"({', '.join(bugs[:6])}{'...' if len(bugs) > 6 else ''})")
    sh("git", "commit", "-q", "-m", msg)
    sh("git", "pull", "--rebase", "-q", "origin", "main")
    r = sh("git", "push", "-q")
    ok = r.returncode == 0
    print(f"{'pushed' if ok else '!! PUSH FAILED'}: {len(bugs)} bugs -> {', '.join(bugs)}",
          flush=True)
    if not ok:
        print((r.stderr or r.stdout)[:400], flush=True)
    return ok


def main():
    print(f"watcher up: batch={BATCH}, generator pid={GEN_PID or 'n/a'}", flush=True)
    pushed_total = 0
    while True:
        render_missing()
        pending = untracked_or_modified(complete_bugs())
        alive = gen_alive()

        if len(pending) >= BATCH or (pending and not alive):
            for i in range(0, len(pending), BATCH):
                chunk = pending[i:i + BATCH]
                # Only hold back a short final chunk while more are still coming.
                if len(chunk) < BATCH and alive:
                    break
                if push(chunk):
                    pushed_total += len(chunk)

        if not alive and not untracked_or_modified(complete_bugs()):
            print(f"generator finished; watcher done. pushed {pushed_total} bugs.", flush=True)
            return 0
        time.sleep(20)


if __name__ == "__main__":
    sys.exit(main())
