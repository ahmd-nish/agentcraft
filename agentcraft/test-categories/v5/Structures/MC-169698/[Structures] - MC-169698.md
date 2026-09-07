# MC-169698: Blocks within igloo basements can generate waterlogged when generating in close proximity to water

**Mojira URL:** [https://bugs.mojang.com/browse/MC-169698](https://bugs.mojang.com/browse/MC-169698)

## Report details

- **Mojira categories:** Structures; World generation
- **Project:** MC
- **Issue key:** MC-169698
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2020-01-10T17:24:34.081-0800
- **Updated:** 2025-04-29T09:09:35.653-0700
- **Resolution date:** 2024-05-27T09:00:35.085-0700
- **Affects versions:** 1.15.1; 1.15.2 Pre-Release 1; 1.15.2 Pre-release 2; 1.16.2 Pre-release 1; 1.16.2; 20w51a; 1.16.5; 21w05b; 21w06a; 21w08b; 21w10a; 1.17.1; 21w37a; 21w38a; 21w42a; 21w43a; 1.18 Pre-release 2; 1.18 Release Candidate 4; 1.18; 1.18.1; 1.19; 1.19.2; 22w42a; 1.19.3; 1.19.4; 23w33a; 24w11a; 24w19b; 24w21b
- **Fix versions:** 1.21 Pre-Release 1
- **Area:** Platform
- **Labels:** igloo
- **Watchers:** 1
- **Attachments:** 9
- **Attachment filenames:** 2021-02-06_13.54.28.png; 2021-02-06_13.55.05.png; 2021-03-14_13.49.22.png; 2024-05-24_19.10.34.png; custom-structure_chest-not-waterlogged-has-AIR-around-it.png; custom-structure-loaded-in-water-should-NOT-have-waterlogged-chest.png; MC-169698.mp4; MC-169698 - 1.19.png; MC-169698 - Iron Bars Example.png
- **Issue links:** Relates:outward:MC-140270:Spawning a structure with waterloggable blocks next to or inside a water source will waterlog the structure | Duplicate:inward:MC-208904:water in a ladder block | Duplicate:inward:MC-217665:Waterlogged ladders | Duplicate:inward:MC-232167:Local water level is not avoided in igloos | Duplicate:inward:MC-236607:Flooded caves flood the ladder section of igloo basements | Duplicate:inward:MC-239455:Flooded Stairs in Igloo | Duplicate:inward:MC-241685:Flooded stairs in igloo | Duplicate:inward:MC-243132:Igloo ladder is waterlogged.

## Description

The Bug:
Blocks within igloo basements can generate waterlogged when generating in close proximity to water.
This issue can most commonly be seen with ladders in igloo basements, but also more rarely occurs with other blocks within the basements as well, such as iron bars.
Here is an example:
Version: 1.19.4

```
Seed: -2178309719778189280
Coordinates: /execute in minecraft:overworld run tp @s 318147.98 30.00 -1419.00 390.27 -66.60
```
Steps to Reproduce:
- Generate a world with the seed provided above and teleport to the given coordinates.

- Look at the blocks within the igloo closely.

- Take note as to whether or not blocks within igloo basements can generate waterlogged when generating in close proximity to water.

Observed Behavior:
Blocks can generate waterlogged.
Expected Behavior:
Blocks would not be able to generate waterlogged.

## Comments (20)

### Comment 1: migrated (2020-01-10T17:24:34.081-0800)

This comment contained multiple image attachments (9), please login to view the attachments.

### Comment 2: migrated (2020-07-31T07:56:28.987-0700)

Still present in 1.16.2 pre-release in seed: 1234567 at /tp 10579 62 2917
This bug has been around for a while but this is the only issue report I can find of it. But anyway, this seems to only happen when structures that generate from nbt files have their blocks replacing water that already exists in the world. The easiest case to find of this is Igloos generating in river biomes. Once one ladder gets waterlogged, the rest gets all waterlogged immediately upon generation which is quite a strange effect that would limit what people can do with customized structures.
It's might also possibly related to the bug where if you save a structure nbt file where you have non-waterlogged stairs surround a water source block, the stairs will become waterlogged when the nbt file is used in structure generation in worldgen (not by structure blocks)

### Comment 3: migrated (2020-08-14T13:37:56.089-0700)

Still present in 1.16.2 full release

### Comment 4: Avoma (2021-02-05T08:37:14.263-0800)

The provided seed and coordinates no longer work in 21w05b.

### Comment 5: Avoma (2021-03-14T06:50:56.319-0700)

Can confirm that this is still an issue in 21w10a. Here's an example of where you can see this, since the current seed + coordinates no longer work.

```Seed: 5872367957045336565
Coordinates: /execute in minecraft:overworld run tp @s 2354.80 36.00 -2890.92 290.59 -64.21```

### Comment 6: Avoma (2021-07-22T10:40:38.890-0700)

Can confirm in 1.17.1.

### Comment 7: migrated (2021-09-17T04:53:34.357-0700)

I have the same seed on accident! What the hell!

### Comment 8: migrated (2021-09-19T11:03:48.409-0700)

Can confirm in 21w37a

### Comment 9: migrated (2021-10-27T10:01:25.384-0700)

Just found one in 21w43a

### Comment 10: MMK21 (2021-12-11T23:28:17.783-0800)

Affects 1.18.1
New seed and coordinates (from MC-241685):

```6456867176503131171
/tp @s -457.5 31 229.5```

### Comment 11: migrated (2022-02-06T12:19:49.217-0800)

Can confirm still an issue in 1.18.1.
Note that when this occurs, this can affect more than just the stairs; multiple items in the igloo basement can be waterlogged, including the iron bars, the sign, the chest, and the side table (which is built from wooden stairs and a slab).

### Comment 12: clamlol (2022-02-24T13:00:00.160-0800)

This seems like a special case of [MC-140270].

### Comment 13: Avoma (2022-06-30T04:26:57.341-0700)

Can confirm in 1.19.
Version: 1.19

```Seed: 3032665062407875672
Coordinates: /execute in minecraft:overworld run tp @s 15539.79 64.20 5156.96 395.42 67.50```

### Comment 14: Avoma (2022-06-30T04:38:05.191-0700)

Additionally, as partially mentioned above already, this also affects any blocks within this structure that can be waterlogged. As an example in the details provided below, you can see this issue occurring with iron bars.
Version: 1.19

```Seed: 3032665062407875672
Coordinates: /execute in minecraft:overworld run tp @s 26917.11 44.93 7031.30 -327.73 23.41```

### Comment 15: migrated (2022-07-18T02:55:29.799-0700)

I think this has merit to be resolved, both for vanilla, and for custom datapacks and structures, as it is rather frustrating.
The place we see a high impact, is custom datapack generation (often, but not limited to, structures), or copying structures between worlds .... many people create ships, with cabins under water, or whatever the structure is that requires air pockets.
In cases like that, if a block that can be waterlogged is stored in an NBT structure file when NOT waterlogged .... when the structure is generated, those blocks should not be waterlogged.
The only scenario I can see where you "want" these blocks to be waterlogged ..... is if (in post generation) that block finds itself between 2 source water blocks.... then sure, it must  become waterlogged.
I've attached example pictures of a custom-structure that has been saved (with NO structure_void around the chest - explicit air blocks) ...
When it is loaded beneath water ... the chest alone is waterlogged ... which is incorrect, there are no source water blocks around it, and it was not waterlogged when it was saved in the structure NBT file.

### Comment 16: migrated (2022-07-18T09:01:49.140-0700)

Kai, that's MC-140270.

### Comment 17: Avoma (2022-09-17T04:11:30.861-0700)

Can confirm in 1.19.2.
Version: 1.19.2

```Seed: -2178309719778189280
Coordinates: /execute in minecraft:overworld run tp @s 318147.98 30.00 -1419.00 390.27 -66.60```

### Comment 18: migrated (2022-12-28T09:33:28.979-0800)

@Dhranios - Based on my understanding of this bug, that specific ticket you mentioned is actually the parent of this one... I believe this one should be closed as a duplicate thereof and the problem should be worked out for all structures, not igloos specifically

Based on my comments on that ticket (MC-140270)...

Here is an example affecting 1.19.3
Seed: -9066070196958847497
Coords: /execute in minecraft:overworld run tp @s -13549.54 60.67 -8508.50 236.25 31.80{*}{*}

### Comment 19: windwend (2023-08-30T12:07:03.252-0700)

Can confirm in 1.20.1.

### Comment 20: COMETC2021A1 (2024-05-10T09:45:44.181-0700)

Can confirm in 24w19b.
