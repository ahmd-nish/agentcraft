# v6 — Executable S2R via routed web verification

v6 changes both the **output target** and the **generation architecture** relative to v1–v5.

Where earlier versions produced four improved prose sections (S2R / OB / EB / Environment) aimed at a human triager, v6 produces a **single executable reproduction procedure** aimed at a downstream LLM agent that must drive Minecraft and verify the defect. The output is written for machine execution, not human reading.

## Architecture

Two model calls per bug, both on `gpt-5.6-sol` via the OpenAI **Responses API**.

```
Mojira report (.md)
      |
      v
  [1] ROUTER            gpt-5.6-sol, reasoning effort = low
      |                 returns exactly NEED_WEB or NO_WEB
      |
      +--- NO_WEB ----> clarifier runs with NO tools
      |
      +--- NEED_WEB --> clarifier runs WITH web_search (tool_choice=auto)
      |
      v
  [2] CLARIFIER         gpt-5.6-sol, reasoning effort = medium
      |
      v
  executable reproduction procedure
```

### Why the router is a separate call

Keeping routing as its own model call — rather than letting the clarifier decide for itself whether to browse — buys three things that matter for the research:

- **Web usage becomes explicit and measurable.** Every decision is logged with its own `response_id`.
- **The clarifier cannot browse unnecessarily.** It only receives the `web_search` tool when the router approved it, so "did not browse" is enforced rather than hoped for.
- **Routing decisions are auditable.** `NEED_WEB` / `NO_WEB` is recorded per bug alongside whether the clarifier *actually* invoked search when it had the option.

The router returns `NEED_WEB` when the reproduction depends on version-specific command syntax not settled by the report, when a command / NBT / datapack / advancement behaviour in the affected version is uncertain, when a step depends on information absent from the report, or when there is meaningful risk of applying modern Minecraft syntax to an older affected version. Unparseable router output falls back to `NEED_WEB` (conservative).

### What the clarifier is instructed to do

The clarifier converts a human-written Mojira report into the **smallest deterministic action sequence** that lets an execution agent reproduce and verify the defect. Key constraints:

- **Grounding** — preserve the affected version, and preserve commands, coordinates, entity/item names, NBT, and numeric values exactly as supplied. Never silently modernize historical syntax. Any recommendation not stated in the report must be tagged `PRACTICAL_ASSUMPTION`.
- **Executability** — assume the execution agent understands no implicit human instruction. "Enter the Nether" must expand into portal construction, ignition, entry, dimension-transition wait, and environment verification. "Use the item" must specify item, hand, input, click-vs-hold, duration, and release condition.
- **Minimality** — reproduce one deterministic variant, not every variant a long historical report mentions.
- **Bug verification** — the hardest part. Setup behaviour must not be confused with buggy behaviour. If an entity moves correctly but snaps instead of interpolating, movement is not the bug; absence of interpolation is.

Output follows a fixed schema: `BUG_ID`, `AFFECTED_VERSION`, `BUG_BEHAVIOR`, `PRECONDITIONS`, `SETUP`, `REPRODUCTION_STEPS` (with `VERIFY` blocks after significant actions), `EXPECTED_BEHAVIOR`, `OBSERVED_BUG_BEHAVIOR`, `SUCCESS_CONDITION`, and `FAILURE_OR_AMBIGUITY` when the report does not support reliable reproduction.

## Run: Commands category

| | value |
|---|---|
| Source | `test-bug-panel/Commands` (same corpus as v5) |
| Bugs | 5 / 5 completed, 0 failed |
| Router model | `gpt-5.6-sol`, reasoning effort `low` |
| Clarifier model | `gpt-5.6-sol`, reasoning effort `medium` |
| Total wall clock | 329 s (~5.5 min) |
| Per bug | avg 66 s (min 49 s, max 109 s) |
| Output length | avg 592 words (min 419, max 821) |

### Routing outcomes

| Bug | Router | Web actually used | Words | Time |
|---|---|---|--:|--:|
| MC-117574 | `NO_WEB` | no | 419 | 49 s |
| MC-121997 | `NO_WEB` | no | 821 | 72 s |
| MC-122717 | `NO_WEB` | no | 521 | 49 s |
| MC-259915 | `NEED_WEB` | **yes** | 601 | 109 s |
| MC-274047 | `NO_WEB` | no | 598 | 49 s |

**1 of 5 bugs triggered web verification.** The router discriminated rather than defaulting to browse — worth noting, since a router that always returns `NEED_WEB` would make the whole two-call design pointless.

### The web-verified case is the clearest evidence the design works

MC-259915 reports that item displays do not interpolate position when teleported. The comment thread spans 13 comments across 2023 and ends with users noting the issue "seems fixed" via a `teleport_duration` option. The affected version, however, is 1.20.1.

The router flagged this as `NEED_WEB` (version-specific behaviour uncertainty). The clarifier searched, established from minecraft.net that `teleport_duration` was introduced in snapshot **23w31a**, and then wrote into the preconditions:

> Do not add a `teleport_duration` tag. That control was introduced in snapshot 23w31a and is not part of the affected 1.20.1 behavior. ([minecraft.net](https://www.minecraft.net/nb-no/article/minecraft-snapshot-23w31a))

That is grounding rule 3 firing exactly as intended: external information was used to *prevent* modernizing the reproduction, not to update it. It also added a stationary pig as a living-entity interpolation comparator, so the execution agent can distinguish "the display snapped" from "the display did not move" — the bug-verification rule working.

## Contents

```
v6/Commands/
├── _research_log.jsonl          one JSON object per bug: routing + generation metadata
└── <MC-XXX>/
    ├── [Commands] - MC-XXX.json   original Jira API dump      (preserved)
    ├── [Commands] - MC-XXX.md     original readable report    (preserved)
    ├── attachments/               text attachments only       (preserved)
    ├── MC-XXX_s2r.md              clarifier output
    └── MC-XXX_s2r.json            clarifier output + full metadata
```

Binary attachments (mp4, png, jpg, gif, mov, mkv, avi, zip, rar, gz, bz2) are excluded to keep the repository clonable; the source corpus is 2.2 GB, this mirror is 348 KB. Text attachments (`.log`, `.txt`, `.nbt`, `.java`, `.json`) are preserved — MC-274047 keeps its four crash-log attachments.

Each `_s2r.json` carries full provenance:

```json
{
  "routing":    { "need_web": true, "router_output": "NEED_WEB", "router_response_id": "resp_..." },
  "generation": { "model": "gpt-5.6-sol", "reasoning_effort": "medium",
                  "web_available": true, "web_actually_used": true, "response_id": "resp_..." },
  "answer": "BUG_ID: ...",
  "elapsed_seconds": 109.4
}
```

`web_available` versus `web_actually_used` are recorded separately: the router can grant the tool and the clarifier can still decline to call it. Both numbers are needed to characterize the system honestly.

## Relationship to earlier versions

| | v1–v4 | v5 | v6 |
|---|---|---|---|
| Corpus | 60 evaluation bugs | 51 categories, 255 bugs | Commands, 5 bugs |
| Output | 4 prose sections | 4 prose sections | 1 executable procedure |
| Audience | human triager | human triager | LLM execution agent |
| Evidence | RAG + community posts + JIRA comments | RAG | routed web search |
| Model | gpt-4o-mini / Qwen 2.5-32B / gpt-oss-120b | gpt-5.6-luna | gpt-5.6-sol |

v6 is not a drop-in successor to v5 — it answers a different question. v5 asks "can we make this report better for a human?"; v6 asks "can we make this report executable by a machine?"

## Reproducing

```bash
export OPENAI_API_KEY=<key>
python v6_clarifier.py "Commands"
```

Script: `v6_clarifier.py` (router instructions, clarifier instructions, batch runner). Both `ROUTER_INSTRUCTIONS` and `CLARIFIER_INSTRUCTIONS` are kept verbatim in the script so the exact prompt text is versioned alongside the outputs.
