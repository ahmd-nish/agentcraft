# MC-191669: Sprinting is disabled when switching your gamemode to spectator while sprinting into a block or general obstruction

**Mojira URL:** [https://bugs.mojang.com/browse/MC-191669](https://bugs.mojang.com/browse/MC-191669)

## Report details

- **Mojira categories:** Input
- **Project:** MC
- **Issue key:** MC-191669
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2020-06-24T12:46:13.922-0700
- **Updated:** 2025-08-07T04:30:14.788-0700
- **Resolution date:** 2025-08-07T04:30:14.717-0700
- **Affects versions:** 1.16.1; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Pre-release 2; 1.16.2 Pre-release 3; 1.16.2 Release Candidate 2; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4; 20w46a; 21w03a; 21w05b; 21w06a; 21w11a; 1.17; 1.18.1; 1.20.4; 24w09a; 1.20.5
- **Fix versions:** 25w33a
- **Area:** Platform
- **Game mode:** Spectator
- **Labels:** game-mode-switch; spectator; sprinting
- **Votes:** 2
- **Watchers:** 2
- **Attachments:** 2
- **Attachment filenames:** 5.mp4; SpectatorSprint.mp4
- **Issue links:** Relates:outward:MC-133414:Sprinting in shallow water is no longer possible | Relates:inward:MC-69216:Switching to spectator mode while fishing keeps rod cast | Duplicate:inward:MC-215165:Spectators cannot sprint-fly when starting out inside blocks | Duplicate:inward:MC-182750:You can't sprint in Spectator when you switch to it in a block(only if using arrow keys to move)

## Description

If change your gamemode to spectator while running into an obstruction, your sprint will be disabled.
Steps to Reproduce:
- Run towards a wall in Creative or Survival mode (continue doing this)

- Press F3 + N to change gamemode

Observed & Expected Results
 - You will not be sprinting when entering spectator mode, and will not be able to sprint at all until changing your gamemode again.
 - Your sprint would continue when changing gamemodes, and not be disabled.
Video
(Since my key presses are not shown, I am sprinting into the wall, switching game modes, then sprinting again in spectator)

Notes
- Related to other sprinting issues:

- The player can fix this themselves by changing their gamemode off spectator, and then changing back.

- This only works for changing gamemode with F3 + N, not by using the gamemode switcher with F3 + F4.

## Comments (16)

### Comment 1: migrated (2020-06-24T12:46:13.922-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: galaxy_2alex (2020-06-24T12:53:42.770-0700)

I am unable to reproduce, please note that double-tapping forwards to sprint does not and never has worked in Spectator and Creative mode. Please provide more detailed steps on how to reproduce, and in the process, please also try to reproduce it again yourself.

### Comment 3: migrated (2020-06-24T13:08:58.967-0700)

This only seems to occur when using a key bound to Sprint in Options -> Controls to sprint and not double-tapping forwards.

### Comment 4: galaxy_2alex (2020-06-24T13:15:41.129-0700)

I am unable to reproduce this with the specific sprint key either, so please provide more detailed reproduction steps and details on the environment - if possible, also provide screenshots while you have your F3 debug screen enabled.

### Comment 5: migrated (2020-06-24T13:34:01.683-0700)

I've provided a video.

### Comment 6: galaxy_2alex (2020-06-24T13:43:30.863-0700)

Lovely, thanks, that helps - was able to reproduce it, I adjusted the title to show what is happening.

### Comment 7: migrated (2020-06-24T18:13:54.964-0700)

By the way, this bug has been around since 1.9.

### Comment 8: migrated (2020-07-16T06:03:28.208-0700)

I reported it first!

### Comment 9: anthony cicinelli (2020-07-16T06:19:54.010-0700)

Bobby N. The mods go with what ever ticket has the most information at the time. Not the first one. Trust me this happened to me once as well.

### Comment 10: galaxy_2alex (2020-07-16T09:01:32.061-0700)

In this case, it's because this one was set with a Mojang Priority.

### Comment 11: migrated (2021-03-19T14:26:13.388-0700)

Can confirm for 21w11a.

### Comment 12: Brevort (2021-06-08T19:39:13.348-0700)

Can confirm in 1.17. Also occurs when the player is right next to a block, not necessarily underground or inside blocks.

### Comment 13: [Mod] Jingy (2023-12-24T16:36:44.830-0800)

Requesting ownership of this issue due to an inactive owner

### Comment 14: migrated (2024-07-08T21:27:49.410-0700)

anyone wanna fix this issue its been four years

### Comment 15: Viradex (2024-07-08T21:40:36.646-0700)

Mojang has thousands of bugs to fix. They will fix it when they can.
Please do not add unnecessary comments like this.

### Comment 16: Benats (2025-06-17T16:01:41.810-0700)

Can confirm in 1.21.6
