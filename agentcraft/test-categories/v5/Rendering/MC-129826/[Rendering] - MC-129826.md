# MC-129826: ["shade": false] is missing from potted cross models, resulting in most potted plants appearing darker than they should

**Mojira URL:** [https://bugs.mojang.com/browse/MC-129826](https://bugs.mojang.com/browse/MC-129826)

## Report details

- **Mojira categories:** Rendering
- **Project:** MC
- **Issue key:** MC-129826
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2018-05-17T14:19:34.448-0700
- **Updated:** 2025-04-26T06:37:31.905-0700
- **Resolution date:** 2024-10-30T12:20:31.416-0700
- **Affects versions:** Minecraft 1.12.2; Minecraft 18w20c; Minecraft 18w22a; Minecraft 18w22c; Minecraft 1.13-pre5; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w43a; Minecraft 18w43b; Minecraft 18w43c; Minecraft 18w47b; Minecraft 18w48a; Minecraft 18w48b; Minecraft 19w04b; Minecraft 19w05a; Minecraft 19w12b; Minecraft 19w13b; Minecraft 19w14a; Minecraft 19w14b; 1.14.4; 19w45a; 1.15.2; 20w15a; 1.16.3; 1.16.4; 20w51a; 21w03a; 21w05b; 21w06a; 21w07a; 21w10a; 21w11a; 21w13a; 21w14a; 21w16a; 1.17 Pre-release 1; 1.17 Pre-release 2; 1.17 Pre-release 3; 1.17; 1.17.1 Pre-release 1; 1.17.1; 21w39a; 21w40a; 21w42a; 1.18 Pre-release 1; 1.18; 1.18.1 Pre-release 1; 1.18.1; 22w06a; 1.18.2; 22w11a; 22w15a; 1.19 Pre-release 1; 1.19; 1.19.1 Pre-release 3; 1.19.2; 1.19.3; 23w04a; 23w18a; 1.20.1; 1.20.4
- **Fix versions:** 24w33a
- **Area:** Gameplay
- **Labels:** 1.8-bad-model-conversion-remnants; 1.8-model-conversion-remnants; 14w25a; unwanted-model-shading; vanilla-parity
- **Watchers:** 1
- **Attachments:** 11
- **Attachment filenames:** 2022-03-18_22.52.40.png; 2022-03-18_23.11.29.png; 2022-03-18_23.12.42.png; 2022-03-19_14.53.34.png; 2022-03-19_14.54.12.png; Corrected Flower Pots.png; Current Flower Pots.png; flower_pot_cross.json; flower pots.jpg; flower pots fix.zip; tinted_flower_pot_cross.json
- **Issue links:** Relates:outward:MC-277950:Open potted eyeblossom is shaded (flower_pot_cross_emissive) | Relates:outward:MC-261214:Amethyst in calibrated sculk sensor is shaded and not stretched | Duplicate:inward:MC-214664:Plants in flower pots are shaded differently from when normally placed

## Description

The bug
When blocks were being converted over to using model files in 1.8, several of these conversions were incomplete and flawed, resulting in a multitude of issues. Many of these were resolved before the release of 1.8, however this specific issue was not.
In 14w25a, models involving flat 2D planes had those planes be rendered darker depending on their directions. This affected blocks such as grass, flowers and mushrooms, and was ultimately fixed (MC-57159). However, the same version also caused plants in flower pots to appear darker for the same reason, and this was not fixed.
As a result, plants which are placed in flower pots appear noticeably darker than those same plants when placed in the world (outside of a flower pot), which has been the case since 14w25a.
A comparison of the appearances of potted objects can be found below:
1.4.2 - 1.7.10 (expected rendering)
1.8 - present (incorrect rendering)

How to fix
This is ultimately incredibly easy to fix - the two texture plane elements in "flower_pot_cross.json" and its tinted version "tinted_flower_pot_cross.json" simply need a

```
"shade": false
```
 line added to them, which should resolve this unwanted darkening.
A comparison of potted objects with and without the fix can be found below:
22w11a (current rendering)
22w11a (fixed rendering)

Further notes
22w11a implemented potted mangrove propagules, which are completely unaffected by this issue affected slightly differently (see MC-262696) as they have a unique, dedicated model. Despite this, shading was not disabled for existing potted crosses in this version.

## Comments (37)

### Comment 1: migrated (2018-05-17T14:19:34.448-0700)

This comment contained multiple image attachments (11), please login to view the attachments.

### Comment 2: migrated (2018-05-29T19:13:56.384-0700)

Confirmed in 18w22a.

### Comment 3: migrated (2018-05-31T16:44:36.208-0700)

Confirmed in 18w22c.

### Comment 4: migrated (2018-06-28T13:58:41.828-0700)

Confirmed in 1.13-pre5.

### Comment 5: migrated (2019-04-07T05:18:02.172-0700)

Was able to re-create this in Minecraft 19w14b.

### Comment 6: TheBoy358 (2019-11-08T03:32:17.064-0800)

Confirmed in 1.14.4 and 19w45a.

### Comment 7: SoloAlguien (2021-01-12T00:58:56.632-0800)

Confirmed in 1.16.4 and 20w51a.
To fix this, the shading has to be removed from the plants (like when they are in the soil without a pot).
Files with the fix:

### Comment 8: SoloAlguien (2021-01-12T01:20:47.633-0800)

Also I attached screenshots of the wrong and fixed versions:

### Comment 9: Avoma (2021-01-12T01:33:46.796-0800)

Can confirm in 20w51a.

### Comment 10: SoloAlguien (2021-01-21T11:14:53.721-0800)

Confirmed in 21w03a.

### Comment 11: Avoma (2021-02-09T01:48:20.813-0800)

Can confirm in 21w05b.

### Comment 12: Avoma (2021-02-17T03:19:16.387-0800)

Can confirm in 21w06a.

### Comment 13: SoloAlguien (2021-03-13T10:06:26.110-0800)

Can confirm in 21w10a.

### Comment 14: SoloAlguien (2021-03-17T14:34:38.942-0700)

Can confirm in 21w11a.

### Comment 15: SoloAlguien (2021-03-27T15:16:54.947-0700)

Attached a resource pack with the fix.

### Comment 16: SoloAlguien (2021-04-02T20:07:31.440-0700)

Can confirm in 21w13a.

### Comment 17: SoloAlguien (2021-04-08T16:15:46.260-0700)

Can confirm in 21w14a.

### Comment 18: SoloAlguien (2021-04-21T12:56:35.558-0700)

Can confirm in 21w16a.

### Comment 19: migrated (2021-04-26T23:42:59.722-0700)

Duplicate of

### Comment 20: SoloAlguien (2021-05-14T12:38:59.241-0700)

Maybe this work as intended, since  was solved in this way.
I personally think the pots don't look good the way they are now and I don't think  has given the best examples and comparisons of this specific case.
I would like, if possible, that the decision be made with the images provided here.

### Comment 21: SoloAlguien (2021-05-28T16:47:24.887-0700)

Can confirm in 1.17 Pre-release 1.

### Comment 22: SoloAlguien (2021-05-31T14:25:15.906-0700)

Can confirm in 1.17 Pre-release 2.

### Comment 23: SoloAlguien (2021-06-01T22:16:46.832-0700)

Can confirm in 1.17 Pre-release 3.

### Comment 24: SoloAlguien (2021-06-20T11:49:40.977-0700)

Can confirm in 1.17 and 1.17.1 Pre-release 1.

### Comment 25: SoloAlguien (2021-07-11T15:31:58.940-0700)

Can confirm in 1.17.1.

### Comment 26: SoloAlguien (2021-09-29T14:25:36.882-0700)

Can confirm in 21w39a.

### Comment 27: muzikbike (2021-10-10T13:45:12.554-0700)

Affects 21w40a.
Requesting ownership as the creator has no activity for 11 months, as well as the fact that my ticket about this was resolved as a duplicate despite offering substantially more information, which would usually result in a ticket like this being forward-resolved.

### Comment 28: SoloAlguien (2021-10-20T10:52:39.367-0700)

Can confirm in 21w42a.

### Comment 29: Avoma (2021-10-20T11:22:42.283-0700)

, this is unrelated to this issue. Please see MCL-16570.

### Comment 30: SoloAlguien (2021-11-11T10:35:44.364-0800)

Can confirm in 1.18 Pre-release 1.

### Comment 31: SoloAlguien (2021-12-03T15:05:41.622-0800)

Can confirm in 1.18 and 1.18.1 Pre-release 1.

### Comment 32: SoloAlguien (2021-12-17T21:31:09.572-0800)

Can confirm in 1.18.1.

### Comment 33: SoloAlguien (2022-03-01T12:10:40.238-0800)

Can confirm in 1.18.2.

### Comment 34: muzikbike (2022-03-18T15:55:32.477-0700)

An interesting thing to note is that mangrove propagules have been given a dedicated model, and that this issue is not present on this model due to shading have been explicitly disabled for it. Curiously, despite this, the existing cross models have been left in their shaded state:

### Comment 35: Avoma (2022-07-25T05:38:47.833-0700)

Can confirm in 1.19.

### Comment 36: Avoma (2022-08-27T04:51:56.976-0700)

Can confirm in 1.19.2.

### Comment 37: migrated (2023-01-28T23:23:29.523-0800)

i can confirm in 1.19.3 and 23w04a
