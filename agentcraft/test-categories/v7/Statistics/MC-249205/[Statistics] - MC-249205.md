# MC-249205: "minecraft.used:minecraft.potion" increases by a value of two when using water bottles to create mud in creative mode

**Mojira URL:** [https://bugs.mojang.com/browse/MC-249205](https://bugs.mojang.com/browse/MC-249205)

## Report details

- **Mojira categories:** Statistics
- **Project:** MC
- **Issue key:** MC-249205
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2022-03-17T12:29:57.077-0700
- **Updated:** 2025-09-02T01:23:53.387-0700
- **Resolution date:** 2025-09-02T01:23:53.333-0700
- **Affects versions:** 22w11a; 22w12a; 22w13a; 22w14a; 22w15a; 22w17a; 22w18a; 1.19 Pre-release 1; 1.19 Release Candidate 2; 1.19; 1.19.1; 1.19.2; 22w45a; 1.19.3; 1.19.4; 1.20.1; 1.21; 1.21.3; 24w45a; 1.21.4
- **Fix versions:** 25w36a
- **Area:** Platform
- **Game mode:** Creative
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** MC-249205.mp4; MC-249205 - Creative Mode Behavior.png; MC-249205 - Survival Mode Behavior.png
- **Issue links:** Duplicate:inward:MC-273932:"Times Used" statistic for watter bottles increases by 2 when converting dirt to mud in creative

## Description

The Bug:
"minecraft.used:minecraft.potion" increases by a value of two when using water bottles to create mud in creative mode.
Steps to Reproduce:
- Create a scoreboard objective for tracking the use of a water bottle and set it to display on the sidebar by using the commands provided below.

```
/scoreboard objectives add UseWaterBottle minecraft.used:minecraft.potion
```

```
/scoreboard objectives setdisplay sidebar UseWaterBottle
```

- Switch into creative mode, place down some dirt, and obtain a water bottle.

- Use the water bottle on the dirt to convert it into mud.

- Take note as to whether or not "minecraft.used:minecraft.potion" increases by a value of two when using water bottles to create mud in creative mode.

Observed Behavior:
The scoreboard increases by a value of two.
Expected Behavior:
The scoreboard would increase by a value of one, just like in survival mode.

## Comments (1)

### Comment 1: migrated (2022-03-17T12:29:57.077-0700)

This comment contained multiple image attachments (3), please login to view the attachments.
