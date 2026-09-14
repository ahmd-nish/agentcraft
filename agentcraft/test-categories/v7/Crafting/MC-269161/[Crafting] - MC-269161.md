# MC-269161: Stonecutter does not support multiple recipes with the same result item type

**Mojira URL:** [https://bugs.mojang.com/browse/MC-269161](https://bugs.mojang.com/browse/MC-269161)

## Report details

- **Mojira categories:** Crafting; UI
- **Project:** MC
- **Issue key:** MC-269161
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-03-06T20:12:05.930-0800
- **Updated:** 2025-05-29T09:07:12.233-0700
- **Resolution date:** 2024-04-11T05:57:19.296-0700
- **Affects versions:** 24w10a; 24w12a
- **Fix versions:** 1.20.5 Pre-Release 2
- **Area:** Platform
- **Watchers:** 2
- **Attachments:** 1
- **Attachment filenames:** test_datapack.zip
- **Issue links:** Duplicate:inward:MC-269823:Stonecutter Items Incorrect with Custom Components

## Description

This issue has existed for a while, but until 24w10a it didn't apply to vanilla as there was no way to add recipes to a stonecutter for which the result itemstack had any custom data. With data components and the codecs for recipes being updated to allow custom data, this issue is now reproducible in vanilla.
You cannot add 2 recipes with a common input whose outputs are the same item type. I have attached a datapack that reproduces the problem, adding 16 recipes, one for each light block level when given an oak plank as an input. You can see that by clicking on the buttons for each recipe, the output does not match the button you clicked.
The cause is a little complex and I first explained it here. The gist is that the Stonecutter recipe selection system relies on a list index for all applicable recipes being the same on the client and server. But the *ordering* of that list is set by RecipeManager#getRecipesFor(RecipeType, Container, Level). In getRecipesFor, the list is sorted using a Comparator that compares the description IDs for the result item which leads to ambiguous ordering when 2 identical result items are present. So the indices in this list get out of sync between the client and the server leading to the visual inconsistency between the button icons and the itemstack put into the result slot of the stonecutter inventory.
Steps to Reproduce
- Download and install the attached test_datapack.

- Place an oak_plank inside a Stonecutter and click around on the various recipes that show up, recipes that are added by the datapack

- Observe that the item created in the result slot does not match the recipe that you clicked on.

## Comments (4)

### Comment 1: migrated (2024-03-06T20:12:05.930-0800)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: [MOD] Greymagic27 (2024-03-10T04:28:45.790-0700)

Please attach steps to reproduce this issue

### Comment 3: Machine Maker (2024-03-10T09:11:17.625-0700)

Ok, I added clearer reproduction steps

### Comment 4: migrated (2024-03-20T17:17:38.918-0700)

Confirmed in 24w12a
