# MC-123739: Recipe book entries are no longer sorted in any meaningful manner

**Mojira URL:** [https://bugs.mojang.com/browse/MC-123739](https://bugs.mojang.com/browse/MC-123739)

## Report details

- **Mojira categories:** Crafting; UI
- **Project:** MC
- **Issue key:** MC-123739
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2018-01-01T16:57:15.843-0800
- **Updated:** 2025-04-26T06:05:17.908-0700
- **Resolution date:** 2024-10-30T03:54:49.677-0700
- **Affects versions:** Minecraft 1.12.2; Minecraft 17w50a; Minecraft 1.13-pre1; Minecraft 1.13.1; 1.15.1; 1.15.2 Pre-release 2; 1.15.2; 20w21a; 1.16.1; 20w27a; 21w03a; 1.16.5; 21w08b; 1.19.3; 1.20.2; 23w46a; 1.20.3 Pre-Release 1; 1.20.3 Pre-Release 3; 1.20.3 Pre-Release 4; 1.20.3; 1.20.4; 24w04a; 24w07a; 24w09a; 24w11a; 1.20.5 Pre-Release 1; 1.20.5; 1.21
- **Fix versions:** 24w40a
- **Area:** Gameplay
- **Labels:** category; recipe-book; sorting
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 2024-04-28_16-27-39.mp4; 2024-10-30_15.57.39.png; 2024-10-30_15.59.32.png
- **Issue links:** Relates:outward:MC-269509:Leather Horse Armor is located in the wrong tab of the recipe book. | Duplicate:inward:MC-267070:Bamboo Mosaic and Honeycomb Block crafting recipes are in the misc category | Relates:outward:MC-1797:Sort order of creative inventory confusing | Duplicate:inward:MC-185449:Recipes in the Recipe Book are shuffled after executing /reload

## Description

Recipe book entries are not sorted in any meaningful manner (even changing randomly upon reloading) leading to inconsistent and confusing usage of the recipe book. This is especially interesting, considering that the recipe book used to be sorted alphabetically, and that block sets were grouped together. Here is a demonstration:

How to reproduce
- Give the player all vanilla recipes

```
/recipe give @p *
```

- Place down a crafting table

- Open the recipe book

- Set to "Showing All" mode

Observed & Expected behavior
 - The item recipes will be randomly placed with no real rhyme or reason for where they are inside each category, leaving the player to search through each category randomly to find the item they want to craft.
 - Each recipe entry would be neatly sorted by item type, colors, category, etc. just as the creative inventory is currently.
Suggested fix:
Either sort the recipe book categories by their alphabetical order, color, id, or just as the creative inventory is done.
Code analysis:
(Mappings: MCP Reborn 1.20.2 // Class: RecipeBookComponent.java // Method: updateCollections(boolean)):

```
private void updateCollections(boolean p_100383_) {
      List<RecipeCollection> list = this.book.getCollection(this.selectedTab.getCategory());
      list.forEach((p_296197_) -> p_296197_.canCraft(this.stackedContents, this.menu.getGridWidth(), this.menu.getGridHeight(), this.book));
      List<RecipeCollection> list1 = Lists.newArrayList(list);
      list1.removeIf((p_100368_) -> !p_100368_.hasKnownRecipes());
      list1.removeIf((p_100360_) -> !p_100360_.hasFitting());
      String s = this.searchBox.getValue();
      if (!s.isEmpty()) {
         ObjectSet<RecipeCollection> objectset = new ObjectLinkedOpenHashSet<>(this.minecraft.getSearchTree(SearchRegistry.RECIPE_COLLECTIONS).search(s.toLowerCase(Locale.ROOT)));
         list1.removeIf((p_301525_) -> !objectset.contains(p_301525_));
      }

      if (this.book.isFiltering(this.menu)) {
         list1.removeIf((p_100331_) -> !p_100331_.hasCraftable());
      }

      this.recipeBookPage.updateCollections(list1, p_100383_);
   }
```
Here, the result list list1 is not sorted in any way before passing it to RecipeBookPage.updateCollections, which does pagination and layout of the recipes onto the buttons of each page.

## Comments (9)

### Comment 1: migrated (2018-01-01T16:57:15.843-0800)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: migrated (2020-10-20T21:46:54.701-0700)

Can confirm for 1.16.3/1.16.4PR1

### Comment 3: FivesBlue (2021-01-27T17:22:09.509-0800)

Can confirm for 21w03a, there is some order, but very little

### Comment 4: Avoma (2021-03-06T10:50:51.872-0800)

Can confirm in 1.16.5 and 21w08b.

### Comment 5: migrated (2022-03-26T18:19:02.598-0700)

Still an issue on 1.18.x, would be much better if entries were to be sorted by either output item or recipe ID.

### Comment 6: migrated (2023-08-21T12:36:25.541-0700)

Can confirm in 1.20.1. Walls and Bamboo Mosaic are in the items tab instead of the building blocks tab. The tabs need reorganization.

### Comment 7: migrated (2023-08-21T12:56:50.953-0700)

This is for sorting within a tab, not for which tab a recipe is assigned. Make a seperate report for that.
RE Alex: while I agree, that leaves recipe groups. Recipe groups are a plain string and not namespaced, so how should they be sorted? Based on the first recipe ID?

### Comment 8: [Mod] Jingy (2023-11-19T17:36:55.985-0800)

Can confirm in 23w46a. I would like to request ownership of this issue to maintain it going forward seeing as the original poster is inactive since 2020.
Specifically, I would like to add actual code to the analysis, as currently it is just an explanation.

### Comment 9: sof (2024-10-29T22:00:27.812-0700)

Fixed in 24w40a. The recipe book is now sorted alphabetically
24w39a:
24w40a:
