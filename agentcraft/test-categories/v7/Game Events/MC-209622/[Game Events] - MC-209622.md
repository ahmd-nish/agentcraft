# MC-209622: Sculk sensors do not detect item frame / glow item frame interactions

**Mojira URL:** [https://bugs.mojang.com/browse/MC-209622](https://bugs.mojang.com/browse/MC-209622)

## Report details

- **Mojira categories:** Game Events
- **Project:** MC
- **Issue key:** MC-209622
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2020-12-26T06:39:01.295-0800
- **Updated:** 2025-04-11T12:51:45.384-0700
- **Resolution date:** 2023-02-07T04:42:54.270-0800
- **Affects versions:** 20w51a; 21w03a; 21w05b; 21w06a; 21w08b; 21w14a; 1.17; 1.17.1; 21w42a; 1.18.1; 1.18.2; 1.19 Pre-release 1; 1.19 Pre-release 2; 1.19 Pre-release 3; 1.19 Pre-release 5; 1.19; 1.19.2; 22w45a
- **Fix versions:** 23w06a
- **Labels:** sculk_sensor
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2020-12-26_14.37.50.png; 2020-12-26_14.37.56.png; 2020-12-26_14.38.00.png; MC-209622.mp4
- **Issue links:** Relates:outward:MC-207418:Breaking paintings/item frames/glow item frames does not alert sculk sensors, even though placing them does

## Description

The bug
Placing, rotating, and removing items from item frames does not activate sculk sensors.
Steps to reproduce
- Place down an item frame and a sculk sensor nearby

- Place any item inside of the item frame
 The sculk sensor is not activated

- Rotate the item in the item frame
 The sculk sensor is not activated

- Remove the item from the item frame
 The sculk sensor is not activated

Expected behavior
The sculk sensor would activate upon placing an item inside it, rotating the item inside it, and removing the item from it.

## Comments (14)

### Comment 1: migrated (2020-12-26T06:39:01.295-0800)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: Avoma (2020-12-26T06:55:28.302-0800)

Can confirm.

### Comment 3: Avoma (2021-01-21T09:14:05.074-0800)

Can confirm in 21w03a.

### Comment 4: Michael Wobst (2021-02-03T14:39:34.566-0800)

Is this still an issue in snapshot 21w05a or later?

### Comment 5: Avoma (2021-02-04T08:45:58.924-0800)

Yes, this is still an issue in 21w05a.

### Comment 6: Avoma (2021-02-13T09:43:43.343-0800)

Can confirm in 21w06a.

### Comment 7: Avoma (2021-02-27T09:56:20.464-0800)

Can confirm in 21w08b. Video attached.

### Comment 8: Avoma (2021-04-10T06:20:53.873-0700)

Can confirm in 21w14a.

### Comment 9: Avoma (2021-06-10T03:55:45.716-0700)

Can confirm in 1.17.

### Comment 10: ampolive (2021-07-07T16:33:36.017-0700)

Can confirm in 1.17.1.

### Comment 11: Avoma (2021-10-27T01:49:23.882-0700)

Can confirm this behavior in 21w42a. Here are some extra details regarding this problem.
The Bug:
Sculk sensors are not activated upon interacting with item frames.
Placing items inside of item frames, rotating them, and/or removing them won't activate nearby sculk sensors.
Steps to Reproduce:
- Place down an item frame and a sculk sensor nearby.

- Place any item inside of the item frame.

- Take note as to whether or not the sculk sensor activates.

- Rotate the item in the item frame.

- Take note as to whether or not the sculk sensor activates.

- Remove the item from the item frame.

- Take note as to whether or not the sculk sensor activates.

Observed Behavior:
Sculk sensors are not activated upon interacting with item frames.
Expected Behavior:
Sculk sensors would be activated upon interacting with item frames. (Placing items inside of item frames, rotating them, and/or removing them would activate nearby sculk sensors).

### Comment 12: Avoma (2021-12-24T10:39:49.467-0800)

Can confirm in 1.18.1.

### Comment 13: Avoma (2022-03-12T02:37:50.030-0800)

Can confirm in 1.18.2.

### Comment 14: Avoma (2022-09-03T07:15:47.448-0700)

Can confirm in 1.19.2.
