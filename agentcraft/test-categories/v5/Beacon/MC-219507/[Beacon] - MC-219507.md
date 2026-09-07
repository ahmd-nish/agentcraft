# MC-219507: Beacon's power reverts back to previous one on world reload

**Mojira URL:** [https://bugs.mojang.com/browse/MC-219507](https://bugs.mojang.com/browse/MC-219507)

## Report details

- **Mojira categories:** Beacon
- **Project:** MC
- **Issue key:** MC-219507
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2021-03-14T07:01:43.231-0700
- **Updated:** 2025-04-29T20:32:39.050-0700
- **Resolution date:** 2021-12-24T22:14:51.257-0800
- **Affects versions:** 21w10a; 21w11a; 21w13a; 21w14a; 21w15a; 21w16a; 21w17a; 21w18a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17 Pre-release 2; 1.17 Pre-release 3; 1.17; 1.17.1; 21w38a; 1.18 Pre-release 5; 1.18 Release Candidate 1; 1.18 Release Candidate 3; 1.18
- **Fix versions:** 1.18.1 Pre-release 1
- **Labels:** beacon; beacon-pyramid; chunk-border
- **Watchers:** 1
- **Attachments:** 5
- **Attachment filenames:** 0.png; 1.png; 2.png; 20210520.png; 20210609.png

## Description

The beacon's power will back to the previous one (or not selected) after reloading the game if its pyramid was set on chunk borders. The change of power cannot appeared.
Reproduce:
I made a video that we can know it clearer and easier to reproduce this issue. Its size was too large, so I post it on https://www.bilibili.com/video/BV1kq4y1D7T6 .
- Put 9 available golden blocks (or iron blocks, diamond blocks, netherite blocks, emerald blocks) on the chunk border, then put a beacon.

- Select power Speed.

- Reload the game, select power Haste.

- Reload the game again, the power is still Speed.

Also you can see that the subscribe shows "Beacon activates" after reloading the game. ← This is probably another issue, but I just put it here.
I created a new world, there're still problems.

## Comments (7)

### Comment 1: migrated (2021-03-14T07:01:43.231-0700)

This comment contained multiple image attachments (5), please login to view the attachments.

### Comment 2: Avoma (2021-07-30T07:23:31.911-0700)

I can't seem to reproduce this issue in 1.17.1. Please provide a video of this issue occurring whilst the F3 debug screen is enabled.

### Comment 3: KeqiaoNana (2021-07-30T09:29:16.023-0700)

I made a video now. which reproduced the issue. About 2 minutes.

### Comment 4: anthony cicinelli (2021-11-18T07:59:46.368-0800)

There is no issue here. Your switching your main effects. You can only have 1 primary effect and a secondary effects

### Comment 5: KeqiaoNana (2021-11-18T08:41:38.550-0800)

Well, To my surprise, this problem didn't happen in those latest snapshot versions such as 1.18 pre-4. Not sure which version repaired it surprisingly. But this problem really happened in 1.16.5 and 1.17.1.
I tested it in 1.18 pre-4 and 1.17.1 just now using random worlds. 1.17.1 can reproduce this problem, but 1.18 pre-4 can't.

### Comment 6: [Mod] violine1101 (2021-11-21T11:09:08.117-0800)

I'm able to confirm that this is in fact still happening in 1.18-pre5.

### Comment 7: boq (2021-11-29T02:24:31.473-0800)

It does not seem that being on chunk border is required - all that matters is if there was any other block change in the same chunk as beacon after power update.
Also, beacons taking some time to activate after reload is not an issue - they are supposed to work like that.
