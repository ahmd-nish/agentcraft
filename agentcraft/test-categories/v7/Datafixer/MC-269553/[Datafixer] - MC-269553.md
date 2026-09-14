# MC-269553: Items with empty enchantments NBT tag do not upgrade as expected

**Mojira URL:** [https://bugs.mojang.com/browse/MC-269553](https://bugs.mojang.com/browse/MC-269553)

## Report details

- **Mojira categories:** Commands; Datafixer
- **Project:** MC
- **Issue key:** MC-269553
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-03-18T00:16:50.923-0700
- **Updated:** 2025-04-11T10:08:25.888-0700
- **Resolution date:** 2024-04-21T14:04:17.489-0700
- **Affects versions:** 24w11a
- **Fix versions:** 24w14a
- **Area:** Platform
- **Labels:** data-fixer
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2024-03-18_07.05.50.png; 2024-03-18_07.10.53.png; 2024-03-18_07.10.55.png; phantomenchantmentupgradetest.zip
- **Issue links:** Relates:outward:MC-271020:enchantment_glint_override=true does not cause pick block to avoid replacing that item

## Description

The bug
Items with an empty NBT tag for enchantments (Enchantments:[]) do not upgrade to the new component system as expected. It'd be expected that they would get an enchantment_glint_override component tag, but this does not happen.
Notably, items with the NBT tag (Enchantments:[{}]) do convert as expected, so it'd be expected that the other form would also do so.
How to reproduce
A world containing "phantom enchanted" items is attached to this ticket.
- Open the attached world in 1.10.2 (in 1.11 to 1.20.4, the items won't visually appear enchanted due to a bug, but the NBT tag is still there)

- Verify that the items look enchanted

- Open the attached world in the latest 1.20.5 snapshot

- Verify that not only do they not look enchanted, but that the empty enchantment tag is completely gone, and these items are now identical to normal unenchanted items

Expected results
These items would keep their enchantment glint in 1.20.5+ by converting to the new enchantment_glint_override component.
Actual results
They do not.

## Comments (1)

### Comment 1: migrated (2024-03-18T00:16:50.923-0700)

This comment contained multiple image attachments (4), please login to view the attachments.
