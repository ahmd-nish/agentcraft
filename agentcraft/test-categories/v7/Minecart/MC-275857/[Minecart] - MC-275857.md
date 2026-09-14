# MC-275857: Minecarts become invisible if a lot of them are in the same area

**Mojira URL:** [https://bugs.mojang.com/browse/MC-275857](https://bugs.mojang.com/browse/MC-275857)

## Report details

- **Mojira categories:** Minecart; Rendering
- **Project:** MC
- **Issue key:** MC-275857
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-08-22T01:01:46.244-0700
- **Updated:** 2025-04-26T16:24:55.343-0700
- **Resolution date:** 2024-09-12T01:24:55.664-0700
- **Affects versions:** 24w34a; 24w36a
- **Fix versions:** 24w37a
- **Area:** Platform
- **Labels:** experimental_minecart
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** image-2024-08-22-18-06-26-755.png; image-2024-08-23-15-34-17-578.png; world.zip
- **Issue links:** Relates:outward:MC-275883:Riding a minecart cluster into a wall freezes the game

## Description

Steps to reproduce:
- Import and open the attached world:

- Press the button on the impulse command block to kill all minecarts

- Flick the lever next to the piston

Observed result:
After some time, the minecarts in a certain area turn invisible until you reload the world.
Expected result:
All minecarts remain visible.

## Comments (5)

### Comment 1: migrated (2024-08-22T01:01:46.244-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: Viradex (2024-08-22T01:06:43.758-0700)

Can confirm. The minecarts suddenly disappeared after about 30 seconds.

### Comment 3: Ceresjanin123 (2024-08-23T06:33:36.438-0700)

For extra info, if you look in the log you'll see it gets absolutely spammed with NAN errors

### Comment 4: J Z (2024-09-11T08:27:26.678-0700)

I think it's fixed in 24w37a.

### Comment 5: Ceresjanin123 (2024-09-11T09:49:37.793-0700)

Yeah it appears fixed in 24w37a
