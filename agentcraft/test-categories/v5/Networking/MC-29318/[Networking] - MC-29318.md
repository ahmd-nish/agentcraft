# MC-29318: Client misses inventory updates while player is manipulating items - causes invisible items

**Mojira URL:** [https://bugs.mojang.com/browse/MC-29318](https://bugs.mojang.com/browse/MC-29318)

## Report details

- **Mojira categories:** Networking
- **Project:** MC
- **Issue key:** MC-29318
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2013-08-24T04:54:07.403-0700
- **Updated:** 2025-10-19T03:03:56.341-0700
- **Resolution date:** 2022-07-09T05:30:31.684-0700
- **Affects versions:** Minecraft 1.6.2; Minecraft 14w30c; Minecraft 1.8.1; Minecraft 1.8.2-pre6; Minecraft 15w44b; Minecraft 1.8.9; Minecraft 16w05b; Minecraft 1.9 Pre-Release 4; Minecraft 1.9; Minecraft 1.9.1 Pre-Release 1; Minecraft 1.9.1 Pre-Release 3; Minecraft 1.9.4; Minecraft 1.10.2; Minecraft 16w35a; Minecraft 16w36a; Minecraft 16w39c; Minecraft 1.12; Minecraft 1.12.2; Minecraft 18w14b; Minecraft 1.13-pre2; Minecraft 1.13-pre5; Minecraft 1.13-pre6; Minecraft 1.13-pre8; Minecraft 1.13; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 1.14 Pre-Release 1; Minecraft 1.14; Minecraft 1.14.1 Pre-Release 2; Minecraft 1.14.2; Minecraft 1.14.3; 1.14.4; 19w35a; 19w37a; 1.15.1; 1.15.2; 20w07a; 20w17a; 20w18a; 20w20b; 20w21a; 20w30a; 1.16.2; 1.16.3; 20w46a; 20w51a
- **Fix versions:** 21w10a
- **Labels:** inventory; invisible; item; replaceitem; slot
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** Minecraft 1.13 7_26_2018 8_13_03 PM.mp4; Minecraft1.144_26_201910_35_30AM.mp4
- **Issue links:** Relates:inward:MC-239935:Client-side desyncs can still occur when using the "/item" or "/give" commands repeatedly | Duplicate:inward:MC-165633:Loot give on some cases can give an invisible item | Duplicate:inward:MC-99295:/give the same tick as losing that item fails on creative mode

## Description

The bug
When using whatever container that automatically updates the contents of a slot (like a furnace) and if the player, with the container GUI open, is constantly moving items into the inventory, the player won't see the container slot update (like a raw steak being cooked).
How to reproduce
- Open the furnace gui

- Place charcoal/coal and keep some item in your inventory

- Place something to be cooked into the furnace

- When the progress bar is almost at the end, start continuously left clicking an item in the inventory

What should happen is that the item to be cooked doesn't update (if it doesn't happen the first time, just retry), the progress bar has finished, and you won't have any item in the output slot, but if you click in it you will get the item cooked.

This also occurs with the /replaceitem command:
How to reproduce
- Put a command block on a clock, with a command such as:

```
/replaceitem entity @p inventory.0 golden_apple
```
→ This will put a golden apple in the first slot of your inventory

- Open your inventory, and move the golden apple to another slot

- As soon as a new one appears, grab it and move it to another slot as well
→ If you got the timing right, the slot will appear blank, even though the command block output in the chat window continues to say "[@: Replaced slot 9 with 1 x [Golden Apple]]"

- Turn off the clock

- Exit the world

- Re-enter the world, and open your inventory
→ There will be a golden apple in the first slot

Why this happens:
This happen because there's a boolean in EntityPlayerMP that's set to true when the server receives a window click packet and then there the function that should send the slot updates is called, though if this boolean is true it will not send the packet to the client to update it (while the server-side thinks from the next update on that the client has received the update).
Basically if the server code updates the content of some slots in the container (raw food to be removed, output slot set to cooked food) while the player is moving other items in the inventory.. it won't get the update.
So one way to fix this would be to know which slot is getting modified by player and block the updates only for that slot and not all the container slots. Another way would be having a resend list where clients that didn't got a certain slot update, get a resend of the packet from the server.

## Comments (22)

### Comment 1: migrated (2013-08-24T04:54:07.403-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: kumasasa (2013-08-26T22:21:33.335-0700)

Confirmed.

### Comment 3: Ezekiel (2014-07-26T11:51:58.110-0700)

Is this still a concern in the latest Minecraft version 14w30c? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 4: migrated (2014-07-26T13:33:00.874-0700)

I've updated the affected version because the problem is still present in 14w30c, the bug is reproducible in the same way.

### Comment 5: galaxy_2alex (2014-10-25T12:25:23.266-0700)

Is this still a concern in the current Minecraft version 1.8.1 Prerelease 3 / Launcher version 1.5.3 or later? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 6: migrated (2014-11-05T08:13:28.931-0800)

Well i have to say that it still happens but in a corner case.
Basicly if the output slot is empty, it all works.
Though if there's already an item and another is in the way and if 2 seconds before that item arrives (cooks if its a furnace) you start moving quickly stuff in the inventory, you won't see the stack number updating, so it seems there's only one item. And you can do this for every new item, so that maybe you finally click on the output and receive 10 items.
Now, i don't know if it's worth updating the affected version, i mean.. this is a very corner case ^^.

### Comment 7: marcono1234 (2016-02-09T05:43:53.712-0800)

Confirmed for
- 16w05b the golden apple example but only for Creative mode

### Comment 8: migrated (2016-02-26T10:27:00.857-0800)

Can confirm for 1.9 pre-4.

### Comment 9: migrated (2016-03-09T14:35:43.217-0800)

Can confirm for 1.9.1 pre-1
Also happens when given an item while manipulating your inventory, as I detailed in MC-99295 before finding this bug.

### Comment 10: migrated (2016-03-12T08:20:29.599-0800)

Bug present in 1.9.1 pre-3

### Comment 11: migrated (2016-07-20T15:07:08.965-0700)

Bug present in 1.10.2

### Comment 12: migrated (2016-07-20T15:44:35.178-0700)

Was already marked as affected.

### Comment 13: migrated (2016-09-16T19:14:14.088-0700)

Confirmed in the 1.11 snapshots as late as 16w36a

### Comment 14: migrated (2018-04-08T02:59:48.541-0700)

Confirmed for 18w14b

### Comment 15: migrated (2018-06-16T23:18:26.053-0700)

Confirmed for 1.13-pre2

### Comment 16: Cavinator1 (2018-07-01T16:04:18.945-0700)

This seems to be happening in 1.13-pre5. I came here from MC-118841
I was testing an advancement system where when you get a certain item it clears the item from your inventory, revokes the advancement, but then gives you a "reward" item. The thing I discovered is that it let me duplicate the reward items by putting the ghost block out and in my inventory over and over again

### Comment 17: migrated (2018-07-04T09:43:43.068-0700)

Seems like this bug and MC-41113 are similar or probably the same.

### Comment 18: migrated (2019-09-05T13:10:15.250-0700)

it appears a lot in snapshots 1.15 but also in some versions 1.14

### Comment 19: migrated (2020-06-29T01:55:57.499-0700)

This bug still present in 1.16.1?

### Comment 20: migrated (2020-07-01T05:48:05.164-0700)

Yes, still the case; Put this in a repeating command block:

```replaceitem entity @p hotbar.8 stone```
 and pick up the item a couple of times, at one point, the client will no longer see an item, but an item is in fact there.

### Comment 21: migrated (2020-09-11T00:55:48.670-0700)

Still in 1.16.3.

### Comment 22: migrated (2021-10-01T04:14:28.291-0700)

I could recreate a similar bug in 1.17.1 with a function on tick

```execute as @a[team=blue,nbt=!{Inventory:[{id:"minecraft:tnt"}]}] if score Aqua tnt matches 1.. if score match match matches 2 run function tntbattle:tnt-blue```

```give @s minecraft:tnt 1
scoreboard players remove Aqua tnt 1```
