# MC-184530: Player movement at low speeds is biased towards cardinal directions

**Mojira URL:** [https://bugs.mojang.com/browse/MC-184530](https://bugs.mojang.com/browse/MC-184530)

## Report details

- **Mojira categories:** Player
- **Project:** MC
- **Issue key:** MC-184530
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2020-05-19T12:10:16.090-0700
- **Updated:** 2025-04-26T10:05:39.907-0700
- **Resolution date:** 2025-01-13T23:12:40.155-0800
- **Affects versions:** 1.15.2; 20w20b; 20w21a; 1.17.1; 1.18.2; 22w15a; 23w51b; 1.21.3; 1.21.4 Pre-Release 1; 1.21.4
- **Fix versions:** 25w02a
- **Labels:** motion; movement; player; slowness
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** 2021-07-21_21.23.18.png; 2024-12-23_22.00.23.png; image-2020-05-19-15-03-19-610.png; image-2020-05-19-15-09-52-755.png; image-2020-05-19-15-11-51-939.png; image-2020-05-19-15-12-15-376.png
- **Issue links:** Relates:outward:MC-271065:Diagonal player movement is not normalized when holding two movement keys

## Description

When the player is sneaking or otherwise moving more slowly than normal, the angle at which they walk gets biased to align with the closest cardinal direction. This effect is most pronounced when the player's angle is only slightly off from the nearest cardinal direction.

Easy way to reproduce and visually demonstrate:
- Go to a flat plane (i.e. a superflat world) and set down two command blocks adjacent to each other, one Impulse and one Repeating.

- In the Repeating command block, put in "/execute as @a as @s run summon minecraft:armor_stand ~ ~ ~ {Small:1b}". This will produce a trail of Armor Stands when the block is powered, to record the player's movement path.

- Select a position in the world about 10 blocks away from the command blocks, in any cardinal direction.

- Create a teleport command that will put you at that specific position. Include the two extra fields for the camera angle, such that the yaw is 6 degrees off from the nearest multiple of 90, pointing you towards the command blocks. I.e. if the position you selected is directly South of the command blocks, the yaw field would need to be 174 or 186.

- Copy the teleport command into the Impulse command block, and then place a lever directly on either command block.

- Aim at the lever, lift your mouse off the table to avoid adjusting your angle manually, and activate the lever.

- Hold W until you are close to the lever, then stop moving and turn it off.

- Repeat step 6

- Hold W and Shift until you are close to the lever, then stop moving and turn it off

- Observe the difference in angle between the two lines of Armor Stands - when sneaking, your angle was flattened out towards the closest cardinal direction.

Expected behaviour: The magnitude of the player's velocity should have no effect on the angle.
Image of the completed set of steps, creating two lines of Armor Stands representing paths of movement:
Edited version with labels:

## Comments (11)

### Comment 1: migrated (2020-05-19T12:10:16.090-0700)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: migrated (2020-05-20T21:37:10.214-0700)

Affects 20w21a

### Comment 3: ampolive (2021-07-21T17:23:29.779-0700)

Can confirm in 1.17.1.

### Comment 4: pulpetti (2022-04-15T02:40:01.502-0700)

In 1.18.2

### Comment 5: Ceresjanin123 (2024-12-23T15:50:49.017-0800)

Can confirm in 1.21.4

### Comment 6: migrated (2025-01-03T21:22:03.616-0800)

This is because whenever your velocity on an axis reachs <.003*slipperiness*0.91 (<.005*slipperiness*0.91 before 1.9), it will be set to 0 for the next calculations since it is "negligible". This code was put in to let the player shift at the edge of a block without having to wait for their velocity to perfectly hit 0 (for instance, in minecraft 1.0.0, this wasn't implemented, and you had to wait ~20 seconds before unshifting, otherwise you would fall off the edge).
In the case of shifting on normal ground in versions above 1.9, if you're at a speed <.00549 on an axis, then you will never accelerate properly on that axis, which causes the issue. In your example, you move at a speed of .00307, which triggers the bug. Fixing this bug would require removing that piece of code, which would require recoding shifting at edges (which they probably should, it is very buggy with ice).

### Comment 7: Dhranios (2025-01-03T22:06:15.030-0800)

It doesn't need to be removed, it just needs to be changed to check total velocity, not per-axis.

### Comment 8: Ceresjanin123 (2025-01-04T02:49:40.077-0800)

I don't know why you mentioned what the formula was before 1.9. It's not relevant anymore and just makes your comment more confusing to read
What would have been more helpful is what version added it as you mention it didn't exist in 1.0.0

### Comment 9: J Z (2025-01-08T11:21:30.005-0800)

This was fixed in 25w02a.

### Comment 10: migrated (2025-01-08T20:38:25.317-0800)

Sorry, I just wanted to be somewhat rigorous with my explanation. Making it not per-axis does solve this issue. However, even after the fix, it still affects other parts of the game, such as shifting at the edge of ice, and other more specific/less important bugs. This is mostly why I saw removing that part of the code as a better choice, since it would remove all of those other issues aswell. Sorry for bringing up older versions.

### Comment 11: GamerGever (2025-01-13T23:12:40.155-0800)

now that this issue is resolved, I'd suggest to open a new report for the other instances of the bug remaining, and in that report you could detail the root cause and point Mojang towards the direction to fix all of them at once and remove unnecessary code.
