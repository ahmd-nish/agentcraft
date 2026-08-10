# v2 vs v3 — manual side-by-side evaluation

**Question**: does injecting Minecraft Feedback community posts (v3) into the improver's user prompt produce measurably better bug-report sections than v2 (no community context)?

**Method**: manual pairwise review of every Steps to Reproduce / Observed Behavior / Expected Behavior section on the 51 bugs that received community posts, for both GPT-4o-mini and Qwen 2.5-32B. Each section pair was labelled `v3-wins`, `v2-wins`, or `tie`. 306 section pairs reviewed in total (51 bugs × 3 sections × 2 models).

**Note**: the 9 bugs with zero community matches above the 0.70 cosine threshold are excluded from this evaluation — they received no intervention.

## Aggregate result

### GPT-4o-mini (153 section pairs)

| Section | v3 wins | v2 wins | ties |
|---|---|---|---|
| Steps to Reproduce | 7 | 3 | 41 |
| Observed Behavior | 15 | 15 | 21 |
| Expected Behavior | 3 | 1 | 47 |
| **Total** | **25 (16%)** | **19 (12%)** | **109 (71%)** |

### Qwen 2.5-32B (153 section pairs)

| Section | v3 wins | v2 wins | ties |
|---|---|---|---|
| Steps to Reproduce | 10 | 6 | 35 |
| Observed Behavior | 8 | 13 | 30 |
| Expected Behavior | 2 | 1 | 48 |
| **Total** | **20 (13%)** | **20 (13%)** | **113 (74%)** |

**On both models the effect is neutral to negative when directly compared, and dominated by ties.**

## Where v3 does win, why does it win?

The wins are almost never "v3 imported new factual detail from a community post". They fall into two patterns:

1. **QA-workflow-bleed removal (Qwen S2R and Qwen OB, most of the v3 wins).** v2 Qwen frequently appended "attach screenshots, ZIP archive of the debug folder, latest.log, crash-reports/*.txt" to S2R or OB. v3 Qwen tends to leave that out. This is stylistic compression — the model is producing tighter prose, not adding grounded information.
2. **Better structuring of pre-existing content (GPT).** MC-231185 and MC-275883 saw v3 separate the two reproduction scenarios more cleanly; MC-268882 saw v3 articulate the namespace collision explicitly. These are re-organisations of what v2 already knew, not new facts.

Only two bugs showed a plausible community-content-derived improvement:

- **MC-275883** (Qwen S2R): v3 added the "Enable the Minecart Improvements experiment in Options" step that v2 omits. The community-post cluster includes "Experimental Minecarts Fix (Java)" at cosine 0.74 — a plausible source.
- **MC-213788** (Qwen OB): v3 added a concrete "101 in-game ticks / 5.05 seconds" timing window. Provenance is less clear.

Everywhere else, v3's "wins" are style-driven, not knowledge-driven.

## Where v3 loses, why does it lose?

Three regression patterns, all more common on v3 than v2:

**Rule 9 regression — meta-commentary appended to OB.** GPT v3 gained 6 new rule-9 violations that were clean in v2. Example endings v3 added: "This bug highlights a critical flaw in the text handling system within the anvil interface, necessitating further investigation by the development team" (MC-156389), "This bug highlights a critical issue in the game mechanics" (MC-160102), "This detailed information should help developers understand and address the specific issue" (Qwen MC-156389).

**Rule 8 regression — QA-workflow bleed at end of OB.** GPT gained several instances of "provide screenshots / ZIP archive of the debug folder / latest.log / crash-reports/*.txt" appearing where v2 didn't have it. GPT went from 2 to 3 OB bleeds; individual cases include MC-197122, MC-235964, MC-268408, MC-269670. (Qwen actually reduced this pattern — see the Qwen wins above.)

**Rule 7 regression — S2R restated inside OB.** Qwen v3 added inline "To reproduce the issue: 1. …" numbered lists inside the OB narrative on multiple bugs (MC-156389, MC-160248, MC-198514, MC-248926). GPT v3 also did this occasionally.

**Catastrophic collapses (Qwen only).** Three bugs where Qwen v3 stubbed out a section that v2 had populated well:

- **MC-277967**: v3 OB collapsed to 14 words, losing the entire explosion-type list. EB collapsed to 5 words ("The game should not crash").
- **MC-250919**: v3 S2R collapsed to a single 8-word sentence.
- **MC-249712**: v3 OB ballooned to 421 words and hallucinated a self-reference ("Code analysis for further details can be found in a specific comment where important parts are marked by a star").

These are Qwen-specific and correlate with tunnel drops during the run — they are quality failures, but they are also runtime-infrastructure failures. A stable run would probably not produce these three.

## Concrete v3 wins (top 5)

1. **MC-275883 (Qwen S2R)** — v3 adds "Enable the Minecart Improvements experiment in Options" step that v2 omits. Plausibly community-derived.
2. **MC-166004 (Qwen S2R + OB)** — v2 has heavy QA-bleed on both S2R and OB; v3 removes it and stays on the IndexOutOfBoundsException mechanism.
3. **MC-268408 (Qwen OB)** — v2 OB devolves into a bulleted attachment checklist; v3 stays as coherent prose about the data-pack-disable interaction.
4. **MC-180257 (Qwen EB)** — v3 EB proposes the *correct* fix (display error message on invalid LodestonePos); v2 EB *endorses the buggy behaviour* ("should allow the creation without any issues").
5. **MC-272406 (Qwen OB)** — v2 OB is a stub with an "### Actual Result" header and 55 words; v3 OB is coherent narrative including the MC-272321 linkage and Hard-difficulty condition.

## Concrete v3 losses (top 5)

1. **MC-277967 (Qwen all three sections)** — catastrophic collapse. OB → 14 words, EB → 5 words.
2. **MC-250919 (Qwen S2R)** — 8-word stub replacing v2's full 7-step reproduction.
3. **MC-171020 (Qwen OB)** — v3 loses the biome × generation-mode failure matrix (Nether Wastes/Crimson Forest/Warped Forest × Surface/Caves) that v2 preserved.
4. **MC-268882 (Qwen OB)** — v3 breaks the semantic contrast between `sharpness` (no crash) and `minecraft:sharpness` (crash), presenting the same command twice as if different.
5. **MC-156389 (Qwen OB)** — v3 combines rule 7 (restates full 4-step reproduction inside OB) and rule 9 (ends with meta-commentary).

## Verdict

**Community-post context does not measurably improve bug-report enhancement on this task, on either model.**

- **GPT-4o-mini** is largely unaffected by community context — the quantitative similarity analysis showed v3-vs-v2 divergence indistinguishable from re-runs of the same prompt (Δ 0.017–0.038). The manual review confirms: 25 v3 wins vs 19 v2 wins vs 109 ties, with the wins coming from re-structuring pre-existing content rather than any community-derived facts. GPT v3 also picked up 6 net new rule-9 meta-commentary regressions.
- **Qwen 2.5-32B** *does* diverge substantially with community context (Δ 0.113–0.178 above the same-prompt noise floor), but the manual review shows this divergence trends toward degradation, not improvement: 20 v3 wins vs 20 v2 wins vs 113 ties. Qwen v3's dominant win pattern is not "used community info" — it's "stopped appending QA-workflow bleed that v2 had", which is a small style improvement. Its loss patterns include rule 7/8/9 regressions and three catastrophic single-section collapses.

**Why the community posts helped so little**: on inspection, the top posts for each bug are usually thematically-adjacent Feedback threads (feature requests, general complaints in the same category) rather than technically-specific match-ups. For example, MC-181313 ("server crash on high-damage arrow") was matched with posts titled "Nerf Harming Arrows Bedrock Edition" and "(Bedrock Parity) /damage" — related in topic, but containing no reproducible bug-mechanic detail that the LLM could fold in. The cosine similarity threshold of 0.70 is admitting posts that share vocabulary and topic but not causal detail. A stricter threshold, or a filter that requires a Minecraft bug-tracker cross-reference in the post body, would likely produce more usable material — but at the cost of admitting fewer posts.

**Practical recommendation**: on this dataset, v3 is not an improvement over v2 for either model. If you want to argue "adding community context improves bug reports," this experiment does not support that claim. The next lever to try is not more posts or a bigger token budget — it is *higher-quality* posts (raise threshold, or require in-post bug-ID references), or a preprocessing step that extracts only the mechanically-relevant sentences from each post rather than dumping title + full details.

## Method notes

- Reviewers: two independent subagent runs, one for each model, given identical rubrics and the same side-by-side markdown (`V2_VS_V3_SIDEBYSIDE.md` in the pipeline repo).
- Rubric asked for: `v3-wins` (meaningfully better), `v2-wins` (regressed with a specific reason), `tie` (cosmetic differences or comparable quality issues on both sides). Rubric also explicitly flagged v14 rules 7/8/9 as regression targets.
- 306 section pairs total. Ties dominate (71–74%) — most section pairs were near-identical in substance.
- Empty-community bugs (9 of 60) excluded — they received no intervention, and their v2-vs-v3 divergence is pure LLM nondeterminism (Δ ~0.19–0.72 similarity depending on section, at temperature 0.5).
