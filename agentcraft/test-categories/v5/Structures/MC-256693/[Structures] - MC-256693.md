# MC-256693: Allays that are holding items ignore note blocks when loaded from structure blocks

**Mojira URL:** [https://bugs.mojang.com/browse/MC-256693](https://bugs.mojang.com/browse/MC-256693)

## Report details

- **Mojira categories:** Mob behaviour; Structures
- **Project:** MC
- **Issue key:** MC-256693
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-10-20T08:11:39.094-0700
- **Updated:** 2025-04-30T04:33:38.819-0700
- **Resolution date:** 2023-05-12T12:00:52.715-0700
- **Affects versions:** 1.19.2; 1.19.3 Release Candidate 3; 1.19.3; 23w04a
- **Fix versions:** 22w42a
- **Area:** Platform
- **Labels:** allay; structure_block
- **Watchers:** 1
- **Attachments:** 5
- **Attachment filenames:** better_moss_farm.nbt; MC-256693.mp4; mc-256693.nbt; MC-256693 - 1.19.2.mp4; MC-256693 - 22w42a (Fixed).mp4

## Description

The Bug:
Allays that are holding items ignore note blocks when loaded from structure blocks.
Saving a structure containing an allay (using a structure block with "Include Entities" on) and loading it in another world causes the allay in the imported structure to ignore note blocks in the position that the structure had a note block. (Newly spawned allays work as expected) Haven't tested whether reloading the world or using a note block in a different position works.
Steps to Reproduce:
- Download the provided structure block .nbt file that contains an empty structure that has an allay holding a gold block within it.

- Create a world and place the .nbt file into the generated\minecraft\structures folder.

- Place down a structure block with the appropriate data already inputted into it by using the command provided below.

```
/setblock ~1 ~ ~1 minecraft:structure_block{ignoreEntities:0b,mode:"LOAD",name:"minecraft:mc-256693",posX:1,posY:0,posZ:1,powered:0b,showboundingbox:1b,sizeX:5,sizeY:5,sizeZ:5}
```

- Open the structure block and click the "LOAD" button to load the structure.

- Obtain a note block and some gold blocks.

- Place down the note block and right-click it while the allay is nearby in an attempt to make the allay like the note block.

- Throw some gold blocks on the ground and wait for the allay to collect them.

- Take note of how the allay ignores the note block and decides to drop the held items at your location instead.

Observed Behavior:
Allays ignore note blocks.
Expected Behavior:
Allays would not ignore note blocks.

## Comments (4)

### Comment 1: migrated (2022-10-20T08:11:39.094-0700)

This comment contained multiple image attachments (5), please login to view the attachments.

### Comment 2: Avoma (2022-12-06T09:58:33.258-0800)

Confirmed. I've rewritten this report to clearly state the problem here and how you can easily go about reproducing it. I've also provided a video that demonstrates this behavior. I had to narrate the video as I didn't have time to annotate it in Adobe Premiere Pro like I normally would. Hope this is okay.

### Comment 3: Brain81505 (2023-01-31T05:59:07.813-0800)

Can confirm in 23w04a

### Comment 4: Avoma (2023-04-25T06:29:05.324-0700)

This issue was present in 1.19.2, but no longer occurs in versions above or equal to 22w42a. This issue was fixed in 22w42a. I'm not sure why both 1.19.3 and 23w04a as marked as affected, because I was unable to reproduce this problem in both of these versions. I've provided video evidence that this problem was broken in 1.19.2 and fixed in 22w42a.
