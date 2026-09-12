# MC-257341: Vex texture does not utilize translucency

**Mojira URL:** [https://bugs.mojang.com/browse/MC-257341](https://bugs.mojang.com/browse/MC-257341)

## Report details

- **Mojira categories:** Textures and models
- **Project:** MC
- **Issue key:** MC-257341
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2022-11-09T08:05:45.308-0800
- **Updated:** 2025-04-29T10:59:10.483-0700
- **Resolution date:** 2024-01-23T07:27:36.960-0800
- **Affects versions:** 22w45a; 22w46a
- **Fix versions:** 1.19.3 Pre-release 1
- **Area:** Expansion B
- **Watchers:** 1
- **Attachments:** 8
- **Attachment filenames:** 2022-11-09_15.49.02.png; 2022-11-09_15.59.49.png; 2022-11-09_19.10.36.png; 2022-11-22_14.32.55.png; allay.png; AllayVexTransparent.png; AllayWingVexWing.png; vex.png
- **Issue links:** Relates:outward:MC-251296:Allay has a transparent texture but it is not transparent in game

## Description

The bug
The bottom half of allays use a partially transparent texture to make the body appear to fade out further down. The vex model was updated in 22w45a as to appear much closer to that of the allay, however the same area on the vex appears completely opaque, which is inconsistent with the allay.
The texture file for the vex appears to have this region set to opaque, making this an oversight with the texture itself rather than an issue with rendering.
How to reproduce
-

```
/summon allay ~-1 ~ ~ {NoAI:1}
```

-

```
/summon vex ~1 ~ ~ {NoAI:1}
```

- Examine the ragged-looking region at the bottom of each mob

Expected results
The vex would have a partially transparent lower half as to be consistent with the allay.
Actual results
It does not, resulting in this inconsistency.

## Comments (7)

### Comment 1: migrated (2022-11-09T08:05:45.308-0800)

This comment contained multiple image attachments (8), please login to view the attachments.

### Comment 2: Tinsel (2022-11-09T16:14:31.247-0800)

Can confirm. Allays also utilizes transparency in not only their ghost tails, but also their wings, which the Vex does not

### Comment 3: lipki (2022-11-10T10:14:15.614-0800)

I can confirm that it is enough to modify texture.

### Comment 4: Tinsel (2022-11-16T08:52:16.926-0800)

Can confirm for 22w46a

### Comment 5: Tinsel (2022-11-22T12:28:34.696-0800)

Although this has been fixed for their lower torso, it seems their wings still don't utilize translucency like the Allay. Is this WAI or just a small oversight?

### Comment 6: Tinsel (2022-11-22T16:05:38.986-0800)

Here's a better image of this. Should this be reopened or should I make this it's own, separate bug report?

### Comment 7: migrated (2022-11-22T16:31:32.010-0800)

I'd say separate report.
