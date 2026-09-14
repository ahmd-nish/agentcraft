# MC-3587: Last use of an anvil causes player to drop their item

**Mojira URL:** [https://bugs.mojang.com/browse/MC-3587](https://bugs.mojang.com/browse/MC-3587)

## Report details

- **Mojira categories:** Items
- **Project:** MC
- **Issue key:** MC-3587
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2012-11-20T20:36:43.893-0800
- **Updated:** 2025-05-29T09:20:37.977-0700
- **Resolution date:** 2021-09-26T23:34:18.379-0700
- **Affects versions:** Minecraft 1.4.5; Minecraft 1.4.7; Minecraft 1.5; Minecraft 1.5.1; Minecraft 1.5.2; Snapshot 13w25c; Minecraft 1.7.4; Minecraft 14w02c; Minecraft 14w03b; Minecraft 14w04a; Minecraft 14w04b; Minecraft 1.7.10; Minecraft 14w30b; Minecraft 14w30c; 1.16.3; 1.16.4 Pre-release 1; 1.16.4 Pre-release 2; 1.16.4 Release Candidate 1; 1.16.4; 20w45a; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w08b; 21w10a; 21w11a; 21w13a; 21w14a; 21w15a; 21w16a; 21w17a
- **Fix versions:** 21w18a
- **Game mode:** Survival
- **Labels:** anvil; inventory
- **Watchers:** 2
- **Attachments:** 0
- **Issue links:** Relates:outward:MC-87935:When closing the inventory while holding an item with the cursor in Creative mode, the item disappears

## Description

Upon using an anvil for the last time before it breaks, taking the output out causes the item to be dropped/thrown.
What I expected to happen was...:
I expected that the item would be placed into my inventory when the anvil breaks.
What actually happened was...:
I removed the new item (without shift-click) causing the anvil to break. As the menu forcefully closes, the item I was holding in the cursor is thrown onto the floor.
Steps to Reproduce:
- Use all charges of the anvil.

- On the last charge, pick up the new item with a click.

- Anvil breaks, causing the menu to close.
   the item is thrown

## Comments (12)

### Comment 1: migrated (2013-06-24T10:51:34.289-0700)

Seen this in 1.5.2 multiple times as well, but my anvil wasn't over the Void so I didn't lose what I was working on.

### Comment 2: Ezekiel (2014-01-26T07:41:56.789-0800)

Is this still a concern in the latest Minecraft version 14w04b? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 3: migrated (2014-01-26T08:20:20.819-0800)

This is still an issue, as of 14w04b.
Any item still in hand when using any object will get thrown forward, when the object is destroyed before the player can place it in their inventory.

### Comment 4: migrated (2014-07-26T17:07:44.945-0700)

This issue is still active. Tested with 14w30c.
When ever the last use of an anvil is used, it will break and close the inventory menu. <-- That is the issue.
This causes the item you just removed to be dropped/thrown,  as you cannot hold an item, with the mouse cursor, when the inventory menu is closed.
The only logical solution I see is to add a forth state to the anvil. aka broken. or to automatically switch to the player's inventory menu, before closing. This way the user can still place the item back into their inventory. It will also prevent the extremely rare chance that the item will get lost (like my first example), when thrown, or stolen by another nearby player.

### Comment 5: Sonicwave (2020-09-16T09:28:56.954-0700)

Changed the reporter to , as they have requested it in Discord and the original reporter has been inactive.

### Comment 6: migrated (2020-09-19T21:36:39.790-0700)

In Bedrock edition the item will be sent back to the inventory instead of being thrown out, perhaps a similar mechanic could also be used

### Comment 7: Avoma (2020-11-25T11:42:35.541-0800)

Can confirm in 20w48a.

### Comment 8: Jack McKalling (2020-11-25T12:23:09.460-0800)

Also works if you start with a "Damaged Anvil" from the creative inventory, and then combine two Sharpness I enchanted books back in survival, a couple of times.
Doesn't happen if you shift-click the output, so it appears that the drop happens because you're holding it in the cursor while the gui is forced closed.

### Comment 9: Avoma (2021-02-04T10:36:57.616-0800)

Can confirm in 21w05b.

### Comment 10: Jack McKalling (2021-05-05T13:46:08.452-0700)

When the anvil is closed, items still in any of the slots or in the cursor are now correctly placed inside the inventory just like with chests.

### Comment 11: migrated (2021-05-07T19:40:44.112-0700)

I never thought this was a bug. I imagine it as hitting your item with a hammer to forge it, but your anvil breaks when you hit it so it falls to the ground before you can grab it.

### Comment 12: windwend (2021-09-26T23:34:18.379-0700)

Seems that this is the way this bug was fixed: items that are held with the cursor when the inventory or any GUI closes, are now transferred directly into the inventory instead of thrown out.
