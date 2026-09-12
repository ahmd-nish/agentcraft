# MC-38022: Order of rendering translucent block faces fails to update with camera position

**Mojira URL:** [https://bugs.mojang.com/browse/MC-38022](https://bugs.mojang.com/browse/MC-38022)

## Report details

- **Mojira categories:** Rendering; Textures and models
- **Project:** MC
- **Issue key:** MC-38022
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2013-10-27T13:39:50.526-0700
- **Updated:** 2025-04-26T03:11:31.635-0700
- **Resolution date:** 2024-10-23T21:24:10.491-0700
- **Affects versions:** Minecraft 1.7.2; Minecraft 14w25b; Minecraft 14w27b; Minecraft 14w29b; Minecraft 1.8-pre2; Minecraft 1.8.3; Minecraft 1.8.8; Minecraft 15w45a; Minecraft 15w46a; Minecraft 15w47a; Minecraft 15w47c; Minecraft 1.8.9; Minecraft 15w51b; Minecraft 1.9 Pre-Release 1; Minecraft 1.9 Pre-Release 2; Minecraft 1.10; Minecraft 1.11; Minecraft 16w50a; Minecraft 1.11.2; Minecraft 17w14a; Minecraft 1.12.2; Minecraft 18w02a; Minecraft 18w08a; Minecraft 18w08b; Minecraft 18w09a; Minecraft 18w11a; Minecraft 18w15a; Minecraft 18w20c; Minecraft 18w21a; Minecraft 18w22c; Minecraft 1.13-pre1; Minecraft 1.13-pre2; Minecraft 1.13-pre3; Minecraft 1.13-pre4; Minecraft 1.13-pre5; Minecraft 1.13-pre6; Minecraft 1.13-pre8; Minecraft 1.13-pre9; Minecraft 1.13-pre10; Minecraft 1.13; Minecraft 18w30b; Minecraft 18w31a; Minecraft 18w32a; Minecraft 18w33a; Minecraft 1.13.1-pre1; Minecraft 1.13.1; Minecraft 1.13.2-pre1; Minecraft 1.13.2-pre2; Minecraft 1.13.2; Minecraft 18w50a; Minecraft 19w04b; Minecraft 19w05a; Minecraft 19w06a; Minecraft 19w07a; Minecraft 19w08a; Minecraft 19w09a; Minecraft 19w11a; Minecraft 19w11b; Minecraft 19w12b; Minecraft 19w13a; Minecraft 19w13b; Minecraft 19w14a; Minecraft 19w14b; Minecraft 1.14 Pre-Release 1; Minecraft 1.14 Pre-Release 2; Minecraft 1.14 Pre-Release 3; Minecraft 1.14 Pre-Release 4; Minecraft 1.14 Pre-Release 5; Minecraft 1.14; Minecraft 1.14.1; Minecraft 1.14.2 Pre-Release 1; Minecraft 1.14.2 Pre-Release 2; Minecraft 1.14.2; Minecraft 1.14.3 Pre-Release 2; Minecraft 1.14.3; Minecraft 1.14.4 Pre-Release 1; Minecraft 1.14.4 Pre-Release 3; Minecraft 1.14.4 Pre-Release 4; Minecraft 1.14.4 Pre-Release 5; Minecraft 1.14.4 Pre-Release 6; 1.14.4; 19w34a; 19w35a; 19w36a; 19w37a; 19w38b; 19w39a; 19w40a; 19w41a; 19w42a; 19w45b; 19w46b; 1.15 Pre-release 1; 1.15 Pre-Release 2; 1.15 Pre-release 3; 1.15 Pre-release 4; 1.15 Pre-release 5; 1.15 Pre-release 6; 1.15 Pre-release 7; 1.15; 1.15.1; 1.15.1 Pre-release 1; 1.15.2 Pre-Release 1; 1.15.2 Pre-release 2; 1.15.2; 20w06a; 20w07a; 20w08a; 20w09a; 20w10a; 20w11a; 20w13a; 20w13b; 20w15a; 20w17a; 20w18a; 20w19a; 20w20a; 20w20b; 20w21a; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 5; 1.16 Pre-release 6; 1.16 Pre-release 7; 1.16 Pre-release 8; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w28a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Release Candidate 1; 1.16.2 Release Candidate 2; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4 Pre-release 1; 1.16.4 Pre-release 2; 1.16.4 Release Candidate 1; 1.16.4; 20w46a; 20w48a; 20w51a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w11a; 1.17 Pre-release 1; 1.17 Pre-release 2; 1.17.1; 21w37a; 21w38a; 21w39a; 21w40a; 21w41a; 21w42a; 1.18 Pre-release 1; 1.18 Pre-release 4; 1.18 Pre-release 5; 1.18 Release Candidate 2; 1.18; 1.18.1; 22w03a; 1.18.2; 22w12a; 22w15a; 22w18a; 1.19 Pre-release 2; 1.19 Pre-release 5; 1.19; 1.19.1; 1.19.2; 22w42a; 1.19.3; 23w06a; 23w07a; 1.20 Release Candidate 1; 1.20; 1.20.1 Release Candidate 1; 1.20.1; 1.20.2; 1.20.4; 24w13a; 1.20.5 Pre-Release 1; 1.20.6; 1.21; 1.21.1; 24w33a
- **Fix versions:** 24w36a
- **Area:** Platform
- **Labels:** honey_block; ice; rendering; slime_block; stripes
- **Watchers:** 1
- **Attachments:** 35
- **Attachment filenames:** 2013-10-27_21.38.25.png; 2013-10-27_21.41.44.png; 2014-05-13_10.32.47.png; 2014-05-13_10.38.55.png; 2014-05-13_11.03.30.png; 2014-06-23_14.35.41.png; 2015-06-09_15.51.45.png; 2015-10-04_13.46.33.png; 2018-02-21_21.13.39.png; 2018-02-22_19.26.48.png; 2018-02-22_19.26.50.png; 2018-02-22_19.27.14.png; 2018-03-04_16.14.56.png; 2018-07-14_01.05.02.png; 2018-07-14_01.05.53.png; 2018-07-17_01.02.57.png; 2018-07-19_15.43.07.png; 2018-08-21_12.50.01.png; 2019-02-06_20.52.15.png; 2019-10-10_11.11.14.png; 2019-11-16_16.06.39.png; 2020-05-12_23.19.22.png; 2020-05-12_23.40.14.png; 2020-06-05_13.06.04.png; 2020-06-05_13.06.14.png; Analysis 1.png; Analysis 2.png; Analysis 3.png; Analysis 4.png; crash-2014-05-13_10.54.01-client.txt; crash-2014-07-02_19.22.27-client.txt; Example Superflat.png; Ice Rendering pre6.gif; Screenshot (5).png; Screenshot-Slime-Light-Bad.png
- **Issue links:** Duplicate:inward:MC-275667:Frozen river ice being wrongly rendered | Relates:outward:MC-277808:Translucency sorting does not work correctly for large models | Relates:inward:MC-173723:Sometimes after loading a chunk, the grass and water colors on some blocks are not correct | Relates:inward:MC-268155:Rendering gaps in the world under specific conditions | Relates:inward:MC-186362:Casting issue: Translucent block rendering breaks down at high distances | Relates:inward:MC-261456:Chunk borders are sometimes visible in water | Duplicate:inward:MC-162672:Subtle light-grey/see-through squares appearing on ice | Relates:outward:MC-9553:Wrong rendering order of particles, hitboxes, clouds, transparent blocks, breaking animations and various other transparent textures | Duplicate:inward:MC-242025:Glass doesn't render properly behind other layers of glass | Duplicate:inward:MC-260342:Ice from far away renders more transparently | Duplicate:inward:MC-242394:Render bug | Duplicate:inward:MC-242393:渲染错误 | Duplicate:inward:MC-239997:Wall of stained glass with water behind it causes a visual bug/glitch | Duplicate:inward:MC-241794:Ice grid render bug | Duplicate:inward:MC-239376:Transparent Ice Blocks rendering | Duplicate:inward:MC-179562:Stained glass and water visual glitch | Duplicate:inward:MC-239011:Ice rendering issues | Duplicate:inward:MC-236819:Ice Makes Boarders Along the Chunk Boarder | Duplicate:inward:MC-39233:Shadow and Ice bugs | Relates:inward:MC-128066:Highly transparent block edges on ice, slime block and honey block | Duplicate:inward:MC-185536:Glass Blocks partially de-load when flying/moving around if the blocks are next to Water | Duplicate:inward:MC-181090:Blue glass placed one block above oceon/sea level causes it to sometimes go invisable | Duplicate:inward:MC-161241:Rarely, when Ice is viewed from a certain angle with water beneath it, it creates a gridlike pattern | Duplicate:inward:MC-161116:Ice Blocks Render Incorrectly | Duplicate:inward:MC-156238:Ice renders weirdly from a distance | Duplicate:inward:MC-153003:Ice rendering isusues | Duplicate:inward:MC-151180:glacier chunks render weird | Duplicate:inward:MC-149667:ice turns invisable | Duplicate:inward:MC-148446:ice rendering glitch | Duplicate:inward:MC-137243:Frost walker boots revealing water underneath ice | Duplicate:inward:MC-134740:Graphic glitch with ice on 1.13 (full-release) | Duplicate:inward:MC-130195:Weird rendering of ice | Duplicate:inward:MC-127570:Weird texture bug with ice. | Duplicate:inward:MC-127299:Ice side texture glitch | Duplicate:inward:MC-126576:Ice on Frozen Ocean loads oddly | Duplicate:inward:MC-126055:ice blocks render glitch | Duplicate:inward:MC-115787:Large sheets of ice render strangely when flying over them | Duplicate:inward:MC-105623:Can See Through Ice At Chunk Borders | Duplicate:inward:MC-104274:Ice rendering Glitch | Duplicate:inward:MC-97730:Boat Ice Viewing Glitch | Duplicate:inward:MC-81195:Slime Block Lighting Bug | Duplicate:inward:MC-50406:Ice in large quantities renders badly from distance. | Duplicate:inward:MC-62421:Ice looks strange from different angles | Duplicate:inward:MC-38842:Ice turns to Water

## Description

The bug
Various visual artifacts appear on translucent blocks after movement, because whatever handles sorting translucency layers does not update as you move around.
How to reproduce
- Create a superflat world with preset:

```
minecraft:bedrock,minecraft:green_stained_glass,minecraft:red_stained_glass,minecraft:blue_stained_glass;minecraft:the_void
```

- Fly up ~10 blocks (doesn't matter much)

- Use this command:

```
/tp @p 100 ~ 100 135 45
```

- Press F3 + T (then wait for chunks to load)

- Use this command:

```
/tp @p 0 ~ 0 -45 45
```
→  You will notice you cannot see the green and red glass in multiple chunks

Expected behaviour
The block faces would be sorted on each frame, so that they always render in the correct order.
Analysis
 has done a good analysis in this comment.
 has done a good analysis in this comment.

## Comments (90)

### Comment 1: migrated (2013-10-27T13:39:50.526-0700)

This comment contained multiple image attachments (35), please login to view the attachments.

### Comment 2: migrated (2014-05-13T01:57:10.734-0700)

Duplicated by MC-38842
Happened to me in 14w19a with an Intel HD 4000, mipmapping or anisotropic filtering turned off.
How to reproduce
- Create New World

- Select "Customized" World type

- Choose "FrozenOcean" biome

Attached crash report.

### Comment 3: kumasasa (2014-05-13T10:53:42.330-0700)

Reopened, not a duplicate of MC-35881

### Comment 4: kumasasa (2014-05-13T10:57:01.870-0700)

@: You can probably update to OX X 10.9.x for free https://itunes.apple.com/us/app/os-x-mavericks/id675248567?mt=12

### Comment 5: migrated (2014-05-13T11:13:22.980-0700)

Same result with another computer using an Intel HD 5000 and running OS X 10.9.2.
@Kumasasa This OS X version is too unstable on my computer

### Comment 6: kumasasa (2014-05-13T11:17:21.803-0700)

WTF ? Unstable software made by Apple ? Impossible....
@all: Anyone having this issue: Please force a crash by pressing F3 + C for 10 seconds while in-game and attach the crash report ([minecraft/crash-reports/crash-<DATE>-client.txt|http://hopper.minecraft.net/help/finding-minecraft-data-folder]) here.

### Comment 7: migrated (2014-05-13T11:25:40.839-0700)

@Kumsasa Hehe, yet I couldn't shut down it without pressing power button, or the computer turned off itself after 5 minutes, etc.

### Comment 8: migrated (2014-06-23T05:35:55.695-0700)

Confirmed for 14w25b.

### Comment 9: migrated (2014-07-02T11:06:15.928-0700)

Confirmed for 14w27b, on Windows 7 64-bit with latest Java 1.8 and Nvidia GTX 670.
The graphical bug seems to occur largely independent of video settings. I have toggled all video settings and the only setting where I was unable to reproduce the bug was with a Render Distance of 2 chunks. With any Render Distance higher than 2 chunks and any other (combination of) video settings I was able to reproduce the graphical glitch.
The only way the glitch disappears is when the rendering resets (for instance when changing certain video settings) or when the player gets closer to the ice.

### Comment 10: migrated (2014-08-25T11:20:12.447-0700)

Confirmed for 1.8pre2 with a GTX 750 Ti

### Comment 11: migrated (2014-11-24T06:50:38.879-0800)

Confirmed for 1.8.1

### Comment 12: Artimipa (2015-04-06T13:12:47.641-0700)

Confirmed for 1.8.3, on Windows 8.1 64-bit with latest Java 1.8 and Nvidia GeForce GT 640M.

### Comment 13: migrated (2015-11-05T10:55:06.452-0800)

Confirmed for 15w45a

### Comment 14: migrated (2015-11-12T06:25:08.551-0800)

Can't reproduce in 15w46a. Is this fixed?

### Comment 15: migrated (2015-11-12T11:21:12.633-0800)

Was able to reproduce this in 15w46a, so this is not fixed.

### Comment 16: migrated (2015-11-12T12:14:16.037-0800)

Indeed, not fixed. Create a superflat world with this preset and fly around a bit: 3;minecraft:bedrock,20*minecraft:water,minecraft:ice

### Comment 17: migrated (2015-11-18T11:55:57.499-0800)

Confirmed for 15w47a and 15w47c

### Comment 18: migrated (2015-12-20T05:50:24.070-0800)

Confirmed for 15w51b

### Comment 19: migrated (2016-02-18T10:02:36.546-0800)

Confirmed for 1.9-pre1 and 1.9-pre2

### Comment 20: migrated (2016-06-22T16:54:42.223-0700)

I believe this might have to do with the block transparency.

### Comment 21: migrated (2016-11-06T03:10:58.172-0800)

Is this still an issue in the latest snapshot 16w44a? If so please update the affected versions.
This is an automated comment on any open or reopened issue with out-of-date affected versions.

### Comment 22: migrated (2016-12-03T00:38:27.956-0800)

Confirmed for 1.11

### Comment 23: jamesmoton (2018-02-21T13:30:38.223-0800)

Confirmed for 18w08a and is way more prevalent now.

### Comment 24: migrated (2018-02-22T09:28:38.847-0800)

This bug sadly ruins the new Frozen Ocean biome. Added some pics from 18w08b

### Comment 25: migrated (2018-03-04T06:18:23.969-0800)

Confirmed in 18w09a

### Comment 26: migrated (2018-03-23T04:52:09.105-0700)

Confirmed in 18w11a

### Comment 27: muzikbike (2018-04-11T09:45:54.499-0700)

Affects 18w15a

### Comment 28: muzikbike (2018-05-18T13:16:49.992-0700)

Affects 18w20c

### Comment 29: migrated (2018-05-31T13:33:40.577-0700)

Confirmed for 18w22c

### Comment 30: muzikbike (2018-06-04T14:13:35.933-0700)

Affects 1.13-pre1

### Comment 31: _zombiehunter (2018-06-22T07:09:53.626-0700)

1.13-pre3

### Comment 32: muzikbike (2018-06-27T16:02:42.768-0700)

Affects 1.13-pre4

### Comment 33: migrated (2018-06-29T13:28:42.199-0700)

Confirmed for 1.13-pre5 with slimeblocks

### Comment 34: ZeNico13 (2018-07-05T00:47:16.145-0700)

Also affects 1.13-pre6

### Comment 35: ZeNico13 (2018-07-13T16:07:39.178-0700)

Affects 1.13-pre8

### Comment 36: ZeNico13 (2018-07-16T16:03:50.184-0700)

Affects 1.13-pre9

### Comment 37: ZeNico13 (2018-07-17T12:01:06.245-0700)

Affects 1.13-pre10

### Comment 38: ZeNico13 (2018-07-18T10:23:37.850-0700)

Confirmed for 1.13-release!

### Comment 39: ZeNico13 (2018-07-27T02:19:22.788-0700)

Still in 18w30b

### Comment 40: ZeNico13 (2018-08-05T06:40:39.690-0700)

Still in 18w31a

### Comment 41: ZeNico13 (2018-08-08T07:30:55.350-0700)

Still in 18w32a

### Comment 42: ZeNico13 (2018-08-15T12:06:49.908-0700)

Still in 18w33a

### Comment 43: ZeNico13 (2018-08-16T09:59:18.679-0700)

Still in 1.13.1-pre1

### Comment 44: migrated (2018-08-20T21:54:47.843-0700)

this happens at chunk borders for me in 1.13

### Comment 45: ZeNico13 (2018-08-22T09:25:55.443-0700)

Still in 1.13.1 release

### Comment 46: ZeNico13 (2018-10-16T14:37:23.192-0700)

Still in 1.13.2-pre1

### Comment 47: ZeNico13 (2018-10-21T10:00:06.627-0700)

Still in 1.13.2-pre2

### Comment 48: ZeNico13 (2018-10-25T00:26:17.597-0700)

Still in 18w43b

### Comment 49: migrated (2018-12-21T05:16:57.485-0800)

Still in 18w50a

### Comment 50: ZeNico13 (2019-02-06T12:00:11.824-0800)

Still in 19w06a despite the fact that the rendering engine has changed.

### Comment 51: ZeNico13 (2019-02-13T09:31:14.179-0800)

Still in 19w07a

### Comment 52: ZeNico13 (2019-02-20T08:06:57.258-0800)

Still in 19w08a

### Comment 53: ZeNico13 (2019-02-27T09:58:27.816-0800)

Still in 19w09a

### Comment 54: ZeNico13 (2019-03-13T13:46:17.629-0700)

Still in 19w11a

### Comment 55: ZeNico13 (2019-03-14T11:45:34.746-0700)

Still in 19w11b

### Comment 56: ZeNico13 (2019-03-22T08:22:02.438-0700)

Still in 19w12b

### Comment 57: [Mod] Neko (2019-03-23T15:43:57.587-0700)

Gave the report to  since the original reporter is inactive.

### Comment 58: migrated (2019-10-03T11:33:15.184-0700)

I can't reproduce the ice glitch in 19w40a.
I think it might've been fixed by the new rendering engine.

### Comment 59: [Mod] violine1101 (2019-10-08T06:00:06.213-0700)

I don't think this can be marked as fixed just yet, the latest snapshot has major issues with mipmaps, causing a moire effect to appear on ice. This issue didn't seem to appear with mipmaps disabled in 1.14.4 either, so we can't be sure it's been fixed just yet.

### Comment 60: ZeNico13 (2019-10-10T02:13:40.008-0700)

No, this bug is still effective despite the new rendering engine!

### Comment 61: migrated (2019-11-11T06:43:42.301-0800)

Confirmed in 19w45b

### Comment 62: migrated (2020-02-07T10:07:23.024-0800)

Confirmed in 20w06a

### Comment 63: migrated (2020-02-15T03:35:11.497-0800)

Confirmed in 20w07a

### Comment 64: migrated (2020-05-25T08:24:23.063-0700)

I just made a post about this not realizing that it was already reported here. This is such a huge graphical bug that has been present for so long and I don't know why it hasn't been fixed yet. I really hope Mojang Studios can fix this in the next version of the game.

### Comment 65: migrated (2020-06-05T10:07:49.137-0700)

Confirmed in Pre-Release 2 for 1.16

### Comment 66: migrated (2020-08-26T10:46:06.592-0700)

this is an really old bug...I hope mojang can fix this because it last for years so it should be considered to fix in higher priority

### Comment 67: SunCat (2020-08-26T13:28:15.788-0700)

It already has "Important" priority. On the other hand, the fact that it's an old bug doesn't make it automatically important, the severity of the issue and how much it affects gameplay / players does

### Comment 68: migrated (2020-08-27T05:32:33.622-0700)

Yes, but it's had "Important" Priority since February, and the bug has existed for 7 years. That's too long for any bug to exist in this game. And I would say that it affects the severity of the gameplay greatly, seeing as literally any water build mixed with glass looks terrible when close to it. It would be 1 thing if this glitch didn't load the glass from barely out of chunk distance, but it can happen as close as 2 chunks away.

### Comment 69: migrated (2021-05-28T14:08:29.368-0700)

Can confirm in 1.17-pre1.

### Comment 70: ampolive (2021-08-23T06:56:33.873-0700)

Can confirm in 1.17.1.

### Comment 71: ampolive (2021-10-06T18:15:45.363-0700)

Can confirm in 21w39a.

### Comment 72: ampolive (2021-10-11T17:28:15.913-0700)

Can confirm in 21w40a.

### Comment 73: migrated (2021-10-13T11:59:23.946-0700)

Can confirm in 21w41a.

### Comment 74: Ceresjanin123 (2021-10-24T05:22:39.092-0700)

Can confirm in 21w42a. Also this appears to be related to chunk borders. As you can see in this screenshot these square patterns align perfectly with chunk borders

### Comment 75: ampolive (2021-11-12T09:16:35.027-0800)

Can confirm in 1.18 Pre-release 1.

### Comment 76: ampolive (2021-11-17T15:42:08.356-0800)

Can confirm in 1.18 Pre-release 4.

### Comment 77: migrated (2021-11-26T05:09:15.256-0800)

Confirmed in 1.18 Release Candidate 1.

### Comment 78: Avoma (2021-12-08T05:02:59.246-0800)

Can confirm in 1.18.

### Comment 79: migrated (2021-12-10T05:07:33.334-0800)

Can confirm in 1.18.1.

### Comment 80: migrated (2022-03-11T23:41:56.795-0800)

I can confirm in 1.18.2
(seems to be happening extremely frequently for me)

### Comment 81: pulpetti (2022-05-24T06:31:15.721-0700)

In 1.19 Pre-2.

### Comment 82: Avoma (2022-07-07T03:21:07.350-0700)

This also affects stained glass. It would probably be worth updating this ticket to mention this to potentially prevent further duplicate reports in the future.

### Comment 83: Avoma (2022-07-29T07:37:14.949-0700)

Can confirm in 1.19.1.

### Comment 84: migrated (2022-08-07T18:52:52.681-0700)

can confirm 1.19.1

### Comment 85: migrated (2023-10-06T09:06:34.441-0700)

Can confirm in 1.20.2

### Comment 86: Ceresjanin123 (2024-02-02T15:43:30.051-0800)

There is a lot of issues with this issue
Some are due to people confusing this bug with MC-9553. For example the "render like water" part from the title was caused in part by MC-9553 and hasn't been reproducible since it's been fixed. It's also specific to the ice + water setup, and isn't representative of the bug. The title also suggests "elevation and angle" has something to do with this but it doesn't, it happens at any angle. You can check that by pressing F3 + T and the bug will go away until you start moving again. Also the bug desc is really meagre, there's a lot more information that's missing.
I request the following be done:
1. Attachments 2015-06-09_15.51.45.png 2018-08-21_12.50.01.png Screenshot-Slime-Light-Bad.png are showing MC-9553 and not relevant and should be removed
2. Attachments crash-2014-05-13_10.54.01-client.txt crash-2014-07-02_19.22.27-client.txt 2014-05-13_11.03.30.png are not relevant and should be removed
2.5 All other attachments could be removed tbh since they're redundant. But idk your policy on that.
3. Update the title to "Order of rendering translucent block faces fails to update with camera position"
4. Update the description:
The Bug:
Various visual artifacts appear on translucent blocks after movement, because whatever handles sorting translucency layers does not update as you move around.
How to reproduce:
1. Create a superflat world with preset

```minecraft:bedrock,minecraft:green_stained_glass,minecraft:red_stained_glass,minecraft:blue_stained_glass;minecraft:the_void```
2. Fly up ~10 blocks (doesn't matter much)
3. Use command /tp @p 100 ~ 100 135 45
4. Press F3 + T (then wait for chunks to load)
5. Use command /tp @p 0 ~ 0 -45 45
6. You will notice you cannot see the green and red glass in multiple chunks
Analysis:
There's probably some kind of mechanism that calculates which translucent block faces are closest to the camera, and then sorts them into the correct rendering order, so that blocks render in front of each other as would be expected. However this ordering task seems to only run sporadically (once when a chunk loads, and again if you're close enough to the chunk). This obviously leads to issues where after your position changes blocks are "in front" of blocks that are now in front of them.
As of reproduction step 4 the top face of a red glass block is in front of (closer to the camera) two side faces of the blue glass block above it.
As we teleport behind it the order should switch (the top face of the red glass block is now behind those two blue faces) however the rendering thingy doesn't realize this and still thinks the top face of the red glass is in front of the two blue faces. Because of this mismatch the red glass block doesn't render properly behind those two block faces.

Note: The "two faces" I'm talking about are invisible because the block faces are culled when two of the same translucent block are next to each other. However you can see it's indeed the side faces trying to render behind the red glass, by making a hole in the glass thus making them visible.
Corroborating evidence:
What I just described with the glass world is also what's going on with the ice (the water is ordered "in front" of the two inside faces of ice, while it's actually behind them) and before the fix to MC-9553 was implemented the water would actually follow this incorrect order and render in front of the ice.
And indeed if we load up our glass world before MC-9553 was fixed and repeat the steps we'll notice the red glass blocks are actually rendering in front of the blue glass (and the green renders in front of both). This confirms my analysis I think
However after that fix, when such mismatch occurs the pixels that are incorrectly "in front" of something don't render at all which is why it looks different now. However it's still the same issue!
Expected behaviour
The block faces would be sorted on each frame, so that they always render in the correct order.

### Comment 87: migrated (2024-02-20T10:46:12.394-0800)

Can confirm 1.20.4, singleplayer default world, probably outside of simulation distance

### Comment 88: ZeNico13 (2024-04-11T14:14:20.226-0700)

Many thanks to  for his very detailed comment!

### Comment 89: douira (2024-04-30T19:48:34.059-0700)

Hi, I'd like to give an explanation for why this is happening, what possible solutions are, and why this is a hard problem in general. I just finished writing my Master's thesis about solving translucency sorting in Minecraft, with the implementation having been done in Sodium. My last year was spent trying to solve this problem efficiently, with the result being a sophisticated approach that solves it correctly and with low overhead by replacing quad distance sorting with different sorting techniques. The problem is, that if you dig into the how the geometry behaves, it quickly becomes either a graph or a spatial partitioning problem. Even accepting that sorting quads by distance does not always yield a correct result, it's not clear exactly when quad distance sorting needs to be performed.
Looking at the code, Minecraft checks if sorting needs to be performed every time the camera movement is more than 1 block away from the last time sorting was performed. Then, it iterates through all visible sections and sorts at most 15 of them per frame. It selects either any section if the camera has just crossed a chunk boundary, or specifically sections that are axis aligned with the camera ("axis-sharing"), where at least one axis of the section's coordinates is the same as the camera's section coordinates. Intuitively, this makes sense, since as you move the camera the ordering becomes wrong and needs to be re-done. As most geometry is axis aligned, performing sorting preferentially on axis-sharing sections is an okay approximation.
The bug in this report happens when the camera gets into a position where the sort order of a section is invalid but isn't updated since either the camera has not moved enough to trigger sorting or the sorting budget was prematurely exhausted. Teleporting means the camera registers a movement, but then resets the "last sort position" to the current position without having sorted all sections with invalidated sort orders. If it moves a little, unless it moves across a section border, only axis-sharing sections will be sorted, which doesn't resolve the visual glitch. Additionally, if the camera moves in a specific way near sensitive sections, the allowance of 15 sections getting sorted per frame could get repeatedly exhausted, thus starving certain sections of sorting altogether. Layered water and glass or different types of stained glass showcase the problem very easily, because the camera only needs to move a relatively small angle relative to the section before artifacts become visible. This angle depends on the geometry and the perspective on the section.
A simple fix might be to sort sections even when the camera has not moved and to prioritize which sections get sorted based on how long ago they were sorted, or based on the position the camera was at when the section was last sorted. The problem remains that sorting sections by distance is expensive, especially when it needs to happen very frequently to mitigate bugs like this one. There's a lot of optimizations and different approaches that can be applied to Minecraft's surprisingly tractable translucency sorting problem, albeit with the introduction of significant complexity as I showed in my work.
I hope this helps, I'm happy to answer any more questions about the translucency sorting problem should they arise.

### Comment 90: migrated (2024-10-12T10:59:44.260-0700)

@douira This is unrelated to this bug, however i need answers from you regarding a bug you mentioned you used to encounter or maybe still do, specifically bug MC155104. I am getting this consistently on 1.21. Did you ever find a fix for this? Please get back to me as soon as you can.
