# MC-236295: The game does not report absent particle texture references in models to the output log

**Mojira URL:** [https://bugs.mojang.com/browse/MC-236295](https://bugs.mojang.com/browse/MC-236295)

## Report details

- **Mojira categories:** Debug; Resource Packs
- **Project:** MC
- **Issue key:** MC-236295
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2021-09-10T15:43:25.935-0700
- **Updated:** 2025-04-26T13:49:35.006-0700
- **Resolution date:** 2024-11-06T08:35:46.622-0800
- **Affects versions:** 1.17.1; 21w38a; 1.19; 1.19.2
- **Fix versions:** 24w45a
- **Watchers:** 1
- **Attachments:** 8
- **Attachment filenames:** 2021-09-10_23.28.14.png; 2021-09-10_23.29.55.png; 2021-09-10_23.30.22.png; 2021-09-10_23.31.42.png; stone-invalid-block-texture.zip; stone-invalid-particle-texture.zip; stone-no-block-texture.zip; stone-no-particle-texture.zip
- **Issue links:** Relates:inward:MC-263121:Missing textures caused by atlas filtering do not always cause errors to appear in the game output log | Relates:inward:MC-270529:Air's model does not define a particle texture, causing issues

## Description

The bug
The game does not output empty particle texture reference warnings in the console at all, even though it results in use of the missing texture.
How to reproduce
Attached are four resource packs which each modify the model for minecraft:stone. These resource packs should be applied independently of each other.
For the purpose of this report, each of the four resource packs is made to be flawed in some sense, as to demonstrate specific cases of absent or invalid references to textures, and the game's reaction to each:
- stone-no-block-texture does not reference a texture to use for the block itself

- stone-invalid-block-texture references a nonexistent texture to use for the block

- stone-no-particle-texture does not reference a texture to use for the particles produced by the block

- stone-invalid-particle-texture references a nonexistent texture to use for the particles produced by the block

To reproduce this issue, firstly make sure no other resource packs are applied, and then:
- Apply one of the four resource packs

- Pay close attention to the game's output log to check for any errors with the resource packs, noting which errors appear with each pack

- Once the resource pack is done loading, place and break stone blocks to check for missing textures, noting where they occur

- Repeat this with the other three resource packs

Expected result
As the missing texture is never, under any circumstances, meant to be used or seen in-game, outside of cases where resources are misconfigured to a point where it must show up, it'd be expected that a warning be shown in the game logs regarding the use of the texture to notify resource pack developers to its presence in cases that may otherwise be overlooked.
Actual result
The game only appears to output an explicit error in cases where an invalid texture is specified.
- stone-no-block-texture:
- Unable to resolve texture reference: #texture in minecraft:block/stone

- The block uses the missing texture on all sides:

-

- stone-invalid-block-texture:
- Using missing texture, unable to load minecraft:textures/block/nonexistent_texture.png : java.io.FileNotFoundException: minecraft:textures/block/nonexistent_texture.png

- The block uses the missing texture on all sides:

-

- stone-no-particle-texture:
- Absolutely no console output at all indicating that a missing texture is used!

- The block uses the missing texture for its particles:

-

- stone-invalid-particle-texture:
- Using missing texture, unable to load minecraft:textures/block/nonexistent_texture.png : java.io.FileNotFoundException: minecraft:textures/block/nonexistent_texture.png

- The block uses the missing texture for its particles:

-

Further notes
Not only is this internally inconsistent among these four detailed cases, it's also inconsistent with other related resource pack errors, such as invalid models, blockstates files referencing nonexistent models, sound events pointing to nonexistent sounds, and so on.
In addition, the unresolved texture reference output for textures which do in fact see direct use within the model could be considered somewhat incomplete, as it doesn't explicitly announce that the missing texture will be used, only hinting that there may be one. I can't think of any cases where the message would show up where the missing texture wouldn't end up being used, however it might be a good idea to output the "Using missing texture" error after such cases as well.
Errors should only be reported by models which end up being directly used in the game - template models which define no textures by themselves but are referenced by other models which apply their own textures should not report anything to the log.

## Comments (2)

### Comment 1: migrated (2021-09-10T15:43:25.935-0700)

This comment contained multiple image attachments (8), please login to view the attachments.

### Comment 2: muzikbike (2024-11-06T07:36:27.271-0800)

Fixed in 24w45a.
