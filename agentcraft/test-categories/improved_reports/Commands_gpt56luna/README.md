# Commands · improved by gpt-5.6-luna

45 BugCraft-Bench bug reports from the **Commands** category, run through the ImproBR v4 pipeline and improved by OpenAI's `gpt-5.6-luna` reasoning model.

## Contents

45 files, one per bug: `MC-<id>_improved.json`. Each file contains the four canonical sections (S2R, OB, EB, Env) plus the retained metadata (ticket key, affected versions, category, resolution, description) so the record is drop-in comparable with the input from `../eligible_reports/Commands/`.

## Inputs

- Source reports: `../eligible_reports/Commands/*.md` (45 files, BugCraft-Bench Markdown format)
- Adapted into the pipeline's preprocessed-JSON schema before improvement; adapter script kept in the run's scratchpad
- All four canonical sections were left empty in the adapted records, so the improver generated S2R / OB / EB from the description and Environment deterministically from the affected-version list

## Pipeline configuration

| | value |
|---|---|
| Model | `gpt-5.6-luna` (OpenAI reasoning) |
| Base URL | `https://api.openai.com/v1` |
| Temperature | 1 (forced — the model rejects any other value) |
| Token cap | via `max_completion_tokens` (reasoning model — the model rejects `max_tokens`) |
| Per-request timeout | 120 seconds (added after two hung-socket incidents mid-run) |
| Community-post injection | **not applied** — precomputed matches only exist for the 60-report evaluation set |
| JIRA-comment injection | **not applied** — same reason |
| Retrieval | Minecraft-wiki RAG via ChromaDB (`all-MiniLM-L6-v2`), cross-encoder rerank (`ms-marco-MiniLM-L-6-v2`), top-5 chunks after allowlist + threshold |
| Section prompts | v14 (same as the 60-report v4 runs) |
| Drift validator | `pydantic-ai` `Verdict` schema, temperature forced to 1 for this model |

Comparison note: this is a **retrieval-only** improvement (community posts and JIRA comments unavailable for these bugs), so the results are closer to v3 than v4 in evidence-mix terms. Everything else — prompts, validator, retry loops, section formatting — matches the v4 runs on the 60-bug evaluation set.

## Run summary

| | value |
|---|---|
| Bugs improved | 45 / 45 |
| Sections filled (of 180) | 180 (100%) |
| Empty-section retries | 1 (MC-73178 lost during a network incident, refilled cleanly on rerun) |
| Total wall clock | ~55 min across three restarts |
| Per-bug time (steady state) | ~29 s |
| API rate-limit hits (429) | 0 |
| Hard errors after timeout patch | 0 |

Two hung-socket incidents in the first two runs (OpenAI responses not returning on a specific long-description bug) were fixed by pinning `timeout=120s` on the `openai.OpenAI` client; the pipeline's own attempt-loop retries handled the recoveries.

## Section length averages

| section | avg words | min | max |
|---|--:|--:|--:|
| Steps to Reproduce | 66 | 8 | 125 |
| Observed Behavior | 88 | 22 | 188 |
| Expected Behavior | 54 | 10 | 67 |
| Environment | 21 | 1 | 119 |

## Known caveat

Reasoning-model outputs occasionally include a Markdown sub-heading (`### Actual behavior`) or a fenced code block inside the OB section, which the v14 OB rules forbid in prose sections. The pipeline's `prose-retry` loop catches bullets and numbered lists but not headings/code blocks. If a strict-prose OB is required for downstream comparisons, a second post-process pass should strip these markers.

## Reproducing this run

```bash
cd /Users/nish/Documents/minecraft-agents/improveBR/replication_package
source .env
export OPENAI_API_KEY=$OPENAI_API_KEY
export OPENAI_BASE_URL=https://api.openai.com/v1
export MODEL_NAME=gpt-5.6-luna

python improbr_pipeline.py \
  --input-dir commands_input/preprocessed \
  --improve \
  --output-dir results_commands_gpt56luna
```

Inputs adapted from `../eligible_reports/Commands/*.md` by the scratchpad adapter (`adapt_md_to_preprocessed.py`).
