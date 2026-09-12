# MC-85582: Entity models in the inventory can render outside the boundaries of the black box

**Mojira URL:** [https://bugs.mojang.com/browse/MC-85582](https://bugs.mojang.com/browse/MC-85582)

## Report details

- **Mojira categories:** Rendering
- **Project:** MC
- **Issue key:** MC-85582
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2015-08-08T15:44:52.769-0700
- **Updated:** 2025-04-30T03:49:47.885-0700
- **Resolution date:** 2023-08-05T04:56:05.420-0700
- **Affects versions:** Minecraft 1.8.8; Minecraft 15w41b; Minecraft 15w42a; Minecraft 15w43c; Minecraft 15w44a; Minecraft 15w44b; Minecraft 15w46a; Minecraft 15w47c; Minecraft 1.13.2; 1.19.2; 22w43a; 1.19.3; 23w06a; 1.19.4; 1.20 Pre-release 7; 1.20
- **Fix versions:** 23w31a
- **Watchers:** 1
- **Attachments:** 8
- **Attachment filenames:** 2015-08-08_18.36.50.png; 2015-10-08_00.03.00.png; 2015-10-08_00.22.16.png; 2015-10-08_00.25.18.png; 2015-10-08_00.25.25.png; MC-85582.png; MC-85582 - Close up.png; MC-85582 - Non-player entity example.png
- **Issue links:** Relates:inward:MC-2791:The player model in the inventory screen renders in the wrong orientation when it's not standing up straight | Duplicate:inward:MC-90068:player lying on inventory when flying with Elytra | Duplicate:inward:MC-90278:Elytra, inventory bug | Duplicate:inward:MC-90290:Character comes out of portrait while gliding with Elytra | Duplicate:inward:MC-91262:When using elytra in midair, when you open inventory the player covers part of the inventory | Duplicate:inward:MC-91782:Character in down | Duplicate:inward:MC-92619:13.11.2015 | Duplicate:inward:MC-93416:Avatar glitch when flying on Elytra | Duplicate:inward:MC-94606:Elytra bug when open the inventory in fly | Duplicate:inward:MC-97431:Opening inventory while flying | Duplicate:inward:MC-98004:Elytra in inventory | Duplicate:inward:MC-98330:Elytra Inventory Bug | Duplicate:inward:MC-101189:Elytra Inventory Appearance In-Flight Boundries | Duplicate:inward:MC-103185:If you fly with eleytra with your inventory open, your body is going through you inventory slots. | Duplicate:inward:MC-111701:Elytra Inventory Glitch | Duplicate:inward:MC-134029:opening inventory while swimming causes inventory character to overlap inventory grid | Duplicate:inward:MC-144970:Items in inventory show on top of the player model while flying | Duplicate:inward:MC-149170:Player in inventory has wrong orientation while flying with elytra | Duplicate:inward:MC-165395:Player rendering behind items in inventory | Duplicate:inward:MC-172070:Player character renders under items in inventory while flying Elytra | Duplicate:inward:MC-175555:When flying with elytra, person display in inventor "E" is upside down | Duplicate:inward:MC-181875:Inventory Sprite not inside box when using elytra | Duplicate:inward:MC-188430:Flying Player overlaps items in inventory | Duplicate:inward:MC-191283:Layers Issue | Duplicate:inward:MC-211187:Elytra flying in inventory | Duplicate:inward:MC-221313:Arrows shot in the feet can be rendered over the item part in the inventory. | Duplicate:inward:MC-231622:Skin In Inventory When Flying With Elytra Is Flipped | Duplicate:inward:MC-254509:Player character minifigure elytra bug | Relates:outward:MC-78777:Player renders behind armor but in front of GUI in inventory | Relates:inward:MC-16164:Donkey/Horse lead still visible over their inventory | Relates:inward:MCPE-19504:Elytra bug - paper doll model renders outside box in inventory when gliding

## Description

The Bug:
Entity models in the inventory can render outside the boundaries of the black box.
This issue can most commonly be seen with the models of players inside their inventories but also occurs with non-player entity models as well, such as horses, when their inventories are accessed. As a result of this problem, the said entity model can render into the inventory and behind inventory items.
Steps to Reproduce:
- Obtain elytra and begin flying.

- Open your inventory, move your mouse cursor around, and look at your player model.

- Take note as to whether or not entity models in the inventory can render outside the boundaries of the black box.

Observed Behavior:
Entity models in the inventory can render outside the boundaries of the black box.
Expected Behavior:
Entity models in the inventory would not be able to render outside the boundaries of the black box.

## Comments (18)

### Comment 1: migrated (2015-08-08T15:44:52.769-0700)

This comment contained multiple image attachments (8), please login to view the attachments.

### Comment 2: migrated (2015-10-07T15:15:54.216-0700)

Reopening - this ticket is about the player model rendering outside the black box (and possibly over the inventory), not about the rotation.

### Comment 3: migrated (2015-10-07T15:18:25.260-0700)

Changing reporter to myself since the original reporter seems inactive. : Let me know if you want it back.

### Comment 4: migrated (2015-10-08T07:18:38.129-0700)

I would like it back redstonehelper please

### Comment 5: migrated (2015-10-08T08:21:02.581-0700)

Changed it back to you, sorry about that. Did I understand your original report right, it's not a duplicate of MC-2791?

### Comment 6: migrated (2015-10-08T08:33:40.450-0700)

this was posted before MC-2719, thank you for changing it back.

### Comment 7: migrated (2015-10-08T08:45:25.698-0700)

What?  was posted way earlier than this ticket, but it might be two separate issues:
- MC-2719 is about the player model in the inventory rotating incorrectly

- I believe  (this ticket) is about the player model being rendered outside the black box

### Comment 8: [Mod]Les3awe (2015-10-15T03:56:19.136-0700)

Confirmed for 15w42a

### Comment 9: [Mod]Les3awe (2015-10-22T04:01:55.886-0700)

Confirmed for 15w43a

### Comment 10: migrated (2015-10-23T06:46:50.164-0700)

Confirmed for 15w43b.

### Comment 11: migrated (2015-10-28T11:42:59.442-0700)

Confirmed for 15w44a.

### Comment 12: migrated (2015-11-12T07:56:00.725-0800)

Confirmed for 15w46a

### Comment 13: migrated (2015-11-20T11:16:46.802-0800)

Confirmed for 15w47a

### Comment 14: migrated (2020-06-17T07:57:58.848-0700)

Can any mod explain why this was put as WAI? The elytra thing is not only weirdly-shaped, but also directional, and seems like the player will look kind of normal when facing north, and then flipped or lopsided with other directions.

### Comment 15: Avoma (2022-09-20T10:02:22.444-0700)

Hi; it looks like this ticket has been reopened by Mojang and is now considered to be a valid issue which is awesome.
I can confirm this behavior; this affects 1.19.2. Also, if it isn't too much to ask, would it be okay if I could take ownership of this ticket since the current reporter has been inactive for over six years? I wish to update it regularly and refine the ticket to include the necessary information, such as steps to reproduce, expected behavior, etc... Thanks in advance.

### Comment 16: Avoma (2022-09-20T11:37:21.489-0700)

This issue isn't exclusive to the player model within the inventory; it can also be seen with other entity models as well. I've updated this ticket to mention this new information.

### Comment 17: Picomos plays (2023-05-30T07:00:20.735-0700)

Affect 1.20 Re-release 7

### Comment 18: Brevort (2023-06-07T08:27:32.597-0700)

Affects 1.20.
