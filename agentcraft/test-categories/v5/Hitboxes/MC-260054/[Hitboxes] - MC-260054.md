# MC-260054: Pink Petals hitbox does not adjust to contents

**Mojira URL:** [https://bugs.mojang.com/browse/MC-260054](https://bugs.mojang.com/browse/MC-260054)

## Report details

- **Mojira categories:** Hitboxes
- **Project:** MC
- **Issue key:** MC-260054
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2023-02-15T08:51:57.169-0800
- **Updated:** 2025-04-30T03:51:09.441-0700
- **Resolution date:** 2023-08-02T08:42:10.930-0700
- **Affects versions:** 23w07a; 23w13a
- **Fix versions:** 23w31a
- **Area:** Expansion A
- **Watchers:** 1
- **Attachments:** 8
- **Attachment filenames:** 2023-02-15_16.46.57.png; 2023-02-15_16.46.58.png; 2023-02-15_16.47.08.png; 2023-02-15_16.47.09.png; 2023-02-15_16.47.54.png; 2023-02-15_16.47.55.png; 2023-02-15_16.48.07.png; 2023-02-15_16.48.08.png
- **Issue links:** Relates:outward:MC-264549:Pink petals with flower_amount 3 have inconsistent hitbox

## Description

The bug
23w07a introduces pink petals, a block which can have up to four instances of itself placed in a single block space. This puts it in a family also inhabited by turtle eggs, sea pickles and candles.
Turtle eggs, sea pickles and candles start out with a small hitbox when they contain one instance, and this hitbox expands dynamically to accommodate an increased number of units within. However, for the pink petals block, this hitbox will remain constant regardless of how many are inside of it.
How to reproduce
- Place one turtle egg

- Place a second turtle egg in that block space

- Place one sea pickle

- Place a second sea pickle in that block space

- Place one candle

- Place a second candle in that block space

- Place one pink petals

- Place a second pink petals in that block space

Expected results
When the second instance is added, each of the blocks would change their hitbox.
Actual results
This is true of the first three, but not of the fourth.

## Comments (2)

### Comment 1: migrated (2023-02-15T08:51:57.169-0800)

This comment contained multiple image attachments (8), please login to view the attachments.

### Comment 2: bodakugga (2023-02-15T13:50:51.268-0800)

Can confirm.
