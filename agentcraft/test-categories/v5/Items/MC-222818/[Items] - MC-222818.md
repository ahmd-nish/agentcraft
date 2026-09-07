# MC-222818: You can ignite TNT in Adventure mode

**Mojira URL:** [https://bugs.mojang.com/browse/MC-222818](https://bugs.mojang.com/browse/MC-222818)

## Report details

- **Mojira categories:** Items; Player
- **Project:** MC
- **Issue key:** MC-222818
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-04-09T11:43:52.578-0700
- **Updated:** 2026-06-17T00:33:45.236-0700
- **Resolution date:** 2026-06-17T00:33:45.148-0700
- **Affects versions:** 1.16.5; 21w14a; 21w15a; 21w16a; 21w17a; 21w18a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17 Pre-release 3; 1.17 Pre-release 4; 1.17 Pre-release 5; 1.17 Release Candidate 1; 1.17 Release Candidate 2; 1.17; 1.17.1 Pre-release 1; 1.17.1 Pre-release 2; 1.17.1 Release Candidate 1; 1.17.1; 21w37a; 21w43a; 1.18; 1.18.1; 22w05a; 22w06a; 1.18.2; 1.19; 1.19.2; 22w43a; 1.19.3; 1.19.4; 1.20.1; 24w20a; 1.21; 1.21.3; 1.21.4; 1.21.7
- **Fix versions:** Future Update
- **Area:** Platform HC
- **Game mode:** Adventure
- **Labels:** tnt
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2021-04-12_09.12.13.png; MC-222818.mp4; MC-222818 - Current Code.png; MC-222818 - Fixed Code.png
- **Issue links:** Relates:outward:MC-255140:Cake can be eaten in adventure mode

## Description

The Bug:
You can ignite TNT in adventure mode.
This behavior is inconsistent as the player cannot ignite candles or campfires in adventure mode, so one would expect the same behavior for TNT.
Steps to Reproduce:
- Obtain some flint and steel, place down some TNT, and switch into adventure mode.

- Attempt to ignite the TNT using the flint and steel.

- Take note as to whether or not you can ignite TNT in adventure mode.

Observed Behavior:
TNT can be ignited.
Expected Behavior:
TNT would not be able to be ignited.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.19.2 using MCP-Reborn.
net.minecraft.world.level.block.TntBlock.java

```
public class TntBlock extends Block {
   ...
   public InteractionResult use(BlockState blockState, Level level, BlockPos blockPos, Player player, InteractionHand interactionHand, BlockHitResult blockHitResult) {
      ItemStack itemstack = player.getItemInHand(interactionHand);
      if (!itemstack.is(Items.FLINT_AND_STEEL) && !itemstack.is(Items.FIRE_CHARGE)) {
         return super.use(blockState, level, blockPos, player, interactionHand, blockHitResult);
      } else {
         explode(level, blockPos, player);
         level.setBlock(blockPos, Blocks.AIR.defaultBlockState(), 11);
         Item item = itemstack.getItem();
         if (!player.isCreative()) {
            if (itemstack.is(Items.FLINT_AND_STEEL)) {
               itemstack.hurtAndBreak(1, player, (player1) -> {
                  player1.broadcastBreakEvent(interactionHand);
               });
            } else {
               itemstack.shrink(1);
            }
         }
         player.awardStat(Stats.ITEM_USED.get(item));
         return InteractionResult.sidedSuccess(level.isClientSide);
      }
   }
   ...
```
If we look at the above class, we can see that there is only one necessary check that's carried out before allowing TNT to be ignited. This check is to quite simply see if the player is holding either flint and steel or a fire charge at the time of the interaction. If they are, the TNT will be ignited. The game doesn't check to see what abilities the player possesses (what game mode they are in) before allowing them to ignite TNT, therefore resulting in this problem occurring.
Fix:
Simply altering the appropriate existing "if" statement by adding an "if else" statement to it to check what abilities the player possesses before allowing them to ignite TNT will resolve this problem.
Current "if" statement:

```
if (!itemstack.is(Items.FLINT_AND_STEEL) && !itemstack.is(Items.FIRE_CHARGE)) {
   ...
} else {
   ...
```
Fixed "if" statement:

```
if (!itemstack.is(Items.FLINT_AND_STEEL) && !itemstack.is(Items.FIRE_CHARGE)) {
   ...
} else if (player.getAbilities().mayBuild) {
   ...
}
return InteractionResult.PASS;
...
```

## Comments (6)

### Comment 1: migrated (2021-04-09T11:43:52.578-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: migrated (2021-04-09T11:45:13.422-0700)

Can confirm

### Comment 3: migrated (2021-04-09T14:48:35.480-0700)

Can confirm in 21w14a

### Comment 4: Avoma (2021-04-10T06:01:00.914-0700)

, 21w14a was already marked as affected.

### Comment 5: Avoma (2021-04-14T09:06:24.287-0700)

Can confirm in 21w15a.

### Comment 6: Avoma (2022-10-18T07:41:42.769-0700)

Following on from my code analysis, I've double-checked my proposed fix and I can confidently confirm that it's fully functioning and works as expected, so I've attached two screenshots to this report, one of which shows the current code and the other that shows the fixed code. I feel this information may be quite insightful hence my reasoning for providing it.
