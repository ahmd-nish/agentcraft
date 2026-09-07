# MC-93185: The exit portal in the end generates at highest block at 0 0 which can make it generate incomplete

**Mojira URL:** [https://bugs.mojang.com/browse/MC-93185](https://bugs.mojang.com/browse/MC-93185)

## Report details

- **Mojira categories:** Structures
- **Project:** MC
- **Issue key:** MC-93185
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2015-11-22T07:02:43.306-0800
- **Updated:** 2025-04-26T04:32:40.896-0700
- **Resolution date:** 2025-01-09T11:12:09.914-0800
- **Affects versions:** Minecraft 15w47c; Minecraft 17w06a; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 19w05a; Minecraft 19w06a; Minecraft 19w07a; Minecraft 19w14a; Minecraft 19w14b; 1.14.4; 1.15 Pre-release 1; 1.15.2; 20w19a; 20w21a; 1.16.3; 1.16.4 Release Candidate 1; 1.16.4; 20w46a; 1.17.1; 1.18.1; 1.20.1; 1.20.4; 23w51b; 1.20.6; 1.21 Pre-Release 2; 1.21; 24w35a
- **Fix versions:** 25w02a
- **Area:** Platform
- **Labels:** end; end_portal; exit
- **Votes:** 0
- **Watchers:** 1
- **Attachments:** 11
- **Attachment filenames:** 2015-11-22_15.52.44.png; 2018-09-12_01.25.46.png; 2022-01-14_18.40.55.png; 2023-07-18_10.54.04.png; 2023-07-18_10.54.05.png; 2023-07-18_11.03.38.png; End portal creation height (15w47c).png; End portal generating at highest block (17w06a).png; MC-93185.zip; screenshot-1.png; Screen Shot 2019-04-04 at 8.46.11 PM.png
- **Issue links:** Relates:inward:MC-207174:When blocks are placed above the End altar, the Ender Dragon comes to rest on top of said blocks rather than on top of the altar | Relates:outward:MC-279325:Broken end portals affected by MC-93185 from before 25w02a not datafixed | Relates:inward:MC-249012:The exit portal in the end can generate underground or partially underground | Duplicate:inward:MC-264338:The End Return portal was destroyed by the Void, and even if the End Dragon was killed, it would not be able to return to the Overworld(without any mod) | Duplicate:inward:MC-264300:Bug:The End Return portal was destroyed by the Void, and even if the End Dragon was killed, it would not be able to return to the Overworld | Duplicate:inward:MC-235505:there are UNBEATABLE Minecraft Seeds?! | Duplicate:inward:MC-231769:End was messed up. | Duplicate:inward:MC-201338:End generation resulted in a large hole in the middle. No portal in middle. | Duplicate:inward:MC-182627:End exit portal does not generate if there's no end stone island at the end origin | Duplicate:inward:MC-200225:Exit Portal fails to spawn when no terrain is generated at 0 0 | Duplicate:inward:MC-166199:End portal can generate underground | Duplicate:inward:MC-144023:The exit portal could naturally generate too low | Relates:outward:MC-82832:End Portal Spawns position changes

## Description

The bug
The exit portal in the end generates at the highest block at 0 0 after opening a pre 1.9 world in 1.9 or newer versions. This can cause the portal to be incomplete. Additionally you might end up with end crystals from old end pillars inside it.
How to reproduce
- Download

-  and drag it into .minecraft\saves.
  Set your Render Distance to 11 or above, due MC-137467.

- Open the world in the latest version (with the new dragon fight).
 → The portal generated at the highest block at 0 0. With this example it generated incomplete, see

- .

How to reproduce (naturally generated)
Seed

```
-953538683905638291
```
Coordinates

```
/execute in minecraft:the_end run tp @s 0.35 22.00 0.79 379.99 90.00
```

## Comments (16)

### Comment 1: migrated (2015-11-22T07:02:43.306-0800)

This comment contained multiple image attachments (11), please login to view the attachments.

### Comment 2: marcono1234 (2015-11-24T09:24:31.956-0800)

Confirmed for
- 15w47c The screenshot added shows the portal just below y=256 as in 1.8 a stone tower was placed that high.

### Comment 3: migrated (2018-09-11T16:27:06.079-0700)

Confirmed for 1.13.1.

### Comment 4: gaspoweredpick (2019-02-19T14:14:50.707-0800)

I found out that exit portals could also naturally generate too low in extremely rare cases. To reproduce that, use the seed -953538683905638291, go to the end, and teleport to 3 19 0.

### Comment 5: gaspoweredpick (2019-04-04T20:45:16.776-0700)

Confirmed for 19w14a

### Comment 6: gaspoweredpick (2019-04-07T14:39:36.524-0700)

Confirmed for 19w14b

### Comment 7: gaspoweredpick (2019-04-11T21:05:28.622-0700)

Confirmed for 1.14 Pre-Release 1

### Comment 8: gaspoweredpick (2019-05-07T21:03:43.603-0700)

Confirmed for 1.14  and 1.14.1 Pre-Release 1

### Comment 9: migrated (2019-11-23T07:23:59.794-0800)

Still in 1.15 Pre Release 1; see MC-166199

### Comment 10: zhangzhen (2023-07-19T05:09:24.282-0700)

seed-8094280050187681634 bugs report:MC-264300  this bug is still in 1.20.1 MC-264338

### Comment 11: COMETC2021A1 (2023-12-20T04:30:28.623-0800)

in 1.20.4 and 23w51a.

### Comment 12: COMETC2021A1 (2024-03-12T02:35:22.425-0700)

Maybe this issue could be fixed by generating the exit portal at a specific height (y1 or above) when there's no solid block at (0,0).

### Comment 13: COMETC2021A1 (2024-05-31T07:35:47.507-0700)

In 1.21-pre2.

### Comment 14: migrated (2024-06-30T17:03:11.724-0700)

Can confirm in 1.21

### Comment 15: COMETC2021A1 (2024-09-02T08:58:35.403-0700)

Still in 24w35a.

### Comment 16: Ceresjanin123 (2024-11-27T11:43:13.380-0800)

By looking at the level.dat you can see in those seeds the end portal is placed at Y -1 despite the end ending at Y0

The simple solution would be forbidding the y value for ExitPortalLocation from being lower than 1 (or better, bedrock_level +1 because of custom worlds)
Also most importantly all affected worlds from before the fix would need to have ExitPortalLocation datafixed to Y1
