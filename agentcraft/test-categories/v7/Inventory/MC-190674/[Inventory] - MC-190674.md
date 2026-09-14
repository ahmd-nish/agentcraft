# MC-190674: Shift clicking banners out of loom causes ghost items

**Mojira URL:** [https://bugs.mojang.com/browse/MC-190674](https://bugs.mojang.com/browse/MC-190674)

## Report details

- **Mojira categories:** Inventory; Items
- **Project:** MC
- **Issue key:** MC-190674
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2020-06-20T03:05:00.174-0700
- **Updated:** 2025-04-29T11:58:02.738-0700
- **Resolution date:** 2023-10-19T03:04:16.851-0700
- **Affects versions:** 1.15.2; 1.16 Release Candidate 1; 1.16; 1.16.4; 20w49a; 20w51a; 21w03a
- **Fix versions:** 21w10a
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** Banner Bug.mp4
- **Issue links:** Relates:outward:MC-192577:If holding down swap hands key over output of furnace, item occasionally is invisible until updated

## Description

The bug
When you shift-click banners out of the banner input slot of a loom while you already have an incomplete stack of that type of banner in your inventory, it will both stack with that incomplete stack and create another separate ghost item.
Video
The video shows the bug. Even though the video was filmed on a machine which doesn't meet the minimum requirements (which is why the loom background is dark), I have confirmed this bug to also be present on newer machines and other operating systems.
How to reproduce
- Have multiple banners of the same type (so they can stack) in your inventory.

- Open a loom.

- Put a part (not all) of the banners into the loom, so that there is at least one incomplete stack in your inventory, which can accept an amount equal to or lower than the amount of banners in the loom to become a complete stack. (In other words, if you have N number of banners in the loom, the stack in you inventory should be 16 - N or smaller).

- Shift click the banners out of the loom back into your inventory.

- The banners from the loom will now have combined with the existing stack, and created a ghost stack.

## Comments (9)

### Comment 1: migrated (2020-06-20T03:05:00.174-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: migrated (2020-06-20T09:54:55.634-0700)

Confirmed this in 1.16 RC-1

### Comment 3: migrated (2020-06-23T07:04:37.725-0700)

Confirmed in 1.16

### Comment 4: migrated (2020-08-13T04:57:32.170-0700)

Quite a major bug imo, not even 'oficially' confirmed or put into a category. Not sure if they forgot about this one. But still there in 1.16.2

### Comment 5: Avoma (2020-12-03T01:52:44.893-0800)

Cannot reproduce in 20w49a.

### Comment 6: Jarno_Wit (2020-12-03T03:24:04.752-0800)

I can still reproduce in 20w49a.
Also, I added a step by step reproduction guide to the description. Could you confirm wether your reproduction attempt did follow this newly added guide, Avoma?

### Comment 7: SPGoding (2021-01-12T18:15:06.983-0800)

Can reproduce in 20w51a as well.

### Comment 8: j_p_smith (2023-10-18T18:20:44.188-0700)

Fixed in 21w10a.

### Comment 9: j_p_smith (2023-10-18T22:31:41.731-0700)

Note: The extra stack is visible for a split second in 21w10a through 1.17.1, but that seems like a separate issue (which no longer occurs anyway).
