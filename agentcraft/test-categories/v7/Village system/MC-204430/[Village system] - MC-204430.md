# MC-204430: Cauldrons filled with water, lava or powder snow cannot be used as a workstation for villagers

**Mojira URL:** [https://bugs.mojang.com/browse/MC-204430](https://bugs.mojang.com/browse/MC-204430)

## Report details

- **Mojira categories:** Block states; Village system
- **Project:** MC
- **Issue key:** MC-204430
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2020-11-06T11:13:55.547-0800
- **Updated:** 2025-04-15T10:21:23.121-0700
- **Resolution date:** 2022-09-01T15:38:42.854-0700
- **Affects versions:** 20w45a; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 21w05a; 21w05b; 21w06a; 21w07a; 21w08a; 21w08b; 21w10a; 21w11a
- **Fix versions:** 21w13a
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** MC-204430.mp4
- **Issue links:** Relates:inward:MC-227469:Leatherworker villagers use the lava cauldron or powder snow cauldron produces water sounds | Relates:inward:MCPE-43961:Villagers lose their job site association with cauldrons filled with lava

## Description

The bug
Because filled cauldrons have been seperated into different blocks, water, lava and powder snow cauldrons don’t work as a workstation to get leatherworker villagers anymore.
How to reproduce:
- Place a cauldron

- Spawn a villager

-  The villager will link to it

- Put water or lava in it
 The villager will unlink from the cauldron.

## Comments (10)

### Comment 1: migrated (2020-11-06T11:13:55.547-0800)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: migrated (2020-11-06T11:19:31.187-0800)

Can confirm

### Comment 3: Avoma (2020-11-06T12:19:01.178-0800)

Hey there!
Just to let you know, I wasn't able to reproduce this in bug in 1.16.4 however, I was able to in 20w45a.

### Comment 4: migrated (2020-11-06T13:07:13.269-0800)

The reason why this can’t be reproduced in 1.16.4 is, because empty cauldrons and cauldrons with water are not seperated in in 2 blocks in 1.16.4. In the snapshot they have been seperated, which also caused MC-203617 to be a thing.

### Comment 5: migrated (2020-11-07T04:17:52.281-0800)

So a cauldron standing outside in the open, filling up with water from rain, will become invalid for villagers as a workstation, even if they have already claimed it as a workstation?

### Comment 6: migrated (2020-11-11T08:57:03.692-0800)

Affects 20w46a
Additionally affects Powder Snow Cauldron

### Comment 7: migrated (2021-01-10T20:38:58.050-0800)

Since villages only naturally generate water cauldrons this has also made leatherworker villagers unable to spawn naturally (or they immediately lose their profession upon generation).

### Comment 8: migrated (2021-02-05T11:24:57.217-0800)

I would suggest separating and marking as not-a-bug for cauldrons filled with lava.

### Comment 9: Avoma (2021-02-17T11:25:20.487-0800)

Can confirm in 21w07a.

### Comment 10: Avoma (2021-02-27T06:45:17.817-0800)

Video attached.
