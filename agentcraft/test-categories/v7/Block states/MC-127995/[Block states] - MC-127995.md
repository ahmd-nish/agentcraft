# MC-127995: You can use bone meal on sea pickles in situations where no sea pickles will grow

**Mojira URL:** [https://bugs.mojang.com/browse/MC-127995](https://bugs.mojang.com/browse/MC-127995)

## Report details

- **Mojira categories:** Block states
- **Project:** MC
- **Issue key:** MC-127995
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2018-04-05T08:39:14.407-0700
- **Updated:** 2025-04-26T06:28:32.006-0700
- **Resolution date:** 2024-08-24T01:19:56.344-0700
- **Affects versions:** Minecraft 18w14b; Minecraft 1.13.1-pre2; Minecraft 1.13.1; 1.14.4; 19w37a; 1.15.1; 20w21a; 1.16 Pre-release 8; 20w28a; 1.16.2 Pre-release 1; 1.16.3; 1.16.4; 20w51a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w16a; 21w18a; 21w19a; 1.17 Pre-release 2; 1.17; 1.17.1; 21w41a; 21w44a; 1.18.1; 1.18.2; 22w18a; 1.19; 1.19.2; 1.19.3; 23w03a; 1.19.4; 23w18a; 1.20 Pre-release 1; 1.20.1
- **Fix versions:** 24w33a
- **Area:** Gameplay
- **Labels:** bone_meal; sea_pickle
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-127995.mp4; MC-127995.png
- **Issue links:** Relates:outward:MC-261423:Pitcher pod crop with a block on top consumes bone meal despite being unable to grow | Duplicate:inward:MC-226962:Bone meal can be used on sea pickle that has the maximum space | Duplicate:inward:MC-224995:Sea Pickels will use bone meal underwater without doing anything. | Duplicate:inward:MC-218922:Sea Pickle uses Bonemeal when not on Coral Block | Duplicate:inward:MC-201486:sea pickle growth

## Description

The Bug
This works both inside and outside of water. It doesn't actually do anything (except showing some fancy particles), even though the bone meal is used up if you are in survival mode.
Steps to Reproduce
-     Place down a singular sea pickle on some dry land.

-     Obtain some bone meal and apply several amounts of it to the sea pickle.

-     Take note as to whether or not you can apply bone meal to sea pickles in situations where they cannot grow.

Observed Behavior
You can apply bone meal to sea pickles in situations where they cannot grow.
Expected Behavior
You would not be able to apply bone meal to sea pickles in situations where they cannot grow.
Code Analysis
Code analysis by  can be found in this comment.

## Comments (23)

### Comment 1: migrated (2018-04-05T08:39:14.407-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: CreeperMagnet_ (2018-04-05T15:28:49.572-0700)

They actually will grow, but only when they're on coral, and only inside water. Might want to add that to the issue, as bone meal shouldn't be able to be used outside of those conditions.
EDIT: They can also be grown inside flowing water, which is probably also a bug.

### Comment 3: migrated (2018-08-20T12:48:02.587-0700)

Affects 1.13.1-pre2.

### Comment 4: Avoma (2020-12-18T10:42:58.758-0800)

Can confirm in 20w51a.

### Comment 5: Avoma (2021-01-20T10:39:33.930-0800)

Can confirm in 21w03a.

### Comment 6: Avoma (2021-02-04T04:51:42.066-0800)

Can confirm in 21w05a.

### Comment 7: Avoma (2021-02-05T02:51:02.591-0800)

Can confirm in 21w05b.

### Comment 8: Avoma (2021-02-11T07:48:29.093-0800)

Can confirm in 21w06a.

### Comment 9: Avoma (2021-02-18T05:12:59.365-0800)

Can confirm in 21w07a.

### Comment 10: Avoma (2021-04-26T10:19:12.884-0700)

Can confirm in 21w16a.

### Comment 11: migrated (2021-05-14T12:00:02.699-0700)

Can confirm in 21w19a

### Comment 12: Avoma (2021-06-26T09:21:17.162-0700)

Can confirm in 1.17.

### Comment 13: ampolive (2021-08-08T15:11:21.363-0700)

Can confirm in 1.17.1.

### Comment 14: Avoma (2021-10-19T01:03:49.830-0700)

I am able to confirm this behavior in 21w41a. Here are some extra details regarding this problem.
The Bug:
You can apply bone meal to sea pickles in situations where they cannot grow.
Steps to Reproduce:
- Place down a singular sea pickle on some dry land.

- Obtain some bone meal and apply several amounts of it to the sea pickle.

- Take note as to whether or not you can apply bone meal to sea pickles in situations where they cannot grow.

Observed Behavior:
You can apply bone meal to sea pickles in situations where they cannot grow.
Expected Behavior:
You would not be able to apply bone meal to sea pickles in situations where they cannot grow.

### Comment 15: shufboyardee (2021-11-10T23:26:03.517-0800)

Can confirm in 21w44a.

### Comment 16: Avoma (2021-12-11T05:28:32.839-0800)

Can confirm in 1.18.1.

### Comment 17: Avoma (2022-03-07T08:34:50.410-0800)

Can confirm in 1.18.2.

### Comment 18: Avoma (2022-05-05T09:20:39.491-0700)

Can confirm in 22w18a. Here's a code analysis of this issue.
Code Analysis:
The following is based on a decompiled version of Minecraft 1.18.2 using MCP-Reborn.
net.minecraft.world.level.block.SeaPickleBlock.java

```public class SeaPickleBlock extends BushBlock implements BonemealableBlock, SimpleWaterloggedBlock {
   ...
   public boolean isValidBonemealTarget(BlockGetter $bg, BlockPos $bp, BlockState $bs, boolean $b) {
      return true;
   }
   ...```
If we look at the above class, we can see that the isValidBonemealTarget() boolean always returns "turn" for sea pickles regardless of any circumstances. This means that they can always have bone meal applied to them.

### Comment 19: Avoma (2022-06-30T09:13:56.315-0700)

Can confirm in 1.19.

### Comment 20: Avoma (2022-08-07T06:07:12.059-0700)

Can confirm in 1.19.2.

### Comment 21: Brain81505 (2023-01-18T03:11:17.209-0800)

Can confirm in 1.19.3

### Comment 22: windwend (2023-01-20T21:01:03.032-0800)

Can confirm in 23w03a.

### Comment 23: shufboyardee (2023-05-12T15:38:09.373-0700)

can confirm in 1.20 Pre-release 1.
