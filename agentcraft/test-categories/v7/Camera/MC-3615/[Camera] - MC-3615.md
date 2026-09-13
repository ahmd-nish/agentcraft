# MC-3615: Lava and water are completely transparent at certain height levels

**Mojira URL:** [https://bugs.mojang.com/browse/MC-3615](https://bugs.mojang.com/browse/MC-3615)

## Report details

- **Mojira categories:** Camera; Rendering
- **Project:** MC
- **Issue key:** MC-3615
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2012-11-21T06:33:25.528-0800
- **Updated:** 2025-10-26T01:31:57.870-0700
- **Resolution date:** 2022-08-17T11:48:37.380-0700
- **Affects versions:** Minecraft 1.4.4; Minecraft 1.4.5; Minecraft 1.4.7; Minecraft 1.5; Minecraft 1.6.2; Minecraft 1.7.4; Minecraft 14w08a; Minecraft 1.7.5; Minecraft 14w10c; Minecraft 14w11b; Minecraft 1.7.9; Minecraft 14w17a; Minecraft 14w18b; Minecraft 14w19a; Minecraft 14w20a; Minecraft 14w20b; Minecraft 14w21b; Minecraft 1.10.2; Minecraft 16w32a; Minecraft 16w32b; Minecraft 16w33a; Minecraft 16w35a; Minecraft 1.11.1; Minecraft 18w07c; Minecraft 1.13-pre6; Minecraft 1.14.2; 1.15.2; 20w06a; 20w08a; 20w22a; 1.16 Pre-release 3; 1.16 Pre-release 4; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w27a; 20w28a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Release Candidate 1; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4 Pre-release 1; 1.16.4 Pre-release 2; 1.16.4 Release Candidate 1; 1.16.4; 20w45a; 20w46a
- **Fix versions:** Minecraft 14w25b; 20w48a
- **Game mode:** Creative
- **Labels:** lava; visibility
- **Watchers:** 2
- **Attachments:** 14
- **Attachment filenames:** 2012-11-10_22.19.06.png; 2012-11-10_22.19.13.png; 2012-11-19_19.09.35.png; 2014-03-02_11.47.11.png; 2014-03-02_11.47.14.png; 2014-03-09_13.26.01.png; 2014-06-22_20.57.01.png; 2020-06-23_01.45.08.png; 2020-11-25_17.56.22.png; 2020-11-25_18.06.18.png; 2020-11-25_18.31.01.png; 2020-11-25_18.32.20.png; 2022-03-09_22.24.11.jpg; 2022-03-16_17.41.05.png
- **Issue links:** Relates:inward:MC-166546:The environment is rendered blue when player is outside water surface | Relates:inward:MC-206610:At certain camera angles around -25.4 in second person, the lava fog effect applies when it shouldn't | Cloners:inward:MC-206561:Water is still completely transparent at certain height levels | Cloners:inward:MC-206842:Lava is still briefly transparent at a specific height level | Relates:outward:MCPE-6965:Lava and water can visually disappear in a certain condition

## Description

The bug
When standing so that the player is just inside lava (a very small range), it is possible to see through it (third screenshot). This also occurs when the player's head is back against a block and touching a block above it in flowing lava that is next to a source block (first two screenshots).
How to reproduce
No surface and no tint
- Switch to Creative mode and start flying

- Use the following commands

```
/setblock ~ 64 ~ lava
```

```
/tp ~ 62.39 ~
```

- Start looking up and down
→ At some point you will see no bottom surface but also no tint

Surface and tint
- Switch to Creative mode and start flying

- Use the following commands

```
/setblock ~ 64 ~ water
```

```
/tp ~ 63.39 ~
```

- Start looking up and down
→ At some point you will see the top surface and the tint

## Comments (40)

### Comment 1: migrated (2012-11-21T06:33:25.528-0800)

This comment contained multiple image attachments (14), please login to view the attachments.

### Comment 2: migrated (2012-11-22T15:51:29.756-0800)

Confirmed.

### Comment 3: migrated (2013-02-04T14:52:45.535-0800)

You shouldn't mark MC-965 as a duplicate, it's an earlier bug report.

### Comment 4: Ezekiel (2014-01-26T07:42:52.833-0800)

Is this still a concern in the latest Minecraft version 14w04b? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 5: migrated (2014-02-07T18:01:22.193-0800)

are you in  flowing lava in the third picture? Because you can see through flowing lava but not solid lava.

### Comment 6: migrated (2014-02-10T13:55:20.400-0800)

In the latest snapshot (currently 14w06b), I can see through lava without the haze in ANY circumstance, but I think that has to do with the new Spectator mode.

### Comment 7: kumasasa (2014-03-02T03:02:00.319-0800)

The clear/reddish effect doesn't correspond with the eye level. If the head is already above but the eyes (red line in collision box) still below the lava surface, the vision is clear.

### Comment 8: migrated (2014-03-09T05:26:35.264-0700)

Confirmed for 10c

### Comment 9: migrated (2014-03-15T14:31:19.773-0700)

Confirmed for 14w11b

### Comment 10: migrated (2014-04-26T02:02:33.798-0700)

Confirmed for 14w17a

### Comment 11: migrated (2014-05-02T08:52:33.617-0700)

Confirmed for 14w18b

### Comment 12: migrated (2014-05-08T08:17:36.453-0700)

Confirmed for 14w19a.

### Comment 13: migrated (2014-05-15T11:37:22.096-0700)

Confirmed for 14w20a and b.

### Comment 14: migrated (2014-05-22T10:08:03.388-0700)

Confirmed for 14w21b.

### Comment 15: kumasasa (2014-06-22T11:57:42.779-0700)

Fixed in 14w25b

### Comment 16: migrated (2014-06-22T12:01:23.087-0700)

yes

### Comment 17: migrated (2016-03-13T12:11:27.782-0700)

reopening because of MC-99595

### Comment 18: FaRo1 (2016-07-01T08:51:06.977-0700)

This also affects water, which is MC-1499, but MC-1499 is claimed as fixed although it isn't. As visible in that one, it also works the other way around (underwater view for over water).

### Comment 19: muzikbike (2018-07-06T05:40:37.433-0700)

Am only able to reproduce the "above lava but underneath lava effect is visible" effect in 1.13-pre6.

### Comment 20: migrated (2020-06-08T06:16:13.225-0700)

Affects  1.16 pre release 2

### Comment 21: migrated (2020-06-22T15:47:37.058-0700)

Being inside lava but it is completely transparent.  1.16 rc 1
EDIT: Removed image.

### Comment 22: migrated (2020-06-26T09:08:50.546-0700)

Affects also 1.16 and 1.16.1

### Comment 23: migrated (2020-07-02T07:38:03.501-0700)

Still happens in 20w27a

### Comment 24: migrated (2020-09-14T08:54:40.644-0700)

If this is fixed, it will be VERY hard to build under lava because of the short vision range. I suggest that Mojang also make the fire resistance effect extend the vision range more for higher levels. Eg. at level 1 fire resistance, you can see an extra block, but at level 255, you can see 255 blocks in lava (or maybe more).

### Comment 25: Sebexan (2020-09-20T04:11:59.723-0700)

It runs on version 1.16.3
The method is used during speedruns when the player is on the boat looking for a fortress or other structures under water.

### Comment 26: [Mod] GoldenHelmet (2020-09-29T17:45:37.135-0700)

A very similar issue in Bedrock Edition is resolved "Won't Fix" (MCPE-6965).

### Comment 27: Sebexan (2020-10-15T10:33:03.349-0700)

Present in 1.16.4 Pre-Release 1

### Comment 28: Sebexan (2020-10-22T10:59:13.118-0700)

Present in 1.16.4 Pre-Release 2

### Comment 29: Sebexan (2020-10-27T10:53:23.793-0700)

Present in 1.16.4 Release Candidate 1

### Comment 30: Sebexan (2020-11-04T11:31:32.675-0800)

Present in 20w45a

### Comment 31: Sebexan (2020-11-11T09:12:35.717-0800)

Present in 20w46a

### Comment 32: migrated (2020-11-17T09:43:07.450-0800)

Way to make that bug in survival
MC-191488

### Comment 33: migrated (2020-11-25T08:46:37.528-0800)

In 20w48a, the fix only applied to lava.

### Comment 34: FaRo1 (2020-11-25T09:33:20.086-0800)

It's actually the opposite now for lava, see
. And it's not even completely fixed, see
. And for water, it's completely unchanged.

### Comment 35: Sebexan (2020-11-25T09:39:42.516-0800)

in 20w48a the lava was partially repaired,
water unchanged
Please reopen it is not 100% fixed

### Comment 36: ItsTinay (2020-11-25T10:04:31.889-0800)

Yea, it is not fully fixed in 20w48a

### Comment 37: [Mod] violine1101 (2020-11-25T10:29:37.298-0800)

Bug report for water in 20w48a →
If you find bugs with how it works now for Lava, please create new bug reports for that as well.

### Comment 38: migrated (2020-11-26T02:18:47.924-0800)

Bug not fixed! I can make it in 20w48a!

### Comment 39: migrated (2020-11-27T10:12:02.039-0800)

@Fabian Röling  describes the issue.

### Comment 40: migrated (2022-03-16T10:02:23.732-0700)

Still happens in lava and water in 1.18.2.
For lava you need to go inside flowing lava.
See comments in  and .
