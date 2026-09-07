# MC-100830: Horses glitch out and warning is logged in console when climbing up stairs

**Mojira URL:** [https://bugs.mojang.com/browse/MC-100830](https://bugs.mojang.com/browse/MC-100830)

## Report details

- **Mojira categories:** Mob behaviour; Player
- **Project:** MC
- **Issue key:** MC-100830
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2016-04-11T10:36:44.545-0700
- **Updated:** 2025-04-26T04:58:25.695-0700
- **Resolution date:** 2024-11-26T03:58:10.209-0800
- **Affects versions:** Minecraft 1.9.2; Minecraft 1.9.4; Minecraft 1.10; Minecraft 1.10.2; Minecraft 16w33a; Minecraft 16w35a; Minecraft 16w36a; Minecraft 16w38a; Minecraft 16w39a; Minecraft 16w39b; Minecraft 16w39c; Minecraft 16w40a; Minecraft 16w41a; Minecraft 16w42a; Minecraft 16w43a; Minecraft 16w44a; Minecraft 1.11 Pre-Release 1; Minecraft 1.11; Minecraft 16w50a; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 1.12 Pre-Release 5; Minecraft 1.12; Minecraft 1.12.1; Minecraft 1.12.2 Pre-Release 1; Minecraft 1.12.2 Pre-Release 2; Minecraft 1.12.2; Minecraft 17w50a; Minecraft 18w01a; Minecraft 18w02a; Minecraft 18w03b; Minecraft 18w05a; Minecraft 18w10d; Minecraft 1.13.1; Minecraft 19w14a; Minecraft 1.14 Pre-Release 3; Minecraft 1.14; 1.14.4; 19w37a; 1.15 Pre-release 1; 1.15.2; 20w11a; 1.16.1; 20w27a; 1.16.2 Pre-release 1; 1.16.2; 20w51a; 1.17 Pre-release 1; 1.17 Pre-release 2; 1.17 Pre-release 3; 1.17; 1.17.1 Pre-release 1; 1.17.1; 21w39a; 21w40a; 21w41a; 1.18 Pre-release 1; 1.18; 1.18.1 Pre-release 1; 1.18.1; 22w03a; 1.18.2; 1.19.2; 23w14a; 1.20.1; 23w40a; 1.21 Pre-Release 2; 1.21
- **Fix versions:** 24w45a
- **Area:** Platform
- **Labels:** horse
- **Watchers:** 1
- **Attachments:** 7
- **Attachment filenames:** 2024-05-31 21-51-22 - Camel.mp4; 2024-05-31 21-51-22 - Horse.mp4; 24W44A.JPG; javaw 2016-06-02 22-33-14-76.avi; MC-100830.png; mojira.png; Screen Shot 2016-04-11 at 1.35.35 PM.png
- **Issue links:** Relates:outward:MC-98421:Horse Movement Bug; Stuck on Block | Relates:inward:MC-248231:The server console is sometimes spammed with "PLAYER moved too quickly!" after a player switches dimensions or teleports long distances | Duplicate:inward:MC-261932:Game log spam "Horse (vehicle of Player) moved wrongly!" | Duplicate:inward:MC-231443:horse on stairs display jitters | Duplicate:inward:MC-226864:Shaky vision while riding horse diagonal on stairs. | Duplicate:inward:MC-154810:bug with horse going up through stairs | Duplicate:inward:MC-147523:Horse above certain speeds is glitching while going over a specific placement of blocks | Duplicate:inward:MC-137290:Horses going up stairs glitch out. | Duplicate:inward:MC-116635:The model of the horse blows when you climb stairs | Duplicate:inward:MC-101772:Horses rubberband on stairs

## Description

When climbing up blocks while riding a horse, the horse occasionally glitches slightly (it gets reset backwards by the server), and the "Horse moved wrongly!" warning is logged in the server console (or game log in singleplayer).
In particular, this happens almost always when walking up stairs with horses, although it doesn't appear to happen with slabs. However, this issue has also been reported to occasionally happen if there are no stairs involved (e.g. MC-147523).
Steps to Reproduce
- Summon a moderately fast horse, e.g. by using the command provided below.

```
/summon minecraft:horse ~ ~ ~ {attributes:[{id:"minecraft:generic.movement_speed",base:0.35d}],Tame:1b,SaddleItem:{count:1,id:"minecraft:saddle"}}
```

- Mount the horse and climb up stairs with it.

- As you do this, pay close attention to the horse's movement and frequently check the server console / game log.

Expected behaviour
The horse can properly walk up the stairs.
Actual behaviour
The horse is very slow walking up the stairs; additionally in the server console / game log, warnings of the following format are sent:

```
Horse (vehicle of <user>) moved wrongly! 0.5
```
Notes
This is a new problem since the 1.9 update, and it happens with all horses, no matter their speed.
This also affects other entities than horses, however it appears most frequently with horses in regular gameplay. For example, camels with Speed II are also affected by this when sprinting, and so are pigs with Speed V.

## Comments (65)

### Comment 1: migrated (2016-04-11T10:36:44.545-0700)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: migrated (2016-04-11T10:59:02.446-0700)

Confirmed. I will also mention that I have started taking the same measures to avoid the glitch

### Comment 3: migrated (2016-05-09T14:21:14.818-0700)

can confirm

### Comment 4: migrated (2016-05-11T03:49:00.787-0700)

This is not just error logs. It manifests in game with a graphical glitch and more importantly slows down your horse.  It also effects Pc.

### Comment 5: migrated (2016-05-13T16:10:01.515-0700)

Same graphical glitch on PC running JRE_1.8.0_66 on Windows 7 pro x64 En.
AMD Radeon HD 6800 Series with Catalyst Version 15.7.1
The problem do not seems to happen when running down the stairs or running perpendicularly.

### Comment 6: hoyskedotte (2016-06-02T13:40:25.411-0700)

This is what it looks like for me. No problems when going up slopes of one block without the stairs

### Comment 7: migrated (2016-06-08T15:33:44.810-0700)

I've upgraded my server to the latest version, 1.10, and I can confirm that the bug STILL EXISTS. Horses still glitch, and the server log fills up with "moved wrongly" errors.

### Comment 8: migrated (2016-09-09T00:11:56.864-0700)

Confirmed in 1.10.2, 16w35a & 16w36a.

### Comment 9: migrated (2016-09-20T11:04:12.885-0700)

Confirmed in 16w38a

### Comment 10: migrated (2016-09-28T07:42:23.007-0700)

Confirmed in 16w39a

### Comment 11: migrated (2016-09-28T14:19:16.707-0700)

This is an issue in 1.10.2, on PC.

### Comment 12: SunCat (2016-09-28T14:36:19.169-0700)

1.10.2 is already marked as affected

### Comment 13: migrated (2016-09-28T20:49:19.188-0700)

I just wanted to confirm that I'm having the issue on PC. The environment is marked as Mac.

### Comment 14: migrated (2016-09-29T08:57:25.216-0700)

Confirmed in 16w39b

### Comment 15: migrated (2016-09-30T09:57:52.237-0700)

Confirmed in 16w39c

### Comment 16: migrated (2016-10-06T12:03:13.577-0700)

Confirmed in 16w40a

### Comment 17: migrated (2016-10-13T11:14:30.528-0700)

Confirmed in 16w41a

### Comment 18: migrated (2016-10-19T11:16:28.987-0700)

Confirmed in 16w42a

### Comment 19: migrated (2016-10-27T12:18:04.868-0700)

Confirmed in 16w43a

### Comment 20: migrated (2016-11-04T00:13:33.099-0700)

Confirmed in 16w44a

### Comment 21: migrated (2016-11-08T14:10:18.829-0800)

Confirmed in 1.11-pre1

### Comment 22: migrated (2016-11-14T14:38:44.076-0800)

Confirmed in 1.11

### Comment 23: migrated (2016-12-02T22:01:44.485-0800)

I also have this problem in 1.11

### Comment 24: SunCat (2016-12-02T22:05:12.358-0800)

, you don't need to confirm for a version that was already confirmed.

### Comment 25: migrated (2016-12-16T13:11:05.930-0800)

While this doesn't happen on slabs with average horse speeds, horses with high speeds or affected by speed potions can glitch out when climbing slopes made of slabs just as they would on stairs.

### Comment 26: migrated (2016-12-17T01:59:04.694-0800)

Confirmed in 16w50a

### Comment 27: migrated (2016-12-23T11:30:45.098-0800)

Confirmed in 1.11.2

### Comment 28: migrated (2017-06-28T11:54:45.769-0700)

Confirmed in 1.12
Also, of note, this only occurs when facing directly up the stairs.
If you turn your horse 90 degrees to the left or right and walk sideways up the stairs, then the issue no longer occurs. Unfortunately the horse is much slower like this.

### Comment 29: [Mod] bemoty (2017-08-10T10:53:57.305-0700)

Can confirm for MC 1.12.1.

### Comment 30: hoyskedotte (2018-03-11T03:38:27.080-0700)

Confirmed for 08w10d.

### Comment 31: migrated (2018-09-02T07:27:02.812-0700)

Confirmed for 1.13.1.

### Comment 32: migrated (2019-04-14T23:21:42.914-0700)

Can confirm 1.14 Pre-Release 2

### Comment 33: migrated (2019-04-17T00:03:29.006-0700)

Still occurs in 1.14 Pre-Release 3 as well.

### Comment 34: migrated (2019-04-17T19:31:03.568-0700)

Funny how the bug is 3 years old. Probably because it's not game-breaking.

### Comment 35: migrated (2019-04-24T03:29:23.424-0700)

Also still occurs in 1.14 (release).

### Comment 36: hoyskedotte (2019-11-22T14:23:43.768-0800)

Confirmed for 1.15pre1

### Comment 37: hoyskedotte (2019-11-25T11:36:03.352-0800)

Confirmed for 1.15pre2

### Comment 38: hoyskedotte (2020-03-16T16:10:21.868-0700)

confirmed for 20w11a

### Comment 39: hoyskedotte (2020-06-27T12:35:51.916-0700)

Confirmed for 1.16.1

### Comment 40: numeritos (2020-07-02T02:26:24.595-0700)

Affects 20w27a

### Comment 41: hoyskedotte (2020-08-03T07:17:13.322-0700)

Affects 1.16.2-pre1

### Comment 42: migrated (2020-09-04T08:32:18.391-0700)

Affects 1.16.2

### Comment 43: Brevort (2021-01-01T17:08:59.195-0800)

Confirmed for 51a

### Comment 44: SoloAlguien (2021-05-30T15:23:36.271-0700)

Can confirm in 1.17 Pre-release 1.

### Comment 45: SoloAlguien (2021-05-31T14:21:48.330-0700)

Can confirm in 1.17 Pre-release 2.
Also, a command to summon a tamed horse with a saddle:

```/summon horse ~ ~ ~ {Tame:1b,SaddleItem:{id:"minecraft:saddle",Count:1b}}```

### Comment 46: SoloAlguien (2021-06-01T22:06:44.575-0700)

Can confirm in 1.17 Pre-release 3.

### Comment 47: SoloAlguien (2021-06-20T09:47:56.019-0700)

Can confirm in 1.17 and 1.17.1 Pre-release 1.

### Comment 48: SoloAlguien (2021-09-29T13:53:56.395-0700)

Can confirm in 21w39a.

### Comment 49: SoloAlguien (2021-10-10T13:47:30.707-0700)

Can confirm in 21w40a.

### Comment 50: SoloAlguien (2021-10-13T10:35:12.643-0700)

Can confirm in 21w41a.

### Comment 51: SoloAlguien (2021-11-11T11:56:25.643-0800)

Can confirm in 1.18 Pre-release 1.

### Comment 52: SoloAlguien (2021-12-03T16:26:54.489-0800)

Can confirm in 1.18 and 1.18.1 Pre-release 1.

### Comment 53: SoloAlguien (2021-12-17T23:14:54.333-0800)

Can confirm in 1.18.1.

### Comment 54: Avoma (2022-01-27T10:49:39.643-0800)

Can confirm in 22w03a.
This may be related to MC-189878 in some shape. In my testing, this error was logged more often when riding horses that were quite fast. Also, just for clarification purposes, this can occur when riding horses up any blocks and not just stairs.
The following errors were printed into the server log when traveling up blocks whilst riding a horse.

```[18:44:22 WARN]: Horse (vehicle of Avoma) moved wrongly! 0.9154393680846553
[18:44:22 WARN]: Horse (vehicle of Avoma) moved wrongly! 0.9379264280524708
[18:44:22 WARN]: Horse (vehicle of Avoma) moved wrongly! 0.9959850208405072
[18:44:24 WARN]: Horse (vehicle of Avoma) moved wrongly! 0.274036825005453
[18:44:24 WARN]: Horse (vehicle of Avoma) moved wrongly! 0.30618116676673424
[18:44:24 WARN]: Horse (vehicle of Avoma) moved wrongly! 0.764109538169123
[18:44:24 WARN]: Horse (vehicle of Avoma) moved wrongly! 0.8690581602023997
[18:44:27 WARN]: Horse (vehicle of Avoma) moved wrongly! 0.277247326405643
[18:44:29 WARN]: Horse (vehicle of Avoma) moved wrongly! 0.41302603970679286
[18:44:29 WARN]: Horse (vehicle of Avoma) moved wrongly! 0.2679860152220215
[18:44:31 WARN]: Horse (vehicle of Avoma) moved wrongly! 0.4108363110471487
[18:44:31 WARN]: Horse (vehicle of Avoma) moved wrongly! 0.4350203576792069
[18:44:31 WARN]: Horse (vehicle of Avoma) moved wrongly! 0.42216544097665576
[18:44:31 WARN]: Horse (vehicle of Avoma) moved wrongly! 0.39889599413755406
[18:44:31 WARN]: Horse (vehicle of Avoma) moved wrongly! 0.33812364641954673```

### Comment 55: SoloAlguien (2022-03-01T14:09:34.498-0800)

Can confirm in 1.18.2.

### Comment 56: Avoma (2022-09-27T09:07:45.955-0700)

Can confirm in 1.19.2. Here are some steps on how to go about easily reproducing this issue.
Steps to Reproduce:
- Start and join a server.

- Summon a moderately fast horse by using the following command.

```/summon minecraft:horse ~ ~ ~ {Attributes:[{Name:"minecraft:generic.movement_speed",Base:0.75}],Tame:1b,SaddleItem:{id:"minecraft:saddle",Count:1b}}```
- Mount the horse and climb blocks with it.

- As you do this, pay close attention to the horse's movement and frequently check the server console.

- Take note as to whether or not horses have glitchy movement when climbing blocks resulting in warnings being printed in the server console.

### Comment 57: Brevort (2023-04-17T17:31:52.056-0700)

Does this cause the horse to go all blinky for several seconds when it happens? Or make the horse stop moving completely?

### Comment 58: Brevort (2023-05-16T06:58:25.830-0700)

Can confirm in 1.20-pre1. The horse sometimes gets stuck indefinitely until you move your mouse around .

### Comment 59: TheWorfer27 (2023-08-06T19:36:08.667-0700)

Can confirm in 1.20.1

### Comment 60: hoyskedotte (2023-10-09T01:33:13.228-0700)

Can confirm 23w40a

### Comment 61: migrated (2024-07-24T16:38:10.417-0700)

Can confirm in 1.21, horses still glitch out a lot while climbing stairs

### Comment 62: hoyskedotte (2024-11-13T04:27:29.342-0800)

This seems to be fixed in 24w45a. Can somebody else confirm?

### Comment 63: Kabakci26 (2024-11-13T08:23:04.003-0800)

I also cannot reproduce this in 24w45a.

### Comment 64: muzikbike (2024-11-13T08:32:11.835-0800)

Is this the issue demonstrated here?: https://youtu.be/r2l2VUNMvwI?t=9m

### Comment 65: hoyskedotte (2024-11-26T03:56:14.516-0800)

Has been fixed by 24w45a. I am able to reproduce in 24w44a, as per screenshot of the log output. (24w44a.jpg)
