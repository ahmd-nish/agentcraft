# v4 — 60 enhanced Minecraft bug reports with community posts + JIRA comments

Same 60 reports, same pipeline, same models (GPT-4o-mini + Qwen 2.5-32B) as [v3](../v3). The single change: on top of v3's community-post block, v4 also injects the Mojang JIRA comment thread already attached to each specific bug.

## Why v4 exists

The v3 experiment (community posts) came back near-neutral in the manual eval — see [`../v3/EVAL_v2_vs_v3.md`](../v3/EVAL_v2_vs_v3.md). Root cause: cosine-matched community posts share vocabulary with the bug but rarely carry causal detail. **JIRA comments are directly attached to each specific bug**, so they carry much higher signal — reproduction confirmations, version-specific regressions, code-level speculation, workarounds, and cross-references to related bug IDs.

The two signals are complementary — community posts describe how end users experience the bug, JIRA comments contain the technical investigation. v4 gives the model both.

## What gets injected

A new **"JIRA Comment Thread"** block, appended to the user prompt right after the existing "Related Community Feedback" block, on the S2R / OB / EB improvement calls. Environment stays deterministic.

Per-comment format (body only — no author/vote metadata, matching v3's design):

```
[Comment 01 | 2019-05-29]
I can confirm that this bug does affect 1.14.2 How I do it: In creative mode
spawn in a villager and set the time of day to 2000. Nearby, place a workstation
without a gui such as a lectern. Get very close and target the side closest to
you, then simply press and HOLD right then left mouse buttons to break and
replace repeatedly. Eventually the game will crash. …

[Comment 02 | 2019-06-03]
It looks like it is fixed as of 1.14.3-pre1. …
```

Boilerplate filtering removes "please attach the full crash report", "+1", "me too", "same issue", and comments shorter than 5 words. Long comments that happen to include the "please attach" phrase but also add reproduction detail are kept.

**Coverage** across the 60-bug corpus:

| | Count |
|---|---|
| Total JIRA comments in the corpus | 290 |
| Comments kept after boilerplate filtering | 203 |
| Bugs with ≥1 usable JIRA comment | 43 / 60 |
| Bugs with ≥1 community post (unchanged from v3) | 51 / 60 |
| Bugs with **both** community and JIRA | 36 / 60 |
| Bugs with **neither** (MC-270097, MC-275566) | 2 / 60 |
| Max JIRA-comment block tokens on one bug | 2,118 (MC-213788, 28 comments) |
| Total JIRA-comment tokens across corpus | ~14k (p50 = 139 tokens/bug) |

The JIRA block is tiny compared to community posts (max 2k vs 15.5k) — comments are short by nature and heavily filtered.

## Prompt structure

```
Original Bug: <summary> - <description>

Improve the '<section>' section while staying true to this specific bug.

Current section: <original>
Affected Versions: <if applicable>
Retrieved knowledge: <top-5 ChromaDB chunks>

---
Related Community Feedback (unchanged from v3)
[Post 01 | score=0.769] Title: … Details: …
...

---
JIRA Comment Thread (NEW in v4)
[Comment 01 | 2019-05-29] <body>
[Comment 02 | 2019-06-03] <body>
...
```

## Contents

```
v4/
├── gpt/    — 60 files, GPT-4o-mini (v13 prompts + v14 OB rules + cleaner fix + community + JIRA)
└── qwen/   — 60 files, Qwen 2.5-32B (Q4_K_M), same prompts + same context sources
```

Each file preserves both context-source stats in `improvement_metadata`:

```json
{
  "improvement_metadata": {
    "original_key": "MC-181313",
    "community_posts": { "posts_included": 20, "tokens": 5373, ... },
    "jira_comments":   { "comments_included": 0, "tokens": 0, "comments_dropped_boilerplate": 1, ... }
  }
}
```

## Run parameters

| | GPT-4o-mini v4 | Qwen 2.5-32B v4 |
|---|---|---|
| Access | OpenAI API | Ollama on Quadro RTX 8000 (Ashburn) via SSH tunnel |
| Wall clock | 20 m 39 s | 1 h 32 m 20 s |
| Per report | ~21 s | ~92 s |
| Fill rate | 60/60 all four sections | 60/60 all four sections |

GPT and Qwen were run **in parallel** — GPT via OpenAI API while Qwen ran on the vast.ai GPU.

## v3 → v4 result (GPT, manually reviewed on the 43 JIRA bugs)

**GPT v4 shows a real, measurable improvement over v3 — this time the intervention actually worked.** Aggregate across 129 section pairs (43 bugs × 3 sections):

| Section | v4 wins | v3 wins | ties |
|---|---|---|---|
| Steps to Reproduce | 5 | 0 | 38 |
| Observed Behavior | 18 | 6 | 19 |
| Expected Behavior | 1 | 0 | 42 |
| **Total** | **24 (19%)** | **6 (5%)** | **99 (77%)** |

For contrast, v2→v3 (community posts alone) was 25 v3-wins / 19 v2-wins / 109 ties — effectively neutral. v3→v4 is 4:1 for v4 where a difference exists. Every S2R pair was either a tie or a v4 win.

Wins are content-driven, not stylistic — you can point to specific comment sentences that appear as facts in v4's output. Full analysis and top-10 win/loss examples in [`EVAL_v3_vs_v4_gpt.md`](./EVAL_v3_vs_v4_gpt.md).

**Qwen v3→v4 comparison is pending.**

## Reproducing this run

```bash
cd improveBR/replication_package

# GPT
MODEL_NAME=gpt-4o-mini \
OPENAI_API_KEY=<your-key> \
python improbr_pipeline.py \
  --input-dir results_60reports_gpt_v2/preprocessed \
  --improve \
  --output-dir results_60reports_gpt_v4 \
  --community-posts-dir "<path>/threshold_0.70_after_bug_creation_cosine_posts" \
  --jira-comments-dir "<path>/selected_60_bug_reports_full_json"

# Qwen (Ollama at 127.0.0.1:11434)
MODEL_NAME=qwen2.5:32b-instruct-q4_K_M \
OPENAI_API_KEY=sk-local \
OPENAI_BASE_URL=http://127.0.0.1:11434/v1 \
LOCAL_LLM=1 \
python improbr_pipeline.py \
  --input-dir results_60reports_gpt_v2/preprocessed \
  --improve \
  --output-dir results_60reports_qwen_v4 \
  --community-posts-dir "<path>/threshold_0.70_after_bug_creation_cosine_posts" \
  --jira-comments-dir "<path>/selected_60_bug_reports_full_json"
```

New pipeline flags added in v4:
- `--jira-comments-dir <path>` — directory containing the full JIRA JSONs (`selected_60_bug_reports_full_json`)
- `--jira-comments-token-budget <int>` — per-bug token cap (default 30,000; corpus max used = 2,118)

Loader lives at `utils/jira_comments.py`. Injection point is `improvers/modules/section_improver.py::_generate_improved_section`. Environment section deliberately skips both context blocks.

## Notes for evaluators

- **v3 vs v4 is the primary comparison.** Same prompts, same community context, only JIRA-comment addition differs. Delta comes from that alone.
- The pipeline preserves the v2 preprocessed cache-key contamination fix (empty prompt block for the 17 bugs without JIRA is genuinely different than the "no jira block at all" v3 prompt — both go through fresh LLM calls, no cache reuse).
- `EVAL_v3_vs_v4_gpt.md` has the manual per-bug scoring for GPT. Qwen equivalent is not yet written.
