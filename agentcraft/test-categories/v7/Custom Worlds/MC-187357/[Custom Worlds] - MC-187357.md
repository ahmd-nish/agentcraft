# MC-187357: Strongholds will not generate in floating_islands or caves preset

**Mojira URL:** [https://bugs.mojang.com/browse/MC-187357](https://bugs.mojang.com/browse/MC-187357)

## Report details

- **Mojira categories:** Custom Worlds; Structures; World generation
- **Project:** MC
- **Issue key:** MC-187357
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2020-06-04T12:11:11.716-0700
- **Updated:** 2025-04-29T20:56:57.128-0700
- **Resolution date:** 2021-11-28T00:46:39.536-0800
- **Affects versions:** 1.16 Pre-release 1; 1.16 Pre-release 2; 1.16 Pre-release 5; 1.16.1
- **Fix versions:** 1.16.2 Pre-release 2
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** mcFlatStronghold.json; mcOverworldDefaults.json

## Description

All other structures seem to generate as normal. I generated a world with the settings below and used /locate to find a stronghold and none were found. I have seen temples, mansions, villages, etc. but no strongholds.

```
{
  "generate_features": true,
  "bonus_chest": false,
  "seed": -1464245863,
  "dimensions": {
    "minecraft:overworld": {
      "generator": {
        "type": "minecraft:noise",
        "seed": -1464245863,
        "biome_source": {
          "type": "minecraft:vanilla_layered",
          "seed": -1464245863,
          "large_biomes": false
        },
        "settings": "minecraft:floating_islands"
      },
      "type": "minecraft:overworld"
    },
    "minecraft:the_nether": {
      "generator": {
        "type": "minecraft:noise",
        "seed": -1464245863,
        "biome_source": {
          "type": "minecraft:multi_noise",
          "seed": -1464245863,
          "preset": "minecraft:nether"
        },
        "settings": "minecraft:nether"
      },
      "type": "minecraft:the_nether"
    },
    "minecraft:the_end": {
      "generator": {
        "type": "minecraft:noise",
        "seed": -1464245863,
        "biome_source": {
          "type": "minecraft:the_end",
          "seed": -1464245863
        },
        "settings": "minecraft:end"
      },
      "type": "minecraft:the_end"
    }
  }
}
```

## Comments (14)

### Comment 1: migrated (2020-06-04T12:11:11.716-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: [Mod] violine1101 (2020-06-04T13:45:23.146-0700)

Your world generation config appears to be incorrectly formatted. Please provide the world generation settings. You can surround plain text like this

```{code}
Put your stuff here...
{code}```

### Comment 3: migrated (2020-06-08T11:50:56.540-0700)

FWIW I was able to produce a large region of overlapping strongholds near spawn with the following setup:

```"structures": {
	"stronghold": {
		"distance": 0,
		"count": 128,
		"spread": 3
	},
	"structures": {
		"minecraft:stronghold": {
			"spacing": 2,
			"separation": 1,
			"salt": 0
		}
	}
}```

### Comment 4: migrated (2020-06-19T16:32:10.265-0700)

Don't generate for me either (specifically I'm using floating islands, ice spike biome) in 1.16-rc1. They always generated fine for me in 1.15 in single-biome worlds (and of this biome).

### Comment 5: migrated (2020-06-20T11:11:19.323-0700)

I'm having the same problem. I want to make a server with floating islands terrain, but it looks like to get to the end I'll have to make one myself in creative mode or something, which is kind of annoying.

### Comment 6: migrated (2020-06-21T06:33:22.939-0700)

Just a tip for until this bug gets fixed: the game is hardcoded to generate strongholds only in the "minecraft:overworld" and "minecraft:amplified" presets for "generator" -> "settings". If you use either of these 2 presets, you can customize the biome source and dimension type and still get strongholds, as long as you include a biome where they can generate.

### Comment 7: migrated (2020-06-21T07:27:49.730-0700)

I was able to produce stronghold generation identical to a vanilla world with the same seed using the stronghold value @Koxiaet mentioned with the values distance=32, spread=3, count=128. I'll attach a file containing the full settings for the overworld to produce a default world identical to just generating a regular world with the same seed. The file contains all of the noise and structure values for the overworld so you don't have to type all of them out yourself. If you want to change the generation to something other than the default, the defaults for floating islands and caves are listed on the [wiki page|https://minecraft.gamepedia.com/Custom].
The main issue here is that this stronghold value isn't documented anywhere. I'll try to add it to the wiki page soon. As far as I'm concerned this isn't really a bug at this point, now that we know how to make them generate.

### Comment 8: migrated (2020-06-21T09:28:36.173-0700)

The stronghold value is now documented on the wiki page for custom worlds.

### Comment 9: migrated (2020-06-22T01:53:19.882-0700)

Strongholds also don't generate on Superflat worlds - that needs to be added to the title.

### Comment 10: migrated (2020-06-22T09:15:11.054-0700)

It's actually very easy to add strongholds to superflat worlds with the same stronghold tag that can be used with the noise generator. I added it to the wiki page so it's properly documented now. I'll attach a sample JSON file that generates a superflat world with strongholds.

### Comment 11: migrated (2020-06-22T11:54:11.981-0700)

You can get them to generate, but sometimes if you fiddle around with the settings they inexplicably won't; /locate will show a stronghold but going there will yield nothing.

### Comment 12: migrated (2020-06-22T15:01:32.728-0700)

That seems like an entirely separate issue then. You can get them to generate if you don't mess with the stronghold settings too much; if you mess with the stronghold settings and that makes them stop generating, then that's a very different issue from strongholds not generating at all.

### Comment 13: migrated (2020-07-10T21:19:06.476-0700)

The stronghold generation in superflat seems to be related to the "features" option. When "features" is set to true, strongholds can generate along with grass and flowers and lakes of water and lava (even when "lakes" is set to false which might also be a problem), but when "features" is set to false, you can locate strongholds and eye of ender to them but they are not actually there. It seems to be impossible to create a superflat world with strongholds but no features, and I don't think that should be the case. Other structures can still generate when features is false. With Rajat Patel's JSON file if you only change "features": false, it will not generate strongholds.

### Comment 14: pulpetti (2020-07-16T12:14:08.171-0700)

In 20w29a.
