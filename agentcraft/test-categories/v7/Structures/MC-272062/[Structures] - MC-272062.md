# MC-272062: Dimension padding doesn't affect the start piece

**Mojira URL:** [https://bugs.mojang.com/browse/MC-272062](https://bugs.mojang.com/browse/MC-272062)

## Report details

- **Mojira categories:** Structures
- **Project:** MC
- **Issue key:** MC-272062
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-05-15T19:12:45.111-0700
- **Updated:** 2025-05-29T09:06:21.466-0700
- **Resolution date:** 2024-10-30T01:31:39.281-0700
- **Affects versions:** 24w20a; 1.21 Pre-Release 2; 1.21 Pre-Release 3; 1.21; 1.21 Release Candidate 1
- **Fix versions:** 24w44a
- **Area:** Expansion B
- **Watchers:** 2
- **Attachments:** 2
- **Attachment filenames:** dimension_padding_bug_report.zip; image-2024-05-15-19-11-51-257.png

## Description

Dimension padding doesn't affect the starting piece. However, it affects every child piece, causing some strange generation.
Steps to Reproduce
- Download the attached datapack. It modifies the plains village structure file to have a dimension padding of 158.

- Add the datapack to a world and create the world.

- Locate and teleport to the nearest plains village. You may need to teleport a few times to find one that starts below y94.

Expected Result
The village won't place at all when the padding doesn't allow it to.
Actual Result
The center piece of the village places, but nothing else.

## Comments (4)

### Comment 1: migrated (2024-05-15T19:12:45.111-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: BugTracker_ (2024-05-15T23:27:10.007-0700)

Can confirm.

### Comment 3: kohara (2024-05-30T12:27:01.089-0700)

can confirm in 1.21-pre1
probably also affects every version from 24w20a to the pre-release

### Comment 4: kohara (2024-06-13T05:35:28.478-0700)

can confirm in 1.21-rc1
