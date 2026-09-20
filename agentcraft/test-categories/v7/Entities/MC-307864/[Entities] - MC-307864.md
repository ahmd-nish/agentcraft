# MC-307864: Small sulfur cubes become large client-side when fed a slimeball after restarting their aging

**Mojira URL:** [https://bugs.mojang.com/browse/MC-307864](https://bugs.mojang.com/browse/MC-307864)

## Report details

- **Mojira categories:** Entities; Mob behaviour
- **Project:** MC
- **Issue key:** MC-307864
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2026-05-01T20:58:48.303-0700
- **Updated:** 2026-05-04T03:42:59.195-0700
- **Resolution date:** 2026-05-04T03:42:59.132-0700
- **Affects versions:** 26.2 Snapshot 1; 26.2 Snapshot 5
- **Fix versions:** 26.2 Snapshot 6
- **Area:** Expansion A
- **Votes:** 1
- **Watchers:** 0
- **Attachments:** 0

## Description

The bug
A desync occurs when restarting the aging of a small sulfur cube and feeding it a slimeball afterward.
Steps to reproduce
- Summon a small sulfur cube.

- Feed it two golden dandelions to stop and restart its aging.

- Feed it a slimeball.

Observed behavior
The sulfur cube will appear large. However, it will still be able to be fed golden dandelions, and when given a block client-side, it will still take damage. When reloaded, it will be small again.
Expected behavior
The sulfur cube would resemble its actual age.

What’s more
In creative mode,if you put the sulfur cube in a bucket, then press E twice to open and close inventory, then you can pour it out successfully, and no activity can make it young again.

## Comments (4)

### Comment 1: Happy Strawberry (2026-05-01T23:43:24.725-0700)

Sometimes, I try to put it into a bucket, and then put it into a chest, and it doesn’t disappear. But I only do it successfully in creative mode, and it doesn’t work every time. I don’t know why.

### Comment 2: Tematiaus (2026-05-01T23:54:49.735-0700)

That is weird

### Comment 3: Happy Strawberry (2026-05-02T01:49:11.324-0700)

I did that (put it into a bucket, and then put it into a chest, and it doesn’t disappear) again, and when I pour the sulfur cube out, It becomes a normal big one, and it doesn’t become small. So that means it “grows up”. How strange!

### Comment 4: Happy Strawberry (2026-05-02T03:58:30.805-0700)

Put it into a bucket, and then press E twice, and I can also pour it out successfully.
