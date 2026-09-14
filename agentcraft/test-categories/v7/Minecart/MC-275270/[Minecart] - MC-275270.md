# MC-275270: Minecart not oriented correctly when placed on a sloped unpowered powered rail

**Mojira URL:** [https://bugs.mojang.com/browse/MC-275270](https://bugs.mojang.com/browse/MC-275270)

## Report details

- **Mojira categories:** Minecart
- **Project:** MC
- **Issue key:** MC-275270
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-08-15T11:09:43.666-0700
- **Updated:** 2025-04-26T16:08:47.667-0700
- **Resolution date:** 2024-08-20T06:00:32.078-0700
- **Affects versions:** 24w33a
- **Fix versions:** 24w34a
- **Area:** Platform
- **Labels:** experimental_minecart
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** image_2024-08-15_181714052.png; image-2024-08-15-18-19-45-192.png; image-2024-08-15-20-09-38-588.png; screenshot-1.png
- **Issue links:** Relates:outward:MC-275203:Minecarts always spawn facing east/west and move upward slightly when being placed on rails | Duplicate:inward:MC-275356:VERY strange visual minecart behavior (Look at Picture and Video!)

## Description

When a minecart is placed on a sloped unpowered powered rail, the minecart stays straight.
Steps to reproduce:
- Build the following setup:

- Place a minecart on the powered rail

Expected result:
Observed result:

## Comments (2)

### Comment 1: migrated (2024-08-15T11:09:43.666-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: Aarolin (2024-08-15T15:21:23.150-0700)

Can confirm. This only affects the experimental minecart toggle. In previous versions, placing the minecart would make the cart slope with the rail, but with the toggle it doesn't. The bug also occurs if the minecart is placed with a dispenser onto an unpowered rail (though doing this requires a 1-tick pulse).
Expected Behaviour (Toggle Off):
Actual Behaviour (Toggle On):
