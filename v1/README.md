# v1 — 60 enhanced Minecraft bug reports

Two parallel enhancement runs over the same 60 real Minecraft bug reports (sourced from Mojang JIRA). One using OpenAI GPT-4o-mini via the OpenAI API, one using Qwen2.5-32B-Instruct (Q4_K_M quantization) running locally on an Nvidia RTX 8000 via Ollama. Both runs used identical inputs and identical prompts (v13 prompt set).

## Contents

```
v1/
├── gpt/    — 60 files, GPT-4o-mini output
└── qwen/   — 60 files, Qwen2.5-32B output
```

Each file is `MC-<jira-key>_improved.json` with sections exposed as top-level string keys:
- `Steps to Reproduce`
- `Observed Behavior`
- `Expected Behavior`
- `Environment`

The original JIRA metadata (summary, description, affected_versions, comments, resolution, etc.) is preserved alongside these keys.

---

## Pipeline

ImproBR runs four stages per report:

1. **Preprocess** — extract structured fields from raw JIRA JSON.
2. **Detection** — an LLM classifier flags which of the four sections are missing or weak.
3. **Retrieval** — knowledge is fetched **once per report** and shared across all section generations:
   - Vector store: ChromaDB with `sentence-transformers/all-MiniLM-L6-v2` embeddings.
   - Cross-encoder rerank: `cross-encoder/ms-marco-MiniLM-L-6-v2`, top-5 chunks returned.
   - An anvil/NBT format blocklist regex filters retrieved chunks so file-format speculation does not bleed into generated text.
4. **Improvement** — **3 separate LLM calls per report**, one per LLM-generated section, each with its own dedicated prompt (see below). `Environment` is deterministic — built by formatting the report's `affected_versions` list, no LLM call.
5. **Validation** — a Pydantic-AI schema (`Verdict`) checks each section for drift from the original bug. On rejection the whole report retries with the validator's rejection text fed back to the improver as targeted feedback (`MAX_IMPROVE_RETRIES=3`).

There is also a section-level format-rejection retry: if the OB section comes back with bullets or a subsection heading, the pipeline re-prompts up to 2 times before accepting.

## Models

| | GPT-4o-mini | Qwen2.5-32B-Instruct |
|---|---|---|
| Access | OpenAI API (`api.openai.com/v1`) | Ollama on RTX 8000 (via SSH tunnel to `127.0.0.1:11434/v1`) |
| Quantization | full precision | Q4_K_M (~19 GB on disk) |
| Wall clock (60 reports) | 17 m 39 s | 1 h 22 m 09 s |
| Per report | ~17 s | ~86 s |
| Fill rate | 60/60 all four sections | 60/60 all four sections |

Both runs used `MAX_IMPROVE_RETRIES=3`, `USE_PYDANTIC_AI=1`, and the identical v13 prompt set below.

---

## Prompts (v13)

The prompt strings are Python f-strings. `{issue_type}` receives the tag from the detection stage (e.g. `crash`, `missing`). `{original_context}` receives the summary + description from the original bug report.

### Steps to Reproduce prompt

```
You are writing the Steps to Reproduce (S2R) section for a Minecraft bug report identified as {issue_type}.

ORIGINAL BUG (single source of truth):
{original_context}

HARD RULES — read every line:

1. Use ONLY details explicitly present in the original report. Do NOT add:
   - versions, editions (Java vs Bedrock), platforms, OS
   - game modes, world types, difficulty, seed, biomes, dimensions
   - specific coordinates, block counts, mob names, items, tools
   unless the original report explicitly named them.
2. Do NOT invent Minecraft mechanics you are unsure of. If unsure, describe
   the outcome in general terms instead of naming a specific key/mechanic.
   (Common qwen mistakes to avoid: "press F5 to sneak" — F5 is 3rd-person
   view; "the in-game backup system" — Minecraft has no such thing.)
3. Prefer the SIMPLEST reproduction path:
   - Use Creative mode + /commands ONLY when it makes the setup shorter and
     does NOT change the bug being reported.
   - Do NOT add "no mods installed", "play for extended period", "build
     significant structures", "gather resources first", or similar padding.
4. For UI-related bugs, use CONCRETE menu paths as they exist in Minecraft.
   Choose from this menu when relevant — do NOT paraphrase, do NOT invent:
     * Main menu: "Singleplayer", "Multiplayer", "Realms", "Options"
     * "Options -> Controls -> Key Binds" (e.g. "Sneak", "Sprint", "Jump")
     * "Options -> Video Settings" (e.g. "Fullscreen", "Render Distance", "GUI Scale")
     * "Options -> Music & Sounds"
     * "Options -> Accessibility Settings"
     * "Singleplayer -> [world] -> Edit -> Open World Folder"
     * "Singleplayer -> [world] -> Edit -> Backup and Load"
     * "Create New World -> More World Options -> [resource pack]"
     * In-game: "F3 debug screen" (biome, coords, chunk info)
     * In-game: "Esc menu -> Save and Quit to Title"
     * Commands: `/gamemode creative`, `/weather rain`, `/summon <entity>`,
       `/give`, `/tp`, `/setblock`. Only use commands you are certain exist.
   When you don't know the exact path, describe the menu category
   generically ("the game's video settings") rather than inventing a name.
5. Between 4 and 10 numbered steps. Each step is ONE action a tester performs.
6. If the bug involves a timed observation (freeze, spawning, animation,
   decay, cooldown, or "wait for X"), split it into an action step and a
   SEPARATE wait step and a SEPARATE observe step. Concrete example:
     BAD:  "3. Toggle Fullscreen on or off. Observe the game freezes ~5s."
     GOOD: "3. Toggle Fullscreen to On.
            4. Wait approximately 5 seconds and observe the game freeze.
            5. After the freeze ends, listen for the jukebox audio to stop.
            6. Toggle Fullscreen to Off.
            7. Wait approximately 5 seconds and observe the game freeze again."
7. Every wait step must state a CONCRETE duration or trigger from the
   original report (e.g. "wait approximately 5 seconds", "wait at least
   10 minutes", "wait until night", "wait for the fuse to detonate").
   Do NOT invent durations the original report did not imply — if the
   report is silent on timing use "wait at least a few minutes" and no more.
8. When the bug is UI-driven, the opening steps should specify:
   (a) game mode ("Creative world with default settings" is a safe
       default when the report doesn't say),
   (b) version if the original report named one,
   and then navigate via the exact menu paths from rule 4.
9. If the report mentions a Minecraft command, cite it in full with
   arguments, in backticks. Examples:
     GOOD:  "`/effect give @p minecraft:speed 60 1`"
     GOOD:  "`/summon minecraft:iron_golem ~ ~ ~`"
     BAD:   "use the /summon command" (no arguments)
     BAD:   "give yourself a status effect" (no command)
   Only cite commands you are certain exist.
10. The FINAL step must be either (a) the observation of the bug, or
    (b) a documentation step ("take a screenshot", "record the fps",
    "note the coordinates"). Not both, unless the report emphasises
    documentation.
11. If the original report is retracted, blank, or non-actionable, write
    the minimum steps that describe the scenario — do NOT invent detail
    to fill space.

FORMATTING:
- Return ONLY the numbered steps.
- Do NOT include "Steps to Reproduce:" or any header.
- Do NOT use ** or ### or bullets — only "1." "2." "3." etc.
- Do NOT add sub-sections like "Expected Behavior", "Environment", "Additional".

Example of a GOOD S2R (concrete + faithful, wait steps explicit):
1. Launch Minecraft Java Edition 1.21.4.
2. Create a new Creative world with default settings.
3. Open Options -> Controls and set the Sneak binding to "Hold".
4. Return to the world and press and hold the Sneak key (default: Left Shift).
5. Wait approximately 1 second, then release the Sneak key.
6. Observe that the character remains sneaking after the key is released.
7. Repeat steps 1-6 in Minecraft Java Edition 1.21.5 to confirm the bug persists.

Example of a GOOD S2R (performance bug with wait+observe breakdown):
1. Launch Minecraft Java Edition 1.21.5.
2. Create a new Singleplayer world in Survival mode with default settings.
3. Set Render Distance to 16 chunks via Options -> Video Settings.
4. Press F3 to open the debug screen and note the current FPS.
5. Move around the world for at least 5 minutes while monitoring the FPS
   on the F3 debug screen.
6. Record any drops to 0 FPS and the approximate duration of each drop.
7. Exit the game and launch Minecraft Java Edition 1.21.8.
8. Repeat steps 2-6 with identical settings.
9. Compare recorded FPS from both versions and note the difference.

Example of a BAD S2R (over-invented — do NOT do this):
1. Create a new Survival world with default settings.
2. Build extensive structures using stone, wood, and obsidian.
3. Ensure no mods or plugins are installed.
4. Play for an extended period without immediate issues.
(^ none of that was in the original report)

Example of a BAD S2R (missing wait step, actions collapsed):
1. Toggle Fullscreen on or off.
2. Observe the game freezes for about 5 seconds and the jukebox goes silent.
(^ should be 4-6 steps with explicit wait and separate observations)
```

### Observed Behavior prompt

```
You are writing the Observed Behavior (OB) section for a Minecraft bug report identified as {issue_type}.

ORIGINAL BUG (single source of truth):
{original_context}

HARD RULES:

1. LENGTH LIMIT: 2 to 4 sentences. Absolute maximum 100 words.
   Long, exhaustive OBs are FAILURES — do not write essays.
2. Describe ONLY what actually happened. Not what should happen. Not the fix.
3. Do NOT speculate about CAUSES. Forbidden phrases include:
   "This might be due to...", "Potential causes:", "chunk corruption",
   "Anvil format issues", "memory constraints", "possibly caused by...",
   "level.dat may be corrupted", "the anvil file...".
4. Do NOT include SUB-SECTIONS. Forbidden headings inside this section:
   "Steps to Reproduce:", "Expected Behavior:", "Environment:",
   "Additional Information:", "Potential Causes:", "Technical Observations:",
   "Relevant Files:", "Conclusion:", "Visual Representation:".
5. Do NOT INVENT observations that are not in the original report. Examples
   of invention to avoid: "The issue does not occur on single-player",
   "Certain structures become invisible", "No errors in console logs",
   "The problem is consistent across multiple sessions" —
   unless the original report literally said so.
6. Do NOT list files (level.dat, r.x.z.mca), byte offsets, or version numbers
   that were not in the original report.

FORMATTING:
- Return ONLY the section content.
- No "Observed Behavior:" header, no ** or ###, no bullets, no numbered subsections.
- Plain prose only, one paragraph.

Example of a GOOD OB (2 sentences, faithful):
The Iron Golem occasionally walks to a nearby grass block and places a
flower on it instead of engaging with hostile mobs. This happens
intermittently without any player action or nearby threats.

Example of a BAD OB (verbose, speculative, section bleed — do NOT do this):
"Iron Golems occasionally exhibit unexpected behavior. Specifically:
 - No hostile mobs are present
 - This does not occur consistently
 Potential Causes: Chunk Corruption; Anvil Format Issues; Memory Constraints
 Steps: 1. Spawn a Golem. 2. Wait. 3. Observe.
 Additional Observations: The issue persists after restarting the game."
```

### Expected Behavior prompt

```
You are writing ONE SHORT PARAGRAPH describing the Expected Behavior for
a Minecraft bug report (identified as {issue_type}). This paragraph
replaces the current Expected Behavior text.

ORIGINAL BUG (single source of truth):
{original_context}

WRITE EXACTLY ONE PARAGRAPH describing what SHOULD have happened when
following the reproduction steps. Base the expectation on what the
original bug implied — invert the observed behavior.

HARD LENGTH: between 30 and 90 words. Aim for ~60 words.

WRITE ONLY THE PARAGRAPH — nothing else. That means:
- No headings, no bullets, no numbered lists.
- No sub-labels ("Additional Information:", "Impact:", etc.).
- No repetition of Steps to Reproduce.
- No speculation about Minecraft internals or file formats.
- No invented mechanics you are unsure of.

Example of a GOOD Expected Behavior paragraph (~55 words):

When "Hold Sneak" is enabled in Options -> Controls, holding the Sneak
key should keep the character sneaking, and releasing the key should
stop the sneak immediately. The state should not toggle on a single
key press. This should behave consistently in Java Edition 1.21.4 and
1.21.5.

Example of a WRONG Expected Behavior (rejected — repeats S2R, invents):

"The player should launch Minecraft, open Options, then Controls, then
set Sneak to Hold, then in-game hold Shift and see the character
sneaking correctly in all game modes on all operating systems including
Windows 10, macOS, and Linux..."
```

### Environment (deterministic — no LLM call)

The Environment section is built by concatenating the report's `affected_versions` list into the format:

```
Minecraft Java Edition Version <version>
```

for a single-version report, or:

```
Minecraft Java Edition Versions: <v1>, <v2>, ... (includes snapshot)
```

for multi-version reports, with the `(includes snapshot)` suffix added if any element matches the snapshot naming pattern (`YYwWWx`). Because this step is deterministic, both GPT and Qwen outputs have identical `Environment` values (avg 9.3 words).

An LLM prompt (`get_environment_prompt`) exists as a fallback path but was not exercised in these runs.

---

## Results at a glance

Average length per section (words):

| | S2R | OB | EB | Env |
|-|-----|-----|-----|-----|
| GPT-4o-mini | 65.5 | 168.5 | 65.2 | 9.3 |
| Qwen2.5-32B | 136.1 | 141.2 | 52.3 | 9.3 |

Manual side-by-side scoring across 180 sections (60 reports × 3 LLM-generated sections):

| Section | Qwen wins | Tie | GPT wins | Qwen ≥ parity |
|---------|-----------|-----|----------|---------------|
| S2R | 9 | 50 | 1 | 59/60 (98%) |
| OB  | 4 | 24 | 32 | 28/60 (47%) |
| EB  | 1 | 59 | 0 | 60/60 (100%) |
| **Total** | **14** | **133** | **33** | **147/180 (82%)** |

Qwen matches or beats GPT on 82% of sections overall. Qwen dominates S2R because the v13 explicit rules (backtick commands, mode+defaults, wait-step breakdown, documentation step) land harder on it than on GPT. Qwen loses OB most often (32/60) — mainly to (a) restating reproduction steps inside OB, (b) leaking QA-workflow guidance (screenshots/debug-folder/ZIP), and (c) closing with meta-commentary ("this bug highlights…"). Those patterns motivate the v14 OB prompt iteration.

One catastrophic Qwen failure: MC-171020 (nether biomes in buffet worlds) — the S2R degenerates into a 2855-word repetition loop of the same 8-step block. 1 / 60 = 1.7%.

## Reproducing the runs

Both runs used the same ImproBR pipeline with:

- `USE_PYDANTIC_AI=1`
- `MAX_IMPROVE_RETRIES=3`
- v13 prompts (above)

GPT run:

```
MODEL_NAME=gpt-4o-mini \
OPENAI_API_KEY=<your-key> \
OPENAI_BASE_URL=https://api.openai.com/v1 \
python improbr_pipeline.py \
  --input-dir <60-reports-flat-schema-dir> \
  --improve \
  --output-dir results_60reports_gpt
```

Qwen run (assumes Ollama with `qwen2.5:32b-instruct-q4_K_M` reachable at `127.0.0.1:11434`):

```
MODEL_NAME=qwen2.5:32b-instruct-q4_K_M \
OPENAI_API_KEY=sk-local \
OPENAI_BASE_URL=http://127.0.0.1:11434/v1 \
LOCAL_LLM=1 \
python improbr_pipeline.py \
  --input-dir <60-reports-flat-schema-dir> \
  --improve \
  --output-dir results_60reports_qwen
```
