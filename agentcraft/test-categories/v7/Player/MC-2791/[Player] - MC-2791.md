# MC-2791: The player model in the inventory screen renders in the wrong orientation when it's not standing up straight

**Mojira URL:** [https://bugs.mojang.com/browse/MC-2791](https://bugs.mojang.com/browse/MC-2791)

## Report details

- **Mojira categories:** Player; Rendering
- **Project:** MC
- **Issue key:** MC-2791
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2012-11-11T04:47:17.450-0800
- **Updated:** 2025-10-24T01:21:06.382-0700
- **Resolution date:** 2025-10-24T01:21:06.301-0700
- **Affects versions:** Minecraft 1.4.2; Minecraft 1.4.4; Snapshot 13w10b; Minecraft 1.5; Snapshot 13w11a; Minecraft 1.5.1; Snapshot 13w16a; Snapshot 13w16b; Minecraft 1.5.2; Snapshot 13w17a; Snapshot 13w18a; Snapshot 13w18b; Snapshot 13w19a; Snapshot 13w21a; Snapshot 13w21b; Snapshot 13w22a; Snapshot 13w23a; Snapshot 13w23b; Snapshot 13w24a; Snapshot 13w24b; Snapshot 13w25a; Snapshot 13w25b; Snapshot 13w26a; Minecraft 1.6; Minecraft 1.6.1; Minecraft 1.6.2; Minecraft 1.6.4; Minecraft 13w38a; Minecraft 13w38b; Minecraft 13w38c; Minecraft 1.7.4; Minecraft 14w03b; Minecraft 14w05b; Minecraft 14w06b; Minecraft 14w07a; Minecraft 14w08a; Minecraft 1.7.5; Minecraft 14w11b; Minecraft 14w20b; Minecraft 14w21a; Minecraft 14w21b; Minecraft 1.8; Minecraft 1.8.1-pre3; Minecraft 15w41b; Minecraft 15w49a; Minecraft 1.10.2; Minecraft 16w32a; Minecraft 16w32b; Minecraft 16w33a; Minecraft 16w35a; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 1.12 Pre-Release 5; Minecraft 1.12.2; Minecraft 17w50a; Minecraft 18w01a; Minecraft 18w02a; Minecraft 1.13.1; 19w39a; 1.15.2; 20w07a; 20w19a; 1.16.1; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.4; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w07a; 21w11a; 21w15a; 21w17a; 1.17; 21w37a; 1.19.2; 22w45a; 1.19.3; 1.19.4; 23w14a; 1.20.1; 1.20.2; 1.20.4; 24w34a
- **Fix versions:** 25w44a
- **Area:** Platform
- **Labels:** behavior; model
- **Votes:** 0
- **Watchers:** 2
- **Attachments:** 10
- **Attachment filenames:** 2013-03-06_21.30.54.png; 2013-03-06_21.31.22.png; 2013-03-06_21.32.29.png; 2015-10-08_09.47.22.png; 2015-10-09_17.44.07.png; image-20250601-110201.png; image-20250601-110511.png; MC-2791.mp4; MC-2791.png; screenshot-1.png
- **Issue links:** Duplicate:inward:MC-293758:Inventory character window has incorrect player rotation when flying with Elytra | Duplicate:inward:MC-207845:Mistake | Relates:outward:MC-85582:Entity models in the inventory can render outside the boundaries of the black box | Duplicate:inward:MC-267043:Elytra Animation tends to be upside down and facing the wrong direction whilst in menu | Duplicate:inward:MC-236820:avatar is not staying in its slot in the inventory while flying or swimming/crawling | Duplicate:inward:MC-183507:Player model issue | Duplicate:inward:MC-137242:Inventory avator upside-down | Duplicate:inward:MC-111855:inventory bug when gliding | Duplicate:inward:MC-19485:Sneaking Dead Body | Duplicate:inward:MC-99849:When flying, the display of the character in the inventory is absurdly posed. | Duplicate:inward:MC-93706:Inventory model inverted while gliding | Duplicate:inward:MC-90403:Inventory flying | Duplicate:inward:MC-90079:If gliding with Elytra Character in Inventory looks Strange | Duplicate:inward:MC-90048:Bug When Use Elytra And Open Inventory | Duplicate:inward:MC-89922:Players render upsidedown | Duplicate:inward:MC-56513:Weird Inventory!!! Not Common But Please Fix!!! | Relates:outward:MC-298942:Character body moves instead of the head when riding a happy ghast

## Description

The bug
When the player is flying, the model in the inventory doesn't shifting its body correctly relative to the mouse position. For example, suppose the game is set to full-screen. If your cursor is at the left side of the screen, the model would look towards your cursor correctly. However, if your cursor is at the right side of the screen, the model would be shifting in the opposite direction relative to the cursor.
This issue does not seem to affect the player's swimming pose.
How to reproduce
- Equip elytra

- Fly using your elytra

- Open your inventory menu

- Move your mouse around, especially to the left and right side of Minecraft (or screen, if you're playing in full-screen mode.)

- Note the model's behavior in relation to the mouse cursor

History of this issue
Originally, this ticket was reported for the inventory screen if the player is dead/dying. However, as of 15w41b, the inventory now closes when you die. It has then been suggested that this issue also occurs when opening the inventory after right-clicking a bed, but before getting into it. This video shows how that looks as of 20w07a: https://youtu.be/1bJgALyjt1Y.

## Comments (54)

### Comment 1: migrated (2012-11-11T04:47:17.450-0800)

This comment contained multiple image attachments (8), please login to view the attachments.

### Comment 2: migrated (2012-11-11T05:36:19.307-0800)

I think the bug should be that you can access your inventory at all during death. It may be better to simply force the inventory GUI to close upon death, as you shouldn't have access to it until you respawn.

### Comment 3: migrated (2012-11-12T23:54:12.295-0800)

What if you're doing something in your inventory, while you're at half a heart left, a zombie came up and killed you, and your mouse is outside of the inventory while you're holding a stack of diamonds?
Especially when the server has settings:
/gamerule keepInventory true
When all of the mentioned above happens, your diamonds will pop out of your inventory, and risk being thrown into a pit of lava, when you can avoid that entirely by not having the inventory GUI affect you when you're holding a stack of items.
It'll become an annoyance for you in the long run.
Thus, I propose that when you die with the inventory menu opened, your model falls down but the inventory doesn't close up immediately. This tells the player that he/she has died, and will take actions upon it.

### Comment 4: migrated (2013-03-06T05:47:24.757-0800)

As of snapshot 13w10b, this problem still exists. Note that when a player dies, the player's skin is reverted back to the default skin.

### Comment 5: migrated (2013-03-11T04:41:02.457-0700)

The bug isn't that the player model doesn't follow the mouse correctly, it's that you can actively use the inventory while dead, as stated above. That means that if you couldn't use the inventory, the bug would be fixed.
Seems easy enough!

### Comment 6: migrated (2013-03-11T04:47:43.252-0700)

I'm going to let others decide on this issue then. As mentioned, it's really easy to fix this.

### Comment 7: migrated (2013-03-12T10:23:18.358-0700)

Confirmed in 1.5pre. Also the skin is reverted back to default skin when you wait long enough.

### Comment 8: migrated (2013-03-23T14:49:18.405-0700)

Confirmed.

### Comment 9: Ezekiel (2013-06-29T13:47:07.441-0700)

Is this still a concern in the current Minecraft version? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 10: migrated (2013-07-03T11:55:18.098-0700)

Yes, it's still an issue.
I'll try to keep up.

### Comment 11: migrated (2013-07-23T19:30:02.207-0700)

To the mods:
Can anyone help monitoring this issue? I'm going to start my conscription service soon, and I won't be available to continue tracking this issue. As of now, this issue is still valid.
Thanks in advance.

### Comment 12: migrated (2014-02-23T08:30:36.671-0800)

Confirmed for 08a

### Comment 13: migrated (2014-03-15T14:26:43.093-0700)

Confirmed for 14w11b

### Comment 14: marcono1234 (2014-06-08T13:18:51.656-0700)

Seems to be fixed in 14w21b there is no sneaking animation anymore

### Comment 15: migrated (2014-06-08T14:43:56.430-0700)

Nope, still a problem.

### Comment 16: galaxy_2alex (2014-10-24T13:06:02.319-0700)

Is this still a concern in the current Minecraft version 1.8.1 Prerelease 3 / Launcher version 1.5.3 or later? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 17: migrated (2014-10-24T13:39:18.491-0700)

in 1.8.1-pre3, the dead body still shifts in strange ways based on the cursor.
However, I think the bigger issue is should the inventory stay open when you die, as discussed above. If keepinventory is off, then it should probably close immediately. As for when it's on, I'm not sure what I think. I'll have to do some testing. Is there any way to set that property on a single player world?

### Comment 18: galaxy_2alex (2014-10-24T13:44:39.542-0700)

It's the same as in Multiplayer, "/gamerule keepInventory true/false".

### Comment 19: migrated (2014-10-24T13:53:45.996-0700)

Ok I don't mess with that stuff ever so I was confused.
I tried setting it to on, and the game told me it was on, but every time I died, it deleted the inventory anyway and dropped the items on the map.

### Comment 20: migrated (2016-08-10T10:52:55.625-0700)

It seems that, now, when you die, you get kicked out of the inventory screen.
However, can confirm with the elytra.

### Comment 21: migrated (2018-08-29T05:46:32.618-0700)

Confirmed for 1.13.1 (elytra).

### Comment 22: muzikbike (2019-09-26T15:00:57.398-0700)

Affects 19w38b with crawling. Can I request ownership?

### Comment 23: migrated (2019-09-27T04:59:43.376-0700)

Connor Steppie, the ownership is at Microsoft/Mojang at this point.

### Comment 24: muzikbike (2019-09-27T07:07:56.902-0700)

...so you're Microsoft?

### Comment 25: muzikbike (2019-09-27T10:05:02.887-0700)

Affects 19w39a

### Comment 26: hoyskedotte (2019-10-17T07:29:08.269-0700)

Easiest way to reproduce now, is by using Elytra and open inventory.
Affects 19w42a.

### Comment 27: [Mod] violine1101 (2020-02-16T12:23:30.371-0800)

Interestingly, this does not happen when swimming / crawling. Also, it's no longer possible to keep the inventory screen open while dying, so I'll update the ticket's description accordingly.
Here's a video of me trying to reproduce the issue in 20w07a by sleeping: https://youtu.be/1bJgALyjt1Y. Not sure if this still qualifies as an instance of this bug (the player's animation looks fairly reasonable to me).

### Comment 28: numeritos (2020-06-18T10:12:39.544-0700)

Affects 1.16-rc1

### Comment 29: Avoma (2020-11-22T14:27:08.939-0800)

I'd like to request the ownership of this report as the reporter has been inactive since September 2019.

### Comment 30: migrated (2020-11-22T22:32:50.767-0800)

@Avoma,
I'm still active, and am still receiving email updates from this bug. It's just that, the bug is still there in the game, and I don't know what new information I can provide about the bug.

### Comment 31: FaRo1 (2020-11-23T01:00:28.462-0800)

The thing to do would be to test it in new snapshots and releases and add those to the version list. Since there already is a somewhat recent version added, it's not that important, but it might help a bit. Also, if you wanted to really put a lot of effort into it, you could do a code analysis or tell people in other places to vote for it, but that's about it.

### Comment 32: Avoma (2020-11-25T11:41:45.478-0800)

Can confirm in 20w48a.

### Comment 33: Avoma (2020-12-24T02:57:33.900-0800)

Can confirm in 20w51a.

### Comment 34: Avoma (2021-01-22T02:56:53.085-0800)

Can confirm in 21w03a.

### Comment 35: Avoma (2021-02-04T10:33:30.644-0800)

Can confirm in 21w05b.

### Comment 36: Avoma (2021-02-12T05:01:15.547-0800)

Can confirm in 21w06a.

### Comment 37: Avoma (2021-02-18T10:39:57.979-0800)

Can confirm in 21w07a. Video attached.

### Comment 38: Avoma (2021-03-28T09:44:57.978-0700)

Can confirm in 1.16.5 and 21w11a.

### Comment 39: Avoma (2021-04-19T01:33:47.623-0700)

Can confirm in 21w15a.

### Comment 40: Avoma (2021-04-30T05:57:40.144-0700)

Can confirm in 21w17a.

### Comment 41: Avoma (2021-06-16T11:55:42.049-0700)

Can confirm in 1.17.

### Comment 42: migrated (2022-07-22T16:48:54.983-0700)

I actually think this ticket hasn't even been triaged by the team yet. Still hoping they would fix this.

### Comment 43: migrated (2022-07-22T22:01:43.869-0700)

It got priority, so it got triaged.

### Comment 44: Kingcat (2022-11-10T05:07:34.087-0800)

Can confirm in 1.19.2 and 22w45a.
The rotation of the model when flying with an elytra has something to do with the facing direction. If you fly north, it looks normal, if you fly south, the model is upside down.

### Comment 45: Brain81505 (2023-02-11T07:39:14.046-0800)

Can confirm in 23w06a

### Comment 46: Picomos plays (2023-05-30T17:11:21.354-0700)

Affect 1.20 Re-release 7

### Comment 47: AMGAMES04 (2023-08-05T05:00:19.842-0700)

Can confirm fixed in 23w31a

### Comment 48: migrated (2024-04-25T00:31:15.126-0700)

Cannot confirm; this has been fixed prior to 1.20.4 and 1.20.5

### Comment 49: migrated (2024-04-25T08:30:35.375-0700)

Oh nice! Finally, we can put this issue to bed.

### Comment 50: Kingcat (2024-04-25T08:54:51.163-0700)

I can still reproduce it in 1.20.5

### Comment 51: clamlol (2024-08-22T00:17:03.237-0700)

I updated the title because from my testing the orientation generally was problematic, the shifting in relation to the cursor seemed mostly fine

### Comment 52: Loupieur (2025-06-01T04:02:15.082-0700)

Can confirm in 1.21.6-pre1

### Comment 53: Loupieur (2025-06-01T04:05:16.902-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 54: Benats (2025-06-18T02:01:27.895-0700)

Can confirm in version 1.21.6
