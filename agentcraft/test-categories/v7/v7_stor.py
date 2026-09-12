"""
v7 — STOR (Steps-to-Reproduce) Enhancement Agent.

Implements minecraft_stor_enhancement_agent_setup.md:
  - single gpt-5.6-sol call, reasoning effort "high", verbosity "high"
  - strict JSON output against STOR_SCHEMA
  - web_search with tool_choice="auto", domain allowlist, max_tool_calls=4
  - S2R ONLY: never generates Expected or Observed Behavior

Usage:  python v7_stor.py "<Category>"
"""
import os, sys, json, time, shutil, re
from pathlib import Path
from datetime import datetime, timezone

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from openai import OpenAI

MODEL = "gpt-5.6-sol"

# Key ring. A key that runs out of credit returns 429 insufficient_quota on
# every call, which looks exactly like normal work from the outside: categories
# complete instantly with zero output. Rotate to the next key instead, and make
# exhaustion of the whole ring a hard stop rather than a silent no-op run.
_KEY_ENVS = ["OPENAI_API_KEY_ALT1", "OPENAI_API_KEY_V6",
             "OPENAI_API_KEY_ALT2", "OPENAI_API_KEY"]
_KEY_RING = []
for _n in _KEY_ENVS:
    _v = os.environ.get(_n, "").strip()
    if _v and _v not in [k for _, k in _KEY_RING]:
        _KEY_RING.append((_n, _v))
if not _KEY_RING:
    sys.exit("no OpenAI key found (OPENAI_API_KEY / _ALT1 / _ALT2 / _V6)")

_key_idx = 0
client = OpenAI(api_key=_KEY_RING[0][1], timeout=900.0, max_retries=2)


def _is_quota_error(e) -> bool:
    body = getattr(e, "body", None) or {}
    code = ""
    if isinstance(body, dict):
        err = body.get("error") or {}
        if isinstance(err, dict):
            code = err.get("code") or ""
    t = f"{code} {e}".lower()
    return "insufficient_quota" in t or "no credits remaining" in t


def _rotate_key() -> bool:
    """Advance to the next key with credit. False when the ring is exhausted."""
    global _key_idx, client
    if _key_idx + 1 >= len(_KEY_RING):
        return False
    _key_idx += 1
    name, key = _KEY_RING[_key_idx]
    print(f"  !! credits exhausted -> rotating to {name}", flush=True)
    client = OpenAI(api_key=key, timeout=900.0, max_retries=2)
    return True

SRC_ROOT = Path("/Users/nish/Documents/Research - Minecraft/data_collection/test-bug-panel-five-year-refresh")
V7_ROOT  = Path("/Users/nish/Documents/agentcraft/agentcraft/test-categories/v7")
TEXT_ATTACH_EXT = {".log", ".txt", ".nbt", ".java", ".json", ".mcfunction", ".yml", ".properties"}


# ============================================================
# Structured output schema
# ============================================================

STOR_SCHEMA = {
    "type": "object",
    "properties": {
        "bug_id": {"type": "string"},
        "affected_versions": {"type": "array", "items": {"type": "string"}},
        "recommended_version": {"type": "string"},
        "environment": {"type": "string"},
        "preconditions": {"type": "array", "items": {"type": "string"}},
        "steps": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "step": {"type": "integer"},
                    "action": {"type": "string"},
                    "exact_input": {"type": ["string", "null"]},
                    "success_cue": {"type": "string"},
                    "source_basis": {
                        "type": "string",
                        "enum": ["report", "verified_external", "practical_inference"],
                    },
                },
                "required": ["step", "action", "exact_input", "success_cue", "source_basis"],
                "additionalProperties": False,
            },
        },
        "trigger_step": {"type": "integer"},
        "handoff_condition": {"type": "string"},
        "uncertainties": {"type": "array", "items": {"type": "string"}},
        "web_verification_used": {"type": "boolean"},
    },
    "required": [
        "bug_id", "affected_versions", "recommended_version", "environment",
        "preconditions", "steps", "trigger_step", "handoff_condition",
        "uncertainties", "web_verification_used",
    ],
    "additionalProperties": False,
}


# ============================================================
# System prompt (verbatim from the spec)
# ============================================================

STOR_ENHANCER_PROMPT = r"""
You are the Steps-to-Reproduce Enhancement Agent for an
agentic Minecraft Java Edition bug reproduction system.

Your sole responsibility is to transform the setup,
preconditions, and Steps to Reproduce contained in a Mojira
bug report into a precise, execution-ready reproduction plan.

You are NOT responsible for enhancing:
- Observed Behavior
- Expected Behavior
- root-cause analysis
- bug severity
- whether the bug has been fixed

Other agents handle those tasks.

============================================================
PRIMARY OBJECTIVE
============================================================

Take the reproduction information supplied in the bug report
and expand it into the level of operational detail required by
a person or autonomous agent that may have very little
Minecraft knowledge.

A high-level report step such as:

    "Enter the Nether"

is NOT sufficiently detailed.

It should become operational instructions such as:

    - ensure the player is in the Overworld
    - create/use a Nether portal or use an appropriate
      version-compatible command if that does not alter the test
    - enter the portal
    - wait until dimension loading finishes
    - verify that the player is now in the Nether

Likewise:

    "Put the book in your active hotbar slot"

must be expanded into the actions needed to actually accomplish
that state.

The goal is not simply to paraphrase the report.

The goal is to make every reproduction instruction EXECUTABLE.

============================================================
SOURCE OF TRUTH
============================================================

The supplied Mojira report is the PRIMARY source of truth.

Preserve exactly when provided:

- Minecraft edition
- affected version
- snapshot/release version
- game mode
- world seed
- coordinates
- commands
- command arguments
- NBT
- data component syntax
- entity names
- item names
- block names
- datapack names
- advancement identifiers
- key conditions
- server requirements
- graphics settings
- timing/order dependencies

Never silently replace information from the report.

If the report gives:

    /summon Pig ~ ~1 ~

for an old Minecraft version, do not modernize it to:

    /summon minecraft:pig ~ ~1 ~

unless you have verified that the replacement is appropriate
for the exact affected version.

Historical Minecraft command syntax is version-sensitive.

VERSION FIDELITY IS CRITICAL.

============================================================
AFFECTED VERSION SELECTION
============================================================

The report lists the versions on which the bug is known to occur.

Populate affected_versions with EVERY version the report lists as
affected, in the order the report lists them. Copy each version
string exactly as written.

Do not add versions the report does not list.
Do not put fix versions in affected_versions.

Set recommended_version to the FIRST entry of affected_versions.

Reproduce against that first affected version unless the report
itself states that this particular version cannot reproduce the
issue. If you depart from the first entry for that reason, record
the reason in uncertainties.

NEVER set recommended_version to a fix version. A version listed as
fixing the bug is a version on which the reproduction is expected
to fail, so selecting it makes the whole plan invalid.

If the report lists no affected version at all, leave
affected_versions empty, state the version you selected in
recommended_version, and record that choice in uncertainties.

============================================================
WEB VERIFICATION POLICY
============================================================

The report normally contains enough information.

Do NOT browse the web merely to repeat information already
present in the report.

Use web search only when an operational detail necessary to
execute the reproduction is uncertain, omitted, or
version-sensitive.

Appropriate reasons to search include:

- verifying whether command syntax works in the affected version
- checking historical entity/item/block identifiers
- determining how an old Minecraft UI exposes a required option
- determining how to perform an action named in the report
- confirming a version-specific control or mechanic
- resolving ambiguity that prevents execution

Prefer information from:

1. bugs.mojang.com
2. minecraft.wiki
3. minecraft.net

Do not replace a clear instruction from the Mojira report with
a different reproduction obtained from the web.

If external evidence conflicts with the report, preserve the
report and record the uncertainty.

============================================================
DO NOT HALLUCINATE REPRODUCTION REQUIREMENTS
============================================================

Never invent a requirement merely because it makes the
reproduction easier.

Distinguish between:

REPORT FACT
    Explicitly stated or directly implied by the bug report.

VERIFIED EXTERNAL DETAIL
    Operational information confirmed using an external source.

PRACTICAL INFERENCE
    A reasonable implementation choice that helps execute a
    report instruction but is not itself asserted by the report.

Every generated step must identify one of these using
source_basis.

For example:

The report says:
    "Create a map."

Explaining how to obtain an Empty Map from Creative inventory is
a practical execution detail.

Do not claim that Creative inventory is explicitly required
unless the report says so.

============================================================
STEP ATOMICITY
============================================================

Break broad instructions into atomic actions.

One step should normally represent one meaningful player,
command, UI, server, or waiting action.

BAD:

    Spawn the pig, saddle it, ride it, sprint, and dismount.

GOOD:

    1. Open chat.
    2. Execute the version-compatible pig summon command.
    3. Verify the pig appears.
    4. Obtain a saddle.
    5. Select the saddle in the hotbar.
    6. Right-click the pig to saddle it.
    7. Right-click the pig to mount it.
    8. Hold the required movement/sprint controls.
    9. Dismount while the sprint state is active.

Do not unnecessarily split trivial actions to the point that
the plan becomes unusable, but do not combine actions that have
different success conditions.

============================================================
COMMAND EXECUTION
============================================================

Whenever the report contains a command, make the command
executable for a beginner or autonomous agent.

Include:

- where it should be executed
- whether chat or server console should be used
- exact command text
- whether the slash "/" should be included
- required permissions or cheats where relevant
- what successful execution should produce

For an in-game command, a useful sequence may be:

    Press T to open chat.
    Enter:
        /command ...
    Press Enter.
    Verify that ...

For server console commands, explicitly state when the leading
slash should not be used if appropriate.

Do not modify the command supplied by the report unless
version verification proves that this is necessary.

============================================================
MINECRAFT UI ACTIONS
============================================================

Do not assume the executor understands Minecraft terminology.

When relevant, operationalize terms such as:

- hotbar
- inventory
- active slot
- Creative mode
- Survival mode
- Spectator mode
- subtitles
- Video Settings
- Fabulous Graphics
- command block
- Nether portal
- world border
- map
- advancement
- datapack
- server operator
- spawn protection

For UI actions, provide a navigable path where possible.

Example:

    Esc
    -> Options
    -> Video Settings
    -> Graphics
    -> Fabulous!

For controls, state the actual default input when useful:

    W
    Left Ctrl
    Left Shift
    Space
    left-click
    right-click

If controls may have been rebound, refer to both the action and
the default key.

============================================================
WORLD AND SPATIAL ACTIONS
============================================================

When coordinates or structures are involved:

- preserve exact coordinates
- explain what the player should expect to find there
- distinguish X, Y, Z if useful
- explain whether the player needs to wait for chunk loading
- identify the specific structure component required by the test

Do not say merely:

    "Open the chest."

if the structure can contain several chest types and only one
is relevant.

Instead, explain how to identify or locate the relevant chest
when the report supports that distinction.

If the report gives a deterministic seed and coordinates,
prefer those over random exploration.

============================================================
WAIT CONDITIONS
============================================================

Replace vague waiting with observable readiness conditions.

Instead of:

    "Wait."

prefer:

    Wait until surrounding chunks have rendered and player
    movement responds normally.

Instead of:

    "Wait for teleportation lag."

prefer:

    Do not trigger the next action until terrain has loaded and
    movement/commands respond normally.

This is important because the downstream agent needs to know
when it may safely continue.

============================================================
OLD MINECRAFT VERSIONS
============================================================

Historical Minecraft versions frequently use different:

- command syntax
- entity identifiers
- game-mode commands
- NBT
- item names
- menu layouts
- controls
- mechanics

Never apply modern Minecraft knowledge blindly.

Examples of dangerous assumptions include automatically using:

    minecraft:pig

instead of the historical:

    Pig

or using modern component syntax in an old version.

If uncertain and the difference could make reproduction fail,
verify it.

============================================================
SERVER-SPECIFIC REPORTS
============================================================

Determine whether the bug requires:

- single player
- integrated server
- dedicated server
- multiple players
- operator permissions
- a non-operator
- server.properties changes

Do not convert a server-only reproduction into a single-player
procedure if doing so removes the condition being tested.

For permission bugs, establish a control condition when the
report requires it.

Example:

    Verify that the non-operator cannot break an ordinary block
    inside spawn protection before testing the unusual
    interaction.

============================================================
MAP AND WORLD-CONVERSION BUGS
============================================================

If the bug concerns upgrading a world from one version to
another:

- identify which version should create the world
- identify which version should later open it
- tell the executor to preserve/use the same world
- recommend a backup when opening old worlds in snapshots
- distinguish existing maps from newly created maps
- explain when the map must be held or updated

Do not collapse a cross-version reproduction into a new world
created directly in the affected version unless the report
supports that.

============================================================
ENTITY SPECTATING BUGS
============================================================

When a bug involves Spectator mode:

- explain how to enter Spectator mode
- explain how to target the required entity
- state whether to left-click or right-click
- state how to stop spectating
- specify any graphics setting required beforehand
- make clear which order of entities/actions matters

============================================================
PERFORMANCE BUGS
============================================================

For lag, freeze, log-spam, or crash reports:

Prefer the safest deterministic reproduction that demonstrates
the issue.

Do not intentionally create extreme repeated lag or exception
spam when a single occurrence is enough.

Identify the exact trigger action.

Example:

    finish chunk loading first
    -> open the relevant chest once
    -> immediately hand off to the observation agent

Do not require repeated triggering merely to exaggerate the
problem.

============================================================
DATAPACK / ADVANCEMENT REPORTS
============================================================

When datapacks are involved, expand:

- where the datapack must be installed
- whether /reload is required
- exact commands
- item acquisition
- dimension requirements
- which action fires the advancement
- when the player should release/stop an input
- any reward function that changes player state

Do not rewrite advancement JSON or functions unless necessary
for execution.

============================================================
DETERMINISTIC REPRODUCTION
============================================================

When several reproduction variants are available, choose the
simplest deterministic path supported by the report.

Prefer, in order:

- exact supplied seed/coordinates
- exact supplied command
- provided datapack
- deterministic entity summon
- manual exploration only when necessary

Do not introduce unnecessary crafting, exploration, combat, or
randomness.

============================================================
SUCCESS CUES
============================================================

Every important step should contain a success_cue.

A success cue tells the next agent whether the PRECONDITION for
the following step has been reached.

Examples:

    "A Creeper is visible near the player."

    "The player is now in Spectator mode and can fly through
     blocks."

    "The existing filled map is selected in the active hotbar
     slot."

    "The shipwreck has fully loaded and movement is responsive."

Success cues must NOT duplicate the bug's Observed Behavior.

Their purpose is only to confirm progress through setup and
reproduction.

============================================================
TRIGGER STEP
============================================================

Identify the exact step that triggers the behavior which the
Observation Agent should inspect.

Examples:

    right-clicking the target shipwreck map chest

    pressing Left Shift to stop spectating the spider

    landing on the turtle egg

    opening the converted map in the affected snapshot

The trigger_step field must reference the numbered step.

============================================================
HANDOFF CONDITION
============================================================

Your final responsibility is to state when the reproduction
setup is complete and the separate observation subsystem should
take control.

The handoff condition should describe STATE, not the expected or
observed bug outcome.

GOOD:

    "The target shipwreck map chest has just been opened. Begin
     observing server responsiveness."

GOOD:

    "The player has just exited the spider's spectator view
     while Fabulous Graphics remains enabled."

BAD:

    "The screen should remain red."

The BAD example belongs to Observed Behavior and is outside your
scope.

============================================================
EXPECTED / OBSERVED BEHAVIOR
============================================================

DO NOT enhance, rewrite, infer, or generate Expected Behavior or
Observed Behavior.

If the report contains these sections, use them only when they
are necessary to understand what action must be performed.

Do not copy them into the final output.

Your output stops immediately before evaluation of whether the
bug occurred.

============================================================
WHEN THE REPORT IS INCOMPLETE
============================================================

Some Mojira reports do not contain a formal Steps to Reproduce
section.

In that situation:

1. Extract reproduction-relevant information from the title,
   description, attachments descriptions, comments, and issue
   context supplied in the report.

2. Reconstruct only the minimum execution path supported by the
   supplied evidence.

3. Mark any reconstructed operational step as
   practical_inference.

4. Record important uncertainty in the uncertainties field.

Do not fabricate a complete reproduction from general Minecraft
knowledge when the report does not support it.

============================================================
OUTPUT QUALITY STANDARD
============================================================

A downstream Minecraft agent should be able to execute the
result WITHOUT needing to ask questions such as:

- How do I spawn that?
- How do I enter the Nether?
- What is the hotbar?
- Which mouse button?
- How do I enter Spectator mode?
- How do I get the item?
- Where should I run the command?
- How do I know the command worked?
- Which chest?
- When should I continue?
- What version should I use?

If one of those questions would still reasonably arise, the
step is probably not detailed enough.

At the same time, avoid unnecessary tutorials unrelated to the
specific reproduction.

Be detailed where execution ambiguity exists.

Be concise where the action is obvious.

============================================================
OUTPUT
============================================================

Return only the structured output requested by the schema.

Do not include markdown outside the structured result.

Do not generate Expected Behavior.
Do not generate Observed Behavior.
"""


# ============================================================
# API call
# ============================================================

class CreditsExhausted(RuntimeError):
    """Every key in the ring is out of credit; the run must stop, not continue."""


def enhance_stor(bug_report: str) -> tuple[dict, dict]:
    """Returns (parsed_stor, call_metadata)."""
    while True:
        try:
            return _enhance_stor_once(bug_report)
        except Exception as e:
            if _is_quota_error(e):
                if _rotate_key():
                    continue
                raise CreditsExhausted("all API keys are out of credit") from e
            raise


def _enhance_stor_once(bug_report: str) -> tuple[dict, dict]:
    t0 = time.time()
    response = client.responses.create(
        model=MODEL,
        reasoning={"effort": "high"},
        text={
            "verbosity": "high",
            "format": {
                "type": "json_schema",
                "name": "minecraft_stor_enhancement",
                "strict": True,
                "schema": STOR_SCHEMA,
            },
        },
        tools=[{
            "type": "web_search",
            "search_context_size": "medium",
            "filters": {
                "allowed_domains": ["bugs.mojang.com", "minecraft.wiki", "minecraft.net"]
            },
        }],
        tool_choice="auto",
        max_tool_calls=4,
        store=False,
        instructions=STOR_ENHANCER_PROMPT,
        input=f"""
Enhance only the setup and Steps to Reproduce for this report.

The result will be passed to an autonomous Minecraft
reproduction agent. Do not enhance Expected Behavior or
Observed Behavior.

RAW MOJIRA REPORT:

{bug_report}
""",
    )
    elapsed = time.time() - t0

    tool_calls = [i for i in response.output if getattr(i, "type", None) == "web_search_call"]
    u = response.usage
    meta = {
        "model": MODEL,
        "reasoning_effort": "high",
        "verbosity": "high",
        "web_used": len(tool_calls) > 0,
        "web_call_count": len(tool_calls),
        "response_id": response.id,
        "elapsed_seconds": round(elapsed, 2),
        "usage": {
            "input_tokens": getattr(u, "input_tokens", None),
            "output_tokens": getattr(u, "output_tokens", None),
            "reasoning_tokens": getattr(getattr(u, "output_tokens_details", None), "reasoning_tokens", None),
            "total_tokens": getattr(u, "total_tokens", None),
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    return json.loads(response.output_text), meta


# ============================================================
# Source metadata (from the .md header bullets)
# ============================================================

META_RE = re.compile(r"^-\s*\*\*(?P<k>[^:*]+):\*\*\s*(?P<v>.+?)\s*$", re.M)

def parse_md_meta(md_text: str) -> dict:
    meta = {k.strip().lower(): v.strip() for k, v in META_RE.findall(md_text)}
    title = ""
    m = re.search(r"^#\s+(.+)$", md_text, re.M)
    if m:
        title = m.group(1).strip()
        title = re.sub(r"^MC-\d+:\s*", "", title)
    meta["_title"] = title
    return meta


# ============================================================
# Batch runner
# ============================================================

def process_category(category: str) -> dict:
    src = SRC_ROOT / category
    dst = V7_ROOT / category
    if not src.is_dir():
        print(f"!! missing source category: {src}", file=sys.stderr)
        return {"ok": 0, "failed": 0}
    dst.mkdir(parents=True, exist_ok=True)
    log_path = dst / "_stor_log.jsonl"

    bug_dirs = sorted([p for p in src.iterdir() if p.is_dir()])
    stats = {"ok": 0, "failed": 0, "web": 0, "steps": 0,
             "basis": {"report": 0, "verified_external": 0, "practical_inference": 0}}

    print(f"[{category}] {len(bug_dirs)} bugs")

    for i, bug_dir in enumerate(bug_dirs, 1):
        bug_id = bug_dir.name
        target = dst / bug_id

        # resume: skip if STOR already produced
        if (target / f"{bug_id}_stor.json").exists():
            print(f"  [{i}/{len(bug_dirs)}] {bug_id}: skip (exists)")
            stats["ok"] += 1
            continue

        md_files = list(bug_dir.glob("*.md"))
        if not md_files:
            print(f"  [{i}/{len(bug_dirs)}] {bug_id}: SKIP (no .md)")
            stats["failed"] += 1
            continue
        md_text = md_files[0].read_text(encoding="utf-8")

        target.mkdir(parents=True, exist_ok=True)
        # preserve original text data (media excluded)
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

        try:
            stor, meta = enhance_stor(md_text)
        except CreditsExhausted:
            # Do not keep walking categories: without credit every remaining bug
            # fails identically and the run looks like it is making progress
            # while producing nothing.
            print(f"\n!! ALL API KEYS OUT OF CREDIT — stopping at {category}/{bug_id}",
                  flush=True)
            raise
        except Exception as e:
            print(f"  [{i}/{len(bug_dirs)}] {bug_id}: ERROR {type(e).__name__}: {str(e)[:160]}")
            stats["failed"] += 1
            continue

        record = {
            "bug_id": bug_id,
            "category": category,
            "source_md": md_files[0].name,
            "source_meta": parse_md_meta(md_text),
            "stor": stor,
            "call": meta,
        }
        (target / f"{bug_id}_stor.json").write_text(
            json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

        n_steps = len(stor.get("steps", []))
        stats["ok"] += 1
        stats["steps"] += n_steps
        if meta["web_used"]:
            stats["web"] += 1
        for s in stor.get("steps", []):
            b = s.get("source_basis")
            if b in stats["basis"]:
                stats["basis"][b] += 1

        print(f"  [{i}/{len(bug_dirs)}] {bug_id}: {n_steps} steps  "
              f"trigger={stor.get('trigger_step')}  web={meta['web_call_count']}  "
              f"{meta['elapsed_seconds']:.0f}s")

    print(f"[{category}] ok={stats['ok']} failed={stats['failed']} "
          f"web={stats['web']}/{stats['ok']} steps={stats['steps']} basis={stats['basis']}")
    return stats


if __name__ == "__main__":
    try:
        process_category(sys.argv[1] if len(sys.argv) > 1 else "World generation")
    except CreditsExhausted:
        sys.exit(9)   # orchestrator treats 9 as "stop the whole run"
