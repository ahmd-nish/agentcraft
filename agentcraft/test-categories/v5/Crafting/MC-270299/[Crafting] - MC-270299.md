# MC-270299: New data pack component crafting doesn't work with suspicious stews

**Mojira URL:** [https://bugs.mojang.com/browse/MC-270299](https://bugs.mojang.com/browse/MC-270299)

## Report details

- **Mojira categories:** Crafting; Data Packs
- **Project:** MC
- **Issue key:** MC-270299
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2024-04-02T12:24:37.548-0700
- **Updated:** 2025-05-29T09:06:11.347-0700
- **Resolution date:** 2024-06-25T00:56:07.385-0700
- **Affects versions:** 24w13a; 24w14a; 1.20.5 Pre-Release 1; 24w21b
- **Fix versions:** 24w33a
- **Area:** Platform
- **Labels:** data-pack; recipes; suspicious_stew
- **Watchers:** 2
- **Attachments:** 6
- **Attachment filenames:** Screenshot 2024-04-02 122237.png; sus_stew_example.zip; sus_stew_example-1.zip; sus_stew_fix.zip; suspicious_stew_from_azure_bluet.json; suspicious_stew_from_flowering_azalea.json

## Description

Expected result: Custom suspicious stew (in this case a modified azure bluet suspicious stew) recipe outputs the water breathing effect.
Actual result: Azure bluet suspicious stew recipe defaults to the blindness effect, however, the recipe properly shows in the crafting table, but the result defaults to the vanilla output.
Description: Suspicious stew recipes that don't override vanilla recipes work fine (see
). Thus, I believe that data packs recipes are not superseding the hardcoded recipes (in this case all of the "crafting_special_suspiciousstew" recipes).
Steps to recreate:
- Add the attached data pack to world (see

- )

- Open world

- Craft azure bluet suspicious stew

- Craft flowering azalea suspicious stew

Proposed solution: Change all suspicious stew recipes to be data driven through data packs with the introduction of custom components in recipes outputs.
Edit: I don't know if this will help, but I made a data pack that implements the vanilla recipes with the new components (see
). To fix it, I used a block filter on the vanilla recipe in the .mcmeta file.

## Comments (3)

### Comment 1: migrated (2024-04-02T12:24:37.548-0700)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: [MOD] Greymagic27 (2024-04-07T04:52:04.365-0700)

Please attach a complete datapack .zip to help reproduce this issue

### Comment 3: BemuseLeader10 (2024-04-07T13:53:41.648-0700)

I have attached the datapack
