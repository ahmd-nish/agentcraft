# MC-198007: Villages replace ice with path blocks instead of wood

**Mojira URL:** [https://bugs.mojang.com/browse/MC-198007](https://bugs.mojang.com/browse/MC-198007)

## Report details

- **Mojira categories:** Structures; Village system; World generation
- **Project:** MC
- **Issue key:** MC-198007
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2020-08-14T10:12:34.694-0700
- **Updated:** 2025-04-10T14:53:42.462-0700
- **Resolution date:** 2022-03-23T11:36:16.763-0700
- **Affects versions:** 1.16.2; 1.16.4; 20w51a; 21w03a; 21w05b
- **Fix versions:** 1.18 Pre-release 5
- **Labels:** village-generation
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2020-08-14_18.08.04.png; 2020-08-14_18.08.16.png; 2020-08-14_18.08.30.png; 2020-08-14_18.08.51.png
- **Issue links:** Relates:inward:MC-200492:Paths generated over shallow water do not replace the water with planks

## Description

As the ice is part of a water body, it'd be expected that it be replaced with wood, as is done for water. This does not happen, however, and the ice is just treated as any other terrain block, resulting in illogical path blocks.
How to reproduce

```
Seed: -7882263134696652088
Coordinates: /execute in minecraft:overworld run tp @s -135.95 63.00 -303308.65 -178.50 22.50
```

## Comments (5)

### Comment 1: migrated (2020-08-14T10:12:34.694-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: markderickson (2020-08-14T14:15:53.274-0700)

Hi there!
I can confirm for release 1.16.2.

### Comment 3: Avoma (2020-12-24T09:51:19.036-0800)

Can confirm in 20w51a.

### Comment 4: Avoma (2021-01-25T11:14:11.842-0800)

Can confirm in 21w03a.

### Comment 5: Avoma (2021-02-05T07:26:40.395-0800)

Can confirm in 21w05b.
