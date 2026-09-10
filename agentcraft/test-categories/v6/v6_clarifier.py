"""
v6 — Executable S2R generation via router + clarifier.

Adapted from the user's research script. Both router and clarifier run on
gpt-5.6-sol via the Responses API. The router decides whether external web
verification is warranted; only then does the clarifier get the web_search tool.

Input : /Users/nish/Documents/Research - Minecraft/data_collection/test-bug-panel/Commands/<MC-XXX>/*.md
Output: agentcraft/test-categories/v6/Commands/<MC-XXX>/
          - original .json / .md          (preserved)
          - text attachments               (preserved; media excluded)
          - MC-XXX_s2r.md                  (clarifier output, human-readable)
          - MC-XXX_s2r.json                (clarifier output + routing metadata)
        plus a run-level JSONL research log.
"""

from openai import OpenAI
from datetime import datetime, timezone
from pathlib import Path
import json, os, sys, time, shutil

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

MODEL = "gpt-5.6-sol"

# OPENAI_API_KEY_V6 is the key this run used; OPENAI_API_KEY is the portable
# fallback so the script runs anywhere without editing.
_KEY = os.environ.get("OPENAI_API_KEY_V6") or os.environ.get("OPENAI_API_KEY")
if not _KEY:
    sys.exit("set OPENAI_API_KEY (or OPENAI_API_KEY_V6)")

client = OpenAI(api_key=_KEY, timeout=300.0, max_retries=2)


# ============================================================
# 1. ROUTER
# ============================================================

ROUTER_INSTRUCTIONS = """
You are a verification router for a Minecraft Java Edition
bug-reproduction system.

Your ONLY task is to determine whether external web verification
is necessary before another LLM converts the supplied bug report
into executable reproduction instructions.

Return EXACTLY one of:

NEED_WEB
NO_WEB

Return NEED_WEB only when at least one of these conditions applies:

1. The answer depends on Minecraft-version-specific command syntax
   that is not clearly established by the supplied bug report.

2. The report contains a command, item, entity, NBT structure,
   datapack feature, advancement trigger, UI location, game mechanic,
   or configuration whose behavior in the affected version is uncertain.

3. A reproduction step depends on technical information that is
   missing from the supplied bug report.

4. There is a meaningful risk of accidentally using modern Minecraft
   behavior or syntax for an older affected version.

5. The user explicitly asks for external verification.

6. Resolving an ambiguity is necessary before the reproduction
   instructions can safely be executed by another LLM agent.

Return NO_WEB when:

- the bug report already contains enough information;
- the question asks for a simple explanation of a supplied step;
- the information is basic Minecraft interaction knowledge;
- the answer can be derived directly from the supplied report;
- external information would only add optional background.

Do not explain your decision.
Return only NEED_WEB or NO_WEB.
"""


# ============================================================
# 2. CLARIFIER
# ============================================================

CLARIFIER_INSTRUCTIONS = """
You are the Reproduction Clarifier in an automated Minecraft Java
Edition bug-reproduction research system.

Your output will NOT primarily be read by a human.

Your instructions will be passed to another LLM agent that must
execute the reproduction inside Minecraft.

Therefore, convert the supplied Mojira bug report into an explicit,
grounded, executable reproduction procedure.

============================================================
PRIMARY OBJECTIVE
============================================================

Produce the smallest deterministic sequence of actions that allows
an execution agent to reproduce and verify the reported buggy behavior.

The Mojira report is the primary source of truth.

Do not improve, reinterpret, or modernize the reported procedure
unless necessary.

============================================================
GROUNDING RULES
============================================================

1. Preserve the affected Minecraft version.

2. Preserve commands, coordinates, entity names, item names,
   advancement identifiers, NBT, datapack names, settings, and
   numerical values exactly when supplied.

3. Never silently replace historical Minecraft syntax with modern
   syntax.

4. Distinguish clearly between:

   - prerequisites
   - setup
   - trigger actions
   - normal intermediate behavior
   - expected behavior
   - actual buggy behavior
   - verification evidence

5. Do not invent missing requirements.

6. If you introduce a practical recommendation that is not stated
   in the bug report, mark it explicitly as:

   PRACTICAL_ASSUMPTION

7. If web search is available, use it only when version-specific
   technical verification is necessary.

8. When web search is used, prefer authoritative Minecraft sources,
   especially:

   - bugs.mojang.com
   - minecraft.net
   - minecraft.wiki

9. Do not let external sources override an explicit fact from the
   supplied Mojira report unless there is a clear contradiction.
   If a contradiction exists, state it.

============================================================
EXECUTABILITY RULES
============================================================

Assume the downstream execution agent does not understand implicit
human instructions.

Translate actions into concrete game operations.

For example:

"enter the Nether"

must become something such as:

- verify player is in Overworld
- obtain/build Nether portal if required
- ignite portal
- move player into portal
- wait for dimension transition
- verify Nether environment is loaded

"put the book in the hotbar"

must become:

- open inventory
- locate the required book
- move it into one of the nine hotbar slots
- close inventory
- select that slot
- verify book is held in main hand

"use the item"

must specify:

- which item
- which hand
- which button/input
- whether to click or hold
- duration or stopping condition
- when to release

"look up and down"

must specify:

- required player/camera location
- camera motion
- what rendering change is being searched for

"run command"

must specify:

- exact command
- dimension/location prerequisites
- expected immediate result

"spawn six entities"

must specify an exact reproducible mechanism.

============================================================
MINIMALITY
============================================================

Prefer the simplest valid reproduction.

Do not make the execution agent reproduce every variant mentioned
in a large historical Mojira report when a single deterministic
variant is enough to establish the bug.

Choose the easiest observable instance unless the report explicitly
requires comparison across multiple cases.

============================================================
BUG VERIFICATION
============================================================

The most important task is identifying what proves that the bug
has actually occurred.

Do not confuse setup behavior with buggy behavior.

Examples:

If an animal makes a hurt sound correctly but a player attack
subtitle is missing, the animal subtitle is NOT the bug.

If TNT launches a player correctly but an advancement fails,
the launch itself is NOT the bug.

If an entity moves correctly but visually snaps instead of
interpolating, movement is NOT the bug; lack of interpolation is.

If a command matches six entities but changes only one, distinguish:

SELECTOR_MATCH_COUNT
ACTUAL_AFFECTED_COUNT
DISPLAYED_FEEDBACK_COUNT

If an invalid value causes an exception, distinguish the invalid
input from the actual observable exception or log spam.

============================================================
STATE-BASED REASONING
============================================================

Represent important transitions conceptually as:

PRECONDITION
    ->
ACTION
    ->
INTERMEDIATE_STATE
    ->
EXPECTED_STATE
    ->
OBSERVED_BUG_STATE

Determine exactly which transition demonstrates the defect.

============================================================
FOLLOW-UP CLARIFICATION
============================================================

If the user asks about one specific reproduction step, such as:

"how to do this?"
"how do I enter the Nether?"
"how do I put it in my hotbar?"
"what should I see?"
"what is the buggy behavior?"

answer ONLY that part.

Expand the requested step into more primitive executable actions.

Do not regenerate the entire reproduction procedure unless required.

============================================================
OUTPUT FORMAT
============================================================

For a complete bug report, use this structure:

BUG_ID:
AFFECTED_VERSION:

BUG_BEHAVIOR:
One concise explanation of the actual defect.

PRECONDITIONS:
Concrete environment and game-state requirements.

SETUP:
Numbered executable setup actions.

REPRODUCTION_STEPS:
Numbered chronological actions.

For every command, include the exact command in a code block.

After important actions provide:

VERIFY:
What the execution agent should observe before continuing.

EXPECTED_BEHAVIOR:
What Minecraft should have done.

OBSERVED_BUG_BEHAVIOR:
What demonstrates the defect.

SUCCESS_CONDITION:
A concise machine-checkable or visually-checkable condition that
means reproduction succeeded.

FAILURE_OR_AMBIGUITY:
Only include this section if the supplied information does not
allow reliable reproduction.

============================================================
STYLE
============================================================

Be explicit.
Be concise.
Use deterministic instructions.
Avoid unnecessary explanation.
Avoid unexplained Minecraft terminology.
Do not use emojis.
Do not use em dashes.

The procedure must be detailed enough for an autonomous LLM agent
to execute without asking a human what an instruction means.
"""


# ============================================================
# 3. WEB-VERIFICATION ROUTER
# ============================================================

def determine_web_requirement(bug_report: str, user_question: str | None = None) -> dict:
    user_question = user_question or "Generate the complete reproduction procedure."

    response = client.responses.create(
        model=MODEL,
        reasoning={"effort": "low"},
        instructions=ROUTER_INSTRUCTIONS,
        input=f"""
MINECRAFT BUG REPORT
====================
{bug_report}

REQUEST
=======
{user_question}
""",
    )

    raw_decision = response.output_text.strip().upper()

    if raw_decision == "NEED_WEB":
        need_web = True
    elif raw_decision == "NO_WEB":
        need_web = False
    else:
        # Conservative fallback for research reliability.
        need_web = True

    return {
        "need_web": need_web,
        "router_output": raw_decision,
        "router_response_id": response.id,
    }


# ============================================================
# 4. MAIN CLARIFICATION PIPELINE
# ============================================================

def clarify_minecraft_bug(bug_report: str, user_question: str | None = None) -> dict:
    user_question = user_question or "Generate a complete executable reproduction procedure."

    # Stage 1: decide whether external verification is needed.
    routing = determine_web_requirement(bug_report=bug_report, user_question=user_question)

    # Stage 2: give web access ONLY if the router approved it.
    request_args = {
        "model": MODEL,
        "reasoning": {"effort": "medium"},
        "instructions": CLARIFIER_INSTRUCTIONS,
        "input": f"""
MINECRAFT BUG REPORT
====================
{bug_report}

CURRENT REQUEST
===============
{user_question}

WEB VERIFICATION STATUS
=======================
{"AVAILABLE - use only when technically necessary."
 if routing["need_web"]
 else "NOT AVAILABLE - derive the answer from the supplied report and established game interaction knowledge."}
""",
    }

    if routing["need_web"]:
        request_args["tools"] = [{"type": "web_search"}]
        request_args["tool_choice"] = "auto"

    response = client.responses.create(**request_args)

    used_web_search = any(
        getattr(item, "type", None) == "web_search_call" for item in response.output
    )

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "routing": {
            "need_web": routing["need_web"],
            "router_output": routing["router_output"],
            "router_response_id": routing["router_response_id"],
        },
        "generation": {
            "model": MODEL,
            "reasoning_effort": "medium",
            "web_available": routing["need_web"],
            "web_actually_used": used_web_search,
            "response_id": response.id,
        },
        "answer": response.output_text,
    }


# ============================================================
# 5. RESEARCH LOGGER
# ============================================================

def save_research_result(result: dict, filename: str):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(json.dumps(result, ensure_ascii=False) + "\n")


# ============================================================
# 6. BATCH RUNNER — one category
# ============================================================

SRC_ROOT = Path("/Users/nish/Documents/Research - Minecraft/data_collection/test-bug-panel")
V6_ROOT  = Path("/Users/nish/Documents/agentcraft/agentcraft/test-categories/v6")

TEXT_ATTACH_EXT = {".log", ".txt", ".nbt", ".java", ".json"}

USER_QUESTION = (
    "Generate instructions detailed enough for another LLM Minecraft agent "
    "to execute and verify this bug."
)


def process_category(category: str):
    src = SRC_ROOT / category
    dst = V6_ROOT / category
    dst.mkdir(parents=True, exist_ok=True)

    log_path = dst / "_research_log.jsonl"
    bug_dirs = sorted([p for p in src.iterdir() if p.is_dir()])

    print(f"[{category}] {len(bug_dirs)} bugs")
    stats = {"need_web": 0, "web_used": 0, "ok": 0, "failed": 0}

    for i, bug_dir in enumerate(bug_dirs, 1):
        bug_id = bug_dir.name
        md_files = list(bug_dir.glob("*.md"))
        if not md_files:
            print(f"  [{i}/{len(bug_dirs)}] {bug_id}: SKIP (no .md)")
            stats["failed"] += 1
            continue

        bug_report = md_files[0].read_text(encoding="utf-8")
        target = dst / bug_id
        target.mkdir(parents=True, exist_ok=True)

        # --- preserve original data (text only; media excluded) ---
        for f in bug_dir.iterdir():
            if f.is_file() and f.suffix.lower() in {".json", ".md"}:
                shutil.copy2(f, target / f.name)
        att_src = bug_dir / "attachments"
        if att_src.is_dir():
            kept = [f for f in att_src.iterdir()
                    if f.is_file() and f.suffix.lower() in TEXT_ATTACH_EXT]
            if kept:
                att_dst = target / "attachments"
                att_dst.mkdir(exist_ok=True)
                for f in kept:
                    shutil.copy2(f, att_dst / f.name)

        # --- run router + clarifier ---
        t0 = time.time()
        try:
            result = clarify_minecraft_bug(bug_report=bug_report, user_question=USER_QUESTION)
        except Exception as e:
            print(f"  [{i}/{len(bug_dirs)}] {bug_id}: ERROR {type(e).__name__}: {e}")
            stats["failed"] += 1
            continue

        elapsed = time.time() - t0
        result["bug_id"] = bug_id
        result["category"] = category
        result["source_md"] = md_files[0].name
        result["elapsed_seconds"] = round(elapsed, 2)

        # --- write outputs ---
        (target / f"{bug_id}_s2r.md").write_text(result["answer"], encoding="utf-8")
        (target / f"{bug_id}_s2r.json").write_text(
            json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        save_research_result(result, str(log_path))

        stats["ok"] += 1
        if result["routing"]["need_web"]:
            stats["need_web"] += 1
        if result["generation"]["web_actually_used"]:
            stats["web_used"] += 1

        print(
            f"  [{i}/{len(bug_dirs)}] {bug_id}: {result['routing']['router_output']}"
            f" web_used={result['generation']['web_actually_used']}"
            f" {len(result['answer'].split())}w {elapsed:.1f}s"
        )

    print(f"[{category}] done — ok={stats['ok']} failed={stats['failed']} "
          f"NEED_WEB={stats['need_web']}/{stats['ok']} web_actually_used={stats['web_used']}")
    return stats


if __name__ == "__main__":
    cat = sys.argv[1] if len(sys.argv) > 1 else "Commands"
    process_category(cat)
