# MC-265033: Slots with item outline textures behave inconsistently when items are placed inside of these slots

**Mojira URL:** [https://bugs.mojang.com/browse/MC-265033](https://bugs.mojang.com/browse/MC-265033)

## Report details

- **Mojira categories:** Textures and models; UI
- **Project:** MC
- **Issue key:** MC-265033
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2023-08-25T04:55:09.274-0700
- **Updated:** 2025-04-11T11:16:59.537-0700
- **Resolution date:** 2024-10-23T00:13:11.096-0700
- **Affects versions:** 1.14.4; 1.20.1; 23w33a; 23w35a; 1.20.2 Pre-release 1; 1.20.2 Pre-release 2; 1.20.2; 23w40a; 23w41a; 23w42a
- **Fix versions:** 24w44a
- **Watchers:** 1
- **Attachments:** 25
- **Attachment filenames:** 2023-08-25_12.36.10.png; 2023-08-25_12.36.13.png; 2023-08-25_12.36.49.png; 2023-08-25_12.36.51.png; 2023-08-25_12.37.02.png; 2023-08-25_12.37.11.png; 2023-08-25_12.37.19.png; 2023-08-25_12.37.30.png; 2023-08-25_12.37.33.png; 2023-08-25_12.37.57.png; 2023-08-25_12.37.58.png; 2023-08-25_12.38.04.png; 2023-08-25_12.38.13.png; 2023-08-25_12.38.30.png; 2023-08-25_12.38.31.png; 2023-08-25_12.38.32.png; 2023-08-25_12.38.33.png; 2023-08-25_12.38.41.png; 2023-08-25_12.39.04.png; 2023-08-25_12.39.05.png; 2023-08-25_12.39.06.png; 2023-08-25_12.39.10.png; 2023-08-25_12.39.25.png; 2023-08-25_12.39.27.png; item-texture-shrinker-23w33a-v1.0.zip
- **Issue links:** Relates:outward:MC-74408:The brewing stand GUI does not have container sprites for the fuel and potion output slots | Duplicate:inward:MC-165092:Output icon in brewing stand is visible if a potion is in the output

## Description

The bug
Some block and entity inventory slots contain item outline textures overlaid on top of the slot to indicate what they accept. When an item is placed into these slots, the game does not behave consistently with respect to if the outline disappears or not.
Prior to 23w31a, these cases were covered in . However, that ticket now only covers brewing stands, even though the issue persists for other slot types.
How to reproduce
A resource pack is attached to this ticket which replaces several item textures and models with small squares, allowing the outline to still be seen if it is not hidden if an item is added to a slot.
Table of slots
The following are all of these outline-using slots as well as how they behave when an item is added. The expected behaviour is that the outline would disappear when an item is placed within, which does not always happen.
Slot
Result
Notes
Player armor slots
 Outline hidden
Original behaviour
Player offhand slot
 Outline hidden

Enchanting table lapis lazuli slot
 Outline hidden
Fixed in 23w31a by MC-259401
Smithing table template slot
 Outline hidden

Smithing table material slot
 Outline hidden

Smithing table input item slot
 Outline hidden

Loom banner slot
 Outline hidden
see also
Loom banner pattern slot
 Outline hidden
see also
Loom dye slot
 Outline hidden
see also
Brewing stand fuel slot
 Outline still present
Likely caused by
Brewing stand bottle slot
 Outline still present
Likely caused by
Horse/donkey/mule saddle slot
 Outline still present
see also
Horse armor slot
 Outline still present
see also
Llama carpet slot
 Outline still present
see also
How to fix
Fixing  would likely fix the brewing stand case. For the horse and llama cases, the normal "slot" texture would need to be used, with the "armor slot"/"saddle slot" texture overlaid on top, like is the case with most other slots.
Further notes
On a tangientally related note, it may also be worth moving all of the slot outline textures from the "items" directory to the "gui" directory since they're GUI related. Loom, horse and llama slot textures are already under "gui", so no change is needed here. The following textures would be moved and possibly renamed:
- item/empty_armor_slot_boots.png

- item/empty_armor_slot_chestplate.png

- item/empty_armor_slot_helmet.png

- item/empty_armor_slot_leggings.png

- item/empty_armor_slot_shield.png

- item/empty_slot_amethyst_shard.png

- item/empty_slot_axe.png

- item/empty_slot_diamond.png

- item/empty_slot_emerald.png

- item/empty_slot_hoe.png

- item/empty_slot_ingot.png

- item/empty_slot_lapis_lazuli.png

- item/empty_slot_pickaxe.png

- item/empty_slot_quartz.png

- item/empty_slot_redstone_dust.png

- item/empty_slot_shovel.png

- item/empty_slot_smithing_template_armor_trim.png

- item/empty_slot_smithing_template_netherite_upgrade.png

- item/empty_slot_sword.png

## Comments (1)

### Comment 1: migrated (2023-08-25T04:55:09.274-0700)

This comment contained multiple image attachments (25), please login to view the attachments.
