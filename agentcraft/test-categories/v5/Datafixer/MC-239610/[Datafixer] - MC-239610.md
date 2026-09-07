# MC-239610: Severe world corruption due to 1.18 snapshots failing to deserialize chunks that 1.17 loads fine

**Mojira URL:** [https://bugs.mojang.com/browse/MC-239610](https://bugs.mojang.com/browse/MC-239610)

## Report details

- **Mojira categories:** Datafixer
- **Project:** MC
- **Issue key:** MC-239610
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2021-10-22T12:39:59.195-0700
- **Updated:** 2025-04-29T21:22:09.017-0700
- **Resolution date:** 2021-11-18T09:46:49.025-0800
- **Affects versions:** 21w42a; 21w43a; 21w44a; 1.18 Pre-release 1
- **Fix versions:** 1.18 Pre-release 3
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** 2021-10-16_20.55.34.png; 2021-10-29_19.40.11.png; 2021-11-11_17.45.32.png; 2021-11-11_17.51.00.png; latestLogExcerpt.log; Palette_Data size mismatch dfu.zip
- **Issue links:** Duplicate:inward:MC-240512:Old chunks replaced with new ones

## Description

The bug
The core of the problem is that Minecraft 1.18 snapshots do not accept all save formats that were previously accepted. Minecraft 1.17 handled chunk sections with a mismatched palette size (e.g. 14 entries -> 4 bits per block) and data size (342 longs -> 12 blocks per long -> 5 bits per block) properly. It calculated the bits per block from the data size, and therefore was able to read the block data correctly.
The expected data size is calculated from the required bits per block which is calculated from the palette size. If the data size does not match the expected value 1.18 will throw an exception and generate a new chunk instead. Minecraft 1.17 snapshots handle this mismatch without any issue.
I haven't checked whether vanilla ever created chunks with this exact format in the past. But I have to assume that the code handling the mismatched size case existed for a reason. I hope you can look up that reason in your version control system (PalettedContainer, deserialization of the NBT, at the end). The code existed since at least minecraft 1.14.4.
For example the optimization mod lithium-fabric relied on chunk sections with this format being loaded properly and created lots of chunk sections with this format. This will lead to world corruption when hundreds of thousands of users upgrade their worlds to 1.18 (snapshots).
I attached a world that I created with the optimization mod lithium that includes lots of chunk sections with a size mismatch (data larger than palette requires). This world loads fine in vanilla 1.17. It breaks in the current 1.18 snapshots, cf. screenshots. As said before, it is possible that previous minecraft vanilla versions also created chunk sections with this save format, which is no longer accepted by 1.18.
How to reproduce
- Download the attached world

-  and save two copies in the saves folder

- Load one copy in 1.17.1
 Notice that the world looks normal, all chunks loaded fine

- Load the second copy in the latest 1.18 snapshot
 Notice that some chunks are corrupted (have regenerated), there are errors in the log (example as attachment)

Fixes
As a fix I suggest to:
add a datafixer that fixes the size mismatch (rewrite data to match the palette's required bit resolution, similar to 1.17 loading code.
or reintroduce the code that handles this case when deserializing chunk sections.
Regarding the screenshots:
The corruptions do not look severe here, but it will replace player bases with new chunks!

## Comments (4)

### Comment 1: migrated (2021-10-22T12:39:59.195-0700)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: migrated (2021-11-07T05:35:56.550-0800)

lmao

### Comment 3: migrated (2021-11-11T09:54:21.320-0800)

Just added two other photos to show more of what is happening, the ocean also is generating like this

### Comment 4: 2No2Name (2021-11-11T10:07:19.758-0800)

Due to the latest terrain blending features, the issue is visually harder to see (unless cutting through a player base). Looking at the log and then checking those chunks for cut off trees and cut off caves reliably shows that this bug is not fixed.
