# MC-248684: Fog on moving pistons happens too early

**Mojira URL:** [https://bugs.mojang.com/browse/MC-248684](https://bugs.mojang.com/browse/MC-248684)

## Report details

- **Mojira categories:** Rendering
- **Project:** MC
- **Issue key:** MC-248684
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2022-02-18T17:48:55.974-0800
- **Updated:** 2025-04-26T14:14:53.147-0700
- **Resolution date:** 2025-01-24T05:38:01.267-0800
- **Affects versions:** 1.18.1 Pre-release 1; 1.18.2 Pre-release 1; 1.18.2; 1.19; 1.19.3; 23w07a
- **Fix versions:** 24w05a
- **Area:** Platform
- **Labels:** fog
- **Watchers:** 1
- **Attachments:** 7
- **Attachment filenames:** 2022-02-19_01.42.15.png; 2022-02-19_01.42.32.png; 2022-02-19_01.42.34.png; 2022-02-19_01.42.44.png; 202302201000.mp4; MC-248684.mp4; MC-248684.png
- **Issue links:** Relates:outward:MC-264821:The fog on armor worn by entities occurs too early

## Description

Found while testing . Very closely relates to MC-244190 - it appears to be effectively the same issue in that it was only resolved for entities and was not for pistons.
The bug
Fog starts to occlude moving pistons far earlier than it does normal blocks and entities, especially vertically - it appears to still use the spherical fog rather than the updated cylindrical fog.
How to reproduce
- Connect pistons to a redstone clock

- Travel far enough away from the pistons such that they're close to being obscured by fog, but not quite (low render distance recommended)

Expected results
The pistons would still fit in with the other blocks, being occluded by fog at the same rate.
Actual results
When in motion, the pistons appear almost completely fogged, even if the blocks around it are only fogged to a comparatively minor extent.

## Comments (6)

### Comment 1: migrated (2022-02-18T17:48:55.974-0800)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: Avoma (2022-03-06T05:48:30.545-0800)

Can confirm in 1.18.2.

### Comment 3: Avoma (2022-06-07T10:36:30.997-0700)

Can confirm in 1.19.

### Comment 4: migrated (2023-02-19T18:06:19.543-0800)

in 23w07a:

### Comment 5: muzikbike (2024-12-29T09:32:43.155-0800)

Can no longer reproduce in 1.21.4 - possibly fixed in 24w05a alongside MC-248689?

### Comment 6: Fantastime (2025-01-24T04:47:41.013-0800)

Does this issue still occur in latest version?
