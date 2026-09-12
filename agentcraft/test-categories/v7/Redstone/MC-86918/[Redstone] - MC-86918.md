# MC-86918: Ender dragon and piglin heads are not activated when powered by comparators

**Mojira URL:** [https://bugs.mojang.com/browse/MC-86918](https://bugs.mojang.com/browse/MC-86918)

## Report details

- **Mojira categories:** Redstone
- **Project:** MC
- **Issue key:** MC-86918
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2015-08-21T09:04:25.847-0700
- **Updated:** 2025-04-30T03:37:13.002-0700
- **Resolution date:** 2023-08-31T12:53:29.821-0700
- **Affects versions:** Minecraft 15w34c; Minecraft 15w34d; Minecraft 15w44b; Minecraft 1.10.2; Minecraft 16w41a; Minecraft 16w42a; Minecraft 1.11.2; Minecraft 1.12.2; Minecraft 17w45b; Minecraft 17w46a; Minecraft 17w47a; Minecraft 17w47b; Minecraft 17w48a; Minecraft 1.13.1; Minecraft 1.13.2-pre2; Minecraft 1.13.2; Minecraft 18w45a; Minecraft 18w46a; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 19w02a; Minecraft 19w03a; Minecraft 19w03b; Minecraft 19w03c; 1.16 Pre-release 5; 1.16.1; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Pre-release 2; 1.16.2 Pre-release 3; 1.16.2 Release Candidate 1; 1.16.2 Release Candidate 2; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4 Pre-release 1; 1.16.4 Pre-release 2; 1.16.4 Release Candidate 1; 1.16.4; 20w45a; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 21w05b; 21w06a; 21w07a; 21w08b; 21w10a; 21w11a; 21w13a; 21w14a; 1.17.1; 21w38a; 21w39a; 21w43a; 1.18 Pre-release 5; 1.18; 1.18.1; 22w05a; 22w07a; 1.18.2 Release Candidate 1; 1.18.2; 1.19; 1.19.1; 1.19.2; 22w43a; 22w46a; 1.19.3; 1.19.4; 1.20; 1.20.1
- **Fix versions:** 23w35a
- **Labels:** dragon_head; piglin_head
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 2015-08-21_17.59.14.png; MC-86918.mp4; setup.png
- **Issue links:** Relates:outward:MC-9194:A Comparator can lock a Repeater, but the Repeater doesn't look like it is locked

## Description

The Bug:
Ender dragon and piglin heads are not activated when powered by comparators.
Please note that if you were to toggle the comparator's mode whilst it's powered, the ender dragon/piglin head would now be activated.
Steps to Reproduce:
- Build the setup as shown in the attachment below.

- Activate the lever and watch the ender dragon's head closely.

- Take note as to whether or not ender dragon and piglin heads are activated when powered by comparators.

Observed Behavior:
Ender dragon and piglin heads are not activated.
Expected Behavior:
Ender dragon and piglin heads would be activated.

## Comments (9)

### Comment 1: migrated (2015-08-21T09:04:25.847-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: migrated (2018-09-12T09:50:23.206-0700)

Confirmed for 1.13.1.

### Comment 3: migrated (2018-10-21T19:41:36.977-0700)

Confirmed for 1.13.2-pre2.

### Comment 4: migrated (2020-06-13T13:18:43.913-0700)

Confirmed in 1.16-pre5.

### Comment 5: Avoma (2021-02-19T07:23:56.725-0800)

Can confirm in 21w07a.

### Comment 6: Avoma (2021-02-20T09:46:37.250-0800)

Video attached.

### Comment 7: Avoma (2021-10-03T03:12:41.663-0700)

Can confirm this in 21w39a. Here are some extra details regarding this problem.
The Bug:
Ender dragon heads are not activated when powered through using comparators.
Please note that if you were to toggle the comparator's mode whilst it's activated, the ender dragon head would now be powered.
Steps to Reproduce:
- Build the setup as shown in the attachment below.

- Activate the lever and watch the ender dragon's head closely.

Observed Behavior:
Ender dragon heads are not activated when powered through using comparators.
Expected Behavior:
Ender dragon heads would be activated when powered through using comparators.

### Comment 8: Avoma (2022-11-16T11:18:33.444-0800)

In 22w46a, the newly introduced piglin heads are also affected by this issue. I've altered this report to include this new information.

### Comment 9: Jeremy (2023-08-30T09:47:54.061-0700)

Fixed in 23w35a
