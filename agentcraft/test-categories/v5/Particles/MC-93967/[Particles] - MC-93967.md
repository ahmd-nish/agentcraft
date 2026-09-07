# MC-93967: The smoke particles of the explosion are displayed when Particles option is set to minimal

**Mojira URL:** [https://bugs.mojang.com/browse/MC-93967](https://bugs.mojang.com/browse/MC-93967)

## Report details

- **Mojira categories:** Particles; Performance
- **Project:** MC
- **Issue key:** MC-93967
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2015-12-06T23:55:27.579-0800
- **Updated:** 2025-04-16T13:03:27.108-0700
- **Resolution date:** 2021-10-18T06:59:00.817-0700
- **Affects versions:** Minecraft 1.8.8; Minecraft 15w47c; Minecraft 15w49a; Minecraft 15w49b; Minecraft 1.8.9; Minecraft 15w50a; Minecraft 15w51a; Minecraft 15w51b; Minecraft 16w02a; Minecraft 16w03a; Minecraft 16w04a; Minecraft 16w05a; Minecraft 16w05b; Minecraft 16w06a; Minecraft 16w07a; Minecraft 1.9 Pre-Release 1; Minecraft 1.9 Pre-Release 2; Minecraft 1.9 Pre-Release 3; Minecraft 1.9 Pre-Release 4; Minecraft 1.9; Minecraft 1.9.1 Pre-Release 1; Minecraft 1.9.1 Pre-Release 2; Minecraft 1.9.1 Pre-Release 3; Minecraft 1.9.2; Minecraft 16w14a; Minecraft 16w15a; Minecraft 16w15b; Minecraft 1.9.3 Pre-Release 1; Minecraft 1.9.3 Pre-Release 3; Minecraft 1.9.3; Minecraft 1.9.4; Minecraft 16w20a; Minecraft 16w21b; Minecraft 1.10.2; Minecraft 16w33a; Minecraft 16w35a; Minecraft 16w36a; Minecraft 16w38a; Minecraft 16w39a; Minecraft 16w40a; Minecraft 16w41a; Minecraft 1.11; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 17w14a; Minecraft 17w15a; Minecraft 17w16a; Minecraft 17w16b; Minecraft 17w17a; Minecraft 17w17b; Minecraft 17w18a; Minecraft 17w18b; Minecraft 1.12 Pre-Release 1; Minecraft 1.12 Pre-Release 2; Minecraft 1.12 Pre-Release 3; Minecraft 1.12 Pre-Release 4; Minecraft 1.12 Pre-Release 5; Minecraft 1.12 Pre-Release 6; Minecraft 1.12 Pre-Release 7; Minecraft 1.12; Minecraft 1.12.1 Pre-Release 1; Minecraft 1.12.1; Minecraft 1.12.2 Pre-Release 1; Minecraft 1.12.2 Pre-Release 2; Minecraft 1.12.2; Minecraft 17w43a; Minecraft 17w43b; Minecraft 17w45a; Minecraft 17w45b; Minecraft 17w46a; Minecraft 17w47a; Minecraft 17w47b; Minecraft 17w48a; Minecraft 17w50a; Minecraft 18w21a; Minecraft 1.13-pre6; Minecraft 1.13; Minecraft 18w30b; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w45a; Minecraft 18w46a; 1.14.4; 19w34a; 19w37a; 19w39a; 19w42a; 19w46b
- **Fix versions:** 1.15 Pre-release 1
- **Labels:** explode; explosion; particle; smoke
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** 2015-12-07_16.51.49.png; 2015-12-07_16.53.32.png; 2015-12-07_16.53.34.png; 2015-12-07_16.53.47.png; 2015-12-07_16.53.49.png; TNT explosion.gif
- **Issue links:** Bonfire Testing:inward:MC-165991:TNT explosion no longer shows additional smoke particles since 1.15 Pre-release 1 | Duplicate:inward:MC-110431:T.N.T explosion particles not affected by the particles option | Duplicate:inward:MC-161781:when set to minimal particles tnt explosion particles still show | Blocks:inward:MC-165991:TNT explosion no longer shows additional smoke particles since 1.15 Pre-release 1

## Description

What I expected to happen was...:
After the explosion of TNT its particles will not appear.
What actually happened was...:
After the explosion, the particles appear and the game lags (on slow computers).
Steps to reproduce:
- Set the Particles option to "Minimum"

- Ignite TNT

## Comments (9)

### Comment 1: migrated (2015-12-06T23:55:27.579-0800)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: migrated (2015-12-07T02:38:41.527-0800)

Confirmed for 15w49b.

### Comment 3: migrated (2018-05-24T03:29:00.020-0700)

Affects 18w21a

### Comment 4: migrated (2018-08-27T08:46:35.771-0700)

Confirmed for 1.13.1.

### Comment 5: migrated (2019-11-20T09:51:49.755-0800)

Affect 19w46b.
Category should include "Performance".

### Comment 6: migrated (2019-11-21T11:28:34.103-0800)

No longer affects 1.15-pre1, where no explosion smoke particles show regardless of what the particles setting is on.

### Comment 7: migrated (2020-06-15T05:26:54.586-0700)

Can confirm fix; no smoke particles display after the explosion.

### Comment 8: [Mod] violine1101 (2020-07-01T07:59:44.197-0700)

This issue is currently blocked by .

### Comment 9: migrated (2021-10-18T06:59:00.817-0700)

This should be reopened when  gets fixed.
