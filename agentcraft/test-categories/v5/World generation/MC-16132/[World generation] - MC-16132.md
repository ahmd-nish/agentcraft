# MC-16132: Cave carvers don't cut through snow blocks

**Mojira URL:** [https://bugs.mojang.com/browse/MC-16132](https://bugs.mojang.com/browse/MC-16132)

## Report details

- **Mojira categories:** World generation
- **Project:** MC
- **Issue key:** MC-16132
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2013-05-22T23:35:17.871-0700
- **Updated:** 2025-04-26T02:53:31.789-0700
- **Resolution date:** 2024-10-22T08:24:20.570-0700
- **Affects versions:** Minecraft 1.5.1; Minecraft 1.5.2; Snapshot 13w19a; Snapshot 13w21a; Minecraft 1.6.1; Minecraft 1.6.2; Minecraft 1.7.4; Minecraft 14w02c; Minecraft 14w03a; Minecraft 14w03b; Minecraft 14w20b; Minecraft 14w21b; Minecraft 15w51b; Minecraft 1.10.2; Minecraft 16w44a; Minecraft 1.12.2; Minecraft 17w50a; Minecraft 18w07c; Minecraft 1.13-pre1; Minecraft 1.13-pre5; Minecraft 1.13; Minecraft 18w30b; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 19w08b; Minecraft 1.14.2; Minecraft 1.14.3 Pre-Release 2; 1.14.4; 19w36a; 19w38b; 19w39a; 19w40a; 19w41a; 19w46a; 1.15 Pre-release 1; 1.15 Pre-release 3; 1.15 Pre-release 4; 1.15 Pre-release 7; 1.15; 1.15.1; 1.15.1 Pre-release 1; 1.15.2 Pre-release 2; 1.15.2; 20w06a; 20w07a; 20w14a; 20w15a; 20w17a; 20w18a; 20w21a; 20w22a; 1.16 Pre-release 1; 1.16 Pre-release 2; 1.16 Pre-release 5; 1.16 Pre-release 6; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w27a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Release Candidate 1; 1.16.4 Release Candidate 1; 1.16.4; 20w46a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w06a; 21w11a; 21w13a; 21w16a; 21w18a; 21w19a; 21w37a; 21w38a; 1.18.2; 1.19 Release Candidate 1; 1.19; 1.19.2; 1.19.3; 1.19.4; 1.20 Pre-release 6; 1.20; 1.20.1; 23w33a; 24w11a; 24w13a; 1.20.6; 1.21; 1.21.1; 1.21.2 Pre-Release 3
- **Fix versions:** Minecraft 14w20b; 24w44a
- **Area:** Platform
- **Labels:** cave-carver; snow; snow_block
- **Watchers:** 1
- **Attachments:** 10
- **Attachment filenames:** 2015-12-18_14.00.56.png; 2015-12-18_14.01.36.png; 2017-12-25_10.29.07.png; 2021-02-10_20.53.07.png; 2021-02-10_20.54.38.png; 2021-09-16_19.54.52.png; MC-16132 - 1.19.png; Screen Shot 2019-09-27 at 6.53.50 PM.png; Screen Shot 2020-06-18 at 1.26.05 PM.png; works_as_intended_i_think_NOT.png
- **Issue links:** Relates:outward:MC-261174:Suspicious gravel is not part of the #overworld_carver_replaceables tag, causing carvers to not cut through it | Relates:outward:MC-94487:Ravines don't naturally cut through sand, sandstone, or terracotta upon generation, but other cave types do. | Duplicate:inward:MC-241435:No snow and ice caves generated | Duplicate:inward:MC-241786:Floating snow in mountains | Duplicate:inward:MC-239814:Mountain Generation | Duplicate:inward:MC-237446:Cave generator doesn't cut through powder snow properly | Duplicate:inward:MC-221684:Floating Sand is Created When Big Caves Generate in Badlands | Duplicate:inward:MC-166150:red sand dosent "exist" according to caves/ravines | Duplicate:inward:MC-49046:Snow blocks not erroding during cave generation

## Description

The Bug:
Cave carvers don't cut through snow blocks.
Cave carvers cut through a variety of surface blocks such as mud, mycelium, podzol, sand, red sand, etc... so it seems rather strange that they don't cut through snow blocks.
Here is an example:
Version: 1.19.3

```
Seed: -51010235163883720
Coordinates: /execute in minecraft:overworld run tp @s 1127.30 80.00 1669.96 -29.47 17.73
```
Steps to Reproduce:
- Generate a world with the seed provided above and teleport to the given coordinates.

- Look at how the cave interacts with nearby snow blocks.

- Take note as to whether or not cave carvers cut through snow blocks.

Observed Behavior:
Cave carvers don't cut through snow blocks.
Expected Behavior:
Cave carvers would cut through snow blocks.

## Comments (45)

### Comment 1: migrated (2013-05-22T23:35:17.871-0700)

This comment contained multiple image attachments (10), please login to view the attachments.

### Comment 2: Torabi (2013-05-24T10:43:20.884-0700)

And "lose on a technicality" you shall, unless you, or someone else, proves that it also occurs in vanilla, unmodded Minecraft.

### Comment 3: migrated (2013-05-24T10:53:43.691-0700)

Confirmed in 13w21a.

### Comment 4: migrated (2013-05-25T18:39:34.774-0700)

This has happened since 1.3.2 at least, I have a world from that version with a shroom island that is just like this.

### Comment 5: Ezekiel (2013-07-11T12:10:08.465-0700)

Is this still a concern in the current Minecraft version? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.
Note: this is a automatic message, so apologies if I miss something.

### Comment 6: bugi74 (2013-07-11T12:25:20.766-0700)

Affects 1.6.2

### Comment 7: bugi74 (2013-07-13T09:52:56.344-0700)

Fix
Quite near the end of the method:
MapGenCaves.generateCaveNode()

```//              if (blockTypeId == Block.grass.blockID) {
                if (blockTypeId == Block.grass.blockID || blockTypeId == Block.mycelium.blockID) {
                    var49 = true;
                }

//              if (blockTypeId == Block.stone.blockID || blockTypeId == Block.dirt.blockID || blockTypeId == Block.grass.blockID) {
                if (blockTypeId == Block.stone.blockID || blockTypeId == Block.dirt.blockID || blockTypeId == Block.grass.blockID || blockTypeId == Block.mycelium.blockID) {```
I think the fix needs no explanation.
I attached a screenshot
 showing the cave in its full glory, courtesy of fixed cave generator. (There are more nearby holes all around that place, they are just out of the view.)

### Comment 8: migrated (2013-08-10T22:53:55.417-0700)

Still an issue as of this post.

### Comment 9: galaxy_2alex (2014-01-22T09:24:58.843-0800)

Is this still a concern in the current Minecraft version 1.7.4 / Launcher version 1.3.8 or later? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 10: migrated (2014-01-22T10:42:46.641-0800)

@Galaxy_2Alex
This effects all versions through 14w03b

### Comment 11: bugi74 (2014-03-02T10:55:33.942-0800)

Affects the same way snow surface in Ice Plains -biome, at least in 1.7.5. See -861, -12, seed -4542366974610774625. Quite likely the same fix applies.

### Comment 12: migrated (2014-05-15T15:30:21.569-0700)

Fixed in 14w20?

### Comment 13: kumasasa (2014-05-17T00:47:28.096-0700)

No, Ice plains see Markku's coordinates above, Mushroom biome: -2983, 66 , -2460, seed -4542366974610774625

### Comment 14: migrated (2014-05-24T11:06:29.054-0700)

This was fixed. See attachment.

### Comment 15: bugi74 (2014-05-24T11:51:13.592-0700)

Nope, not fixed in 14w21b. That particular example shows a cave that pokes the surface somewhat perpendicular to it, which has had no problems. See the seed/coords mentioned by me and you can still find the same issue is there (at least for ice plains -biome).
EDIT: Actually, maybe the mycelium case is indeed solved, my memory being as poor as it is and it has been so long time; perhaps the cave wouldn't have even poked through the mycelium surface if the issue wasn't fixed...  In any case, the ice plains snow surface is still bugged.

### Comment 16: migrated (2014-05-24T11:52:04.425-0700)

Second to last picture on there, starting with Minecraft_14w21b.

### Comment 17: kumasasa (2014-05-24T11:53:25.648-0700)

Not fixed in 14w21b.

### Comment 18: migrated (2014-05-24T11:54:35.563-0700)

Cannot reproduce.

### Comment 19: kumasasa (2014-05-24T11:58:52.254-0700)

@: -861, 64, -12, Seed -4542366974610774625

### Comment 20: galaxy_2alex (2014-10-25T09:50:18.250-0700)

Is this still a concern in the current Minecraft version 1.8.1 Prerelease 3 / Launcher version 1.5.3 or later? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 21: migrated (2015-12-18T06:22:56.127-0800)

(As of 15w51b) Looks like cave generation does cut through mycelium, but not snow. Also doesn't cut through packed ice (see the 3 most recently-added attachments)
One other little thing to note is that ravine generation follows slightly different rules than other kinds of cave generation, see MC-94487. I think that ravines will require their own separate fix.

### Comment 22: migrated (2016-11-05T18:13:10.438-0700)

Is this still an issue on the latest snapshot 16w44a?

### Comment 23: bugi74 (2016-11-06T01:19:03.631-0800)

Still issue, still the given example location shows: -861, 64, -12, Seed -4542366974610774625  (ice/snow)

### Comment 24: migrated (2016-12-10T08:26:27.419-0800)

Is this still a problem in Minecraft 1.11?

### Comment 25: gaspoweredpick (2018-06-29T16:35:53.157-0700)

Can confirm for 1.13-pre5. I also noticed that the same applies to red sand in the 1.13 snapshots because now the caves and ravines will no longer cut through red sand just like they don't cut through snow and mycelium.

### Comment 26: gaspoweredpick (2019-02-23T15:42:57.917-0800)

Confirmed for 1.13.2 and 19w08b.

### Comment 27: gaspoweredpick (2019-06-09T20:43:48.460-0700)

Although this should be easy to fix with red sand, fixing this for snow blocks may (or may not) cause a new bug that may not be fixed. Since snow blocks generate in igloos and snowy villages, making caves cut through snow can cause these structures to become obliterated by the caves. Somewhat similar problems have already happened to diorite, andesite, and granite in the new village structures, as they could get replaced by ores and other stone types.

### Comment 28: bugi74 (2019-06-10T00:28:12.888-0700)

Depends on the order of generation. If caves are carved before igloos/villages are put in, there won't be a problem (assuming the igloo/village generation coming later is smart enough to not "build" over air). If the caves/ravines are done after igloos/villages, I'd imagine it is a "natural" consequence that anything in cave's/ravine's path gets handled just as violently as the natural materials like solid rock and dirt, i.e. removed.

### Comment 29: migrated (2020-04-09T00:15:06.504-0700)

In 20w15a this affects Blackstone too

### Comment 30: migrated (2020-04-29T12:40:36.500-0700)

It’s kinda a big issue inside Mesa biomes. This may be a forgotten bug but it should affect 20w18a.

### Comment 31: migrated (2020-06-02T12:35:52.186-0700)

affects 20w22a

### Comment 32: migrated (2021-02-10T17:56:55.808-0800)

Seems to be present with the new cave generation in 21w06a

### Comment 33: migrated (2021-04-06T05:11:33.232-0700)

Affects 1.16.5 and 21w13a. but 1.16.5 isn't listed in affected versions.

### Comment 34: migrated (2021-04-22T09:31:26.005-0700)

Affects 21w16a.
I suggest fixing this by having a list of blocks that shouldn't be carved - possibly only bedrock. Caves generate pretty early, after surface builders and before all other generation features, so it shouldn't cause problems.

### Comment 35: migrated (2021-05-05T10:46:57.546-0700)

Still exists in 21w18a.

### Comment 36: syarumi (2021-09-16T13:33:38.350-0700)

Affects 21w37a, seems like it only affects snow blocks now?
They also don't cut through powder snow.

### Comment 37: ampolive (2021-09-16T17:47:01.830-0700)

After testing for a while, it seems that red sand is still not cut by cave carvers in some occasions.

### Comment 38: migrated (2021-09-16T18:37:47.465-0700)

Not cutting into powder snow is intentional according to devs' Twitter. Not sure about the rest.

### Comment 39: syarumi (2021-10-04T12:52:29.695-0700)

There are some instances where whole cave entrances might get covered in snow due to this, especially in groves / snowy slopes.
Powder snow not getting cut by caves might be intended, so ideally carvers should try to convert regular snow into powder snow, although that still won't fix snow blocks floating in the air.

### Comment 40: muzikbike (2021-10-30T13:25:14.444-0700)

Disagree with resolution. This often results in floating snow blocks, which are downright unsightly.

### Comment 41: EchoBlade (2022-02-09T00:58:29.498-0800)

Also disagree with resolution. This mountain cave looks like a giant parkour course inside, floating and isolated snow blocks EVERYWHERE. And all the cave entrances are either completely covered in snow or covered with just enough to make it a chore to get through them. Aren't cave entrances supposed to be... entrances? I'm pretty sure if cave entrances in the plains biome were blocked by a thin layer of grass, that would be considered a bug. Why is this not? It's also worth noting that grass blocks are able to spawn inside caves, but AREN'T found floating in midair inside them. Surely the same would apply to snow blocks. This hardly seems intentional, this looks like an oversight at best or laziness at worst.

### Comment 42: migrated (2022-06-03T01:38:20.236-0700)

Confirmed for 1.18.2 and 1.19-rc1.

### Comment 43: Avoma (2022-07-02T06:57:16.886-0700)

Can also confirm this behavior in 1.19. Here's an example of where this can be seen in this version.
Version: 1.19

```Seed: 7329541731365554898
Coordinates: /execute in minecraft:overworld run tp @s -806.62 122.53 133.86 -24.66 0.22```

### Comment 44: Avoma (2022-09-14T12:25:15.553-0700)

Can confirm in 1.19.2.
Version: 1.19.2

```Seed: -2055074493936140863
Coordinates: /execute in minecraft:overworld run tp @s 38775.30 94.00 -3078.96 -433.26 -17.75```

### Comment 45: migrated (2023-02-27T04:53:18.453-0800)

Can confirm in 1.19.3
