"""Rebuild v7_bug_index.csv by walking the v7 tree itself.

The earlier builder walked the source corpus, which was correct while v7 mirrored it
exactly. Networking now diverges (its five bugs were replaced from a separate panel),
so the tree is the only accurate source of truth.
"""
import csv
import json
import sys
from pathlib import Path

V7 = Path("/Users/nish/Documents/agentcraft/agentcraft/test-categories/v7")
OUT = V7 / "v7_bug_index.csv"


def mojira_url(bug_id):
    project = bug_id.split("-")[0] if "-" in bug_id else "MC"
    return f"https://bugs.mojang.com/browse/{project}/issues/{bug_id}"


def raw_fields(bug_dir, bug_id):
    for f in bug_dir.glob("*.json"):
        if f.name.endswith(("_stor.json", "_v5_improved.json")):
            continue
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        if isinstance(d, dict) and d.get("issues"):
            return d["issues"][0].get("fields", {}) or {}
    return {}


def comment_count(bug_dir):
    import re
    for f in bug_dir.glob("*.md"):
        m = re.search(r"^##\s+Comments\s+\((\d+)\)", f.read_text(errors="replace"), re.M)
        if m:
            return int(m.group(1))
    return 0


def main():
    rows = []
    for bd in sorted(V7.glob("*/MC-*")):
        if not bd.is_dir():
            continue
        cat, bug = bd.parent.name, bd.name
        sp = bd / f"{bug}_stor.json"
        rec = json.loads(sp.read_text()) if sp.exists() else {}
        s = rec.get("stor", {}) or {}
        call = rec.get("call", {}) or {}
        fl = raw_fields(bd, bug)

        def names(k):
            return "; ".join(v.get("name", "") for v in (fl.get(k) or []) if isinstance(v, dict))

        affected = names("versions")
        rows.append({
            "bug_id": bug,
            "category": cat,
            "url": mojira_url(bug),
            "summary": (fl.get("summary") or "").replace("\n", " ").strip(),
            "affected_versions": affected,
            "first_affected_version": affected.split(";")[0].strip() if affected else "",
            "fix_versions": names("fixVersions"),
            "status": (fl.get("status") or {}).get("name", ""),
            "resolution": (fl.get("resolution") or {}).get("name", ""),
            "created": (fl.get("created") or "")[:10],
            "watch_count": (fl.get("watches") or {}).get("watchCount", ""),
            "attachment_count": len(fl.get("attachment") or []),
            "comment_count": comment_count(bd),
            "state": "v7_stor" if s else "raw_only",
            "stor_step_count": len(s.get("steps", []) or []) if s else "",
            "trigger_step": s.get("trigger_step", ""),
            "recommended_version": s.get("recommended_version", ""),
            "web_calls": call.get("web_call_count", ""),
            "source_category": rec.get("source_category", ""),
            "repo_path": f"agentcraft/test-categories/v7/{cat}/{bug}",
        })

    rows.sort(key=lambda r: (r["category"], r["bug_id"]))
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    import collections
    c = collections.Counter(r["state"] for r in rows)
    print(f"{OUT}  ({len(rows)} rows)")
    print(f"  states: {dict(c)}")
    print(f"  categories: {len({r['category'] for r in rows})}")
    checked = [r for r in rows if r["affected_versions"] and r["recommended_version"]]
    first = sum(1 for r in checked
                if r["recommended_version"].strip() == r["affected_versions"].split(";")[0].strip())
    print(f"  first-affected-version: {first}/{len(checked)}")
    for r in checked:
        if r["recommended_version"].strip() != r["affected_versions"].split(";")[0].strip():
            print(f"    deviation: {r['category']}/{r['bug_id']} -> {r['recommended_version']} "
                  f"(first: {r['affected_versions'].split(';')[0].strip()})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
