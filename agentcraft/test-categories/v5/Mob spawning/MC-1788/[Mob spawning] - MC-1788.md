# MC-1788: Ocelots do not spawn naturally on Peaceful difficulty in jungles and bamboo jungles

**Mojira URL:** [https://bugs.mojang.com/browse/MC-1788](https://bugs.mojang.com/browse/MC-1788)

## Report details

- **Mojira categories:** Mob spawning
- **Project:** MC
- **Issue key:** MC-1788
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2012-11-01T16:38:20.793-0700
- **Updated:** 2026-06-10T14:10:49.717-0700
- **Resolution date:** 2026-04-22T00:52:43.231-0700
- **Affects versions:** Minecraft 1.4.2; 1.16.3; 1.16.4 Pre-release 1; 1.16.4 Pre-release 2; 1.16.4 Release Candidate 1; 1.16.4; 20w45a; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 21w05b; 21w11a; 1.17; 21w40a; 1.18.1; 1.19.3; 23w04a; 1.20.1; 23w32a; 1.21 Pre-Release 3; 1.21; 1.21.3; 1.21.8; 25w32a; 1.21.9; 1.21.11
- **Fix versions:** 26.2 Snapshot 4
- **Area:** Gameplay
- **Labels:** mob; ocelot; peaceful; spawning
- **Votes:** 14
- **Watchers:** 2
- **Attachments:** 1
- **Attachment filenames:** image-20260422-034954.png
- **Issue links:** Duplicate:inward:MC-194320:Ocelot spawns | Duplicate:inward:MC-104824:Ocelots dissapearing after changing difficulty | Duplicate:inward:MC-16357:Ocelots spawn using the hostile mob spawner | Duplicate:inward:MC-19742:Peaceful doesn't work with ocelots? | Duplicate:inward:MC-67851:hostle kitty!

## Description

The bug
Despite being friendly mobs, ocelots will not spawn on peaceful in jungle or bamboo jungle biomes
Code Analysis
The reason this happens is because for the mob cap in jungle and bamboo jungle biomes they are counted as monsters instead of creatures
Current Code
net/minecraft/data/worldgen/biome/OverworldBiomes.java

```
public static Biome jungle() {
      MobSpawnSettings.Builder mobspawnsettings$builder = new MobSpawnSettings.Builder();
      BiomeDefaultFeatures.baseJungleSpawns(mobspawnsettings$builder);
      mobspawnsettings$builder.addSpawn(MobCategory.CREATURE, new MobSpawnSettings.SpawnerData(EntityType.PARROT, 40, 1, 2)).addSpawn(MobCategory.MONSTER, new MobSpawnSettings.SpawnerData(EntityType.OCELOT, 2, 1, 3)).addSpawn(MobCategory.CREATURE, new MobSpawnSettings.SpawnerData(EntityType.PANDA, 1, 1, 2));
      return baseJungle(0.9F, false, false, true, mobspawnsettings$builder);
   }

   public static Biome bambooJungle() {
      MobSpawnSettings.Builder mobspawnsettings$builder = new MobSpawnSettings.Builder();
      BiomeDefaultFeatures.baseJungleSpawns(mobspawnsettings$builder);
      mobspawnsettings$builder.addSpawn(MobCategory.CREATURE, new MobSpawnSettings.SpawnerData(EntityType.PARROT, 40, 1, 2)).addSpawn(MobCategory.CREATURE, new MobSpawnSettings.SpawnerData(EntityType.PANDA, 80, 1, 2)).addSpawn(MobCategory.MONSTER, new MobSpawnSettings.SpawnerData(EntityType.OCELOT, 2, 1, 1));
      return baseJungle(0.9F, true, false, true, mobspawnsettings$builder);
   }
```
Fixed Code
net/minecraft/data/worldgen/biome/OverworldBiomes.java

```
public static Biome jungle() {
      MobSpawnSettings.Builder mobspawnsettings$builder = new MobSpawnSettings.Builder();
      BiomeDefaultFeatures.baseJungleSpawns(mobspawnsettings$builder);
      //Setting the MobCategory to Creature for Ocelot fixes MC-1788
      mobspawnsettings$builder.addSpawn(MobCategory.CREATURE, new MobSpawnSettings.SpawnerData(EntityType.PARROT, 40, 1, 2)).addSpawn(MobCategory.CREATURE, new MobSpawnSettings.SpawnerData(EntityType.OCELOT, 2, 1, 3)).addSpawn(MobCategory.CREATURE, new MobSpawnSettings.SpawnerData(EntityType.PANDA, 1, 1, 2));
      return baseJungle(0.9F, false, false, true, mobspawnsettings$builder);
   }

   public static Biome bambooJungle() {
      MobSpawnSettings.Builder mobspawnsettings$builder = new MobSpawnSettings.Builder();
      BiomeDefaultFeatures.baseJungleSpawns(mobspawnsettings$builder);
      //Setting the MobCategory to Creature for Ocelot fixes MC-1788
      mobspawnsettings$builder.addSpawn(MobCategory.CREATURE, new MobSpawnSettings.SpawnerData(EntityType.PARROT, 40, 1, 2)).addSpawn(MobCategory.CREATURE, new MobSpawnSettings.SpawnerData(EntityType.PANDA, 80, 1, 2)).addSpawn(MobCategory.CREATURE, new MobSpawnSettings.SpawnerData(EntityType.OCELOT, 2, 1, 1));
      return baseJungle(0.9F, true, false, true, mobspawnsettings$builder);
   }
```

## Comments (42)

### Comment 1: migrated (2012-11-05T08:47:23.016-0800)

Were you in the jungle, which is the only biome they naturally spawn in?

### Comment 2: migrated (2012-11-05T08:48:43.591-0800)

Yes of course.

### Comment 3: migrated (2012-11-05T08:53:20.347-0800)

Yes, annoyed me from the very beginning

### Comment 4: migrated (2012-11-05T08:57:05.495-0800)

^ Hi five!  That also annoys me, that's why I brought it up here.
If You could please just vote it up, so it's more likely it'll get noticed…

### Comment 5: migrated (2012-11-05T10:36:58.397-0800)

Here, have an upvote

### Comment 6: migrated (2012-11-07T13:04:37.780-0800)

Thank You!! 😊

### Comment 7: kumasasa (2013-02-04T14:43:30.624-0800)

Confirmed but unknown if intended.
Ocelots are considered as "Monster" for the game, so that they don't spawn in peaceful.

### Comment 8: migrated (2013-02-04T23:24:11.192-0800)

What about wolves though? They can even attack You, but they still spawn on the easiest difficulty.

### Comment 9: migrated (2013-02-17T11:52:04.447-0800)

Intended, source: http://www.minecraftwiki.net/wiki/Issues/Weekly_12w04a#Bugs_7

### Comment 10: migrated (2013-02-17T13:12:54.901-0800)

It's only they despawn because they were created using a HOSTILE monster spawner - they are not hostile, are they?
Please think it though, give it a chance

### Comment 11: migrated (2013-02-17T13:14:53.487-0800)

```[N] = This is not a bug. (It is intended behaviour and will not be changed)```
For feature suggestions/changes please use the MineCraft Forums: Suggestions.

### Comment 12: migrated (2013-02-17T13:18:20.112-0800)

>__< That means they'll never look at it.

### Comment 13: migrated (2013-05-20T08:31:53.667-0700)

It may be intentional that mobs spawned with the hostile mob spawner do despawn and don't spawn in peaceful difficulty.
Still, ocelots are not hostile so it makes no sense for them to spawn using the hostile mob spawner. This makes it impossible to get cats on peaceful maps or on servers with hostile mobs disabled, which is just stupid. Please think about this again.

### Comment 14: migrated (2013-05-20T09:18:22.422-0700)

^ Exactly!
I still do not believe it works as intended as well.

### Comment 15: migrated (2014-07-04T18:22:12.570-0700)

yea honestly, ocelots are not hostile in any way shape or form, they are completely neutral even when tamed. so why not make em spawn on peaceful? wolves do, and they are hostile when aggravated. why spawn them with a mob spawner? make it the same spawn thing as wolves.

### Comment 16: migrated (2015-01-08T21:05:07.936-0800)

Is this bug that ocelots don't spawn naturally, or that they don't spawn from mob spawners? The description seems to be talking about natural spawning, but several of the comments are referring to mob spawners.

### Comment 17: migrated (2015-02-11T20:25:23.161-0800)

Could someone clarify the bug going on here? Is it natural spawning, or mob spawners?

### Comment 18: migrated (2015-02-12T00:48:40.780-0800)

Both, probably. But the main issue is that they don't spawn naturally in the jungle on peaceful difficulty. Which makes cats completely unavailable when playing on peaceful without cheats.

### Comment 19: migrated (2020-09-27T22:18:08.050-0700)

I think the category of this should be "Mob Spawning"

### Comment 20: migrated (2020-11-06T08:52:48.728-0800)

Ocelots are underneath the monster spawns category in the biome file for jungles. To fix this bug, all they need to do is move it to the passive spawns like every other animal is in. I ran some tests with custom biomes, and Peaceful mode stops any mobs from spawning that are inside the monster spawns category, even if they aren't a monster at all.

### Comment 21: Avoma (2021-01-08T06:22:22.751-0800)

Can confirm in 20w51a.

### Comment 22: Avoma (2021-01-29T12:12:49.475-0800)

Can confirm in 21w03a.

### Comment 23: Avoma (2021-02-05T09:08:48.790-0800)

Can confirm in 21w05b.

### Comment 24: Avoma (2021-03-18T02:53:41.110-0700)

Can confirm in 21w11a.

### Comment 25: migrated (2021-03-18T02:55:13.839-0700)

Relates to MC-186131.

### Comment 26: migrated (2021-08-29T09:27:59.589-0700)

The actual bug is that they are in the hostile mob cap, so if you for example have 70 shulkers loaded in singleplayer and you go to a jungle no ocelots will spawn. Solution is to let them be part of passive mob cap, and follow the rules of passive mob spawning

### Comment 27: Ceresjanin123 (2021-10-09T01:39:40.853-0700)

Can confirm in 21w40a

### Comment 28: migrated (2022-07-22T16:30:50.068-0700)

This is because ocelots are concidered hostile in the code

### Comment 29: migrated (2023-01-04T07:05:33.933-0800)

Can confirm in 1.19.2.

### Comment 30: migrated (2023-01-04T11:55:49.653-0800)

Affects 1.19.3

### Comment 31: Brain81505 (2023-01-24T23:24:54.780-0800)

Can confirm in 23w04a

### Comment 32: Brain81505 (2023-02-01T08:05:34.659-0800)

Can confirm in 23w06a

### Comment 33: Brain81505 (2023-07-05T08:57:56.007-0700)

Can confirm in 1.20.1

### Comment 34: Minecraft386882 (2024-11-10T06:06:09.535-0800)

Can confirm for 1.21.3

### Comment 35: Minecraft386882 (2024-11-26T09:00:28.927-0800)

Confirmed in 1.21.4 prerelease 2

### Comment 36: stephen clayton (2025-05-08T16:27:33.220-0700)

confirm 1.21.4

### Comment 37: KarenEP (2025-08-01T11:24:25.727-0700)

Still true in 1.21.8. Please fix this. I want ocelots.

### Comment 38: AerospaceCoot35 (2025-12-27T14:51:03.580-0800)

Surprised this hasn’t been fixed yet. Maybe it is because the ocelot has now mostly been forgotten about since the splitting of cats from the mob.

### Comment 39: KarenEP (2025-12-27T17:04:05.937-0800)

Still true in 1.21.11

### Comment 40: wallenplays1211 (2026-04-21T09:53:00.663-0700)

Affects in 26.1.2 and 26.2 snapshot 4.
In 26.2 snapshot 4, Piglins and Hoglins can spawn in peaceful, so Ocelot should be spawned in peaceful.

### Comment 41: Sightnado (2026-04-21T20:31:56.107-0700)

Cannot reproduce in 26.2 Snapshot 4; I am able to get ocelots to spawn in Peaceful difficulty. Only took them 13 years aha

### Comment 42: phizlip (2026-04-21T20:50:00.087-0700)

Can confirm @Sightnado’s findings:
