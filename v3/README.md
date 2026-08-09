# v3 — 60 enhanced Minecraft bug reports with community-post context

Same 60 reports, same pipeline, same model (GPT-4o-mini) as [v2](../v2). The single change: community-post context is injected into each per-section improvement call.

## Why v3 exists

v1 and v2 gave the LLM only the raw bug report plus five retrieved chunks from a Minecraft QA-workflow knowledge base. Real Minecraft users don't file bugs in isolation — they also post on [Minecraft Feedback](https://feedback.minecraft.net) describing the same or adjacent issues in their own words. The hypothesis for v3: giving the LLM the semantically-similar community posts as additional context should let it write more grounded Steps to Reproduce, describe the Observed Behavior in language that matches how users actually experience the bug, and avoid inventing reproduction details that aren't in the original ticket.

## Data source

Community posts come from `data_collection/selected_60_community_post_mapping/threshold_0.70_after_bug_creation_cosine_posts/`. Mapping method:

- Encoder: `nomic-v1.5`
- Similarity: cosine
- Threshold: **>= 0.70**
- Time filter: `post_created_at >= bug_created_at` (posts that came after the JIRA report was filed — so the community is describing the same bug that already exists, not the other direction)
- Per-bug ranking: sorted descending by cosine score

Post-count distribution across the 60 bugs:

| Posts injected | # of bugs |
|---|---|
| 0 (no matches above 0.70) | 9 |
| 1–3 | 14 |
| 4–9 | 17 |
| 10–19 | 10 |
| 20–49 | 8 |
| 50+ | 2 (MC-185285: 81, MC-267937: 38 tied with 35) |

Total posts injected across the corpus: **648**.

## What gets injected

For each bug, all posts above the 0.70 threshold are formatted as a single "Related Community Feedback" block and **appended to the user prompt** for the Steps to Reproduce / Observed Behavior / Expected Behavior improvement calls. Environment is skipped (built deterministically from `affected_versions`).

Per-post format (title + details only — social signal like vote counts intentionally omitted so the LLM treats posts as independent observations rather than voting them):

```
[Post 01 | score=0.769]
Title: <post title>
Details: <post body>

[Post 02 | score=0.755]
Title: ...
Details: ...
```

The block is preceded by a short header instructing the model to treat posts as supporting signal (not to invent facts that only appear in community posts, and not to copy post prose verbatim).

## Why community context lives in the USER prompt, not the system prompt

OpenAI's chat completions API has automatic prompt caching that kicks in on the stable prefix (≥1024 tokens) shared across calls. The pipeline makes three per-report calls (S2R, OB, EB) with a stable system prompt containing the rules and few-shot examples. The community block, by contrast, is bug-specific — putting it in the system prompt would poison the cache for every call. In the user prompt, the system-prompt prefix stays cache-hot across all 180 calls while the community-post variance sits in the (uncached) user payload.

## Token budget & context management

- gpt-4o-mini context window: 128k
- Per-bug community-block token budget: **60,000 tokens** (hard cap; excess posts dropped in ascending score order)
- Largest observed community block: MC-185285 at 15,534 tokens (81 posts) — well under budget
- No bug in the corpus triggered a drop

Token counts computed with `tiktoken` using the `o200k_base` encoding (gpt-4o-mini's tokenizer).

## Fields kept per post

Only `title` and `details` — the two human-readable content fields. Deliberately excluded: vote_sum, comment_count, follower_count, timestamps, URLs, author_id, topic_id. Removing engagement metadata was a design choice — including votes would let the LLM implicitly rank posts by community popularity, which biases the enhancement toward whatever loudest users complain about rather than treating each post as an independent observation of the same bug.

## Prompt structure — the S2R user prompt for a bug WITH community posts

```
Original Bug: <summary> - <description>

Improve the 'Steps to Reproduce' section while staying true to this specific bug.

Current section: <original S2R>
Affected Versions: <if applicable>
Retrieved knowledge: <top-5 chunks from ChromaDB via cross-encoder rerank>

---
Related Community Feedback (Minecraft Feedback posts semantically similar to this bug, cosine >= 0.70, sorted by similarity):
Use these as additional signal for how end users describe the issue. Treat as supporting context — do NOT invent facts that only appear in community posts, and do NOT copy community-post prose verbatim.

[Post 01 | score=0.769]
Title: ...
Details: ...

[Post 02 | score=0.755]
Title: ...
Details: ...

...
```

Bugs with 0 posts get an empty community block (identical user prompt to v2), so their outputs are cache-identical to v2 — any v3-vs-v2 delta is directly attributable to community context.

## Contents

```
v3/
└── gpt/    — 60 files, GPT-4o-mini output (v13 prompts + v14 OB rules + cleaner fix + community context)
```

Each file is `MC-<jira-key>_improved.json` with sections exposed as top-level string keys:

- `Steps to Reproduce`
- `Observed Behavior`
- `Expected Behavior`
- `Environment`

`improvement_metadata.community_posts` records per-bug injection stats:

```json
{
  "improvement_metadata": {
    "original_key": "MC-181313",
    "community_posts": {
      "bug_key": "MC-181313",
      "posts_available": 20,
      "posts_included": 20,
      "posts_dropped_over_budget": 0,
      "tokens": 5373
    }
  }
}
```

## Run parameters

| | GPT-4o-mini + community |
|---|---|
| Access | OpenAI API (`api.openai.com/v1`) |
| Wall clock | 23 m 35 s |
| Per report | ~24 s |
| Fill rate | 60/60 all four sections |
| Total posts injected | 648 across 51 bugs |
| Max posts in one bug | 81 (MC-185285) |
| Max token spend on posts | 15,534 tokens (MC-185285) |
| Community-block token budget | 60,000 (hard cap; never triggered) |

Preprocessed inputs were reused from `v2/preprocessed/` (cleaner fix already applied — `@ ~ / $ ^ =` preserved). Prompts are v13 + v14 OB rules unchanged from v2 — only the user prompt is augmented with the community block.

## Per-section word-count summary

| Section | avg (words) | min | max |
|---|---|---|---|
| Steps to Reproduce | 62.5 | 23 | 189 |
| Observed Behavior | 164.4 | 98 | 302 |
| Expected Behavior | 67.5 | 57 | 88 |
| Environment | 9.3 | 5 | 50 |

Broadly similar to v2 lengths — the community block informs content, not length ceilings.

## Reproducing this run

```bash
cd improveBR/replication_package
MODEL_NAME=gpt-4o-mini \
OPENAI_API_KEY=<your-key> \
python improbr_pipeline.py \
  --input-dir results_60reports_gpt_v2/preprocessed \
  --improve \
  --output-dir results_60reports_gpt_v3_community \
  --community-posts-dir "<path>/threshold_0.70_after_bug_creation_cosine_posts" \
  --community-token-budget 60000
```

Community-post loader lives at `utils/community_posts.py`. The user-prompt injection point is `improvers/modules/section_improver.py::_generate_improved_section`. Environment section deliberately skips community context.

## Notes for evaluators

- **v2 vs v3 head-to-head is the primary comparison.** Same model, same prompts, same inputs — the only variable is community-post injection. 9 bugs (empty community folders) will be cache-identical to v2 by design; a real delta will only appear on the 51 bugs with posts.
- **v1 → v2 → v3 progression** — v1 had corrupted commands (cleaner bug); v2 fixed the cleaner and added OB rules 7-9; v3 layers community context on top of v2.
- Qwen v3 is not run yet — the community-context wiring is model-agnostic and the same `--community-posts-dir` flag would work against a local Ollama endpoint. Skipped here because the user asked for GPT first.
