# MC-243458: Worldgen data packs don't work on servers at first launch

**Mojira URL:** [https://bugs.mojang.com/browse/MC-243458](https://bugs.mojang.com/browse/MC-243458)

## Report details

- **Mojira categories:** Custom Worlds; Data Packs; Dedicated Server
- **Project:** MC
- **Issue key:** MC-243458
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2021-11-30T17:33:53.977-0800
- **Updated:** 2025-04-30T06:52:54.530-0700
- **Resolution date:** 2022-09-13T00:37:39.288-0700
- **Affects versions:** 1.18; 1.18.1 Release Candidate 1; 1.18.1 Release Candidate 2; 1.18.1; 22w03a; 22w05a; 1.18.2 Pre-release 2; 1.18.2 Release Candidate 1; 1.18.2; 22w18a; 1.19 Pre-release 1; 1.19 Pre-release 2; 1.19 Release Candidate 1; 1.19 Release Candidate 2; 1.19; 22w24a
- **Fix versions:** 22w42a
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** testpack.zip

## Description

Datapacks which overwrites the default world generation do not work on servers. If you put the datapack in the world/datapacks/ folder before the server is started and the world is generated, it will not generate the specified biomes, which are specified in the datapack. After stopping the server, deleting all region files (world/region/*) and starting the server again the correct world generation is used. This can't be intedend, if this is the only way to load a worldgen-datapack on a server.

Steps to Reproduce:
- Place the server.jar in an empty folder.

- Create the folders /world/datapacks/.

- Place the testpack.zip inside the datapacks folder.

- Accept Eula and start the server.

- Join the server.

Observed Results:
The server generates a normal world ignoring the worldgen settings of the datapack. After stopping the server, deleting all the regions files and starting the server again the world is generating as defined in the datapack.

Expected Results:
The server should generate the world respecting all worldgen settings from the datapack (like it works in singleplayer).

Notes:
The testpack.zip generates a world with a testbiome, which is a copy of the plains biome, but with red skylight.

## Comments (4)

### Comment 1: migrated (2021-11-30T17:33:53.977-0800)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: isXander (2022-04-17T14:04:09.314-0700)

Cannot repeat on 1.18.2

### Comment 3: FX - PR0CESS (2022-05-10T18:28:49.775-0700)

Can confirm in 1.18.2 and 22w18a

### Comment 4: apple502j (2022-05-28T09:51:12.737-0700)

It seems like this is caused by the game loading in safe mode when level.dat file is missing.
