# MC-267006: The Distance Flown statistics rapidly increases when you are standing in Ender Dragon's hitbox

**Mojira URL:** [https://bugs.mojang.com/browse/MC-267006](https://bugs.mojang.com/browse/MC-267006)

## Report details

- **Mojira categories:** Collision; Statistics
- **Project:** MC
- **Issue key:** MC-267006
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2023-11-25T04:08:11.174-0800
- **Updated:** 2025-04-29T08:41:48.825-0700
- **Resolution date:** 2024-06-18T04:24:43.063-0700
- **Affects versions:** Minecraft 13w36a; 1.20.2; 1.20.3 Pre-Release 2; 1.20.3 Pre-Release 4; 1.20.3; 1.20.4; 23w51b; 24w03a; 24w09a; 24w10a; 24w13a; 24w14a; 1.20.5 Pre-Release 1; 1.20.5 Pre-Release 4; 1.20.5; 1.20.6 Release Candidate 1; 1.20.6; 24w18a; 24w20a; 24w21b; 1.21 Pre-Release 1; 1.21 Pre-Release 2
- **Fix versions:** 24w33a
- **Area:** Platform
- **Labels:** EnderDragon; Player; Server; statistics
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** image-2024-05-28-12-50-45-086.png; Not move but flown 80km.mp4

## Description

When a player(survival mode) is standing in an Ender Dragon's hitbox, the Distance Flown statistic will rapidly increase.
In the attached video, The Distance Flown increased about 80km within less than a minute.
This is not a duplicate of  because in this case players actually don't move.
Steps to reproduce
1.run /data merge entity @e[type=ender_dragon,limit=1] {DragonPhase:3} to make the dragon land.
2.When the dragon land, stand at the center of the dragon and switch to survival mode.
3.Open the statistics and note down the distance flown.
4.Waiting until the dragon knockback you, open the statistics and note down the distance flown again.
Observed behaviour:
The distance flown increased over 50 km.
Expected behaviour:
The distance flown don't increase.
Notes:
This bug happened since 1.9.
I think it's because the dragon always gives player a large amount of server velocity when they are in the Dragon's knockback hitbox even if the player don't actually move.

## Comments (3)

### Comment 1: migrated (2023-11-25T04:08:11.174-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: COMETC2021A1 (2023-11-29T01:35:51.631-0800)

Confirmed in 1.20.3-pre4.
This issue can be traced back to 1.9.

### Comment 3: COMETC2021A1 (2024-05-27T21:51:02.927-0700)

Run this command when you are in Ender Dragon's hitbox:
/data get entity @s Motion
You will find a large number of Motion on X or Z axis (20-150)
See this screenshot
This motion is only on server side but not on client side.
So this should be a client-server desync.
