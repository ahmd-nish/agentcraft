"""Emit low_interaction_54_index.csv: the source panel CSV enriched with STOR results.

Keeps the original selected-low-interaction-bugs.csv untouched alongside it, so the
provided file stays authoritative for panel membership.
"""
import csv
import json
import sys
from pathlib import Path

PANEL = Path("/Users/nish/Documents/agentcraft/agentcraft/test-categories/low-interaction-54")
OUT = PANEL / "low_interaction_54_index.csv"


def mojira_url(bug_id: str) -> str:
    project = bug_id.split("-")[0] if "-" in bug_id else "MC"
    return f"https://bugs.mojang.com/browse/{project}/issues/{bug_id}"


def main():
    rows = list(csv.DictReader((PANEL / "selected-low-interaction-bugs.csv").open()))
    out = []
    for r in rows:
        bug = r["bug_id"]
        d = PANEL / bug
        rec = {}
        sp = d / f"{bug}_stor.json"
        if sp.exists():
            try:
                rec = json.loads(sp.read_text())
            except Exception:
                rec = {}
        s = rec.get("stor", {}) or {}
        call = rec.get("call", {}) or {}
        avs = s.get("affected_versions") or []

        out.append({
            "bug_id": bug,
            "category": r["category"],
            "url": mojira_url(bug),
            "reproduction_method": r.get("reproduction_method", ""),
            "what_to_do": r.get("what_to_do", ""),
            "other_constraints": r.get("other_constraints", ""),
            "has_stor": "yes" if s else "no",
            "has_pdf": "yes" if (d / f"{bug}.pdf").exists() else "no",
            "has_v5_baseline": "yes" if (d / f"{bug}_v5_improved.json").exists() else "no",
            "recommended_version": s.get("recommended_version", ""),
            "affected_versions": "; ".join(avs),
            "step_count": len(s.get("steps", []) or []) if s else "",
            "trigger_step": s.get("trigger_step", ""),
            "precondition_count": len(s.get("preconditions", []) or []) if s else "",
            "uncertainty_count": len(s.get("uncertainties", []) or []) if s else "",
            "web_verified": s.get("web_verification_used", ""),
            "web_calls": call.get("web_call_count", ""),
            "elapsed_seconds": round(call.get("elapsed_seconds", 0), 1) if call else "",
            "attachment_count": r.get("attachment_count", ""),
            "folder": f"agentcraft/test-categories/low-interaction-54/{bug}",
        })

    out.sort(key=lambda x: (x["reproduction_method"], x["category"], x["bug_id"]))
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)

    n_stor = sum(1 for o in out if o["has_stor"] == "yes")
    n_pdf = sum(1 for o in out if o["has_pdf"] == "yes")
    print(f"{OUT}  ({len(out)} rows)")
    print(f"  stor={n_stor}/{len(out)}  pdf={n_pdf}/{len(out)}")
    # first-affected-version discipline: recommended must be avs[0]
    checked = [o for o in out if o["affected_versions"] and o["recommended_version"]]
    firsts = sum(1 for o in checked
                 if o["recommended_version"].strip() == o["affected_versions"].split(";")[0].strip())
    print(f"  picks first affected version: {firsts}/{len(checked)}")
    bad = [o["bug_id"] for o in checked
           if o["recommended_version"].strip() != o["affected_versions"].split(";")[0].strip()]
    if bad:
        print(f"  !! not-first: {bad}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
