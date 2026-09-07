# MC-156663: Villager pathfinding broken in water

**Mojira URL:** [https://bugs.mojang.com/browse/MC-156663](https://bugs.mojang.com/browse/MC-156663)

## Report details

- **Mojira categories:** Mob behaviour; Village system
- **Project:** MC
- **Issue key:** MC-156663
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2019-07-13T06:23:24.627-0700
- **Updated:** 2025-04-30T06:13:21.809-0700
- **Resolution date:** 2022-11-22T04:19:55.951-0800
- **Affects versions:** Minecraft 1.14.4 Pre-Release 5; 1.15.2; 20w15a; 20w16a; 20w17a; 20w18a; 20w19a; 20w20a; 20w22a; 1.16.1; 1.16.4; 20w49a; 1.17.1; 22w12a
- **Fix versions:** 1.19.3 Pre-release 1
- **Labels:** mob; pathfinding; water
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2019-07-13_09.20.30.png; 2020-03-09_12.45.58.png; 2020-03-09_12.47.52.png; test-setup.png
- **Issue links:** Relates:inward:MC-245697:Certain mobs can't get out of water that is at least two blocks deep

## Description

The bug
I have already seen the "fixed" bug report MC-151333 but the villagers still get stuck in the water. I have been trying to make a swamp village in a part of swampland that has no exposed land anywhere but the villagers keep jumping in the water and once they do they just swim in it.
I have found that the pathfinding is broken in where they still swim in the water but they can't seem to detect a bed where they need to swim out of the water and then onto land to get to it. As soon as I push the villager onto land he goes to the bed.
In the picture below a villager is in the water right beside a bed at night but isn't going into it.
How to reproduce
See @ in this comment and this video.

## Comments (17)

### Comment 1: migrated (2019-07-13T06:23:24.627-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: migrated (2020-03-09T04:49:25.252-0700)

Still present in 1.15.2
The villagers pathfinding in water is really bad, even thoug, they seem to try to pathfind throgh water when standing on land but as soon as they enter the water, their pathfinding breaks and they usually loose their work and bed.
I have hovever noticed that it depends on how deep the water is at the edge between land/water. If the edge is 1 block deep only, then the villagers are able to pathfind out of the water easily enough, but if the water is 2 blocks or more deep, then they cannot.
As can be seen from the screenshots. 1. Villager in a puddle of water 2 block deep is unable to pathfind correctly to land and aquire a job.
As soon as i place a block in the water so there is only 1 block depth agains the edge of the land/water, the villager aquires the job and starts pathfinding out of the water.

### Comment 3: migrated (2020-03-09T05:02:59.845-0700)

Here's a video showing the behaviour https://youtu.be/iaydB_oyMjI

### Comment 4: migrated (2020-03-26T05:03:51.084-0700)

This bug is still happening in 20w13a

### Comment 5: migrated (2020-04-09T11:25:51.856-0700)

Still present in 20w15a, the villagers happily walks into the water but can not pathfind out of it again, rather problematic with them getting stuck in the water.

### Comment 6: bugi74 (2020-04-09T12:57:51.087-0700)

(Testing on 1.15.2)
Seems that villagers happily find their paths through (or more like into) 2 block deep pits, whether it has water or not.  It could be that the path finding routine simply ignores water, and thus does not consider that the villager is actually floating and could step on the shore. For the routine, the villager is stuck "virtually on the bottom" until the water's floor/ground has a path of 1 block steps out of the bottom. (Or seems to work like so.)
I think this might apply to many more mobs than just villagers.
Possibly the solution could be to somehow make pathfinding consider floatable (and safe) liquids in a special way (considering the 2nd liquid block from top as solid with high movement cost). Alternately, if the entity can still move in the water towards some edges, check a special case of pathfinding from the current real position (floating high in the topmost water) to next block (whether that is shore or something in the deep), which might allow the crucial step of getting forward enough for the normal pathfinding to work its way further. The latter way might be easier to implement, but may also fail with some arrangements.

### Comment 7: migrated (2020-04-15T08:59:50.561-0700)

still present in 20w16a

### Comment 8: migrated (2020-04-24T05:41:43.265-0700)

Still present in 20w17a
May I request ownership of this ticket?

### Comment 9: migrated (2020-04-29T13:18:43.654-0700)

Still present in 20w18a

### Comment 10: migrated (2020-05-07T06:48:40.304-0700)

Still present in 20w19a

### Comment 11: migrated (2020-05-13T11:42:34.773-0700)

still present in 20w20a

### Comment 12: migrated (2020-05-29T11:21:18.564-0700)

still present in 20w22a

### Comment 13: migrated (2020-06-10T10:59:27.372-0700)

still present in 1.16 Pre-release 3

### Comment 14: pulpetti (2020-07-16T14:48:59.826-0700)

Still in 20w29a

### Comment 15: Avoma (2020-12-07T10:36:11.649-0800)

I am unable to reproduce this issue in 20w49a.

### Comment 16: bugi74 (2020-12-07T13:54:09.221-0800)

I was able to reproduce in 20w49a. They can still step up from 1 deep water, but not from 2 deep water.
However, if there are more than 1 villager in the "same spot" near land, as they keep pushing each other, they may start jumping, and one of them may get pushed on the land while jumping. A lone villager didn't get out.
My test case was to surround the village bell area (5x5 area) with 3 wide pool of water, with the innermost radius of the pool being 1 deep, rest 2 deep. Thus, when they want to get to the meeting, they will happily find their path all the way to bell area (on land), chat a while, but once the meeting is over and they should get back to work, all they do is to spread to outer edges, and can't get out (unless randomly "helped" by another villager).
(Attached screenshot of the test setup ("test-setup.png").. well, trying to.)

### Comment 17: ampolive (2021-08-07T08:40:43.074-0700)

Can confirm in 1.17.1.
