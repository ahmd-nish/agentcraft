# MC-173020: Minecarts can't pickup entities at some heights

**Mojira URL:** [https://bugs.mojang.com/browse/MC-173020](https://bugs.mojang.com/browse/MC-173020)

## Report details

- **Mojira categories:** Entities; Minecart
- **Project:** MC
- **Issue key:** MC-173020
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2020-02-23T14:25:24.573-0800
- **Updated:** 2025-04-26T09:25:14.761-0700
- **Resolution date:** 2024-11-18T09:40:04.665-0800
- **Affects versions:** 1.15.2; 20w08a; 1.16 Release Candidate 1; 1.16; 1.16.1; 1.16.4; 20w45a; 20w49a; 1.16.5; 21w05a; 21w15a; 21w16a; 1.17 Pre-release 1; 1.17.1; 21w37a; 22w13a
- **Fix versions:** 22w16a
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** fixed3.mp4; MC-173020 Cannot Reproduce in 24w46a.mp4; Minecart_pickup_bug.png

## Description

While testing on how to pickup ghasts with minecarts, I found that some heights are "cursed" as a minecart cannot pickup a ghast where it will at others heights. That happen on versions 1.12.2, 1.15.2 and 1.16.1.
The bug
If a minecart is more than 2 blocks up from a vertical sub-chunk border, it will never pick entities located in the vertical sub-chunk below the border.
How to reproduce
- Place a soul sand block at Y=15

- At Y=18, make a 3 by 3 blocks square rail line floating around the soul sand

- Spawn a wither-skeleton on the soul sand

- Launch a empty minecart on the rail circle
→  The minecart will not pickup the wither-skeleton, but it will if the setup is make one block offset vertically

Code analysis
From analysis on Minecraft java 1.15.1:
The bug comes from the getEntities functions in net.minecraft.world.level.chunk.LevelChunk. These functions will look at sub-chunks only 2 blocks down and up from a given collision box; so it can miss entities taller than 2 blocks.

## Comments (14)

### Comment 1: migrated (2020-02-23T14:25:24.573-0800)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: migrated (2020-06-20T08:14:02.335-0700)

Affects 1.16 Release Candidate 1

### Comment 3: migrated (2020-07-30T07:40:10.904-0700)

Affects 1.16.2 Pre-release 1

### Comment 4: migrated (2020-11-07T06:28:31.288-0800)

Affects 20w45a

### Comment 5: migrated (2020-12-03T06:58:44.678-0800)

Affects 20w49a

### Comment 6: migrated (2021-02-03T14:34:56.826-0800)

Affects 21w05a

### Comment 7: migrated (2021-04-14T09:25:12.957-0700)

Affects 21w15a

### Comment 8: migrated (2021-04-21T10:59:44.834-0700)

Affects 21w16a

### Comment 9: migrated (2021-05-27T06:51:15.826-0700)

Affects 1.17 Pre-release 1

### Comment 10: migrated (2021-09-16T03:41:41.087-0700)

Affects 21w37a

### Comment 11: migrated (2022-04-04T03:49:54.212-0700)

Affects 22w13a

### Comment 12: migrated (2022-06-17T08:11:37.949-0700)

I can no longer reproduce this issue with the given instructions in 1.19

### Comment 13: Onk2 (2023-04-05T14:09:02.696-0700)

This bug is out of the game in 1.19 as the way the game search for entities has changed.

### Comment 14: JervieA20 (2024-11-18T06:20:05.619-0800)

Cannot Reproduce in Latest Snapshot (24w46a)
