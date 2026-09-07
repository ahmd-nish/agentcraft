# MC-260750: Magma blocks use unnecessary random ticking for an outdated feature, causing performance issues

**Mojira URL:** [https://bugs.mojang.com/browse/MC-260750](https://bugs.mojang.com/browse/MC-260750)

## Report details

- **Mojira categories:** Performance
- **Project:** MC
- **Issue key:** MC-260750
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2023-03-04T06:20:52.616-0800
- **Updated:** 2025-04-30T05:07:35.131-0700
- **Resolution date:** 2023-03-22T02:49:45.195-0700
- **Affects versions:** 1.19.3; 1.19.4 Pre-release 3; 1.19.4
- **Fix versions:** 23w12a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2023-03-04_15.28.58.png; 2023-03-04_15.33.27.png
- **Issue links:** Relates:inward:MC-260951:Magma blocks can generate exposed to the air beside aquifers

## Description

This is an optimization issue, although it is notable only on very specific cases such as the one described later.
The bug
Prior to 1.13, magma blocks used to extinguish water above them by using the random ticking system. After the update, this feature was removed making the random ticking no longer necessary for magma blocks. However, this feature was not properly removed and some remaining code is still present on the game, more concretely, the random ticking. Due to this, the game still checks for magma blocks on random ticking wasting a bit of performance.
Steps to reproduce
For expected behaviour:
- Create a superflat world just with the bedrock and 20 layers of stone, and with mobs disabled.

- Set 'random tick speed' game rule to an high number (1000+)

-  On the Alt+F3 menu, notice how performance remains unaffected.

For this bug:
- Create a superflat world just with the bedrock and 20 layers of magma blocks and mobs disabled.

- Set 'random tick speed' game rule to an high number (1000+)

-  On the Alt+F3 menu, notice how the performance meter shows an increase.

This is very likely not intended, because apparently magma blocks don't do anything related to random events or game ticking (except for entity damage, but that's from a different).
Code analysis
Here's a code analysis along with a potential fix regarding this issue.
The following is based on a decompiled version of Minecraft 1.19.2 using MCP-Reborn.
net.minecraft.world.level.block.MagmaBlock.java

```
public class MagmaBlock extends Block {
   ...
   public void randomTick(BlockState $bs, ServerLevel $sl, BlockPos $bp, RandomSource $rs) {
      BlockPos blockpos = $bp.above();
      if ($sl.getFluidState($bp).is(FluidTags.WATER)) {
         $sl.playSound((Player)null, $bp, SoundEvents.FIRE_EXTINGUISH, SoundSource.BLOCKS, 0.5F, 2.6F + ($sl.random.nextFloat() - $sl.random.nextFloat()) * 0.8F);
         $sl.sendParticles(ParticleTypes.LARGE_SMOKE, (double)blockpos.getX() + 0.5D, (double)blockpos.getY() + 0.25D, (double)blockpos.getZ() + 0.5D, 8, 0.5D, 0.25D, 0.5D, 0.0D);
      }

   }
   ...
```
If we look at the above class, we can see that the block is checking if a water fluid is in the same block position as the magma block, which is impossible in vanilla minecraft but the game still checks this because it is used on random ticking. Before 1.13, the block used to check the block above instead, for the feature explained before (it is very likely that the old code is now commented). After the update, this was forgotten to be removed and at net.minecraft.world.level.block.Blocks the magma block definition still defines it as a random ticking block.
Potential Fix:
Simply removing the .randomTicks() method within this line of code should resolve this problem, along with removing MagmaBlock.randomTick() method to remove extra unnecessary code:
net.minecraft.world.level.block.Blocks.java

```
public class Blocks {
   ...
   public static final Block MAGMA_BLOCK = register("magma_block", new MagmaBlock(BlockBehaviour.Properties.of(Material.STONE, MaterialColor.NETHER).requiresCorrectToolForDrops().lightLevel((p_152684_) -> {       return 3;
    }).randomTicks().strength(0.5F).isValidSpawn((p_187421_, p_187422_, p_187423_, p_187424_) -> {
       return p_187424_.fireImmune();    }).hasPostProcess(Blocks::always).emissiveRendering(Blocks::always)));
   ...
}
```

## Comments (7)

### Comment 1: migrated (2023-03-04T06:20:52.616-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: migrated (2023-03-04T10:16:13.807-0800)

Confirmed.

### Comment 3: Moesh (2023-03-08T00:19:03.103-0800)

This is feedback, not a bug.

### Comment 4: migrated (2023-03-08T00:30:58.386-0800)

It's a performance issue, not feedback. This actively uses up server performance while having no effect.

### Comment 5: ISRosillo14 (2023-03-08T01:08:51.658-0800)

(rant alert) Moesh I'm NOT asking for the outdated feature to be added back, I'm just indicating that said old feature was not removed properly and it is causing performance issues. The magma block is literally checking if there's water AT the same block the magma block is IN! This is nonsense.
Please read the full report and not just the title, please reconsider reopening. I think I will ask Avoma to create a new ticket with better and appropiate title and descriptions.

### Comment 6: Moesh (2023-03-08T01:59:27.412-0800)

Thanks for the feedback everyone. This bug was caught in the gray area of our "needs gameplay impact" policy. We have triaged this bug and will look to create a more consistent ruling for bugs that indicate performance impact.

### Comment 7: migrated (2023-03-08T03:50:19.894-0800)

Well, it was clearly stated in the title and description it impacted performance.
