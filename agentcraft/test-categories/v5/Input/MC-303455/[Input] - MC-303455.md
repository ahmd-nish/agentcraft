# MC-303455: The cursor is no longer centered when opening a container or menu on Wayland

**Mojira URL:** [https://bugs.mojang.com/browse/MC-303455](https://bugs.mojang.com/browse/MC-303455)

## Report details

- **Mojira categories:** Input; UI
- **Project:** MC
- **Issue key:** MC-303455
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2025-10-21T11:50:07.386-0700
- **Updated:** 2026-03-27T01:42:50.154-0700
- **Resolution date:** 2025-10-28T02:44:06.045-0700
- **Affects versions:** 25w43a
- **Fix versions:** 25w44a
- **Area:** Platform HC
- **Votes:** 4
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** image-20251021-190758.png

## Description

As of snapshot 25w43a, Minecraft now runs on Wayland natively instead of XWayland on Linux. This comes with unfortunate side effects. One is the cursor no longer being centered when opening a container or menu.

Steps to reproduce the issue
1. Make sure you are using Wayland and not X11
2. Launch snapshot 25w43a
3. Join a world and open the inventory, any other container or press ESC to open the pause menu
4. Move around the cursor and close the menu or container
5. Reopen the menu or container

Expected result
The cursor will always center like it did prior 25w43a.

Actual result
The cursor does not center.

## Comments (7)

### Comment 1: tryashtar (2025-10-21T11:55:35.813-0700)

Confirmed, thanks for reporting. I’m curious, did you also have issues where the game icon is invisible and the cursor looks different inside the window?

### Comment 2: shrobbyy (2025-10-21T12:07:03.373-0700)

@tryashtar Yeah, I do. I will make separate reports for that.

### Comment 3: muzikbike (2025-10-21T12:08:02.492-0700)

There appear to be associated errors:

### Comment 4: jjlr (2025-10-22T16:54:32.406-0700)

Also happening on Fedora 42 running Gnome 48.

### Comment 5: Arvixion (2025-10-25T12:02:29.988-0700)

Also confirmed for fedora

### Comment 6: tryashtar (2026-02-17T12:54:47.505-0800)

25w44a removed wayland support. 26.1-snapshot-8 re-added it behind the PREFER_WAYLAND debug property. This seems to be fixed when using that mode.

### Comment 7: bai (2026-03-27T01:42:50.154-0700)

and now they removed again in 26.1-8
