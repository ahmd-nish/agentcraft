# MC-86846: Changing a powered Command block from impulse/chain mode to repeat mode doesn't trigger it until repowering

**Mojira URL:** [https://bugs.mojang.com/browse/MC-86846](https://bugs.mojang.com/browse/MC-86846)

## Report details

- **Mojira categories:** Block states; Commands; Redstone
- **Project:** MC
- **Issue key:** MC-86846
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2015-08-20T14:30:54.998-0700
- **Updated:** 2025-04-29T21:13:24.428-0700
- **Resolution date:** 2021-11-19T07:56:09.058-0800
- **Affects versions:** Minecraft 15w34b; Minecraft 15w44b; Minecraft 15w50a; Minecraft 15w51b; Minecraft 16w05b; Minecraft 1.9; Minecraft 1.9.1 Pre-Release 1; Minecraft 1.9.1 Pre-Release 2; Minecraft 1.9.1 Pre-Release 3; Minecraft 1.10.2; Minecraft 16w43a; Minecraft 1.11; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 1.12.2; Minecraft 18w03b; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 19w04b; Minecraft 1.14 Pre-Release 2; Minecraft 1.14 Pre-Release 3; Minecraft 1.14 Pre-Release 4; Minecraft 1.14 Pre-Release 5; Minecraft 1.14.1; Minecraft 1.14.2 Pre-Release 1; Minecraft 1.14.2 Pre-Release 2; Minecraft 1.14.2; Minecraft 1.14.3; Minecraft 1.14.4 Pre-Release 1; Minecraft 1.14.4 Pre-Release 3; Minecraft 1.14.4 Pre-Release 4; Minecraft 1.14.4 Pre-Release 5; Minecraft 1.14.4 Pre-Release 6; 1.14.4; 19w34a; 19w35a; 19w36a; 19w37a; 19w38b; 19w39a; 19w40a
- **Fix versions:** 19w41a
- **Labels:** chain-mode; impulse-mode; powered-command-block; repeat-mode; trigger
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** repeatingCommandBlock.webm
- **Issue links:** Duplicate:inward:MC-156789:Repeating Command Blocks Won't work 1.14.1+ | Duplicate:inward:MC-87257:"Always active" Command Blocks not running after switched to "Repeat"-mode | Duplicate:inward:MC-91133:Active command blocks turned into repeating command blocks don't automatically start executing | Duplicate:inward:MC-92636:Repeat type Command Blocks suddenly stop working | Duplicate:inward:MC-94459:Command block "Always Active" | Duplicate:inward:MC-94667:Repeat Command Blocks don't activate when switching from other modes to Repeat when on No Redstone mode | Duplicate:inward:MC-94952:Conditional statements don't carry correctly | Duplicate:inward:MC-96494:You can't give Levitation effect via Commandblocks. | Duplicate:inward:MC-96770:Command Blocks | Duplicate:inward:MC-96799:Command Blocks wont do /setblock | Duplicate:inward:MC-109479:Repeating command block not repeating | Duplicate:inward:MC-114776:Command blocks do not work properly after switching from Chain | Duplicate:inward:MC-143287:Command blocks on always activate do not activate after changing mode to repeat | Duplicate:inward:MC-150230:Repeating command blocks do not repeat. | Duplicate:inward:MC-155264:Repeating command blocks are not working | Duplicate:inward:MC-208887:/give repeating_command_block is glitched. | Relates:outward:MC-95873:Command Blocks Sometimes Don't Work After being placed from Ctrl+Middle Click | Relates:inward:MC-149038:Command blocks on repeating with always active or need redstone stop working

## Description

I don't know whether or not this is intended to be this way, but i'll report it anyways just to be sure.
When you place an impulse command block and put a command in it and then activate it, it works. But if you keep it powered and you change it from impulse to repeat, it wont trigger. It will trigger once it is turned off and turned on again.
Additional description from :
To clarify the description a bit, this occurs both if the block is set to "Needs Redstone" and is receiving power, and also if it's set to "Always Active". It's also worth noting that this is not fixed by updating the block, the setting must actually be changed back to Needs Redstone, then back to Always Active.
This bug also occurs with impulse mode. Set it to Chain and Always Active and type in a command. Then change it to impulse. The command will not be run until it is changed to and from Needs Redstone.

## Comments (19)

### Comment 1: migrated (2015-08-20T14:30:54.998-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: migrated (2015-12-11T14:09:02.729-0800)

Ok I think I know what's happening:
When changing command block options (well, for now on: impulse to repeat mode), they don't consider their new options until they are redstone updated.
Also, if you do this and the command block is set to "Always active", you need to put it to "needs redstone", press done and set it back again to "Always active" to consider his new state.

### Comment 3: migrated (2016-02-02T08:14:47.525-0800)

also occures with chain -> repeat, not only impulse -> repeat

### Comment 4: migrated (2016-03-10T16:07:38.099-0800)

Effects all 1.9 pres, 1.9 snapshots, 1.9.1 pre 1, and 1.9.1 pre 2.

### Comment 5: migrated (2016-03-13T09:38:50.933-0700)

The enviroment is supposed to contain pc details.

### Comment 6: migrated (2016-03-13T09:57:00.347-0700)

Confirmed for 1.9.1 pre release 3

### Comment 7: migrated (2016-03-14T20:05:45.891-0700)

To clarify the description a bit, this occurs both if the block is set to "Needs Redstone" and is receiving power, and also if it's set to "Always Active". It's also worth noting that this is not fixed by updating the block, the setting must actually be changed back to Needs Redstone, then back to Always Active.
This bug also occurs with impulse mode. Set it to Chain and Always Active and type in a command. Then change it to impulse. The command will not be run until it is changed to and from Needs Redstone.

### Comment 8: migrated (2016-07-15T12:04:55.609-0700)

This bug is also in 1.10.2
Video: https://www.mediafire.com/?62mb0zbpb6r0o6b

### Comment 9: TheTamedWolf (2016-11-22T14:22:07.980-0800)

I can confirm this is happening in 1.11.
I would set a command block down, type in a command like: say @p Hello :and put it to repeat and always active. Then I would let it run for 2 seconds and then I would go in and change it to impulse and I expected it to run the command immediately after that, at least once, but got nothing. Went back in and changed it to needs redstone then powered it. And it works.  Also I went away like a few blocks and went back to try another command block i had sitting around (it was working perfectly before) and it stopped working. Haven't a clue why. The command for that one was: testfor @p[x=1050,y=56,z=-449,r=1,score_Adult=1] :And like I said it was working perfectly before, and changing the command block nor changing it's settings works. It seems the testfor command is a little finicky too but idk.

### Comment 10: migrated (2018-01-28T14:15:57.170-0800)

confirmed for 18w03b.

### Comment 11: migrated (2019-01-28T13:17:48.781-0800)

Still affects 19w04b.

### Comment 12: migrated (2019-04-19T01:44:04.677-0700)

I have the same problem when using a chain command block and switching it to "Repeat" via the UI.

It works after setting to "Needs Redstone" and back to "Always Active"

Version: Minecraft 1.14 Pre-Release 5

### Comment 13: ZeNico13 (2019-05-13T10:25:33.852-0700)

Still in 1.14.1 Release

### Comment 14: ZeNico13 (2019-05-17T12:19:49.758-0700)

Still in 1.14.2 Pre-Release 1 and 1.14.2 Pre-Release 2

### Comment 15: migrated (2019-06-26T06:39:49.362-0700)

Still in 1.14.3

### Comment 16: migrated (2019-08-29T10:10:56.260-0700)

Here's an extract of , it's a duplicate post, but it has a lot of information about the problem:

Here is a list of commands in repeating command blocks that does not work:
(Boosts) If you are in a certain team and crouch and that your boost score is 0, you get an effect:
Command#.1 (Repeat): /effect give @a[team=Speedster,scores={Crouch=1..,Boost=0}] minecraft:speed 8 13 true
Command#.2 (Chained): /scoreboard players set @a[team=Speedster,scores={Crouch=1..,Boost=0}] Crouch 0

Commands that says when the boosts are on or off (the "Boost" scoreboard is affected by eating rotten flesh): (these 4 commands run in a loop)
Command #.1 (Repeat) /tellraw @a[scores={Boost=3}] {"text":"Boosts ON!","color":"dark_green"}
Command#.2 (Chained): /scoreboard players set @a[scores={Boost=3}] Boost 0

Command #.1 (Repeat): tellraw @a[scores={Boost=1}] {"text":"Boosts OFF!","color":"dark_red"}
Command #.2 (Chained): scoreboard players set @a[scores={Boost=1}] Boost 2

Here is a list of commands in repeating command blocks that does work:
If you walk on light blue concrete, you get a speed boost:
(Repeat): /execute at @a if block ~ ~-1 ~ minecraft:light_blue_concrete run effect give @p[distance=..3] minecraft:speed 1 15

Mobs have special effects:
(Repeat): /execute at @e[type=creeper] run effect give @e[distance=0..1,type=creeper] minecraft:blindness 10 0 true

From what I could see right now, the only commands on repeat that does not seem to work are the one that needs a specific criteria/another scoreboard objective to be activated (for exemple, having {boost=0} or {crouch=1..}).

Also, the bug is still happening in Snapshot 19w35a

### Comment 17: migrated (2019-10-04T00:29:51.082-0700)

Have you tried placing a block next to it after changing it to repeat? This issue may be related to quasi connectivity and working as intended.

### Comment 18: migrated (2019-10-06T12:30:55.531-0700)

@o62 I tried placing a block next to it after changing it to repeat, but it still didn't work.

### Comment 19: migrated (2021-11-19T07:56:09.058-0800)

This is happening again in 1.17.1
