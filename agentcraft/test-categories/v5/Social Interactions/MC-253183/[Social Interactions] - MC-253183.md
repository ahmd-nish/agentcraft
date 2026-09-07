# MC-253183: The word "Unrelated" within the "gui.chatSelection.fold" string is incorrectly capitalized

**Mojira URL:** [https://bugs.mojang.com/browse/MC-253183](https://bugs.mojang.com/browse/MC-253183)

## Report details

- **Mojira categories:** Social Interactions
- **Project:** MC
- **Issue key:** MC-253183
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2022-06-16T09:29:44.047-0700
- **Updated:** 2025-03-20T23:48:49.471-0700
- **Resolution date:** 2022-06-29T06:56:23.296-0700
- **Affects versions:** 22w24a
- **Fix versions:** 1.19.1 Pre-release 1
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-253183.png; MC-253183 - Analysis.png

## Description

The Bug:
The word "Unrelated" within the "gui.chatSelection.fold" string is incorrectly capitalized.
This string currently reads "%s Unrelated messages hidden" (where "%s" represents a number), so there is no need to capitalize the word "Unrelated" here. In English, when a number is used at the beginning of a sentence, there is no need to capitalize the word that comes after it, and doing this is often seen as grammatically incorrect.
Below, I've constructed a table that states all of the necessary and relevant information regarding this issue.
Affected String:
Before reading the table, please note the following:
- Words colored in GREEN are correct.

- Words colored in RED are incorrect.

Translation Key
Current String
Expected String
String URL on Crowdin
gui.chatSelection.fold
%s Unrelated messages hidden
%s unrelated messages hidden
https://crowdin.com/translate/minecraft/10002/enus-engb#5296050
h3. Steps to Reproduce:
- Display this string by executing the command provided below.

```
/tellraw @s {"translate":"gui.chatSelection.fold"}
```
- Look closely at the capitalization within this string.

- Take note as to whether or not the word "Unrelated" within the "gui.chatSelection.fold" string is incorrectly capitalized.

Observed Behavior:
The word "Unrelated" is incorrectly capitalized.
Expected Behavior:
The word "Unrelated" would not be capitalized.

## Comments (2)

### Comment 1: migrated (2022-06-16T09:29:44.047-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: [Mod] turbo (2022-06-16T09:30:24.112-0700)

Can confirm.
