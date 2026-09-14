# MC-245819: Lighting can still occasionally lag behind world generation

**Mojira URL:** [https://bugs.mojang.com/browse/MC-245819](https://bugs.mojang.com/browse/MC-245819)

## Report details

- **Mojira categories:** Lighting
- **Project:** MC
- **Issue key:** MC-245819
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-12-20T01:59:41.869-0800
- **Updated:** 2025-03-25T13:08:44.686-0700
- **Resolution date:** 2023-04-26T03:00:11.096-0700
- **Affects versions:** 1.18.1; 22w03a; 22w05a; 22w06a; 1.18.2 Pre-release 1; 1.18.2; 22w13a; 22w15a; 22w17a; 1.19 Pre-release 3; 1.19 Pre-release 5; 1.19; 1.19.1 Pre-release 4; 1.19.1; 1.19.2; 22w43a; 1.19.3; 1.19.4
- **Fix versions:** 23w17a
- **Watchers:** 1
- **Attachments:** 7
- **Attachment filenames:** 2022-01-14_17.28.00.png; 2022-01-14_17-26-51.mkv; 2022-01-23 13-39-28.mp4; MC-245819.mp4; MC-245819.png; MC-245819 (2).png; MC-245819 - 22w13a.png

## Description

The Bug:
Lighting can still occasionally lag behind world generation.
Please note that this issue can only be seen for a split second and could take multiple attempts to reproduce.
Steps to Reproduce:
- Start a server, join it, and grant yourself operator permissions.

- Teleport yourself far away from the spawn chunks by using the command provided below.

```
/tp @s ~1000 ~ ~
```

- Run "/kill" and as you respawn, look at your surroundings closely.

- Take note as to whether or not lighting can still occasionally lag behind world generation.

Observed Behavior:
Lighting lags behind world generation.
Expected Behavior:
Lighting wouldn't lag behind world generation.

## Comments (7)

### Comment 1: migrated (2021-12-20T01:59:41.869-0800)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: Avoma (2021-12-20T02:00:02.394-0800)

This ticket clones MC-236764.

### Comment 3: Misode (2021-12-20T06:43:39.772-0800)

From your video it looks like the chunks that have the lighting glitch were already generated (due to them rendering correctly a second before), leading me to believe this is unrelated to world generation.

### Comment 4: [Mod] Jingy (2022-01-14T15:28:44.089-0800)

I was unable to replicate the described issue, so it could possibly be hardware dependant. (Computer specs attached as a screenshot)

### Comment 5: Avoma (2022-01-15T04:19:24.151-0800)

This issue may be exclusive to server environments (LAN worlds and multiplayer servers) since I as well, was unable to reproduce this in singleplayer. This statement could be incorrect however, this is what I've determined from my testing.

### Comment 6: Avoma (2022-01-23T06:09:49.616-0800)

This issue is still present in 22w03a. I've altered the reproduction steps to hopefully make reproducing this much easier.

### Comment 7: ampolive (2022-01-23T08:26:23.969-0800)

Can confirm with the provided reproduction steps. It's very brief. This is not exclusive to server environments as I could reproduce it in singleplayer.
