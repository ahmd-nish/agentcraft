# MC-212036: Hand animation still plays when 7 blocks under a boat

**Mojira URL:** [https://bugs.mojang.com/browse/MC-212036](https://bugs.mojang.com/browse/MC-212036)

## Report details

- **Mojira categories:** Player Animation
- **Project:** MC
- **Issue key:** MC-212036
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2021-01-19T17:22:38.128-0800
- **Updated:** 2025-03-25T13:23:37.382-0700
- **Resolution date:** 2022-07-05T12:51:11.529-0700
- **Affects versions:** 20w28a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w07a; 21w08b; 21w14a; 21w15a; 21w16a; 21w17a; 1.17; 1.17.1; 21w42a; 1.18.1; 1.18.2
- **Fix versions:** 22w11a
- **Labels:** hand-animation
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2021-01-19_18.22.25.png; MC-212036.mp4; MC-212036 - 1.18.2.png; MC-212036 - 22w11a (Fixed).png

## Description

The Bug
The hand animation still plays when right clicking under a boat 7 blocks away
Reproduce
-     Switch into creative mode and summon a boat above your head

```
/summon minecraft:boat ~ ~6.5 ~ {NoGravity:1b}
```

-     Attempt to ride the boat by right-clicking on it

-     Take note as to whether or not the hand animation plays when attempting to interact with the boat despite it being too far away

Observed Result
The hand animation plays when attempting to interact with boats despite them being too far away.
Expected Result
The hand animation would not play when attempting to interact with boats that are too far away.

## Comments (17)

### Comment 1: migrated (2021-01-19T17:22:38.128-0800)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: Avoma (2021-01-20T01:16:35.379-0800)

Can confirm.

### Comment 3: Avoma (2021-01-21T07:32:15.160-0800)

Can confirm in 21w03a.

### Comment 4: Avoma (2021-02-05T05:29:40.866-0800)

Can confirm in 21w05b.

### Comment 5: Avoma (2021-02-12T09:45:39.557-0800)

Can confirm in 21w06a.

### Comment 6: Avoma (2021-02-20T12:46:05.753-0800)

Can confirm in 21w07a. Here are some steps to reproduce this issue:
Steps to Reproduce:
- Go into creative mode.

- Run the following command:

```/summon minecraft:boat ~ ~6.5 ~ {NoGravity:1b}```
→  Notice how the hand animation plays, despite the player not entering the boat.

### Comment 7: Avoma (2021-02-21T03:49:55.589-0800)

Can confirm in 1.16.5.

### Comment 8: Avoma (2021-04-09T03:24:03.624-0700)

Can confirm in 21w14a. Relates to .

### Comment 9: Avoma (2021-04-19T03:52:06.852-0700)

Can confirm in 21w15a. Video attached.

### Comment 10: Avoma (2021-04-24T06:48:31.549-0700)

Can confirm in 21w16a.

### Comment 11: Avoma (2021-04-28T10:22:11.700-0700)

Can confirm in 21w17a.

### Comment 12: Avoma (2021-06-10T03:10:14.082-0700)

Can confirm in 1.17.

### Comment 13: Avoma (2021-09-03T09:39:07.035-0700)

Can confirm in 1.17.1.

### Comment 14: Avoma (2021-10-27T02:14:17.994-0700)

Can confirm this behavior in 21w42a. Here are some extra details regarding this problem.
The Bug:
The hand animation plays when attempting to interact with boats despite them being too far away.
Steps to Reproduce:
- Switch into creative mode and summon a boat above your head.

```/summon minecraft:boat ~ ~6.5 ~ {NoGravity:1b}```
- Attempt to ride the boat by right-clicking on it.

- Take note as to whether or not the hand animation plays when attempting to interact with the boat despite it being too far away.

Observed Behavior:
The hand animation plays when attempting to interact with boats despite them being too far away.
Expected Behavior:
The hand animation would not play when attempting to interact with boats that are too far away.

### Comment 15: Avoma (2021-12-28T09:51:15.426-0800)

Can confirm in 1.18.1.

### Comment 16: Avoma (2022-03-09T11:41:24.142-0800)

Can confirm in 1.18.2.

### Comment 17: Avoma (2022-06-17T11:39:10.296-0700)

This issue was present in 1.18.2, but no longer occurs in versions above or equal to 22w11a. With that being said, this issue has been fixed in 22w11a. To reinforce my claims, I've attached two screenshots demonstrating the difference in behavior between versions.
