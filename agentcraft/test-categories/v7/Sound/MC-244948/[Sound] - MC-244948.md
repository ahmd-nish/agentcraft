# MC-244948: The "minecraft:item.bundle.remove_one" sound plays even when no items are unpacked from bundles

**Mojira URL:** [https://bugs.mojang.com/browse/MC-244948](https://bugs.mojang.com/browse/MC-244948)

## Report details

- **Mojira categories:** Sound
- **Project:** MC
- **Issue key:** MC-244948
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2021-12-06T06:06:42.421-0800
- **Updated:** 2025-04-26T14:08:21.003-0700
- **Resolution date:** 2024-10-09T02:52:17.575-0700
- **Affects versions:** 1.18; 1.18.1; 22w03a; 22w05a; 22w06a; 1.18.2 Pre-release 1; 1.18.2; 22w12a; 22w15a; 1.19; 1.19.1; 1.19.2; 22w44a; 1.19.3; 1.19.4; 1.20.1; 1.20.5; 1.20.6 Release Candidate 1; 1.21
- **Fix versions:** 24w33a
- **Area:** Gameplay
- **Labels:** bundle
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-244948.mp4; MC-244948.png
- **Issue links:** Duplicate:inward:MC-271257:Empty bundle plays sound "Item unpacked" when right-clicked over an empty slot

## Description

The Bug:
The "minecraft:item.bundle.remove_one" sound, otherwise known as the "Item unpacked" sound, plays even when no items are unpacked from bundles.
Steps to Reproduce:
- Give yourself a bundle by using the command provided below.

```
/give @s minecraft:bundle
```

- Open your inventory, hold the bundle with your mouse cursor, right-click, and listen closely as you do this.

- Take note as to whether or not the "minecraft:item.bundle.remove_one" sound plays even when no items are unpacked from bundles.

Observed Behavior:
A sound can be heard even when not unpacking items.
Expected Behavior:
A sound would only be heard when items are unpacked.
Code Analysis:
Tentative code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.18.1 using MCP-Reborn.
net.minecraft.world.item.BundleItem.java

```
public class BundleItem extends Item {
   ...
   public boolean overrideStackedOnOther(ItemStack $is, Slot $s, ClickAction $ca, Player $p) {
      if ($ca != ClickAction.SECONDARY) {
         return false;
      } else {
         ItemStack itemstack = $s.getItem();
         if (itemstack.isEmpty()) {
            this.playRemoveOneSound($p);
            ...
```
If we look at the above class, we can see that if you were to attempt to right-click on an empty inventory slot whilst holding a bundle with your mouse cursor, the playRemoveOneSound() method would be called. This method plays the "minecraft:item.bundle.remove_one" sound and since no checks are carried out to see whether or not the bundle held by the mouse cursor has items inside of it, this results in the sound being played even when items aren't unpacked from bundles.

## Comments (4)

### Comment 1: migrated (2021-12-06T06:06:42.421-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: Viradex (2024-09-29T03:29:03.599-0700)

I am unable to reproduce this in 24w39a.

### Comment 3: syarumi (2024-10-08T18:12:20.733-0700)

I'm unable to reproduce this as well in 1.21.2 pre1.

### Comment 4: Avoma (2024-10-09T02:51:55.358-0700)

This issue was present in 1.21.1 but no longer occurs in 24w33a. This issue was fixed in 24w33a.
