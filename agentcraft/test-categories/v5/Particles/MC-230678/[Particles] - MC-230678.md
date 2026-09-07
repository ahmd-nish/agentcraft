# MC-230678: Cauldron fills with powder snow in frozen ocean biome while it's visually raining

**Mojira URL:** [https://bugs.mojang.com/browse/MC-230678](https://bugs.mojang.com/browse/MC-230678)

## Report details

- **Mojira categories:** Block states; Particles
- **Project:** MC
- **Issue key:** MC-230678
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-06-29T14:53:40.425-0700
- **Updated:** 2025-04-30T06:01:24.842-0700
- **Resolution date:** 2022-12-15T02:29:51.552-0800
- **Affects versions:** 1.17; 1.17.1 Pre-release 2; 1.17.1; 21w37a; 1.18 Pre-release 6; 1.18 Pre-release 7; 1.18.1; 22w11a; 22w14a; 22w18a; 1.19; 1.19.1 Pre-release 4; 1.19.1 Pre-release 5; 1.19.1; 1.19.2; 22w42a; 1.19.3 Pre-release 2; 1.19.3
- **Fix versions:** 23w03a
- **Labels:** frozen_ocean
- **Watchers:** 1
- **Attachments:** 8
- **Attachment filenames:** 2021-06-29_14.45.13.png; 2021-06-29 19-15-34.mp4; 2021-09-16_18.22.13.png; 2021-11-22_19.34.16.png; 2021-12-16_19.33.48.png; 2021-12-16_19.35.23.png; DeepFrozenOcean.png; MC-230678.png
- **Issue links:** Relates:inward:MC-255811:Level#isRainingAt(BlockPos) always returns false for snowy and frozen biomes, even when it is raining | Relates:inward:MC-254132:Wolves do not get wet when raining in Frozen Oceans | Relates:outward:MC-247836:Riptide doesn't work in rain within a frozen ocean biome

## Description

The bug
Cauldrons are supposed to be filled with water while it's raining, and powder snow while it is snowing. Frozen oceans have a unique temperature gradient that makes it snow in certain places and rain in others. However, whenever a cauldron is placed in this biome, it is filled with powder snow regardless of which local region it is in, even if it is visually raining. Ice and snow are formed as normal (i.e. following the boundaries of the local temperature values).
How to reproduce
- Find a frozen ocean, or create a superflat world with just frozen ocean

- Use /fill command to create a large layer of cauldrons under open sky

- Change weather to raining/snowing

- Observe that some cauldrons are filled with powder snow even if it is raining

- Replace the platform with solid blocks, and see how snow layers are formed normally

This bug does not exist for the deep frozen ocean biome.
Code analysis
Code analysis can be found in this comment.

## Comments (13)

### Comment 1: migrated (2021-06-29T14:53:40.425-0700)

This comment contained multiple image attachments (8), please login to view the attachments.

### Comment 2: ampolive (2021-06-29T15:14:51.967-0700)

Can confirm in 1.17.1 Pre-release 2.

### Comment 3: ampolive (2021-08-02T05:24:22.332-0700)

Can confirm in 1.17.1.

### Comment 4: ampolive (2021-09-16T14:22:34.242-0700)

Can confirm in 21w37a.

### Comment 5: ampolive (2021-10-07T07:15:47.896-0700)

Can confirm in 21w39a.

### Comment 6: windwend (2021-12-15T17:53:44.460-0800)

Ampolive, thanks for the code analysis. I was wondering, can you do some more code-digging to figure out why deep frozen ocean doesn't have this problem? You can post the code analysis for that under this issue as well.

### Comment 7: ampolive (2021-12-16T04:40:14.321-0800)

I imagine it doesn't happen because the deep frozen ocean precipitation is set to "rain" in its biome file.

### Comment 8: windwend (2021-12-16T13:39:25.357-0800)

I don't think a single biome precipitation value explains how this bug doesn't exist for deep frozen ocean. In the image I just attached, you can see that in a superflat world I have created, cauldrons can collect powder snow or water according to the local temperature gradient.

### Comment 9: ampolive (2021-12-16T14:06:50.333-0800)

Thanks for the new info! My initial analysis is incorrect, I overlooked some details.

### Comment 10: ampolive (2021-12-16T14:20:54.488-0800)

In ServerLevel#tickChunk(...), this code sets the precipitation to SNOW when the temperature is below 0.15, even if the biome has RAIN.

```...
Biome.Precipitation $$16 = this.getBiome($$12).getPrecipitation();
if ($$16 == Biome.Precipitation.RAIN && $$14.coldEnoughToSnow($$13)) {
                    $$16 = Biome.Precipitation.SNOW;
                }
$$15.getBlock().handlePrecipitation($$15, (Level)this, $$13, $$16);
...```
So, the temperature gradient is only respected if the biome precipitation is set to RAIN. If the biome precipitation is set to SNOW, then the cauldron will always fill with powder snow. Frozen oceans (not deep frozen oceans) have a biome precipitation set to SNOW, so they never fill up with water.
net.minecraft.world.level.block.CauldronBlock.java (1.18.1, Mojang mappings)

```...
    @Override
    public void handlePrecipitation(BlockState $$0, Level $$1, BlockPos $$2, Biome.Precipitation $$3) {
        if (!CauldronBlock.shouldHandlePrecipitation($$1, $$3)) {
            return;
        }
        if ($$3 == Biome.Precipitation.RAIN) {
            $$1.setBlockAndUpdate($$2, Blocks.WATER_CAULDRON.defaultBlockState());
            $$1.gameEvent(null, GameEvent.FLUID_PLACE, $$2);
        } else if ($$3 == Biome.Precipitation.SNOW) {
            $$1.setBlockAndUpdate($$2, Blocks.POWDER_SNOW_CAULDRON.defaultBlockState());
            $$1.gameEvent(null, GameEvent.FLUID_PLACE, $$2);
        }
    }
...```

### Comment 11: ampolive (2021-12-16T14:34:38.397-0800)

Upon closer inspection, it seems that the opposite may happen in deep frozen oceans: cauldrons fill with water while it's snowing. It might be a different issue.

### Comment 12: Avoma (2022-06-28T01:10:30.591-0700)

Can confirm in 1.19.

### Comment 13: Avoma (2022-07-27T10:45:56.695-0700)

Can confirm in 1.19.1.
