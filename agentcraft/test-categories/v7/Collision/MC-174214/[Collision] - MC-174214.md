# MC-174214: Fireworks for crossbow go through an entity if it is close to a player

**Mojira URL:** [https://bugs.mojang.com/browse/MC-174214](https://bugs.mojang.com/browse/MC-174214)

## Report details

- **Mojira categories:** Collision; Projectiles
- **Project:** MC
- **Issue key:** MC-174214
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2020-03-08T07:27:13.978-0700
- **Updated:** 2025-04-26T09:29:31.566-0700
- **Resolution date:** 2024-09-12T06:19:59.277-0700
- **Affects versions:** 20w10a; 20w11a; 20w12a; 20w13b; 20w14a; 20w18a; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Release Candidate 1; 1.16.2 Release Candidate 2; 1.16.2; 1.16.3; 1.16.4 Pre-release 1; 1.16.4 Release Candidate 1; 1.16.4; 20w45a; 20w51a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w14a; 21w15a; 1.17 Pre-release 2; 1.17 Pre-release 5; 1.17 Release Candidate 1; 1.17; 1.17.1 Release Candidate 1; 1.17.1; 21w37a; 21w40a; 21w43a; 1.18 Pre-release 5; 1.18; 1.18.1 Release Candidate 1; 1.19; 1.19.1 Release Candidate 2; 1.19.1 Release Candidate 3; 1.19.1; 1.19.2 Release Candidate 1; 1.19.2; 22w42a; 1.19.3 Release Candidate 1; 1.19.3; 23w04a; 23w06a; 1.19.4 Release Candidate 1; 1.19.4 Release Candidate 3; 1.19.4; 23w16a; 23w17a; 23w18a; 1.20 Pre-release 1; 1.20 Pre-release 2; 1.20 Pre-release 4; 1.20 Pre-release 5; 1.20 Pre-release 6; 1.20 Pre-release 7; 1.20 Release Candidate 1; 1.20; 1.20.1 Release Candidate 1; 1.20.1; 23w31a; 23w32a; 23w33a; 23w35a; 1.20.2 Pre-release 2; 1.20.2 Release Candidate 1; 1.20.2; 23w40a; 23w41a; 23w42a; 23w43b; 23w44a; 23w45a; 23w46a; 1.20.3 Pre-Release 2; 1.20.3 Release Candidate 1; 1.20.4; 23w51b; 24w03b; 24w04a; 24w05b; 24w06a; 24w07a; 24w09a; 24w11a; 24w12a; 24w13a; 24w14a; 1.20.5 Pre-Release 1; 1.20.5 Pre-Release 3; 1.20.5 Release Candidate 2; 1.20.5; 1.20.6 Release Candidate 1; 1.20.6; 24w18a; 24w21b; 1.21 Pre-Release 2; 1.21 Pre-Release 4; 1.21; 1.21 Release Candidate 1; 1.21.1; 24w33a; 24w34a; 24w35a
- **Fix versions:** 24w37a
- **Area:** Gameplay
- **Watchers:** 1
- **Attachments:** 8
- **Attachment filenames:** 2020-03-08_22.26.36.png; 2020-03-08_22.26.38.png; 2022-06-09_11.51.46.png; 2022-06-09_11.51.58.png; 2022-06-09_16.09.24.png; 2024-09-12_21.18.10.png; 2024-09-12_21.19.00.png; MC-174214.mp4
- **Issue links:** Blocks:inward:MC-276480:Projectile no longer moves correctly when it is deflected | Relates:outward:MC-122335:Projectiles go through an entity if it is close to a player or a snow golem | Relates:inward:MC-268468:Fireballs and wind charges can be hit through solid blocks | Bonfire Testing:inward:MC-270181:Wind charges go through an entity if it is close to a player

## Description

The bug
Fireworks for crossbow go through an entity if it is close to a player.
How to reproduce
- /summon enderman ~ ~ ~ {NoAI:1b}

- go up very close to it

- Shoot an arrow using a crossbow
→  The arrow hits

- Shoot a fireworks rocket using a crossbow
→  The rocket passes right through the enderman.

- Shulker fixed in 1.19.

## Comments (16)

### Comment 1: migrated (2020-03-08T07:27:13.978-0700)

This comment contained multiple image attachments (8), please login to view the attachments.

### Comment 2: Avoma (2021-01-09T04:25:16.672-0800)

Can confirm in 20w51a.

### Comment 3: Avoma (2021-01-24T11:48:22.939-0800)

Can confirm in 21w03a.

### Comment 4: Avoma (2021-02-04T07:27:46.427-0800)

Can confirm in 21w05a.

### Comment 5: Avoma (2021-02-04T11:37:58.808-0800)

Can confirm in 21w05b.

### Comment 6: Avoma (2021-02-11T09:31:39.132-0800)

Can confirm in 21w06a.

### Comment 7: Avoma (2021-02-18T09:49:51.587-0800)

Can confirm in 21w07a.

### Comment 8: Avoma (2021-02-20T07:59:19.895-0800)

Video attached.

### Comment 9: Avoma (2021-04-11T10:19:43.519-0700)

Can confirm in 21w14a.

### Comment 10: Avoma (2021-04-17T07:18:27.114-0700)

Can confirm in 21w15a.

### Comment 11: Avoma (2021-06-14T02:20:33.886-0700)

Can confirm in 1.17.

### Comment 12: [Mod]Les3awe (2022-06-08T20:52:54.035-0700)

Fixed in 1.19.

### Comment 13: migrated (2022-06-09T00:30:17.700-0700)

A shulker hitbox is very different (entities can not walk through them), you sure this is fixed, and was not just not the case for shulkers?

### Comment 14: migrated (2022-06-09T01:14:21.077-0700)

That's what I thought.

### Comment 15: [Mod]Les3awe (2022-06-09T01:16:19.680-0700)

@, Confirmed to affect 1.19.
It's weird, I've been using shulkers to test this report before and it's reproducible very well, since the shulker hitbox is solid enough.

### Comment 16: [Mod]Les3awe (2024-09-12T06:19:59.275-0700)

Fixed in 24w37a along with MC-276480.
