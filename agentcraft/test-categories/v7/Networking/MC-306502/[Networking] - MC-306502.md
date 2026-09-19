# MC-306502: Uploading a world to a snapshot Realm wipes it

**Mojira URL:** [https://bugs.mojang.com/browse/MC-306502](https://bugs.mojang.com/browse/MC-306502)

## Report details

- **Mojira categories:** Networking
- **Project:** MC
- **Issue key:** MC-306502
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Community Consensus
- **Mojang priority:** Very Important
- **Created:** 2026-02-18T08:47:00.086-0800
- **Updated:** 2026-03-12T01:27:33.259-0700
- **Resolution date:** 2026-03-12T01:27:33.125-0700
- **Affects versions:** 26.1 Snapshot 9
- **Fix versions:** 26.1 Pre-Release 2
- **Area:** Platform EC
- **Votes:** 2
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** IMG_0169.mov

## Description

For Snapshot 7, 8, and 9, when a singleplayer world is uploaded to the snapshot realm, it regenerates the whole world and just spawns you on a brand new world of that seed. I know that at the very least this does not occur in Snapshot 1. I have tried using old worlds and uploading them to the realm, making new worlds in the current snapshot version and then uploading them to the realm, closing the realm and reopening it, all to no avail. No matter what, when I upload a world it regenerates the entire save rather than carry over the world save containing progress.

## Comments (5)

### Comment 1: [MCQA] DaFron (2026-02-19T00:37:36.650-0800)

Hi!
Thank you for your report!
Could you please provide more details.
- Could you please record a video of the issue and upload it?

- What do you mean by “It regenerates the entire save rather than carry over the world save “

- Does this issue describes your topic ?

Quick Links:
📓 Issue Guidelines – 💬 Mojang Support – 📧 Suggestions – 📖 Minecraft Wiki

### Comment 2: Skaggs (2026-02-19T16:10:27.835-0800)

Hi, by regenerates the world I mean that it totally refreshes/wipes the world. Like it keeps the same seed, but all progress gets wiped. That issue unfortunately doesn’t match this, as I get no errors, it goes through fine, it just comes out with the save not being the same

### Comment 3: Skaggs (2026-02-19T16:16:57.543-0800)

This comment contained multiple media attachments (2), please login to view the attachments.

### Comment 4: Hen G (2026-02-20T23:04:18.840-0800)

Just wanted to chip in and say I have the same problem. I tried uploading an existing world into a realms save file with matching installations specifically on snapshot 9. Despite having the level data and the player data files in the directory, none of the data transfers over and ended up being a completely new world with the same seed.

### Comment 5: Hen G (2026-02-20T23:11:59.648-0800)

Something to add onto that is the time and weather does match when uploaded into the new upload. I downloaded the world file during a thunderstorm night-time in game and it was the same time and weather after uploading it into realms.
