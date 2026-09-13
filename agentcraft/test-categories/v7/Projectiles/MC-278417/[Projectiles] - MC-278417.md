# MC-278417: Arrows and tridents on fire and stuck in the ground cannot be extinguished by rain

**Mojira URL:** [https://bugs.mojang.com/browse/MC-278417](https://bugs.mojang.com/browse/MC-278417)

## Report details

- **Mojira categories:** Projectiles
- **Project:** MC
- **Issue key:** MC-278417
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2024-11-20T03:03:27.176-0800
- **Updated:** 2025-04-26T17:33:00.847-0700
- **Resolution date:** 2025-01-28T14:41:10.562-0800
- **Affects versions:** 24w36a; 1.21.3; 24w46a; 1.21.4 Pre-Release 1; 1.21.4
- **Fix versions:** 25w02a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** Minecraft 25w02a - Singleplayer 2025-01-11 15-42-34.mp4; Minecraft 25w02a - Singleplayer 2025-01-11 16-07-28.mp4
- **Issue links:** Relates:outward:MC-279830:Fire value is not decreased for projectiles (arrows, trident) with inGround:1b

## Description

A flaming arrow no longer decreases the value of its Fire tag if it's stuck on the ground. If it starts raining, the Fire value will be updated to -1s, but the arrow will still visually be on fire.
How to reproduce:
- Stand in the open.

- Execute the following commands in order:

```
/weather clear
```

```
/give @s minecraft:bow[minecraft:enchantments={levels:{"minecraft:flame":1}}]
```

```
/give @s minecraft:arrow
```

- Shoot the arrow into the ground.

- Execute the following command twice:

```
/data get entity @n[type=minecraft:arrow] Fire
```
→  Both times, the value will be 2000 minus the number of ticks passed while the arrow was travelling in mid-air, which means the value did not change between the two executions of the same command.

- Execute the following command:

```
/weather rain
```

- Execute the command from step 4 again.
→  The value is now -1s, but the arrow is still not put out.

Expected result:
Flaming arrows and tridents stuck on the ground would be extinguished by rain.
Observed result:
Flaming arrows and tridents stuck on the ground cannot be extinguished by rain.
Notes:
- Flaming arrows and tridents in mid-air can still be extinguished by rain.

- This issue is not present in 1.21.1 or earlier versions.

## Comments (4)

### Comment 1: migrated (2024-11-20T03:03:27.176-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: [Mod] ManosSef (2024-12-09T07:21:17.163-0800)

Arrows and tridents not being extinguished by placing water on them is actually tracked at , which has the same priority, so I have now made this report specific to rain not extinguishing those projectiles.

### Comment 3: yalming22 (2025-01-10T23:11:44.042-0800)

This issue has been fixed in 25w02a.

### Comment 4: knirch (2025-01-26T23:58:12.008-0800)

Burning arrows get Fire updated to -1s and updates visually now in rain.

Note that the edit to my report states that burning arrows are extinguished while flying through rain; This was not stated in my report. I did have the comment about Fire ticking while in flight, and as a control set it to 2 to see if a ticked to 0 arrow stopped being on fire while in motion which it properly did.
It's related, but might be reported elsewhere. ie that Fire does not tick when inGround:1b. Meaning, a landed arrow will burn for 1200 ticks (life) regardless of how many Fire ticks remained. (unless it's raining )
