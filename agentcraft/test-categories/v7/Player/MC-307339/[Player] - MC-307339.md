# MC-307339: The player's vertical motion is reset when moving on the ground

**Mojira URL:** [https://bugs.mojang.com/browse/MC-307339](https://bugs.mojang.com/browse/MC-307339)

## Report details

- **Mojira categories:** Player
- **Project:** MC
- **Issue key:** MC-307339
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2026-04-07T15:35:32.182-0700
- **Updated:** 2026-05-11T06:58:32.244-0700
- **Resolution date:** 2026-05-11T06:58:32.182-0700
- **Affects versions:** 26.2 Snapshot 1
- **Fix versions:** 26.2 Snapshot 7
- **Area:** Platform HC
- **Watchers:** 1
- **Attachments:** 0

## Description

The players y motion is set to 0 every 20 ticks and whenever moving when on ground.
Steps to reproduce:
Output the players y motion using a repeating command block: '/tellraw @p {"nbt":"Motion[1]", "entity":"@p"}'
Stand still then move the camera around, stand still again then move the player around.
Expected:
y motion is a constant value: -0.0784.
Actual:
y motion is set to 0 every 20 ticks or whenever the player moves.

## Comments (0)

No comments were available in the downloaded comment corpus.
