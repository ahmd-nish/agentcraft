# MC-254074: Frogs don't play their walking animation when they take damage

**Mojira URL:** [https://bugs.mojang.com/browse/MC-254074](https://bugs.mojang.com/browse/MC-254074)

## Report details

- **Mojira categories:** Mob behaviour; Parity
- **Project:** MC
- **Issue key:** MC-254074
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2022-07-10T05:38:30.628-0700
- **Updated:** 2025-04-30T05:31:54.651-0700
- **Resolution date:** 2023-02-15T09:42:31.205-0800
- **Affects versions:** 1.19; 1.19.1 Pre-release 4; 1.19.1 Release Candidate 2; 1.19.1; 1.19.2; 22w42a; 22w44a; 1.19.3 Pre-release 1; 1.19.3 Pre-release 2; 1.19.3 Pre-release 3; 1.19.3 Release Candidate 1; 1.19.3 Release Candidate 3; 1.19.3; 23w04a
- **Fix versions:** 23w05a
- **Area:** Gameplay
- **Labels:** frog; vanilla-parity
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** Minecraft Preview 2022-07-10 14-48-30.mp4
- **Issue links:** Relates:outward:MC-260081:Sniffers don't play their walking animations when they are damaged | Relates:inward:MC-256479:Camels don't play their walking animations when they are damaged

## Description

Summary:
Compared to other mobs, frogs do not play the walking animation when they take damage. This is also a parity issue, as there is no such issue in bedrock (since version 1.19.10.23 when adding damage animation to mobs https://twitter.com/atorstling/status/1534525221155348480?t=lwhc9b9at9ZSgzm36Bt45A&s=09)
Steps to reproduce:
- Place a magma block to prevent the frog from walking.

- Summon a frog on him.

- Watch the frog take damage.

Observed results:
When taking damage, the frog does not play the walking animation like other mobs.
Expected results:
When taking damage, the frog plays a walking animation like other mobs.
Video:
Bedrock

## Comments (11)

### Comment 1: migrated (2022-07-10T05:38:30.628-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: Avoma (2022-07-20T11:11:41.598-0700)

I can confirm this behavior.

### Comment 3: Avoma (2022-07-27T10:46:48.308-0700)

Can confirm in 1.19.1.

### Comment 4: Avoma (2022-08-11T03:45:38.079-0700)

Can confirm in 1.19.2.

### Comment 5: Tanuki_Bakero (2022-10-25T03:52:25.474-0700)

Confirmed with 22w42a

### Comment 6: Tanuki_Bakero (2022-11-05T09:47:27.865-0700)

Confirmed with 22w44a

### Comment 7: Tanuki_Bakero (2022-11-25T14:04:29.445-0800)

Confirmed with 1.19.3 Pre-release 2

### Comment 8: Tanuki_Bakero (2022-11-30T07:47:51.573-0800)

Confirmed with 1.19.3 Pre-release 3

### Comment 9: Tanuki_Bakero (2022-12-01T13:08:32.933-0800)

Confirmed with 1.19.3 Release Candidate 1

### Comment 10: Tanuki_Bakero (2022-12-06T14:07:02.548-0800)

Confirmed with 1.19.3 Release Candidate 3

### Comment 11: Tanuki_Bakero (2023-01-29T06:10:51.608-0800)

Confirmed with 23w04a
