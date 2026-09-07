# MC-279016: Moving through tripwire in Spectator mode and changing game mode after moving away activates the tripwire

**Mojira URL:** [https://bugs.mojang.com/browse/MC-279016](https://bugs.mojang.com/browse/MC-279016)

## Report details

- **Mojira categories:** Collision; Player
- **Project:** MC
- **Issue key:** MC-279016
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2024-12-27T01:35:24.750-0800
- **Updated:** 2026-04-11T10:11:11.950-0700
- **Resolution date:** 2025-09-19T12:07:34.128-0700
- **Affects versions:** 24w45a; 1.21.4
- **Fix versions:** 25w09a
- **Area:** Platform
- **Votes:** 1
- **Watchers:** 3
- **Attachments:** 4
- **Attachment filenames:** 25w08a.mp4; 25w09a.mp4; Lunar Client 1.21.4 (d5f284d_version_1-21-2-take2) 2024-12-27 20-34-35.mp4; MC-279016.mp4
- **Issue links:** Duplicate:inward:MC-279133:Interactive Blocks get triggered by Spectators when switching to a different gamemode | Relates:outward:MC-279033:Moving through cobwebs in Spectator mode and changing game mode to survival/adventure after moving away slows down the player for a brief period

## Description

After going through a tripwire hook in spectator mode and changing to another gamemode, the tripwire hook will activate.
What I expected to happen was...:
The tripwire hook to stay deactivated after changing back from spectator mode.
What actually happened was...:
The tripwire hook had activated after passing through it in spectator mode and leaving spectator mode.
Steps to Reproduce:
- Create a world with cheats enabled.

- Build a small tripwire hook mechanism.

- Change into spectator mode.

- Pass through the tripwire in spectator.

- Change into Creative / Survival / Adventure mode.

- Tripwire will activate, does not matter where you are.

## Comments (10)

### Comment 1: migrated (2024-12-27T01:35:24.750-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: flow_santohyj123 (2024-12-27T02:46:02.898-0800)

Modified versions are not supported.

### Comment 3: BugTracker_ (2024-12-27T03:44:41.695-0800)

Please try reproducing this in the official Minecraft launcher with no mods installed.

### Comment 4: J Z (2024-12-27T04:51:43.980-0800)

I can confirm this in vanilla Minecraft; the bug does not always happen, though, perhaps depending on player angle. The bug also affects nether portals, end portals and end gateways; it was introduced in 24w45a.

### Comment 5: flow_santohyj123 (2024-12-27T15:09:54.115-0800)

This bug also seems to affect sweet berry bushes, cactus, fire, campfires, wither roses, and cobwebs. Should this be a new report instead?

### Comment 6: J Z (2024-12-28T04:19:27.499-0800)

@santohyj123: As @ManosSef already split the instance with portals from the instance with tripwires, it would probably be a good idea to create a new report for these other blocks.
I created a bug report, by the way, for a log warning that gets outputted as a side effect when you do the procedure with cobwebs, which I hope doesn't take away anything from what you wanted to report.

### Comment 7: flow_santohyj123 (2024-12-28T07:00:00.795-0800)

Seems like this bug and related spectator issues started occuring in version 24w45a.
Also, thanks , created the bug reports.

### Comment 8: TheUnknownOne (2025-01-04T07:39:49.610-0800)

I tried doing what J Z suggested (to help out since this bug can get a little annoying when spectating sensitive contraptions) and it immediately got a comment labeling it as a duplicate of this post.  (shrugs)

### Comment 9: J Z (2025-03-05T13:48:18.740-0800)

Cannot reproduce in 25w10a.

### Comment 10: J Z (2025-03-17T08:29:36.513-0700)

Fixed in 25w09a.
