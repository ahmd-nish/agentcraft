# MC-280155: Random ticks can cause entity build-up in lazy chunks

**Mojira URL:** [https://bugs.mojang.com/browse/MC-280155](https://bugs.mojang.com/browse/MC-280155)

## Report details

- **Mojira categories:** Chunk loading; Performance
- **Project:** MC
- **Issue key:** MC-280155
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2025-02-06T02:44:27.863-0800
- **Updated:** 2026-03-11T03:45:48.118-0700
- **Resolution date:** 2025-02-26T05:52:31.165-0800
- **Affects versions:** 25w06a
- **Fix versions:** 25w09a
- **Area:** Platform HC
- **Labels:** block; lag; server; world
- **Votes:** 2
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** image_2025-02-06_103321779.png; image_2025-02-06_104336231.png

## Description

Summary:
Due to the new changes with random ticks in loaded chunks away from the player, item entities can be created due to a random tick interaction in a non-entity-processing chunk and will not begin to despawn until the chunk they are in becomes entity-processing. This could lead to undesirable and accidental item build-up that may cause high MSPT or crash servers. A realistically common example of this may be a chunk being loaded for an extended duration while being unintentionally near a player-built cactus, sugar cane, pumpkin/melon, or bamboo farm that automatically harvests the crops through any block-based interactions (such as pistons extending, or cacti naturally popping off when grown adjacent to a block).
This seems unintentional and could be especially dangerous in the edge case where a cactus may have naturally generated within the lazy spawn chunks in a way that causes it to break upon growth due to the surrounding terrain or structures.
Suggested Fix:
Allowing random ticks to only occur within entity-processing chunks would greatly reduce the chances of this happening and better align with the spirit of the change.
Steps To Reproduce:
1. Create an empty or superflat creative world and use all of the following commands to ensure a clean test:

```
/gamerule doMobSpawning false
/gamerule spawnChunkRadius 0
/tp @e[type=!minecraft:player] ~ -1000 ~
```
2. Set up a dummy scoreboard objective to track the number of loaded entities as follows:

```
/scoreboard objectives add entities dummy
/scoreboard objectives setdisplay sidebar entities
```
3. Enable the Chunk borders display using F3 + G and Stand somewhere within the middle of a chunk. Place an easily discernible block to mark this chunk so you don't lose it.
Forceload the chunk you are standing in using the command:

```
/forceload add ~ ~
```
4. Move to the next chunk over in any cardinal or ordinal direction and place a block of sand with a cactus planted on top and a stable block placed diagonally one block upwards and one block adjacent in any cardinal direction from the cactus (an image of this setup is attached below)
5. Enter spectator mode via F3 + N and use the command:

```
/gamerule spectatorsGenerateChunks false
```
This will ensure you do not interfere with the simulated area
6. Now allow the cactus to randomly tick and break on the block to generate cactus items. You can check how many exist currently using your scoreboard and the command:

```
/execute store result score @s entities if entity @e[type=item, nbt={"Item":{"id":"minecraft:cactus"}}]
```
You can speed up the process by increasing the random tick speed (to a number that your system can reasonably handle), and even view that the items build-up and don't despawn by fast-forwarding 6000 ticks (item despawn time) as they are not in entity processing chunks. Those commands are as follows:

```
/gamerule randomTickSpeed 3000
```
(to check for build-up, wait for items to appear, then run the next commands)

```
/tick freeze
/gamerule randomTickSpeed 0
/execute store result score @s entities if entity @e[type=item, nbt={"Item":{"id":"minecraft:cactus"}}]
/tick sprint 6000
/execute store result score @s entities if entity @e[type=item, nbt={"Item":{"id":"minecraft:cactus"}}]
```
You should observe the same number of items, indicating that the entities are not being ticked and will not despawn.
Expected Result:
The cactus should not grow as it resides in lazy chunks, preventing any potentially unwanted entities from being instantiated.
Observed Result:
The cactus continues to grow and break, amassing many item entities that do not age nor despawn.

## Comments (1)

### Comment 1: migrated (2025-02-06T02:44:27.863-0800)

This comment contained multiple image attachments (2), please login to view the attachments.
