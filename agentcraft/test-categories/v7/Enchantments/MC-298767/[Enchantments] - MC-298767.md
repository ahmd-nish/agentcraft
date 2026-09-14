# MC-298767: Piercing arrows phase through mobs that are in the same block

**Mojira URL:** [https://bugs.mojang.com/browse/MC-298767](https://bugs.mojang.com/browse/MC-298767)

## Report details

- **Mojira categories:** Combat; Enchantments; Projectiles
- **Project:** MC
- **Issue key:** MC-298767
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2025-06-15T02:11:16.850-0700
- **Updated:** 2025-10-09T01:04:37.469-0700
- **Resolution date:** 2025-10-09T01:04:37.432-0700
- **Affects versions:** 1.21.5; 1.21.6 Release Candidate 1; 1.21.6; 1.21.7 Release Candidate 1; 1.21.8; 25w35a
- **Fix versions:** 25w41a
- **Area:** Platform
- **Votes:** 4
- **Watchers:** 2
- **Attachments:** 2
- **Attachment filenames:** 1.mp4; Minecraft 2025.06.15 - 11.02.06.29.mp4
- **Issue links:** Duplicate:inward:MC-301020:Piercing arrows do not pierce as expected at level IV when hit entities are on the same block

## Description

steps to reproduce:
1) pick any 2 mobs with the same hitbox size
2) put them both in a 1x1 hole
3) get them to half a heart
4) shoot them with a piercing crossbow

expected result:
both mobs die

actual result:
only one of the mobs dies

## Comments (3)

### Comment 1: Rounduction (2025-06-15T02:11:17.515-0700)

This comment contained multiple media attachments (2), please login to view the attachments.

### Comment 2: AA64 (2025-06-15T03:14:48.812-0700)

I can confirm it.

### Comment 3: Benats (2025-06-17T12:56:25.435-0700)

It also works on 1.21.6
