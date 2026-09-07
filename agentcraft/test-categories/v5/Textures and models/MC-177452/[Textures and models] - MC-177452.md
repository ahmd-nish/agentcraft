# MC-177452: Unneeded faces inside repeater models

**Mojira URL:** [https://bugs.mojang.com/browse/MC-177452](https://bugs.mojang.com/browse/MC-177452)

## Report details

- **Mojira categories:** Textures and models
- **Project:** MC
- **Issue key:** MC-177452
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2020-04-04T17:28:27.217-0700
- **Updated:** 2025-04-26T09:43:05.423-0700
- **Resolution date:** 2024-08-17T07:32:14.908-0700
- **Affects versions:** 1.15.2; 20w14a; 20w18a; 20w21a; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16.1; 20w27a; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 20w49a; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w08b; 21w15a; 21w16a; 21w20a; 1.17 Pre-release 1; 1.17; 1.17.1; 1.18; 1.18.1; 1.18.2; 1.19; 1.19.2; 1.20 Pre-release 1; 1.20.1; 23w43a; 1.21
- **Fix versions:** 24w33a
- **Area:** Gameplay
- **Labels:** 1.8-bad-model-conversion-remnants; 1.8-model-conversion-remnants; unnecessary-planes
- **Watchers:** 1
- **Attachments:** 14
- **Attachment filenames:** 2020-04-05_01.26.11.png; 2020-04-05_01.26.15.png; repeater_1tick_locked.json; repeater_1tick_on_locked.json; repeater_1tick.json; repeater_2tick_locked.json; repeater_2tick_on_locked.json; repeater_2tick.json; repeater_3tick_locked.json; repeater_3tick_on_locked.json; repeater_3tick.json; repeater_4tick_locked.json; repeater_4tick_on_locked.json; repeater_4tick.json
- **Issue links:** Relates:outward:MC-177453:Unneeded faces inside comparator models | Relates:outward:MC-208191:Unneeded face in candle cake model

## Description

The resource pack attached to MC-214686 offers a complete fix for this issue. Mojang have my full permission to (and are encouraged to) replace the affected vanilla model files with the contents of the resource pack.
The bug
Redstone repeater models define faces for the bottoms of unlit redstone torches, as well as the bottom of locks for locked repeaters, despite these never being visible without clipping into the repeater itself. Powered torches correctly omit such faces due to not using a single cuboid.
How to reproduce
- Place down an unpowered redstone repeater

- Enter Spectator mode

- Fly into the repeater such that the bottoms of the torches are in view

Expected behaviour
The unpowered torches would not have any bottom faces defined since such faces are never possible to see in normal gameplay.
Actual behaviour
These bottom faces are defined anyway, bloating the model file and forcing the game to render useless faces.
How to fix
The resource pack attached to MC-214686 fixes this issue completely.

## Comments (17)

### Comment 1: migrated (2020-04-04T17:28:27.217-0700)

This comment contained multiple image attachments (14), please login to view the attachments.

### Comment 2: migrated (2020-05-20T18:26:42.731-0700)

There is no reason to remove the bottoms of these blocks as in anarchy servers these blocks are used as bases and removal of the bottoms can lead to base leaking

### Comment 3: Avoma (2020-12-03T10:57:25.454-0800)

Can confirm in 20w49a.

### Comment 4: Avoma (2021-01-20T03:47:33.942-0800)

Can confirm in 20w51a.

### Comment 5: Avoma (2021-02-05T06:59:07.965-0800)

Can confirm in 21w05b.

### Comment 6: Avoma (2021-02-13T08:35:53.277-0800)

Can confirm in 21w06a.

### Comment 7: Avoma (2021-03-01T01:21:48.679-0800)

Can confirm in 1.16.5 and 21w08b.

### Comment 8: Avoma (2021-04-18T10:46:08.615-0700)

Can confirm in 21w15a.

### Comment 9: Avoma (2021-04-26T02:51:46.103-0700)

Can confirm in 21w16a.

### Comment 10: Avoma (2021-06-12T11:53:40.758-0700)

Can confirm in 1.17.

### Comment 11: ampolive (2021-07-17T17:41:04.061-0700)

Can confirm in 1.17.1 for the unpowered repeaters, and locked repeaters. Powered repeaters do not have the bottom faces of the torches.

### Comment 12: Avoma (2021-12-08T07:21:25.090-0800)

Can confirm in 1.18.

### Comment 13: Avoma (2021-12-17T05:34:35.490-0800)

Can confirm in 1.18.1.

### Comment 14: Avoma (2022-03-07T09:52:44.970-0800)

Can confirm in 1.18.2.

### Comment 15: Avoma (2022-06-26T11:37:02.955-0700)

Can confirm in 1.19.

### Comment 16: Avoma (2022-09-06T10:28:02.561-0700)

Can confirm in 1.19.2.

### Comment 17: muzikbike (2024-08-15T09:41:03.284-0700)

24w33a fixes this
