# MC-302362: Clicking on "Singleplayer" or "Multiplayer" in the main menu then immediately clicking on a world or server joins it even when not clicking the play button

**Mojira URL:** [https://bugs.mojang.com/browse/MC-302362](https://bugs.mojang.com/browse/MC-302362)

## Report details

- **Mojira categories:** Input; UI
- **Project:** MC
- **Issue key:** MC-302362
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2025-09-28T14:02:39.483-0700
- **Updated:** 2026-03-11T03:45:18.335-0700
- **Resolution date:** 2025-10-22T01:52:25.585-0700
- **Affects versions:** 1.21.9 Release Candidate 1; 1.21.9
- **Fix versions:** 25w44a
- **Area:** Platform HC
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** MC-302362.mp4
- **Issue links:** Relates:outward:MC-301852:Placing a stack of items onto a slot and immediately shift-clicking it into a container moves all items of that type into the container | Relates:outward:MC-303393:Double-clicking to collect all items of the same kind at the mouse cursor is now overly sensitive

## Description

Entering the singleplayer or multiplayer menu and within 250 milliseconds clicking anywhere on a world or server (even if not on the play button on the world’s icon) causes the client to join that world or server. Since 250 milliseconds is the maximum possible time after a click when a second click can be performed for it to count as a double click, I assume the game thinks it’s a double click and joins the world or server just like when double-clicking it normally. This does not occur in 1.21.8.
How to reproduce:
- In the main menu, click on “Singleplayer” or “Multiplayer.”

- Within 250 milliseconds from the previous step, click somewhere on a world or server except on its play button.
→  The client joins the world or server.

Expected result:
Entering a different menu in the middle of a double click would prevent it from functioning as a double click.
Observed result:
Entering the singleplayer or multiplayer menu and immediately single-clicking on a world or server functions as a double click and joins the world or server.

## Comments (0)

No comments were available in the downloaded comment corpus.
