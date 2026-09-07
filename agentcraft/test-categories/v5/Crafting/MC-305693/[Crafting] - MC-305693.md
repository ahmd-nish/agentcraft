# MC-305693: Smelting recipes do not add the correct count of items to the output

**Mojira URL:** [https://bugs.mojang.com/browse/MC-305693](https://bugs.mojang.com/browse/MC-305693)

## Report details

- **Mojira categories:** Crafting; Data Packs
- **Project:** MC
- **Issue key:** MC-305693
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2026-01-13T09:37:06.470-0800
- **Updated:** 2026-03-11T03:44:17.686-0700
- **Resolution date:** 2026-01-21T06:50:48.441-0800
- **Affects versions:** 26.1 Snapshot 3
- **Fix versions:** 26.1 Snapshot 5
- **Area:** Platform HC
- **Votes:** 3
- **Watchers:** 0
- **Attachments:** 3
- **Attachment filenames:** 2026-01-13_09.34.57.png; 2026-01-13_09.35.15.png; SmeltingTweaksDP.zip

## Description

Expected Behavior
A smelting recipe with a count greater than 1 in the result field should add that many items to the output item stack when smelting finishes.
Observed Behavior
When the output stack is empty, the correct number of items is added to the output stack. (i.e. if the count for a smelting recipe is set to 4, and the furnace output is empty, the initial item stack will have 4 items in it.
After the first item is smelted, future smelting only adds 1 item to the output stack, regardless of the count.
Steps to Reproduce
- Add the attached datapack to a world.

- Place a stack of cactus in the furnace.

- Place fuel in the furnace.

- After the first item is smelted, there will be 4 dye in the output slot:

- After the second item is smelted, there will be 5 dye int the output slot.

The attached datapack adds a single recipe that causes a single cactus to produce 4 green_dye instead of 1. The recipe’s cookingtime has been decreased to make observing the bug faster:
data/minecraft/recipe/green_dye.json :

```
{
  "type": "minecraft:smelting",
  "category": "misc",
  "cookingtime": 20,
  "experience": 1.0,
  "ingredient": "minecraft:cactus",
  "result": {
    "id": "minecraft:green_dye",
    "count": 4
  }
}
```

## Comments (2)

### Comment 1: DqwertyC (2026-01-13T09:37:08.158-0800)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: DqwertyC (2026-01-13T09:57:30.981-0800)

I’ve also checked, and this does impact blasting and smoking recipes, though campfire_cooking do behave as expected.
