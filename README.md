# agentcraft

Enhanced Minecraft bug reports produced by the ImproBR pipeline.

## Iterations
- **[v1](./v1)** — 60 bug reports enhanced by GPT-4o-mini and Qwen2.5-32B-Instruct (Q4_K_M) using the v13 prompt set.
- **[v2](./v2)** — same 60 reports, same models, with two fixes: preprocessor cleaner now preserves Minecraft-command characters (`@ ~ / $ ^ =`), and the Observed Behavior prompt tightened with rules 7-9 (no S2R restatement, no QA-workflow bleed, no meta-comment endings). **Use v2 for evaluation** — v1 had ~two-thirds of reports fed to the LLMs with commands corrupted by the preprocessor.
