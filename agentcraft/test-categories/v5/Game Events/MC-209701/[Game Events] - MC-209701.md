# MC-209701: Sculk sensors are not activated upon placing food onto campfires

**Mojira URL:** [https://bugs.mojang.com/browse/MC-209701](https://bugs.mojang.com/browse/MC-209701)

## Report details

- **Mojira categories:** Game Events
- **Project:** MC
- **Issue key:** MC-209701
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2020-12-27T04:44:23.391-0800
- **Updated:** 2025-03-25T12:31:11.613-0700
- **Resolution date:** 2022-05-23T06:04:23.362-0700
- **Affects versions:** 20w51a; 21w03a; 21w05a; 21w05b; 21w06a; 21w07a; 21w08b; 21w10a; 21w14a; 21w15a; 21w17a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17 Pre-release 3; 1.17 Pre-release 5; 1.17 Release Candidate 1; 1.17 Release Candidate 2; 1.17; 1.17.1 Pre-release 1; 1.17.1 Pre-release 3; 1.17.1; 21w38a; 21w41a; 21w43a; 1.18; 1.18.1; 22w05a; 1.18.2; 22w14a; 22w17a; 22w18a; 1.19 Pre-release 1
- **Fix versions:** 1.19 Pre-release 2
- **Labels:** sculk_sensor
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-209701.mp4; MC-209701.png

## Description

The Bug:
Sculk sensors are not activated upon placing food onto campfires.
Steps to Reproduce:
- Place down a campfire.

- Place down a sculk sensor nearby and place some food onto the campfire.

- Take note as to whether or not sculk sensors are activated upon placing food onto campfires.

Observed Behavior:
Sculk sensors are not activated upon placing food onto campfires.
Expected Behavior:
Sculk sensors would be activated upon placing food onto campfires.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.18.2 using MCP-Reborn.
net.minecraft.world.level.block.CampfireBlock.java

```
public class CampfireBlock extends BaseEntityBlock implements SimpleWaterloggedBlock {
   ...
   public InteractionResult use(BlockState $bs, Level $l, BlockPos $bp, Player $p, InteractionHand $ih, BlockHitResult $bhr) {
      BlockEntity blockentity = $l.getBlockEntity($bp);
      if (blockentity instanceof CampfireBlockEntity) {
         CampfireBlockEntity campfireblockentity = (CampfireBlockEntity)blockentity;
         ItemStack itemstack = $p.getItemInHand($ih);
         Optional<CampfireCookingRecipe> optional = campfireblockentity.getCookableRecipe(itemstack);
         if (optional.isPresent()) {
            if (!$l.isClientSide && campfireblockentity.placeFood($p.getAbilities().instabuild ? itemstack.copy() : itemstack, optional.get().getCookingTime())) {
               $p.awardStat(Stats.INTERACT_WITH_CAMPFIRE);
               return InteractionResult.SUCCESS;
            }
            ...
```
If we look at the above class, we can see that placing food onto campfires simply isn't registered as a game event as the gameEvent() method is never called, thus not detecting this action as a vibration.
Potential Fix:
Simply calling the gameEvent() method where appropriate within this piece of code should resolve this problem. The "BLOCK_CHANGE" game event tag would be expected to be used here as campfires are visually changed when food is placed onto them. The following line of code could be used in order to fix this:

```
$LEVEL.gameEvent($PLAYER, GameEvent.BLOCK_CHANGE, $BLOCKPOS);
```

## Comments (2)

### Comment 1: migrated (2020-12-27T04:44:23.391-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: migrated (2020-12-27T08:20:09.560-0800)

Can confirm. Affects both regular and soul campfires.
