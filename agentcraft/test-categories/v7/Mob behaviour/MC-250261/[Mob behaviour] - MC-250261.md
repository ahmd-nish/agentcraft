# MC-250261: Frogs can lay spawn on flowing water

**Mojira URL:** [https://bugs.mojang.com/browse/MC-250261](https://bugs.mojang.com/browse/MC-250261)

## Report details

- **Mojira categories:** Mob behaviour
- **Project:** MC
- **Issue key:** MC-250261
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-04-17T03:48:07.697-0700
- **Updated:** 2025-04-16T17:34:02.801-0700
- **Resolution date:** 2022-08-16T09:25:18.843-0700
- **Affects versions:** 22w15a; 22w16b; 22w17a; 22w19a; 1.19 Pre-release 1; 1.19 Pre-release 5; 1.19 Release Candidate 2; 1.19
- **Fix versions:** 22w24a
- **Labels:** frog; frog-spawn
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** MC-250261.mp4; MC-250261.png; setup.png
- **Issue links:** Relates:inward:MCPE-152559:Frogs lay eggs on Flowing Water

## Description

The Bug:
Players are unable to manually place frogspawn on flowing water so having frogs being able to lay spawn here seems illogical. Additionally, when the frogspawn receives a block update, it is instantly destroyed.
Steps to Reproduce:
- Build the setup as shown in the attachment below.

- Summon two frogs nearby and breed them.

- Wait for the pregnant frog to approach the water and lay its spawn.

- Take note as to whether or not frogs can lay spawn on flowing water.

Observed Behavior:
Frogs can lay spawn on flowing water.
Expected Behavior:
Frogs would not be able to lay spawn on flowing water.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 22w15a using Mojang mappings.
In FrogAi#initLaySpawnActivity(...), a new TryLaySpawnOnWaterNearLand behavior is created for the frog. In the code:
net.minecraft.world.entity.ai.behavior.TryLaySpawnOnWaterNearLand.java

```
...
    @Override
    protected void start(ServerLevel $$0, Frog $$1, long $$2) {
        BlockPos $$3 = $$1.blockPosition().below();
        for (Direction $$4 : Direction.Plane.HORIZONTAL) {
            BlockPos $$6;
            BlockPos $$5 = $$3.relative($$4);
            if (!$$0.getBlockState($$5).is(Blocks.WATER) || !$$0.getBlockState($$6 = $$5.above()).isAir()) continue;
            $$0.setBlock($$6, this.spawnBlock.defaultBlockState(), 3);
            $$0.playSound(null, $$1, SoundEvents.FROG_LAY_SPAWN, SoundSource.BLOCKS, 1.0f, 1.0f);
            $$1.getBrain().eraseMemory(this.memoryModule);
            return;
        }
    }
...
```
The behavior checks if the block adjacent to the block the frog is standing on is water, and if there is air on top of it. Because flowing water is considered a water block, frogs are able to lay their spawn here.

## Comments (5)

### Comment 1: migrated (2022-04-17T03:48:07.697-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: ampolive (2022-04-17T12:49:03.131-0700)

Relates to MC-250267.

### Comment 3: Avoma (2022-04-18T00:27:21.011-0700)

, I've included the code analysis you did on MC-250267 to the description of this ticket () since I feel it's insightful and also because it's essentially the same cause of both of these issues. I've credited you where appropriate and I hope you're okay with this.

### Comment 4: ampolive (2022-04-18T05:04:59.040-0700)

No problem at all!

### Comment 5: Avoma (2022-04-29T10:55:30.179-0700)

Relates to MCPE-152559.
