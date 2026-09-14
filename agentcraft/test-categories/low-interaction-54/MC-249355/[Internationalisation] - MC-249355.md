# MC-249355: The hyphen used within the statistics menu to show a null value is untranslatable

**Mojira URL:** [https://bugs.mojang.com/browse/MC-249355](https://bugs.mojang.com/browse/MC-249355)

## Report details

- **Mojira categories:** Internationalisation
- **Project:** MC
- **Issue key:** MC-249355
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2022-03-23T11:48:27.754-0700
- **Updated:** 2025-03-25T12:56:45.749-0700
- **Resolution date:** 2023-09-01T04:26:34.754-0700
- **Affects versions:** 1.18.2; 1.19 Pre-release 1; 1.19; 1.19.1; 1.19.2; 22w43a; 22w45a; 1.19.3; 1.19.4; 1.20.1
- **Fix versions:** 1.20.2 Pre-release 1
- **Area:** Platform
- **Labels:** translatability
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** MC-249355 - Context.png

## Description

The Bug:
The "-" symbol within the statistics menu used to show a null value is untranslatable and is missing a translation key.
Steps to Reproduce:
- Attempt to search for the existence of this string by using this search filter on the official Minecraft crowdin project.

- Take note as to whether or not the hyphen used within the statistics menu to show a null value is untranslatable.

Observed Behavior:
The hyphen used within the statistics menu to show a null value is untranslatable.
Expected Behavior:
The hyphen used within the statistics menu to show a null value would be translatable.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.18.2 using MCP-Reborn.
net.minecraft.client.gui.screens.achievement.StatsScreen.java

```
public class StatsScreen extends Screen implements StatsUpdateListener {
   ...
   class ItemStatisticsList extends ObjectSelectionList<StatsScreen.ItemStatisticsList.ItemRow> {
      ...
      class ItemRow extends ObjectSelectionList.Entry<StatsScreen.ItemStatisticsList.ItemRow> {
         ...
         protected void renderStat(PoseStack $ps, @Nullable Stat<?> $s, int $i0, int $i1, boolean $b) {
            String s = $s == null ? "-" : $s.format(StatsScreen.this.stats.getValue($s));
            GuiComponent.drawString($ps, StatsScreen.this.font, s, $i0 - StatsScreen.this.font.width(s), $i1 + 5, $b ? 16777215 : 9474192);
         }
         ...
```
If we look at the above class, we can see that the hyphen used within the statistics menu to show a null value is hardcoded, and as a result, is untranslatable. This is evident through the following piece of code:

```
String s = $s == null ? "-" ...
```

## Comments (2)

### Comment 1: migrated (2022-03-23T11:48:27.754-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: Avoma (2022-03-23T11:49:15.989-0700)

I've reported this because MC-177172, (which is a report about the hyphen within the villager trading GUI not being translatable), is considered a valid problem by Mojang Studios, therefore leading me to believe that the hyphen within the statistics menu used to show a null value, should be translatable as well.
