# MC-251934: Sculk sensors are not activated upon frogs laying frogspawn

**Mojira URL:** [https://bugs.mojang.com/browse/MC-251934](https://bugs.mojang.com/browse/MC-251934)

## Report details

- **Mojira categories:** Game Events
- **Project:** MC
- **Issue key:** MC-251934
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-05-19T09:17:27.024-0700
- **Updated:** 2025-04-30T05:38:05.190-0700
- **Resolution date:** 2023-02-07T00:32:29.371-0800
- **Affects versions:** 1.19 Pre-release 1; 1.19 Pre-release 2; 1.19 Pre-release 5; 1.19 Release Candidate 2; 1.19; 1.19.1 Pre-release 2; 1.19.1; 1.19.2; 1.19.3
- **Fix versions:** 23w06a
- **Labels:** sculk_sensor
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-251934.mp4; MC-251934.png
- **Issue links:** Relates:inward:MC-215767:Sculk sensors do not detect turtles laying an egg

## Description

The Bug:
Sculk sensors are not activated upon frogs laying frogspawn.
Steps to Reproduce:
- Summon two frogs near some water.

- Breed the frogs and place down a sculk sensor nearby.

- Wait until one of the frogs lays frogspawn.

- Take note as to whether or not sculk sensors are activated upon frogs laying frogspawn.

Observed Behavior:
Sculk sensors aren't activated.
Expected Behavior:
Sculk sensors would be activated.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.19 Pre-release 2 using Mojang mappings.
net.minecraft.world.entity.ai.behavior.TryLaySpawnOnWaterNearLand.java

```
public class TryLaySpawnOnWaterNearLand extends Behavior<Frog> {
   private final Block spawnBlock;
   private final MemoryModuleType<?> memoryModule;
   ...
   @Override
   protected void start(ServerLevel serverLevel, Frog frog, long l) {
      BlockPos blockPos = frog.blockPosition().below();
      for (Direction direction : Direction.Plane.HORIZONTAL) {
         BlockPos blockPos2;
         BlockPos blockPos3 = blockPos.relative(direction);
         if (!serverLevel.getBlockState(blockPos3).is(Blocks.WATER) || !serverLevel.getBlockState(blockPos2 = blockPos3.above()).isAir()) continue;
         serverLevel.setBlock(blockPos2, this.spawnBlock.defaultBlockState(), 3);
         serverLevel.playSound(null, frog, SoundEvents.FROG_LAY_SPAWN, SoundSource.BLOCKS, 1.0f, 1.0f);
         frog.getBrain().eraseMemory(this.memoryModule);
         return;
      }
   }
   ...
```
If we look at the above class, we can see that frogs laying frogspawn simply isn't registered as a game event as the gameEvent() method is never called, thus not detecting this action as a vibration.

## Comments (3)

### Comment 1: migrated (2022-05-19T09:17:27.024-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: pulpetti (2022-05-24T06:25:12.250-0700)

In 1.19 Pre-2.

### Comment 3: Mask3D_WOLF (2022-10-25T13:33:32.511-0700)

Possibly relates to MC-215767 ?
