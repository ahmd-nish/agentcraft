# MC-274372: using_item advancement trigger keeps being activated even after the item stops being used, after teleporting to another dimension

**Mojira URL:** [https://bugs.mojang.com/browse/MC-274372](https://bugs.mojang.com/browse/MC-274372)

## Report details

- **Mojira categories:** Advancements; Data Packs
- **Project:** MC
- **Issue key:** MC-274372
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2024-07-11T23:34:21.110-0700
- **Updated:** 2025-04-26T15:55:04.943-0700
- **Resolution date:** 2024-08-07T01:15:52.237-0700
- **Affects versions:** 1.21
- **Fix versions:** 24w33a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** Bug.mp4; MC-274372.zip

## Description

The using_item advancement keeps trigger even when the player isn't holding down right mouse button if the reward function has a command that let the player teleport through dimension, causing the player to be stuck at a position unless they no longer holding the item.
The advancement:

```
{
    "criteria":
    {
        "book":
        {
            "trigger": "minecraft:using_item",
            "conditions":
            {
                "item":
                {
                    "items": "minecraft:book"
                }
            }
        }
    },
    "rewards":
    {
        "function": "test:book"
    }
}
```
The function:

```
advancement revoke @s only test:book
execute in overworld run tp @s 0 -60 0 0 0
playsound entity.player.teleport
```
What I expected to happen was:
The advancement stop trigger when release right mouse button.
What actually happened was:
The advancement keeps trigger and execute the reward function none-stop.
Steps to Reproduce:
1. Put the following datapack into your world and /reload it.
2. Use the following command to get an edible book.

```
/give @s book[food={can_always_eat: true, eat_seconds: 86400, nutrition: 1, saturation: 1}]
```
3. Go to the nether.
4. In the nether, start using the book until you appear in the overworld.
5. You will be teleported back to the overworld, and stuck at (0, -60, 0) until you use the book again or switch to another hotbar slot.

## Comments (3)

### Comment 1: migrated (2024-07-11T23:34:21.110-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: [Mod] ManosSef (2024-07-12T04:32:16.452-0700)

Please note that the attached file is not a data pack, it is a zip file containing a data pack folder. I've taken the liberty to fix it for you.

### Comment 3: AC (2024-07-12T04:57:11.804-0700)

Thank you so much, then I will delete the old file in order to avoid confusion.
