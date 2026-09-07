# MC-165182: Inventory/GUI textures no longer handle translucent pixels correctly

**Mojira URL:** [https://bugs.mojang.com/browse/MC-165182](https://bugs.mojang.com/browse/MC-165182)

## Report details

- **Mojira categories:** Rendering; Resource Packs; UI
- **Project:** MC
- **Issue key:** MC-165182
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2019-11-08T00:04:53.249-0800
- **Updated:** 2025-04-29T08:08:41.282-0700
- **Resolution date:** 2024-07-25T00:35:36.612-0700
- **Affects versions:** 19w45a; 1.15 Pre-release 1; 1.15 Pre-Release 2; 1.15 Pre-release 3; 1.15 Pre-release 4; 1.15 Pre-release 5; 1.15 Pre-release 6; 1.15.1; 1.15.2 Pre-Release 1; 20w06a; 20w11a; 20w12a; 20w14a; 20w16a; 1.16.2 Release Candidate 1; 1.16.5; 21w11a; 21w13a; 21w14a; 21w16a; 21w17a; 21w18a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17; 1.17.1 Pre-release 1; 1.17.1; 21w39a; 21w40a; 21w42a; 1.18 Pre-release 1; 1.18; 1.18.1 Pre-release 1; 1.18.1; 22w03a; 1.18.2; 1.19.2; 1.19.4; 24w14a; 1.20.5 Pre-Release 1; 1.20.5 Pre-Release 2; 24w19b
- **Fix versions:** 24w33a
- **Area:** Platform
- **Labels:** GUI; custom; gui-slider; inventory; opacity; rendering; resource-pack; resource-pack-support; texture; translucency; translucency-nonfunctional
- **Watchers:** 1
- **Attachments:** 12
- **Attachment filenames:** custom GUI.zip; image-2019-11-08-16-06-25-857.png; image-2019-11-08-16-07-04-831.png; image-2019-11-08-16-07-44-017.png; image-2019-11-08-16-08-21-333.png; image-2019-11-08-16-08-30-725.png; image-2019-11-08-16-09-07-716.png; image-2019-11-08-16-09-32-747.png; image-2019-11-08-16-17-01-315.png; image-2019-11-23-14-13-36-564.png; image-2019-11-23-14-16-51-336.png; translucent-inventories-24w14a-v1.0.zip
- **Issue links:** Relates:outward:MC-270049:Enchanting table buttons and level icons render translucent pixels as opaque | Duplicate:inward:MC-163941:GUI doesn't render properly | Bonfire Testing:outward:MC-270530:Horses, donkeys, mules, llamas and camels all use the same inventory texture file

## Description

Possibly clones MC-47342.
The bug
If a texture file for an inventory screen is given translucent pixels, those pixels will render completely opaque in-game.
This was not the case prior to release 1.15 for many screens.
Affected screens
Everything located in textures/gui/container (excluding gamemode_switcher.png) is affected by this issue:
- Anvils

- Beacons

- Furnaces, blast furnaces and smokers

- Brewing stands

- Cartography tables

- Crafters

- Crafting tables

- Dispensers and droppers

- Enchanting tables

- Chests (both sizes), trapped chests (both sizes), ender chests, minecarts with chests, barrels

- Grindstones

- Hoppers and minecarts with hoppers

- Horses, donkeys, mules, llamas, trader llamas and camels

- The Survival inventory screen

- Looms

- Shulker boxes

- Smithing tables

- Stonecutters

- Villagers

- Creative inventory screens

In addition, the following are also affected:
- Book-and-quills and written books

- Recipe Book

The advancements window renders translucent pixels correctly.
I am unable to test if the demo screen background is also affected, however the attached resource pack also retextures this.
How to reproduce
- Download and apply the attached resource pack:

- Enter any of the aforementioned inventory screens

Expected results
The inventory screen would be translucent.
Actual results
It is not.
Further notes
Comparison using another attached resource pack in 1.14.4 and 1.15 respectively:
1.14.4
1.15

## Comments (27)

### Comment 1: migrated (2019-11-08T00:04:53.249-0800)

This comment contained multiple image attachments (12), please login to view the attachments.

### Comment 2: migrated (2019-11-22T22:14:23.177-0800)

This comment contained an image attachment, please login to view the attachment.

### Comment 3: migrated (2019-11-22T22:17:09.965-0800)

that's what it should be like

### Comment 4: SPGoding (2020-01-01T12:06:45.207-0800)

I've updated the description to make it clearer with a table showing the differences, and removed some useless information. Hope you will be fine with this.

### Comment 5: SoloAlguien (2021-03-17T15:40:40.926-0700)

Can confirm in 21w11a.

### Comment 6: SoloAlguien (2021-04-02T20:31:36.529-0700)

Can confirm in 21w13a.

### Comment 7: SoloAlguien (2021-04-08T16:19:12.339-0700)

Can confirm in 21w14a.

### Comment 8: SoloAlguien (2021-04-21T13:03:22.753-0700)

Can confirm in 21w16a.

### Comment 9: SoloAlguien (2021-05-02T11:35:51.499-0700)

Can confirm in 21w17a.

### Comment 10: SoloAlguien (2021-05-07T12:24:45.588-0700)

Can confirm in 21w18a.

### Comment 11: SoloAlguien (2021-05-15T17:58:03.625-0700)

Can confirm in 21w19a.

### Comment 12: SoloAlguien (2021-05-21T22:10:59.301-0700)

Can confirm in 21w20a.

### Comment 13: SoloAlguien (2021-05-28T16:51:27.534-0700)

Can confirm in 1.17 Pre-release 1.

### Comment 14: SoloAlguien (2021-05-31T17:28:34.047-0700)

Can confirm in 1.17 Pre-release 2.

### Comment 15: SoloAlguien (2021-06-01T22:27:38.313-0700)

Can confirm in 1.17 Pre-release 3.

### Comment 16: SoloAlguien (2021-06-20T11:52:01.597-0700)

Can confirm in 1.17 and 1.17.1 Pre-release 1.

### Comment 17: SoloAlguien (2021-07-11T15:37:36.575-0700)

Can confirm in 1.17.1.

### Comment 18: SoloAlguien (2021-09-29T14:29:45.507-0700)

Can confirm in 21w39a.

### Comment 19: SoloAlguien (2021-10-10T14:20:26.362-0700)

Can confirm in 21w40a.

### Comment 20: SoloAlguien (2021-10-20T10:56:03.088-0700)

Can confirm in 21w42a.

### Comment 21: SoloAlguien (2021-11-11T11:05:17.200-0800)

Can confirm in 1.18 Pre-release 1.

### Comment 22: SoloAlguien (2021-12-03T15:31:48.249-0800)

Can confirm in 1.18 and 1.18.1 Pre-release 1.

### Comment 23: SoloAlguien (2021-12-17T21:47:36.811-0800)

Can confirm in 1.18.1.

### Comment 24: pulpetti (2022-01-30T02:26:24.771-0800)

In 22w03a.

### Comment 25: SoloAlguien (2022-03-01T12:57:04.780-0800)

Can confirm in 1.18.2.

### Comment 26: migrated (2023-03-29T08:48:01.937-0700)

still in 1.19.4

### Comment 27: muzikbike (2024-04-02T09:45:15.344-0700)

As the reporter of many other UI translucency problems, can I become the owner of this specific report?
