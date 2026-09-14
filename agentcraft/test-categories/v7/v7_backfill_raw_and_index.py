"""Mirror every remaining v7-corpus bug into v7/<Category>/<MC-ID>/ as-is, then
emit a single index CSV covering all 255 bugs.

"As-is" means the original Jira dump, the rendered .md, and text attachments --
no enhancement, since v7 STOR needs API credit. Nothing existing is overwritten,
and no *_stor.json is created, so the v7 resume check still picks these up.

Canonical Mojira URL form: https://bugs.mojang.com/browse/<PROJECT>/issues/<KEY>
"""
import csv
import json
import shutil
import sys
from pathlib import Path

SRC7 = Path("/Users/nish/Documents/Research - Minecraft/data_collection/test-bug-panel-five-year-refresh")
V7 = Path("/Users/nish/Documents/agentcraft/agentcraft/test-categories/v7")
CSV_OUT = V7 / "v7_bug_index.csv"

TEXT_ATTACH_EXT = {".log", ".txt", ".nbt", ".java", ".json", ".mcfunction", ".yml", ".properties"}


def mojira_url(bug_id: str) -> str:
    project = bug_id.split("-")[0] if "-" in bug_id else "MC"
    return f"https://bugs.mojang.com/browse/{project}/issues/{bug_id}"


def load_issue(bug_dir: Path):
    """The raw Jira dump, or None. Files are named '[Category] - MC-X.json'."""
    for f in bug_dir.glob("*.json"):
        if f.name.endswith("_stor.json") or f.name.endswith("_v5_improved.json"):
            continue
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        if isinstance(d, dict) and d.get("issues"):
            return d["issues"][0]
    return None


def comment_count(bug_dir: Path) -> int:
    """Parsed from the rendered .md's '## Comments (N)' heading."""
    import re
    for f in bug_dir.glob("*.md"):
        m = re.search(r"^##\s+Comments\s+\((\d+)\)", f.read_text(errors="replace"), re.M)
        if m:
            return int(m.group(1))
    return 0


def copy_new(src: Path, dst: Path) -> int:
    if dst.exists():
        return 0
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return 1


def main():
    src_bugs = sorted(
        (d for d in SRC7.glob("*/*") if d.is_dir() and d.name.startswith("MC-")),
        key=lambda p: (p.parent.name, p.name),
    )
    print(f"v7 corpus: {len(src_bugs)} bugs in {len(set(d.parent.name for d in src_bugs))} categories")

    mirrored, new_cats = 0, set()

    for sdir in src_bugs:
        cat, bug_id = sdir.parent.name, sdir.name
        target = V7 / cat / bug_id
        existed = target.exists()

        n = 0
        for f in sdir.iterdir():
            if f.is_file() and f.suffix.lower() in {".json", ".md"}:
                n += copy_new(f, target / f.name)
        att = sdir / "attachments"
        if att.is_dir():
            for f in att.iterdir():
                if f.is_file() and f.suffix.lower() in TEXT_ATTACH_EXT:
                    n += copy_new(f, target / "attachments" / f.name)
        if n:
            mirrored += 1
            if not existed:
                new_cats.add(cat)

    # ---- index ----
    rows = []
    for sdir in src_bugs:
        cat, bug_id = sdir.parent.name, sdir.name
        target = V7 / cat / bug_id
        iss = load_issue(sdir) or {}
        fl = iss.get("fields", {}) or {}

        has_stor = (target / f"{bug_id}_stor.json").exists()
        has_v5 = (target / f"{bug_id}_v5_improved.json").exists()
        if has_stor:
            state = "v7_stor"
        elif has_v5:
            state = "v5_baseline"
        else:
            state = "raw_only"

        stor_steps = trigger = ""
        rec_version = ""
        if has_stor:
            try:
                rec = json.loads((target / f"{bug_id}_stor.json").read_text())
                s = rec.get("stor", rec)
                stor_steps = len(s.get("steps", []) or [])
                trigger = s.get("trigger_step", "")
                rec_version = s.get("recommended_version", "")
            except Exception:
                pass

        def names(key):
            return "; ".join(v.get("name", "") for v in (fl.get(key) or []) if isinstance(v, dict))

        affected = names("versions")
        rows.append({
            "bug_id": bug_id,
            "category": cat,
            "url": mojira_url(bug_id),
            "summary": (fl.get("summary") or "").replace("\n", " ").strip(),
            "affected_versions": affected,
            "first_affected_version": affected.split(";")[0].strip() if affected else "",
            "fix_versions": names("fixVersions"),
            "status": ((fl.get("status") or {}).get("name") or ""),
            "resolution": ((fl.get("resolution") or {}).get("name") or ""),
            "created": (fl.get("created") or "")[:10],
            "watch_count": ((fl.get("watches") or {}).get("watchCount") or ""),
            "attachment_count": len(fl.get("attachment") or []),
            # The Jira dump omits the comment field entirely; the rendered .md
            # carries the thread, headed "## Comments (N)".
            "comment_count": comment_count(sdir),
            "state": state,
            "stor_step_count": stor_steps,
            "trigger_step": trigger,
            "recommended_version": rec_version,
            "repo_path": str(target.relative_to(V7.parent.parent.parent)),
        })

    rows.sort(key=lambda r: (r["category"], r["bug_id"]))
    with CSV_OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    from collections import Counter
    c = Counter(r["state"] for r in rows)
    print(f"\nmirrored (new files) : {mirrored} bugs")
    print(f"new category folders : {len(new_cats)}")
    print(f"\nindex -> {CSV_OUT}  ({len(rows)} rows)")
    for k in ("v7_stor", "v5_baseline", "raw_only"):
        print(f"  {k:<14} {c.get(k, 0)}")
    missing = [r["bug_id"] for r in rows if not r["summary"]]
    if missing:
        print(f"  !! {len(missing)} rows without summary: {missing[:5]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
