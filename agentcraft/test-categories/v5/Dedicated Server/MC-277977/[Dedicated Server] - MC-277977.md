# MC-277977: Teleporting large distances whilst gliding prevents the world from loading and player model glitchiness

**Mojira URL:** [https://bugs.mojang.com/browse/MC-277977](https://bugs.mojang.com/browse/MC-277977)

## Report details

- **Mojira categories:** Commands; Dedicated Server
- **Project:** MC
- **Issue key:** MC-277977
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-10-30T17:52:39.605-0700
- **Updated:** 2025-04-26T17:21:14.150-0700
- **Resolution date:** 2024-11-25T07:53:16.972-0800
- **Affects versions:** 24w44a
- **Fix versions:** 1.21.4 Pre-Release 3
- **Area:** Platform
- **Labels:** teleport; teleportation; teleporting
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2024-10-31 00-38-52.mp4; 2024-10-31 00-39-39.mp4

## Description

I can consistently reproduce this with the /spreadplayers command and not with /teleport, but this issue has occurred in contexts without any /spreadplayers, only /teleport. I believe this may be reproduceable if you were to teleport onto a solid block but I couldn't get it to happen locally.
The footage attached was taken on a local dedicated server on a laptop with low performance, but this has been reproduced on a public (external) server with optimal MSPT too.
This supposedly started occurring around when the crashes caused by  started happening, so it's likely related to that part of the code having been refactored.
Steps to Reproduce:
- Glide in the air with an elytra (or any equipped item with the glider component)

- Run

```

```
/spreadplayers 0 0 0 25000 false @s{\code}

- Wait to be teleported and observe the glitch

This may need to be retried a few times to get this effect to work as it doesn't seem to happen every time.
Observed Results:
No chunks appear to load around the player, your position in the F3 screen is fixed at one spot, and the player model is rapidly changing rotation (see attached video)
This can stay this way for only a few seconds, or for many minutes. Sometimes moving your head around can fix it, but often you have to relog before anything works correctly.
Expected Results:
The chunks load as normal

## Comments (2)

### Comment 1: migrated (2024-10-30T17:52:39.605-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: COMETC2021A1 (2024-11-21T02:10:22.346-0800)

Cannot reproduce in 1.21.4-pre1.
