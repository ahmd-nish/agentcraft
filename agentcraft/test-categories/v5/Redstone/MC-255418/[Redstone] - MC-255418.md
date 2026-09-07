# MC-255418: Vertical redstone dust placed against dropper/dispenser/hopper doesn't visually disappear when the dust above is removed

**Mojira URL:** [https://bugs.mojang.com/browse/MC-255418](https://bugs.mojang.com/browse/MC-255418)

## Report details

- **Mojira categories:** Block states; Redstone
- **Project:** MC
- **Issue key:** MC-255418
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-08-22T01:04:42.146-0700
- **Updated:** 2025-04-11T12:40:15.153-0700
- **Resolution date:** 2023-09-05T06:32:45.521-0700
- **Affects versions:** 1.19.2; 1.20 Release Candidate 1; 1.20
- **Fix versions:** 1.20.2 Pre-release 1
- **Area:** Platform
- **Labels:** bug; client-side; redstone; redstone-circut; redstone-dust; redstone-wire; rendering; rendering-bug; vertical
- **Watchers:** 1
- **Attachments:** 16
- **Attachment filenames:** 2022-08-22_08.16.50.png; 2022-08-22_08.19.47.png; 2022-08-22_08.24.56.png; 2022-08-22_08.29.36.png; 2022-08-22_08.31.27.png; 2022-08-22_08.38.21.png; 2022-08-22_08.40.02.png; 2022-08-22_08.42.21.png; 2022-08-22_08.45.13.png; 2022-08-22_08.48.39.png; 2022-08-22_08.48.43.png; 2022-08-22_08.51.25.png; 2022-08-22_08.51.28.png; 2022-08-22_08.56.36.png; 2022-08-22_09.01.55.png; weirdRedstoneBehaviour.mp4
- **Issue links:** Duplicate:inward:MC-264810:Visual Vertical Redstone Glitch using Hoppers | Relates:outward:MC-264809:Redstone comparators cause redstone dust connection issue | Duplicate:inward:MC-263098:Redstonedust being shown connected to wrong sides.

## Description

When you place redstone dust against a dropper or dispenser while that same piece of dust is being redirected and powered(as seen below),

if the top piece of redstone dust is broken, the vertical piece of dust still shows.
Even weirder is that if the dispenser is removed the vertical dust still displays:
Once the block has been removed another can be put in it's place creating some interesting situations:
This is entirely visual and client-side only as the dust doesn't actually power anything(like a redstone lamp).
A re-log or a block update(e.g placing a target block next to the other side of the redstone) fixes this issue and returns the dust to the expected state.
As far as I have tested this only happens on dispenser, droppers and hoppers although the hopper behaves slightly differently as it isn't a solid block.
When the layout of blocks is placed with a hopper instead of a dropper the redstone redirects into the hopper:
and then when the dust is removed it remains redirected into the hopper:
A strange behaviour occurs on the player's F3 screen too. After making the redstone do this to the hopper, the F3 screen displays "enabled: false" yet it still picks up items:
After a look in the hopper's gui it updates and returns to correctly display that it is "enabled: false":

The F3 screen for the wire also displays that it is facing up:

Weirdly this only occurs when the redstone is powered. If the same setup is built but without power the redstone dust doesn't display vertically.

Also, if the redstone power is removed after the redstone has been glitched it will return to the expected state (as this is a block update for the redstone).

Similarly this does not occur without the redirection of the redstone:

Here is a short video of the setup:

 I have only tested this in 1.19.2 but it might exist in previous versions as well.

## Comments (1)

### Comment 1: migrated (2022-08-22T01:04:42.146-0700)

This comment contained multiple image attachments (16), please login to view the attachments.
