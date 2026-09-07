# MC-275276: Minecarts can phase through blocks at the bottom of a slant

**Mojira URL:** [https://bugs.mojang.com/browse/MC-275276](https://bugs.mojang.com/browse/MC-275276)

## Report details

- **Mojira categories:** Minecart
- **Project:** MC
- **Issue key:** MC-275276
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2024-08-15T11:16:26.207-0700
- **Updated:** 2025-04-26T16:08:58.838-0700
- **Resolution date:** 2024-08-21T13:01:02.918-0700
- **Affects versions:** 1.21.1; 24w33a
- **Fix versions:** 24w34a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** 2024-08-18_20.15.20.png; 2024-08-18_20.19.27.png; 2024-08-18_20.19.45.png; 2024-08-21_14-54-57.mp4; Observed.png; Setup.png
- **Issue links:** Relates:inward:MC-8004:Minecarts can move inside of or through blocks at the end of curved or downward sloped rails | Relates:outward:MC-275210:Minecarts can phase through blocks when travelling diagonally upwards | Duplicate:inward:MC-275608:Minecarts clip through blocks when they're on a decline

## Description

Steps to reproduce:
- Build the following setup:

- Push the minecart down the slope

Observed result:
Expected result:
The minecart would not phase through the block at the bottom of the slope.
It occurs with all types of rails, and the faster it goes, the more likely it is to go onto the rails to the left.

## Comments (7)

### Comment 1: migrated (2024-08-15T11:16:26.207-0700)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: Aarolin (2024-08-15T15:05:20.804-0700)

Can confirm. This only happens with the experimental toggle on, and isn't present in either 1.21 or the untoggled game. It happens regardless of the minecart max speed, whether it's the default, 1, or 1000.

### Comment 3: migrated (2024-08-16T13:22:22.449-0700)

after further review, I would appreciate if this were left in the game. It isn't intuitive, but it for sure is fun and useful.

### Comment 4: The Ziglin Brute (2024-08-17T11:05:23.188-0700)

Confirmed

### Comment 5: migrated (2024-08-18T05:21:31.548-0700)

I can provide another case that is used widely in technical MC community.
For this setup:
If I place the cart at the white wool, with minecart experiments turning off, the cart should be blocked by the amethyst, and then lose its velocity (eventually, the cart falls with no velocity, and will be burned by the lava in the cauldron). However, in the experiments, although it is blocked, it does not lose its velocity and keep moving forward.

### Comment 6: Ceresjanin123 (2024-08-21T10:48:38.994-0700)

This appears fixed in 24w34a

### Comment 7: [Mod] Jingy (2024-08-21T12:54:35.622-0700)

I can also verify this was fixed in 24w34a.
