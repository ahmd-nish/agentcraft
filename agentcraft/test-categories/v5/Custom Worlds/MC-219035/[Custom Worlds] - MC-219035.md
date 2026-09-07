# MC-219035: Fossil structures can't generate in far east and south blocks of a chunk

**Mojira URL:** [https://bugs.mojang.com/browse/MC-219035](https://bugs.mojang.com/browse/MC-219035)

## Report details

- **Mojira categories:** Custom Worlds; World generation
- **Project:** MC
- **Issue key:** MC-219035
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2021-03-11T05:22:05.711-0800
- **Updated:** 2025-04-29T21:25:10.913-0700
- **Resolution date:** 2021-11-16T10:59:37.385-0800
- **Affects versions:** 21w10a; 21w11a
- **Fix versions:** 1.18 Pre-release 1
- **Labels:** world-generation
- **Watchers:** 1
- **Attachments:** 7
- **Attachment filenames:** 2021-03-11_13.46.44.png; 2021-03-17_22.28.32.png; 2021-11-12_16.05.33.png; 2021-11-12_16.06.50.png; 2021-11-12_18.13.06.png; FossilBug-1.zip; FossilBug-1-18-pre-1.zip

## Description

When generating a fossil feature the structure is placed at a random position in the chunk. However this position never includes the far east and south blocks in that chunk (chunk coordinates X=15 or Z=15). This is most obvious when generating structures with size 15x15 as those are always placed at chunk coordinate 0, 0 leaving a one block gap.
(Note that the placement in a grid is not a bug as the feature explicitly makes sure that the structures do not cross chunk boundaries.)
How to reproduce:
- Create a world with the attached datapack

- Teleport to a savanna

- Go into spectator mode and fly downwards

- You will see the structures as in the image above

(Note that while this reproduction involves a datapack the bug also affects the vanilla fossils, although its much less obvious because of their smaller size and rarity)
Code analysis:
(using the official mappings and some variable renaming)
The position to place the structure in the chunk is calculated by
{color:#cc7832}int {color}x = random.nextInt({color:#6897bb}16 {color}- size.getX()){color:#cc7832};
 {color}{color:#cc7832}int {color}z = random.nextInt({color:#6897bb}16 {color}- size.getZ()){color:#cc7832};{color}
However, as the upper bound of random.nextInt is exclusive, the maximum value of x is 16 - size.getX() - 1. The structure would then reach to x + size.get(X) - 1 = 16 - 1 - 1 = 14

## Comments (4)

### Comment 1: migrated (2021-03-11T05:22:05.711-0800)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: jacobsjo (2021-11-12T07:30:12.254-0800)

Not fixed in 1.18 Pre-release 1.
1.18 Pre-release 1 added an in_square placement modifier. However this simply caused MC-241234. If (in a datapack), this placement modifier is not used, the fossil feature still does it's own placement inside the chunk, but is still unable to generate in the far east or south blocks of the chunk.
I've attached an updated Datapack to confirm this. This datapack generated two different fossil features in two layers.
- The bottom layer around Y=-30 generates fossils of size 15x15 to show the same issue still exists

- The top layer around Y=30 generates fossils of size 10x10, to show that this isn't simply the case because of the missing in_square placement modifier.

### Comment 3: ampolive (2021-11-12T13:12:43.263-0800)

Can confirm not fixed in 1.18 Pre-release 1. Please reopen this issue.

### Comment 4: jacobsjo (2021-11-16T10:59:37.385-0800)

Fixed in 1.18 Pre-release 2. No reopen necessary anymore. (Fossils are now supposed to be used with a in_square placement modifier)
