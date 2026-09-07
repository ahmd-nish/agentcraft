# MC-269996: Custom names of Interaction entities render at wrong location

**Mojira URL:** [https://bugs.mojang.com/browse/MC-269996](https://bugs.mojang.com/browse/MC-269996)

## Report details

- **Mojira categories:** Data Packs; Entities
- **Project:** MC
- **Issue key:** MC-269996
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-03-27T15:28:33.169-0700
- **Updated:** 2025-05-29T09:06:15.480-0700
- **Resolution date:** 2024-07-24T03:06:13.934-0700
- **Affects versions:** 1.20.4; 24w13a; 1.20.6; 1.21
- **Fix versions:** 24w33a
- **Area:** Platform
- **Watchers:** 2
- **Attachments:** 3
- **Attachment filenames:** 2024-03-27_15.07.38.png; 2024-03-27_15.08.12.png; 2024-03-27_15.16.25.png
- **Issue links:** Relates:outward:MC-273578:Interaction entities position passengers incorrectly

## Description

Since 1.20.3, Interaction entities have been able to display custom names given the resolution of MC-236501 This is a great convenience when it comes to custom content creation for artificial mobs. It can allow with one entity, a hitbox and a naturally positioned and functional nametag (i.e. visible when looked-at or always respecting "CustomNameVisible"). However, currently to take full advantage of this functionality a modified server is required to force the game client understand the height (and width) of the desired Interaction entity dimensions.
As is, summoning an Interaction entity with a custom name shows the nameplate rendered as if the height of the entity was zero, instead of above what should be the real height of the entity. This is because the internally the cached Entity#dimensions field of the entity is not recomputed (as would by Entity#refreshDimensions()) when the width or height of Interaction entity changes, leading to Entity#getBbHeight() and Entity#getBbWidth() always being zero. This inconsistency also impacts the server, however those effects are less observable.
A modified server can workaround this oversight by forcing a dimension refresh by syncing an arbitrary Entity#DATA_POSE change when updating width and height, though being mindful to order the Pose last in the synched entries.
For data pack makers however, nothing can be done to fix the erroneous nameplate rendering, limiting the possibilities of the custom named Interaction entity usage.
Steps to reproduce:
- In Minecraft 1.20.3 or later, summon an Interaction entity with a custom name and width/height matching an Armor Stand using the command:
/summon interaction ~ ~ ~ {CustomName:'"Test"',CustomNameVisible:1,width:0.5,height:1.975}

- Summon a regular Armor Stand with custom name using the command:
/summon armor_stand ~ ~ ~ {CustomName:'"Test"',CustomNameVisible:1}

- Summon a marker Armor Stand with custom name using the command:
/summon armor_stand ~ ~ ~ {CustomName:'"Test"',CustomNameVisible:1,Marker:1}

Expected results:
- The Interaction entity's nameplate should render above the entity at a height corresponding to the specified height value (1.975 in this case, same as the summoned regular Armor Stand).

Observed results:
- The Interaction entity's nameplate renders as if the entity had zero height, similar to the summoned marker Armor Stand. I have attached three screenshots demonstrating each summoned entity for reference.

## Comments (3)

### Comment 1: migrated (2024-03-27T15:28:33.169-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: [MOD] Greymagic27 (2024-03-29T05:05:18.331-0700)

Please update the description to include consice steps on how to reproduce this issue, as well as expected VS observed results

### Comment 3: GrantGryczan (2024-06-18T21:33:37.124-0700)

Confirmed in 1.21. Also, relates to .
