# MC-129888: Naturally-generated seagrass and kelp destroys ice

**Mojira URL:** [https://bugs.mojang.com/browse/MC-129888](https://bugs.mojang.com/browse/MC-129888)

## Report details

- **Mojira categories:** World generation
- **Project:** MC
- **Issue key:** MC-129888
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2018-05-18T13:28:12.410-0700
- **Updated:** 2025-04-26T06:36:40.306-0700
- **Resolution date:** 2024-12-14T06:22:10.433-0800
- **Affects versions:** Minecraft 18w20c; Minecraft 18w21a; Minecraft 18w21b; Minecraft 18w22a; Minecraft 18w22b; Minecraft 18w22c; Minecraft 1.13-pre1; Minecraft 1.13-pre2; Minecraft 1.13-pre3; Minecraft 1.13-pre6; Minecraft 1.13; Minecraft 18w30b; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 19w02a; Minecraft 19w03a; Minecraft 19w04b; Minecraft 19w05a; Minecraft 19w06a; Minecraft 19w07a; Minecraft 19w11b; Minecraft 19w12b; Minecraft 19w13b; Minecraft 19w14a; Minecraft 19w14b; Minecraft 1.14 Pre-Release 1; Minecraft 1.14; Minecraft 1.14.3; 1.14.4; 1.15 Pre-release 1; 1.15.1; 1.15.2; 1.16.3; 1.16.4; 20w46a; 20w51a; 21w03a; 21w05b; 21w06a; 21w44a; 1.18.1; 1.19; 1.19.3; 1.20.2; 23w43b; 23w45a; 1.20.3 Pre-Release 2; 1.20.3; 1.20.4 Release Candidate 1; 1.20.4; 1.20.5; 1.20.6; 1.21; 1.21.3
- **Fix versions:** 24w44a
- **Area:** Platform
- **Labels:** ice; seagrass
- **Watchers:** 1
- **Attachments:** 8
- **Attachment filenames:** 2018-05-18_21.25.05.png; 2018-05-18_21.25.52.png; 2023-10-31_18.53.32.png; 2023-10-31_18.53.45.png; 2023-10-31_18.53.59.png; MC-129888 - 1.17.1.png; MC-129888 - 1.19.png; MC-129888 - 21w44a.png
- **Issue links:** Relates:outward:MC-128329:Seagrass interferes with village bridge generation

## Description

Observed Behavior
Generated seagrass can overwrite blocks of ice in frozen biomes.
Expected Behavior
Generated seagrass should let the ice layout intact.
How to reproduce
Version: 1.21

```
Seed: -953538683905638291
Coordinates: /execute in minecraft:overworld run tp @s 22428.278 63 -1640.890 150.1 44.2
```

## Comments (17)

### Comment 1: migrated (2018-05-18T13:28:12.410-0700)

This comment contained multiple image attachments (8), please login to view the attachments.

### Comment 2: gaspoweredpick (2018-05-18T13:33:35.510-0700)

Relates to

### Comment 3: Michael Wobst (2018-05-19T05:28:18.767-0700)

Please always provide the seed and coordinates.

### Comment 4: muzikbike (2018-05-21T06:04:38.809-0700)

-3663419213315141181
/tp @s 1568 ~ -1184

### Comment 5: migrated (2018-09-22T19:35:38.778-0700)

Confirmed for 1.13.1.

```Coords: /tp @s 1709 64 -1210 200 50
Seed: same as desc.
(1568 ~ -1184 teleported me to land)```

### Comment 6: muzikbike (2018-12-03T02:56:24.557-0800)

Can I give up ownership of this ticket to someone else?

### Comment 7: gaspoweredpick (2019-03-31T15:47:26.045-0700)

Confirmed for 19w13b

### Comment 8: Avoma (2021-01-19T11:55:12.010-0800)

Can confirm in 20w51a.

### Comment 9: Avoma (2021-01-22T02:10:22.937-0800)

Can confirm in 21w03a.

### Comment 10: Avoma (2021-02-05T06:14:06.456-0800)

Can confirm in 21w05b.

### Comment 11: Avoma (2021-02-13T06:20:09.184-0800)

Can confirm in 21w06a.

### Comment 12: Avoma (2021-11-09T12:17:01.996-0800)

Can confirm this in both 1.17.1 and 21w44a.
This also appears to affect kelp as well and not just seagrass.

```Version: 1.17.1
Seed: 6284615873921193244
Coordinates: /execute in minecraft:overworld run tp @s 499.92 64.04 -832.87 -672.92 51.91```

```Version: 21w44a
Seed: -7206245882723273550
Coordinates: /execute in minecraft:overworld run tp @s -3799.22 63.20 -3089.73 171.02 46.81```

### Comment 13: Avoma (2021-11-12T10:42:54.188-0800)

I'd like to request ownership of this ticket since the current reporter has been inactive for over a year. I'm willing to keep this report updated and will continue to provide all of the necessary information.

### Comment 14: Avoma (2021-12-31T11:31:20.695-0800)

Can confirm in 1.18.1.

### Comment 15: Avoma (2022-07-26T05:52:43.407-0700)

Can confirm in 1.19.
Version: 1.19

```Seed: -953538683905638291
Coordinates: /execute in minecraft:overworld run tp @s 22422.08 64.39 -1630.53 580.59 48.97```

### Comment 16: Brain81505 (2023-01-18T02:43:46.138-0800)

Can confirm in 1.19.3

### Comment 17: Minecraft386882 (2024-11-21T07:24:21.014-0800)

Confirmed in 1.21.3
