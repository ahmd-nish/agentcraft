# MC-240021: Cullface arguments in cauldrons are excessive

**Mojira URL:** [https://bugs.mojang.com/browse/MC-240021](https://bugs.mojang.com/browse/MC-240021)

## Report details

- **Mojira categories:** Textures and models
- **Project:** MC
- **Issue key:** MC-240021
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2021-10-29T06:21:17.774-0700
- **Updated:** 2025-04-26T14:01:02.731-0700
- **Resolution date:** 2024-09-10T04:25:01.837-0700
- **Affects versions:** 1.17.1; 21w43a
- **Fix versions:** 1.18 Pre-release 1
- **Labels:** unnecessary-cullface
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2021-10-29_13.43.07.png; 2021-10-29_13.43.09.png; 2021-10-29_13.43.18.png; cauldron-interior-fix-21w43a-v1.0.zip

## Description

The bug
In very early 2019, cauldrons were changed such that the interior faces would be culled if a block existed right on top of said cauldron, since there was no way of actually being able to see these faces outside of Spectator mode. A later 1.14 snapshot, however, implemented crawling, which allowed for the insides of cauldrons to be inhabited in Survival gameplay while a block was on top of it. The face culling results in the effects of MC-206620.
How to reproduce
- Build the contraption shown in the screenshots below

- Using the trapdoor to initiate crawling, enter the cauldron, then pull the lever

- Note that you can see clearly outside of the cauldron while in it (MC-206620)

Expected behaviour
The interior faces of the cauldron would not be culled, since it's a region the player can enter in Survival without exploiting glitches
Actual behaviour
The model file, assuming the player cannot enter cauldrons like this, still has interior faces set to be culled.
How to fix
This is another simple model fix, as all that needs done is the removal of cullface from these five specific faces (where the cullface is "up", but the face plane direction itself is not "up", excluding for the bottom interior, which can then be seen to not be flush with the top face due to its low y "to" value). The resource pack attached fixes this issue in its entirety, and can therefore easily just be copied into the jar file to fix this (as usual I give full permission/rights to Mojang to use this).
The resource pack also completely fixes , removes the line that disables ambient occlusion as it wasn't doing much anyway besides making cauldrons visually inconsistent from other blocks, and also tidies up the model code to make it easier to read.

## Comments (3)

### Comment 1: migrated (2021-10-29T06:21:17.774-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: Arisa Bot (2021-11-10T14:24:12.490-0800)

Please do not add Affected Versions to resolved reports.
Have a look at the Resolution and the comments to see why this ticket has been resolved. If you think this ticket has been resolved erroneously you can contact the Mojira staff on Discord or Reddit.
-- I am a bot. This action was performed automatically! If you think it was incorrect, please notify us on Discord or Reddit

### Comment 3: Arisa Bot (2021-11-11T04:32:40.143-0800)

Please do not add Affected Versions to resolved reports.
Have a look at the Resolution and the comments to see why this ticket has been resolved. If you think this ticket has been resolved erroneously you can contact the Mojira staff on Discord or Reddit.
-- I am a bot. This action was performed automatically! If you think it was incorrect, please notify us on Discord or Reddit
