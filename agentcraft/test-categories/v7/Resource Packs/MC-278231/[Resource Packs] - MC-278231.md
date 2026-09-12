# MC-278231: Space characters at the end of a line in book and quill are invisible even if given a texture

**Mojira URL:** [https://bugs.mojang.com/browse/MC-278231](https://bugs.mojang.com/browse/MC-278231)

## Report details

- **Mojira categories:** Resource Packs; UI
- **Project:** MC
- **Issue key:** MC-278231
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2024-11-09T10:03:25.898-0800
- **Updated:** 2025-05-04T13:32:17.786-0700
- **Resolution date:** 2025-05-04T13:32:17.761-0700
- **Affects versions:** 24w45a
- **Fix versions:** 25w18a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 9
- **Attachment filenames:** 2024-11-09_18.00.47.png; 2024-11-09_18.00.51.png; 2024-11-09_18.01.03.png; 2024-11-09_18.01.06.png; 2024-11-09_18.01.26.png; 2024-11-09_18.01.27.png; 2025-05-04_15.57.10-20250504-065710.png; 2025-05-04_15.59.43-20250504-065943.png; space-distinguisher-24w45a-v1.0.zip

## Description

Discovered while testing .
The bug
If space characters are given a visual appearance, and typed into a book and quill, any that are at the end of a line will be completely invisible.
How to reproduce
- Download and apply the attached resource pack

- Type something followed by a space

Expected results
The space would be visible.
Actual results
It is in chat or on a sign, but not in a book.

## Comments (4)

### Comment 1: migrated (2024-11-09T10:03:25.898-0800)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: BugTracker_ (2024-11-09T10:34:34.891-0800)

Can confirm.

### Comment 3: apple502j (2025-05-03T23:56:52.466-0700)

Can no longer reproduce in 25w18a. Will check if this is the fix version.

### Comment 4: apple502j (2025-05-04T00:03:19.450-0700)

Fix version is indeed 25w18a.
