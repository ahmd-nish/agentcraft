# MC-295841: Interactive collision check path is broken

**Mojira URL:** [https://bugs.mojang.com/browse/MC-295841](https://bugs.mojang.com/browse/MC-295841)

## Report details

- **Mojira categories:** Collision
- **Project:** MC
- **Issue key:** MC-295841
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Community Consensus
- **Mojang priority:** Important
- **Created:** 2025-03-25T02:58:59.326-0700
- **Updated:** 2025-09-09T02:24:52.032-0700
- **Resolution date:** 2025-09-09T02:24:51.903-0700
- **Affects versions:** 1.21.5 Release Candidate 2; 1.21.5; 25w16a; 25w32a
- **Fix versions:** 25w32a; 25w37a
- **Area:** Platform
- **Votes:** 59
- **Watchers:** 4
- **Attachments:** 11
- **Attachment filenames:** 1_21_6_pr1.png; 2025-09-08_00.05.01-20250907-210502.png; 25w08a-20250324-233510 (389e08ab-2719-4bd9-be12-3a305b0afd6b).png; 25w09b-20250324-233448.png; Collision issue.zip; destination_position_fail_projectiles.zip; destination_position_fail_regular_entities.zip; image-20250907-205036.png; Screenshot 2025-09-07 225950-20250907-195951.png; Screenshot 2025-09-07 231538.png; wrong_movement_vector.zip

## Description

When an entity moves, it's supposed to trigger pressure plates and interact with such blocks along its path of motion.
In 24w33a a collision raycast was introduced to create that behavior, however, 25w09a changed it in a bad way.
• Previously (25w08a-) entities moving along all 3 axes in a single tick checked these blocks along their movement path:
(see attached screenshot called 25w08a), in it you can see that the interacted blocks lie all along a diagonal path from start to finish of the single tick movement of an entity. All of the blocks lie along the diagonal path (except the center is cut out, which was done to fix a crash issue MC-275437)
• Currently (25w09a+) entities, while moving along all 3 axes in a single tick, check the blocks along their corkscrew path, like in this picture:
(see attached screenshot called 25w09b), in it you can see that the interacted blocks lie along the corkscrew path of the entity, however the parts of the corkscrew path are missing. This is because now each separate cardinal movement is handled separately and the collision raycast is performed separately for each axis, and as stated above, said raycast is capped to not cause game crashes, thus it skips the middles of the movements along cardinal directions.
How to replicate:
- ﻿﻿﻿download the attached world, enter it in whichever version you want to observe the behavior (25w08a / 25w09b / 1.21.5-rc2).

- ﻿﻿﻿run/tp -2.53 76.00 5.53 to get to the setup.

- ﻿﻿﻿At the setup youll see 2 command blocks, one will spawn a fast tnt entity and highlight in red all of the strings it collided with in 1 tick. The second command block will clear the volume from red wool, in case you want to trigger the setup a second time, clear the volume before doing it.

- ﻿﻿﻿Observe the red wool blocks, they indicate which strings were successfully triggered by fast tnt.

Observed behavior:
- interactive collision checks follow a corkscrew path, with gaps in it

Expected behavior:
- Either: fast entities check their path along a diagonal for interactive collisions as they did in 25w08a

- Or:      fast entities check their path along a corkscrew for interactive collisions, but without gaps in it (and the total length of the edges of the corckscrew path is capped to prevent reintroduction of MC-275437), while still calling the interactive collisions at the movement destination point, regardless of the cap, as it did previously in 25w08a (this is important, as some redstone contraptions rely on entities being able to press pressure plates at the destination of their movement). Please notice, that implementing corckscrew path where each separate arm is in itself a raycast (as it is done now 25w09a+)  is very wastefull of performance as they can easily be replaced with much simpler logic while retaining the exact same behavior.

Both these options sound valid, unlike whatever it is currently doing in 1.21.5-rc2
Implications of current behavior(why its bad):
- ﻿﻿Currently (1.21.5-rc2) the entities will load the chunks outside the loaded area if shot fast enough (because one of the collision checks happens on the corner of the corckscrew, which lies outside render distance, when entity is shot far enough diagonally), they wont load their entire path, so it wont immideately crash the server as it did in MC-275437, but it drastically increases the lag from tnt warping cannons nonetheless :(

- ﻿﻿﻿Current;y (1.21.5-rc2) the interactive collisions (of non projectile entities) are only ever checked in lines that are aligned with the coordinate axis, yet they still use the raycast logic to process each line. The raycast was specifically written to handle diagonal movements, and is incredibly expensive compared to just a loop interating over a single coordinate which will suffice to cover an axis aligned line without loss of the behavior.

As now im unable to edit my own reports, please check the comments to see if i added any additional info to the report.
Code Analysis and Proposed Solution:
https://gist.github.com/VelizarBG/053a5590cc28413b7abb28c6b3704481
Credits:
Velizar (@VelizarBG) - Code Analysis and Proposed Solution
Update 1.21.6-pr1
Some refactoring was done in 1.21.6-pr1 which worsened this issue.
Now instead of using the Movement vector to determine which direction the corkscrew of the raycast is twisted, it uses the dispplacement vector to do that, which obviously leads to the Interactive-collision-raycast-corcwcrew to twist in the opposite direction compared to direction in which the regular block face collision of the movement is twisted. This makes it so that the Interactive blocks are triggered far away from the actual path taken by the entity
(see the screenshot attached in the comment from 28.05.25). In it the entity block face collision goes in order: +y, +x, +z. But the interactive collision cast goes in order: +y, +z, +x. which makes is go though a wall which it isnt supposed to be even close to. Thus it goes through a wall.

## Comments (11)

### Comment 1: Savvvage_ (2025-03-25T02:59:00.752-0700)

This comment contained an image attachment, please login to view the attachment.

This comment contained an image attachment, please login to view the attachment.

This comment contained an image attachment, please login to view the attachment.

### Comment 2: Savvvage_ (2025-03-25T03:28:53.098-0700)

The corkscrew path of interactive collision checks was likely implemented to fix the  in 25w09a, which makes sense, so it would make sense to continue with it using a corkscrew path instead of a diagonal, but without gaps, capped and triggering the endmost point of the motion regardless of the cap.
If you are interested, the current cap is hardcoded within the addCollisionsAlongTravel() method within the BlockGetter class. The cap is right now set to 16 iterations of the cast.

### Comment 3: Rozbiynik (2025-03-25T08:48:46.227-0700)

can confirm in 1.21.5-rc2

### Comment 4: Savvvage_ (2025-03-31T08:08:59.765-0700)

This issue is related to these 4 issues:

as it happens in almost the same place in code, mainly in the logic of the checkInsideBlocks() call and the logic of calls directly within it.

### Comment 5: Savvvage_ (2025-05-28T06:07:15.551-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 6: Savvvage_ (2025-08-05T08:58:22.938-0700)

Not fixed

### Comment 7: Savvvage_ (2025-08-05T12:54:22.276-0700)

As of 25w32a:
- The interactive collision check path still evaluates the corners of the corkscrew, which it should not do for the reasons outlined in the report above.

- The interactive collision path sometimes fails to visit the end position of the movement.

- The interactive collision path uses a movement vector that is not adjusted for block face collisions, causing it to differ from the actual direction of the entity's movement.

- The Entity.Movement#axisIndependant field appears to be misspelled in the official Mojang mappings. It should be “axisIndependent, although based on the implementation, “axisDependent” sounds more appropriate.

The replication setup provided in this report still behaves almost identically to how it did in 25w31a and earlier. This suggests the fix may not have been fully verified before the issue was marked as resolved.
This would be the 11th time we (TMC) have to re-report issues related to interactive collisions, and it’s becoming increasingly frustrating - for us, and likely for you as well. We would be happy to provide a working fix to help ensure the issue is resolved correctly and prevent further back-and-forth. If you’re open to accepting a fix from our side, please let us know by replying to this comment.

### Comment 8: Shugoh (2025-09-01T05:09:02.905-0700)

Hey , we would very much like to see this being resolved properly as well. Sorry to hear that there are still some issues remaining. We have a pending fix for not visiting the corkscrew corners. But it would be great to get some clarity on the other two issues you mention.

Could you expand on when the end position is not visited? Would be great to have a repro case for this. Could you also expand on the third point as well?

If you have any suggestions, that would also work great as an explanation.

### Comment 9: Savvvage_ (2025-09-07T14:10:43.597-0700)

Hello, sorry for the wait.
Here are the test setups and the explanations as requested:
In case with regular entities, end position of the movement is not visited because the visited_position_counter (i) never reaches 0 which makes it not execute the end position collision, here is the code:
Notice how the atomicInteger (inside the checkInsideBlocks) is not necessarily equal to the j when the checkInsideBlocks is exited, thus the retuned value is less than i, thus the i-=checkInsideBlocks is bigger than 0, thus the i<=0check fails.

Here is the replication setup:
To use it, just press the note block next to the sign saying “launch tnt“. It will automatically spawn a tnt and accelerate it, then it will let it move for exactly 1gt and kill it before it moves a second time. It will also spawn a nether star at the end position of the tnt’s movement, to show where the end position is, so that you can observe that no interactive collisions were performed there.
In case with projectiles, the end position of the movement is not visited, because the code for that is missing. Here is the replication setup:
The interactive collision path uses a wrong movement vector. What i mean by this:
The block face collisions (the .collide)
uses the velocity of the entity (the vec3) to determine which direction to twist the corkscrew of the block face collisions

But the interactive collisions use the displacement of the entity (the vec32) instead, to determine which direction to twist the corkscrew of the interactive collisions.
This makes the two corkscrews to sometimes twist in the opposite directions, which makes the path of the interactive collisions can go through walls, as shown in this screenshot:

In this case the block face collisions go in order: +y, +x, +z. But the interactive collision cast goes in order: +y, +z, +x. which makes is go though a wall.

Here is the showcase world for the twisting direction:
To use it, just press the note block next to the sign saying “launch tnt“. It will automatically spawn a tnt and accelerate it, then will let it move for exactly 1gt and kill it before it moves a second time.  Just look at the tnt velocity, think of the order in which it is supposed to twist the interactive collision corkscrew and compare to the observed order.

### Comment 10: stacked_dynamite (2025-09-07T15:21:57.112-0700)

With regards to the counter causing issues, another option - instead of using counters to stop the iteration - is to simply make the getBlockState call in Entity::checkInsideBlocks not chunk load. A similar example already exists the BlockCollisions class where it gets the ChunkAccess from Level::getChunkForCollisions - which does not chunk load - before calling getBlockState using the ChunkAccess.

### Comment 11: Shugoh (2025-09-09T02:05:06.307-0700)

Thanks for the additional information, and the test cases, this made it a lot more clear what was wrong. There are pending fixes for all of these issues described, and the test cases provided verify that. This issue will be resolved with these changes, but please let me know if there are any outstanding issues or any oversights.
