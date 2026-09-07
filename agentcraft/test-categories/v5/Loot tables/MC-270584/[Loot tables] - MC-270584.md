# MC-270584: Vault/Ominous Vault loot isn't predetermined, allowing players to create backups of their worlds to get desired rewards

**Mojira URL:** [https://bugs.mojang.com/browse/MC-270584](https://bugs.mojang.com/browse/MC-270584)

## Report details

- **Mojira categories:** Loot tables
- **Project:** MC
- **Issue key:** MC-270584
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2024-04-10T08:53:50.588-0700
- **Updated:** 2025-05-29T09:07:01.288-0700
- **Resolution date:** 2024-07-11T10:38:47.027-0700
- **Affects versions:** 1.20.4; 1.20.5 Pre-Release 1; 1.20.5 Pre-Release 3; 1.20.5; 1.20.6; 24w20a; 24w21b; 1.21 Pre-Release 1; 1.21; 1.21 Release Candidate 1
- **Fix versions:** 24w19a
- **Area:** Expansion B
- **Watchers:** 2
- **Attachments:** 6
- **Attachment filenames:** MC-270584-No-Repro-1st-Attempt.png; MC-270584-No-Repro-2nd-Attempt.png.png; MC-270584-Repro-1st-Attempt-Vault.png; MC-270584-Repro-2nd-Attempt-Vault.png.png; MC-270584-Repro-3rd-Attempt-Vault.png.png; screenshot-1.png
- **Issue links:** Relates:inward:MC-184019:Ok so there is this really creepy ender dragon gitch that MADE ME not play minecraft for 4 years | Relates:inward:MCPE-184019:Trial Chambers loot is random in the same seed

## Description

This only realistically affects singleplayer. When you open a vault, you get a different set of rewards each time if you've created multiple copies of a world. This means for example, if you see a heavy core in an ominous vault, it's theoretically a guaranteed chance to get it simply by making copies of your world before opening the vault, repeating the process until you eventually get it.
Steps to reproduce:
1. Find a trial chamber and locate a vault.
2. Press F3+C to copy your coordinates.
3. Exit and make a copy of that world.
4. Open that vault in one of the copies of the world.
5. Open that same vault in the other copy of your world.
Observed results: I got a different set of rewards each time.
Expected results: I should get the same set of rewards each time.
Video demonstrating the issue: https://youtu.be/MFutDmMbWj8

## Comments (5)

### Comment 1: migrated (2024-04-10T08:53:50.588-0700)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: [Mod] Jingy (2024-04-10T17:21:34.409-0700)

I couldn't seem to reproduce this (possibly to my own fault). Both the loot tables for the two different worlds on the original and the backup provided the same loot.
The poison arrows and the carrot were the first vault I opened, and the loot following was another one I opened. This was the same on both worlds:

### Comment 3: [MOD] Greymagic27 (2024-04-11T03:35:40.838-0700)

I'm also unable to reproduce this on an ominous vault:
First attempt:

Second attempt:

However, when using a normal vault I could reproduce this:
First attempt:

Second attempt:

Third attempt:

### Comment 4: migrated (2024-04-12T09:42:36.215-0700)

Interesting. I only tested it on ominous vaults and it worked for me, so I assumed normal vaults shouldn't be any different.
I'm a bit busy right now but I'll re-verify my reproduction steps tomorrow.

### Comment 5: migrated (2024-04-16T10:08:21.307-0700)

Sorry it took a while, I sorted out my school stuff and now that summer vacation is here, I've uploaded the reproduction video.
