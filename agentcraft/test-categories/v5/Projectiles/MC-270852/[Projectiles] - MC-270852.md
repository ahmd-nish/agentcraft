# MC-270852: Fully charged projectiles that are thrown or fired at a nearby shulker will not deflect properly

**Mojira URL:** [https://bugs.mojang.com/browse/MC-270852](https://bugs.mojang.com/browse/MC-270852)

## Report details

- **Mojira categories:** Projectiles
- **Project:** MC
- **Issue key:** MC-270852
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2024-04-16T22:55:52.935-0700
- **Updated:** 2025-04-26T15:35:32.868-0700
- **Resolution date:** 2024-11-16T13:05:38.403-0800
- **Affects versions:** Minecraft 15w31a; 1.20.4; 1.20.5 Pre-Release 3; 1.21; 24w36a
- **Fix versions:** 24w37a
- **Area:** Gameplay
- **Labels:** arrow; breeze; projectile; shulker; trident
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** 2024-04-28_16-08-41.mp4; 24w36a.mp4; 24w37a.mp4; ShulkerDeflectClose1.mp4; ShulkerDeflectClose2.mp4; ShulkerDeflectClosePlayerView.mp4
- **Issue links:** Relates:inward:MC-92175:Projectiles sometimes visually break before hitting a target | Relates:inward:MC-214546:Projectiles (including arrows) sometimes pass through entities without hitting them | Relates:inward:MC-125936:When projectiles spawn inside a hitbox, they don't hit the hitbox of the entity they are inside | Relates:inward:MC-148451:Shulkers with shells closed still take damage from snowballs and other shulker bullets | Relates:inward:MC-223466:Shulkers can deflect arrows before they are completely closed

## Description

When the player shoots a projectile at a closed shulker or a breeze from a distance of 1-3 blocks away, the projectile will almost instantly be deflected at the camera's position, never getting near the entity.
Steps to Reproduce:
- Summon a shulker with no AI:

```
/summon minecraft:shulker ~ ~ ~ {NoAI:1b}
```

- Fire an arrow at it from 1-3 blocks away
 &rarr; observe result

- Fire an arrow at it from >=4.5 blocks away
&rarr; observe result

Observed Behavior:
When firing it from a closer distance, the arrow will almost instantly be deflected at the camera position, and the player's view will be visually cluttered from all the arrow and particles created. The arrow will also not damage the player due to  and/or . When attempting this same issue with breezes, the behavior is less noticable comparatively (shown in the video/s)
Expected Behavior:
The arrow would get near the shulker's hitbox before being deflected properly at close distances just as it does from further away.
Screenshots/Videos:
Reproducing the issue from a third-person perspective:

Reproducing the issue in first person:

## Comments (5)

### Comment 1: migrated (2024-04-16T22:55:52.935-0700)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: migrated (2024-04-19T15:54:28.366-0700)

Hello Jiingy!
After further revision, this seems to be an error with Minecraft's rebounding code, and being to close propels it much too fast in the wrong direction.
Hope this can help!

### Comment 3: [Mod] Jingy (2024-04-28T14:09:28.692-0700)

First appeared in 15w31a, when shulkers were added:

### Comment 4: Viradex (2024-08-02T19:41:17.768-0700)

Possibly related to MC-271539.

### Comment 5: [Mod] Jingy (2024-11-16T13:03:34.966-0800)

This issue was fixed in 24w37a. The previous snapshot; 24w36a has buggy behavior with both arrows and tridents, and then in 24w37a both projectiles are fixed and properly deflect.
24w36a:

24w37a:
