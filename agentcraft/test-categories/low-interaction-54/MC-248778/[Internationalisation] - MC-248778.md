# MC-248778: The item count symbol within shulker box tooltips is untranslatable

**Mojira URL:** [https://bugs.mojang.com/browse/MC-248778](https://bugs.mojang.com/browse/MC-248778)

## Report details

- **Mojira categories:** Internationalisation
- **Project:** MC
- **Issue key:** MC-248778
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-02-23T06:18:40.822-0800
- **Updated:** 2025-05-03T09:20:46.679-0700
- **Resolution date:** 2023-09-01T04:26:31.931-0700
- **Affects versions:** 1.18.1; 1.18.2 Release Candidate 1; 1.18.2; 1.19 Pre-release 1; 1.19; 1.19.1; 1.19.2; 22w43a; 22w45a; 1.19.3; 1.19.4; 1.20.1
- **Fix versions:** 1.20.2 Pre-release 1
- **Area:** Platform
- **Labels:** shulker_box; translatability
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** MC-248778 - Context.png
- **Issue links:** Relates:outward:MC-238807:"Out of memory!" message is untranslatable | Relates:inward:MC-248817:The track output characters within command blocks are untranslatable | Duplicate:inward:MC-129565:Shulker box preview count affected by item display name styling

## Description

The Bug:
The "x" symbol that exists before the number of items in shulker box tooltips is untranslatable and is missing a translation key.
Steps to Reproduce:
- Attempt to search for the existence of this string by using this search filter on the official Minecraft crowdin project.

- Take note as to whether or not the item count symbol within shulker box tooltips is untranslatable.

Observed Behavior:
The item count symbol within shulker box tooltips is untranslatable.
Expected Behavior:
The item count symbol within shulker box tooltips would be translatable.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.18.1 using MCP-Reborn.
net.minecraft.world.level.block.ShulkerBoxBlock.java

```
public class ShulkerBoxBlock extends BaseEntityBlock {
   ...
   public void appendHoverText(ItemStack $is, @Nullable BlockGetter $bg, List<Component> $l, TooltipFlag $tf) {
      ...
      if (compoundtag != null) {
         ...
         if (compoundtag.contains("Items", 9)) {
            NonNullList<ItemStack> nonnulllist = NonNullList.withSize(27, ItemStack.EMPTY);
            ContainerHelper.loadAllItems(compoundtag, nonnulllist);
            int i = 0;
            int j = 0;

            for(ItemStack itemstack : nonnulllist) {
               if (!itemstack.isEmpty()) {
                  ++j;
                  if (i <= 4) {
                     ++i;
                     MutableComponent mutablecomponent = itemstack.getHoverName().copy();
                     mutablecomponent.append(" x").append(String.valueOf(itemstack.getCount()));
                     $l.add(mutablecomponent);
                  }
               }
            }
            ...
```
If we look at the above class, we can see that the item count symbol within shulker box tooltips is hardcoded, and as a result, is untranslatable. This is evident through the following line of code:

```
mutablecomponent.append(" x").append(String.valueOf(itemstack.getCount()));
```

## Comments (2)

### Comment 1: migrated (2022-02-23T06:18:40.822-0800)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: bodakugga (2022-03-08T05:36:52.344-0800)

The ideal fix would include variables for the item name and the amount (so something like %s x%s), so that translators can change the word order or spacing if needed. You might want to add this to the OP.
