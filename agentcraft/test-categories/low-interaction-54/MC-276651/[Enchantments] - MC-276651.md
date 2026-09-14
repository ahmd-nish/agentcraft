# MC-276651: damage_item does not repair items when the value is negative

**Mojira URL:** [https://bugs.mojang.com/browse/MC-276651](https://bugs.mojang.com/browse/MC-276651)

## Report details

- **Mojira categories:** Data Packs; Enchantments
- **Project:** MC
- **Issue key:** MC-276651
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-09-12T16:36:13.036-0700
- **Updated:** 2025-04-26T16:46:58.155-0700
- **Resolution date:** 2024-10-01T04:22:24.927-0700
- **Affects versions:** 24w37a; 24w38a
- **Fix versions:** 24w40a
- **Area:** Platform
- **Labels:** damage-item; data-pack; enchantment
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** image-2024-09-18-20-23-28-123.png; repair testing 1.zip

## Description

Starting from 1.21, it was possible to make enchantments that repaired the enchanted item using a negative value for the damage_item component. However, as of 24w33a and up to the most recent snapshot 24w37a, this is no longer possible.
Steps to Reproduce:
- Get the following item:

```
/give @p minecraft:netherite_chestplate[minecraft:damage=591]
```

- Enchant it with the following command:

```
/enchant @p testing:repair_damage_negative_test
```

- Hold the damaged item in your mainhand

Expected Result:
The item continues to have one durability point repaired every 20 ticks, like before.
Actual Result:
The item is not repairing itself over time, it remains at it's current durability amount.

## Comments (3)

### Comment 1: migrated (2024-09-12T16:36:13.036-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: [Mod] Jingy (2024-09-18T15:59:07.956-0700)

This seems intentional to me provided an item should only be damaged by a positive integer, but I've confirmed the report.

### Comment 3: MNight_4 (2024-09-18T16:35:36.994-0700)

An alternative would be to use an “Item Modifier” to change the damage of the item, but even doing this still an issue.
"Set damage" only allows you to use a value between 0~1, being forced to calculate ( 1 / max_damage x amount of damage to repair). This is possible to achieve with a scoreboard, but due to the use of decimals, if the item uses an high max_damage value, it's possible that the result will give an erroneous decimal.
It would be much more appropriate (if this is possible) to revert the change that doesn't allow the use of negative values, or change the field of the “damage_item” effect, to allow discounting the damage value.
