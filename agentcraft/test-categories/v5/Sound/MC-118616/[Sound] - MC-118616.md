# MC-118616: The sounds of magma cubes and slimes aren't controlled by the "Hostile Creatures" sound slider

**Mojira URL:** [https://bugs.mojang.com/browse/MC-118616](https://bugs.mojang.com/browse/MC-118616)

## Report details

- **Mojira categories:** Sound
- **Project:** MC
- **Issue key:** MC-118616
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2017-06-11T19:26:11.793-0700
- **Updated:** 2025-04-30T03:44:46.925-0700
- **Resolution date:** 2023-08-17T02:41:00.290-0700
- **Affects versions:** Minecraft 1.12; Minecraft 1.12.1; Minecraft 1.12.2 Pre-Release 1; Minecraft 1.12.2 Pre-Release 2; Minecraft 1.12.2; Minecraft 17w43b; Minecraft 17w45a; Minecraft 17w46a; Minecraft 18w20c; Minecraft 1.13-pre8; Minecraft 1.13; Minecraft 18w30b; Minecraft 18w31a; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 19w02a; Minecraft 19w12b; Minecraft 19w13b; Minecraft 1.14.1; Minecraft 1.14.2; Minecraft 1.14.3; 1.14.4; 19w36a; 1.15 Pre-release 6; 1.15.2; 20w11a; 20w12a; 20w22a; 1.16 Pre-release 5; 1.16.1; 1.16.2; 1.16.3; 1.16.4; 21w03a; 21w05b; 21w06a; 21w11a; 21w17a; 1.17.1; 21w42a; 21w44a; 1.18 Pre-release 1; 1.18 Pre-release 5; 1.18; 1.18.1; 22w05a; 1.18.2; 22w11a; 1.19; 1.19.1 Pre-release 5; 1.19.1; 1.19.2; 1.19.3; 1.19.4; 1.20; 1.20.1
- **Fix versions:** 23w33a
- **Labels:** magma_cube; slime
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-118616.mp4; MC-118616.png
- **Issue links:** Duplicate:inward:MC-142173:The Slime's Sound is Classified as a Friendly Creature | Duplicate:inward:MC-156684:Slimes considered as friendly creatures for sound settings | Duplicate:inward:MC-174571:Magma Cube sounds affected by friendly creatures slider | Duplicate:inward:MC-186575:Slime's audio is controlled by the Friendly Creatures bar in audio settings. | Duplicate:inward:MC-189740:Slime sound is classified as a Friendly Creature sound | Duplicate:inward:MC-190824:Hostile Creature sounds mixed with Friendly | Duplicate:inward:MC-196396:Friendly Creatures And Hostile Creatures Fliped | Duplicate:inward:MC-200243:Magma Cube Sounds classified as Friendly Creatures | Duplicate:inward:MC-242046:Magma Cube and Slime sounds are classified under Friendly Creature sounds | Duplicate:inward:MC-249231:Magma cubes' sounds | Duplicate:inward:MC-255773:Slimes are considered Friendly Creatures | Duplicate:inward:MC-262082:Slimes volume only changes with friendly creatures option. | Relates:outward:MC-66364:Hostile Creatures Sound Slider changes volume of Slime Blocks.

## Description

The Bug:
The sounds of magma cubes and slimes aren't controlled by the "Hostile Creatures" sound slider.
Any action that is created through a hostile entity doing something that doesn't result in blocks being changed, is normally controlled by the "Hostile Creatures" sound slider. For example, the sounds of skeletons burning, zombies groaning, and drowned stepping, are all controlled by the "Hostile Creatures" sound slider as they should be, because the entities are performing these actions.
The sounds of magma cubes and slimes aren't controlled by the "Hostile Creatures" sound slider when they should be, and are instead controlled by the "Friendly Creatures" sound slider.
Steps to Reproduce:
- Navigate to the "Music & Sounds" settings menu.

- Turn the "Friendly Creatures" sound slider to "OFF".

- Turn every other sound slider to "100%".

- Exit this menu, summon some magma cubes or slimes, and listen closely as they jump around.

- Take note as to whether or not the sounds of magma cubes and slimes can be heard, (are controlled by the "Friendly Creatures" sound slider instead of the "Hostile Creatures" sound slider).

Observed Behavior:
The sounds of magma cubes and slimes aren't controlled by the "Hostile Creatures" sound slider and are instead controlled by the "Friendly Creatures" sound slider.
Expected Behavior:
The sounds of magma cubes and slimes would be controlled by the "Hostile Creatures" sound slider.

## Comments (18)

### Comment 1: migrated (2017-06-11T19:26:11.793-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: [Mod] bemoty (2017-08-10T05:19:47.379-0700)

Can confirm for MC 1.12.1.

### Comment 3: migrated (2018-07-02T08:12:13.575-0700)

Maybe related to the fact that you can sleep when slimes are nearby, maybe they are somehow "peaceful" mobs in the code.

### Comment 4: Nergalic (2019-05-19T08:54:58.569-0700)

Can confirm that this bug still is present as of v1.14.1.

### Comment 5: migrated (2019-08-03T19:35:36.698-0700)

Bug still present as of 1.14.4

### Comment 6: migrated (2020-03-13T13:05:28.572-0700)

Bug still present as of 20w11a

### Comment 7: Tinsel (2020-03-18T16:35:28.600-0700)

In 20w12a

### Comment 8: migrated (2020-06-14T16:05:34.563-0700)

Bug still present as of 1.16pre-5

### Comment 9: migrated (2020-06-21T14:16:52.366-0700)

Still present in 1.15.2

### Comment 10: migrated (2020-07-29T01:32:21.928-0700)

It won't be fixed in 1.15.2

### Comment 11: migrated (2020-12-13T11:13:57.786-0800)

Still present in 1.16.4

### Comment 12: Avoma (2021-02-02T00:41:41.829-0800)

Can confirm in 21w03a.

### Comment 13: Avoma (2021-02-08T00:39:06.736-0800)

Can confirm in 21w05b.

### Comment 14: Avoma (2021-02-13T11:52:37.366-0800)

Can confirm in 21w06a.

### Comment 15: Avoma (2021-03-28T12:03:15.856-0700)

Can confirm in 21w11a. Relates to .

### Comment 16: Avoma (2021-05-03T00:39:44.715-0700)

Can confirm in 21w17a.

### Comment 17: Avoma (2021-07-25T07:31:07.481-0700)

Can confirm in 1.17.1.

### Comment 18: Avoma (2021-10-23T02:02:43.264-0700)

Can confirm in 21w42a. Here are some extra details regarding this problem.
The Bug:
Magma cubes and slime sounds are controlled by the "Friendly Creatures" sound slider.
Steps to Reproduce:
- Navigate to the "Music & Sounds" settings menu.

- Turn the "Friendly Creatures" sound slider to "0%".

- Turn every other sound slider to "100%".

- Exit this menu and summon some magma cubes and slimes.

- Listen closely as they jump around.

- Take note as to whether or not magma cubes and slime sounds can be heard, (are controlled by the "Friendly Creatures" sound slider).

Observed Behavior:
Magma cubes and slime sounds are controlled by the "Friendly Creatures" sound slider.
Expected Behavior:
Magma cubes and slime sounds would not be controlled by the "Friendly Creatures" sound slider. Instead, these sounds should be controlled by the "Hostile Creatures" sound slider, as magma cubes and slimes are hostile entities.
