# MC-248758: Logged error: `Detected setBlock in a far chunk`

**Mojira URL:** [https://bugs.mojang.com/browse/MC-248758](https://bugs.mojang.com/browse/MC-248758)

## Report details

- **Mojira categories:** World generation
- **Project:** MC
- **Issue key:** MC-248758
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-02-22T08:50:03.053-0800
- **Updated:** 2026-05-05T07:18:27.371-0700
- **Resolution date:** 2026-05-05T00:24:13.013-0700
- **Affects versions:** 1.18.1; 1.18.2 Pre-release 2; 1.18.2 Pre-release 3; 1.18.2 Release Candidate 1; 1.18.2; 22w12a; 22w13a; 22w15a; 1.19 Release Candidate 1; 1.19; 1.19.1 Pre-release 5; 23w03a; 24w10a; 1.21 Pre-Release 2; 25w04a
- **Fix versions:** 26.2 Snapshot 6
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2022-02-22-7.log.gz; latest.log
- **Issue links:** Relates:inward:MC-232676:The count_multilayer decorator tries to place features in invalid positions

## Description

Create a world with this seed and you will immediately notice an error in the console.
8680357063582821254
Possibly related to  and MC-230004?

```
[19:46:29] [Worker-Main-17/ERROR]: Detected setBlock in a far chunk [-15, -2], pos: gi{x=-228, y=24, z=-32}, status: minecraft:features, currently generating: ResourceKey[minecraft:worldgen/placed_feature / minecraft:large_dripstone]
[19:46:29] [Worker-Main-17/ERROR]: Detected setBlock in a far chunk [-15, -2], pos: gi{x=-227, y=24, z=-32}, status: minecraft:features, currently generating: ResourceKey[minecraft:worldgen/placed_feature / minecraft:large_dripstone]
[19:46:29] [Worker-Main-17/ERROR]: Detected setBlock in a far chunk [-15, -2], pos: gi{x=-226, y=24, z=-32}, status: minecraft:features, currently generating: ResourceKey[minecraft:worldgen/placed_feature / minecraft:large_dripstone]
[19:46:29] [Worker-Main-17/ERROR]: Detected setBlock in a far chunk [-15, -2], pos: gi{x=-225, y=24, z=-32}, status: minecraft:features, currently generating: ResourceKey[minecraft:worldgen/placed_feature / minecraft:large_dripstone]
[19:46:29] [Worker-Main-17/ERROR]: Detected setBlock in a far chunk [-14, -2], pos: gi{x=-224, y=24, z=-32}, status: minecraft:features, currently generating: ResourceKey[minecraft:worldgen/placed_feature / minecraft:large_dripstone]
[19:46:29] [Worker-Main-17/ERROR]: Detected setBlock in a far chunk [-14, -2], pos: gi{x=-223, y=24, z=-32}, status: minecraft:features, currently generating: ResourceKey[minecraft:worldgen/placed_feature / minecraft:large_dripstone]
[19:46:29] [Worker-Main-17/ERROR]: Detected setBlock in a far chunk [-14, -2], pos: gi{x=-222, y=24, z=-32}, status: minecraft:features, currently generating: ResourceKey[minecraft:worldgen/placed_feature / minecraft:large_dripstone]
[19:46:29] [Worker-Main-17/ERROR]: Detected setBlock in a far chunk [-14, -2], pos: gi{x=-221, y=23, z=-32}, status: minecraft:features, currently generating: ResourceKey[minecraft:worldgen/placed_feature / minecraft:large_dripstone]
[19:46:29] [Worker-Main-17/ERROR]: Detected setBlock in a far chunk [-14, -2], pos: gi{x=-221, y=24, z=-32}, status: minecraft:features, currently generating: ResourceKey[minecraft:worldgen/placed_feature / minecraft:large_dripstone]
[19:46:29] [Worker-Main-17/ERROR]: Detected setBlock in a far chunk [-14, -2], pos: gi{x=-220, y=23, z=-32}, status: minecraft:features, currently generating: ResourceKey[minecraft:worldgen/placed_feature / minecraft:large_dripstone]
[19:46:30] [Worker-Main-17/ERROR]: Detected setBlock in a far chunk [-14, -2], pos: gi{x=-220, y=24, z=-32}, status: minecraft:features, currently generating: ResourceKey[minecraft:worldgen/placed_feature / minecraft:large_dripstone]
[19:46:30] [Worker-Main-17/ERROR]: Detected setBlock in a far chunk [-14, -2], pos: gi{x=-219, y=23, z=-32}, status: minecraft:features, currently generating: ResourceKey[minecraft:worldgen/placed_feature / minecraft:large_dripstone]
[19:46:30] [Worker-Main-17/ERROR]: Detected setBlock in a far chunk [-14, -2], pos: gi{x=-218, y=23, z=-32}, status: minecraft:features, currently generating: ResourceKey[minecraft:worldgen/placed_feature / minecraft:large_dripstone]
```

## Comments (13)

### Comment 1: migrated (2022-02-22T08:50:03.053-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: fullfungo (2022-02-22T18:05:22.724-0800)

Could not replicate in 1.18.1

### Comment 3: fullfungo (2022-02-22T18:05:50.109-0800)

Could not replicate in 1.18.2 Pre-release 2

### Comment 4: ampolive (2022-02-24T15:12:03.735-0800)

I was able to reproduce this issue.

### Comment 5: Lolo (2022-02-25T06:36:21.972-0800)

Affects version 1.18.2 RC-1

### Comment 6: Lolo (2022-02-28T06:59:40.942-0800)

Affects version 1.18.2

### Comment 7: Lolo (2022-03-26T04:20:18.846-0700)

This bug affects version 22w12a

### Comment 8: Lolo (2022-04-01T11:44:42.314-0700)

This bug affects version 22w13a

### Comment 9: Lolo (2022-04-17T13:19:41.460-0700)

This bug affects version 22w15a

### Comment 10: Lolo (2022-06-02T11:54:22.392-0700)

This bug affects version 1.19 rc 1

### Comment 11: Lolo (2022-07-16T06:04:27.881-0700)

This bug affects version 1.19.1 Pre-release 5

### Comment 12: clamlol (2024-03-06T11:50:30.336-0800)

Affects 24w10a.

```Seed: 5959569177826005615
Coordinates: /execute in minecraft:overworld run tp @s 2821 86 -848```

### Comment 13: J Z (2025-01-28T11:08:50.761-0800)

Affects 25w04a.
Seed: "44466836031555693"
Position: "/execute in minecraft:overworld run tp @s 215.55 -16.00 -903.53 -175.04 60.15"
