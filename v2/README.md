# v2 — 60 enhanced Minecraft bug reports (cleaner fix + OB rule tightening)

Same 60 reports, same pipeline, same models as [v1](../v1). Two changes:

1. **Preprocessor cleaner fix** — a bug in `data/preprocessor.py` was destroying Minecraft-command syntax before the LLM ever saw the input.
2. **OB prompt tightening (v14 rules 7-9)** — three new rules added to `get_observed_behavior_prompt` targeting the failure patterns observed in the v1 GPT-vs-Qwen comparison.

## Why v2 exists — the cleaner bug

`data/preprocessor.py`'s `clean_text()` had a whitelist regex intended to strip HTML/URL/markdown noise:

```python
# BEFORE (v1)
text = re.sub(r'[^\w\s.,;:!?()[\]{}"-]', ' ', text)
```

The whitelist excluded six characters that Minecraft commands cannot function without:

| Char | Meaning | v1 impact on the 60-report corpus |
|---|---|---|
| `@` | Target selector — `@s` = me, `@p` = nearest player, `@e` = all entities | 18 reports lost every occurrence (25 total) |
| `~` | Relative coordinate — `~ ~3 ~` = 3 blocks above me | 9 reports lost every occurrence (96 total) |
| `/` | Command prefix — `/give`, `/summon`, `/execute`, `/tp` | **38 reports** lost every occurrence (153 total) |
| `=` | NBT / blockstate — `{damage=100}`, `[axis=y]` | 14 reports lost every occurrence (46 total) |
| `$` | Macro variable + Java stack trace inner classes | 19 reports lost every occurrence (148 total) |
| `^` | Local coordinate — `^^^` for player-facing direction | 20 reports lost every occurrence (20 total) |

Concrete example, from MC-181313 (`Server crashes when critical arrow with very high damage value hits an entity`):

- Original bug in the JIRA report:
  ```
  /execute at @s anchored eyes run summon arrow ~ ~3 ~ {damage:1e100d,crit:1b}
  ```
- What the LLM actually received after v1 preprocessing:
  ```
  execute at s anchored eyes run summon arrow 3 {damage:1e100d,crit:1b}
  ```

The `@s` (self selector) collapsed to `s`, the `~ ~3 ~` (3 blocks above me) collapsed to a bare `3`, and the `/` command prefix disappeared. An LLM can guess that `s` was `@s`, but it cannot know that `3` used to mean "3 blocks up." GPT reasonably guessed "at my eye level" — placing the arrow at the player's face where it never falls. The bug being reported requires a **falling** arrow with lethal terminal velocity, so the reproduction step doesn't actually reproduce the bug.

Qwen went further off: dropped part of the arguments and reordered steps so the arrow spawn happens before switching out of Creative mode. Since Creative-mode players are invulnerable, the arrow can't hit and the bug never fires.

**This affected roughly two-thirds of the corpus.** Most Minecraft bugs in the benchmark are triggered by console commands. The v1 comparison between models was in large part a test of which LLM handles broken input more gracefully — not which produced better bug reports from clean input.

### The fix

```python
# AFTER (v2)
text = re.sub(r'[^\w\s.,;:!?()[\]{}"@~/$^=-]', ' ', text)
```

All six Minecraft-command characters are now preserved. HTML tags, URLs, and markdown images are still stripped by earlier regexes in the same function.

## Change 2 — OB prompt rules 7-9

The `get_observed_behavior_prompt` in `improvers/modules/section_prompts.py` gained three new rules targeting failure patterns quantified in the v1 analysis:

- **Rule 7 — no S2R restatement.** 17/32 of Qwen's v1 OB losses restated the reproduction steps inside the Observed Behavior section ("To reproduce this issue, first…"). OB is supposed to describe what was observed, not the recipe.
- **Rule 8 — no QA-workflow bleed.** 5/32 v1 losses had text like "gather screenshots highlighting…, a ZIP archive of the debug folder, latest.log, crash-reports/*.txt" bleeding from the retrieved knowledge base into the OB narrative. That guidance belongs in report metadata, not in the observation.
- **Rule 9 — no meta-commentary endings.** 6/32 v1 losses ended with self-referential closers like "This bug highlights a critical flaw…" or "This detailed description will assist developers…". End on a concrete observation, not a summary.

Each rule includes an explicit forbidden-phrase list. A new BAD example demonstrates all three failure modes in one paragraph and points to what should have been cut.

## Contents

```
v2/
├── gpt/    — 60 files, GPT-4o-mini output (v13 prompts + v14 OB rules + cleaner fix)
└── qwen/   — 60 files, Qwen2.5-32B output (same prompts + same fix)
```

Each file is `MC-<jira-key>_improved.json` with sections exposed as top-level string keys:
- `Steps to Reproduce`
- `Observed Behavior`
- `Expected Behavior`
- `Environment`

## Run parameters

| | GPT-4o-mini | Qwen2.5-32B-Instruct |
|---|---|---|
| Access | OpenAI API (`api.openai.com/v1`) | Ollama on Quadro RTX 8000 (Delaware host) via SSH tunnel |
| Quantization | full precision | Q4_K_M |
| Wall clock | 18 m 33 s | 1 h 37 m 47 s |
| Per report | ~19 s | ~98 s |
| Fill rate | 60/60 all four sections | 60/60 all four sections |

Both runs used `MAX_IMPROVE_RETRIES=3`, `USE_PYDANTIC_AI=1`, and identical prompts. Pipelines ran in parallel from clean `llm_cache/`.

## v1 → v2: what changed in a sample report

**MC-181313** — `Server crashes when critical arrow with very high damage value hits an entity`

GPT v1 Steps to Reproduce (broken command):
```
1. Launch Minecraft Java Edition.
2. Switch to Survival mode.
3. Execute the command: `execute at s anchored eyes run summon arrow 3 {damage:1e100d,crit:1b}`.
4. Wait for the arrow to hit you.
5. Observe that the server crashes upon impact.
```

GPT v2 Steps to Reproduce (repaired command):
```
1. Launch Minecraft.
2. Switch to Survival mode.
3. Execute the command: `/execute at @s anchored eyes run summon arrow ~ ~3 ~ {damage:1e100d,crit:1b}`.
4. Wait for the arrow to hit you.
5. Observe that the server crashes upon impact.
```

Qwen v2 Steps to Reproduce:
```
1. Switch to Survival mode.
2. Run the command `/execute at @s anchored eyes run summon arrow ~ ~3 ~ {damage:1e100d,crit:1b}`.
3. Wait for the arrow to hit you.
4. Observe that the server crashes once the arrow hits you.
```

**MC-238375** — `Crash and or data corruption upon attempting to save a world with a world border center over 30 million blocks`

GPT v1:
```
3. Execute the command `worldborder center 50000000 50000000`.
4. Execute the command `kill`.
```

GPT v2:
```
3. Execute the command `/worldborder center 50000000 50000000`.
4. Execute the command `/kill`.
```

## Reproducing the runs

The cleaner fix lives at `data/preprocessor.py:344`. Rebuild `preprocessed/` from raw before improving (the auto-preprocessing step handles this):

```
# GPT
MODEL_NAME=gpt-4o-mini \
OPENAI_API_KEY=<your-key> \
OPENAI_BASE_URL=https://api.openai.com/v1 \
python improbr_pipeline.py \
  --input-dir <60-reports-flat-schema-dir> \
  --improve \
  --output-dir results_60reports_gpt_v2

# Qwen (Ollama at 127.0.0.1:11434, model qwen2.5:32b-instruct-q4_K_M)
MODEL_NAME=qwen2.5:32b-instruct-q4_K_M \
OPENAI_API_KEY=sk-local \
OPENAI_BASE_URL=http://127.0.0.1:11434/v1 \
LOCAL_LLM=1 \
python improbr_pipeline.py \
  --input-dir <60-reports-flat-schema-dir> \
  --improve \
  --output-dir results_60reports_qwen_v2
```

## Notes for evaluators

- v1 outputs remain at `../v1/` for direct v1-vs-v2 comparison.
- The `llm_cache/` directory in the pipeline should be cleared before switching preprocessor versions, otherwise old broken responses can be served for identical model+prompt calls.
- The v14 OB rules were not exhaustively validated on their own — an earlier isolated v14 sweep was largely served from cache. v2 is the first fresh run of v14 OB rules alongside the cleaner fix.
