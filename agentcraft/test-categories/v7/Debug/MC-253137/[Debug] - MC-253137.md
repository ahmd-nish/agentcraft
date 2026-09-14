# MC-253137: The game output console is logged with errors regarding missing signatures from property textures when joining LAN worlds

**Mojira URL:** [https://bugs.mojang.com/browse/MC-253137](https://bugs.mojang.com/browse/MC-253137)

## Report details

- **Mojira categories:** Debug
- **Project:** MC
- **Issue key:** MC-253137
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2022-06-15T14:49:23.838-0700
- **Updated:** 2025-04-29T11:42:24.768-0700
- **Resolution date:** 2023-11-07T11:43:39.187-0800
- **Affects versions:** 22w24a; 1.19.1 Pre-release 1; 1.19.1 Release Candidate 1; 1.19.1 Pre-release 2; 1.19.1 Pre-release 5; 22w43a; 22w46a; 1.20 Pre-release 6; 23w31a
- **Fix versions:** 23w32a
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** latest.log; MC-253137.png; screenshot-1.png
- **Issue links:** Cloners:inward:MC-264966:"Signature is missing from Property textures" appears in the logs of some Minecraft worlds due to player heads

## Description

The Bug:
The game output console is logged with errors regarding missing signatures from property textures when joining LAN worlds.
In my testing, this issue is exclusive to LAN worlds and cannot be reproduced on singleplayer worlds or multiplayer servers.
When joining a LAN world, the following is printed into the game output console:

```
[10:36:12] [Worker-Main-3/ERROR]: Signature is missing from Property textures
```
Steps to Reproduce:
- Launch an instance of the game with logs enabled.

- Get another player to start a world and open it to LAN.

- Join the LAN world and look at the game output console.

- Take note as to whether or not the game output console is logged with errors regarding missing signatures from property textures when joining LAN worlds.

Observed Behavior:
Errors are printed into the game output console.
Expected Behavior:
No errors would be printed into the game output console.

## Comments (8)

### Comment 1: migrated (2022-06-15T14:49:23.838-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: Avoma (2022-06-16T10:36:05.609-0700)

Further investigating concludes that this issue is exclusive to LAN worlds and cannot be reproduced on singleplayer worlds or multiplayer servers. I've updated this ticket accordingly to reflect this new information.

### Comment 3: Avoma (2023-05-28T02:55:12.324-0700)

The core problem here is still present, but the error message is now slightly different. I'm not exactly sure when this change was made, but I've updated this ticket accordingly. Just leaving a note of this here.

### Comment 4: mattp12 (2023-08-02T10:08:39.623-0700)

Also happens on 23w31a when joining a single player world, but not every time it seems?

### Comment 5: Lolo (2023-08-20T12:19:42.739-0700)

Affects Minecraft 23w32a and 23w33a (even in Minecraft Singleplayer)

### Comment 6: blublu_owns123 (2023-11-05T11:26:17.746-0800)

just happen on my world for 1.20.2.
19:16:54.910
com.mojang.authlib.yggdrasil.YggdrasilMinecraftSessionService
Worker-Main-6
Signature is missing from Property textures
19:28:33.020
com.mojang.authlib.yggdrasil.YggdrasilMinecraftSessionService
Worker-Main-4
Signature is missing from Property textures
19:28:33.020
com.mojang.authlib.yggdrasil.YggdrasilMinecraftSessionService
Worker-Main-4
Signature is missing from Property textures
19:29:10.732
com.mojang.authlib.yggdrasil.YggdrasilMinecraftSessionService
Worker-Main-6
Signature is missing from Property textures
19:29:44.112
com.mojang.authlib.yggdrasil.YggdrasilMinecraftSessionService
Worker-Main-2
Signature is missing from Property textures
19:29:56.648
com.mojang.authlib.yggdrasil.YggdrasilMinecraftSessionService
Worker-Main-8
Signature is missing from Property textures
19:29:56.803
com.mojang.authlib.yggdrasil.YggdrasilMinecraftSessionService
Worker-Main-2
Signature is missing from Property textures
20:49:27.082
com.mojang.authlib.yggdrasil.YggdrasilMinecraftSessionService
Worker-Main-3
Signature is missing from Property textures
20:49:41.492
com.mojang.authlib.yggdrasil.YggdrasilMinecraftSessionService
Worker-Main-5
Signature is missing from Property textures
20:54:05.877
com.mojang.authlib.yggdrasil.YggdrasilMinecraftSessionService
Worker-Main-14
Signature is missing from Property textures
20:54:05.878
com.mojang.authlib.yggdrasil.YggdrasilMinecraftSessionService
Worker-Main-15
Signature is missing from Property textures

### Comment 7: [Mod] turbo (2023-11-05T11:59:06.760-0800)

@ This has been reported again as  (you can find it as a linked issue), which has been fixed as of 23w42a. This means that 1.20.2 is affected, but the latest snapshot is not.

### Comment 8: blublu_owns123 (2023-11-07T11:43:39.187-0800)

@ its this the Original Post of the issue?
