# MC-276317: Projectiles visually update slowly when their motion is changed

**Mojira URL:** [https://bugs.mojang.com/browse/MC-276317](https://bugs.mojang.com/browse/MC-276317)

## Report details

- **Mojira categories:** Commands; Networking; Projectiles
- **Project:** MC
- **Issue key:** MC-276317
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-09-04T09:51:33.514-0700
- **Updated:** 2025-04-26T16:37:51.265-0700
- **Resolution date:** 2024-09-10T08:25:51.792-0700
- **Affects versions:** 24w36a
- **Fix versions:** 24w37a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** es_reproducing.mp4; link to video-1.txt
- **Issue links:** Duplicate:inward:MC-276419:Freshly summoned arrows with copied-from-another-entity Motion tag fall flat before teleporting to where they were shot to.

## Description

When a projectile that also displays a direction such as an arrow or a trident has its Motion changed, it will visually continue to advance in its old trajectory in a chaotic manner.
In the attached video I am using a datapack that changes arrows Motion so that they follow already landed arrows, their behavior has not changed since 24w35a. but visually they continue to follow their old trajectory for a few seconds.
Video example: https://youtu.be/-czvnLJv1do?si=1nQcCMhHf0kDCp2w,

(The sky is not glitched, there's just a lot of glass)
Only projectiles that display their direction seem to be affected, so arrows, tridents and wither skulls. While snowballs, ender_pearls, or wind charges are not affected.
The delay in the visual update is not tied to any command, it instead appears to be universal, it does not matter if i use data modify, data merge, or if the arrow is hit with a wind charge in mid air, the correct motion will only be displayed after one second.
TNT explosions update the arrows visual motion correctly.
Steps to reproduce
- Join any world in 24w36a with cheats enabled.

- Using a bow and an arrow, fire in any direction.

- While the arrow is in the air, use the following command in the chat or with a command block:

```
/data merge entity @n[type=minecraft:arrow] {Motion:[0.0d,1.0d,0.0d]}
```
alternatively use the command:

```
/data modify entity @n[type=minecraft:arrow] Motion set value [0.0d,1.0d,0.0d]
```

Observed behavior
The arrow flies its old trajectory for about a second, after which it teleports to its true location, sometimes the arrow teleports to its true location but does not display the correct Motion, so it remains out of sync with its true position for another second or more before teleporting again. If the arrow visually lands before correcting its position to its true location, it produces no sound when hitting the ground.
Expected behavior
The arrow immediately follows its new trajectory, displaying its position and motion correctly.
By placing a repeating command block on the ground and activating it after inserting the following command:

```
execute as @e[type=minecraft:arrow] at @s run particle minecraft:electric_spark ^ ^ ^ 0 0 0 0 0 force @a
```
It is possible to see the true location of the arrow while the previous steps are being performed.

## Comments (4)

### Comment 1: migrated (2024-09-04T09:51:33.514-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: [Mod] Jingy (2024-09-05T10:25:19.180-0700)

Would  describe your issue?

### Comment 3: PALKIP (2024-09-05T11:31:08.756-0700)

No, in this case the delay affects only projectiles that display a direction, like arrows or tridents, snowballs are not affected, also the method used to change the projectile's Motion does not influence the update delay, the only method that seems to update the arrow's displayed Motion correctly is TNT's explosions.

### Comment 4: [Mod] Jingy (2024-09-05T12:27:08.408-0700)

In that case, please provide clear steps to reproduce this issue. If required, attach any necessary commands or datapacks to recreate the issue.
