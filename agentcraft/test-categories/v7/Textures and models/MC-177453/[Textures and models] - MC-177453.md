# MC-177453: Unneeded faces inside comparator models

**Mojira URL:** [https://bugs.mojang.com/browse/MC-177453](https://bugs.mojang.com/browse/MC-177453)

## Report details

- **Mojira categories:** Textures and models
- **Project:** MC
- **Issue key:** MC-177453
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2020-04-04T17:31:35.141-0700
- **Updated:** 2025-04-26T09:43:42.586-0700
- **Resolution date:** 2024-08-17T07:14:49.205-0700
- **Affects versions:** 1.15.2; 20w14a; 20w18a; 20w21a; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16.1; 20w27a; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 20w49a; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w08b; 21w15a; 21w16a; 21w20a; 1.17 Pre-release 1; 1.17; 1.17.1; 1.18; 1.18.1; 1.18.2; 1.19; 1.19.2; 1.20 Pre-release 1; 1.20.1; 23w43a; 1.21
- **Fix versions:** 24w33a
- **Area:** Gameplay
- **Labels:** 1.8-bad-model-conversion-remnants; 1.8-model-conversion-remnants; unnecessary-planes
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2020-04-05_01.26.20.png; comparator_on.json; comparator_subtract.json; comparator.json
- **Issue links:** Relates:inward:MC-177452:Unneeded faces inside repeater models | Relates:outward:MC-208191:Unneeded face in candle cake model | Duplicate:inward:MC-193574:Cullface inconsistency with torches on repeaters | Duplicate:inward:MC-159201:Lit torches on repeaters and comparators are missing their bottom texture, while they have a bottom face when unlit

## Description

The resource pack attached to MC-214686 offers a complete fix for this issue. Mojang have my full permission to (and are encouraged to) replace the affected vanilla model files with the contents of the resource pack.
The bug
Redstone comparator models define faces for the bottoms of unlit redstone torches, despite these never being visible without clipping into the comparator itself. Powered torches correctly omit such faces due to not using a single cuboid.
How to reproduce
- Place down an unpowered redstone comparator

- Enter Spectator mode

- Fly into the comparator such that the bottoms of the torches are in view

Expected behaviour
The unpowered torches would not have any bottom faces defined since such faces are never possible to see in normal gameplay.
Actual behaviour
These bottom faces are defined anyway, bloating the model file and forcing the game to render useless faces.
How to fix
The resource pack attached to MC-214686 fixes this issue completely.

## Comments (16)

### Comment 1: migrated (2020-04-04T17:31:35.141-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: Avoma (2020-12-03T10:56:17.044-0800)

Can confirm in 20w49a.

### Comment 3: Avoma (2021-01-20T03:47:15.142-0800)

Can confirm in 20w51a.

### Comment 4: Avoma (2021-02-05T06:59:23.203-0800)

Can confirm in 21w05b.

### Comment 5: Avoma (2021-02-13T08:35:58.666-0800)

Can confirm in 21w06a.

### Comment 6: Avoma (2021-03-01T01:21:42.479-0800)

Can confirm in 1.16.5 and 21w08b.

### Comment 7: Avoma (2021-04-18T10:45:57.212-0700)

Can confirm in 21w15a.

### Comment 8: Avoma (2021-04-26T02:51:37.472-0700)

Can confirm in 21w16a.

### Comment 9: Avoma (2021-06-12T11:53:47.046-0700)

Can confirm in 1.17.

### Comment 10: ampolive (2021-07-17T17:38:21.909-0700)

Can confirm in 1.17.1.

### Comment 11: Avoma (2021-12-08T07:21:29.899-0800)

Can confirm in 1.18.

### Comment 12: Avoma (2021-12-17T05:34:29.779-0800)

Can confirm in 1.18.1.

### Comment 13: Avoma (2022-03-07T09:52:48.711-0800)

Can confirm in 1.18.2.

### Comment 14: Avoma (2022-06-26T11:36:57.658-0700)

Can confirm in 1.19.

### Comment 15: Avoma (2022-09-06T10:28:06.849-0700)

Can confirm in 1.19.2.

### Comment 16: muzikbike (2024-08-15T09:41:12.143-0700)

24w33a fixes this
