# MC-215139: Some water in caves will not start flowing

**Mojira URL:** [https://bugs.mojang.com/browse/MC-215139](https://bugs.mojang.com/browse/MC-215139)

## Report details

- **Mojira categories:** World generation
- **Project:** MC
- **Issue key:** MC-215139
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2021-02-11T12:39:46.509-0800
- **Updated:** 2025-04-11T14:09:37.498-0700
- **Resolution date:** 2021-11-19T11:46:34.941-0800
- **Affects versions:** 21w06a; 21w38a; 21w39a; 21w40a; 21w41a; 21w44a
- **Fix versions:** 1.18 Pre-release 1
- **Labels:** water
- **Watchers:** 1
- **Attachments:** 9
- **Attachment filenames:** 2021-02-11_15.26.51.png; 2021-02-11_15.27.00.png; MC-215139 - 1.18 Pre-release 1.mp4; MC-215139 - 1.18 Pre-release 1.png; MC-215139 - 1.18 Pre-release 1 (2).png; MC-215139 - 21w40a.png; MC-215139 - 21w41a.png; MC-215139 - 21w44a.png; MC-215139 - 21w44a (2).png
- **Issue links:** Duplicate:inward:MC-237671:Liquids in aquifers occasionally do not flow correctly | Duplicate:inward:MC-237688:Weird water generation | Relates:outward:MC-203712:Amethyst Geodes cause floating water/lava to generate when intersecting water/lava caves/pools

## Description

The bug
Water in caves will occasionally not flow, unless it is updated.
How to reproduce
- Create a default world with seed 4876135133240268742

- Run the following command:

```
/execute in minecraft:overworld run tp @s 5990 -22 1164 -326 11
```
 The water is not flowing

Expected behavior
All water in caves that can flow would flow, without the need for a block update in order for it to begin flowing.

## Comments (9)

### Comment 1: migrated (2021-02-11T12:39:46.509-0800)

This comment contained multiple image attachments (9), please login to view the attachments.

### Comment 2: migrated (2021-02-12T06:54:36.399-0800)

Relates to

### Comment 3: Avoma (2021-02-19T12:06:25.866-0800)

This issue can no longer be reproduced using the provided seed & coordinates.

### Comment 4: Avoma (2021-03-27T11:34:39.155-0700)

Relates to MC-203712.

### Comment 5: Avoma (2021-10-11T01:36:40.545-0700)

Can confirm this behavior in 21w40a. Here are some extra details regarding this problem.
The Bug:
Water in caves sometimes doesn't flow.
Steps to Reproduce:
- Enter the following seed and coordinates.

```Seed: 4876135133240268742
Coordinates: /execute in minecraft:overworld run tp @s 5990.68 -22.00 1164.30 -325.79 10.56```
- Take note as to whether or not the water is flowing.

Observed Behavior:
Water in caves sometimes doesn't flow.
Expected Behavior:
Water in caves would always flow.

### Comment 6: Avoma (2021-10-17T03:12:24.901-0700)

Can confirm this in 21w41a.

### Comment 7: Avoma (2021-11-04T10:35:02.069-0700)

Can confirm that this issue is still present in 21w44a.

```Version: 21w44a
Seed: -7123216856550990646
Coordinates: /execute in minecraft:overworld run tp @s -201887.16 52.88 577.96 56.50 13.69```

### Comment 8: Avoma (2021-11-15T01:39:47.302-0800)

This issue doesn't appear to be fixed in 1.18 Pre-release 1, therefore, I'm requesting for this ticket to be reopened. You can create a world with the following seed and teleport to the following coordinates in order to reproduce this in 1.18 Pre-release 1.

```Version: 1.18 Pre-release 1
Seed: 5518843328198964868
Coordinates: /execute in minecraft:overworld run tp @s -3256.64 20.73 -5797.15 -6134.40 30.36```

### Comment 9: Avoma (2021-11-19T11:46:34.941-0800)

This issue was present in 1.18 Pre-release 1, but is no longer in 1.18 Pre-release 3 likely due to the fix of MC-223840. There is no need to reopen this report.
