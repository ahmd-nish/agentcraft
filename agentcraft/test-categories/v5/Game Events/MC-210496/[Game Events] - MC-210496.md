# MC-210496: Sculk sensors are not activated upon harvesting sweet berry bushes

**Mojira URL:** [https://bugs.mojang.com/browse/MC-210496](https://bugs.mojang.com/browse/MC-210496)

## Report details

- **Mojira categories:** Game Events
- **Project:** MC
- **Issue key:** MC-210496
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-01-04T03:10:30.584-0800
- **Updated:** 2025-04-11T11:50:21.406-0700
- **Resolution date:** 2022-05-19T08:30:51.906-0700
- **Affects versions:** 20w51a; 21w03a; 21w05a; 21w05b; 21w06a; 21w07a; 21w08b; 21w10a; 21w11a; 21w14a; 21w15a; 21w17a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17 Release Candidate 1; 1.17; 1.17.1 Pre-release 1; 1.17.1 Release Candidate 1; 1.17.1; 21w37a; 21w38a; 1.18; 1.18.1; 22w05a; 1.18.2; 22w14a; 22w18a; 1.19 Pre-release 1
- **Fix versions:** 1.19 Pre-release 2
- **Labels:** sculk_sensor
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** MC-210496.mp4
- **Issue links:** Relates:inward:MC-213803:Sculk sensors are not activated upon harvesting glow berries from cave vines

## Description

The Bug:
Sculk sensors are not activated upon harvesting sweet berry bushes.
Steps to Reproduce:
- Place down a sweet berry bush.

- Apply bone meal to it until berries can be seen on the bush.

- Place down a sculk sensor nearby.

- Harvest the sweet berry bush.

- Take note as to whether or not sculk sensors are activated upon harvesting sweet berry bushes.

Observed Behavior:
Sculk sensors are not activated upon harvesting sweet berry bushes.
Expected Behavior:
Sculk sensors would be activated upon harvesting sweet berry bushes.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.18.2 using MCP-Reborn.
net.minecraft.world.level.block.SweetBerryBushBlock.java

```
public class SweetBerryBushBlock extends BushBlock implements BonemealableBlock {
   ...
   public InteractionResult use(BlockState $bs, Level $l, BlockPos $bp, Player $p, InteractionHand $ih, BlockHitResult $bhr) {
      int i = $bs.getValue(AGE);
      boolean flag = i == 3;
      if (!flag && $p.getItemInHand($ih).is(Items.BONE_MEAL)) {
         return InteractionResult.PASS;
      } else if (i > 1) {
         int j = 1 + $l.random.nextInt(2);
         popResource($l, $bp, new ItemStack(Items.SWEET_BERRIES, j + (flag ? 1 : 0)));
         $l.playSound((Player)null, $bp, SoundEvents.SWEET_BERRY_BUSH_PICK_BERRIES, SoundSource.BLOCKS, 1.0F, 0.8F + $l.random.nextFloat() * 0.4F);
         $l.setBlock($bp, $bs.setValue(AGE, Integer.valueOf(1)), 2);
         return InteractionResult.sidedSuccess($l.isClientSide);
      } else {
         return super.use($bs, $l, $bp, $p, $ih, $bhr);
      }
   }
   ...
```
If we look at the above class, we can see that harvesting berries from sweet berry bushes simply isn't registered as a game event as the gameEvent() method is never called, thus not detecting this action as a vibration.
Potential Fix:
Simply calling the gameEvent() method where appropriate within this piece of code should resolve this problem. The "BLOCK_CHANGE" game event tag would work nicely in this instance here as the block states of sweet berry bushes are changed when they're harvested. The following line of code could be used in order to fix this:

```
$LEVEL.gameEvent($PLAYER, GameEvent.BLOCK_CHANGE, $BLOCKPOS);
```

## Comments (2)

### Comment 1: migrated (2021-01-04T03:10:30.584-0800)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: migrated (2021-01-04T06:58:07.717-0800)

Can confirm
