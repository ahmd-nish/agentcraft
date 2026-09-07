# MC-171177: You can enter nether portals in creative mode by running against the frame of the portal

**Mojira URL:** [https://bugs.mojang.com/browse/MC-171177](https://bugs.mojang.com/browse/MC-171177)

## Report details

- **Mojira categories:** Hitboxes; Player
- **Project:** MC
- **Issue key:** MC-171177
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2020-02-06T10:00:45.503-0800
- **Updated:** 2025-04-11T10:18:34.929-0700
- **Resolution date:** 2024-03-21T06:25:25.284-0700
- **Affects versions:** 1.15.2; 20w06a; 20w09a; 1.16.4 Pre-release 2; 1.16.4; 20w49a; 20w51a; 1.17.1; 1.18; 1.18.2; 1.19; 1.19.2; 1.19.3; 1.19.4; 1.20; 1.20.1; 1.20.4
- **Fix versions:** 23w51a
- **Game mode:** Creative
- **Labels:** nether_portal
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-171177.mp4; setup.png
- **Issue links:** Relates:outward:MC-218811:Big dripleaves tilt when touched from the side | Duplicate:inward:MC-202772:Crossing Nether portal without walking on the blocks where it is activated

## Description

The Bug:
You can enter nether portals in creative mode by running against the frame of the portal.
This shouldn't be the case because you don't actually touch the nether portal blocks; you only touch the nether portal's frame, therefore you should not traverse dimensions.
Steps to Reproduce:
- Build the setup as shown in the provided attachment.

- Switch into creative mode and stand on top of and in the middle of the two emerald blocks.

- Face the direction of the nether portal and begin running forward.

- As soon as you touch the gold blocks on the floor, jump and continue running so that you land on the diamond blocks and run against the frame of the nether portal.

- Take note as to whether or not you can enter nether portals in creative mode by running against the frame of the portal.

Observed Behavior:
You can enter nether portals in creative mode by running against the frame of the portal.
Expected Behavior:
You would not be able to enter nether portals in creative mode by running against the frame of the portal.

## Comments (8)

### Comment 1: migrated (2020-02-06T10:00:45.503-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: Avoma (2020-12-03T12:14:27.707-0800)

Can confirm in 20w49a.

### Comment 3: Avoma (2021-01-15T03:40:44.904-0800)

Can confirm in 20w51a.

### Comment 4: Avoma (2021-07-20T11:41:33.704-0700)

Can confirm in 1.17.1.

### Comment 5: Avoma (2022-03-10T08:12:26.791-0800)

Can confirm in 1.18.2. This ticket relates to .

### Comment 6: Avoma (2022-06-13T01:51:29.326-0700)

Can confirm in 1.19.

### Comment 7: Avoma (2022-09-13T08:42:03.738-0700)

Can confirm in 1.19.2.

### Comment 8: Avoma (2024-03-21T06:25:06.576-0700)

This issue was present in 1.20.4 but no longer occurs in 23w51a. This issue has been fixed in 23w51a so I'll be resolving this ticket as fixed.
