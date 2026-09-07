# MC-253638: The symbols used within shulker box tooltips to show random loot table contents are untranslatable

**Mojira URL:** [https://bugs.mojang.com/browse/MC-253638](https://bugs.mojang.com/browse/MC-253638)

## Report details

- **Mojira categories:** Internationalisation
- **Project:** MC
- **Issue key:** MC-253638
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2022-06-27T02:26:41.265-0700
- **Updated:** 2025-03-25T13:39:27.386-0700
- **Resolution date:** 2023-09-01T04:26:37.071-0700
- **Affects versions:** 1.19; 1.19.1 Release Candidate 1; 1.19.1 Pre-release 2; 1.19.1 Pre-release 5; 1.19.1 Release Candidate 2; 1.19.1; 1.19.2; 22w43a; 22w45a; 1.19.3; 1.19.4; 1.20.1
- **Fix versions:** 1.20.2 Pre-release 1
- **Labels:** shulker_box; translatability
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** MC-253638 - Context.png

## Description

The Bug:
The "???????" symbols that are used within shulker box tooltips to show random loot table contents are missing a translation key. Every other string throughout the game that contains the "?" symbol allows it to be correctly translatable, therefore introducing an inconsistency.
If you wish to display this string of text in-game, you can run the following command provided below and observe the tooltip of the shulker box.

```
/give @s minecraft:shulker_box{BlockEntityTag:{LootTable:"minecraft:chests/simple_dungeon"}}
```
Steps to Reproduce:
- Attempt to search for the existence of this string by using this search filter on the official Minecraft crowdin project.

- Take note as to whether or not the symbols used within shulker box tooltips to show random loot table contents are untranslatable.

Observed Behavior:
The symbols used within shulker box tooltips to show random loot table contents are untranslatable.
Expected Behavior:
The symbols used within shulker box tooltips to show random loot table contents would be translatable.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.19.1 Release Candidate 1 using Mojang mappings.
net.minecraft.world.level.block.ShulkerBoxBlock.java

```
public class ShulkerBoxBlock extends BaseEntityBlock {
   ...
   @Override
   public void appendHoverText(ItemStack itemStack, @Nullable BlockGetter blockGetter, List<Component> list, TooltipFlag tooltipFlag) {
      super.appendHoverText(itemStack, blockGetter, list, tooltipFlag);
      CompoundTag compoundTag = BlockItem.getBlockEntityData(itemStack);
      if (compoundTag != null) {
         if (compoundTag.contains("LootTable", 8)) {
            list.add(Component.literal("???????"));
         }
         ...
```
If we look at the above class, we can see that the symbols used within shulker box tooltips to show random loot table contents are hardcoded, and as a result, are untranslatable. This is evident through the following line of code:

```
list.add(Component.literal("???????"));
```

## Comments (2)

### Comment 1: migrated (2022-06-27T02:26:41.265-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: Avoma (2022-06-27T02:29:06.253-0700)

This ticket closely relates to MC-248778.
