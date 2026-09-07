# MC-9644: Launched falling_block entities do not travel through portals

**Mojira URL:** [https://bugs.mojang.com/browse/MC-9644](https://bugs.mojang.com/browse/MC-9644)

## Report details

- **Mojira categories:** Entities
- **Project:** MC
- **Issue key:** MC-9644
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2013-02-11T14:55:42.265-0800
- **Updated:** 2025-04-29T09:32:51.146-0700
- **Resolution date:** 2024-05-07T04:40:19.134-0700
- **Affects versions:** Snapshot 13w06a; Minecraft 1.5; Snapshot 13w11a; Minecraft 1.5.1; Minecraft 1.5.2; Snapshot 13w18c; Snapshot 13w19a; Minecraft 1.8; Minecraft 1.8.1-pre3; Minecraft 1.10.2; Minecraft 16w42a; Minecraft 1.12.2; Minecraft 1.13-pre3; 1.15.2; 20w21a; 1.16 Release Candidate 1; 1.16; 1.16.2; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w07a; 21w08b; 21w11a; 21w15a; 21w17a; 1.17; 1.17.1; 1.19; 1.19.2; 1.19.3; 1.19.4; 1.20 Release Candidate 1; 1.20; 1.20.1; 1.20.4; 1.20.5 Release Candidate 1
- **Fix versions:** 24w19a
- **Area:** Platform
- **Labels:** falling_block; nether_portal
- **Watchers:** 1
- **Attachments:** 5
- **Attachment filenames:** 2013-02-12_00.11.16.png; 2014-11-04_12.03.30.png; 2014-11-04_12.06.43.png; MC-9644.mp4; MC-9644.png
- **Issue links:** Relates:inward:MC-8983:Primed TNT cannot travel through nether portals | Relates:inward:MC-254004:Falling Block Entities do not process their End Gateway Cooldown Timer | Duplicate:inward:MC-261829:Falling Blocks Can't Go Through Nether Portals.

## Description

I made an anvil-launching cannon with TNT and redstone.
What I expected to happen was the anvil would be sent into the nether like an arrow or other moving entity.
What actually happened was the anvil passed through the portal blocks as if they weren't there and landed on the other side.
How to reproduce
- Place a nether portal block (make sure it is not on the ground)

```
/setblock ~ ~ ~3 nether_portal
```

- Place a gravity-affected block above it

```
/setblock ~ ~2 ~3 sand
```
→  The block falls straight through the nether portal block without being transported to/from the nether

## Comments (23)

### Comment 1: migrated (2013-02-11T14:55:42.265-0800)

This comment contained multiple image attachments (5), please login to view the attachments.

### Comment 2: migrated (2013-02-11T15:14:13.359-0800)

Confirmed. Also applies to all FallingBlock entities.

### Comment 3: migrated (2014-11-04T10:10:24.907-0800)

Still an issue in version 1.8 and 1.8.1-pre3

### Comment 4: kumasasa (2015-12-06T05:55:14.024-0800)

Is this still an issue in the current Minecraft Snapshot 15w49b or later? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 5: qwerty23495 (2018-06-21T23:48:32.965-0700)

Can confirm in 1.13-pre3.

### Comment 6: migrated (2019-12-25T21:53:11.242-0800)

Still an issue in 1.15.1. Have tested with sand.

### Comment 7: j_p_smith (2020-05-25T02:09:20.861-0700)

Confirmed in 1.15.2 and 20w21a.
Steps to reproduce (much easier than the steps provided):
- Place a nether portal block (make sure it is not on the ground)

```/setblock ~ ~ ~3 nether_portal```

- Place a gravity-affected block above it

```/setblock ~ ~2 ~3 sand```
→  The block falls straight through the nether portal block without being transported to/from the Nether

### Comment 8: migrated (2020-05-25T06:43:13.197-0700)

Problem is, this issue is hard enough already because it's hard for the game to calculate where the block will land, especially with the example Jacob Smith posed.

### Comment 9: migrated (2020-06-19T09:27:37.945-0700)

Affects 1.16 Release Candidate 1

### Comment 10: migrated (2020-11-10T11:34:36.421-0800)

Affects 20w45a

### Comment 11: Avoma (2020-12-23T02:44:16.461-0800)

Can confirm in 20w51a.

### Comment 12: Avoma (2021-01-28T06:08:54.594-0800)

Can confirm in 21w03a.

### Comment 13: Avoma (2021-02-05T12:07:34.083-0800)

Can confirm in 21w05b.

### Comment 14: Avoma (2021-02-12T05:10:09.317-0800)

Can confirm in 21w06a.

### Comment 15: Avoma (2021-02-18T10:56:29.015-0800)

Can confirm in 21w07a.

### Comment 16: Avoma (2021-03-04T04:54:46.238-0800)

Can confirm in 1.16.5 and 21w08b.

### Comment 17: Avoma (2021-03-27T03:21:57.694-0700)

Can confirm in 21w11a.

### Comment 18: Avoma (2021-04-19T01:52:17.108-0700)

Can confirm in 21w15a.

### Comment 19: Avoma (2021-04-30T06:08:26.490-0700)

Can confirm in 21w17a.

### Comment 20: Avoma (2021-06-16T11:58:44.228-0700)

Can confirm in 1.17.

### Comment 21: Avoma (2021-07-18T10:46:12.493-0700)

Can confirm in 1.17.1.

### Comment 22: Avoma (2022-06-24T05:20:29.359-0700)

Can confirm in 1.19.

### Comment 23: Avoma (2022-09-14T12:17:56.231-0700)

Can confirm in 1.19.2.
