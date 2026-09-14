# MC-209929: Sculk sensors are not activated upon filling composters

**Mojira URL:** [https://bugs.mojang.com/browse/MC-209929](https://bugs.mojang.com/browse/MC-209929)

## Report details

- **Mojira categories:** Game Events
- **Project:** MC
- **Issue key:** MC-209929
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2020-12-29T08:11:00.400-0800
- **Updated:** 2025-04-16T15:21:47.784-0700
- **Resolution date:** 2023-02-08T04:26:42.440-0800
- **Affects versions:** 20w51a; 21w03a; 21w05a; 21w05b; 21w06a; 21w07a; 21w08b; 21w10a; 21w14a; 21w15a; 21w17a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17 Release Candidate 1; 1.17 Release Candidate 2; 1.17; 1.17.1 Pre-release 1; 1.17.1; 21w38a; 21w40a; 1.18; 1.18.1; 1.18.2; 22w14a; 22w17a; 22w18a; 1.19 Pre-release 1; 1.19 Pre-release 3; 1.19 Pre-release 5; 1.19 Release Candidate 2; 1.19; 1.19.2; 22w45a; 1.19.3
- **Fix versions:** 23w06a
- **Labels:** composter; sculk_sensor
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-209929.mp4; MC-209929.png
- **Issue links:** Duplicate:inward:MC-251352:Sculk Sensor doesn't detect composter changes | Relates:inward:MCPE-155371:Sculk Sensor doesn't detect composter changes

## Description

The Bug:
Sculk sensors are not activated upon filling composters.
Steps to Reproduce:
- Place down a composter along with a sculk sensor nearby.

- Fill the composter with a cake and watch the sculk sensor closely as you do this.

- Take note as to whether or not sculk sensors are activated upon filling composters.

Observed Behavior:
Sculk sensors aren't activated.
Expected Behavior:
Sculk sensors would be activated.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.18.2 using MCP-Reborn.
net.minecraft.world.level.block.ComposterBlock.java

```
public class ComposterBlock extends Block implements WorldlyContainerHolder {
   ...
   public InteractionResult use(BlockState $bs, Level $l, BlockPos $bp, Player $p, InteractionHand $ih, BlockHitResult $bhr) {
      int i = $bs.getValue(LEVEL);
      ItemStack itemstack = $p.getItemInHand($ih);
      if (i < 8 && COMPOSTABLES.containsKey(itemstack.getItem())) {
         if (i < 7 && !$l.isClientSide) {
            BlockState blockstate = addItem($bs, $l, $bp, itemstack);
            $l.levelEvent(1500, $bp, $bs != blockstate ? 1 : 0);
            $p.awardStat(Stats.ITEM_USED.get(itemstack.getItem()));
            ...
```
If we look at the above class, we can see that filling composters simply isn't registered as a game event as the gameEvent() method is never called, thus not detecting this action as a vibration.
Potential Fix:
Simply calling the gameEvent() method where appropriate within this piece of code should resolve this problem. The "BLOCK_CHANGE" game event tag would be expected to be used here as the block states of composters are changed when they're filled. The following line of code could be used in order to fix this:

```
$LEVEL.gameEvent($PLAYER, GameEvent.BLOCK_CHANGE, $BLOCKPOS);
```

## Comments (3)

### Comment 1: migrated (2020-12-29T08:11:00.400-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: migrated (2020-12-29T08:12:39.121-0800)

Can confirm

### Comment 3: ampolive (2021-10-11T05:49:16.945-0700)

Can confirm in 21w40a.
