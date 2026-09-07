# MC-239344: All torches in mineshafts are facing the wrong way

**Mojira URL:** [https://bugs.mojang.com/browse/MC-239344](https://bugs.mojang.com/browse/MC-239344)

## Report details

- **Mojira categories:** Structures; World generation
- **Project:** MC
- **Issue key:** MC-239344
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-10-19T11:20:21.104-0700
- **Updated:** 2025-04-29T21:40:09.357-0700
- **Resolution date:** 2021-11-02T05:04:48.394-0700
- **Affects versions:** 21w41a; 21w42a; 21w43a
- **Fix versions:** 21w44a
- **Watchers:** 1
- **Attachments:** 10
- **Attachment filenames:** 2021-10-19_19.59.07.png; 2021-10-19_19.59.30.png; 2021-10-19_19.59.40.png; 2021-10-19_20.00.01.png; 2021-10-19_20.00.23.png; 2021-10-19_20.00.43.png; 2021-10-19_20.01.06.png; 2021-10-19_20.01.17.png; Expected.png; unexpected.png

## Description

Note: This has been unreported for a long time and it's probably the real reason for MC-216561 as unless there happens to be a random block behind the torch it won't generate making torches rarer. Also could possibly be the reason for MC-216432
Bug Description: This is probably a recurrence of MC-124966, all torches in mineshafts are now facing the wrong way. This apart from being a bug in of itself probably makes torches rarer as those won't generate unless they happen to have a random supporting block generate. I also do not know the first version this started to occur in.
Expected Behaviour:
All torches in mineshafts generate attached to the wooden support pillars
Observed Behaviour:
All torches generate rotated 180* in the other direction
How to reproduce:
Locate any mineshaft structure (it doesn't matter whether it's above or below y0) and find any torches you will find that all of them are rotated

## Comments (8)

### Comment 1: migrated (2021-10-19T11:20:21.104-0700)

This comment contained multiple image attachments (10), please login to view the attachments.

### Comment 2: ampolive (2021-10-19T11:41:13.381-0700)

Isn't this the same issue as MC-200494?

### Comment 3: Ceresjanin123 (2021-10-19T12:24:06.203-0700)

Well no this is about all torches being rotated 180 degrees but because of MC-200494 they can attach to other blocks after they're rotated

### Comment 4: migrated (2021-10-19T12:39:47.516-0700)

So are there any instances of the torch being rotated without a block there? If not, I'd say it's the same bug in the code.

### Comment 5: Ceresjanin123 (2021-10-19T13:47:59.230-0700)

well because of the fix to MC-124966 they can't

### Comment 6: migrated (2021-10-19T14:54:33.392-0700)

Then it is the same issue, you just found the direct source (it being the wrong facing state), and that information should be added to the other report.

### Comment 7: migrated (2021-10-27T06:57:49.947-0700)

Can confirm, also since this report has found the source of the bug it should become the parent report

### Comment 8: ampolive (2021-10-30T15:12:54.818-0700)

Can confirm. Relates to MC-200494, MC-216432 and MC-216561.
