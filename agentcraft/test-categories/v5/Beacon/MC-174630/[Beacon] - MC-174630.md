# MC-174630: The secondary beacon effect remains when switching the primary effect

**Mojira URL:** [https://bugs.mojang.com/browse/MC-174630](https://bugs.mojang.com/browse/MC-174630)

## Report details

- **Mojira categories:** Beacon
- **Project:** MC
- **Issue key:** MC-174630
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2020-03-12T08:18:59.646-0700
- **Updated:** 2026-06-10T14:09:19.265-0700
- **Resolution date:** 2026-05-27T00:39:30.726-0700
- **Affects versions:** 1.15.2; 20w11a; 20w18a; 20w20b; 20w22a; 20w51a; 1.16.5; 21w06a; 21w08b; 1.18; 1.20.2; 1.20.4; 24w11a; 1.20.6; 1.21
- **Fix versions:** 26.2 Pre-Release 1
- **Votes:** 1
- **Watchers:** 1
- **Attachments:** 0
- **Issue links:** Relates:inward:MC-2440:Beacons keep higher level effects when partially destroyed | Duplicate:inward:MC-265630:Beacons can give two primary powers at once

## Description

The bug
When you have selected a primary and a secondary effect (that is not regeneration), you can keep that effect even after you switch the primary effect. This allows a beacon to provide two different primary effects.
How to reproduce
- Activate a beacon with a complete pyramid.

```
/fill ~-4 ~-1 ~-4 ~4 ~-4 ~4 minecraft:iron_block
/setblock ~ ~ ~ minecraft:beacon
```

- Select Speed as the primary effect and Speed 2 as the secondary effect

- Change the primary effect to Resistance without changing the secondary effect

- Wait for the Speed 2 effect to run out
 Notice that you have both Speed and Resistance. Note that the beacon interface shows that the secondary effect is deactivated.

Expected behavior
Either the beacon interface should shows that Speed 1 is active as secondary effect, OR the secondary (speed) effect should be removed when setting a different primary effect.

## Comments (3)

### Comment 1: Avoma (2020-12-18T08:41:09.967-0800)

Can confirm in 20w51a.

### Comment 2: Avoma (2021-02-15T02:06:52.644-0800)

Can confirm in 21w06a.

### Comment 3: Avoma (2021-03-01T01:37:19.300-0800)

Can confirm in 1.16.5 and 21w08b.
