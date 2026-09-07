# MC-9232: When loading a world, the held item from the previously loaded world is briefly visible

**Mojira URL:** [https://bugs.mojang.com/browse/MC-9232](https://bugs.mojang.com/browse/MC-9232)

## Report details

- **Mojira categories:** Player Animation
- **Project:** MC
- **Issue key:** MC-9232
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2013-02-05T08:23:54.744-0800
- **Updated:** 2025-04-30T04:16:12.699-0700
- **Resolution date:** 2023-06-11T21:48:26.230-0700
- **Affects versions:** Minecraft 1.4.7; Snapshot 13w05a; Snapshot 13w05b; Minecraft 1.5; Snapshot 13w11a; Minecraft 1.5.1; Minecraft 1.5.2; Minecraft 1.6.1; Minecraft 1.6.2; Minecraft 1.7.4; Minecraft 14w06a; Minecraft 1.7.5; Minecraft 14w11b; Minecraft 14w17a; Minecraft 14w18a; Minecraft 14w19a; Minecraft 14w21b; Minecraft 14w25b; Minecraft 14w26b; Minecraft 14w27a; Minecraft 14w28a; Minecraft 14w28b; Minecraft 14w31a; Minecraft 14w32a; Minecraft 14w33a; Minecraft 1.8; Minecraft 1.8.1-pre3; Minecraft 1.8.1; Minecraft 1.8.2-pre1; Minecraft 1.8.2-pre4; Minecraft 1.8.6; Minecraft 15w44b; Minecraft 15w50a; Minecraft 1.9; Minecraft 1.10.2; Minecraft 16w32b; Minecraft 16w42a; Minecraft 16w43a; Minecraft 1.11; Minecraft 16w50a; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 1.12.2; Minecraft 17w50a; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w45a; Minecraft 18w46a; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 19w12b; Minecraft 19w13b; Minecraft 19w14a; Minecraft 19w14b; Minecraft 1.14; Minecraft 1.14.2; 1.14.4; 19w37a; 19w40a; 1.15 Pre-release 1; 1.15; 1.15.1 Pre-release 1; 1.15.2; 20w14a; 20w15a; 20w17a; 20w21a; 1.16 Pre-release 5; 1.16.1; 20w27a; 1.16.2; 1.16.3; 1.16.4; 20w48a; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w07a; 21w11a; 21w15a; 1.17; 1.17.1; 21w41a; 21w42a; 1.18 Pre-release 4; 1.18 Pre-release 6; 1.18 Pre-release 7; 1.18 Release Candidate 3; 1.18; 1.18.1 Release Candidate 1; 1.18.1
- **Fix versions:** 22w03a
- **Labels:** block; hand; held; hotbar; inventory; item; singleplayer; switches; world
- **Watchers:** 1
- **Attachments:** 5
- **Attachment filenames:** 2013-02-05_11.14.47_2.png; 2013-02-05_11.14.47.png; Bug-MC-9232.mp4; crash-2013-02-05_11.01.02-client.txt; MC-9232.mp4
- **Issue links:** Relates:inward:MC-132039:Players briefly spawn in wrong coordinates for one frame, holding item from a previous save game before being teleported without item | Relates:outward:MC-133703:Right hand shown for one tick after joining world, ignoring handedness | Duplicate:inward:MC-27398:Holding "fake" objects when loading worlds | Duplicate:inward:MC-55955:Item Held When Switching Worlds Not Changing | Duplicate:inward:MC-56645:Item of a previous world shown in the end when connecting. | Duplicate:inward:MC-99420:On New World Creation You Initially Hold Previous World's Possession | Duplicate:inward:MC-113449:Loading separate world hand bug | Duplicate:inward:MC-144751:Item displayed in hand when loading new world | Duplicate:inward:MC-147491:Item in hand when entering a new world | Duplicate:inward:MC-150140:Item from last world you played in renders when making a new world | Duplicate:inward:MC-152552:You appair with a bucket when you creates a world | Duplicate:inward:MC-166325:Items in hotbar from a previous world appear quickly when loading a new one. | Duplicate:inward:MC-167854:Entering a new world will still render the item held in hand in old world | Duplicate:inward:MC-177982:Held items display from wrong save file | Duplicate:inward:MC-189488:Held items from a previous world momentarily show up when first joining a new world | Duplicate:inward:MC-193284:Items still visually persist when creating a new world while tabbed out | Duplicate:inward:MC-195393:Visual glitch from changing worlds while holding items | Duplicate:inward:MC-199728:When Joining new world item appears from last | Duplicate:inward:MC-202228:Item visible in hand on new world when not there. | Duplicate:inward:MC-216054:Ghost appearance from previous game inventory when creating or changing maps | Duplicate:inward:MC-220331:why do i see an axe | Duplicate:inward:MC-232182:Visual bug after | Duplicate:inward:MC-232721:Shows off hand items from the previous world when loading in new world. | Duplicate:inward:MC-239607:Hand items appear in new World (visual glitch) | Duplicate:inward:MC-245013:Selected item from the previous world is still being held since game starts | Duplicate:inward:MC-248633:hand item shown from world before | Relates:inward:MC-5962:When first loading a world, chests and trapped chests have a visual glitch in hotbar | Relates:inward:MC-76679:Wrong hand position after going through portal / loading world (combined with missing item) | Relates:inward:MC-108945:The totem of undying appears on relog.

## Description

This happens in Singleplayer, any gamemode, especially on lower render distance.
Expected:
When loading a world, your hand should be holding the thing currently selected in the hotbar.
Actually seen:
Your hand starts out (briefly) holding the thing selected in the hotbar in the last world you were in, then it does the item-switching animation (lower hand holding previous item, raise hand now holding current item).
It's quick, so to reproduce it, try a few times.
Steps:
1) Have 2 worlds created.
2) In one world, select something from the hotbar so it's held in-hand, e.g. lime wool.
3) Save and quit, open the other world.  Select something else in-hand, e.g. nether brick.
4) Save and quit, open the first world again.  Your hand will lower the nether brick, and raise the lime wool.

## Comments (33)

### Comment 1: migrated (2013-02-05T08:23:54.744-0800)

This comment contained multiple image attachments (5), please login to view the attachments.

### Comment 2: migrated (2013-02-05T09:02:06.655-0800)

Confirmed.

### Comment 3: marcono1234 (2014-06-18T09:03:22.990-0700)

Confirmed for 14w25a
How to see it very clear:
-
- Open first world get dirt in your hand

- Close first world

- Open second world and while opening open another programm or minimize Minecraft

### Comment 4: migrated (2014-06-28T15:21:02.404-0700)

May relate to the bug where boss health bars are still visible for a moment after going into a different world/server.

### Comment 5: shufboyardee (2014-07-24T08:46:22.082-0700)

Fixed as of 25a.

### Comment 6: marcono1234 (2014-07-30T11:32:00.652-0700)

That is not fixed!
Confirmed for
- 14w31a

- Minecraft 1.8-pre 1

### Comment 7: Sonicwave (2014-10-05T14:27:26.502-0700)

Confirmed for 1.8.

### Comment 8: Sonicwave (2015-01-06T21:44:19.374-0800)

Confirmed in 1.8.2-pre1.

### Comment 9: shufboyardee (2015-07-30T11:59:38.929-0700)

This is definitely fixed as of 15w31a: you now always start initially (briefly) with an empty hand, rather than the item from the other world.

### Comment 10: migrated (2015-09-10T14:25:34.522-0700)

Your version of Minecraft is no longer supported. We are currently only accepting bugs found in the latest official release and the snapshot most recently released thereafter.
To change your game to a different version, start the launcher. Select Edit Profile. In the "Use Version" dropdown menu, select the game version you want. Then click Save Profile.
If you're able to reproduce this issue in the latest version of Minecraft, please open a new issue and attach a crash report from a supported version.
--- This action was performed automagically. If you believe this was done erroneously, please  raise an issue.

### Comment 11: migrated (2015-09-10T14:28:04.645-0700)

Your version of Minecraft is no longer supported. We are currently only accepting bugs found in the latest official release and the snapshot most recently released thereafter.
To change your game to a different version, start the launcher. Select Edit Profile. In the "Use Version" dropdown menu, select the game version you want. Then click Save Profile.
If you're able to reproduce this issue in the latest version of Minecraft, please open a new issue and attach a crash report from a supported version.
--- This action was performed automagically. If you believe this was done erroneously, please  raise an issue.

### Comment 12: shufboyardee (2015-09-10T14:30:20.482-0700)

Well, Arisa bot, that's because I've been trying to have some person mark it as fixed, for some time now, but you're a bot, so do whatever you like.  I suppose fixed/invalid it doesn't really matter.

### Comment 13: migrated (2015-10-31T12:09:46.471-0700)

Fixed in 15w31a.

### Comment 14: migrated (2015-11-01T04:26:58.896-0800)

Not fixed as of 15w44a.

### Comment 15: migrated (2015-11-01T08:27:34.922-0800)

Reopened.

### Comment 16: JUE13 (2017-12-27T00:28:18.063-0800)

Confirmed for 17w50a.

### Comment 17: migrated (2018-09-17T12:28:06.650-0700)

Confirmed for 1.13.1.

### Comment 18: migrated (2020-04-09T14:20:14.761-0700)

Confirmed for 20w15a.

### Comment 19: migrated (2020-06-01T13:05:11.959-0700)

Will mojang ever fix this bug?

### Comment 20: migrated (2020-06-13T14:50:08.936-0700)

Seems to affect 1.16-pre5; see MC-189488.

### Comment 21: Avoma (2020-12-01T09:46:03.290-0800)

Can confirm in 20w48a.

### Comment 22: Avoma (2020-12-24T03:11:17.803-0800)

Can confirm in 20w51a.

### Comment 23: Avoma (2021-01-29T12:01:54.472-0800)

Can confirm in 21w03a.

### Comment 24: Avoma (2021-02-05T12:04:43.795-0800)

Can confirm in 21w05b.

### Comment 25: Avoma (2021-02-12T05:08:36.627-0800)

Can confirm in 21w06a.

### Comment 26: Avoma (2021-03-27T03:20:55.495-0700)

Can confirm in 21w11a.

### Comment 27: Brevort (2021-04-16T19:46:21.196-0700)

Confirmed for 21w15a.

### Comment 28: windwend (2021-06-20T13:26:38.965-0700)

Can confirm for 1.17.

### Comment 29: ampolive (2021-07-05T14:17:28.429-0700)

Can confirm in 1.17.1 Release Candidate 2.

### Comment 30: ampolive (2021-10-13T11:04:38.984-0700)

Can confirm in 21w41a.

### Comment 31: ampolive (2021-10-20T09:31:13.615-0700)

Can confirm in 21w42a.

### Comment 32: ampolive (2021-11-17T11:43:30.349-0800)

Can confirm in 1.18 Pre-release 4.

### Comment 33: shufboyardee (2023-06-11T21:36:10.076-0700)

This is fixed since 1.18.2 snapshot 22w03a.
