# MC-209932: Sculk sensors only detect the last turtle egg being broken when being stepped on

**Mojira URL:** [https://bugs.mojang.com/browse/MC-209932](https://bugs.mojang.com/browse/MC-209932)

## Report details

- **Mojira categories:** Game Events
- **Project:** MC
- **Issue key:** MC-209932
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2020-12-29T08:20:10.906-0800
- **Updated:** 2025-04-30T08:06:08.759-0700
- **Resolution date:** 2022-05-24T06:13:23.446-0700
- **Affects versions:** 20w51a; 21w03a; 21w05a; 21w05b; 21w06a; 21w07a; 21w08b; 21w10a; 21w14a; 21w15a; 21w17a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17 Release Candidate 1; 1.17 Release Candidate 2; 1.17; 1.17.1 Pre-release 1; 1.17.1; 1.18; 1.18.1; 1.18.2; 22w11a; 22w14a; 22w17a; 1.19 Pre-release 1
- **Fix versions:** 1.19 Pre-release 3
- **Labels:** sculk_sensor
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-209932.mp4; MC-209932.png

## Description

The Bug:
Sculk sensors only detect the last turtle egg being broken when being stepped on.
Steps to Reproduce:
- Place down four turtle eggs on the same block.

- Place down a sculk sensor nearby, stand on top of the turtle eggs, and wait for them to break.

- Take note as to whether or not sculk sensors only detect the last turtle egg being broken when being stepped on.

Observed Behavior:
Sculk sensors aren't actiavted.
Expected Behavior:
Sculk sensors would be activated.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.18.2 using MCP-Reborn.
net.minecraft.world.level.block.TurtleEggBlock.java

```
public class TurtleEggBlock extends Block {
   ...
   private void decreaseEggs(Level $l, BlockPos $bp, BlockState $bs) {
      $l.playSound((Player)null, $bp, SoundEvents.TURTLE_EGG_BREAK, SoundSource.BLOCKS, 0.7F, 0.9F + $l.random.nextFloat() * 0.2F);
      int i = $bs.getValue(EGGS);
      if (i <= 1) {
         $l.destroyBlock($bp, false);
      } else {
         $l.setBlock($bp, $bs.setValue(EGGS, Integer.valueOf(i - 1)), 2);
         $l.levelEvent(2001, $bp, Block.getId($bs));
      }

   }
   ...
```
If we look at the above class, we can see that when the last turtle egg is broken, the destroyBlock() method is called. The destroyBlock() method then calls the gameEvent() method resulting in a vibration being produced. The problem here is that when there is more than one turtle egg occupying the same space, and one of them was to be destroyed, the gameEvent() method is never called, thus not detecting this action as a vibration.
Potential Fix:
Simply calling the gameEvent() method where appropriate within this piece of code should resolve this problem. The "BLOCK_DESTROY" game event tag would be expected to be used here as the turtle eggs are destroyed.

## Comments (5)

### Comment 1: migrated (2020-12-29T08:20:10.906-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: markderickson (2020-12-29T09:28:27.863-0800)

Can confirm

### Comment 3: migrated (2020-12-29T09:42:24.769-0800)

Can confirm, There are 4 eggs that can break 1 only but if the last egg breaks it will vibrate the sculk sensor. It should be fixed

### Comment 4: muzikbike (2020-12-30T04:15:48.527-0800)

Relates to MC-207679. Reckon you could add the sculk_sensor label to this ticket and any other tickets you've reported in this vein?

### Comment 5: ampolive (2021-07-07T17:02:23.505-0700)

Can confirm in 1.17.1.
