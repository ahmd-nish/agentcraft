# MC-160001: Skulls, signs, hanging signs, banners and decorated pots have no breaking/sprinting particles

**Mojira URL:** [https://bugs.mojang.com/browse/MC-160001](https://bugs.mojang.com/browse/MC-160001)

## Report details

- **Mojira categories:** Particles
- **Project:** MC
- **Issue key:** MC-160001
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2019-08-28T16:29:47.257-0700
- **Updated:** 2026-05-23T09:57:32.303-0700
- **Resolution date:** 2024-12-10T05:37:40.969-0800
- **Affects versions:** 1.14.4; 19w35a; 19w36a; 19w37a; 19w38b; 19w39a; 19w40a; 19w41a; 19w42a; 19w44a; 19w45a; 1.15 Pre-release 1; 1.15 Pre-Release 2; 1.15 Pre-release 3; 1.15 Pre-release 4; 1.15 Pre-release 6; 1.15 Pre-release 7; 1.15.1 Pre-release 1; 1.15.2 Pre-Release 1; 1.15.2 Pre-release 2; 20w06a; 20w07a; 20w08a; 20w09a; 20w10a; 20w11a; 20w12a; 20w13a; 20w21a; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 5; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.3; 1.16.4; 20w49a; 20w51a; 21w03a; 21w05b; 21w06a; 21w20a; 1.17 Pre-release 1; 1.17; 1.17.1; 1.18.1; 1.18.2; 22w17a; 1.19; 1.19.2; 1.19.3; 23w05a; 1.20; 1.20.1; 1.21
- **Fix versions:** 24w46a
- **Area:** Gameplay
- **Labels:** missing-particle
- **Watchers:** 1
- **Attachments:** 7
- **Attachment filenames:** 2019-08-29_00.20.15.png; 2019-08-29_00.25.40.png; 2019-08-29_00.25.51.png; 2019-08-29_00.26.03.png; 2019-08-29_00.29.12.png; 2019-08-29_00.29.24.png; MC-160001.mp4
- **Issue links:** Duplicate:inward:MC-58127:No particles are produced while breaking signs or hanging signs | Relates:outward:MC-278286:Standing banners have breaking/sprinting particles but wall banners do not | Relates:inward:MC-166355:Item frames and paintings do not produce particles when broken

## Description

When punching or sprinting on certain blocks, no particles are given off, at least not until they actually break. This affects skulls, wall skulls (do these really need to still use a tile entity renderer?), banners, wall banners, signs and wall signs. Falling from a height into these blocks or successfully breaking them does produce particles as intended.
It may also be worth noting that all head blocks are also subject to  when regrading falling particles.

## Comments (17)

### Comment 1: migrated (2019-08-28T16:29:47.257-0700)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: FaRo1 (2019-09-12T13:11:35.559-0700)

Confirmed for 1.14.4 and 19w37a, at least the breaking particles for all three and the sprinting particles for skulls. Banner and sign sprinting particles are impossible to test in Vanilla, because they have no collision box.

### Comment 3: muzikbike (2019-09-18T05:19:41.531-0700)

has your back here for testing those ones

### Comment 4: migrated (2020-05-20T09:49:23.140-0700)

Affects 20w21a

### Comment 5: Avoma (2020-12-04T10:34:38.319-0800)

Can confirm in 20w49a.

### Comment 6: Avoma (2021-01-19T12:15:59.268-0800)

Can confirm in 20w51a.

### Comment 7: Avoma (2021-02-05T06:31:47.938-0800)

Can confirm in 21w05b.

### Comment 8: Avoma (2021-02-13T06:35:11.767-0800)

Can confirm in 21w06a.

### Comment 9: Avoma (2021-06-27T11:08:45.093-0700)

Can confirm in 1.17.

### Comment 10: Avoma (2021-07-22T05:06:39.690-0700)

Can confirm in 1.17.1.

### Comment 11: Avoma (2021-07-22T05:06:39.859-0700)

Can confirm in 1.17.1.

### Comment 12: Avoma (2021-12-20T06:09:14.415-0800)

Can confirm in 1.18.1.

### Comment 13: Avoma (2022-03-23T08:27:09.936-0700)

Can confirm in 1.18.2.

### Comment 14: Avoma (2022-07-15T11:57:26.853-0700)

Can confirm in 1.19.

### Comment 15: migrated (2023-06-09T04:24:48.330-0700)

Affects 1.20

### Comment 16: boq (2024-11-04T07:19:06.917-0800)

Resolved, except for signs

### Comment 17: muzikbike (2026-05-23T09:57:32.303-0700)

I believe signs should also be resolved now.
