# MC-65931: The pick block function doesn't work with entities while in survival or adventure mode

**Mojira URL:** [https://bugs.mojang.com/browse/MC-65931](https://bugs.mojang.com/browse/MC-65931)

## Report details

- **Mojira categories:** Player
- **Project:** MC
- **Issue key:** MC-65931
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2014-08-07T09:53:16.837-0700
- **Updated:** 2025-04-26T03:41:18.391-0700
- **Resolution date:** 2024-10-31T07:17:51.593-0700
- **Affects versions:** Minecraft 1.7.10; Minecraft 14w32b; Minecraft 14w32d; Minecraft 14w33a; Minecraft 14w33c; Minecraft 14w34a; Minecraft 14w34b; Minecraft 14w34c; Minecraft 14w34d; Minecraft 1.8-pre1; Minecraft 1.8-pre2; Minecraft 1.8-pre3; Minecraft 1.8; Minecraft 1.8.1-pre1; Minecraft 1.8.1-pre2; Minecraft 1.8.1-pre3; Minecraft 1.8.1-pre4; Minecraft 1.8.1-pre5; Minecraft 1.8.1; Minecraft 1.8.2-pre1; Minecraft 1.8.2-pre5; Minecraft 1.8.6; Minecraft 15w31a; Minecraft 15w33b; Minecraft 15w34a; Minecraft 15w35b; Minecraft 15w36c; Minecraft 15w39b; Minecraft 15w41b; Minecraft 15w44a; Minecraft 15w44b; Minecraft 15w45a; Minecraft 15w46a; Minecraft 15w47a; Minecraft 15w49a; Minecraft 15w50a; Minecraft 15w51b; Minecraft 16w02a; Minecraft 16w03a; Minecraft 16w06a; Minecraft 1.9 Pre-Release 1; Minecraft 1.9; Minecraft 1.9.1 Pre-Release 2; Minecraft 1.9.2; Minecraft 1.9.3; Minecraft 1.9.4; Minecraft 16w20a; Minecraft 1.10 Pre-Release 1; Minecraft 1.10; Minecraft 1.10.2; Minecraft 16w32a; Minecraft 16w32b; Minecraft 16w33a; Minecraft 16w35a; Minecraft 16w36a; Minecraft 16w38a; Minecraft 16w39a; Minecraft 16w39b; Minecraft 16w39c; Minecraft 16w40a; Minecraft 16w41a; Minecraft 16w42a; Minecraft 16w43a; Minecraft 16w44a; Minecraft 1.11 Pre-Release 1; Minecraft 1.11; Minecraft 16w50a; Minecraft 1.11.1; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 17w13a; Minecraft 17w14a; Minecraft 17w15a; Minecraft 17w16a; Minecraft 17w16b; Minecraft 17w17a; Minecraft 17w17b; Minecraft 17w18a; Minecraft 1.12 Pre-Release 5; Minecraft 1.12 Pre-Release 6; Minecraft 1.12 Pre-Release 7; Minecraft 1.12; Minecraft 17w31a; Minecraft 1.12.1 Pre-Release 1; Minecraft 1.12.1; Minecraft 1.12.2 Pre-Release 1; Minecraft 1.12.2 Pre-Release 2; Minecraft 1.12.2; Minecraft 17w43a; Minecraft 17w43b; Minecraft 17w45a; Minecraft 17w48a; Minecraft 17w50a; Minecraft 18w01a; Minecraft 18w03b; Minecraft 1.13-pre1; Minecraft 1.13; Minecraft 18w30b; Minecraft 1.13.1; 1.14.4; 1.15 Pre-release 6; 1.16.1; 1.16.2 Release Candidate 1; 1.16.2; 1.16.3; 1.16.4; 20w46a; 20w49a; 21w03a; 21w05b; 21w06a; 21w07a; 21w17a; 21w18a; 1.17; 1.17.1; 21w41a; 21w42a; 21w43a; 1.18 Pre-release 1; 1.18 Pre-release 7; 1.18; 1.18.1; 22w03a; 22w05a; 22w06a; 22w07a; 1.18.2 Release Candidate 1; 1.18.2; 22w17a; 22w18a; 1.19; 1.19.1; 1.19.2; 22w43a; 1.19.3; 1.19.4; 1.20; 1.20.1; 24w11a; 1.21; 1.21.1; 24w33a; 24w44a; 1.21.3
- **Fix versions:** 24w44a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** Creative_after_pick_block.png; Creative_before_pick_block.png; MC-65931.mp4; MC-65931.png; Survival_after_pick_block.png; Survival_before_pick_block.png
- **Issue links:** Duplicate:inward:MC-275081:"Pick Block" bind doesn't work on entities in survival mode, which isn't consistent with creative mode | Duplicate:inward:MC-264958:Middle clicking on entities | Duplicate:inward:MC-201377:Middle mouse button to quickly select ship | Duplicate:inward:MC-197414:Pick block does not work on entities in survival mode | Duplicate:inward:MC-167843:Pick block used on fish in survival mode does not cause the player to switch to a fish bucket

## Description

The Bug:
The pick block function doesn't work with entities while in survival or adventure mode.
Using the pick block function on a block in survival or adventure mode would switch your hotbar selection to that block if you have it present in your inventory. This isn't the case for entities such as item frames, boats, paintings, minecarts, armor stands, end crystals, etc...
Steps to Reproduce:
- Obtain two item frames and switch into survival mode.

- Place one of them down and begin holding anything other than the item frame in your inventory.

- Use the pick block function whilst looking at the item frame you just placed.

- Take note as to whether or not the pick block function works with entities while in survival or adventure mode.

Observed Behavior:
The pick block function doesn't work.
Expected Behavior:
The pick block function would work.

## Comments (21)

### Comment 1: migrated (2014-08-07T09:53:16.837-0700)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: galaxy_2alex (2014-08-07T09:57:13.713-0700)

The Armor Stand part is a bug for all game modes.

### Comment 3: migrated (2015-11-11T09:38:12.908-0800)

Armor stand works for creative in 15w45a

### Comment 4: migrated (2015-11-11T10:21:30.505-0800)

Armor stands ended up getting their own ticket.

### Comment 5: migrated (2017-05-04T08:48:08.536-0700)

Please do not mark unreleased versions as affected.
You don't have access to them yet.

### Comment 6: JUE13 (2017-05-23T19:26:16.816-0700)

Confirmed for 1.12-pre5

### Comment 7: migrated (2020-05-19T08:53:15.414-0700)

This also was an issue in legacy console edition when pick block got added, but for legacy console edition this issue got fixed.

### Comment 8: j_p_smith (2020-06-27T12:03:52.918-0700)

Confirmed in 1.16.1.

### Comment 9: Avoma (2021-01-22T11:51:55.383-0800)

Can confirm n 21w03a.

### Comment 10: Avoma (2021-02-06T06:55:08.703-0800)

Can confirm in 21w05b.

### Comment 11: Avoma (2021-02-12T06:22:32.677-0800)

Can confirm in 21w06a.

### Comment 12: Avoma (2021-02-19T04:26:57.994-0800)

Can confirm in 21w07a.

### Comment 13: Avoma (2021-05-02T02:46:43.213-0700)

Can confirm in 21w17a.

### Comment 14: migrated (2021-05-02T09:40:09.815-0700)

I would like to request ownership as the original reporter hasn’t been active since September 2017. I will keep this ticket updated.

### Comment 15: Avoma (2021-06-26T04:23:11.072-0700)

Can confirm in 1.17.

### Comment 16: Avoma (2021-07-13T00:55:28.394-0700)

Can confirm in 1.17.1.

### Comment 17: Avoma (2021-10-13T06:28:13.737-0700)

Can confirm this behavior in 21w40a. Here are some extra details regarding this problem.
The Bug:
The pick block function doesn't work with entities whilst in survival or adventure mode.
Steps to Reproduce:
- Obtain two item frames and switch into survival mode.

- Place one of them down and begin holding anything other than the item frame in your inventory.

- Use the pick block function whilst looking at the item frame you just placed, and take note as to whether or not you are now holding an item frame in your hand.

Observed Behavior:
The pick block function doesn't work with entities whilst in survival or adventure mode.
Expected Behavior:
The pick block function would work with entities whilst in survival or adventure mode.

### Comment 18: migrated (2024-08-10T11:55:24.906-0700)

it doesn't work due to a redundant check in the net.minecraft.client.MinecraftClient class, method doItemPick()
For blocks it checks if (type = HitResult.Type.BLOCK)
For entities it checks if (type = HitResult.Type.ENTITY|| !bl)
where bl is only true when the player is in creative mode.
bl is still used later in the code to see if the player can pull items out of creative inventory, but please, remove it from the entity check, im begging

### Comment 19: migrated (2024-08-15T16:42:21.080-0700)

Can confirm in 24w33a.

### Comment 20: haykam (2024-10-30T22:33:34.789-0700)

This issue was fixed in Minecraft snapshot 24w44a due to a refactor involving the pick item functionality.

### Comment 21: Avoma (2024-10-31T07:17:45.341-0700)

Can confirm that this issue was fixed in 24w44a.
