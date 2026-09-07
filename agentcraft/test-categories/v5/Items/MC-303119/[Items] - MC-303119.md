# MC-303119: Feeding a cat or wolf in Survival mode with only one item in the selected item slot does not restore as much health as it should

**Mojira URL:** [https://bugs.mojang.com/browse/MC-303119](https://bugs.mojang.com/browse/MC-303119)

## Report details

- **Mojira categories:** Items
- **Project:** MC
- **Issue key:** MC-303119
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2025-10-13T17:45:39.809-0700
- **Updated:** 2025-12-10T00:21:33.212-0800
- **Resolution date:** 2025-12-10T00:21:33.156-0800
- **Affects versions:** 1.21.10; 25w41a; 25w43a
- **Fix versions:** 26.1 Snapshot 1
- **Area:** Platform
- **Watchers:** 0
- **Attachments:** 1
- **Attachment filenames:** Bug in wolf and cat feeding.mp4

## Description

Steps to reproduce the issue
In Survival or Adventure, with only one item in the selected item  slot, feed a tamed cat or wolf. The cat must have 8 or less health and the wolf must have 37 or less health.
For a more controlled scenario, you can use commands to summon the animals. These three commands:

```
/summon cat ~ ~1 ~ {Tags:[BugTest],Sitting:1b,Health:1}
/summon wolf ~ ~1 ~ {Tags:[BugTest],Sitting:1b,Health:1}
/execute as @e[tag=BugTest] run data modify entity @s Owner set from entity @p UUID
```
After the commands, place exactly one raw cod* in two hotbar slots and, in survival or adventure mode, feed each animal with a cod.

*Or any item #wolf_food for the wolf and any item #cat_food for the cat
Expected result
The animal restore health according to the nutrition of the food*. In the case of raw cod, restore four health ​for the wolf and restore two health ​​for the cat.
So in the controlled scenario, when using the command /execute as @e[tag=BugTest] run data get entity @s Health in chat, we should have the following result:
Cat has the following entity data: 3.0f
Wolf has the following entity data: 5.0f
This expected result happens when animals are fed in creative or when feeding more than one item in the selected item slot.
To do more than one test with the same animals, the command /execute as @e[tag=BugTest] run data modify entity @s Health set value 1 can be useful to set the health back to 1.

*More specifically: restore by double the value of the food.nutrition component for the wolf and restore by the value of food.nutrition for the cat. It is considered that food.nutrition = 1 if not defined (however in these cases the actual and expected result is the same).
Actual result
Regardless of the food, the cat only restore 1 health and the wolf only restore 2 health.
The controlled scenario, when using the command /execute as @e[tag=BugTest] run data get entity @s Health in chat, we have as a result:
Cat has the following entity data: 2.0f
Wolf has the following entity data: 3.0f
Different than expected.
Note: The same happens if we customize the tags #cat_food or #wolf_food or the food or use_remainder component.
Probable reason
The game only reads the item used to feed the animal after the item disappears from the slot due to being used. This way, it considers the item air that does not have the food component defined, thus considering it as if the food's nutrition were 1.
If so, to fix it, simply change the order to first read the item's component and then remove it.

## Comments (1)

### Comment 1: Aloi (2025-10-13T17:45:40.393-0700)

This comment contained multiple media attachments (2), please login to view the attachments.
