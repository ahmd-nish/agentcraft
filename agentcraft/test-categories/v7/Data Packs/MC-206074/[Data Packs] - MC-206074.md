# MC-206074: Survival tab of Creative inventory desyncs if changed manually after an external change

**Mojira URL:** [https://bugs.mojang.com/browse/MC-206074](https://bugs.mojang.com/browse/MC-206074)

## Report details

- **Mojira categories:** Data Packs
- **Project:** MC
- **Issue key:** MC-206074
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2020-11-19T06:23:19.661-0800
- **Updated:** 2025-05-29T09:14:53.602-0700
- **Resolution date:** 2024-08-15T14:55:01.865-0700
- **Affects versions:** 20w46a; 21w10a; 21w14a; 1.17 Release Candidate 1; 1.17 Release Candidate 2; 1.17; 1.20.2; 23w40a; 1.20.4; 24w05a; 24w05b; 1.21
- **Fix versions:** 24w33a
- **Area:** Platform
- **Watchers:** 2
- **Attachments:** 3
- **Attachment filenames:** backpacksdatapack_withbug.zip; image-2020-11-19-15-09-45-202.png; image-2020-11-19-15-13-34-609.png
- **Issue links:** Duplicate:inward:MC-273675:Debug Stick Duplicate Bug | Duplicate:inward:MC-273673:When item is focused in hotbar, dropping the item while opening the creative menu duplicates the item. | Relates:outward:MC-273377:No debug stick in hand, but I can still edit blocks | Duplicate:inward:MC-268178:Item desync / duplication when dropping items in creative mode | Relates:inward:MC-219018:Ghost items can be created using /item (server doesn't update client inventory correctly)

## Description

Hi! I was working with a datapack for 1.17 (the one I uploaded here) to resolve a bug of the datapack. I found a minecraft bug. It seems /item could duplicate items and create strange ghost items. As you can see in the screenshots, if I check for the existence of the backpack item the game returns true, and if I ask the nbt it gives me the nbt of the item. However, that item should be there, but not 'ghost' and the other backpack(in my inventory) should exist. In this way, the command duplicates(not always) the items.
Do you want to check? Try this datapack, maybe with resource pack (search on the web for it, Backpacks Datapack). Give you a backpack with /loot give @s loot ulg:backpack/backpack or craft it. Place it in the off hand, right click, go to your inventory. Take the opened backpack to a slot of the inventory(not the hotbar slots). It will return on your second hand. Try again and again putting it in the inventory. At a moment, it will not return to the second hand. Now try checking for the item using /data get or predicates, or if data o [nbt={}] arg. You'll find it.
Take an item in your hotbar, select it and press F or the switch item button you have.
You will have successfully duplicated the backpack.
I don't know how to explain it, but at least I can post this try datapack and make you check and study the problem. For a better and less-laggy minecraft. Thanks
Steps to Reproduce:
- Ensure you are in Creative mode with a clear inventory

- Stand on the ground and drop a block of stone (item form) directly downwards

- Open the Survival tab of the Creative inventory

- Wait until you pick up the stone

- Without closing your inventory, move the stone to a different hotbar or inventory slot

- Close your inventory

- Right-click on the ground while the first hotbar slot is the active (main hand) slot
→  A block of stone is placed, even though your hand is empty

## Comments (6)

### Comment 1: migrated (2020-11-19T06:23:19.661-0800)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: migrated (2020-11-19T10:03:08.788-0800)

It seems to happen only in creative mode.

### Comment 3: Calverin (2021-06-06T15:43:12.821-0700)

Confirmed for 1.17-rc1. Also happens in adventure and survival mode. Occurs when immediately replacing an item that was just dropped with /item replace.

### Comment 4: Calverin (2021-06-07T11:05:45.090-0700)

https://youtu.be/__4kjmqCGw8
Steps to reproduce bug  in Minecraft 1.17-rc2:
1-  Run `/scoreboard objectives add drop minecraft.dropped:minecraft.dirt`
2- In a repeating command block, put `/execute as @a[scores={drop=1..}] run item replace entity @s weapon.mainhand with dirt`
3- In an always active chain command block after the last repeating one, put `/scoreboard players reset @a drop`
4- Power the repeating command block
5- In any game mode aside from spectator, drop a block of dirt, after the first block, you should receive a new "ghost" dirt block that is invisible and upon dropping behaves like a normal item.

### Comment 5: j_p_smith (2023-10-10T19:14:52.834-0700)

The reproduction steps by  actually describe a different issue, namely MC-219018 which has been fixed for some time now. The original issue that was reported here (and triaged) is a Creative-only issue that is still reproducible (see updated description for method).

### Comment 6: [Mod] Jingy (2024-05-14T16:55:07.062-0700)

Looks related to MC-242392
