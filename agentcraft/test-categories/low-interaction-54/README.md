# low-interaction-54 — manual test panel

54 Minecraft bugs selected for **low interaction cost**: each is reachable with a short,
mostly deterministic setup — a command or two, a settings toggle, or inspection of a file
outside the running game — rather than long survival play or rare world state.

This folder is self-contained: every bug carries its original report, its enhanced
Steps-to-Reproduce, and a printable verification worksheet. Nothing here references the
wider corpus.

## Layout

```
low-interaction-54/
├── selected-low-interaction-bugs.csv   the provided panel definition (authoritative)
├── low_interaction_54_index.csv        enriched index — one row per bug, STOR results
├── _stor_log.jsonl                     one record per generated bug
└── <MC-XXXXX>/                         one folder per bug
    ├── [Category] - MC-XXXXX.json      original Jira dump
    ├── [Category] - MC-XXXXX.md        rendered report + comment thread
    ├── attachments/                    text attachments only
    ├── MC-XXXXX_stor.json              v7 STOR record
    ├── MC-XXXXX.pdf                    verification worksheet
    ├── MC-XXXXX_v5_improved.json       v5 baseline, where one exists
    └── MC-XXXXX_v5_improved.pdf
```

Binary attachments (png, mp4, zip, mkv, …) are excluded; the source panel carries 132 png
and 17 mp4 files that add nothing to reproduction and inflate the repo.

## Reproduction method

The panel splits three ways, per the `reproduction_method` column:

| method | bugs | what it takes |
|---|---|---|
| `commands` | 29 | run one or more commands in-game |
| `settings/UI` | 19 | toggle an option or navigate a screen |
| `outside-game inspection` | 6 | inspect a log, save file, or resource outside the client |

## What the STOR gives you

Each `MC-XXXXX_stor.json` answers exactly one question — *what must be done to reach the
point where the bug should be observed* — and stops there. It deliberately contains no
Expected or Observed Behavior; deciding whether the bug occurred is the tester's job.

Every step declares where it came from via `source_basis`:

- `report` — stated or directly implied by the Mojira report
- `verified_external` — confirmed against minecraft.wiki / minecraft.net / bugs.mojang.com
- `practical_inference` — an execution detail that makes an instruction runnable, which
  the report never asserts

That makes "did the agent invent a requirement?" an auditable question rather than a
judgement call.

`recommended_version` is always the **first** entry of `affected_versions` — never a fix
version.

## The worksheet PDF

One page per section: metadata, reproduction target, preconditions, numbered steps with
`exact_input` in monospace and a colour-coded `source_basis` badge, the trigger step
highlighted, handoff condition, uncertainties, and a blank **Manual result** table
(version used / reproduced / trigger reached / crash file / notes / tester).

The bug ID links to `https://bugs.mojang.com/browse/MC/issues/<KEY>`.

## Index columns

`low_interaction_54_index.csv` joins the panel definition to the STOR output:

`bug_id`, `category`, `url`, `reproduction_method`, `what_to_do`, `other_constraints`,
`has_stor`, `has_pdf`, `has_v5_baseline`, `recommended_version`, `affected_versions`,
`step_count`, `trigger_step`, `precondition_count`, `uncertainty_count`, `web_verified`,
`web_calls`, `elapsed_seconds`, `attachment_count`, `folder`

Sorted by `reproduction_method`, then category — so a testing session can be picked up one
method at a time.

## Generation

```bash
python lowint54_build.py    # assemble folders from source corpus + existing artifacts
python lowint54_run.py      # STOR for anything missing, then worksheets
python lowint54_index.py    # rebuild the index CSV
```

`lowint54_run.py` imports `v7_stor.py` and `v7_pdf.py` from `../v7/`, so prompt, schema,
model (`gpt-5.6-sol`, reasoning effort `high`) and worksheet layout are identical to v7 —
these records are directly comparable with the v7 corpus.
