# MC-183784: Visual bug to the Game Mode Switcher debug menu after resizing the window

**Mojira URL:** [https://bugs.mojang.com/browse/MC-183784](https://bugs.mojang.com/browse/MC-183784)

## Report details

- **Mojira categories:** Debug
- **Project:** MC
- **Issue key:** MC-183784
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2020-05-13T09:49:41.136-0700
- **Updated:** 2025-08-07T04:30:11.171-0700
- **Resolution date:** 2025-08-07T04:30:11.102-0700
- **Affects versions:** 20w20a; 1.16.1; 20w30a; 1.16.4 Pre-release 2; 1.16.4; 20w46a; 20w49a; 20w51a; 21w03a; 1.17.1; 21w42a; 1.18.1; 1.18.2; 22w13a; 1.19; 1.19.2; 1.19.4; 23w12a; 1.20.1; 1.20.6; 24w19b; 1.21.4; 1.21.5
- **Fix versions:** 25w33a
- **Area:** Platform
- **Labels:** game-mode-switcher
- **Watchers:** 2
- **Attachments:** 4
- **Attachment filenames:** 2020-05-13_18.42.41.png; MC-183784.mp4; MC-183784.png; MC-183784 - Analysis.png
- **Issue links:** Duplicate:inward:MC-293763:F3+F4 Visual Glitch | Duplicate:inward:MC-267876:Glitchy gamemode switcher ui | Duplicate:inward:MC-261319:Gamemode Switcher icons duplicate upon toggling fullscreen | Duplicate:inward:MC-195807:Visual duplication glitch-gamemode switcher icons | Duplicate:inward:MC-297958:Gamemode Switcher // Rendering Issue

## Description

The Bug
When changing the window size while the menu is open, the icons appear glitched out
Steps to Reproduce
-     Bring up the gamemode switcher menu. (Hold F3 and press F4).

-     Whilst still having this menu open, resize your game window.

-     Take note as to whether or not gamemode switcher icons are duplicated after resizing your game window.

Observed Behavior
Gamemode switcher icons are duplicated after resizing your game window.
Expected Behavior
Gamemode switcher icons would not be duplicated after resizing your game window.

## Comments (13)

### Comment 1: migrated (2020-05-13T09:49:41.136-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: [MOD] Greymagic27 (2020-05-13T09:58:45.105-0700)

Looks like

### Comment 3: migrated (2020-05-13T10:01:00.590-0700)

It's not the same. My report was when you change gamemodes this way you need to press F3 twice to use the debug screen.

### Comment 4: [MOD] Greymagic27 (2020-05-13T10:23:08.528-0700)

That tells me for not reading the reports properly! I've reopened this now.

### Comment 5: Avoma (2021-01-19T05:37:46.199-0800)

Can confirm in 20w51a.

### Comment 6: Avoma (2021-01-26T03:22:02.133-0800)

Can confirm in 21w03a.

### Comment 7: Avoma (2021-07-16T04:07:34.255-0700)

Can confirm in 1.17.1.

### Comment 8: Avoma (2021-10-25T03:59:04.320-0700)

Can confirm this behavior in 21w42a. Here are some extra details regarding this problem.
The Bug:
Gamemode switcher icons are duplicated after resizing your game window.
Steps to Reproduce:
- Bring up the gamemode switcher menu. (Hold F3 and press F4).

- Whilst still having this menu open, resize your game window.

- Take note as to whether or not gamemode switcher icons are duplicated after resizing your game window.

Observed Behavior:
Gamemode switcher icons are duplicated after resizing your game window.
Expected Behavior:
Gamemode switcher icons would not be duplicated after resizing your game window.

### Comment 9: Avoma (2021-12-19T07:43:29.338-0800)

Can confirm in 1.18.1.

### Comment 10: Avoma (2022-04-05T12:05:23.301-0700)

Can confirm in 1.18.2 and 22w13a.

### Comment 11: Avoma (2022-07-26T10:41:59.964-0700)

Can confirm in 1.19.

### Comment 12: Avoma (2022-09-29T06:09:40.588-0700)

Can confirm in 1.19.2.

### Comment 13: MincraftEinstein (2023-10-03T16:49:33.108-0700)

Can confirm it's still here in 1.20.2
