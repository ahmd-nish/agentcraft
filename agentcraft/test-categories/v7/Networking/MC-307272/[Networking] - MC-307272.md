# MC-307272: Servers can no longer detect left clicks from players in Spectator mode

**Mojira URL:** [https://bugs.mojang.com/browse/MC-307272](https://bugs.mojang.com/browse/MC-307272)

## Report details

- **Mojira categories:** Networking
- **Project:** MC
- **Issue key:** MC-307272
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Plausible
- **Mojang priority:** Normal
- **Created:** 2026-04-06T12:22:57.014-0700
- **Updated:** 2026-05-11T02:15:01.908-0700
- **Resolution date:** 2026-05-11T02:15:01.833-0700
- **Affects versions:** 26.1.1
- **Fix versions:** 26.2 Snapshot 7
- **Area:** Platform HC
- **Votes:** 5
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 1.21.11.mp4; 26.1.2.mp4

## Description

Short description of the issue:
From Minecraft 1.8, all the way until and including 1.11.10, it was possible for servers to detect when a spectator hit their left click button. This no longer happens as of 1.11.11 and 26.1(.1)
This breaks a lot of minigame servers and custom maps that utilize left clicking abilities while having players be in Spectator UI, such as “left click to continue” in cut scenes (like when floating above the map reading titles, detecting when the player has finished reading them), left click to move to next player or map, and so on.
This happens because ServerboundSwingPacket is no longer being sent when left clicking in Spectator mode as of 1.21.11 and 26.1(.1)
Given this has been in the game for 12 years, and in that time, been utilized heavily, I don’t see this being anything other than a unintended side-effect of a different change done to Minecraft, or a innocent change that was done without thinking of the larger consequences it would have. Both of which I would consider in the area of unintended behavior, so I am making a bug report in hopes to get it resolved! :)
If this was intentional, I would hope an actual replacement for it should be added, because removing it completely, limits are lot of creativity in minigames and maps, and as previously mentioned, breaks a lot of existing minigames and maps.
Steps to reproduce the issue
N/A
Expected result
Server receives a ServerboundSwingPacket when a connected client in Spectator mode left clicks.
Actual result
Server does not receive any packet or indication of a left click from a connected client in Spectator mode.

## Comments (2)

### Comment 1: 216fd76053f04a95bba4a54794b9926b (2026-04-10T15:23:36.665-0700)

Can confirm!

### Comment 2: 216fd76053f04a95bba4a54794b9926b (2026-04-22T03:03:00.430-0700)

These reproduction steps have been tested with Minecraft 26.1.2
One easy way to reproduce this bug involves joining a minigame server.
It does involve a few steps, but it’s the only straightforward method of reproduction I’ve thought of, so it’ll have to do.
- Join a minigame server such as mc.hypixel.net

- Join a SkyWars game with the following command /play solo_normal

- Allow the game to start and jump into the void immediately

- Upon dying, you will enter Hypixel’s version of “spectator” mode

- Fortunately, there’s a neat feature on the server that, under normal circumstances without this bug, allows you to go near a player and right-click them to enter vanilla first-person spectator mode

- Now that you’ve entered spectator mode, the bug finally reveals itself: normally, the server allows you to left-click whilst spectating somebody to open a menu; however, due to this bug, the menu never opens

Version 1.21.11 of the game is the last one where this works properly.
Version 26.1 introduces this issue.

1.21.11

26.1.2
