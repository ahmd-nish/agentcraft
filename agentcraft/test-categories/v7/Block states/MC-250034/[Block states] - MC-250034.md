# MC-250034: Standing on top of mud as it converts to clay causes the player to fall through or be pushed out of the block

**Mojira URL:** [https://bugs.mojang.com/browse/MC-250034](https://bugs.mojang.com/browse/MC-250034)

## Report details

- **Mojira categories:** Block states
- **Project:** MC
- **Issue key:** MC-250034
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2022-04-08T07:43:51.918-0700
- **Updated:** 2025-04-11T12:42:08.208-0700
- **Resolution date:** 2022-11-06T06:02:50.319-0800
- **Affects versions:** 22w14a; 22w15a; 22w16b; 22w18a; 1.19 Pre-release 3
- **Fix versions:** 1.19 Pre-release 5
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** 2022-04-08_15.39.09.png; 2022-04-08_15.39.13.png; 2022-04-08_15.39.14.png; 2022-04-08_15.40.54.png; MC-250034.mp4; MC-250034.png
- **Issue links:** Relates:outward:MC-104259:Player / mob stuck on farmland while it changes to dirt

## Description

Relates to
The bug
If the player (or probably any other entity) is standing on top of a mud block as soon as that mud block becomes clay via the dripstone mechanic, the player will fall into the clay block. If there are no blocks around that clay block, this can additionally cause them to be pushed out of it sideways.
How to reproduce
- Place mud

- Place a block below the mud

- Place a stalactite below the block

- Stand on the mud

- Wait or set randomTickSpeed to a high value

Expected results
As the mud converts to clay, the player would be moved upwards slightly to accommodate the clay block's hitbox, as is done for farmland that becomes dirt.
Actual results
The player is not moved upwards and falls into the clay as a result.
Code analysis
Code analysis by  can be found in this comment.

## Comments (3)

### Comment 1: migrated (2022-04-08T07:43:51.918-0700)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: Avoma (2022-04-27T00:45:21.727-0700)

Can confirm in 22w16b. This could be fixed by calling the pushEntitiesUp() method where appropriate, just like how farmland does when it converts to dirt to avoid entities standing on top of it from "falling" into the ground.

### Comment 3: Avoma (2022-05-25T07:55:17.347-0700)

I can confirm this behavior in 1.19 Pre-release 3. Here's a code analysis regarding this issue.
Code Analysis:
The following is based on a decompiled version of Minecraft 1.19 Pre-release 3 using Mojang mappings.
net.minecraft.world.level.block.PointedDripstoneBlock.java

```public class PointedDripstoneBlock extends Block implements Fallable, SimpleWaterloggedBlock {
   ...
   public static void maybeTransferFluid(BlockState blockState, ServerLevel serverLevel, BlockPos blockPos, float f) {
      ...
      Optional<FluidInfo> optional = PointedDripstoneBlock.getFluidAboveStalactite(serverLevel, blockPos, blockState);
      ...
      if (optional.get().sourceState.is(Blocks.MUD) && fluid == Fluids.WATER) {
         BlockState blockState2 = Blocks.CLAY.defaultBlockState();
         serverLevel.setBlockAndUpdate(optional.get().pos, blockState2);
         serverLevel.gameEvent(GameEvent.BLOCK_CHANGE, optional.get().pos, GameEvent.Context.of(blockState2));
         serverLevel.levelEvent(1504, blockPos2, 0);
         return;
      }
      ...```
If we look at the above class, we can see that when mud converts into clay, the pushEntitiesUp() method (a method responsible for pushing entities upwards) is never called throughout the piece of code, resulting in entities sinking into blocks shortly after mud converts into clay.
