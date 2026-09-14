# MC-96198: Boats / rafts move into blocks when landing in less than one block deep water

**Mojira URL:** [https://bugs.mojang.com/browse/MC-96198](https://bugs.mojang.com/browse/MC-96198)

## Report details

- **Mojira categories:** Collision
- **Project:** MC
- **Issue key:** MC-96198
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2016-01-28T08:34:35.715-0800
- **Updated:** 2025-10-15T01:48:08.178-0700
- **Resolution date:** 2024-05-07T04:40:21.412-0700
- **Affects versions:** Minecraft 16w04a; Minecraft 16w05b; Minecraft 16w06a; Minecraft 1.9 Pre-Release 1; Minecraft 1.9 Pre-Release 2; Minecraft 1.10.2; Minecraft 1.11; Minecraft 1.11.2; Minecraft 1.12 Pre-Release 6; Minecraft 1.12 Pre-Release 7; Minecraft 1.12.2; Minecraft 18w05a; Minecraft 1.14; Minecraft 1.14.1; 20w14a; 1.16.1; 20w28a; 1.16.3; 1.16.4; 20w46a; 20w48a; 21w05b; 21w06a; 21w13a; 1.17 Pre-release 1; 1.17; 1.17.1; 1.18; 1.18.1; 1.18.2; 1.19 Pre-release 3; 1.19 Release Candidate 2; 1.19; 1.19.1 Pre-release 5; 1.19.2; 22w42a; 22w45a; 1.19.3; 1.20; 1.20.1; 23w44a
- **Fix versions:** 24w19a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2016-01-28_17.23.14.png; 2016-01-29_20.30.04.png; boat.mp4; boatClipHeights.mp4
- **Issue links:** Duplicate:inward:MC-96382:Boat sinking into ground from water_bucket flow | Duplicate:inward:MC-104599:Boats Fall Through The Floor | Duplicate:inward:MC-128546:boat glitch when going too fast | Duplicate:inward:MC-151870:Boats can clip through blocks when falling into flowing-water | Duplicate:inward:MC-177486:boats glitch in the ground when falling into flowing water | Duplicate:inward:MC-197353:Boat slid into ground after dismounting | Duplicate:inward:MC-201953:Boats can fall through blocks when pushed into flowing water | Duplicate:inward:MC-214961:Boat falls through the floor on certain turns | Duplicate:inward:MC-215403:The player sunk into the ground while boating in a cave | Duplicate:inward:MC-222097:sinking boat | Duplicate:inward:MC-226801:Sometimes riding a boat in flowing water causes you to get stuck in blocks for a moment | Duplicate:inward:MC-229766:Boat sinks through blocks | Duplicate:inward:MC-230069:Boat getting stuck | Duplicate:inward:MC-234154:Boat able to phase through blocks | Duplicate:inward:MC-244101:Boat when placed on water went into the ground | Duplicate:inward:MC-246979:cats in boat in flowing water descend into block below and suffocate | Duplicate:inward:MC-249024:Boat disappears when on water above soul sand | Duplicate:inward:MC-251769:Boat Sinks in falling flowing water | Duplicate:inward:MC-252322:Boats clip through blocks | Duplicate:inward:MC-252746:Sinking through block when on a boat | Duplicate:inward:MC-253700:the boat gets stuck in blocks | Duplicate:inward:MC-253981:Glitch with boat and flowing water | Duplicate:inward:MC-254233:Oak Boat with Chest sinks under the water while you are on fire. | Duplicate:inward:MC-256565:Bamboo Raft Clipping through blocks under flowing water stream | Duplicate:inward:MC-256676:New bug in 1.19.3 snapshot | Duplicate:inward:MC-257274:Boats move through solid floor if falling onto shallow water | Duplicate:inward:MC-257568:Boat adios in 13 cm deep water (falls through blocks) | Duplicate:inward:MC-258764:Boats become unable to move and will sink into the ground if you drive it from plane of water. It will not sink into the ground untill you leave the boat. | Duplicate:inward:MC-263380:The boat sinks when it encounters downward flowing water and cannot be ridden | Duplicate:inward:MC-263572:boat glitch in ground | Duplicate:inward:MC-264435:Boats go thru floor | Duplicate:inward:MC-266381:The ship got stuck in the soil | Relates:inward:MC-122493:Boats fall through blocks when slightly intersecting with water | Duplicate:inward:MC-265256:The boat sinks when it encounters downward flowing water and cannot be ridden

## Description

The bug
A boat will glitch / sink through blocks when it falls onto shallow water (see screenshot for setup to reproduce glitch or 3 Glitches with Boats- 1.12 Vanilla Survival)
How to reproduce
- Grab a boat

- Create setup shown in screenshot

- Speed up using 'W' and move towards the waterfall. once you fall on the floor below, you will sink/glitch through the ground, as shown in the video here: https://www.youtube.com/watch?v=Q8mtxsNCOAE

Code analysis
Based on 1.12.2 decompiled using MCP 9.40
It appears the call to Entity.setPosition(double, double, double) in the method net.minecraft.entity.item.EntityBoat.updateMotion() is causing this:

```
if (this.previousStatus == EntityBoat.Status.IN_AIR && this.status != EntityBoat.Status.IN_AIR && this.status != EntityBoat.Status.ON_LAND)
{
    this.waterLevel = this.getEntityBoundingBox().minY + (double)this.height;
    // The following line appears to be causing the bug
    this.setPosition(this.posX, (double)(this.getWaterLevelAbove() - this.height) + 0.101D, this.posZ);
    this.motionY = 0.0D;
    this.lastYd = 0.0D;
    this.status = EntityBoat.Status.IN_WATER;
}
```
It is unknown if leaving this out solves this bug without causing any other problems.

## Comments (23)

### Comment 1: migrated (2016-01-28T08:34:35.715-0800)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: migrated (2016-01-28T08:39:13.134-0800)

cannot confirm

### Comment 3: AgentM (2016-01-28T12:44:49.678-0800)

Tell me what the issue was for reproducing it @FVbico
Were you in the latest snapshot.
Try going at full speed and use F5 mode for optimal setup. (Reference the video if needed)

### Comment 4: migrated (2016-01-28T13:45:12.837-0800)

I was and I was, it just didn't happen to me

### Comment 5: migrated (2016-01-29T17:48:47.009-0800)

I was able to reproduce it. (16w04a)
1.	Launch the boat off the upper level of water.
2.	Keep holding “W” until landing in the lower flowing water.

### Comment 6: migrated (2016-06-25T06:47:03.651-0700)

Was able to reproduce in this video: https://www.youtube.com/watch?v=4FNCWE3xgL4

### Comment 7: migrated (2016-11-19T15:29:27.996-0800)

Can confirm for 1.11

### Comment 8: migrated (2018-08-24T03:10:35.105-0700)

This issue relates to MC-136358 and .

### Comment 9: migrated (2018-09-15T17:29:02.595-0700)

I don't seem to be able to reproduce in 1.13.1; instead of sinking through the floor, the boat glitches above the water flow repeatedly.

### Comment 10: migrated (2019-05-02T03:26:39.393-0700)

Surprisingly, I can reproduce now! Confirmed for 1.14.

### Comment 11: j_p_smith (2020-06-29T12:40:07.190-0700)

Confirmed in 1.16.1.

### Comment 12: Avoma (2020-11-26T11:06:43.207-0800)

Can confirm in 20w48a.

### Comment 13: Avoma (2021-02-07T02:32:10.706-0800)

Can confirm in 21w05b.

### Comment 14: Nassim Jahnke (2021-08-10T03:41:08.701-0700)

Still an issue in 1.17.1. As already stated, the issue stems from the following call in Boat#floatBoat

```this.setPos(this.getX(), (double) (this.getWaterLevelAbove() - this.getBbHeight()) + 0.101D, this.getZ());```
where you get the following values if placing a boat at feet height y=64 for example

```getWaterLevelAbove() = 64.44444
getBbHeight() = 0.5625
(double) (this.getWaterLevelAbove() - this.getBbHeight()) + 0.101D = 63.98294274902344```
This video shows where this can also be abused to clip through a bedrock layer, player bases and similar.

### Comment 15: Avoma (2021-12-29T04:25:02.884-0800)

Can confirm in 1.18.1. It's important to note that this can be reproduced without boats needing to fall from high places into water.

### Comment 16: Qcom (2022-05-12T13:07:58.771-0700)

This can also be reproduced by placing a boat in the corner of a minimum height flowing water block between heights 8 to 63.

### Comment 17: migrated (2022-05-29T07:39:18.798-0700)

Can confirm the bug is still in 1.19 prerelease3

### Comment 18: migrated (2022-06-05T14:47:08.302-0700)

Can confirm in 1.19-rc2

### Comment 19: Avoma (2022-10-19T09:24:17.723-0700)

Can confirm in 22w42a. This now also affects bamboo rafts.

### Comment 20: Avoma (2022-10-22T10:53:28.278-0700)

Can confirm in 1.19.2.

### Comment 21: Lunarian (2023-06-16T05:03:06.836-0700)

Can confirm in 1.20.1 per MC-263572.

### Comment 22: Ellivers (2023-12-11T13:37:30.443-0800)

Can confirm in 1.20.4.

### Comment 23: migrated (2024-03-25T22:22:05.946-0700)

can't believe this bug is 8 years old
