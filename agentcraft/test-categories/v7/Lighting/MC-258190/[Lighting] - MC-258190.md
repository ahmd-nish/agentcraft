# MC-258190: Bubble columns let skylight through

**Mojira URL:** [https://bugs.mojang.com/browse/MC-258190](https://bugs.mojang.com/browse/MC-258190)

## Report details

- **Mojira categories:** Lighting
- **Project:** MC
- **Issue key:** MC-258190
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2022-11-29T00:32:43.546-0800
- **Updated:** 2025-04-30T06:07:15.099-0700
- **Resolution date:** 2022-12-02T14:01:20.640-0800
- **Affects versions:** 1.19.3 Pre-release 2; 1.19.3 Pre-release 3
- **Fix versions:** 1.19.3 Release Candidate 1
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 7
- **Attachment filenames:** Inked20221129154039188.jpg; Inked20221129154134576-1.jpg; Inked20221129154813121-1.jpg; Inked20221130080126236.jpg; Inked20221130083043694.jpg; Inked20221130083457062.jpg; MC-258190 - Version Behavior Comparison.png
- **Issue links:** Relates:inward:MC-258257:Bubble columns retain their light levels from the sky after upgrading old worlds

## Description

The Bug
A soul sand under the water is glowing in the daytime if there is no block above it.(Please look at the photo below.)

Steps to Reproduce
Put a soul sand under the water, if the bubble can flow up to the surface, it is glowing.

## Comments (13)

### Comment 1: migrated (2022-11-29T00:32:43.546-0800)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: [Mod] violine1101 (2022-11-29T01:30:56.627-0800)

Huh, interesting – probably water columns let more light through than water itself. Does this also apply to magma bubble columns?

### Comment 3: ampolive (2022-11-29T03:11:34.961-0800)

Confirmed. This also affects magma bubble columns.

### Comment 4: bcdbdeve (2022-11-29T06:09:52.795-0800)

Yes.The skylight is higher near the bubble columns .And it was not fixed in 1.19.3 pre3.(Look at the newest pictures.)However,it is not always appear in this verion.

### Comment 5: bcdbdeve (2022-11-29T19:18:56.207-0800)

1.19.3 pre1,22w46a~22w42a also have this bug.(Although I didn't try 22w43a~22w45a, I think all of these verions have this bug,because 22w42a has this bug,.)But 1.19.2 doesn't.

### Comment 6: Tinsel (2022-12-01T11:56:03.976-0800)

According to slicedlime's video this is not fixed

### Comment 7: Avoma (2022-12-01T13:19:35.445-0800)

Huh; that's rather bizarre. In my testing, this appears to be correctly fixed in 1.19.3 Release Candidate 1.

### Comment 8: ampolive (2022-12-01T13:58:46.314-0800)

This also appears to be correctly fixed in my testings.

### Comment 9: [Mod] violine1101 (2022-12-01T14:19:28.030-0800)

The way slicedlime's videos are made is that the world is first setup in the older snapshot, and then upgraded to the newer one. Since light levels are part of the save data, old bubble columns from 1.19.3-pre3 will still have skylight in 1.19.3-rc1 until a block update. That's probably why it didn't show up as properly fixed in slicedlime's video.

### Comment 10: slicedlime (2022-12-02T00:42:07.800-0800)

The video was made by upgrading the world, blocking the bubble column at the bottom (placing a block above the soul sand) and then removing the block again. So just updating the blocks definitely was not sufficient to eliminate the bug.

### Comment 11: Avoma (2022-12-02T01:07:05.798-0800)

Ahh, I see; that's super interesting... Should we reopen this ticket then to mention this new information and that the problem here isn't fully fixed?

### Comment 12: [Mod] violine1101 (2022-12-02T08:07:09.185-0800)

I feel like a new ticket would probably be more appropriate than reusing this one.

### Comment 13: Avoma (2022-12-02T10:41:12.279-0800)

No worries; I've created a new ticket regarding the problem that remains here which can be found at .
