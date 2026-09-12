# v7 — STOR Enhancement Agent

v7 implements the dedicated **STOR (Steps-to-Reproduce) Enhancement Agent** specified in `minecraft_stor_enhancement_agent_setup.md`.

It answers one question and stops:

> Exactly what must be done to reach the point where the bug behavior should be observed?

## What changed from v6

v6 produced a full prose procedure that included `EXPECTED_BEHAVIOR` and `OBSERVED_BUG_BEHAVIOR`. v7 **deliberately does not**. Those belong to separate downstream Observed/Expected enhancers; the STOR agent's output stops immediately before any evaluation of whether the bug occurred.

| | v6 | v7 |
|---|---|---|
| Scope | full procedure incl. Expected + Observed | **S2R only** — both explicitly forbidden |
| Output | free-form markdown | **strict JSON schema** |
| Reasoning effort | medium | **high** |
| Verbosity | default | **high** |
| Web routing | separate router call | `tool_choice="auto"` in one call |
| Web domains | unrestricted | **allowlisted**, `max_tool_calls=4` |
| Provenance | `PRACTICAL_ASSUMPTION` inline in prose | **`source_basis` enum on every step** |
| Trigger / handoff | implicit in prose | explicit `trigger_step` + `handoff_condition` |
| Corpus | `test-bug-panel` | `test-bug-panel-five-year-refresh` (disjoint) |

## Configuration

```python
model            = "gpt-5.6-sol"
reasoning        = {"effort": "high"}
text.verbosity   = "high"
text.format      = json_schema, strict=True, STOR_SCHEMA
tools            = [web_search, search_context_size="medium",
                    allowed_domains=[bugs.mojang.com, minecraft.wiki, minecraft.net]]
tool_choice      = "auto"
max_tool_calls   = 4
store            = False
```

Input is the bug's `.md` — title, metadata, description, and full comment thread.

## Output schema

Every bug produces one strict-JSON object:

| field | meaning |
|---|---|
| `bug_id`, `recommended_version`, `environment` | what to run, and where |
| `preconditions[]` | state that must hold before step 1 |
| `steps[]` | atomic actions (below) |
| `trigger_step` | the numbered step after which observation begins |
| `handoff_condition` | STATE at handoff, never the expected/observed outcome |
| `uncertainties[]` | anything that could make reproduction unreliable |
| `web_verification_used` | model's own declaration |

Each step carries:

```json
{
  "step": 11,
  "action": "Press Enter once to execute the command...",
  "exact_input": "/execute in minecraft:overworld run tp @s -3256.64 20.73 -5797.15 -6134.40 30.36",
  "success_cue": "The chat field closes and the player is teleported to an underground cave...",
  "source_basis": "report"
}
```

### `source_basis` is the research-relevant field

Every step declares where its content came from:

- **`report`** — explicitly stated or directly implied by the Mojira report
- **`verified_external`** — confirmed against an allowlisted source (historical command syntax, old entity IDs, version-specific UI paths)
- **`practical_inference`** — an execution detail that makes a report instruction runnable, but which the report never asserts

This is what lets an enhanced STOR explain *where each added detail came from* — and makes "did the agent invent a requirement?" an auditable question rather than a judgement call. Opening the Creative inventory to obtain a saddle is a legitimate `practical_inference`; claiming the report *requires* Creative mode would be a fabrication.

## Corpus and ordering

Source: `test-bug-panel-five-year-refresh` — 51 categories, 255 bugs, disjoint from the corpus used in v5 (different bug IDs throughout).

Categories are processed in **reverse alphabetical order**, starting at `World generation` and ending at `Accessibility`.

## Contents

```
v7/<Category>/
├── _stor_log.jsonl              one record per bug (STOR + call metadata)
└── <MC-XXX>/
    ├── [Category] - MC-XXX.json   original Jira dump       (preserved)
    ├── [Category] - MC-XXX.md     original report          (preserved)
    ├── attachments/               text attachments only    (preserved)
    ├── MC-XXX_stor.json           STOR + source meta + call metadata
    └── MC-XXX.pdf                 manual-verification worksheet
```

The PDF is a printable worksheet: metadata table, reproduction target, preconditions, numbered steps with `exact_input` in monospace and a colour-coded `source_basis` badge, the trigger step highlighted, handoff condition, uncertainties, and a blank **Manual result** table (version used / reproduced / trigger reached / crash file / notes / tester).

Binary attachments (mp4, png, jpg, gif, mov, mkv, avi, zip, rar, gz, bz2) are excluded — the source corpus is 1.8 GB. Text attachments (`.log`, `.txt`, `.nbt`, `.java`, `.json`, `.mcfunction`, `.yml`, `.properties`) are preserved.

Each `MC-XXX_stor.json` records full call provenance: `response_id`, `web_call_count`, elapsed time, and token usage including reasoning tokens.

## Reproducing

```bash
export OPENAI_API_KEY=<key>
python v7_stor.py "World generation"     # STOR
python v7_pdf.py  "World generation"     # worksheets
```

`v7_stor.py` carries `STOR_ENHANCER_PROMPT` verbatim, so the exact prompt text is versioned alongside the outputs it produced.
