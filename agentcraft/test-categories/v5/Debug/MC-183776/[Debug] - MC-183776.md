# MC-183776: After switching game modes using F3+F4, you need to press F3 twice to toggle the debug screen

**Mojira URL:** [https://bugs.mojang.com/browse/MC-183776](https://bugs.mojang.com/browse/MC-183776)

## Report details

- **Mojira categories:** Debug; Input
- **Project:** MC
- **Issue key:** MC-183776
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2020-05-13T09:25:42.349-0700
- **Updated:** 2025-10-09T12:36:59.149-0700
- **Resolution date:** 2025-06-17T09:14:44.699-0700
- **Affects versions:** 20w20a; 20w20b; 20w21a; 20w22a; 1.16 Pre-release 1; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 4; 1.16 Pre-release 5; 1.16 Pre-release 6; 1.16 Pre-release 8; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w27a; 20w28a; 20w30a; 1.16.2 Release Candidate 1; 1.16.2 Release Candidate 2; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4 Pre-release 1; 1.16.4; 20w45a; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w06a; 21w08b; 21w11a; 21w13a; 21w15a; 1.17; 1.17.1; 21w42a; 21w44a; 1.18 Pre-release 1; 1.18 Release Candidate 1; 1.18.1; 22w03a; 22w07a; 1.18.2 Pre-release 1; 1.18.2; 22w11a; 22w12a; 22w14a; 22w15a; 22w18a; 22w19a; 1.19 Pre-release 4; 1.19 Pre-release 5; 1.19; 1.19.2; 1.19.3; 23w03a; 1.19.4 Pre-release 2; 1.19.4; 23w17a; 23w18a; 1.20 Pre-release 1; 1.20.1; 23w31a; 23w32a; 23w33a; 1.20.2; 23w43a; 1.20.4; 24w04a; 24w09a; 1.21 Pre-Release 3; 1.21 Pre-Release 4; 1.21; 24w34a; 24w45a; 24w46a; 1.21.5 Release Candidate 1
- **Fix versions:** 25w31a
- **Area:** Platform
- **Labels:** game-mode-switch
- **Votes:** 1
- **Watchers:** 2
- **Attachments:** 1
- **Attachment filenames:** Minecraft 20w20a - Singleplayer 2020-05-13 12-24-17.mp4
- **Issue links:** Duplicate:inward:MC-189098:F3 does not toggle debug information for one press after using the Game Mode Switcher | Duplicate:inward:MC-213044:F3 button out of sync upon game start | Duplicate:inward:MC-206629:Must press F3 an extra time to open the debug menu after using the gamemode switcher | Duplicate:inward:MC-203787:F3 takes two presses to open debug menu after using F3+F4 to switch gamemode | Duplicate:inward:MC-193142:Pressing F3 after using F3+F4 does not work | Duplicate:inward:MC-191638:Need to press F3 twice to open debug menu after using game mode switcher (F3 + F4) | Duplicate:inward:MC-183889:Need to double press f3 to open f3 menu | Cloners:inward:MC-302737:After using the game mode switcher, you need to press F3 twice to toggle the debug overlay

## Description

The Bug
For some very odd reason you need to click F3 twice now if you change gamemodes this way. Doesn't affect commands. Very good UI for the new gamemode screen I have to say, good work Mojang!
Steps to Reproduce
- Open the gamemode switcher and switch into any gamemode. (Hold F3 and press F4 to bring up this menu and to navigate between gamemodes).

- Hit the F3 key in an attempt to enable the debug menu.

- Take note of whether the F3 debug menu is enabled.

- Hit the F3 key again.

- Take note as to whether or not the F3 debug menu is now enabled.

Observed Behavior
After using the gamemode switcher, you are required to press the F3 key twice in order to enable the debug menu.
Expected Behavior
After using the gamemode switcher, you would not be required to press the F3 key twice in order to enable the debug menu. Instead, you should only have to press the F3 key once in order to enable the debug menu after using the gamemode switcher.
Code analysis
Code analysis by  can be found in this comment.

## Comments (36)

### Comment 1: migrated (2020-05-13T09:25:42.349-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: Whomsky (2020-05-13T11:46:32.928-0700)

Can confirm

### Comment 3: migrated (2020-05-18T10:01:39.756-0700)

I often noticed that F3 sometimes didn’t toggle debug screen, now I finally know when it happens.

### Comment 4: migrated (2020-06-05T07:19:18.017-0700)

Confirmed for 1.16 Prerelease 1

### Comment 5: migrated (2020-06-15T16:03:13.273-0700)

Confirmed in 1.16 Pre-release 6.

### Comment 6: migrated (2020-11-05T09:43:02.562-0800)

Confirmed in 20w45a.

### Comment 7: Avoma (2021-01-19T05:38:00.327-0800)

Can confirm in 20w51a.

### Comment 8: Avoma (2021-01-26T03:23:59.399-0800)

Can confirm in 21w03a.

### Comment 9: migrated (2021-02-10T14:27:52.255-0800)

Confirm in 21w06a

### Comment 10: migrated (2021-03-19T14:29:22.942-0700)

Affects 21w11a.

### Comment 11: clamlol (2021-03-31T12:00:19.239-0700)

Can confirm in 21w13a

### Comment 12: clamlol (2021-04-15T17:51:34.341-0700)

Can confirm in 21w15a

### Comment 13: Avoma (2021-06-24T10:32:47.743-0700)

Can confirm in 1.17.

### Comment 14: migrated (2021-07-06T15:54:10.464-0700)

Can confirm 1.17.1

### Comment 15: Avoma (2021-10-25T03:53:17.331-0700)

Can confirm this behavior in 21w42a. Here are some extra details regarding this problem.
The Bug:
After using the gamemode switcher, you are required to press the F3 key twice in order to enable the debug menu.
Steps to Reproduce:
- Open the gamemode switcher and switch into any gamemode. (Hold F3 and press F4 to bring up this menu and to navigate between gamemodes).

- Hit the F3 key in an attempt to enable the debug menu.

- Take note of whether the F3 debug menu is enabled.

- Hit the F3 key again.

- Take note as to whether or not the F3 debug menu is now enabled.

Observed Behavior:
After using the gamemode switcher, you are required to press the F3 key twice in order to enable the debug menu.
Expected Behavior:
After using the gamemode switcher, you would not be required to press the F3 key twice in order to enable the debug menu. Instead, you should only have to press the F3 key once in order to enable the debug menu after using the gamemode switcher.

### Comment 16: AllPlayed (2021-11-07T08:44:31.090-0800)

Can confirm this behavior in 21w44a

### Comment 17: AllPlayed (2021-11-12T06:39:57.956-0800)

Can confirm, as well, in 1.18 Pre-Release 1

### Comment 18: migrated (2021-11-25T10:25:25.421-0800)

Can confirm in 1.18 rc1

### Comment 19: Avoma (2021-12-19T07:43:18.924-0800)

Can confirm in 1.18.1.

### Comment 20: clamlol (2022-01-25T16:08:03.503-0800)

Affects 22w03a.

### Comment 21: clamlol (2022-02-16T14:01:35.681-0800)

Affects 22w07a.

### Comment 22: clamlol (2022-02-18T13:47:33.331-0800)

Affectx 1.18.2-pre1.

### Comment 23: clamlol (2022-03-16T13:33:32.058-0700)

Affects 22w11a.

### Comment 24: Chandler (2022-03-23T21:46:06.715-0700)

Code analysis
(placed in the comments to avoid crowding the description)
net.minecraft.client.Keyboard.java (22w11a, Yarn mappings)

```if (this.client.currentScreen == null || this.client.currentScreen.passEvents) {
            InputUtil.Key bl = InputUtil.fromKeyCode(key, scancode);
            if (action == 0) {
                KeyBinding.setKeyPressed(bl, false);
                if (key == 292) {
                    if (this.switchF3State) {
                        this.switchF3State = false;
                    } else {
                        this.client.options.debugEnabled = !this.client.options.debugEnabled;
                        this.client.options.debugProfilerEnabled = this.client.options.debugEnabled && Screen.hasShiftDown();
                        this.client.options.debugTpsEnabled = this.client.options.debugEnabled && Screen.hasAltDown();
                    }
                }
            }
. . .
}```
This if-statement is responsible for toggling on and off the debug menu when F3 is released. However, this.client.currentScreen == null is false when F3 + F4 is pressed because it pulls up a screen. In this case, the release of the F3 key is not detected because the screen remains open until after it is released, and thus this.switchF3State remains set to true. This is why it takes two more presses of F3 to toggle the menu.
A potential easy fix for this would be to change the following code earlier in net.minecraft.client.Keyboard.java#processF3() from

```case 293: {
                if (!this.client.player.hasPermissionLevel(2)) {
                    this.debugLog("debug.gamemodes.error", new Object[0]);
                } else {
                    this.client.setScreen(new GameModeSelectionScreen());
                }
                return true;
            }```
 to

```case 293: {
                if (!this.client.player.hasPermissionLevel(2)) {
                    this.debugLog("debug.gamemodes.error", new Object[0]);
                    return true;
                } else {
                    this.client.setScreen(new GameModeSelectionScreen());
                    return false;
                }
            }```
to make sure this.switchF3State is never set to true when F3+F4 is pressed and succeeds.

### Comment 25: clamlol (2022-03-25T14:58:01.909-0700)

Affects 22w12a (edit: and 22w14a).

### Comment 26: Avoma (2022-04-15T12:09:50.864-0700)

Can confirm in 1.18.2 and 22w15a.

### Comment 27: clamlol (2022-05-04T17:05:50.239-0700)

Affects 22w18a.

### Comment 28: clamlol (2022-05-12T13:06:46.207-0700)

Affects 22w19a.

### Comment 29: clamlol (2022-05-18T13:35:56.535-0700)

Affects 1.19-pre1.

### Comment 30: migrated (2022-10-25T18:21:18.349-0700)

Affects 22w42a

### Comment 31: migrated (2023-08-09T18:13:53.682-0700)

In 23w32a and in 1.20.1

### Comment 32: mattp12 (2023-10-07T11:51:55.307-0700)

Confirmed for 23w40a

### Comment 33: AllPlayed (2024-06-05T04:25:05.996-0700)

Affects 1.21 Pre-release 3

### Comment 34: AllPlayed (2024-06-09T05:09:33.539-0700)

Affects 1.21 Pre-release 4

### Comment 35: AllPlayed (2024-06-13T10:51:32.470-0700)

Affects 1.21 and the Release Candidate 1

### Comment 36: RayZ_R (2024-08-27T04:05:50.688-0700)

The fix by @TriWonder81 resolves the bug, but it creates a new one:
When pressing F3+F4+ESC and then releasing F3, the debug menu will open, which doesn't happen without the fix. This occurs because when pressing F3+F4, this.switchF3State is set to false, but when pressing ESC to exit the screen, this.switchF3State isn't changed, which means the F3 menu will open when F3 is released.
Both the initial and the new bug can be fixed by adding setSwitchF3State method to net.minecraft.client.Keyboard.java:

```public void setSwitchF3State(boolean switchF3State) {
    this.switchF3State = switchF3State;
}```
and changing switchF3State in checkForClose method of net.minecraft.client.gui.screen.GameModeSelectionScreen.java:

```private boolean checkForClose() {
    if (!InputUtil.isKeyPressed(this.client.getWindow().getHandle(), GLFW.GLFW_KEY_F3)) {
        this.apply();
        this.client.setScreen(null);
        this.client.keyboard.setSwitchF3State(false); // added
        return true;
    } else {
        return false;
    }
}```
so, when GameModeSelectionScreen closes by releasing F3, switchF3State is set to false, otherwise, when ESC is pressed, it is true.
