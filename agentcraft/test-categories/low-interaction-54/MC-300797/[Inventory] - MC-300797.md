# MC-300797: The glowing effect causes entities to render incorrectly inside of inventories

**Mojira URL:** [https://bugs.mojang.com/browse/MC-300797](https://bugs.mojang.com/browse/MC-300797)

## Report details

- **Mojira categories:** Inventory; Rendering
- **Project:** MC
- **Issue key:** MC-300797
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2025-08-06T21:40:07.386-0700
- **Updated:** 2026-03-11T03:53:32.957-0700
- **Resolution date:** 2025-08-25T04:07:39.706-0700
- **Affects versions:** 25w32a; 25w34b
- **Fix versions:** 25w35a
- **Area:** Platform G
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2025-08-06_21.34.51.png; 2025-08-07_02.39.33.png; 2025-08-07_02.40.11.png; 2025-08-07 02-36-37.mp4
- **Issue links:** Duplicate:inward:MC-301420:When glowing character appears on side of the screen | Relates:outward:MC-276826:Entity models render completely white in GUI screens while affected by glowing and invisibility at the same time

## Description

If an entity has the glowing effect, part or the whole entity model will render with a solid color based on the glowing effect's color. The whole entity or part of the entity model can also render into the world with the glowing effect (when view at the correct angles).
How to reproduce
Players
- Give yourself the glowing effect

```
/effect give @s minecraft:glowing infinite
```

-  Open the survival inventory

Horses
- Summon a horse

- Tame the horse

- Give the horse the glowing effect

```
/effect give @n[type=minecraft:horse] minecraft:glowing infinite
```

- Put on horse armor

- Shift right click on the horse to open it's inventory

Observed behavior
The entity models are fully or partially rendered solid in the glowing effect's color. At certain camera angles, you can also see the entity is being render in the world twice. You can see this better if you change GUI Scale to 1 in Options... > Video Settings....
Expected behavior
The entity models in inventories should have the same rendering behavior as 1.21.8.

## Comments (2)

### Comment 1: Ruglan rodvold (2025-08-06T21:40:08.117-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: [Mod] Asteraoth (2025-08-07T00:01:52.357-0700)

This comment contained an image attachment, please login to view the attachment.

This comment contained an image attachment, please login to view the attachment.

This comment contained multiple media attachments (2), please login to view the attachments.
