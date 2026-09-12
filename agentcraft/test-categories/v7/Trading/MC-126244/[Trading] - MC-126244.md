# MC-126244: '/locate', explorer maps, and treasure maps can cause extreme TPS lag, even leading to a complete server freeze if structure generation is turned off

**Mojira URL:** [https://bugs.mojang.com/browse/MC-126244](https://bugs.mojang.com/browse/MC-126244)

## Report details

- **Mojira categories:** Commands; Performance; Structures; Trading
- **Project:** MC
- **Issue key:** MC-126244
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2018-02-23T13:04:00.497-0800
- **Updated:** 2025-04-29T08:53:11.383-0700
- **Resolution date:** 2024-06-09T07:05:41.377-0700
- **Affects versions:** Minecraft 18w08b; Minecraft 18w09a; Minecraft 18w10c; Minecraft 18w10d; Minecraft 18w11a; Minecraft 18w15a; Minecraft 18w16a; Minecraft 18w19b; Minecraft 18w20a; Minecraft 18w22a; Minecraft 18w22b; Minecraft 18w22c; Minecraft 1.13-pre1; Minecraft 1.13-pre2; Minecraft 1.13-pre3; Minecraft 1.13-pre4; Minecraft 1.13-pre5; Minecraft 1.13-pre6; Minecraft 1.13-pre7; Minecraft 1.13-pre8; Minecraft 1.13-pre9; Minecraft 1.13-pre10; Minecraft 1.13; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w43b; Minecraft 18w43c; Minecraft 18w44a; Minecraft 18w45a; Minecraft 18w47b; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 19w02a; Minecraft 19w03a; Minecraft 19w03b; Minecraft 19w03c; Minecraft 19w08b; Minecraft 19w09a; Minecraft 19w12b; Minecraft 19w13b; Minecraft 19w14a; Minecraft 19w14b; Minecraft 1.14 Pre-Release 2; Minecraft 1.14 Pre-Release 3; Minecraft 1.14 Pre-Release 4; Minecraft 1.14; Minecraft 1.14.2 Pre-Release 2; Minecraft 1.14.3 Pre-Release 2; Minecraft 1.14.3 Pre-Release 3; Minecraft 1.14.3; Minecraft 1.14.4 Pre-Release 3; Minecraft 1.14.4 Pre-Release 4; Minecraft 1.14.4 Pre-Release 5; Minecraft 1.14.4 Pre-Release 6; 1.14.4 Pre-Release 7; 1.14.4; 19w34a; 19w35a; 19w36a; 19w37a; 19w38b; 19w39a; 19w40a; 19w41a; 19w42a; 19w45b; 19w46b; 1.15 Pre-release 1; 1.15 Pre-Release 2; 1.15 Pre-release 3; 1.15 Pre-release 4; 1.15 Pre-release 5; 1.15 Pre-release 6; 1.15 Pre-release 7; 1.15; 1.15.1; 1.15.1 Pre-release 1; 1.15.2 Pre-Release 1; 1.15.2 Pre-release 2; 1.15.2; 20w06a; 20w07a; 20w08a; 20w09a; 20w10a; 20w11a; 20w13a; 20w13b; 20w15a
- **Fix versions:** Minecraft 1.13-pre6; 20w17a
- **Labels:** /locate
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 1.14.3_crash-2019-07-17_17.23.37-server.txt; 1.14.4_crash-2019-07-17_19.59.15-server.txt; crash-2018-07-06_11.44.47-client.txt
- **Issue links:** Duplicate:inward:MC-126375:/Locate Immediatley Drops Down My Fps | Duplicate:inward:MC-126711:When using /locate says 'Could not Find That Structure Near by" and game lags some much I searched for Igloo | Duplicate:inward:MC-128452:the game stop  calculate entities when I type /locate in the singleplayer chat | Duplicate:inward:MC-128913:[Crash] Overloaded Locate Command | Duplicate:inward:MC-130671:/locate Monument freezes game and prevents reloading | Duplicate:inward:MC-131176:Locate monument | Duplicate:inward:MC-131280:Game Crashes when /locate Village command is used | Duplicate:inward:MC-131550:Crash World | Duplicate:inward:MC-131671:Locate command crashes game when dungeon is not found | Duplicate:inward:MC-131828:Trying to locate distant structures is very resource intensive and may cause crashes | Duplicate:inward:MC-131941:/locate | Duplicate:inward:MC-132022:/locate uses all memory & crashes game | Duplicate:inward:MC-132066:locate command doesnt work | Duplicate:inward:MC-132403:You can't search the coordinates of a woodland residence | Duplicate:inward:MC-132935:Trading paper for emerald with a cartographer villager causes timeout on server, and all players get disconnected. | Duplicate:inward:MC-132946:Extreme  tick lag when using the /locate command | Duplicate:inward:MC-133027:The command "/locate" cause a serve crash. | Duplicate:inward:MC-133062:/locate Mansion not working | Duplicate:inward:MC-133068:Cartographer Trading Results in Unending FPS drop | Duplicate:inward:MC-133651:World tick lag after open chest in Shipwreck | Duplicate:inward:MC-133961:/locate makes FPS huge drop and crash | Duplicate:inward:MC-134781:generated chests in ships not displaying on first opening. | Duplicate:inward:MC-136464:Underwater chest make the game stop | Duplicate:inward:MC-136764:Empty maps bug in 1.13.1 | Duplicate:inward:MC-136849:Villager Trading very bugged | Duplicate:inward:MC-137249:Is imposible open some chest with a map in a ship | Duplicate:inward:MC-137827:/locate takes very long time to locate faraway things | Duplicate:inward:MC-138327:Game freeze on /locate Jungle_pyramid | Duplicate:inward:MC-138461:Tressure chest GUI on ship recks not displaying. | Duplicate:inward:MC-139056:Unlocking the explorer maps trade from Cartographers massively increases the ms per tick and essentially kills the world | Duplicate:inward:MC-139280:/locate creates extreme lag that affects mobs and world generator | Duplicate:inward:MC-139314:Open chest under water and server crashes | Duplicate:inward:MC-140431:MInecraft stop working after the third interaction with the cartographer | Duplicate:inward:MC-141680:"/locate mansion" crashes the game | Duplicate:inward:MC-142118:Cartographer trade freezes the game on 1.13.2 | Duplicate:inward:MC-142908:Using command "/locate " sometimes crashs the game | Duplicate:inward:MC-143094:Map item freezing | Duplicate:inward:MC-145782:Woodland explorer map takes for ever to generate and freezes game. | Duplicate:inward:MC-146488:Using /locate when the structure doesn't exist causes the game to enter a weird, glitch state | Duplicate:inward:MC-148089:locate command freezes the game | Duplicate:inward:MC-148301:Chests take a while to open | Duplicate:inward:MC-148577:Command /locate will "pause" the game | Duplicate:inward:MC-149062:Cartographer trade freezes the game on 1.13.2 | Duplicate:inward:MC-149743:Sunken Ship Chest Crash | Duplicate:inward:MC-149962:World can freeze while cartographer villager unlocks an explorer map | Duplicate:inward:MC-150893:All Mobs either freezing or dissapearing when /locate is used | Duplicate:inward:MC-151249:Leveling up Cartographer causes chunks to fail loading | Duplicate:inward:MC-151575:Using /locate softlocks the game, having to use task manager to close it | Duplicate:inward:MC-151722:/locate | Duplicate:inward:MC-151832:Game freezes when locating a village in superflat world. | Duplicate:inward:MC-152069:Crashing Servers | Duplicate:inward:MC-153132:/locate command freezes the game | Duplicate:inward:MC-153622:Using locate Village with structure generation off crashes servers | Duplicate:inward:MC-156128:some generated chests cause massive lag | Duplicate:inward:MC-156303:If you enter "/locate <Structure>" in the world where the "Generate Structures" is disabled, then the world is frozen | Duplicate:inward:MC-157024:1.14 Fatal Server Crash when using /locate command | Duplicate:inward:MC-158088:Opening Chests With Treasure Maps Inside Causes Extreme Slow Down on SSP & Crash on SMP | Duplicate:inward:MC-158804:bug on map errore code -1 | Duplicate:inward:MC-158829:/locate monument not working | Duplicate:inward:MC-158860:Levelling up villagers freezes the game | Duplicate:inward:MC-158865:Cartographer crashes server in 1.14.4 | Duplicate:inward:MC-159181:The game doesn't work(about game code) | Duplicate:inward:MC-159339:Chests in Shipwrecks won't open properly | Duplicate:inward:MC-160141:Minecraft Realm /locate bug | Duplicate:inward:MC-160694:Cartographer trades crash world when structures are off | Duplicate:inward:MC-162032:Cartography Villagers glitching on worlds with no structures | Duplicate:inward:MC-162178:Locate Command on a World with Generated Structures Off Causes Crash | Duplicate:inward:MC-162985:Bug in singleplayer with cartographer | Duplicate:inward:MC-162989:Map Villager Crash with no Structures | Duplicate:inward:MC-163429:/locate lags game | Duplicate:inward:MC-164938:Locate causes lag | Duplicate:inward:MC-164960:Trading with Cartographer Villager | Duplicate:inward:MC-166230:Game freezes using locate command | Duplicate:inward:MC-166564:Extreme Lag when opening Shipwreck Treasure Map Chest on Realms | Duplicate:inward:MC-167302:Server crashs when opening a map chest in shipwreck | Duplicate:inward:MC-169572:Cartographers time out server when searching for structures | Duplicate:inward:MC-170159:/locate can lock up the game if no features are generated. | Duplicate:inward:MC-170199:/locate freezes the world or times out servers when structure generation is disabled | Duplicate:inward:MC-173116:[DUPLICATE] World time freeze | Duplicate:inward:MC-173409:"/locate" bug | Duplicate:inward:MC-173592:Issue with Cartographer Villager | Duplicate:inward:MC-174681:Redstone and AI do not work after using the "locate" command. | Duplicate:inward:MC-176463:World stops responding after typing /locate EndCity | Duplicate:inward:MC-177355:Using /locate jungle_pyramid in jungle superflat freezes world | Duplicate:inward:MC-177520:cartographer crashes server when leveling up past apprentice | Duplicate:inward:MC-179636:/locate in a world without generated structures seemingly softlocks the game | Duplicate:inward:MC-179692:Trading with cartographer will crash the vanilla 1.15.2 server | Duplicate:inward:MC-180991:/locate in a no structures world is like a crash | Duplicate:inward:MC-184343:When with villagers game crashes . Tried no sound lower setting still it locks up and does not resolve its self. | Duplicate:inward:MC-184553:uncontrolled chunk loading by /locate in world with structures disabled | Duplicate:inward:MC-185477:Locate command broken | Duplicate:inward:MC-190745:/locate crashes world | Relates:outward:MC-171049:locatebiome tries to find biomes that do not exist in current dimension or that do not generate at all | Relates:inward:MC-177035:exploration_map with EndCity as destination takes incredibly long time | Relates:inward:MC-139841:Using /locate to find pillager outposts in a superflat world freezes the game | Cloners:inward:MC-269520:The game freezes when using /locate in a world without structures enabled

## Description

The bug
The server will cause lag when we try to locate any of the structures away. With structure generation turned off, this can completely freeze the server.
Note that /locatebiome (introduced in 20w06a) has a timeout.

## Comments (67)

### Comment 1: migrated (2018-02-23T13:04:00.497-0800)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: migrated (2018-02-25T03:57:37.699-0800)

I'm pretty sure that is normal. How can the game know where the structures are placed without checking the seed?

### Comment 3: black-hole (2018-02-25T04:04:46.877-0800)

@Dungeneer In earlier versions, like 1.12.2 the structures are located based on the seed without loading/creating chunks.

### Comment 4: migrated (2018-03-03T05:05:48.713-0800)

I believe this issue may be linked to the bug in which structures that are too far away fail to be located, which didn't happen in 1.12.2. Not sure if I should make a new report for that issue (haven't found a match through searching), or if I should forego that for now as a fix to the current issue may also fix that issue as well.

### Comment 5: CreeperMagnet_ (2018-03-06T15:14:24.505-0800)

As  said, this is caused by structures not being able to be located.
This also affects explorer maps, and is still present in 18w10a.
Someone might want to update the description and title, or create an entirely new issue.

### Comment 6: migrated (2018-03-09T13:02:42.956-0800)

I tested this in the 18w10d Vanilla server and a few locates is will lag the server for 7-8 seconds.

### Comment 7: migrated (2018-03-18T09:22:26.672-0700)

Still present in 18w11a, /locate to a Mansion returns 'Could not find that structure nearby' and badly lags the client for several seconds.  It's also consistent with EndCity and consistent through a dozen single player survival worlds I've created and tested on.

### Comment 8: migrated (2018-04-11T09:41:19.707-0700)

Confirmed in 18w15a, still gives lag and error message for structures that are too far away.

### Comment 9: migrated (2018-05-09T10:10:00.288-0700)

Still not working 18w19b.
In general Locate is not working. Tested for buried treasure and others. It shows a location for those, but getting there (where is says you are 1 block away) there is nothing there. Both times it was at Y=0 where the N blocks away dropped to 0.

### Comment 10: migrated (2018-05-15T10:07:33.613-0700)

The following may, or may not, be useful.
1) Create world in latest build (18w20a)
2) Use locate mansion. Returns not found.
3) Copy seed, create same world in released version of MC.
4) Locate mansion. Works.
5) Re-open original world in 18w20a.
6) TP to mansion location. Mansion is there. (Verifying mansions are getting created, just that locate is not working as expected)
7) Locate mansion while standing next to it. Works. (Verifying that locate works some of the time. Distance SEEMS to be the issue (but read on!).
8) Press F3. Fly away. Very quickly the amount of memory used is 100%. (Note computer has 32GB and 64 bit Java is in use, but only 4 is allocated). However, at over 1000 blocks, the locate STILL SEEMS TO WORK (but read on!).
9) Due to 100% mem use, save quit. Allocate 8 GB of mem to "latest release" profile, Restart.
10) Do locate, from where it worked before. NOT FOUND. Indicating that locate failing IS NOT simply distance dependent. It is a sticky bit of some sort.
11) Fly back toward mansion. MANSION IS IN SIGHT, but about 100 or less away. Try locate. Locate fails.

Perhaps this will lend further insights. Cheers.

### Comment 11: migrated (2018-05-18T17:11:46.135-0700)

This lags my game more than a few seconds.. I have a large biomes world, and testing the locate command lags to the point of the game freezing- I am simply forced to force quit the game.

### Comment 12: McModknower (2018-06-15T10:52:24.167-0700)

Is this related to https://bugs.mojang.com/projects/MC/issues/MC-130449 ?

### Comment 13: migrated (2018-06-15T13:34:43.776-0700)

@ I guess no, this issue it's about the /locate command.

### Comment 14: Leon_Xu (2018-06-15T20:22:34.855-0700)

Still not work normally in 1.13 pre-2.
"/locate" can only locate the structure(s) in loaded chunck(s).

### Comment 15: migrated (2018-06-21T06:35:25.558-0700)

Guys, locate command works properly... Lag is caused because the command is generating all chunks and checking if there is any structure you are searching for... And if message Could not find that structure nearby shows up, then the structure is NOT NEARBY..

### Comment 16: [Mod] violine1101 (2018-06-21T06:37:41.123-0700)

It shouldn't halt the entire game for 10 seconds though. Besides, /locate didn't generate chunks in order to locate something in 1.12.2.

### Comment 17: migrated (2018-06-21T20:43:45.457-0700)

1.13 pre3 new random world, not a lot generated around spawn.
Locate works fine if structure is roundabout <500 Blocks away.
Gives little Lag if <800 Blocks, randomly crashes
Mostly crashes game after huge lag if >1000
Since now... ALWAYS crashes if not even nearby.
Open to Lan makes it a lot worth although nobody else joined game.
No Crash Report added

### Comment 18: migrated (2018-06-26T06:56:02.760-0700)

My results in 1.13-pre4;
1) "Could not find that structure nearby" is not fixed.
2) Vanilla lag is not fixed.
3) FPS drop I think is fixed.

### Comment 19: CivetKitty (2018-06-26T07:59:28.880-0700)

It hasn't been fixed at all. I tested the command using the seed -4654979345475103749 at spawn, and tried to locate a mansion. Of course, it failed. I also tried unlocking an explorer map, but after doing the empty map trade with a cartographer, the game froze for a moment and the trade wasn't generated.

### Comment 20: qwerty23495 (2018-06-26T08:06:53.620-0700)

Please reopen

### Comment 21: Jacie_krece (2018-06-26T08:15:47.011-0700)

@MrWener /locate Village generates error "Cloud not find that structure nearby" even if on the village well. Simply this command isn't working.

### Comment 22: migrated (2018-06-26T08:26:00.625-0700)

/locate is continuing to crash my vanilla pre-release 4 server, so this issue doesn't seem to be resolved as of yet.

### Comment 23: migrated (2018-06-29T13:18:48.042-0700)

/locate still a bug for Mansion and Desert Temple as of 1.13 pre 5 - It will lag tremendously without giving coordinates then eventually crash.

### Comment 24: CreeperMagnet_ (2018-06-29T13:21:32.849-0700)

, that doesn't matter anymore. This bug has already been marked as resolved for the NEXT version. It doesn't matter if it affects the current version, what matters is if it will affect the next version. Adding another affected version won't change anything about this bug. They obviously have enough information, and have already fixed it. (Hopefully.)

### Comment 25: migrated (2018-06-29T22:41:54.294-0700)

I also discovered this loophole, which was discovered in May.

### Comment 26: migrated (2018-07-04T07:10:55.818-0700)

Unfortunately, it is not fixed yet.

### Comment 27: migrated (2018-07-04T07:34:23.700-0700)

I can also confirm that /locate Mansion timed out on 1.13-pre6 as well.

### Comment 28: migrated (2018-07-05T01:04:46.821-0700)

For people who time out and crash, can you post your crashlog ?

### Comment 29: migrated (2018-07-06T09:56:52.413-0700)

It doesn't seem to cause severe lag on my end anymore, but the structure still can't be located. It doesn't time out or crash, but will a forced crash be of any use here?

### Comment 30: migrated (2018-07-10T13:33:54.504-0700)

Hello, ! Today I tryed the /locate command with pre7 and finally we have the better experience!
The /locate command is run better on 1.13-pre7, but the Vanilla lag (when typing /locate <locate> command the Vanilla server will lag) is not fixed yet.

Here's my results on 1.13-pre7:
- FPS drop is fixed.

- "Could not find that structure nearby" error message is fixed.

- Vanilla lag is not fixed.

### Comment 31: FaRo1 (2018-07-10T14:19:38.377-0700)

"Vanilla" means unmodified. You mean server lag.

### Comment 32: migrated (2018-07-11T05:10:39.996-0700)

@ Yes.

### Comment 33: qwerty23495 (2018-07-11T05:17:39.125-0700)

Server lag won't be fixed until the /locate command stops generating chunks to look for structures.

### Comment 34: migrated (2018-07-16T08:24:17.494-0700)

1.13pre9 still has this problem

### Comment 35: Makzevu (2018-07-18T11:51:32.960-0700)

Is this still in 1.13?

### Comment 36: migrated (2018-07-19T13:10:26.417-0700)

I noticed in pre10 that new worlds were ok, /locate had no lag and returned accurate coords as in structures were actually there.  Old worlds, those I created in earlier 1.13 snapshots, had no lag anymore but /locate returned coords where structures were not there.  1.13 also seems ok thus far in my limited testing with a new world.

### Comment 37: FaRo1 (2018-07-19T23:31:20.005-0700)

Are the structures also missing in 1.12.2 worlds? Upgrading between snapshots is not always supported.

### Comment 38: migrated (2018-07-20T06:38:02.852-0700)

No, 1.12.2 was fine.  I didn't try to bring a 1.12.2 generated world into 1.13 snapshots or even 1.13.  I was merely trying to point out that the issue, at least for me, looks to be resolved.  Thanks!

### Comment 39: FaRo1 (2018-07-20T06:42:28.825-0700)

I was asking whether /locate in 1.13 finds structures in 1.12 worlds, either generated in 1.12, generated in 1.13 or not yet generated. Those are three test cases that should be checked before this gets closed.

### Comment 40: qwerty23495 (2018-07-20T06:46:54.268-0700)

I can confirm that 1.13 locate can find 1.12 generated structures. I tested with '/locate Mansion' in Etho's LP world, and I was directed to a Mansion that had already spawned and had been looted.

### Comment 41: migrated (2018-08-06T07:53:49.821-0700)

There's still lag when opening a shipwreck map chest (just the map chest).  I added some more info re: this to a bug report already marked as duplicate as above: https://bugs.mojang.com/browse/MC-133651
Is it always to be expected to have lag on a server for it to generate the treasure maps upon opening the chest?  (and also in a singleplayer world?)

### Comment 42: migrated (2018-10-24T23:00:59.207-0700)

can reproduce in 18w43a and 18w43b.

### Comment 43: migrated (2018-10-26T03:36:37.286-0700)

Can confirm for 1.13.2 and 18w43a/b/c.

### Comment 44: migrated (2019-03-05T00:19:46.423-0800)

19w09a results:
There are no longer FPS drop or "Could not find that structure nearby" error. But when try to locate some structure the vanilla server will cause lag.

### Comment 45: migrated (2019-04-05T06:20:05.873-0700)

The only problem is the TPS lag. I can't get any FPS drop errors now.

### Comment 46: migrated (2019-05-18T03:28:44.256-0700)

Confirmed for 1.14.2 Pre-Release 2

### Comment 47: Makzevu (2019-06-01T07:46:42.266-0700)

Discussion for all reports on Mojira related to Performance Errors.

### Comment 48: migrated (2019-07-17T19:53:54.211-0700)

Perhaps related to MC-157024 fatal server crash when using /locate command.

### Comment 49: migrated (2019-07-18T08:38:03.586-0700)

Affects 1.14.4 Pre-Realease 7
My servers are crashing because of this
Server console output when using /locate Village:
[10:31:07] [Server Watchdog/FATAL]: A single server tick took 60.00 seconds (should be max 0.05)
[10:31:07] [Server Watchdog/FATAL]: Considering it to be crashed, server will forcibly shutdown.
EDIT: This is happening when the world is generated with generate-structures=false.

### Comment 50: migrated (2019-07-20T00:11:10.000-0700)

Affects 1.14.4 - and still will stop any single player or server in it's tracks if the world was generated with generate-structures=false.  To recreate in single player : while in "Create New World" click on "More World Options", then click on Generate Structures to turn it off.  Create the new world and execute the command /locate Village.  Then wait while it comes to a complete halt.

### Comment 51: migrated (2019-08-09T14:52:34.149-0700)

The Minecraft server client times out even with generate structures set to true on 1.14.4. See MC-158088 for more details.

### Comment 52: migrated (2020-02-02T18:55:40.640-0800)

Still seeing this 1.15.2. Very reproducible on opening chest in sunken ship. Have upped the max-tick-allowed to 480000 and still crashes.

### Comment 53: dscheJ-Ouh (2020-02-18T20:22:55.944-0800)

On slower/weaker systems, the game first freezes, then crashes with a Java Heap Exception on opening the treasure map chest in sunken ships. (1.15.2)

### Comment 54: migrated (2020-03-24T03:04:21.504-0700)

Im having the same problem, me and my friends are having troubles with the cartographer.  The server just freezes after the villager reaches Journeyman. Also our world was generated with generate structure to on

### Comment 55: migrated (2020-06-09T13:54:39.174-0700)

Still a problem in 1.15.2, especially when the cartographer villager ranks up Ocean Explorer map trade.

### Comment 56: migrated (2020-06-19T13:08:22.081-0700)

Setting "max-tick 600000" causes a timeout disconnect for the clients, but the game continues after a pause. So clients can reconnect and the game is not crashed.
The default "max-tick 60000" crashes the sever and the game is sent back some minutes due to not saved data.

### Comment 57: migrated (2021-03-20T16:38:08.612-0700)

This doesn't seem to be fixed. I'm getting this problem on a 100% vanilla server on 1.16.5. When the cartographer levels up, the server freezes for everyone. Is there any way this can be marked as not resolved?

### Comment 58: migrated (2021-06-05T09:28:59.645-0700)

Having this problem on a 1.16.3 server running on an AWS t3a.medium instance. Johannes' workaround works for me.

### Comment 59: migrated (2021-06-20T05:42:50.779-0700)

We discovered, that you can prevent server crash (in Shipwrecks) when setting (but in this thime the chest will not have a trasure map)

```max-tick-time=-1```

### Comment 60: migrated (2021-06-20T06:03:10.879-0700)

I discoved what causes this problem:

It only happens, when you try to get a trasure map in an area where most chunks arround you are already generated in a older version.
Seems that the game tries to find an burried trasure for the map, but it can find a burried trassure, because there are not enough unloaded chunks arround.

Mojang should yust check "if there is not area close, where a burried trassure could be place --> Skip generatting of trasure map" this would fix the problem

### Comment 61: ZeNico13 (2021-06-20T07:23:19.881-0700)

@ I think if you still have this problem, you should create a new ticket and post it here in a comment. If you can attach a demonstration video, that would be great!

### Comment 62: migrated (2021-07-09T16:39:36.157-0700)

Still getting this in 1.17 and 1.17.1. Game freezes for upwards of 10 minutes when leveling up a cartographer.

### Comment 63: migrated (2021-07-29T13:35:34.585-0700)

I have found that this is a problem in 1.17.1, but it happens for me even when structures are in the world. Attempting to close the game by saving and quitting cause it to save the world for an extended period of time, and pressing alt+f4 causes the screen to go black without it actually closing
edit: And it only seems to happen when locating mansions

### Comment 64: ZeNico13 (2021-08-12T11:25:03.228-0700)

@ I think you should create a new ticket for this, and mention this new ticket here in a comment. If you can attach a demonstration video that would be great!

### Comment 65: tqz78 (2021-08-12T11:30:10.111-0700)

Different problem; it only happens with OptiFine when trading with a cartographer, not by using a /locate command. See MC-228721.

### Comment 66: migrated (2021-10-12T10:28:38.703-0700)

New ticket MC-238830 , but just for the server lag caused by opening a buried treasure map in a chest in a stronghold or /locate buried_treasure somehow having to take an unreasonably long time to locate the nearest buried treasure, not the mansion issue that just seems to be an optifine bug.

The odd thing is this seems to have been fixed in the 1.16 snapshots but by 1.16.5 it's still just as big of a bug... then by 1.17 and 1.17.1 it seems to be fully fixed again. Then starting at 21w37a it has resurfaced yet again, which indicates that it isn't a really high priority issue that is easily broken from update to update.

Edit: This turns out to already have been reported as MC-238830 but not listed in the comments here. Probably will just be merged with that one.

### Comment 67: migrated (2022-07-12T07:45:27.499-0700)

For me i can confirm this happens in 1.19 in which it soft locks my game not letting me leave. Even after restarting the launcher and doing End Task in task manager because I couldn't close it. I still would not be able to do anything normally like i would fly through the floor and I also got straight up put on a Lead by a llama. It only worked normally on the 3rd reboot. Even though its a world with multiple biomes when I do /locate biome [?] it will do the same thing. I have a video that shows the bugs but it is "Too big of a file size". I might crop the video except I have no idea how to do that. I don't know if I should open this for a new ticket? But location maps also crash your game pretty much infinitely cuz when you restart the game your still holding it. I might add another comment later with more detail after I look into this more!
