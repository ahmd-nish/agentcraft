# MC-202036: Adding a biome to a datapack shifts biome IDs in existing chunks

**Mojira URL:** [https://bugs.mojang.com/browse/MC-202036](https://bugs.mojang.com/browse/MC-202036)

## Report details

- **Mojira categories:** Custom Worlds
- **Project:** MC
- **Issue key:** MC-202036
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2020-10-12T07:08:32.613-0700
- **Updated:** 2025-05-02T00:39:02.852-0700
- **Resolution date:** 2021-10-11T19:17:11.896-0700
- **Affects versions:** 20w30a; 1.16.3; 1.16.4 Release Candidate 1; 1.16.4; 20w46a; 21w03a; 1.16.5; 21w17a; 1.17.1
- **Fix versions:** 21w38a
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** Incendium_v3.0.3.zip; Incendium v3.1.zip
- **Issue links:** Duplicate:inward:MC-196336:Custom Biome map changes on relog | Duplicate:inward:MC-196388:Custom Biome map changes on relog.

## Description

When a datapack with custom biomes is loaded, the biomes it defines are assigned IDs according to their lexicographic order. When a new biome is added to an existing world but its name gets sorted anywhere else than at the end, it causes the biomes that follow it to shift. Chunks only store the resulting IDs in their biome maps and not the names, so they become corrupted, showing the biome that precedes the correct one.

This can be quite easily fixed if chunks stored not only the biome IDs, but also a mapping that allowed retrieving the actual name, kinda like the block palette already works for a chunk section. Since there is usually only one biome per chunk, it's just a matter of storing one additional pair in the chunk data. This would also make it possible to define more than 256 biomes for a world.

## Comments (12)

### Comment 1: migrated (2020-10-12T07:08:32.613-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: migrated (2020-10-12T07:10:37.643-0700)

Uhm, this was supposed to be created for Minecraft: Java Edition. Can it be moved?

### Comment 3: migrated (2020-10-12T07:38:33.196-0700)

No, but you can tell the mods to move to the right project

### Comment 4: migrated (2020-10-12T07:38:56.314-0700)

But otherwise, this will be resolved as invalid by a mod

### Comment 5: migrated (2020-10-13T07:09:17.814-0700)

I've moved the report.
Can you please check the affected version and update if needed.

### Comment 6: tryashtar (2020-10-28T20:29:28.012-0700)

Please add a datapack/steps to reproduce

### Comment 7: Starmute (2020-10-28T20:29:29.327-0700)

Affects 1.16.4-RC

### Comment 8: Starmute (2020-10-28T20:33:12.048-0700)

I've added two versions of a datapack which can be used for testing purposes. Install v3.0.3 first, load some chunks in the Nether, and then delete it and install v3.1.

### Comment 9: migrated (2021-08-12T05:23:09.007-0700)

Confirmed for 1.17.1.

### Comment 10: migrated (2021-08-12T07:41:14.941-0700)

Requesting the title to be changed to be a bit more accurate:
1. only custom biome IDs get shifted
2. vanilla adding biomes also shifts them
3. mention the core issue
Suggested title: Addition of new biomes shifts IDs of custom biomes from data packs due to missing ID mapping

### Comment 11: migrated (2021-09-29T10:16:51.069-0700)

Seems fixed in the newest snapshot with the chunk format changes:
Chunk’s Level.Biomes are now paletted and live in a similar container structure in Level.Sections[].biomes

### Comment 12: migrated (2021-10-08T08:14:02.843-0700)

(@Dhranios)
Fixed, game internals use biome name instead of whole biome list in code now
