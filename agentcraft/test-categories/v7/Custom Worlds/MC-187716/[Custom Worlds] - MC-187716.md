# MC-187716: Nether biome surface builder types incorrectly assume the world height is 128 blocks

**Mojira URL:** [https://bugs.mojang.com/browse/MC-187716](https://bugs.mojang.com/browse/MC-187716)

## Report details

- **Mojira categories:** Custom Worlds
- **Project:** MC
- **Issue key:** MC-187716
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2020-06-05T13:47:27.412-0700
- **Updated:** 2025-04-11T14:13:33.359-0700
- **Resolution date:** 2021-11-06T16:15:08.252-0700
- **Affects versions:** 1.16 Pre-release 2; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w27a; 20w28a; 1.16.2 Pre-release 1; 1.16.2 Pre-release 3; 1.16.2; 1.16.4; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5 Release Candidate 1; 1.16.5; 21w05a; 21w06a; 21w07a; 21w08a; 21w08b; 21w10a; 21w11a; 21w13a; 21w14a; 21w15a; 21w16a; 21w17a; 21w18a; 21w20a; 1.17 Pre-release 2; 1.17 Release Candidate 1; 21w42a; 21w43a
- **Fix versions:** 21w44a
- **Labels:** Surface_builders; custom-worldgen
- **Watchers:** 1
- **Attachments:** 10
- **Attachment filenames:** 2020-06-05_20.55.52.png; 2020-06-05_21.35.32.png; 2020-06-05_21.36.00.png; 2020-06-05_21.38.14.png; 2020-06-05_21.41.27.png; 2020-06-21_01.56.43.png; Taller Nether.zip; Taller Nether-1.zip; worldgen_settings_export.json; worldgen settings export.json
- **Issue links:** Duplicate:inward:MC-192852:Nether biomes don't generate groundcover over Y=127 even if there is terrain. | Duplicate:inward:MC-193912:Custom world geoation problems | Duplicate:inward:MC-196663:Surface builders used by new Nether biomes stop above y=127 | Duplicate:inward:MC-197338:custom nether dimension_type logicalHeight does not actually change the dimension height | Duplicate:inward:MC-207390:Nether biomes do not generate as intended above y=128 | Duplicate:inward:MC-212300:Nether biomes don't apply above y=128 | Duplicate:inward:MC-215178:Nether Wastes blocks don't generate above y128 and below y0 in the World Type: Caves | Duplicate:inward:MC-223577:Certain Features Not Generating Above Height 128 in 256-High Nether | Duplicate:inward:MC-227515:Nether biome surface builder types incorrectly assume the world height is 128 blocks | Relates:inward:MC-208816:No terrain nor feature generation currently supports negative Y values

## Description

This bug happens because the surface builder types for Nether biomes assume the world is 128 blocks tall.
Other surface builder types - which do not make this assumption - do not have this issue.
This applies to these surface builder types:
minecraft:nether_forest
minecraft:soul_sand_valley
minecraft:basalt_deltas
Likely it also applies to minecraft:nether, but I have not verified this personally.

## Comments (29)

### Comment 1: migrated (2020-06-05T13:47:27.412-0700)

This comment contained multiple image attachments (10), please login to view the attachments.

### Comment 2: migrated (2020-06-21T07:52:47.398-0700)

I experienced the same bug, it's way more clear if you set default_block to something else like stone. You get a very obvious hard line at y=128 where the actual nether biomes no longer generate most of their features and instead it's just a stone noise map. In this screenshot you can see I'm in a soul sand valley, but above y=128 there's no soul sand at all. Features like warped/crimson fungus trees and nether fossils sometimes generate slightly above y=128. Also, almost all of the Basalt Deltas generate above y=128; however, they generate without blackstone.

### Comment 3: migrated (2020-08-03T19:05:21.757-0700)

Partially valid.
Features like ores, fire patches, lava springs, flowstone clusters and mushrooms are configured on a feature level, having an altitude cap of 128. You can manually overwrite these and raise the cap to 256, also manually doubling the spawn rates to keep the feature density of original terrain. Ores and other features will normally generate above regular height by doing so. It's logical for these to be configured that way by default, considering the ore spawns above bedrock ceiling would always fail.
The only problem are surface builders used by nether biomes, which unlike the overworld surface builders don't extend beyond level 127. You can see that by changing surface builder of say warped forest to the one used by mushroom island - mycelium has no issues spawning above level 127. There seems to be a hard cap coded into the surface builders of wart forests, soul sand valleys and basalt deltas, added before devs considered they would be used for custom terrain generation exceeding that height. Unless raising or removing the cap costs a significant loss in performance, it would be great to have that altered.

### Comment 4: migrated (2020-08-11T07:43:50.593-0700)

I think it wouldn't decrease game performence, since surface builder only checks if blocks can be repleaced by its values, so it wouldn't even try to do so above the bedrock layer, where everythig is air. I can support this thesis by my observations on how this works. If we try to increse the nether height, surface builder will always replace 128 level where it is possible, even if there is a netherrack one block above.
It'd be modifiable if we get surface types (minecraft:nether_forest, minecraft:basalt_deltas, minecraft:soul_sand_valley and minecraft:nether) in our hand. It seems like those types have hard-coded height limit, because after changing type to, for example, minecraft:default from nether_forest, crimson and warped forests will have nylium on ground above 128 level, however, since we changed it from minecraft:nether_forest, wart blocks won't generate both on surface and on ceilling. Same with deltas and valley. Their features won't generate, unless they're specified somewhere
Giving us surface types wouldn't hurt game performance at all actually and would fix all the issues of this kind.

### Comment 5: migrated (2020-08-15T04:46:42.826-0700)

@BillyGalbreath you showed the exact thing, this issue is about. You didn't "fix" this

### Comment 6: migrated (2020-08-15T05:01:00.130-0700)

The 3 classes used for nether surface builders are hardcoded to 127 rather than the configured 'k' value
https://github.com/pl3xgaming/Purpur/blob/ver/1.16.2/patches/server/0127-Use-configured-height-for-nether-surface-builders.patch
Using 'k' instead of 127 fixes this issue as seen here https://www.youtube.com/watch?v=7m6Fc-aVQoA

### Comment 7: migrated (2020-12-02T10:41:20.978-0800)

the file i normaly use for the bug test is broken as of 20w49a
unfortunaly i can no longer test and update this bug report until i have a new file/datapack

### Comment 8: migrated (2020-12-16T09:57:34.815-0800)

i got a file that is working again

### Comment 9: migrated (2021-02-02T07:26:37.373-0800)

Is this happening because of 3d biomes? The basalt deltas is generated the whole height.

### Comment 10: migrated (2021-02-02T09:55:37.021-0800)

the bastalt deltas stop generating the ground above y127 so its just netherrack instead of blackstone or basalt

### Comment 11: migrated (2021-02-02T12:22:47.723-0800)

Another note: Same issue occurs with negative y values

### Comment 12: migrated (2021-03-10T11:55:33.976-0800)

my current computer did not meet the minimum requirements and now snapshot 20w10a does no longer work for me and i will be unable to properly update the affected version on time

### Comment 13: migrated (2021-03-10T13:01:23.897-0800)

I can reproduce this issue in 21w10a. Did you try updating gpu driver by the way? There is a chance your PC will meet requirements.

### Comment 14: migrated (2021-03-10T13:09:29.769-0800)

I'd like to further maintain this issue since you are unable to further provide affected versions. Would you be okay with me taking ownership of this issue? If you say yes I'll request ownership of this issue in the Mojira Discord. Thanks!

### Comment 15: migrated (2021-03-11T02:07:43.194-0800)

i think i can use another computer in the evening and continue updating this bug report.
also my computer is a lenovo T430 and only has intel HD graphics 3000 while the minimum requirements are intel HD graphics 4000

### Comment 16: migrated (2021-03-31T13:28:03.586-0700)

@verified_gamer i have a intel HD graphics 2500 and the snapshot works for me

### Comment 17: migrated (2021-03-31T14:39:48.833-0700)

thanks for offering your help Michael but i already have another computer to test the snapshots on

### Comment 18: migrated (2021-04-08T01:10:41.002-0700)

In 21w14a mojang added the "min_surface_height" tag which is for defining the starting height of the surface builder, this tag also configures the minimum surface builder height of Nether Biomes. This change adds a point of inconsistency with this bug: Being able to define minimum surface level height but not maximum surface level height.

Yes, what I said makes no sense. It's just an excuse to create another reason why this bug should be fixed

### Comment 19: migrated (2021-06-06T04:01:43.442-0700)

This bug happens because the surface builder types for Nether biomes assume the world is 128 blocks tall.
Other surface builder types - which do not make this assumption - do not have this issue.
This applies to these surface builder types:
minecraft:nether_forest
minecraft:soul_sand_valley
minecraft:basalt_deltas
Likely it also applies to minecraft:nether, but I have not verified this personally.
Please add this information to the bug report.

On top of that, it would be convenient to have a couple of labels added to the report as well, such as surface_builders and custom-worldgen.

### Comment 20: migrated (2021-06-06T04:05:26.530-0700)

I also request the title of this bug report be changed to "Nether biome surface builder types incorrectly assume the world height is 128 blocks", because that is actually the root cause of this bug.
As soon as there are Nylium blocks for huge fungi and Nether forest vegetation to generate on top of, it will simply do so.

### Comment 21: migrated (2021-10-21T11:49:49.666-0700)

This still occurs in the latest 1.18 snapshots including 21w42a. I created a datapack to make the nether 256 tall and yet those three surface builders refuse to generate their respective blocks above y=128.

### Comment 22: migrated (2021-10-22T06:17:11.355-0700)

You can fix this in 1.17.1 and older by chaning the type of the surface builder to default.
So data/minecraft/worldgen/configured_surface_builder/[nether_biome].json:
From:
"type": "minecraft:nether_forest"
To
"type": "minecraft:default"

### Comment 23: migrated (2021-10-28T08:27:41.863-0700)

@Peter Rabbit can i get that datapack, updating the .json file for the Import Settings button is a lot of work and my most recent version got lost when i got a new laptop

### Comment 24: migrated (2021-10-28T09:03:44.351-0700)

I attached the latest version of my 256 tall nether data pack updated for 21w43a.

### Comment 25: migrated (2021-11-03T13:00:03.366-0700)

Haven't checked last snapshot but in 21w44a this appears to have been fixed!!

### Comment 26: migrated (2021-11-04T11:05:20.112-0700)

I can confirm that 21w44a has fixed 256 tall nether generation with an updated version of my data pack. Soul sand/soil, basalt deltas, crimson nylium, and warped nylium all generate up to the custom height limit,

### Comment 27: migrated (2021-11-04T16:14:50.043-0700)

seems to be fixed, but biomes seem to generate 2D and not 3D

### Comment 28: migrated (2021-11-06T08:31:45.879-0700)

3D noise was never added in the nether.

### Comment 29: migrated (2021-11-06T16:15:08.252-0700)

CalXee nether uses 3d noise since 1.16, but it's on a small scale. Like blending on Y level can extend to 3-4 blocks
