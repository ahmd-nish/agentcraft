# MC-276825: Transmute recipes allow air as output

**Mojira URL:** [https://bugs.mojang.com/browse/MC-276825](https://bugs.mojang.com/browse/MC-276825)

## Report details

- **Mojira categories:** Crafting; Data Packs
- **Project:** MC
- **Issue key:** MC-276825
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2024-09-18T11:32:42.416-0700
- **Updated:** 2025-02-11T06:09:49.071-0800
- **Resolution date:** 2024-10-09T04:16:40.909-0700
- **Affects versions:** 24w38a
- **Fix versions:** 1.21.2 Pre-Release 2
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** Minecraft 24w38a - Singleplayer 2024-09-19 03-24-40.mp4; transmute_pack.zip

## Description

Summary
A recipe with crafting_transmute type can set its result to minecraft:air, and such recipes are considered valid. This is not possible with other types of recipes.
There is no way to craft air using this method. However, when the recipe is granted, the recipe book shows how to craft air.
Steps to Reproduce
- Add the attached data pack to a world

- Run /recipe give @s test:test_recipe

- Open Crafting Table

Expected Result
Recipe fails to load, the command fails, and no air is present on the recipe book.
Actual Result
The recipe loads, the command succeeds, and air is present on the recipe book.

## Comments (1)

### Comment 1: migrated (2024-09-18T11:32:42.416-0700)

This comment contained multiple image attachments (2), please login to view the attachments.
