# MC-248833: The parentheses used before and after the warning label within the language menu are untranslatable

**Mojira URL:** [https://bugs.mojang.com/browse/MC-248833](https://bugs.mojang.com/browse/MC-248833)

## Report details

- **Mojira categories:** Internationalisation
- **Project:** MC
- **Issue key:** MC-248833
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2022-02-27T03:34:13.545-0800
- **Updated:** 2025-05-29T09:10:03.664-0700
- **Resolution date:** 2023-09-01T04:26:36.581-0700
- **Affects versions:** 1.18.1; 1.18.2 Release Candidate 1; 1.18.2; 1.19 Pre-release 1; 1.19; 1.19.1; 1.19.2; 22w43a; 22w45a; 1.19.3; 1.19.4; 1.20.1
- **Fix versions:** 1.20.2 Pre-release 1
- **Area:** Platform
- **Labels:** translatability
- **Watchers:** 2
- **Attachments:** 1
- **Attachment filenames:** MC-248833 - Context.png

## Description

The Bug:
The "(" and ")" symbols used before and after the warning label within the language menu are untranslatable and are missing translation keys.
This is a problem because every other string throughout the game that contains parentheses is translatable, therefore introducing an inconsistency. Below, I've constructed a table to visually demonstrate how and why this is a valid internationalization issue and to show the inconsistency.
Translation Key
String
Context
Are parentheses translatable?
selectServer.hiddenAddress
(Hidden)
This string is used to show when a server address is hidden.
Yes
menu.modded
(Modded)
This string is used within the title screen to show when your instance of Minecraft is modded.
Yes
options.biomeBlendRadius.3
3x3 (Fast)
This string is used within the video settings menu to show the value of the biome blend radius option.
Yes
multiplayer.status.no_connection
(no connection)
This string is used within the multiplayer menu to show when you have no connection to a server.
Yes
pack.folderInfo
(Place pack files here)
This string is used within pack menus to show where to place packs.
Yes
pack.incompatible.new
(Made for a newer version of Minecraft)
This string is used within pack menus to show that the desired pack is made for a newer version of Minecraft.
Yes
pack.incompatible.old
(Made for an older version of Minecraft)
This string is used within pack menus to show that the desired pack is made for an older version of Minecraft.
Yes
N/A
(Language translations may not be 100%% accurate)
This string is used within the language menu to warn players that language translations may not be fully accurate.
No
h3. Steps to Reproduce:
- Attempt to search for the existence of the string "(" by using this search filter, and the existence of the string ")" using this search filter, on the official Minecraft crowdin project.

- Take note as to whether or not the parentheses used before and after the warning label within the language menu are untranslatable.

Observed Behavior:
The parentheses used before and after the warning label within the language menu are untranslatable.
Expected Behavior:
The parentheses used before and after the warning label within the language menu would be translatable. To maintain consistency with other similar strings, the parentheses should be included within the "options.languageWarning" translatable text component.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.18.1 using MCP-Reborn.
net.minecraft.client.gui.screens.LanguageSelectScreen.java

```
public class LanguageSelectScreen extends OptionsSubScreen {
   private static final Component WARNING_LABEL = (new TextComponent("(")).append(new TranslatableComponent("options.languageWarning")).append(")").withStyle(ChatFormatting.GRAY);
   ...
```
If we look at the above class, we can see that the parentheses used before and after the warning label within the language menu are hardcoded, and as a result, are untranslatable. This is evident through the following piece of code:

```
(new TextComponent("(")) ... append(")")
```

## Comments (3)

### Comment 1: migrated (2022-02-27T03:34:13.545-0800)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: migrated (2022-02-27T09:42:59.104-0800)

I wonder why they're not just part of the string...

### Comment 3: Avoma (2022-02-28T01:25:21.926-0800)

I've constructed a table and added it to the description to show the inconsistency here and why I believe this is a valid internationalization issue. Hopefully this assists in understanding why this is a problem.
