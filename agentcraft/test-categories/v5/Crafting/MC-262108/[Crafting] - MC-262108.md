# MC-262108: Smithing table GUI issue with custom recipes

**Mojira URL:** [https://bugs.mojang.com/browse/MC-262108](https://bugs.mojang.com/browse/MC-262108)

## Report details

- **Mojira categories:** Crafting; Items
- **Project:** MC
- **Issue key:** MC-262108
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2023-04-25T16:11:48.330-0700
- **Updated:** 2025-04-30T04:18:29.393-0700
- **Resolution date:** 2023-06-08T02:32:35.220-0700
- **Affects versions:** 23w16a; 23w17a; 23w18a; 1.20 Pre-release 1; 1.20 Pre-release 6
- **Fix versions:** 23w31a
- **Area:** Expansion A
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** MC-262108 Datapack.zip

## Description

There is an inconsistency with the behavior of shift+click in smithing table gui when a datapack adds a recipe that uses a trim material item (eg: gold ingot, iron ingot, amethyst shard...) as the smithing template (as in a recipe that uses, f.e., a gold ingot as the smithing template, and something else in the third slot). This does not apply to other items, which behave as expected.
Observed Behavior:
Shift+click on the item in the inventory will not put the item in the template slot, when the materials slot (third slot) is empty the item will be put in there, when the material slot is already occupied by something else shift+click on the item will not move it at all.
You can manually drag the item in the template slot with the mouse and it will work.
Expected behavior:
To keep consistency with other workbenches, when shift+click is used the item should be put in the materials slot, and if it's already occupied it should be automatically transported to the template slot. The reverse would also work.
How to reproduce:
- Download the attached datapack (it adds two new recipes for the netherite axe, both using a diamond axe in the second slot and netherite ingot in the third slot, but one uses a gold ingot as the smithing template and the other uses a dirt block).

- Create a test world with said datapack.

- Get a gold ingot, a dirt block and a netherite ingot in your inventory

- Open a smithing table

- Shift+click on the dirt block --> It gets placed in the template slot, as expected

- Shift+click on the gold ingot --> It gets placed in the third slot, as expected

- Now place the netherite ingot in the third slot

- Shift+click on the gold ingot --> It will not be placed in the template slot, contrary to what happens with the dirt block (this is the issue)

- Try placing the gold ingot in the template slot manually --> this works as expected

As you can see there is an inconsistency with the behavior of shift+click depending if the item is considered an armor trim material or not. This should be fixed as shift+click in any other workbench's gui will place the item in its next available slot if one of them is already occupied (eg: blaze powder in brewing stands, which can go in both the fuel and ingredient slots).

## Comments (3)

### Comment 1: migrated (2023-04-25T16:11:48.330-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: Brain81505 (2023-04-28T07:57:57.538-0700)

Please give me the data pack for this issue, it's easier than to create it.

### Comment 3: ArrotinoD (2023-04-28T09:26:34.186-0700)

@Brain81505 I added the datapack, it includes two new recipes for the netherite axe, one using a gold ingot as template and one using a dirt block. You can see that shift click on the gold ingot won't put it in the template slot, but it will work on the dirt.
