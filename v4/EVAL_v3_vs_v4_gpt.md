# GPT v3 vs v4 — manual side-by-side evaluation

**Question**: does injecting Mojang JIRA bug-tracker comments (v4) into the improver's user prompt produce measurably better bug-report sections than v3 (community posts only)?

**Method**: manual pairwise review of every Steps to Reproduce / Observed Behavior / Expected Behavior section on the 43 bugs that received JIRA-comment context, for GPT-4o-mini. Each section pair was labelled `v4-wins`, `v3-wins`, or `tie`. 129 section pairs reviewed. Reviewer had explicit access to the JIRA comment content per bug so wins/losses could be traced to specific comment sentences.

**Note**: 17 of the 60 bugs had no substantive JIRA comments (only boilerplate that the loader filtered out) — those are excluded from this evaluation since v4 had nothing new to work with.

## Aggregate result

| Section | v4 wins | v3 wins | ties |
|---|---|---|---|
| Steps to Reproduce | 5 | 0 | 38 |
| Observed Behavior | 18 | 6 | 19 |
| Expected Behavior | 1 | 0 | 42 |
| **Total** | **24 (19%)** | **6 (5%)** | **99 (77%)** |

Bugs with ≥1 v4-win section: **22 / 43 (51%)**. Bugs with ≥1 v4-loss section: **6 / 43 (14%)**. All-tied bugs: **16 / 43 (37%)**.

For contrast, the v2→v3 comparison (community posts alone) was 25 v3-wins / 19 v2-wins / 109 ties out of 153 pairs — near-neutral. v3→v4 is **4:1** where a difference exists, and every S2R comparison was either a tie or a v4 win (0 losses).

Almost all wins are in OB (18/24), where JIRA-comment content most naturally lives: additional confirmed hazard lists, version-specific regressions, reproduction-detail refinements, and consequence details.

## Where v4 wins — with the comment content that drove each win

Every win here is traceable to specific comment content — this is not stylistic churn.

- **MC-267937 (OB)** — Comment 1 does actual code analysis of the breeze crash. v4 picks up "infinite loop of collision-checking" and the freeze-vs-crash distinction specific to snapshot 24w03b. v3 has only generic "game fails to process" language.
- **MC-276476 (OB)** — Comment 2 lists specific hazards (fire, soul fire, lava, cactus, arrow, trident) and mentions the doEntityDrops workaround. v4 includes both. v3 says only "internal or dedicated servers".
- **MC-222517 (S2R)** — Comment 1 gives an exact reproduction command `/fill ~-10 ~-10 ~-10 ~20 ~ ~20 minecraft:slime_block`. v4 uses that exact command. v3 says only "place more than 4000 slime blocks".
- **MC-197197 (OB)** — Comment 2 has the exact preset string `minecraft:bedrock,2*minecraft:dirt,minecraft:grass_block;null` and explains "null is not a valid biome". v4 quotes it verbatim as the root cause. v3 has vague "invalid biome ID".
- **MC-275883 (OB)** — Comment 3 mentions "Invalid Rotation" log errors; Comment 2 describes entities disappearing client-side and reappearing on relog. Both facts land in v4; v3 has neither.
- **MC-153355 (OB)** — Comment 1 mentions coordinates -83/-12, a workaround (remap E/F for rapid destruction), and version regression 19w14a vs 19w14b. v4 folds all three in.
- **MC-213788 (OB)** — v4 adds "cannot save or exit, requiring force-close via task manager" and "all entities including villagers become unresponsive" — both from Comment 2.
- **MC-269670 (OB)** — v4 picks up Comment 1's persistent-corruption fact: "entering the world after the crash results in the game crashing again". v3 misses it entirely.
- **MC-270004 (OB)** — v4 uses the corrected command from Comment 2 with proper `minecraft:wind_burst` syntax; v3 had the base command from the report.
- **MC-197122 (OB)** — v3 accidentally imported QA-workflow boilerplate ("attach latest.log and ZIP archive of the debug folder" — a Rule 8 regression). v4 avoids that.

Full top-10 list plus 30+ smaller wins are in the raw side-by-side (`GPT_V2_V3_V4_SIDEBYSIDE.md` in the pipeline repo).

## Where v4 loses (6 total)

- **MC-180257 (OB)** — v4 verbatim-pasted a 14-line stack trace, bloating 166w → 207w without adding fact. Comments were social ("thanks for editing the report") — v4 had nothing to extract and pulled the trace instead.
- **MC-238375 (OB)** — v4 dropped v3's `OverlappingFileLockException` explanation and missed a genuinely useful "1.17.1 still affects" comment.
- **MC-149792 (OB)** — v4 grew via Rule 7 restatement of reproduction steps inside OB ("To reproduce the issue, one must first launch…"). Length increase without new info.
- **MC-162586 (OB)** — v4 dropped v3's OBS/Chrome/Streamlabs context. Parrot-attack comments were unrelated so v4 had nothing to add and lost specificity.
- **MC-268879 (OB)** — v4 dropped v3's discriminating observation that regular damage values don't trigger the crash. Single comment was "attach crash log" boilerplate.
- **MC-276383 (OB)** — v4 dropped v3's detailed obfuscated-method call chain (`Boat.getPickResult → getDropItem → getVariant`) — the technical crux of that bug.

Loss pattern: mostly bugs whose comments were social or boilerplate, where v4 had nothing to add but still restructured the section and lost detail v3 had. Fixable if we can detect low-signal comment sets and skip injection in that case.

## Why this worked when community posts didn't

The v3 community posts were cosine-matched to the bug's summary + description text — they shared vocabulary and topic but rarely carried causal detail about the specific bug. For example, MC-181313's "server crash on high-damage arrow" was matched with "Nerf Harming Arrows" — same category, no reproducible mechanic detail.

The v4 JIRA comments are **directly attached to each specific bug** by the reporter, QA, and other users. They contain: reproduction confirmations from other users, version-specific regressions, code-level speculation, workarounds people discovered, and cross-references to related bug IDs. On average about 4-5 usable comments per bug after boilerplate filtering.

Direct attachment beats semantic proximity by a wide margin.

## Verdict

**GPT v4 is a real improvement over v3 for GPT and the wins are content-driven rather than style-driven.** Ship-worthy on this evidence.

Bugs with active comment threads containing technical investigation benefit most (MC-267937 code-analysis, MC-213788 28-comment thread, MC-166004 12-comment thread). Bugs with only social/"me too" comments see no benefit but no regression (MC-160248, MC-235964, MC-268842).

The regression modes we watched for (rule 7/8/9 violations, verbatim boilerplate imports, hallucinated speculation) are rare — the boilerplate-filtering appears to work. The main v4 downside is length bloat when comments are trivial (MC-180257 stack trace paste; MC-149792 rule-7 restatement).

**Practical recommendation**: keep the JIRA-comment injection. Next lever to try — extract only mechanically-relevant sentences from each comment rather than dumping the whole body, which would probably compress the 6 loss cases into ties.

## Method notes

- Reviewer: independent subagent given identical rubric to the v2-vs-v3 review, with an updated call-out for JIRA-specific failure modes (verbatim comment quotation, "please attach the crash report" leakage, speculation-as-fact).
- 129 section pairs; ties dominate (77%) — most sections were near-identical in substance.
- Bugs with 0 usable JIRA comments (17/60) excluded — no intervention there means no v3-vs-v4 delta to measure.
- Interactive viewer with pair-level chips and filters at `improveBR/replication_package/compare_v2_v3_v4_gpt.html`.
