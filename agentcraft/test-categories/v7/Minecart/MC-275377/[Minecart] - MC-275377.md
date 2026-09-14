# MC-275377: Derailed minecarts snap onto nearby rails after falling down

**Mojira URL:** [https://bugs.mojang.com/browse/MC-275377](https://bugs.mojang.com/browse/MC-275377)

## Report details

- **Mojira categories:** Minecart
- **Project:** MC
- **Issue key:** MC-275377
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2024-08-15T20:56:52.484-0700
- **Updated:** 2025-04-26T16:12:20.333-0700
- **Resolution date:** 2024-08-21T12:25:56.899-0700
- **Affects versions:** 24w33a
- **Fix versions:** 24w34a
- **Labels:** experimental_minecart
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2024-08-21_14.24.40.png; image-2024-08-16-11-52-06-558.png; image-2024-08-16-11-52-33-905.png; Setup.png

## Description

Steps to reproduce:
- Build the following setup in a world with the Minecart Improvements experiment enabled:

- Push the minecart a bit

- Break the powered rail underneath the minecart

- Break the block underneath the minecart

Observed result:
Whatever the minecart's x, z values were, it will snap onto the center of the rail.
Expected result:
The minecart will keep its x, z values like in 1.21.1 and below.

## Comments (2)

### Comment 1: migrated (2024-08-15T20:56:52.484-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: [Mod] Jingy (2024-08-21T12:24:57.093-0700)

Fixed in 24w34a:
