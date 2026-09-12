# MC-278182: Items glitch inside the piston head when pushed through powder snow or cobwebs

**Mojira URL:** [https://bugs.mojang.com/browse/MC-278182](https://bugs.mojang.com/browse/MC-278182)

## Report details

- **Mojira categories:** Entities; Redstone
- **Project:** MC
- **Issue key:** MC-278182
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2024-11-07T17:36:00.329-0800
- **Updated:** 2025-10-02T04:33:54.946-0700
- **Resolution date:** 2025-10-02T04:33:54.867-0700
- **Affects versions:** Minecraft 1.14; 24w45a
- **Fix versions:** 1.21.10 Release Candidate 1
- **Area:** Platform
- **Labels:** item; piston
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** image-2024-11-08-02-26-10-600.png; image-2024-11-08-02-26-38-321.png; Item glitch bug world download.zip; Java_versions 2024.11.08 - 02.28.18.01.mp4
- **Issue links:** Relates:outward:MC-11293:Pistons push items the wrong way

## Description

Item entities can glitch inside the piston's head (block 36) upon being moved, if they are inside cobweb/power snow, and under some special conditions.
This issue is specially bad since powder snow being introduced (1.17) but it can be replicated in 1.14 with cobweb.
How to Replicate:
Open the world download attached in 1.14
Power the command blocks, which will summon multiple item entities
Power the piston
Expected behavior:
All entities move towards the next block, and exact same position for all
Observed Behavior:
Some entities glitch inside the piston head. This means they'll all randomly spread across the block.
As mentioned earlier, this issue becomes specially problematic for powder snow (1.17+), since this can be moved by pistons. Powder snow is very commonly used for item aligners, to slow down entities, etc. It is crucial to fix this issue. A video showcasing the issue will be attached too (recorded in 1.21).

## Comments (5)

### Comment 1: migrated (2024-11-07T17:36:00.329-0800)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: migrated (2024-11-07T17:57:07.963-0800)

This needs to be changed!

### Comment 3: migrated (2024-11-07T18:08:15.144-0800)

This is really important for reliably working with item entities. Please fix

### Comment 4: Viradex (2024-11-08T00:09:03.942-0800)

Can confirm.

### Comment 5: migrated (2024-11-10T11:21:55.998-0800)

this issue is related to MC-278255 , not  nor
