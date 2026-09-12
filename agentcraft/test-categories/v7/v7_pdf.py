"""
v7 PDF generator — one manual-verification worksheet per bug, built from
<bug>_stor.json. Visual language follows the v5 worksheets: title, id/category
line, metadata table, numbered steps, blank MANUAL RESULT table, footer.

Structured for STOR: each step carries exact_input, success_cue and a
source_basis badge; the trigger step is marked; handoff condition and
uncertainties get their own blocks. No Observed/Expected sections (out of scope).

Usage:  python v7_pdf.py "<Category>"
"""
import sys, json, subprocess, html, tempfile, os
from pathlib import Path

V7_ROOT = Path("/Users/nish/Documents/agentcraft/agentcraft/test-categories/v7")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

BASIS_LABEL = {
    "report": ("REPORT", "#1d4ed8", "#dbeafe"),
    "verified_external": ("VERIFIED", "#047857", "#d1fae5"),
    "practical_inference": ("INFERRED", "#b45309", "#fef3c7"),
}


def esc(s):
    return html.escape(str(s) if s is not None else "")


def build_html(rec: dict) -> str:
    stor = rec["stor"]
    meta = rec.get("source_meta", {}) or {}
    call = rec.get("call", {}) or {}
    bug_id = rec["bug_id"]
    category = rec["category"]
    title = meta.get("_title") or meta.get("summary") or bug_id

    def metarow(label, value):
        if not value:
            return ""
        return f'<tr><th>{esc(label)}</th><td>{esc(value)}</td></tr>'

    affected = meta.get("affects versions", "")
    if len(affected) > 300:
        affected = affected[:300].rsplit(";", 1)[0] + " (+more)"

    meta_rows = "".join([
        metarow("Status", " / ".join(x for x in [meta.get("status", ""), meta.get("resolution", "")] if x)),
        metarow("Affected", affected),
        metarow("Fixed in", meta.get("fix versions", "")),
        metarow("Reported", (meta.get("created", "") or "")[:10]),
        metarow("Mojira category", meta.get("mojira categories", "")),
    ])

    # preconditions
    pre = stor.get("preconditions") or []
    pre_html = "".join(f"<li>{esc(p)}</li>" for p in pre) or "<li class='none'>None recorded.</li>"

    # steps
    trigger = stor.get("trigger_step")
    step_html = []
    for s in stor.get("steps", []):
        n = s.get("step")
        is_trig = (n == trigger)
        lbl, fg, bg = BASIS_LABEL.get(s.get("source_basis", ""), ("?", "#475569", "#e2e8f0"))
        exact = s.get("exact_input")
        exact_html = (f'<div class="exact"><span class="k">input</span>'
                      f'<code>{esc(exact)}</code></div>') if exact else ""
        step_html.append(f"""
        <li class="step{' trigger' if is_trig else ''}">
          <div class="stephead">
            <span class="num">{esc(n)}</span>
            <span class="badge" style="color:{fg};background:{bg}">{lbl}</span>
            {'<span class="trigtag">TRIGGER</span>' if is_trig else ''}
          </div>
          <div class="action">{esc(s.get('action',''))}</div>
          {exact_html}
          <div class="cue"><span class="k">success cue</span>{esc(s.get('success_cue',''))}</div>
        </li>""")
    steps_html = "".join(step_html)

    unc = stor.get("uncertainties") or []
    unc_html = ("".join(f"<li>{esc(u)}</li>" for u in unc)
                if unc else "<li class='none'>None recorded.</li>")

    web_note = (f"web verification used ({call.get('web_call_count', 0)} search"
                f"{'es' if call.get('web_call_count', 0) != 1 else ''})"
                if call.get("web_used") else "no web verification")

    # Mojira permalink.
    #
    # The source .md files point at bugs.mojang.com/browse/<id>, but that host
    # now answers every issue path with the same ~750-byte "Mojira Public Bug
    # Tracker" landing shell -- it carries no issue data, so the link is dead
    # for a specific bug. The tracker itself moved to Atlassian cloud, which is
    # what the raw Jira payload agrees with: issues[0].self is
    # https://mojira.atlassian.net/rest/api/3/issue/<numeric-id>.
    mojira_url = f"https://mojira.atlassian.net/browse/{bug_id}"

    # Every affected version the report listed, with the selected one marked.
    # Selection should be the first entry; showing the whole list lets a tester
    # fall back to the next version without reopening the Mojira issue.
    avs = stor.get("affected_versions") or []
    rec = stor.get("recommended_version", "") or ""
    if avs:
        chips = "".join(
            f'<span class="ver{" sel" if (v and v in rec) else ""}">{esc(v)}</span>'
            for v in avs
        )
        affected_html = (f'<div class="lead"><b>Affected versions '
                         f'({len(avs)}):</b><div class="vers">{chips}</div></div>')
    else:
        affected_html = ('<div class="lead"><b>Affected versions:</b> '
                         '<span class="muted">none listed in the report</span></div>')

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{esc(bug_id)}</title>
<style>
  @page {{ size: A4; margin: 16mm 15mm 14mm 15mm; }}
  * {{ box-sizing: border-box; }}
  body {{ margin:0; font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
         color:#1f2937; font-size:10.2pt; line-height:1.45; }}
  h1 {{ font-size:16pt; font-weight:600; margin:0 0 4px; line-height:1.25;
        color:#111827; }}
  .idline {{ font-family:"SF Mono",Menlo,Consolas,monospace; font-size:10pt;
             color:#374151; margin-bottom:14px; }}
  .idline a {{ color:#2563eb; text-decoration:none; border-bottom:1px solid #bfdbfe; }}
  .idline .cat {{ color:#9ca3af; font-family:inherit; margin-left:8px;
                  font-size:8.5pt; letter-spacing:.06em; text-transform:uppercase; }}
  table.meta {{ width:100%; border-collapse:collapse; margin-bottom:18px;
                font-size:9pt; }}
  table.meta th {{ text-align:left; font-weight:500; color:#4b5563; width:112px;
                   background:#f3f4f6; padding:5px 9px; border:1px solid #e5e7eb;
                   vertical-align:top; }}
  table.meta td {{ padding:5px 9px; border:1px solid #e5e7eb; color:#1f2937; }}
  /* Each section opens on its own page. The first one continues the cover page,
     which already carries the title and metadata table. */
  h2 {{ font-size:8.8pt; font-weight:600; letter-spacing:.1em; text-transform:uppercase;
        color:#2563eb; margin:0 0 10px; padding-bottom:3px;
        border-bottom:1px solid #dbeafe;
        break-before:page; page-break-before:always; }}
  h2.first {{ break-before:auto; page-break-before:auto; margin-top:20px; }}
  .lead {{ background:#f8fafc; border-left:3px solid #2563eb; padding:8px 12px;
           margin-bottom:6px; font-size:9.6pt; }}
  .lead b {{ color:#1e40af; font-weight:600; }}
  .vers {{ margin-top:5px; }}
  .ver {{ display:inline-block; font-family:"SF Mono",Menlo,monospace; font-size:8pt;
          background:#eef2f7; border:1px solid #dbe2ea; border-radius:3px;
          padding:1.5px 6px; margin:0 4px 4px 0; color:#475569; }}
  .ver.sel {{ background:#1d4ed8; border-color:#1d4ed8; color:#fff; font-weight:700; }}
  .muted {{ color:#9ca3af; font-style:italic; }}
  ul.plain {{ margin:0; padding-left:18px; }}
  ul.plain li {{ margin-bottom:4px; }}
  li.none {{ color:#9ca3af; font-style:italic; list-style:none; margin-left:-18px; }}
  ol.steps {{ list-style:none; margin:0; padding:0; counter-reset:none; }}
  li.step {{ border:1px solid #e5e7eb; border-radius:4px; padding:8px 11px;
             margin-bottom:7px; break-inside:avoid; page-break-inside:avoid; }}
  li.step.trigger {{ border-color:#f59e0b; background:#fffbeb; border-width:1.5px; }}
  .stephead {{ display:flex; align-items:center; gap:7px; margin-bottom:4px; }}
  .num {{ font-family:"SF Mono",Menlo,monospace; font-weight:700; font-size:10pt;
          color:#111827; min-width:18px; }}
  .badge {{ font-size:6.8pt; font-weight:700; letter-spacing:.07em; padding:1.5px 5px;
            border-radius:2px; }}
  .trigtag {{ font-size:6.8pt; font-weight:700; letter-spacing:.07em; padding:1.5px 5px;
              border-radius:2px; color:#92400e; background:#fde68a; }}
  .action {{ margin-bottom:4px; }}
  .exact {{ margin:4px 0; }}
  .exact code {{ font-family:"SF Mono",Menlo,Consolas,monospace; font-size:8.8pt;
                 background:#f1f5f9; border:1px solid #e2e8f0; border-radius:3px;
                 padding:2px 6px; display:inline-block; word-break:break-all;
                 color:#0f172a; }}
  .cue {{ font-size:9pt; color:#4b5563; }}
  .k {{ display:inline-block; font-size:6.8pt; font-weight:700; letter-spacing:.08em;
        text-transform:uppercase; color:#9ca3af; margin-right:6px; }}
  .keep {{ break-inside:avoid; page-break-inside:avoid; }}
  table.result {{ width:100%; border-collapse:collapse; margin-top:6px; font-size:9pt; }}
  table.result th {{ text-align:left; font-weight:500; color:#4b5563; width:132px;
                     background:#f9fafb; padding:9px; border:1px solid #e5e7eb; }}
  table.result td {{ padding:9px; border:1px solid #e5e7eb; height:26px;
                     color:#9ca3af; }}
  .foot {{ margin-top:16px; padding-top:8px; border-top:1px solid #e5e7eb;
           font-size:7.8pt; color:#9ca3af; display:flex;
           justify-content:space-between; }}
  .foot a {{ color:#6b7280; text-decoration:none; }}
</style></head><body>

<h1>{esc(title)}</h1>
<div class="idline"><a href="{mojira_url}">{esc(bug_id)}</a><span class="cat">{esc(category)}</span></div>

<table class="meta">{meta_rows}</table>

<h2 class="first">Reproduction target</h2>
<div class="lead"><b>Use version:</b> {esc(stor.get('recommended_version',''))}</div>
{affected_html}
<div class="lead"><b>Environment:</b> {esc(stor.get('environment',''))}</div>

<h2>Preconditions</h2>
<ul class="plain">{pre_html}</ul>

<h2>Steps to reproduce</h2>
<ol class="steps">{steps_html}</ol>

<h2>Handoff to observation</h2>
<div class="lead">{esc(stor.get('handoff_condition',''))}</div>

<h2>Uncertainties</h2>
<ul class="plain">{unc_html}</ul>

<div class="keep">
<h2>Manual result</h2>
<table class="result">
  <tr><th>Version used</th><td></td></tr>
  <tr><th>Reproduced?</th><td>YES / NO / PARTIAL</td></tr>
  <tr><th>Trigger reached?</th><td>YES / NO</td></tr>
  <tr><th>Crash file</th><td></td></tr>
  <tr><th>Notes</th><td></td></tr>
  <tr><th>Tested by / date</th><td></td></tr>
</table>
</div>

<div class="foot">
  <span>{esc(bug_id)} &nbsp;|&nbsp; {esc(category)} &nbsp;|&nbsp; v7 STOR &nbsp;|&nbsp; {esc(web_note)}</span>
  <a href="{mojira_url}">mojira.atlassian.net/browse/{esc(bug_id)}</a>
</div>

</body></html>"""


def render(rec_path: Path) -> bool:
    rec = json.loads(rec_path.read_text(encoding="utf-8"))
    out_pdf = rec_path.parent / f"{rec['bug_id']}.pdf"
    html_text = build_html(rec)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as tf:
        tf.write(html_text)
        tmp = tf.name
    try:
        subprocess.run(
            [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
             "--hide-scrollbars", "--no-pdf-header-footer",
             f"--print-to-pdf={out_pdf}", f"file://{tmp}"],
            capture_output=True, timeout=120,
        )
        return out_pdf.exists() and out_pdf.stat().st_size > 1000
    finally:
        os.unlink(tmp)


def process_category(category: str):
    cat_dir = V7_ROOT / category
    recs = sorted(cat_dir.glob("*/*_stor.json"))
    ok = fail = 0
    for r in recs:
        if render(r):
            ok += 1
        else:
            fail += 1
            print(f"  PDF FAILED: {r.parent.name}")
    print(f"[{category}] pdf ok={ok} failed={fail}")
    return ok, fail


if __name__ == "__main__":
    process_category(sys.argv[1] if len(sys.argv) > 1 else "World generation")
