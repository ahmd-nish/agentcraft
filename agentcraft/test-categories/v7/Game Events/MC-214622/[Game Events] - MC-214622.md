# MC-214622: Sculk sensors do not detect daylight detector mode switching

**Mojira URL:** [https://bugs.mojang.com/browse/MC-214622](https://bugs.mojang.com/browse/MC-214622)

## Report details

- **Mojira categories:** Game Events
- **Project:** MC
- **Issue key:** MC-214622
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-02-09T04:27:42.979-0800
- **Updated:** 2025-03-20T23:51:53.126-0700
- **Resolution date:** 2022-05-24T05:28:23.391-0700
- **Affects versions:** 21w05b; 21w06a; 21w07a; 21w08b; 21w11a; 21w14a; 21w17a; 1.17; 1.17.1; 21w43a; 1.18.1; 1.18.2; 22w18a; 1.19 Pre-release 1
- **Fix versions:** 1.19 Pre-release 3
- **Labels:** sculk_sensor
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 2021-02-09_12.26.16.png; 2021-02-09_12.26.17.png; MC-214622.mp4

## Description

I'd strongly recommend also adding a sound (or empty sound event at the very least) for this, since many related actions (e.g. changing a comparator's mode) have sounds.
This action would without a doubt be considered a "block change", and as such should create a vibration of some sort.
How to reproduce
- Place down a daylight detector and a sculk sensor nearby

- Change the mode of the daylight detector by right-clicking on it

- Take note as to whether or not a vibration is created and/or if the sculk sensor is activated upon switching the daylight detector's mode

Expected Behavior
A vibration would be produced upon switching daylight detector modes, which the sculk sensor would detect.
Observed Behavior
No such vibration is produced, and the sculk sensor is not activated at all.
Code analysis
Code analysis by  can be found in this comment.

## Comments (17)

### Comment 1: migrated (2021-02-09T04:27:42.979-0800)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: migrated (2021-02-09T07:59:46.894-0800)

Can confirm

### Comment 3: Avoma (2021-02-11T08:20:08.620-0800)

Can confirm in 21w06a.

### Comment 4: Avoma (2021-02-20T04:05:14.702-0800)

Can confirm in 21w07a.

### Comment 5: Avoma (2021-02-20T05:36:05.160-0800)

Video attached.

### Comment 6: Avoma (2021-02-26T06:54:43.987-0800)

Can confirm in 21w08b.

### Comment 7: Avoma (2021-03-20T04:34:40.344-0700)

Can confirm in 21w11a.

### Comment 8: Avoma (2021-04-10T02:53:58.726-0700)

Can confirm in 21w14a.

### Comment 9: migrated (2021-04-14T13:07:12.616-0700)

Since the Daylight Sensor Transition doesn't make sound, I don't think it would activate a Sculk Sensor, since they detect sound.

### Comment 10: migrated (2021-04-21T03:00:34.134-0700)

They detect vibrations, not sounds

### Comment 11: Avoma (2021-04-29T01:15:00.658-0700)

Can confirm in 21w17a.

### Comment 12: Avoma (2021-06-09T11:49:57.333-0700)

Can confirm in 1.17.

### Comment 13: Avoma (2021-07-07T12:20:37.432-0700)

Can confirm in 1.17.1.

### Comment 14: Avoma (2021-10-28T05:12:20.930-0700)

Can confirm this behavior in 21w43a. Here are some extra details regarding this problem.
The Bug:
Sculk sensors are not activated upon switching between daylight detector modes.
Steps to Reproduce:
- Place down a daylight detector and a sculk sensor nearby.

- Change the mode of the daylight detector by right-clicking on it.

- Take note as to whether or not sculk sensors are activated upon switching between daylight detector modes.

Observed Behavior:
Sculk sensors are not activated upon switching between daylight detector modes.
Expected Behavior:
Sculk sensors would be activated upon switching between daylight detector modes.

### Comment 15: Avoma (2021-12-20T00:10:21.630-0800)

Can confirm in 1.18.1.

### Comment 16: Avoma (2022-03-06T10:50:41.268-0800)

Can confirm in 1.18.2.

### Comment 17: Avoma (2022-05-07T04:33:44.892-0700)

Can confirm in 22w18a. Here's a code analysis regarding this issue.
Code Analysis:
The following is based on a decompiled version of Minecraft 1.18.2 using MCP-Reborn.
net.minecraft.world.level.block.DaylightDetectorBlock.java

```public class DaylightDetectorBlock extends BaseEntityBlock {
   ...
   public InteractionResult use(BlockState $bs, Level $l, BlockPos $bp, Player $p, InteractionHand $ih, BlockHitResult $bhr) {
      if ($p.mayBuild()) {
         if ($l.isClientSide) {
            return InteractionResult.SUCCESS;
         } else {
            BlockState blockstate = $bs.cycle(INVERTED);
            $l.setBlock($bp, blockstate, 4);
            updateSignalStrength(blockstate, $l, $bp);
            return InteractionResult.CONSUME;
         ...```
If we look at the above class, we can see that switching the "inverted" mode on daylight detectors simply isn't registered as a game event as the gameEvent() method is never called, thus not detecting this action as a vibration.
Potential Fix:
Simply calling the gameEvent() method where appropriate within this piece of code should resolve this problem. The "BLOCK_CHANGE" game event tag would be expected to be used here as the block states of daylight detectors are changed. The following line of code could be used in order to fix this:

```$LEVEL.gameEvent($PLAYER, GameEvent.BLOCK_CHANGE, $BLOCKPOS);```
