# MC-274047: Setting certain fields in NBT to invalid characters causes exceptions to be logged, potentially causing lag

**Mojira URL:** [https://bugs.mojang.com/browse/MC-274047](https://bugs.mojang.com/browse/MC-274047)

## Report details

- **Mojira categories:** Commands; Performance
- **Project:** MC
- **Issue key:** MC-274047
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2024-07-01T02:39:09.119-0700
- **Updated:** 2026-04-11T10:12:44.846-0700
- **Resolution date:** 2025-04-12T03:17:02.294-0700
- **Affects versions:** 1.21; 1.21.1 Release Candidate 1; 1.21.1; 24w33a; 24w34a; 24w35a; 24w36a; 24w37a; 24w38a; 24w39a; 24w40a; 1.21.2 Pre-Release 1; 1.21.2 Pre-Release 2; 1.21.2 Pre-Release 3; 1.21.2 Pre-Release 4; 1.21.2 Pre-Release 5; 1.21.2 Release Candidate 1; 1.21.2 Release Candidate 2; 1.21.2; 24w44a; 1.21.3; 24w45a; 1.21.4 Pre-Release 1; 1.21.4 Pre-Release 2; 1.21.4 Pre-Release 3; 1.21.4 Release Candidate 1; 1.21.4 Release Candidate 3; 1.21.4; 25w02a; 25w03a; 25w04a; 25w05a; 25w06a
- **Fix versions:** 25w07a
- **Area:** Platform
- **Votes:** 1
- **Watchers:** 2
- **Attachments:** 4
- **Attachment filenames:** FallingBlock entity with invalid LootTable.txt; FallingBlock entity with invalid Name.txt; Placing Suspicious Sand with Invalid LootTable.txt; Spawner.txt

## Description

The Bug
When setting certain NBT fields to invalid characters (such as ? and =), an exception is outputted in the log. A large amount of exceptions can cause lag to most systems.
Examples of some fields that cause errors when invalid characters are entered include RecipesUsed, LootTable, Name, and possibly more.
Steps to Reproduce (Direct)
Run the command specified for all situations below, then look in the game logs. Note if there is a stack trace exception or not.
Placing Suspicious Sand with invalid LootTable:
Place down the block this command gives you, and check the log.

```
/give @s minecraft:suspicious_sand[minecraft:block_entity_data={id:brushable_block,LootTable:"?"}]
```
FallingBlock entity with invalid Name:
This displays an error message in chat as well.
 Running the command below in a repeating command block causes high MSPT lag.

```
/summon minecraft:falling_block ~ ~ ~ {BlockState:{"Name":"?"}}
```
FallingBlock entity with invalid LootTable:

```
/summon minecraft:falling_block ~ ~ ~ {BlockState:{"Name":"suspicious_sand"},TileEntityData:{LootTable:"?"}}
```
Steps to Reproduce (Spawner)
 This may cause severe FPS lag.
Run the command below (attempting to right-click this spawn egg on the ground will also output an exception and not spawn anything):

```
/give @s minecraft:breeze_spawn_egg[minecraft:entity_data={id:arrow,inBlockState:{Name:"?"}}]
```
Place a monster spawner below you, and right-click the spawner with the spawn egg.
Run the command below while on top of the spawner:

```
/data modify block ~ ~-1 ~ SpawnData.entity.inBlockState set value {Name:"?"}
```
View the game logs and note if stack trace exceptions are spammed or not.
Observed Results
Exceptions are sometimes spammed to the game's log. In some cases, an FPS and TPS drop is noticeable. In the case of the spawner bug, errors continue to be spammed even when on the Esc menu in singleplayer.
The log file can also be huge due to these exceptions being spammed.
See the following text files for the exceptions experienced. They are all named respective to the thing which caused it.
-

-

-

-

Expected Result
There would be no spammed exceptions. Instead, an error message could be logged informing the player of the issue.

## Comments (7)

### Comment 1: migrated (2024-07-01T02:39:09.119-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: [Mod] violine1101 (2024-07-01T02:42:22.163-0700)

What's the exact exception / error message that shows up in the log when these happen? Please add that as "Observed behavior".

### Comment 3: Viradex (2024-07-01T02:54:47.977-0700)

I've added the exceptions that occur for each case in its separate text file, as otherwise, the description would be too large. Please let me know if the exceptions need to be in the description.

### Comment 4: [Mod] violine1101 (2024-07-01T03:02:57.765-0700)

Thanks, I've added the main error message to the description directly. It's possible that this counts as two distinct bugs (one for loot table, the other for name) since the error messages are different.

### Comment 5: Viradex (2024-07-01T03:05:05.310-0700)

Should I split this report into two separate bugs in that case?

### Comment 6: [Mod] violine1101 (2024-07-01T03:11:59.925-0700)

No that's not necessary. Checking the exceptions further, the "Loading entity NBT" errors are also caused by the same underlying exception of non-[a-z0-9/._-] characters in the resource location. The main issue here is that the message is spammed and the client lags.

### Comment 7: [Mod] ManosSef (2024-07-01T05:38:27.766-0700)

Can confirm.
