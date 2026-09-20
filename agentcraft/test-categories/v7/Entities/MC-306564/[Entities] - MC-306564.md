# MC-306564: Item entities' health does not decrease uniformly when on cacti

**Mojira URL:** [https://bugs.mojang.com/browse/MC-306564](https://bugs.mojang.com/browse/MC-306564)

## Report details

- **Mojira categories:** Entities; Items
- **Project:** MC
- **Issue key:** MC-306564
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2026-02-22T02:18:40.412-0800
- **Updated:** 2026-03-11T03:45:26.113-0700
- **Resolution date:** 2026-03-11T03:44:49.374-0700
- **Affects versions:** 26.1 Snapshot 9
- **Fix versions:** 26.1 Pre-Release 2
- **Area:** Platform HC
- **Watchers:** 2
- **Attachments:** 1
- **Attachment filenames:** 2026-02-22 17-53-04 (747f90a5-6e56-47bb-90fe-f342d494d291).mp4

## Description

Short description
When an item entity is summoned on a cactus and the game is tick stepped, its health decreases irregularly instead of uniformly to 0 within the expected 5 ticks.
Steps to reproduce
- Freeze the game with /tick freeze.

- Summon an item entity at a specific position on a cactus (e.g., using /summon minecraft:item ~ ~ ~ {Item:{count:1,id:"minecraft:sand"},PickupDelay:40}). Ensure the cactus is placed so that the item spawns in contact with it (e.g., directly above or inside the cactus block).

- Check the item's health using a command like /execute as @e[type=item,distance=..5] run data get entity @s Health.

- Step forward 5 ticks with /tick step 5.

- Repeat steps 3–4 multiple times (e.g., up to 15 ticks total).

Expected result
The item entity's health should decrease uniformly from 5 to 0 over the course of 5 ticks, and the entity should be removed (due to cactus damage) after 5 ticks.
Actual result
- Initially, the item entity has health 5.

- After 5 ticks, health is 3 (decrease of 2).

- After 10 ticks, health is around 1–2 (decrease of 1–2 from previous, not consistent).

- After 15 ticks, some entities have health 1, while others have already been removed (deleted).

The health decrease is not uniform, and the removal timing is inconsistent across entities.

## Comments (1)

### Comment 1: Automation for Jira (2026-02-22T02:18:51.711-0800)

Thank you for helping us improve Minecraft! We saved your files:
