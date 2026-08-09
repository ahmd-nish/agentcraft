# agentcraft

Enhanced Minecraft bug reports produced by the ImproBR pipeline.

## Iterations
- **[v1](./v1)** — 60 bug reports enhanced by GPT-4o-mini and Qwen2.5-32B-Instruct (Q4_K_M) using the v13 prompt set.
- **[v2](./v2)** — same 60 reports, same models, with two fixes: preprocessor cleaner now preserves Minecraft-command characters (`@ ~ / $ ^ =`), and the Observed Behavior prompt tightened with rules 7-9 (no S2R restatement, no QA-workflow bleed, no meta-comment endings). v1 had ~two-thirds of reports fed to the LLMs with commands corrupted by the preprocessor.
- **[v3](./v3)** — same 60 reports, same GPT-4o-mini, same v13+v14 prompts. New: **community-post context** from Minecraft Feedback (cosine >= 0.70 semantic matches, post_created_at >= bug_created_at) injected into the S2R / OB / EB user prompts. 51 of 60 bugs receive community context (9 have no matches above threshold); 648 posts total. Primary comparison is v2 vs v3 — same model / prompts / inputs, only community context differs.
