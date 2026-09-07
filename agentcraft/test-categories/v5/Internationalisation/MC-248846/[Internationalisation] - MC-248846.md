# MC-248846: The colon used within the death screen to show the player's score is untranslatable

**Mojira URL:** [https://bugs.mojang.com/browse/MC-248846](https://bugs.mojang.com/browse/MC-248846)

## Report details

- **Mojira categories:** Internationalisation
- **Project:** MC
- **Issue key:** MC-248846
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2022-02-28T02:14:23.229-0800
- **Updated:** 2025-04-30T03:36:38.357-0700
- **Resolution date:** 2023-09-01T04:26:35.216-0700
- **Affects versions:** 1.18.1; 1.18.2 Release Candidate 1; 1.18.2; 1.19 Pre-release 1; 1.19; 1.19.1; 1.19.2; 22w43a; 22w45a; 1.19.3; 1.19.4; 1.20.1
- **Fix versions:** 1.20.2 Pre-release 1
- **Area:** Platform
- **Labels:** translatability
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** MC-248846 - Context.png

## Description

The Bug:
The ":" symbol that exists after the word "Score" within the death screen is untranslatable and is missing a translation key.
Every language has its own rules that it follows. This ranges from spelling words differently, to using different punctuation under certain circumstances. Throughout the game, different languages can have symbols translated differently, therefore leading me to believe that this is a valid internationalization problem. For example, take the "options.controls" translatable text component which reads "Controls..." in English (US), and "按鍵設定⋯⋯" in Chinese Traditional, Hong Kong. As you can see the periods/full stops used within the Chinese Traditional, Hong Kong translation are completely different from the ones used in the English (US) translation. With this piece of knowledge in mind, some languages may interpret the use of the ":" symbol differently.
Steps to Reproduce:
- Attempt to search for the existence of this string by using this search filter on the official Minecraft crowdin project.

- Take note as to whether or not the colon used within the death screen to show the player's score is untranslatable.

Observed Behavior:
The colon used within the death screen to show the player's score is untranslatable.
Expected Behavior:
The colon used within the death screen to show the player's score would be translatable.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.18.1 using MCP-Reborn.
net.minecraft.client.gui.screens.DeathScreen.java

```
public class DeathScreen extends Screen {
   ...
   protected void init() {
      ...
      this.deathScore = (new TranslatableComponent("deathScreen.score")).append(": ").append((new TextComponent(Integer.toString(this.minecraft.player.getScore()))).withStyle(ChatFormatting.YELLOW));
   ...
```
If we look at the above class, we can see that the colon used within the death screen to show the player's score is hardcoded, and as a result, is untranslatable. This is evident through the following piece of code:

```
append(": ")
```

## Comments (2)

### Comment 1: migrated (2022-02-28T02:14:23.229-0800)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: bodakugga (2022-03-08T05:35:14.209-0800)

The ideal fix would include variables for the "Score" string and the score value, so it would be something like "%s: %s", or "Score: %s"
