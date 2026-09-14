# MC-248230: Players get stuck on the "Loading terrain..." screen after rejoining the world whilst above or below the build limit

**Mojira URL:** [https://bugs.mojang.com/browse/MC-248230](https://bugs.mojang.com/browse/MC-248230)

## Report details

- **Mojira categories:** Chunk loading
- **Project:** MC
- **Issue key:** MC-248230
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2022-01-23T06:47:14.044-0800
- **Updated:** 2025-04-30T07:31:57.017-0700
- **Resolution date:** 2022-07-14T15:12:36.627-0700
- **Affects versions:** 22w03a
- **Fix versions:** 22w05a
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-248230.mp4; MC-248230.png

## Description

The Bug:
When a player exits a world in any dimension whilst below y level -64, or above y level 320, if they were to rejoin it, they would be stuck on the "Loading terrain..." screen forever. This issue did not occur in 1.18.1.
Steps to Reproduce:
- Launch an instance of 22w03a and create a new world with cheats enabled.

- Teleport yourself high up into the air.

```
/tp @s ~ 1000 ~
```
- Leave the world before traveling below y level 320.

- Reload into the same world and wait around thirty seconds.

- Take note as to whether or not players get stuck on the "Loading terrain..." screen after rejoining the world whilst above or below the build limit.

Observed Behavior:
Players get stuck on the "Loading terrain..." screen.
Expected Behavior:
Players would not get stuck on the "Loading terrain..." screen, just like in 1.18.1.

## Comments (8)

### Comment 1: migrated (2022-01-23T06:47:14.044-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: Dott (2022-01-23T18:08:29.565-0800)

I was able to reproduce this bug without dying
- Teleport at y-coordinate like -100

- Make sure you're falling, Esc -> Save and Quit

- When you enter the world again, you will see a screen that says "Loading terrain..." and hear the sound of void damage

### Comment 3: Avoma (2022-01-24T00:11:49.012-0800)

Hi, yes, thank you for this information!
Regarding your statement, I did some further investigating and indeed found that no death is required in order to reproduce this, as you mentioned above already. This problem actually occurs when reloading into a world whilst above or below the build limit, (below y level -64, or above y level 320). Since I'm the reporter of this ticket, I've updated it to reflect this new information. Thank you!

### Comment 4: migrated (2022-05-10T17:38:57.872-0700)

I’ve ran into this problem on my server except it is not the height it’s in 1.18.2 I died and left the server, and when I tried to relog it was stuck on loading terrain

### Comment 5: migrated (2022-07-01T15:06:26.266-0700)

I think this bug still exists in 1.19. I cant excess one of my world due to the infinite loading terrain screen. Would love to know how to fix this.

### Comment 6: migrated (2022-07-01T15:59:58.071-0700)

See .

### Comment 7: migrated (2022-07-14T14:12:48.133-0700)

I experienced this today. Was respawned the Ender Dragon and was pushed off of one of the obsidian  pillars and died. Exited world before respawning. When I tried loading the world it keeps saying Building terrain.

P.s It is the latest version of minecraft and the software my ps4 console is up to date.

### Comment 8: migrated (2022-07-14T15:12:36.627-0700)

This is for java edition...
