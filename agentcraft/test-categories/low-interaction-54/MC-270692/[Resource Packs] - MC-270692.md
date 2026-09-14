# MC-270692: Textures for empty slots do not support translucent pixels

**Mojira URL:** [https://bugs.mojang.com/browse/MC-270692](https://bugs.mojang.com/browse/MC-270692)

## Report details

- **Mojira categories:** Rendering; Resource Packs; Textures and models
- **Project:** MC
- **Issue key:** MC-270692
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2024-04-12T12:26:16.100-0700
- **Updated:** 2025-04-10T14:59:23.558-0700
- **Resolution date:** 2024-09-21T17:22:12.312-0700
- **Affects versions:** 1.20.4; 1.20.5 Pre-Release 1; 1.20.5 Pre-Release 2; 24w19b
- **Fix versions:** 24w33a
- **Labels:** translucency-nonfunctional
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** 2024-04-12_19.52.38.png; 2024-04-12_19.52.50.png; 2024-04-12_20.02.57.png; 2024-04-12_20.20.48.png; 2024-04-12_20.20.59.png; empty-slot-translucency-1.20.5pre1-v1.0.zip
- **Issue links:** Relates:outward:MC-109447:Inconsistency in transparency of GUI PNG files - only some can be transparent + hover-bugs | Relates:outward:MC-270765:Bundle background does not handle translucent pixels correctly

## Description

More loosely relates to these issues:  MC-145821  MC-165403
The bug
If textures used for empty slots are given translucent textures, they will incorrectly render as opaque in-game.
This concerns standalone sprites for empty slots - in most cases, the slots are baked into the UI texture (see MC-165182).
Affected slots
- slot.png (used in Statistics and in superflat customization)

- Bundle slots

- Donkey/mule/llama chest slots

The saddle, armor and carpet slots used for horses, donkeys, mules, llamas and camels are also affected by this issue, but this specific case is covered under MC-269445. Making the slot item outline its own texture, and then baking the actual slot shape into the UI texture file (one for each mob), would fix  and .
How to reproduce
- Download and apply the attached resource pack

- Enter the statistics item menu, the superflat customization menu, a donkey/mule/llama's UI or mouse over a bundle

- Observe

Expected results
Translucent slots.
Actual results
Entirely opaque.

## Comments (1)

### Comment 1: migrated (2024-04-12T12:26:16.100-0700)

This comment contained multiple image attachments (6), please login to view the attachments.
