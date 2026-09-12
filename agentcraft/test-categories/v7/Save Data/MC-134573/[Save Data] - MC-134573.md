# MC-134573: The game freezes while doing a world backup

**Mojira URL:** [https://bugs.mojang.com/browse/MC-134573](https://bugs.mojang.com/browse/MC-134573)

## Report details

- **Mojira categories:** Save Data; UI
- **Project:** MC
- **Issue key:** MC-134573
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2018-07-22T08:45:30.540-0700
- **Updated:** 2026-02-03T01:44:21.732-0800
- **Resolution date:** 2026-02-03T01:44:21.681-0800
- **Affects versions:** Minecraft 1.13; Minecraft 18w30b; Minecraft 18w31a; Minecraft 1.13.1-pre1; Minecraft 1.13.1; Minecraft 1.13.2-pre1; Minecraft 1.13.2-pre2; Minecraft 1.13.2; Minecraft 18w43a; Minecraft 18w43b; Minecraft 19w11b; Minecraft 19w12b; Minecraft 19w13b; Minecraft 19w14a; Minecraft 19w14b; Minecraft 1.14 Pre-Release 1; Minecraft 1.14 Pre-Release 2; Minecraft 1.14 Pre-Release 3; Minecraft 1.14 Pre-Release 4; Minecraft 1.14 Pre-Release 5; Minecraft 1.14; Minecraft 1.14.1 Pre-Release 1; Minecraft 1.14.1; Minecraft 1.14.2 Pre-Release 1; Minecraft 1.14.2 Pre-Release 2; Minecraft 1.14.2 Pre-Release 3; Minecraft 1.14.2 Pre-Release 4; Minecraft 1.14.2; Minecraft 1.14.3 Pre-Release 2; Minecraft 1.14.3 Pre-Release 3; Minecraft 1.14.3 Pre-Release 4; Minecraft 1.14.3; Minecraft 1.14.4 Pre-Release 1; Minecraft 1.14.4 Pre-Release 2; Minecraft 1.14.4 Pre-Release 3; Minecraft 1.14.4 Pre-Release 4; Minecraft 1.14.4 Pre-Release 5; Minecraft 1.14.4 Pre-Release 6; 1.14.4; 19w39a; 1.15.2; 20w11a; 20w15a; 20w19a; 20w22a; 1.16.2; 20w49a; 1.16.5; 21w06a; 21w08b; 1.18.1; 1.19; 1.19.2; 1.19.3; 1.19.4 Pre-release 4; 1.19.4; 1.20.1 Release Candidate 1; 1.20.1; 1.21.1; 24w36a; 1.21.4; 25w03a
- **Fix versions:** 26.1 Snapshot 6
- **Area:** Platform
- **Labels:** backup; backup-screen; lag; world; world-conversion
- **Votes:** 1
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** image-2018-07-22-17-33-40-482.png; launcher_log.txt; MC-134573.png; screenshot-1.png
- **Issue links:** Duplicate:inward:MC-279667:The game is stuck while creating a backup | Duplicate:inward:MC-146438:There's no loading screen for backing up a world, causing the game to freeze momentarily | Duplicate:inward:MC-223143:Minecraft is Freezing every time I try to create a backup

## Description

Hi. Whenever I optimize a large world Minecraft will freeze for me while doing the necessary backup.
Steps to Reproduce:
- Click on Optimize World (1.12 world)

- Click 'Backup and Load'

- See how Minecraft will freeze after a while.

OR:
- Click on Edit World

- Click 'Make Backup'

- See how Minecraft will freeze after a while.

For the test purpose I used the Białowieża Forest map showcased on Minecraft.net some time ago. This world is about 18GB large (~8GB bigger than our average server worlds). It will however finish doing the backup after a while and then start to run the chunk upgrade process which runs smoothly again.
I've also uploaded a picture showcasing the problem. Yeah, my CPU is at 99%, but Minecraft had two full threads and about 10% of my CPU for this task so this shouldn't be a problem (while the OS drive and the drive Minecraft is installed on had also little work to do). The problem here seems to be (just guessing) that the backup process is being done in the same thread as the render thread instead of a worker thread.

## Comments (26)

### Comment 1: migrated (2018-07-22T08:45:30.540-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: qwerty23495 (2018-08-05T13:50:19.431-0700)

We do not have enough information to find the cause of this issue.
After having this issue, please attach the full launcher log file found in [.minecraft/launcher_log.txt|http://hopper.minecraft.net/help/guides/minecraft-logs/] here.

### Comment 3: migrated (2018-08-05T16:36:08.127-0700)

Ok, I just added the launcher log to the issue (after it appeared again. After the backup was done and thus the world upgrade happens I clicked cancel as the world upgrade itself isn't affected).
Afterwards I tested it again with the same world and it happened again (look at screenshot-1 for details). For this test I also decided to have the log output window open to better see what the log put's out when it occurs and afterwards.
Also note that whether this issue occurs depends on the world size. Smaller worlds aren't affected, thought I haven't figured out the smallest necessary world size for the issue too occur, thus I'm always going with the largest map I've got as I know that it will definitly happen on this map size.

### Comment 4: migrated (2018-08-05T18:02:16.825-0700)

I've also found out, the issue also applies to the normal backup functionality of Minecraft (see the updated description of the issue) and worlds as small as 460MB on my SSD also cause the issue to occur, so no need for a multiply gigabyte world to force this issue to occur (at least on my system).

### Comment 5: Ezekiel (2018-08-24T08:24:01.128-0700)

This happens for me as well. It is because the game is not running the backup on a second thread, so it is freezing while it is copying the files.

### Comment 6: migrated (2018-10-17T09:51:12.220-0700)

I could also reproduce this on Minecraft 1.13.2-pre1.

### Comment 7: migrated (2018-10-18T08:04:25.247-0700)

Please do not mark unreleased versions as affected.
You don't have access to them yet.

### Comment 8: migrated (2018-10-18T08:08:59.426-0700)

I could reproduce the problem on Minecraft 1.13.2-pre2, even thought this Bot thinks the version hasn't been released yet. My Minecraft Launcher tells me it has been released.

### Comment 9: migrated (2019-06-15T10:53:20.694-0700)

It's still a problem on Minecraft 1.14.3 Pre-Release 3.

### Comment 10: migrated (2019-07-04T10:37:32.120-0700)

Minecraft 1.14.4 Pre-Release 2 is still affected (I can't edit the affected versions on mobile).

### Comment 11: migrated (2020-01-29T10:11:31.088-0800)

It's still a problem in 1.15.2.

### Comment 12: migrated (2020-05-20T08:49:21.912-0700)

In addition to freezing, while frozen Minecraft won't allow me to switch to other programs because the graphics is frozen displaying minecraft.  It unfreezes the display when the backup completes.  It would be VERY helpful if I could see progress on the backup.

### Comment 13: Avoma (2021-02-10T04:26:51.740-0800)

Can confirm in 21w05b.

### Comment 14: Avoma (2021-02-16T10:02:48.389-0800)

Can confirm in 21w06a.

### Comment 15: Avoma (2021-03-08T00:56:40.655-0800)

Can confirm in 1.16.5 and 21w08b.

### Comment 16: MMK21 (2021-12-03T22:50:33.035-0800)

Affects 1.18

### Comment 17: MMK21 (2021-12-11T07:33:52.658-0800)

Affects 1.18.1

### Comment 18: numeritos (2022-01-05T08:14:30.339-0800)

This should be fixed by adding a % screen like when you load a world, and also of course using a worker thread instead of the render one

### Comment 19: Avoma (2022-07-16T04:23:52.122-0700)

Can confirm in 1.19.

### Comment 20: Avoma (2022-10-15T06:29:31.949-0700)

Can confirm in 1.19.2.

### Comment 21: Avoma (2022-12-22T01:47:16.551-0800)

I've removed the environment field of this ticket since this problem here doesn't appear to be environmentally exclusive.

### Comment 22: Brevort (2023-03-09T07:06:41.704-0800)

Can confirm in 1.19.4-pre4. As Alan said, the game becomes completely unresponsive and if you are fullscreened you can't tab out to other programs, which is quite frustrating.

### Comment 23: migrated (2023-04-18T07:39:19.903-0700)

I can confirm the issue for 1.19.4

### Comment 24: migrated (2023-04-18T09:23:29.597-0700)

Something i noticed is the game unfreezes and finishes the backup in windowed mode, however it forces me to force close the program on fullscreen.

### Comment 25: Brevort (2023-06-09T12:07:59.802-0700)

Affects 1.20.1 Release Candidate 1.

### Comment 26: Maximus_3069 (2026-01-31T16:00:38.318-0800)

Can confirm in 1.21.11
