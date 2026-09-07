# MC-248844: The page indicator symbol within the recipe book GUI is untranslatable

**Mojira URL:** [https://bugs.mojang.com/browse/MC-248844](https://bugs.mojang.com/browse/MC-248844)

## Report details

- **Mojira categories:** Internationalisation
- **Project:** MC
- **Issue key:** MC-248844
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2022-02-28T00:51:07.838-0800
- **Updated:** 2025-03-25T13:08:19.987-0700
- **Resolution date:** 2023-09-01T04:26:33.347-0700
- **Affects versions:** 1.18.1; 1.18.2 Release Candidate 1; 1.18.2; 1.19 Pre-release 1; 1.19; 1.19.1; 1.19.2; 22w43a; 22w45a; 1.19.3; 1.19.4; 1.20.1
- **Fix versions:** 1.20.2 Pre-release 1
- **Area:** Platform
- **Labels:** translatability
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** MC-248844 - Context.png

## Description

The Bug:
The "/" symbol that exists between the value of the current and total pages within the recipe book GUI is untranslatable and is missing a translation key.
This is a problem because every other string throughout the game that contains the "/" symbol is translatable, therefore introducing an inconsistency. Below, I've constructed a table to visually demonstrate how and why this is a valid internationalization issue and to show the inconsistency.
Translation Key
String
Context
Is the "/" symbol translatable?
item.minecraft.bundle.fullness
%s/%s
This string is used within bundle tooltips to show the fullness of a bundle.
Yes
filled_map.level
(Level %s/%s)
This string is used within filled map tooltips to show the level of a filled map.
Yes
item.durability
Durability: %s / %s
This string is used within item tooltips to show the durability of an item.
Yes
sleep.players_sleeping
%s/%s players sleeping
This string is displayed within the action bar to show how many players are currently sleeping.
Yes
N/A
%s/%s
This string is used within the recipe book GUI to show what page of the recipe book the player is on.
No
h3. Steps to Reproduce:
- Attempt to search for the existence of this string by using this search filter on the official Minecraft crowdin project.

- Take note as to whether or not the page indicator symbol within the recipe book GUI is untranslatable.

Observed Behavior:
The page indicator symbol within the recipe book GUI is untranslatable.
Expected Behavior:
The page indicator symbol within the recipe book GUI would be translatable.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.18.1 using MCP-Reborn.
net.minecraft.client.gui.screens.recipebook.RecipeBookPage.java

```
public class RecipeBookPage {
   ...
   public void render(PoseStack $ps, int $i0, int $i1, int $i2, int $i3, float $f) {
      if (this.totalPages > 1) {
         String s = this.currentPage + 1 + "/" + this.totalPages;
         int i = this.minecraft.font.width(s);
         this.minecraft.font.draw($ps, s, (float)($i0 - i / 2 + 73), (float)($i1 + 141), -1);
      }
      ...
```
If we look at the above class, we can see that the page indicator symbol within the recipe book GUI is hardcoded, and as a result, is untranslatable. This is evident through the following line of code:

```
String s = this.currentPage + 1 + "/" + this.totalPages;
```

## Comments (2)

### Comment 1: migrated (2022-02-28T00:51:07.838-0800)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: Avoma (2022-06-16T09:34:07.423-0700)

This ticket relates to MC-253176.
