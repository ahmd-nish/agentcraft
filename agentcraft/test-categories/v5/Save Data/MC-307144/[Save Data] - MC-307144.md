# MC-307144: The game reads world generation data from data packs or world_gen_settings.dat inconsistently, preventing updating large biome sources

**Mojira URL:** [https://bugs.mojang.com/browse/MC-307144](https://bugs.mojang.com/browse/MC-307144)

## Report details

- **Mojira categories:** Datafixer; Save Data
- **Project:** MC
- **Issue key:** MC-307144
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2026-03-30T10:53:33.579-0700
- **Updated:** 2026-05-12T14:36:54.396-0700
- **Resolution date:** 2026-05-11T00:33:17.838-0700
- **Affects versions:** 26.1; 26.1.1; 26.1.2; 26.2 Snapshot 2; 26.2 Snapshot 3; 26.2 Snapshot 5
- **Fix versions:** 26.2 Snapshot 7
- **Area:** Platform EC
- **Votes:** 12
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** [1] 1.21.11 WorldGenSettings (7ec3b102-d807-4984-866b-82a48a2ebca0).png; [2] 26.1 world_gen_settings (546c3c0b-63e5-45e0-9136-ee4d32bc3394).png; [3] 26.1 to 1.21.11 Migration (1693c26e-9835-4a72-a8db-22b448600c74).png; [4] NBT Reading Error.log; [5] Terralith 1.21.11.zip; [6] Terralith 26.1.zip
- **Issue links:** Duplicate:inward:MC-308004:Overriding overworld dimension (world preset) with custom dimension implementation crashes the game on second world load

## Description

In 26.1, level.dat was split up, with WorldGenSettings being moved to its own world_gen_settings.dat file. However, the behaviour of this data has changed, which causes issues with updating worlds that have large custom biome sources.
1. Datapacks no longer affect worldgen settings
For 1.21.11, WorldGenSettings in the level.dat would store data regarding dimensions that were edited by a datapack. See Image 1 to view how this looks when Terralith and New in Town: Dimensions are installed. Terralith replaces the overworld preset with the full biomes list supplied by its dimension/overworld.json file, and all of New in Town’s dimensions are registered.
In 26.1, this is no longer the case - see Image 2 to view what world_gen_settings.dat looks like with the exact same datapacks installed. The overworld’s preset is still set and not replaced with Terralith’s biome source; and none of New in Town’s dimensions are registered here either. Both Terralith and New in Town: Dimensions work in game though, so I assume the game reads directly from the datapack instead of copying the data to world_gen_settings.dat.
It’s worth noting that although world_gen_settings.dat does not seem to match exactly what is happening in game, it is not completely ignored. When I created a fully Vanilla world, and then edited the world_gen_settings.dat by hand to replace the preset with a custom biomes list that consisted of a single minecraft:plains entry, re-entering the world did correctly spawn only Plains biomes, as expected.
2. Migrating from 1.21.11 to 26.1 preserves worldgen settings
Normally this seems like intended and expected behaviour, but because of the previous section, this causes inconsistencies. In Image 3, it shows what the world_gen_setting.dat file looks like when migrating a 1.21.11 world (the exact same one used for Image 1) to 26.1. Notice how the biomes list is still present. Although the data is preserved correctly through migration, it is different than Image 2, in which the world has the exact same setup, but instead was created in 26.1 instead of being migrated from 1.21.11.
There is also an odd inconsistency when the world_gen_settings.dat is deleted. One would expect for the game to (re)generate a Vanilla world_gen_settings.dat, due to the error the game puts in the log (see below) about falling back to default settings. However, the file still has the biomes list as if it was migrated from 1.21.11 to 26.1, instead of being freshly (re)generated in 26.1. I am unaware of any caching of world_gen_settings.dat, so I wonder if the game reads from installed datapacks, which is different than the behaviour shown in the first section.

```
[Worker-Main-60/ERROR]:Unable to read or access the world gen settings file! Falling back to the default settings with a random world seed. /path/to/data/minecraft/world_gen_settings.dat
```
3. NBT tags in 26.1 worldgen settings have a size limit
For some reason, the game has an issue reading NBT tags that are too large inside world_gen_settings.dat - it throws a NbtAccounterException, and prevents the world from loading. See Attachment 4 for the full log file when this happens, or right below this paragraph for the expanded line.

```
java.util.concurrent.ExecutionException: net.minecraft.nbt.NbtAccounterException: Tried to read NBT tag that was too big; tried to allocate: 2097146 + 8 bytes where max allowed: 2097152
```
This is not an issue for worlds newly created in 26.1; as explained in the first section, the game seems to read the dimension data directly from the datapack itself instead of writing to world_gen_settings.dat. However, this can trigger when the behaviour from section 2 migrates a very large biomes list from 1.21.11’s WorldGenSettings to 26.1’s world_gen_settings.dat.
Why is this a problem? (Recap)
A user has created a world in 1.21.11 using a datapack with a very large custom biome source. The user wants to upgrade their world to 26.1, so they update Minecraft to 26.1 and swap to the 26.1 version of their datapack. They click “Upgrade and Play” on their world, which has the game migrate the WorldGenSettings from their world’s level.dat to the new world_gen_settings.dat file. However, because the biomes list is too big of an NBT tag for the game to read in world_gen_settings.dat, the world cannot load.
Unfortunately, this is not straightforward for the user to remedy either. If they simply delete the world_gen_settings.dat, the too-large biomes NBT tag is rewritten into the file again. They could create a fresh world in 26.1 with their datapack installed and then move over the world_gen_settings.dat into their existing world, but they must be very careful to use the same seed so the world does not suddenly change seeds.
How to reproduce
- Create a 1.21.11 world with Terralith installed (see Attachment 5).

- Save and exit the world, quit the game, then upgrade your instance from 1.21.11 to 26.1.

- Inside your world’s files, delete the 1.21.11 version of Terralith and replace it with the 26.1 version (see Attachment 6).

- Start your newly updated 26.1 instance, find your test world, and click “Upgrade and Play”.

- Attempt to join the world, and observe the game prevents you from joining due to errors in datapack or level data.

## Comments (1)

### Comment 1: Automation for Jira (2026-03-30T10:53:40.856-0700)

Thank you for helping us improve Minecraft! We saved your files:
[^[1] 1.21.11 WorldGenSettings (7ec3b102-d807-4984-866b-82a48a2ebca0).png]
[^[2] 26.1 world_gen_settings (546c3c0b-63e5-45e0-9136-ee4d32bc3394).png]
[^[3] 26.1 to 1.21.11 Migration (1693c26e-9835-4a72-a8db-22b448600c74).png]
[^[4] NBT Reading Error.log]
[^[5] Terralith 1.21.11.zip]
[^[6] Terralith 26.1.zip]
