# MC-155084: Horses' armor, reins, and bridles experience z-fighting

**Mojira URL:** [https://bugs.mojang.com/browse/MC-155084](https://bugs.mojang.com/browse/MC-155084)

## Report details

- **Mojira categories:** Textures and models
- **Project:** MC
- **Issue key:** MC-155084
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2019-06-24T01:50:09.678-0700
- **Updated:** 2025-04-30T04:50:40.298-0700
- **Resolution date:** 2023-04-14T23:45:27.653-0700
- **Affects versions:** Minecraft 1.14.2; 1.14.4; 1.15 Pre-release 5; 1.15; 1.15.2; 20w12a; 20w18a; 20w19a; 20w20a; 1.16 Pre-release 3; 1.16 Release Candidate 1; 1.16; 1.16.2; 1.16.3; 1.16.4; 20w45a; 20w49a; 1.16.5; 21w06a; 21w10a; 21w17a; 21w18a; 1.17; 1.17.1; 21w39a; 21w40a; 21w42a; 1.18 Pre-release 1; 1.18 Pre-release 5; 1.18 Pre-release 8; 1.18; 1.18.1 Pre-release 1; 1.18.1; 22w03a; 22w05a; 22w06a; 22w07a; 1.18.2; 22w17a; 22w18a; 22w19a; 1.19 Pre-release 1; 1.19 Pre-release 2; 1.19 Pre-release 3; 1.19 Pre-release 4; 1.19 Pre-release 5; 1.19 Release Candidate 2; 1.19; 1.19.2; 22w43a; 22w44a; 22w46a; 1.19.3 Pre-release 2; 1.19.3; 23w04a; 23w05a; 1.19.4
- **Fix versions:** 23w14a
- **Labels:** entity-model; z-fighting
- **Watchers:** 1
- **Attachments:** 11
- **Attachment filenames:** 2019-06-24_11.47.53.png; 2019-06-24_11.48.04.png; 2019-12-06_19.40.13.png; 2019-12-06_19.40.26.png; 2019-12-06_19.40.37.png; 2019-12-06_19.40.47.png; 2021-10-20_15.07.14.png; Bug.png; image-2020-12-02-18-16-15-662.png; image-2022-08-10-09-05-51-754.png; MC-155084.mp4
- **Issue links:** Duplicate:inward:MC-161032:Lines in horse armor | Duplicate:inward:MC-167927:Horse Saddles have weird visual glitching on them | Duplicate:inward:MC-175025:Horse rein rendering | Duplicate:inward:MC-183850:Horse armor bugs the horse bridles (also, there's a Z-fighting) | Duplicate:inward:MC-190544:Mislocated pixels on golden horse armor texture | Duplicate:inward:MC-190625:Horse Armor handles look like spectography lines. | Duplicate:inward:MC-198222:Horse texture bug | Duplicate:inward:MC-202381:Horse armor has z fighting when viewed from the front | Duplicate:inward:MC-204794:Texture bug with Horse Armor | Duplicate:inward:MC-204838:Wheh siting on a horse with saddle and horse amor, you can see weird pixels | Duplicate:inward:MC-227415:Glitchy Horse Armor Textures | Duplicate:inward:MC-234132:Horse Armour Minor Graphical Glitch | Duplicate:inward:MC-259056:Horse Armor / Saddle Reins Texture | Relates:inward:MC-163875:Wandering Traider running very fast without potions. | Relates:inward:MCPE-163875:Bridles on horses, mules and donkeys create z-fighting

## Description

The Bug:
Horses' armor, reins, and bridles experience z-fighting.
Steps to Reproduce:
- Summon a horse equipped with a saddle and some armor by using the command provided below.

```
/summon minecraft:horse ~ ~ ~ {Tame:1b,ArmorItem:{id:"minecraft:diamond_horse_armor",Count:1b},SaddleItem:{id:"minecraft:saddle",Count:1b}}
```

- Mount the horse, look closely at the horse's reins and take note as to whether or not z-fighting can be seen.

- Look below the horse's reins at either side of their neck and take note as to whether or not z-fighting can be seen.

- Dismount the horse, look at its bridle and take note as to whether or not z-fighting can be seen.

Observed Behavior:
Horses' armor, reins, and bridles experience z-fighting.
Expected Behavior:
Horses' armor, reins, and bridles would not experience z-fighting.

## Comments (36)

### Comment 1: migrated (2019-06-24T01:50:09.678-0700)

This comment contained multiple image attachments (11), please login to view the attachments.

### Comment 2: Tinsel (2020-03-18T16:31:58.404-0700)

In 20w12a

### Comment 3: Tinsel (2020-04-29T10:34:50.568-0700)

20w18a

### Comment 4: Tinsel (2020-05-06T11:45:37.901-0700)

In 20w19a

### Comment 5: Tinsel (2020-06-10T10:15:45.605-0700)

In 1.16 Pre 3

### Comment 6: migrated (2020-11-08T20:33:03.852-0800)

Confirmed for 20w45a

### Comment 7: migrated (2020-12-02T18:16:46.191-0800)

20w49a, as well as on the front face of the horse.

### Comment 8: Avoma (2021-02-14T09:01:51.835-0800)

Can confirm in 21w06a.

### Comment 9: Avoma (2021-03-13T06:53:23.042-0800)

Can confirm in 21w10a. Video attached.

### Comment 10: Tinsel (2021-04-28T10:13:26.279-0700)

In 21w17a

### Comment 11: Tinsel (2021-05-05T13:27:48.067-0700)

In 21w18a

### Comment 12: Tinsel (2021-06-08T12:15:23.501-0700)

In 1.17

### Comment 13: ampolive (2021-08-05T15:47:31.228-0700)

Can confirm in 1.17.1.
P.S. "you may need to take a closer look" would be an amazing splash text.

### Comment 14: SoloAlguien (2021-09-29T15:08:35.186-0700)

Can confirm in 21w39a.

### Comment 15: SoloAlguien (2021-10-10T14:45:05.011-0700)

Can confirm in 21w40a.

### Comment 16: SoloAlguien (2021-10-20T11:10:54.600-0700)

Can confirm in 21w42a.

### Comment 17: Tinsel (2021-11-11T10:30:18.492-0800)

Still in 1.18 Pre-1! It's pretty noticeable during gameplay..

### Comment 18: Avoma (2021-11-19T11:11:01.545-0800)

I'd like to request ownership of this ticket since the current reporter has been inactive since November of 2019.

### Comment 19: SoloAlguien (2021-12-03T15:22:14.411-0800)

Can confirm in 1.18 and 1.18.1 Pre-release 1.

### Comment 20: Tinsel (2022-02-02T13:12:20.221-0800)

Still in 22w05a

### Comment 21: SoloAlguien (2022-03-01T12:29:16.699-0800)

Can confirm in 1.18.2.

### Comment 22: Tinsel (2022-05-05T20:48:58.635-0700)

Still in 22w18a

### Comment 23: Tinsel (2022-05-13T14:53:09.504-0700)

Can confirm for 22w19a

### Comment 24: Tinsel (2022-05-18T14:06:28.419-0700)

Also in 1.19 Pre-1

### Comment 25: Tinsel (2022-05-24T11:48:30.410-0700)

Can confirm for 1.19 Pre-2

### Comment 26: Tinsel (2022-05-25T18:06:06.150-0700)

As well as 1.19 Pre-3

### Comment 27: Tinsel (2022-05-30T12:12:49.525-0700)

In 1.19 Pre-4

### Comment 28: Tinsel (2022-06-01T20:58:45.628-0700)

Still in 1.19 Pre-5

### Comment 29: Brenden0784 (2022-08-10T07:03:01.348-0700)

Can confirm for 1.19.2

### Comment 30: Tinsel (2022-11-05T16:17:30.862-0700)

Can confirm for 22w44a

### Comment 31: Tinsel (2022-11-16T11:12:52.319-0800)

In 22w46a

### Comment 32: Tinsel (2022-11-23T09:25:53.621-0800)

In 1.19.3 Pre-1

### Comment 33: Tinsel (2022-11-23T12:33:21.448-0800)

In 1.19.3 Pre-2

### Comment 34: Tinsel (2022-12-07T20:26:15.042-0800)

In 1.19.3

### Comment 35: Tinsel (2023-01-25T11:32:19.177-0800)

Also in 23w04a

### Comment 36: Tinsel (2023-02-01T20:20:35.787-0800)

In 23w05a
