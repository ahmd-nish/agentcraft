# agentcraft

Enhanced Minecraft bug reports produced by the ImproBR pipeline.

## Iterations
- **[v1](./v1)** — 60 bug reports enhanced by GPT-4o-mini and Qwen2.5-32B-Instruct (Q4_K_M) using the v13 prompt set.
- **[v2](./v2)** — same 60 reports, same models, with two fixes: preprocessor cleaner now preserves Minecraft-command characters (`@ ~ / $ ^ =`), and the Observed Behavior prompt tightened with rules 7-9 (no S2R restatement, no QA-workflow bleed, no meta-comment endings). v1 had ~two-thirds of reports fed to the LLMs with commands corrupted by the preprocessor.
- **[v3](./v3)** — same 60 reports, same GPT-4o-mini and Qwen, same v13+v14 prompts. New: **community-post context** from Minecraft Feedback (cosine >= 0.70 semantic matches, post_created_at >= bug_created_at) injected into the S2R / OB / EB user prompts. 51 of 60 bugs receive community context (9 have no matches above threshold); 648 posts total. Primary comparison is v2 vs v3 — same model / prompts / inputs, only community context differs. Manual eval ([`v3/EVAL_v2_vs_v3.md`](./v3/EVAL_v2_vs_v3.md)) found the effect was **near-neutral** on both models.
- **[v4](./v4)** — same 60 reports, same models. Adds **JIRA-comment injection** on top of v3's community-post block. Directly-attached Mojang bug-tracker comments carry much higher signal than cosine-matched community posts (reproduction confirmations, version-specific regressions, code-level speculation, workarounds). 43 of 60 bugs have ≥1 usable JIRA comment (203 comments total after boilerplate filtering). Manual eval ([`v4/EVAL_v3_vs_v4_gpt.md`](./v4/EVAL_v3_vs_v4_gpt.md)) shows GPT v4 is a **real improvement** over v3 — 24 v4-wins vs 6 v3-wins across 129 section pairs (v3-vs-v4 GPT), 4:1 where a difference exists.
