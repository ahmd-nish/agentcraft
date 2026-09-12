# MC-279570: Some piston operations don't send neighbor updates

**Mojira URL:** [https://bugs.mojang.com/browse/MC-279570](https://bugs.mojang.com/browse/MC-279570)

## Report details

- **Mojira categories:** Redstone
- **Project:** MC
- **Issue key:** MC-279570
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2025-01-16T06:10:51.661-0800
- **Updated:** 2025-04-10T15:04:36.857-0700
- **Resolution date:** 2025-01-22T03:00:42.035-0800
- **Affects versions:** 25w03a
- **Fix versions:** 25w04a
- **Area:** Expansion A
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** missing_neighbor_updates_on_piston_breaking_lever.mp4
- **Issue links:** Relates:inward:MC-279326:Lit observers no longer send block updates when moved by a piston

## Description

After the fix of , some piston operations still don't cause neighbor updates, as they used to before 25w02a. This means many redstone contraptions containing piston blocks may break.
Steps to reproduce:
Follow the visual instructions in the attached video.
The redstone dust is supposed to depower after the lever is destroyed by the piston.
Code analysis and proposed solution:
This issue still persists because the observer subissue() seems to have been fixed by allowing the UPDATE_MOVE_BY_PISTON flag, in alternative to UPDATE_NEIGHBORS, to also cause calling BlockStateBase#affectNeighborsAfterRemoval, but two of the different combinations of flags in PistonBaseBlock#moveBlocks don't contain the UPDATE_MOVE_BY_PISTON flag, thus causing the general issue of missing updates to partly persist.
I would encourage fixing this by removing the UPDATE_MOVE_BY_PISTON flag check in LevelChunk#setBlockState and instead adding the UPDATE_NEIGHBORS flag (either in-place or an intermediate method) to any place UPDATE_MOVE_BY_PISTON is used and a neighbor update is expected, and to all the combinations of flags in PistonBaseBlock#moveBlocks, except the UPDATE_NONE | UPDATE_KNOWN_SHAPE combination (that one would actually negatively impact the current behavior if modified because sticky pistons pulling a block are not supposed to cause a neighbor update on retraction).

## Comments (1)

### Comment 1: migrated (2025-01-16T06:10:51.661-0800)

This comment contained an image attachment, please login to view the attachment.
