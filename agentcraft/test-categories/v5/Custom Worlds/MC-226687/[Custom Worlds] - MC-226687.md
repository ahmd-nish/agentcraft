# MC-226687: Sea Level is assumed to be Y = 63 in numerous parts of Minecraft

**Mojira URL:** [https://bugs.mojang.com/browse/MC-226687](https://bugs.mojang.com/browse/MC-226687)

## Report details

- **Mojira categories:** Custom Worlds; World generation
- **Project:** MC
- **Issue key:** MC-226687
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-05-28T15:48:04.003-0700
- **Updated:** 2025-04-26T13:23:22.273-0700
- **Resolution date:** 2025-01-13T03:20:31.571-0800
- **Affects versions:** 1.17 Pre-release 1; 1.17; 1.18 Pre-release 3; 1.18 Pre-release 4; 1.18.1; 22w12a; 1.19.2; 1.19.3; 23w07a; 1.20.2; 23w45a
- **Fix versions:** 24w33a
- **Area:** Platform
- **Labels:** datapack
- **Votes:** 2
- **Watchers:** 1
- **Attachments:** 5
- **Attachment filenames:** image-2021-05-28-13-51-26-889.png; image-2021-05-28-15-20-10-697.png; image-2021-05-28-15-23-10-492.png; SnowTestUnder63.zip; TallOceansTest.zip
- **Issue links:** Relates:outward:MC-249005:Strongholds can generate floating in superflat worlds | Relates:inward:MC-278019:Superflat worlds have their sea level at Y=-63 | Duplicate:inward:MC-259341:Monument height unable to be modified

## Description

The bugs listed here all stem from the bugged method in the screenshot(Level.getSeaLevel). Several bug reports were NOT made because fixing this singular bugged method would fix all the bugs listed.
Since 1.16's datapack system has been introduced, sea level has become a configurable argument in the chunk generator.

But there's one issue, a lot of places still assume that sea level is 63 when this is no longer the case when changing the sea level in the chunk generator.
I've attached the TallOceansTest & SnowTestUnder63 Datapack to recreate these issues listed.
This source of the issue can be narrowed down to `Level.getSeaLevel` method and usages of it as shown here:
This means all usages of this method, are possibly "broken" when this value is not changed together with Chunk Generator's sea level.
My solution:
In ServerLevel, override this method and call: this.chunkSource.getGenerator.getSeaLevel and on the client you'd most likely need some sort of packet containing the sea level of the current chunk generator/ServerLevel.
Here are a list of issues that may occur when changing sea level:
1. Dolphins, Drowned, Turtles, & Squid spawning does not occur in oceans in water when sea level is above Y 63.
No real good way to visualize this. But I've attached a datapack which increases both ocean depth & and the chunk generator's sea level to show this issue. All of the code for these can be found in the respective Mob's spawn rules.
2. Axolotls & Glowsquid spawning only occurs when the Ocean Floor Heightmap is under Y 63 as seen here in the `WaterAnimal` class:

```
public static boolean checkUndergroundWaterCreatureSpawnRules(EntityType<? extends LivingEntity> entityType, LevelAccessor world, MobSpawnType spawnReason, BlockPos pos, Random random) {
 return pos.getY() < world.getSeaLevel() && pos.getY() < world.getHeight(Heightmap.Types.OCEAN_FLOOR, pos.getX(), pos.getZ());
}
```
3. Ocelot spawning is not obstructed under the chunk generator sea level(when above 63) and ALWAYS obstructed when Chunk Generator sea level/terrain is under 63.
As seen here in the `Ocelot` class.

```
public boolean checkSpawnObstruction(LevelReader world) {
   if (world.isUnobstructed(this) && !world.containsAnyLiquid(this.getBoundingBox())) {
      BlockPos blockPos = this.blockPosition();
      if (blockPos.getY() < world.getSeaLevel()) {
         return false;
      }

      BlockState blockState = world.getBlockState(blockPos.below());
      if (blockState.is(Blocks.GRASS_BLOCK) || blockState.is(BlockTags.LEAVES)) {
         return true;
      }
   }

   return false;
}
```
4. Phantom Anchor Point is set to Y 64 when under Y 63 when Chunk Generator Sea Level is different
This may or may not be correct but the intention seems to be that the anchor point when under sea level(what I would believe should be the Chunk Generator's sea level) should be +1 on the Chunk Generator Sea Level. As seen here in the `Phantom.setAnchorAboveTarget` class:

```
private void setAnchorAboveTarget() {
      Phantom.this.anchorPoint = Phantom.this.getTarget().blockPosition().above(20 + Phantom.this.random.nextInt(20));
      if (Phantom.this.anchorPoint.getY() < Phantom.this.level.getSeaLevel()) {
         Phantom.this.anchorPoint = new BlockPos(Phantom.this.anchorPoint.getX(), Phantom.this.level.getSeaLevel() + 1, Phantom.this.anchorPoint.getZ());
      }

   }
}
```
5. Bats do not spawn in caves under the Chunk Generator's elevated sea level and are guaranteed to spawn where the Chunk Generator's sea level is lower than 63. As seen here in Bat.checkBatSpawnRules:

```
public static boolean checkBatSpawnRules(EntityType<Bat> type, LevelAccessor world, MobSpawnType spawnReason, BlockPos pos, Random random) {
   if (pos.getY() >= world.getSeaLevel()) {
      return false;
   } else {
      int i = world.getMaxLocalRawBrightness(pos);
      int j = 4;
      if (isHalloween()) {
         j = 7;
      } else if (random.nextBoolean()) {
         return false;
      }

      return i > random.nextInt(j) ? false : checkMobSpawnRules(type, world, spawnReason, pos, random);
   }
}
```
6. Drowned cannot spawn above Y 58 and are always deep enough to spawn in any fluids under Y 58.
As seen here in Drowned.isDeepEnoughToSpawn:

```
private static boolean isDeepEnoughToSpawn(LevelAccessor world, BlockPos pos) {
   return pos.getY() < world.getSeaLevel() - 5;
}
```

7. Blue Ice Feature will fail in water bodies above Y 62.
As seen in BlueIceFeature.place:

```
if (blockPos.getY() > worldGenLevel.getSeaLevel() - 1) {
   return false;
}
```
8. Ocean monuments spawn at a hardcoded height of Y 63, disregarding ocean floor height/sea level. You can see that here: https://youtu.be/5lfsKyAyifI
The code that produces this can be found in 2 places in the `OceanMonumentPieces` class.
8a. OceanMonumentPieces.postProcess:

```
public boolean postProcess(WorldGenLevel world, StructureFeatureManager structureAccessor, ChunkGenerator chunkGenerator, Random random, BoundingBox boundingBox, ChunkPos chunkPos, BlockPos pos) {
   int i = Math.max(world.getSeaLevel(), 64) - this.boundingBox.minY();
```
8b. OceanMonumentPieces.generateWaterBox:

```
protected void generateWaterBox(WorldGenLevel world, BoundingBox box, int x, int y, int z, int width, int height, int depth) {
   for(int i = y; i <= height; ++i) {
      for(int j = x; j <= width; ++j) {
         for(int k = z; k <= depth; ++k) {
            BlockState blockState = this.getBlock(world, j, i, k, box);
            if (!FILL_KEEP.contains(blockState.getBlock())) {
               if (this.getWorldY(i) >= world.getSeaLevel() && blockState != FILL_BLOCK) {
                  this.placeBlock(world, Blocks.AIR.defaultBlockState(), j, i, k, box);
               } else {
                  this.placeBlock(world, FILL_BLOCK, j, i, k, box);
               }
            }
         }
      }
   }

}
```
9. Blocks of air are ALWAYS placed in Ocean ruins when the chunk generator's sea level is ABOVE 63 or blocks of water are ALWAYS placed when Chunk Generator sea level is UNDER 63 in `handleDataMarker`.
As seen in OceanRuinPieces.handleDataMarker:

```
else if ("drowned".equals(metadata)) {
   Drowned drowned = (Drowned)EntityType.DROWNED.create(world.getLevel());
   drowned.setPersistenceRequired();
   drowned.moveTo(pos, 0.0F, 0.0F);
   drowned.finalizeSpawn(world, world.getCurrentDifficultyAt(pos), MobSpawnType.STRUCTURE, (SpawnGroupData)null, (CompoundTag)null);
   world.addFreshEntityWithPassengers(drowned);
   if (pos.getY() > world.getSeaLevel()) {
      world.setBlock(pos, Blocks.AIR.defaultBlockState(), 2);
   } else {
      world.setBlock(pos, Blocks.WATER.defaultBlockState(), 2);
   }
```

10. Axolotl & Turtle Path finding may produce inaccuracies in oceans w/ water above 53.
Not sure on enttiy AI myself but this issue can be seen in `AmphibiousNodeEvaluator.getNeighbors` when incrementing a Path Finding Node's cost malus:

```
public int getNeighbors(Node[] successors, Node node) {
   int i = super.getNeighbors(successors, node);
   BlockPathTypes blockPathTypes = this.getCachedBlockType(this.mob, node.x, node.y + 1, node.z);
   BlockPathTypes blockPathTypes2 = this.getCachedBlockType(this.mob, node.x, node.y, node.z);
   int k;
   if (this.mob.getPathfindingMalus(blockPathTypes) >= 0.0F && blockPathTypes2 != BlockPathTypes.STICKY_HONEY) {
      k = Mth.floor(Math.max(1.0F, this.mob.maxUpStep));
   } else {
      k = 0;
   }

   double d = this.getFloorLevel(new BlockPos(node.x, node.y, node.z));
   Node node2 = this.findAcceptedNode(node.x, node.y + 1, node.z, Math.max(0, k - 1), d, Direction.UP, blockPathTypes2);
   Node node3 = this.findAcceptedNode(node.x, node.y - 1, node.z, k, d, Direction.DOWN, blockPathTypes2);
   if (this.isNeighborValid(node2, node)) {
      successors[i++] = node2;
   }

   if (this.isNeighborValid(node3, node) && blockPathTypes2 != BlockPathTypes.TRAPDOOR) {
      successors[i++] = node3;
   }

   for(int l = 0; l < i; ++l) {
      Node node4 = successors[l];
      if (node4.type == BlockPathTypes.WATER && this.prefersShallowSwimming && node4.y < this.mob.level.getSeaLevel() - 10) {
         ++node4.costMalus;
      }
   }

   return i;
}
```
11. Phantom Spawning changes when sea level is changed from Y 63.
Issue can be found in: PantomSpawner.tick
12. Biome temperature height adjustment is hardcoded to Y 64(I presume this to be sea level + 1). You can see this issue very clearly here with these 2 images:
Vanilla:
Snow Test Under 63(Sea level is -12) datapack:
The code in question can be found in Biome.getHeightAdjustedTemperature:

```
private float getHeightAdjustedTemperature(BlockPos pos) {
   float f = this.climateSettings.temperatureModifier.modifyTemperature(pos, this.getBaseTemperature());
   if (pos.getY() > 64) {
      float g = (float)(TEMPERATURE_NOISE.getValue((double)((float)pos.getX() / 8.0F), (double)((float)pos.getZ() / 8.0F), false) * 4.0D);
      return f - (g + (float)pos.getY() - 64.0F) * 0.05F / 30.0F;
   } else {
      return f;
   }
}
```

## Comments (10)

### Comment 1: migrated (2021-05-28T15:48:04.003-0700)

This comment contained multiple image attachments (5), please login to view the attachments.

### Comment 2: migrated (2021-05-28T17:58:17.140-0700)

@osfanjoshua Counterpoint, all these seemingly separate bugs are all caused by a single bug, the world using a hardcoded value for sealevel instead of the chunkgenerator's sealevel that the world already has. This disconnection between the hardcoded sealevel and actual sealevel used for worldgen cascades and causes numerous amount of issues down the line.

It seems far to unproductive to create a bug report for every single issue caused by a single bug and have the mojang dev hunt down every single one of these reports to mark as resolved  when they fix the one root cause.

### Comment 3: muzikbike (2021-11-04T08:10:27.335-0700)

Is the sky turning black under the sea level also part of this?

### Comment 4: ampolive (2021-11-04T08:18:18.143-0700)

()

### Comment 5: ampolive (2021-11-17T04:19:50.443-0800)

Can confirm in 1.18 Pre-release 2.

### Comment 6: ampolive (2021-11-17T04:21:27.280-0800)

The code in Biome.getHeightAdjustedTemperature(...) has been changed to 80 instead of 64, however.

### Comment 7: ampolive (2021-11-17T04:25:41.389-0800)

Also, now glow squids use their own spawn rules, but still are dependent on the hardcoded sea level.
net.minecraft.world.entity.GlowSquid.java (Mojang mappings, 1.18-pre2)

```public static boolean checkGlowSquideSpawnRules(EntityType<? extends LivingEntity> $$0, ServerLevelAccessor $$1, MobSpawnType $$2, BlockPos $$3, Random $$4) {
        return $$1.getBlockState($$3).is(Blocks.WATER) && $$3.getY() <= $$1.getSeaLevel() - 33;
    }```

### Comment 8: ampolive (2021-11-17T08:54:49.360-0800)

Can confirm in 1.18 Pre-release 3.

### Comment 9: ampolive (2021-11-18T03:53:21.607-0800)

Can confirm in 1.18 Pre-release 4.

### Comment 10: aceplante (2023-01-30T22:20:23.123-0800)

Potentially the cause of [MC-257201] Nether caves not filling to sea level - Jira (mojang.com) too?
