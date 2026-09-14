# MC-151828: Woodland mansion structure '1x1_b3' has dark oak leaf block with persistent tag set to 'false'

**Mojira URL:** [https://bugs.mojang.com/browse/MC-151828](https://bugs.mojang.com/browse/MC-151828)

## Report details

- **Mojira categories:** Structures; World generation
- **Project:** MC
- **Issue key:** MC-151828
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2019-05-14T02:24:14.228-0700
- **Updated:** 2025-04-29T08:11:17.029-0700
- **Resolution date:** 2024-07-23T01:18:46.603-0700
- **Affects versions:** Minecraft 1.14.1; Minecraft 1.14.2 Pre-Release 1; Minecraft 1.14.2 Pre-Release 2; 1.14.4; 19w45b; 1.15.1; 1.15.2; 20w12a; 20w51a; 1.16.5; 21w06a; 21w08b; 1.17.1; 1.18 Pre-release 5; 1.18.2; 1.19 Release Candidate 1; 1.19 Release Candidate 2; 1.19; 22w24a; 1.19.1; 1.19.2; 1.19.4; 1.20.1
- **Fix versions:** 24w33a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2019-05-14_17.22.08.png; MC-151828.mp4
- **Issue links:** Duplicate:inward:MC-152610:woodland mansion shortage the "dark oak leaves " on the fence in 1x1_b3 ("Single bed bedroom") | Relates:inward:MC-271137:Leaves from the Trial Chamber entrance room tree won't decay

## Description

The Bug
The dark oak leaf block with the "1x1_b3" woodland mansion structure has its persistent tag set to false. As a result of this block's persistent tag being set to false, the dark oak leaf will eventually decay.
How to Reproduce

```
/setblock ~ ~ ~ structure_block{mode:"LOAD", name:"woodland_mansion/1x1_b3"}
```
Observed Behavior
The leaf block on the small tree has the tag that'll make it decay
Expected Behavior
The dark oak leaf block with the "1x1_b3" woodland mansion structure would have its persistent tag set to true.

## Comments (18)

### Comment 1: migrated (2019-05-14T02:24:14.228-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: Avoma (2020-12-23T07:21:14.306-0800)

Can confirm in 20w51a.

### Comment 3: Avoma (2021-02-17T06:00:21.919-0800)

Can confirm in 21w06a.

### Comment 4: Avoma (2021-03-01T06:42:59.066-0800)

Can confirm in 1.16.5 and 21w08b.

### Comment 5: migrated (2021-06-02T21:26:10.893-0700)

Can confirm in 1.17-pre4.

### Comment 6: Avoma (2021-07-31T09:17:56.347-0700)

Can confirm in 1.17.1.

### Comment 7: Avoma (2021-11-22T05:02:39.942-0800)

Can confirm this behavior in 1.18 Pre-release 5. Here are some extra details regarding this problem.
The Bug:
The dark oak leaf block with the "1x1_b3" woodland mansion structure has its persistent tag set to false.
As a result of this block's persistent tag being set to false, the dark oak leaf will eventually decay.
Steps to Reproduce:
- Summon the "1x1_b3" woodland mansion structure by running the following command and powering the structure block.

```/setblock ~ ~ ~ minecraft:structure_block{mode:"LOAD",name:"woodland_mansion/1x1_b3"}```
- Enable the F3 debug screen.

- Look at the dark oak leaf block within this structure and take note of what its persistent tag is set to.

Observed Behavior:
The dark oak leaf block with the "1x1_b3" woodland mansion structure has its persistent tag set to false.
Expected Behavior:
The dark oak leaf block with the "1x1_b3" woodland mansion structure would have its persistent tag set to true.

### Comment 8: Avoma (2022-03-31T09:11:52.563-0700)

Can confirm in 1.18.2.

### Comment 9: MacchuPicchu (2022-06-02T23:33:04.925-0700)

Present in 1.19-rc1.

### Comment 10: MacchuPicchu (2022-06-03T07:32:03.993-0700)

Present in 1.19-rc2.

### Comment 11: MacchuPicchu (2022-06-16T06:01:39.699-0700)

Present in 22w24a.

### Comment 12: Avoma (2022-07-28T06:44:12.524-0700)

Can confirm in 1.19.1. This issue can now be more easily reproduced by using the "/place" command.

```/place template minecraft:woodland_mansion/1x1_b3```

### Comment 13: Avoma (2022-08-30T05:37:01.956-0700)

Can confirm in 1.19.2.

### Comment 14: MacchuPicchu (2023-03-20T17:50:57.124-0700)

Present in 1.19.4.

### Comment 15: sh20000sh (2023-06-17T06:09:51.104-0700)

Present on 1.20.1

### Comment 16: migrated (2023-06-18T00:19:33.923-0700)

wtf

### Comment 17: migrated (2023-06-18T03:10:08.642-0700)

Please only post comments if you have information to add.

### Comment 18: sh20000sh (2023-08-20T01:59:09.296-0700)

Considering its first reported version, it seems like related with 'flattening'. Decay related tag prior to this was 'decayable' and after then, it changed into 'persistent'. And tags in structure looks like hadn't touched.
