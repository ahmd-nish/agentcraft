# MC-223840: Lava blocks from "Lava Aquifers" don't get updated when a cave cuts through underneath them

**Mojira URL:** [https://bugs.mojang.com/browse/MC-223840](https://bugs.mojang.com/browse/MC-223840)

## Report details

- **Mojira categories:** World generation
- **Project:** MC
- **Issue key:** MC-223840
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2021-04-21T12:36:50.248-0700
- **Updated:** 2025-04-29T21:24:16.008-0700
- **Resolution date:** 2021-11-17T09:28:30.898-0800
- **Affects versions:** 21w16a; 21w18a; 21w19a; 1.17; 1.17.1 Pre-release 1; 1.17.1; 21w44a; 1.18 Pre-release 1
- **Fix versions:** 1.18 Pre-release 3
- **Labels:** block-update; lava-aquifer; liquid; world-generation
- **Watchers:** 1
- **Attachments:** 7
- **Attachment filenames:** image-2021-04-21-21-32-00-110.png; image-2021-04-21-21-37-36-488.png; imagen_2021-04-27_141214.png; MC-223840.mp4; MC-223840 - 1.18 Pre-release 1.png; MC-223840 - 21w43a.png; MC-223840 - Analysis.png
- **Issue links:** Duplicate:inward:MC-224952:Lava lakes appear with empty spaces | Duplicate:inward:MC-224965:Lava aquifers float | Duplicate:inward:MC-228551:1.17 There is floating magma in the cave of the preview packet | Duplicate:inward:MC-228891:Floating Lava | Duplicate:inward:MC-230608:Glitching | Duplicate:inward:MC-240635:Sometimes lava doesn't flow down | Relates:inward:MC-226313:Lava can generate floating in caves

## Description

A lava aquifer generated with a cave directly beneath it. At some spots in the cave's ceiling, the lava aquifer and the cave connect. In those spots, the lava abruptly gets cut off and remains floating within the holes in the ceiling.
Steps to reproduce:
1. Generate a Lush-Cave Single-Biome world with the seed "-453190375585913630" in Java Edition Snapshot 21w16a with the experimental Caves&Cliffs datapack enabled
2. Go to 218/-44/277
3. Look at the ceiling towards the southern wall of the cave
Expected result: Lava flowing from the aquifer into the cave
Actual result: Lava remains stationary and requires manual updating
EDIT: After closer inspection, the phenomenon appears to generate at an intersection of lava aquifer + noise case + cave carver.
View from inside the cave:
View from atop the lava aquifer

## Comments (12)

### Comment 1: migrated (2021-04-21T12:36:50.248-0700)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: migrated (2021-04-27T05:18:24.769-0700)

Possible Bad Lava Aquifer generation
- Seed: 6345268163135639060

- Coordinates: -206 -44 -57 | x -206, y -44, z -57

### Comment 3: migrated (2021-05-07T02:32:31.314-0700)

Relates to

### Comment 4: Avoma (2021-05-12T08:05:22.202-0700)

Can confirm in 21w19a. Here are the seed + coordinates of where you can encounter this issue.

```Caves & Cliffs 21w19a Datapack
Seed: -8856052761302060561
Coordinates: /execute in minecraft:overworld run tp @s 68.70 -53.83 180.70 -213.65 23.51```

### Comment 5: Avoma (2021-07-06T11:16:56.679-0700)

Can confirm in 1.17.1.

### Comment 6: migrated (2021-09-25T10:40:01.012-0700)

I am unable to reproduce this issue in 21w38a.

### Comment 7: Fry (2021-11-03T08:52:54.671-0700)

Is this still an issue in the latest snapshot?

### Comment 8: TheBoy358 (2021-11-03T09:15:07.043-0700)

I'm unable to reproduce this bug in 21w43a with the steps to reproduce and Avoma's commentary and video.

### Comment 9: Avoma (2021-11-03T10:05:21.065-0700)

This issue no longer appears to be present in 21w43a. In my testing, I located several lava aquifers, all of which intersected caves at some point, and found that all lava within them appeared to flow correctly.
EDIT: Scratch that. This can still be reproduced in 21w43a but is very uncommon and less severe. This ticket also relates to . You can use the following seed and coordinates to reproduce this in 21w43a.

```Version: 21w43a
Seed: 6642560457107728397
Coordinates: /execute in minecraft:overworld run tp @s 305.72 -19.45 875.74 -968.83 28.18```

### Comment 10: Fry (2021-11-12T00:35:34.095-0800)

Is this still an issue in 1.18 pre-release 1? fluid propagation was improved

### Comment 11: Avoma (2021-11-15T01:24:19.642-0800)

Yep, this issue is still present in 1.18 Pre-release 1 despite the fluid propagation changes. You can use the following seed and coordinates to reproduce this in 1.18 Pre-release 1.

```Version: 1.18 Pre-release 1
Seed: 5518843328198964868
Coordinates: /execute in minecraft:overworld run tp @s -902.59 -19.74 -2347.49 -2265.39 28.72```

### Comment 12: JochCool (2021-11-17T09:28:30.898-0800)

Can confirm that this was fixed in 1.18-pre3
