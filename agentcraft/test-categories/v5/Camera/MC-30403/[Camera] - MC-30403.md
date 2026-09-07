# MC-30403: Sprinting isn't canceled when dismounting rideable entities while sprinting

**Mojira URL:** [https://bugs.mojang.com/browse/MC-30403](https://bugs.mojang.com/browse/MC-30403)

## Report details

- **Mojira categories:** Camera
- **Project:** MC
- **Issue key:** MC-30403
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2013-09-07T08:26:25.857-0700
- **Updated:** 2025-04-30T06:00:08.460-0700
- **Resolution date:** 2022-12-19T05:04:21.945-0800
- **Affects versions:** Minecraft 13w36a; Minecraft 13w36b; Minecraft 1.7.2; Minecraft 1.7.4; Minecraft 14w02b; Minecraft 14w02c; Minecraft 14w05b; Minecraft 14w06b; Minecraft 14w07a; Minecraft 14w08a; Minecraft 1.7.5; Minecraft 14w11b; Minecraft 1.7.9; Minecraft 1.7.10; Minecraft 14w33c; Minecraft 14w34a; Minecraft 14w34b; Minecraft 14w34c; Minecraft 1.8; Minecraft 1.8.1-pre3; Minecraft 15w47c; Minecraft 1.9.1; Minecraft 1.9.2; Minecraft 16w14a; Minecraft 16w32b; Minecraft 1.11; Minecraft 17w06a; Minecraft 1.12.1; Minecraft 1.12.2 Pre-Release 1; Minecraft 1.12.2 Pre-Release 2; Minecraft 1.12.2; Minecraft 17w43a; Minecraft 17w43b; Minecraft 17w45a; Minecraft 17w48a; Minecraft 17w50a; Minecraft 18w09a; Minecraft 1.13-pre1; Minecraft 1.13-pre3; Minecraft 1.13-pre6; Minecraft 1.13-pre10; Minecraft 1.13; Minecraft 18w30b; Minecraft 18w31a; Minecraft 1.13.1; Minecraft 1.13.2-pre2; 1.14.4; 1.15 Pre-release 3; 1.15; 1.15.1; 1.15.2; 20w13b; 20w17a; 20w18a; 20w19a; 20w21a; 20w22a; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 4; 1.16 Pre-release 5; 1.16 Pre-release 6; 1.16 Pre-release 7; 1.16 Pre-release 8; 1.16; 1.16.1; 20w29a; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4; 20w46a; 20w51a; 21w03a; 21w05b; 21w06a; 21w07a; 21w11a; 21w13a; 21w14a; 21w17a; 1.17; 1.17.1 Pre-release 1; 1.17.1 Pre-release 2; 1.17.1 Pre-release 3; 1.17.1 Release Candidate 1; 1.17.1; 21w38a; 21w39a; 21w40a; 21w41a; 21w42a; 1.18 Pre-release 1; 1.18 Pre-release 6; 1.18; 1.18.1; 22w03a; 22w05a; 22w06a; 22w07a; 1.18.2 Release Candidate 1; 1.18.2; 22w14a; 22w17a; 22w19a; 1.19; 1.19.1; 1.19.2; 22w42a; 22w43a; 22w44a; 22w45a
- **Fix versions:** Minecraft 14w34d; 22w44a; 23w03a
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 2022-11-02_23.55.09.png; MC-30403.mp4; MC-30403.png
- **Issue links:** Relates:inward:MC-256831:Camel "moved wrongly" output when using ability in a cobweb | Relates:inward:MC-256543:Dashing Camels stop dash momentum when rider dismounts it mid dash | Relates:outward:MC-29711:"Sprinting" While flying | Relates:inward:MC-256506:Camels riding entities get permanently stuck in dash mode | Duplicate:inward:MC-256560:Camals keeps running when player dashes with them in a boat | Duplicate:inward:MC-256592:Dashing on a Camel while its on a boat gets it stuck on dash animation | Duplicate:inward:MC-256610:Camel's dashing animation not stopping while in a vehicle | Duplicate:inward:MC-256634:Camel in Boat using dash ability | Duplicate:inward:MC-256667:camel dash bug | Duplicate:inward:MC-256762:Camel doesn't stop dashing in boat even after you get out | Duplicate:inward:MC-257023:Camel animation error | Duplicate:inward:MC-257037:Camel raft or boat (with / without chest) rides and endless walks on the boat or raft (with / without chest) | Relates:inward:MC-256512:Camels with no gravity won't stop their dash animation while in the air

## Description

The Bug:
Sprinting isn't canceled when dismounting rideable entities while sprinting.
When dismounting a rideable entity while you're sprinting, your sprinting state doesn't reset; you'll need to stop and start sprinting again in order to reset it.
Steps to Reproduce:
- Spawn a saddled pig, mount it, and hold the sprint key.

- Dismount the pig while sprinting and take note of how you're still in the sprinting state (as indicated by the change in FOV) even if you slow down.

- Stop and start sprinting again by pressing the sprint key moving and forwards before stopping.

- Take note of how sprinting is now canceled (as indicated by the change in FOV).

Observed Behavior:
Players continue to sprint after dismounting entities even if you slow down.
Expected Behavior:
Players would stop sprinting after dismounting entities when they slow down.

## Comments (40)

### Comment 1: migrated (2013-09-07T08:26:25.857-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: galaxy_2alex (2013-09-07T08:42:30.499-0700)

Relates to MC-29711

### Comment 3: migrated (2014-01-15T11:07:20.710-0800)

Still an issue in 13w02c.

### Comment 4: migrated (2014-03-02T01:35:03.730-0800)

Still an issue in 1.7.5 and 14w08a

### Comment 5: migrated (2014-04-22T08:12:52.388-0700)

Confirmed for 1.7.9 and 14w11

### Comment 6: migrated (2014-07-29T14:00:32.921-0700)

Is this still a concern in the current Minecraft version 14w30c or later? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 7: migrated (2014-08-20T07:05:52.083-0700)

confirmed for 14w34d

### Comment 8: Torabi (2014-08-20T09:28:20.427-0700)

Actually, I'm seeing this as fixed, along with MC-29711. Sprinting while swimming wading, or riding a horse, boat, or minecart both changes the FOV and increases movement speed, but pressing sprint while riding a minecart no longer does either.

### Comment 9: migrated (2014-08-20T09:38:56.824-0700)

Why is an unfixed bug being resolved as fixed? I tested it in 14w34d 10 seconds ago. FOV changes in minecarts, boats, on horses and in water when trying to sprint. To sprint you need to hold the forward button and press the sprint button. Double tapping forward does not work on the other side. And now you can actualy fly faster by sprinting since 14w43d, thats cool.

### Comment 10: Torabi (2014-08-20T09:48:18.168-0700)

Because I just tested it, and believe that it's been fixed. Double-tapping doesn't seem to work, but the sprint key does. Further testing with a stopwatch, instead of just eyeballing it, confirms that this hasn't actually been fixed.

### Comment 11: migrated (2014-08-20T09:51:42.566-0700)

And it should not. It basicaly gives you the impression that everything in-game has 2speeds.

### Comment 12: galaxy_2alex (2014-08-20T09:56:50.327-0700)

Reopened.

### Comment 13: migrated (2014-08-20T10:18:15.387-0700)

In addition it looks like sprinting under water and walking has also the same speed.

### Comment 14: migrated (2015-11-25T10:45:14.005-0800)

Affects 15w47c

### Comment 15: migrated (2015-11-26T14:12:58.973-0800)

Still in 15w47c. I only tested swimming. Works only if you press the sprint key, double tapping forward does not work. What is wierd is, that I did some speed testing and 'sprint swimming' was consistenly faster than swimming. I had 2 block deep water. Maybe this came from touching the ground?

### Comment 16: migrated (2016-04-09T00:52:15.662-0700)

Sill in 1.9.2 / 16w14a
Also works with Elytra
(and in case of minecart and boat, the particles of sprinting appear below me)

### Comment 17: migrated (2016-11-06T03:10:18.253-0800)

Is this still an issue in the latest snapshot 16w44a? If so please update the affected versions.
This is an automated comment on any open or reopened issue with out-of-date affected versions.

### Comment 18: tryashtar (2016-11-30T20:56:08.530-0800)

Still here up through 1.11.
Also, reports that describe how sprinting in these scenarios also creates particles are marked as duplicates of this, although this report does not mention it (some comments do).

### Comment 19: pokechu22 (2018-02-14T13:31:47.164-0800)

As of 18w07a, swimming now activates a special mode and as such is not affected by this issue.

### Comment 20: migrated (2018-10-20T09:09:51.341-0700)

Confirmed for 1.13.2-pre2.

### Comment 21: migrated (2020-06-08T04:21:54.757-0700)

Confirmed for 1.16 Pre-release 2.

### Comment 22: migrated (2020-06-10T15:19:08.041-0700)

Confirmed in 1.16-pre3.

### Comment 23: migrated (2020-06-11T12:58:37.409-0700)

Confirmed in 1.16-pre4.

### Comment 24: migrated (2020-06-12T14:11:29.641-0700)

Confirmed in 1.16-pre5.

### Comment 25: migrated (2020-06-17T02:20:39.573-0700)

Confirmed in 1.16-pre7.

### Comment 26: numeritos (2020-06-20T16:38:27.740-0700)

Affects 1.16-rc1

### Comment 27: Avoma (2020-12-23T03:12:27.838-0800)

Can confirm in 20w51a.

### Comment 28: Avoma (2021-01-29T12:02:52.856-0800)

Can confirm in 21w03a.

### Comment 29: Avoma (2021-02-05T09:09:30.803-0800)

Can confirm in 21w05b.

### Comment 30: Avoma (2021-02-12T05:37:48.799-0800)

Can confirm in 21w06a.

### Comment 31: Avoma (2021-02-19T02:49:45.611-0800)

Can confirm in 21w07a. Video attached.

### Comment 32: Brevort (2021-02-23T10:38:07.237-0800)

This even occurs if you are riding a horse with no saddle!

### Comment 33: Avoma (2021-03-29T05:38:26.229-0700)

Can confirm in 21w11a.

### Comment 34: Avoma (2021-04-06T10:42:26.307-0700)

Can confirm in 21w13a.

### Comment 35: Avoma (2021-04-11T03:03:55.281-0700)

Can confirm in 21w14a.

### Comment 36: Avoma (2021-04-30T09:38:14.462-0700)

Can confirm in 21w17a.

### Comment 37: Avoma (2021-06-17T04:40:53.936-0700)

Can confirm in 1.17.

### Comment 38: Avoma (2022-11-01T10:06:51.287-0700)

I've refined this ticket a little in order to fix grammar errors and precisely state the problem in a tad bit more detail. I hope this is okay.

### Comment 39: [Mod]Les3awe (2022-11-02T08:56:24.569-0700)

Still affects camels in 22w44a.

### Comment 40: Avoma (2022-11-02T09:15:30.881-0700)

Following on from what  said, this issue appears to have only been fixed for horses, donkeys, and mules. Other rideable entities such as pigs, striders, and camels are still affected.
