# MC-117574: Using /setblock or /fill to re-place a block entity keeps old NBT (if no NBT specified) but clears inventories, even when the command fails

**Mojira URL:** [https://bugs.mojang.com/browse/MC-117574](https://bugs.mojang.com/browse/MC-117574)

## Report details

- **Mojira categories:** Block states; Commands
- **Project:** MC
- **Issue key:** MC-117574
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2017-05-17T09:31:47.785-0700
- **Updated:** 2025-05-27T07:46:21.092-0700
- **Resolution date:** 2025-01-08T14:41:49.035-0800
- **Affects versions:** Minecraft 1.12 Pre-Release 3; Minecraft 1.12 Pre-Release 4; Minecraft 1.12 Pre-Release 5; Minecraft 1.12 Pre-Release 6; Minecraft 1.12 Pre-Release 7; Minecraft 1.12; Minecraft 1.12.1; Minecraft 1.12.2; Minecraft 17w46a; Minecraft 17w47b; Minecraft 17w48a; Minecraft 17w50a; Minecraft 18w01a; Minecraft 18w03b; Minecraft 18w08b; Minecraft 18w11a; Minecraft 18w19b; Minecraft 1.13-pre1; Minecraft 1.13-pre2; Minecraft 1.13-pre3; Minecraft 1.13-pre4; Minecraft 1.13-pre5; Minecraft 1.13-pre6; Minecraft 1.13-pre7; Minecraft 1.13-pre8; Minecraft 1.13-pre9; Minecraft 1.13-pre10; Minecraft 1.13; Minecraft 18w30a; Minecraft 18w30b; Minecraft 18w31a; Minecraft 18w32a; Minecraft 18w33a; Minecraft 1.13.1-pre1; Minecraft 1.13.1-pre2; Minecraft 1.13.1; Minecraft 1.13.2-pre1; Minecraft 1.13.2-pre2; Minecraft 1.13.2; Minecraft 18w43a; Minecraft 18w43b; Minecraft 18w43c; Minecraft 18w44a; Minecraft 18w45a; Minecraft 18w46a; Minecraft 18w47a; Minecraft 18w47b; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 19w02a; Minecraft 19w03a; Minecraft 19w03b; Minecraft 19w03c; Minecraft 19w04b; Minecraft 19w05a; Minecraft 19w06a; Minecraft 19w07a; Minecraft 19w08a; Minecraft 19w08b; Minecraft 19w09a; Minecraft 19w11a; Minecraft 19w11b; Minecraft 19w12a; Minecraft 19w12b; Minecraft 19w13a; Minecraft 19w13b; Minecraft 19w14a; Minecraft 19w14b; Minecraft 1.14 Pre-Release 1; Minecraft 1.14 Pre-Release 2; Minecraft 1.14 Pre-Release 3; Minecraft 1.14 Pre-Release 4; Minecraft 1.14 Pre-Release 5; Minecraft 1.14; Minecraft 1.14.1 Pre-Release 1; Minecraft 1.14.1 Pre-Release 2; Minecraft 1.14.1; Minecraft 1.14.2 Pre-Release 1; Minecraft 1.14.2 Pre-Release 2; Minecraft 1.14.2 Pre-Release 3; Minecraft 1.14.2 Pre-Release 4; Minecraft 1.14.2; Minecraft 1.14.3 Pre-Release 2; Minecraft 1.14.3 Pre-Release 3; Minecraft 1.14.3 Pre-Release 4; Minecraft 1.14.3; Minecraft 1.14.4 Pre-Release 1; Minecraft 1.14.4 Pre-Release 2; Minecraft 1.14.4 Pre-Release 3; Minecraft 1.14.4 Pre-Release 4; Minecraft 1.14.4 Pre-Release 5; Minecraft 1.14.4 Pre-Release 6; 1.14.4 Pre-Release 7; 1.14.4; 19w34a; 19w35a; 19w36a; 19w37a; 19w38b; 19w39a; 19w40a; 19w41a; 19w42a; 19w45b; 19w46b; 1.15 Pre-release 1; 1.15 Pre-Release 2; 1.15 Pre-release 3; 1.15 Pre-release 4; 1.15 Pre-release 5; 1.15 Pre-release 6; 1.15 Pre-release 7; 1.15; 1.15.1; 1.15.1 Pre-release 1; 1.15.2 Pre-Release 1; 1.15.2 Pre-release 2; 1.15.2; 20w06a; 20w07a; 20w08a; 20w09a; 20w10a; 20w11a; 20w13a; 20w13b; 20w15a; 20w17a; 20w18a; 20w19a; 20w20a; 20w20b; 20w21a; 20w22a; 1.16 Pre-release 1; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 4; 1.16 Pre-release 5; 1.16 Pre-release 6; 1.16 Pre-release 7; 1.16 Pre-release 8; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w27a; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Pre-release 2; 1.16.2 Pre-release 3; 1.16.2 Release Candidate 1; 1.16.2 Release Candidate 2; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4 Pre-release 1; 1.16.4 Pre-release 2; 1.16.4 Release Candidate 1; 1.16.4; 20w46a; 20w48a; 20w51a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w11a; 1.17 Pre-release 2; 1.17; 23w07a; 1.19.4; 1.20 Pre-release 6; 1.20.2; 1.20.4; 24w13a; 24w44a; 1.21.3; 1.21.4
- **Fix versions:** 25w02a
- **Area:** Platform
- **Labels:** /fill; /setblock; block; block-data; command; nbt; nbt-tags; replace
- **Watchers:** 2
- **Attachments:** 0
- **Issue links:** Duplicate:inward:MC-278825:/Setblock will remove container data but fail. | Relates:outward:MC-50166:Game states that "The block couldn't be placed" when using /setblock to place air in a space occupied by a tile entity, despite working | Duplicate:inward:MC-262998:Lectern don't update with mcfunction | Duplicate:inward:MC-260399:setblock of decorated pot won't replace pot with different NBT | Duplicate:inward:MC-202388:/setblock command will lose nbt data （e.g chest） | Relates:outward:MC-30995:/setblock replace doesn't replace same block with different tile entity / NBT data | Duplicate:inward:MC-136829:When using /setblock to place a chest at the same location twice, chest contents get deleted | Duplicate:inward:MC-123648:Loot_table Bug | Duplicate:inward:MC-122836:/setblock Keeps Data From Blocks It Replaces | Duplicate:inward:MC-120438:Signs don't replace signs | Duplicate:inward:MC-119826:Cannot setblock a sign on the position of another sign | Duplicate:inward:MC-119806:Skulls bug | Duplicate:inward:MC-119249:setblock replace not working for mob_spawners | Duplicate:inward:MC-118677:Return "No block filled" when try to empty chest with /fill command

## Description

The bug
When using /setblock or /fill to replace a block entity, this keeps the old NBT (if no NBT is specified), but clears the inventories, even if the command fails.
Additionally, the command will fail if the specified block state matches the existing one, even if there is new NBT to apply. The result is only inventories clearing.
How to reproduce
- Example 1:

```
/setblock ~1 ~ ~ dropper[facing=up]{CustomName:"\"first\"",Items:[{id:stone,Count:1b,Slot:0b}]}
```
This places a dropper as expected. Now run the following command:

```
/setblock ~1 ~ ~ dropper[facing=up]{CustomName:"\"updated\"",Items:[{id:stone,Count:1b,Slot:0b}]}
```
Expected behavior: command succeeds (because NBT differs), dropper updates name.
Actual behavior: command fails (because the blockstates are the same), dropper does not update name, inventory clear.
Note: Leaving off the NBT in the last command has the same effect.

- Example 2:

```
/setblock ~1 ~ ~ command_block[facing=up]{Command:"first"}
```
This places a command block as expected. Now run the following command:

```
/setblock ~1 ~ ~ command_block[facing=down]
```
Expected behavior: command block is empty
Actual behavior: command block contains the command "first".
Note: including NBT in the last command successfully places a new block as expected.

## Comments (33)

### Comment 1: migrated (2017-05-17T18:32:54.552-0700)

The bug seems to completely erase the nbt data of the block, to reprodice simply put this command in a command block and run it twice.

```setblock ~ ~1 ~ dropper facing=up replace {Items:[{id:"minecraft:stone",Count:1b}]}```
The first time the command is run there will be a stone block in the dropper and the second time the dropper will be empty.

### Comment 2: tryashtar (2017-05-17T19:07:15.883-0700)

Hey @Bertie2011, we did some testing and I rewrote your report to be more detailed. Hope you don't mind!

### Comment 3: migrated (2017-05-18T00:18:53.137-0700)

@tryashtar
No, I don't mind. I didn't have much time to test things out, thanks for expanding my post =)

### Comment 4: marcono1234 (2017-05-18T04:30:38.160-0700)

Could be related to MC-50166 since replacing all blocks with air / barrier blocks first was likely done to remove tile entities.

### Comment 5: migrated (2017-05-18T08:23:04.299-0700)

Confirmed in Minecraft 1.12 Pre Release 4

### Comment 6: migrated (2017-05-19T07:53:18.221-0700)

Confirmed in Minecraft 1.12 Pre Release 5

### Comment 7: insane96mcp (2017-06-03T02:53:20.455-0700)

Can confirm for 1.12 Pre-7

### Comment 8: migrated (2017-06-07T08:58:52.170-0700)

Confirmed for 1.12!
I hoped that the delay would mean a fix before the release.
EDIT:
Possible temporary fix for map makers: Use the destroy argument instead of the replace argument and make sure to do: /gamerule doTileDrops false. This prevents the block to appear as item after destruction.

### Comment 9: migrated (2017-08-29T13:59:30.270-0700)

The same issue with me, too!

### Comment 10: tryashtar (2017-11-17T19:03:49.414-0800)

Was not fixed with the new command system. Updated the syntax of the commands to 1.13's format.

### Comment 11: blablubbabc (2017-12-15T18:53:31.344-0800)

Confirmed for snapshot 17w50a. Hope this finds its way into 1.13, with all those nbt-related command changes.

### Comment 12: lord.quadrato (2018-06-15T09:59:34.198-0700)

Confirmed for 1.13-pre2

### Comment 13: AlexMCool (2018-06-26T07:03:06.640-0700)

Affects 1.13-pre4

### Comment 14: AlexMCool (2018-06-28T08:02:26.356-0700)

Affects 1.13-pre5

### Comment 15: AlexMCool (2018-07-04T06:29:13.491-0700)

Affects 1.13-pre6

### Comment 16: AlexMCool (2018-07-10T10:56:29.640-0700)

Affects 1.13-pre7

### Comment 17: AlexMCool (2018-07-13T08:09:24.058-0700)

And 1.13-pre8

### Comment 18: AlexMCool (2018-07-16T08:25:56.853-0700)

And 1.13-pre9

### Comment 19: AlexMCool (2018-07-19T02:57:24.618-0700)

And 1.13

### Comment 20: AlexMCool (2018-07-25T09:44:33.841-0700)

And 18w30a

### Comment 21: AlexMCool (2018-07-26T10:47:46.130-0700)

And 18w30b

### Comment 22: AlexMCool (2018-08-01T11:04:59.543-0700)

And 18w31a

### Comment 23: migrated (2018-11-18T22:44:15.667-0800)

Confirmed for 18w46a.

### Comment 24: ZeNico13 (2019-02-20T08:25:06.701-0800)

Still in 19w08a

### Comment 25: migrated (2019-03-14T08:29:59.303-0700)

Please do not mark unreleased versions as affected.
You don't have access to them yet.

### Comment 26: ZeNico13 (2019-05-13T08:31:45.943-0700)

Still in 1.14.1 Release

### Comment 27: migrated (2019-11-03T19:42:02.351-0800)

Present in 19w44a

### Comment 28: migrated (2020-11-11T09:47:41.948-0800)

Still seeing this in 1.16.3
Trying to use fill command to replace end_gateway blocks with different nbt results in No blocks filled message.

### Comment 29: Jack McKalling (2022-09-14T15:58:06.907-0700)

It seems like this issue doesn't necessarily have anything to do with inventories. What happens is that the target block just gets "cleared" of data, and simply not (re)populated with the specified NBT.
As if replacing a block with differing NBT is interpreted as invalid data for the block and just forced erased upon replace.

### Comment 30: MrBurdy (2023-05-28T02:40:52.774-0700)

I've had the same problem with lecterns, and no matter how much I replaced the block with air and then put in the new lecternwithnbt, the new lectern has the old NBTs. (although in the meantime I've put in a block of air to 'clear').
And 1.20 last pre realase.

### Comment 31: migrated (2024-10-26T05:10:07.337-0700)

Affects 1.21.3

### Comment 32: migrated (2024-10-30T10:18:26.973-0700)

Affects 24w44a

### Comment 33: tryashtar (2025-01-08T14:41:49.029-0800)

The first example is fixed in 25w02a, and the second example is now intended, per these changes in the changelog:
- If the block entity data is not specified, and the existing block has data, the block entity data will be preserved

- If the block entity data is specified, the block entity data will be set to the specified value

- To clear the block entity data explicitly, you must now specify the block entity data as {}

- The operation is now successful if either the block state changed or the block entity data changed
