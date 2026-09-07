# MC-228486: Cannot switch to other windows using Cmd+Tab on macOS

**Mojira URL:** [https://bugs.mojang.com/browse/MC-228486](https://bugs.mojang.com/browse/MC-228486)

## Report details

- **Mojira categories:** Input
- **Project:** MC
- **Issue key:** MC-228486
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2021-06-10T21:20:15.188-0700
- **Updated:** 2025-04-16T13:02:24.414-0700
- **Resolution date:** 2024-02-01T13:20:35.905-0800
- **Affects versions:** 1.17 Pre-release 1; 1.17; 1.17.1 Pre-release 1
- **Fix versions:** 24w05b
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** MC-228486.mp4
- **Issue links:** Duplicate:inward:MC-226855:Cannot Tab Out of Minecraft in Latest Pre-Release | Duplicate:inward:MC-228977:Can't command-tab in MacOS | Duplicate:inward:MC-229815:On MacOS, 1.17 cannot go to background | Blocks:outward:MC-132029:cmd-tab from F11 forces minimize to Dock on macOS

## Description

I can't switch between tabs on Minecraft with command tab when using Minecraft's built-in fullscreen mode, I can usually press command and then tab to change tabs but since I got 1.17 this no longer works
What I expected to happen was...:
when I press command tab a little bar could appear and I should go to my desktop screen
What actually happened was...:
I get a little bar that swaps them but it doesn't swap
Steps to Reproduce:
1. press command tab
2. ...
3. ...

## Comments (3)

### Comment 1: migrated (2021-06-10T21:20:15.188-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: pine1needle (2021-06-17T23:01:35.589-0700)

Switching windows using Cmd+Tab is only broken if you are using Minecraft's built-in fullscreen mode. More detailed behavior is described in the table below.

1.16.5
1.17
Minecraft's built-in fullscreen
Cmd+Tab partially works.  You can tab out of Minecraft, but you can't tab back into Minecraft due to .
Cmd+Tab doesn't work.  Here's a video:
 (In the video, the "java" icon is Minecraft; see MCL-15163.)
macOS's native fullscreen
Cmd+Tab works.
Cmd+Tab works.
Windowed (not fullscreen)
Cmd+Tab works.
Cmd+Tab works.
By "Minecraft's built-in fullscreen", I am referring to the fullscreen mode that can be toggled in Minecraft's video settings or alternatively by pressing Fn+Ctrl+F11. (Ctrl might be optional for you depending on your keyboard settings in system preferences.) By "macOS's native fullscreen", I am referring to the fullscreen mode that can be toggled by clicking the green circle on the upper left corner of the window.
This is probably related to , and maybe also to MC-170545.

### Comment 3: clamlol (2024-02-01T13:17:14.987-0800)

The behavior in 24w05b seems the same as in 1.16.5; that is, this issue has been fixed and  has been unblocked.
