# MC-256485: Camels that spawn within villages can spawn inside blocks

**Mojira URL:** [https://bugs.mojang.com/browse/MC-256485](https://bugs.mojang.com/browse/MC-256485)

## Report details

- **Mojira categories:** Mob spawning; Structures
- **Project:** MC
- **Issue key:** MC-256485
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-10-19T06:52:17.790-0700
- **Updated:** 2025-04-30T04:18:44.808-0700
- **Resolution date:** 2023-06-08T01:51:24.479-0700
- **Affects versions:** 22w42a; 22w43a; 22w44a; 1.19.3; 23w03a; 23w04a; 23w05a; 1.19.4 Pre-release 4; 1.19.4; 23w12a; 23w13a; 23w14a; 23w16a; 23w17a; 23w18a; 1.20 Pre-release 2; 1.20 Pre-release 6; 1.20 Release Candidate 1; 1.20
- **Fix versions:** 23w31a
- **Area:** Expansion A
- **Labels:** camel
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2022-10-19_09.41.48.png; MC-256485.png
- **Issue links:** Relates:inward:MC-253396:Iron golems and cats that spawn within villages can spawn inside of trees

## Description

The Bug:
Camels that spawn within villages can spawn inside blocks.
In some cases, this can cause the camels to take suffocation damage and potentially die.
Here is an example:
Version: 1.19.3

```
Seed: -381051283335009767
Coordinates: /execute in minecraft:overworld run tp @s -446.99 72.00 2502.34 -23.39 6.11
```
Steps to Reproduce:
- Generate a world with the seed provided above and teleport to the given coordinates.

- Look closely at the camel and the blocks around it.

- Take note as to whether or not camels that spawn within villages can spawn inside blocks.

Observed Behavior:
Camels can spawn inside blocks.
Expected Behavior:
Camels would not be able to spawn inside blocks.

## Comments (13)

### Comment 1: migrated (2022-10-19T06:52:17.790-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: ampolive (2022-10-19T06:55:25.334-0700)

Could you please provide coordinates and seed?

### Comment 3: Tinsel (2022-12-07T20:31:34.902-0800)

In 1.19.3

### Comment 4: Tinsel (2023-01-19T14:49:41.513-0800)

Can confirm for 23w03a.
Here's another seed for the newest version: 158672035778931320
Spawn has a desert village, though the camel may walk out of the well before you can see it. Here's coords to a different one that puts you right in front of the fountain, where you can see the camel spawned inside of the blocks: -1375/ 63/ 648

### Comment 5: Tinsel (2023-01-25T11:25:02.196-0800)

In 23w04a

### Comment 6: Tinsel (2023-02-01T20:25:59.581-0800)

Can confirm for 23w05a

### Comment 7: Tinsel (2023-03-26T13:58:55.094-0700)

In 1.19.4 and 23w12a

### Comment 8: Tinsel (2023-03-29T13:02:27.001-0700)

In 23w13a

### Comment 9: Tinsel (2023-04-05T11:21:19.562-0700)

In 22w14a

### Comment 10: Tinsel (2023-04-21T19:45:18.504-0700)

In 23w16a

### Comment 11: Tinsel (2023-04-26T21:47:51.906-0700)

In 23w17a

### Comment 12: Tinsel (2023-05-03T15:26:42.707-0700)

Still in 23w18a

### Comment 13: Brevort (2023-05-31T08:10:57.559-0700)

Affects 1.20 rc 1. Can cause them to immediately suffocate upon the generation of the village.
