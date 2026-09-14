# MC-306812: Inventories with no text fields cause key binds to conflict with IME input methods

**Mojira URL:** [https://bugs.mojang.com/browse/MC-306812](https://bugs.mojang.com/browse/MC-306812)

## Report details

- **Mojira categories:** Accessibility; Input; Internationalisation
- **Project:** MC
- **Issue key:** MC-306812
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2026-03-11T10:00:04.045-0700
- **Updated:** 2026-03-16T05:47:06.344-0700
- **Resolution date:** 2026-03-13T05:35:40.327-0700
- **Affects versions:** 26.1 Pre-Release 1
- **Fix versions:** 26.1 Pre-Release 2
- **Area:** Platform HC
- **Votes:** 1
- **Watchers:** 2
- **Attachments:** 3
- **Attachment filenames:** 屏幕截图 2026-03-12 001045.png; 屏幕截图 2026-03-12 001139.png; 屏幕截图 2026-03-12 001300.png

## Description

The intended goal for 26.1-snapshot-10 was: “If there are no screens open, IME input will be canceled”. Players should be able to hold W, A, S, D, Left Shift, Q, E, and other keys to move or control the game without being affected by the input method. However, once a GUI is opened, the situation becomes uncontrollable.
When I enter a Survival world and open my inventory, a chest, or any other GUI that does not require text input, I can still press Shift to switch the input method between Chinese and English.
Once switched to Chinese input mode, I am able to type Chinese in the GUI, which means I cannot or struggle to perform the following actions in the GUI:
- Press E to close the open GUI

- Press Q to drop the selected item

- Press Ctrl + Q to drop the entire stack

- Press F to swap items with the offhand

- Press 1–9 to move the hovered item to the corresponding hotbar slot or swap positions

These functions only work properly if I press Shift again to switch back to English input mode.
Holding Shift and clicking an item in the GUI quickly moves it from the inventory to the hotbar—a common vanilla mechanic. Unfortunately, this also causes players to accidentally trigger the Shift key to switch input languages, breaking the actions described above.
I am using Microsoft Pinyin, the default Chinese input method for Windows, which by default uses Shift to toggle between Chinese and English modes.
I believe a key part of the problem is that GUIs like the inventory or chest do not have text focus, yet text input is still possible. As a result, the intended goal for 26.1-snapshot-10 — “IME will be opened when a text input gains focus and closed when a text input loses focus” — has also failed.

## Comments (1)

### Comment 1: Automation for Jira (2026-03-11T10:00:11.812-0700)

Thank you for helping us improve Minecraft! We saved your files:
