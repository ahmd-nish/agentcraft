# MC-3697: TNT submerged in water can destroy item frames, paintings, armor stands, and other similar entities

**Mojira URL:** [https://bugs.mojang.com/browse/MC-3697](https://bugs.mojang.com/browse/MC-3697)

## Report details

- **Mojira categories:** Entities
- **Project:** MC
- **Issue key:** MC-3697
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2012-11-22T07:39:37.860-0800
- **Updated:** 2025-05-29T09:20:39.599-0700
- **Resolution date:** 2024-09-14T06:21:16.400-0700
- **Affects versions:** Minecraft 1.4.5; Snapshot 12w50a; 1.15.2; 20w16a; 1.16 Pre-release 2; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Pre-release 2; 1.16.2 Pre-release 3; 1.16.2 Release Candidate 1; 1.16.2 Release Candidate 2; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4 Pre-release 1; 1.16.4 Pre-release 2; 1.16.4 Release Candidate 1; 1.16.4; 20w45a; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w07a; 21w08b; 21w10a; 21w11a; 21w13a; 21w14a; 21w15a; 21w17a; 21w20a; 1.17; 1.17.1 Release Candidate 1; 1.17.1; 21w39a; 21w40a; 21w42a; 1.18; 1.18.1; 22w05a; 1.18.2 Release Candidate 1; 1.18.2; 22w14a; 22w18a; 1.19; 1.19.1 Pre-release 5; 1.19.1; 1.19.2; 22w43a; 1.19.3; 1.19.4; 1.20; 1.20.1; 23w33a; 24w11a; 24w13a; 1.20.6; 1.21; 1.21.1
- **Fix versions:** 24w33a
- **Area:** Platform
- **Labels:** armor_stand; glow_item_frame; item_frame; leash_knot; painting; tnt
- **Watchers:** 2
- **Attachments:** 6
- **Attachment filenames:** 2012-11-22_10.38.01.png; 2012-11-22_10.38.07.png; 2012-11-22_10.39.20.png; 2024-08-14_03.08.23.png; MC-3697.mp4; setup.png
- **Issue links:** Relates:outward:MC-276700:Underwater explosions can still destroy vehicles | Relates:inward:MCPE-183527:TNT submerged in water can destroy armor stands, leash knots and paintings

## Description

The Bug:
TNT submerged in water can destroy item frames, paintings, armor stands, and other similar entities.
Steps to Reproduce:
- Build the setup as shown in the attachment below.

- Ignite the TNT and wait for it to explode.

- Take note as to whether or not TNT submerged in water can destroy item frames, paintings, armor stands, and other similar entities.

Observed Behavior:
TNT can destroy item frames, paintings, armor stands, and other similar entities.
Expected Behavior:
TNT would not be able to destroy item frames, paintings, armor stands, and other similar entities.

## Comments (23)

### Comment 1: migrated (2012-11-22T07:39:37.860-0800)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: migrated (2012-11-22T07:40:41.798-0800)

This is because item frames are NOT blocks. TNT in water only affects entities, which item frames and paintings are.

### Comment 3: migrated (2012-11-22T07:41:33.737-0800)

It will also have a chance to destroy the drops.
Technically the drops are also entities and can be damaged, hence throwing them into lava or a cactus destroys them. Explosions also can destroy drops.

### Comment 4: migrated (2012-12-18T06:14:02.915-0800)

This is not a bug.
Close this?

### Comment 5: migrated (2012-12-19T01:55:12.312-0800)

dont forget paintings and item frames are not blocks but entities so they get 'killed' by the TNT

### Comment 6: migrated (2020-04-01T00:46:38.067-0700)

Why is this reopened? Paintings and Item Frames are entities, so should be destroyed by TNT regardless of whether it's in water.

### Comment 7: Uriel Salischiker (2020-04-01T00:59:17.754-0700)

It has been reopened by Mojang

### Comment 8: migrated (2020-04-16T00:58:35.805-0700)

Confirmed in 20w16a

### Comment 9: migrated (2020-06-20T10:18:51.090-0700)

Affects 1.16 Release Candidate 1
Also happens with respawn anchors.

### Comment 10: Avoma (2020-11-25T11:43:30.292-0800)

Can confirm in 20w48a.

### Comment 11: migrated (2021-01-12T06:21:42.154-0800)

affects 20w51a, it never fixed, until its done yet.
its just an entity, not a block.

### Comment 12: Avoma (2021-01-17T10:37:45.883-0800)

Relates to MC-175250.

### Comment 13: Avoma (2021-01-22T03:03:11.894-0800)

Can confirm in 21w03a. Also affects armour stands.

### Comment 14: Avoma (2021-02-04T10:37:29.988-0800)

Can confirm in 21w05b.

### Comment 15: Avoma (2021-02-18T10:44:52.849-0800)

Can confirm in 21w07a. Video attached.

### Comment 16: Avoma (2021-04-19T01:39:05.151-0700)

Can confirm in 21w15a.

### Comment 17: Avoma (2021-04-30T06:00:50.530-0700)

Can confirm in 21w17a.

### Comment 18: ampolive (2021-06-07T10:22:13.355-0700)

Can confirm in 1.17 Release Candidate 2.

### Comment 19: migrated (2021-06-09T05:20:51.889-0700)

Affects 1.17

### Comment 20: ampolive (2021-07-02T17:08:05.636-0700)

Can confirm in 1.17.1 Release Candidate 1.

### Comment 21: Avoma (2021-10-03T02:51:28.895-0700)

Can confirm this in 21w39a. Here are some extra details regarding this problem.
The Bug:
TNT is able to destroy item frames, paintings, armor stands, and other entities, even when submerged in water.
Steps to Reproduce:
- Build the setup as shown in the attachment below.

- Ignite the TNT and wait for it to explode.

Observed Behavior:
TNT is able to destroy item frames, paintings, armor stands, and other entities, even when submerged in water.
Expected Behavior:
TNT would not be able to destroy item frames, paintings, armor stands, and other entities, when submerged in water.

### Comment 22: theGlotzerify (2022-02-10T17:28:05.105-0800)

can confirm in 1.18.1

### Comment 23: KR_ (2023-12-05T07:15:21.492-0800)

Can confirm in 1.20.3 rc-1
