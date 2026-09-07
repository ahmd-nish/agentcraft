# MC-199238: Unneeded faces and missing cullface in dragon egg model

**Mojira URL:** [https://bugs.mojang.com/browse/MC-199238](https://bugs.mojang.com/browse/MC-199238)

## Report details

- **Mojira categories:** Textures and models
- **Project:** MC
- **Issue key:** MC-199238
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2020-08-29T09:04:46.141-0700
- **Updated:** 2025-04-26T11:12:12.679-0700
- **Resolution date:** 2024-08-15T09:07:21.189-0700
- **Affects versions:** 1.16.2; 1.16.3; 1.16.4; 20w46a; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w08b; 21w11a; 21w13a; 21w14a; 21w16a; 21w17a; 21w18a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17; 1.17.1; 21w39a; 21w40a; 21w42a; 21w44a; 1.18; 1.18.1 Pre-release 1; 1.18.1; 1.18.2; 1.19; 1.19.2; 1.19.4 Pre-release 3; 1.19.4; 23w14a; 1.20 Pre-release 1; 1.20.1; 23w43a; 1.21; 1.21.1 Release Candidate 1; 1.21.1
- **Fix versions:** 24w33a
- **Area:** Gameplay
- **Labels:** cullface-missing-from-model; unnecessary-planes
- **Watchers:** 1
- **Attachments:** 10
- **Attachment filenames:** 2020-08-29_15.57.29.png; 2020-08-29_17.00.21.png; 2020-08-29_17.00.36.png; 2020-08-29_17.00.55.png; 2020-08-29_17.01.07.png; 2020-08-29_17.01.31.png; dragon_egg.json; dragon-egg-fix-21w40a-v1.0.zip; dragon-egg-fix-21w41a-v1.1.zip; MC-199238.mp4
- **Issue links:** Relates:outward:MC-208191:Unneeded face in candle cake model | Relates:outward:MC-193948:Unneeded face inside attached unpowered tripwire hook model

## Description

The resource pack attached offers a complete fix for this issue. Mojang have my full permission to (and are encouraged to) replace the affected vanilla model files with the contents of the resource pack.
Download resource pack:
- 21w41a:

The bug
The dragon egg includes numerous block faces which cannot be seen normally - in order to see these faces, clipping into the block is required, such as through Spectator mode. In addition, the topmost and bottommost faces are missing cullface specifications standard of other models which have faces which end up hidden by adjacent blocks.
How to reproduce
- Place down a dragon egg

- Enter Spectator mode

- Fly inside of the dragon egg
- You will find yourself inside of a stack of cuboids, with many of the faces of these cuboids completely invisible from outside

- Now place opaque blocks on the top and bottom of the egg

- Fly into these opaque blocks
- Looking closely reveals that the dragon egg faces against these blocks are still visible despite their complete occlusion

Expected results
Only faces which are visible during normal gameplay are rendered.
Actual results
Every single face of each cuboid, including the ones which are only visible if the player is inside of the dragon egg, is always rendered.
How to fix
The resource pack attached to this ticket fixes this issue completely - all lines pertaining to these redundant faces are deleted (which shrinks the model file considerably), and the top and bottom faces now have cullface specified.
The model also fixes MC-120417, and re-enables ambient occlusion for the model, as it was disabled before despite offering little to no visual difference.
Formatting has also been changed for consistency and readability.

## Comments (26)

### Comment 1: migrated (2020-08-29T09:04:46.141-0700)

This comment contained multiple image attachments (10), please login to view the attachments.

### Comment 2: markderickson (2020-09-02T09:48:44.947-0700)

Hi there!
I can confirm.

### Comment 3: Avoma (2020-11-23T08:56:35.051-0800)

I can confirm for 20w46a.

### Comment 4: Avoma (2021-01-15T05:29:04.924-0800)

Can confirm in 20w51a.

### Comment 5: Avoma (2021-02-05T07:33:27.819-0800)

Can confirm in 21w05b.

### Comment 6: Avoma (2021-02-13T09:16:44.236-0800)

Can confirm in 21w06a.

### Comment 7: Avoma (2021-02-28T08:56:23.199-0800)

Can confirm in 21w08b. Video attached.

### Comment 8: Avoma (2021-03-24T07:51:11.299-0700)

Can confirm in 21w11a.

### Comment 9: SoloAlguien (2021-04-02T21:35:18.008-0700)

Can confirm in 21w13a.

### Comment 10: SoloAlguien (2021-04-08T16:23:51.468-0700)

Can confirm in 21w14a.

### Comment 11: SoloAlguien (2021-04-21T13:42:29.302-0700)

Can confirm in 21w16a.

### Comment 12: SoloAlguien (2021-05-02T11:43:05.168-0700)

Can confirm in 21w17a.

### Comment 13: SoloAlguien (2021-05-07T12:30:11.116-0700)

Can confirm in 21w18a.

### Comment 14: SoloAlguien (2021-05-15T18:06:31.127-0700)

Can confirm in 21w19a.

### Comment 15: SoloAlguien (2021-06-01T22:30:14.977-0700)

Can confirm in 1.17 Pre-release 3.

### Comment 16: Avoma (2021-06-11T10:43:20.519-0700)

Can confirm in 1.17.

### Comment 17: SoloAlguien (2021-07-11T15:40:22.531-0700)

Can confirm in 1.17.1.

### Comment 18: SoloAlguien (2021-09-29T14:36:05.532-0700)

Can confirm in 21w39a.

### Comment 19: SoloAlguien (2021-10-20T10:59:35.074-0700)

Can confirm in 21w42a.

### Comment 20: ampolive (2021-11-10T15:45:52.501-0800)

Can confirm in 21w44a.

### Comment 21: SoloAlguien (2021-12-03T15:11:54.999-0800)

Can confirm in 1.18 and 1.18.1 Pre-release 1.

### Comment 22: SoloAlguien (2021-12-17T21:34:27.858-0800)

Can confirm in 1.18.1.

### Comment 23: SoloAlguien (2022-03-01T12:16:07.995-0800)

Can confirm in 1.18.2.

### Comment 24: Avoma (2022-07-10T05:35:37.724-0700)

Can confirm in 1.19.

### Comment 25: Avoma (2022-09-08T05:36:58.354-0700)

Can confirm in 1.19.2.

### Comment 26: muzikbike (2024-08-15T09:01:04.857-0700)

This issue is completely fixed as of 24w33a.
