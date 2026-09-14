# MC-697: Default singleplayer player data is always used for players opening world

**Mojira URL:** [https://bugs.mojang.com/browse/MC-697](https://bugs.mojang.com/browse/MC-697)

## Report details

- **Mojira categories:** Player
- **Project:** MC
- **Issue key:** MC-697
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2012-10-25T23:26:16.898-0700
- **Updated:** 2026-04-04T07:37:29.631-0700
- **Resolution date:** 2026-04-04T07:37:05.164-0700
- **Affects versions:** Minecraft 1.4.2; Minecraft 1.4.6; Minecraft 1.7.4; Minecraft 14w05b; Minecraft 14w06b; Minecraft 14w07a; Minecraft 14w08a; Minecraft 1.7.10; Minecraft 14w32d; Minecraft 1.8.1-pre3; Minecraft 1.9.4; Minecraft 1.10; Minecraft 1.10.1; Minecraft 1.10.2; Minecraft 1.11.2; Minecraft 1.12.1; Minecraft 1.12.2; Minecraft 1.13-pre6; Minecraft 18w30b; Minecraft 1.13.2; Minecraft 1.14 Pre-Release 2; Minecraft 1.14 Pre-Release 3; Minecraft 1.14 Pre-Release 4; Minecraft 1.14 Pre-Release 5; 1.14.4; 1.15.2; 20w13b; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w27a; 20w28a; 1.16.2; 1.16.4; 1.16.5; 21w06a; 21w07a; 21w08b; 21w11a; 21w14a; 1.17 Release Candidate 2; 1.17; 1.19.3; 23w03a; 23w04a; 23w05a; 23w06a; 1.20.4
- **Fix versions:** 26.1 Snapshot 6
- **Area:** Platform
- **Labels:** duplication; playerdata
- **Votes:** 1
- **Watchers:** 4
- **Attachments:** 0
- **Issue links:** Duplicate:inward:MC-231106:Lost inventory when using new pc | Duplicate:inward:MC-222811:Found dupe bug | Duplicate:inward:MC-210908:Duplication Glitch with LAN worlds. | Duplicate:inward:MC-176509:In single-player worlds, statistics and advancements are unique to each Mojang account, while inventory is shared. | Duplicate:inward:MC-199552:Player data merged with launcher user switch | Duplicate:inward:MC-193732:Inventorys duplicated by switching accounts (singleplayer) | Duplicate:inward:MC-175955:LAN Inventories Inconsistant | Duplicate:inward:MC-175421:Singleplayer with multiple accounts dupe | Duplicate:inward:MC-167227:When ever a account is switch it keeps the same inventory in that world, it essentially duplicates everything a player has. | Duplicate:inward:MC-157967:Local Area Network Server Progress Deleted | Duplicate:inward:MC-145307:Old player's inventory is loaded on LAN game | Duplicate:inward:MC-133046:Player 2 logs into a single player world and receives the inventory from player 1. | Duplicate:inward:MC-124097:2nd Player Advancements overwritten by 1st Player advancements | Duplicate:inward:MC-122674:Inventory Switch | Duplicate:inward:MC-13576:Different accounts accessed via the same PC share inventories | Relates:inward:MC-2368:Accidental joining of game causes world to not save for the session | Duplicate:inward:MC-67379:Item Cloning Glitch in LAN Survival | Duplicate:inward:MC-112043:Incorrect Character Data on LAN Server | Duplicate:inward:MC-80246:Duplicating items in Singleplayer using Open to LAN feature | Relates:inward:MC-5405:Duplication of Items/xp in game | Duplicate:inward:MC-17785:Server login inventory copy | Relates:inward:MC-5222:Join server with correct skin and username, but wrong inventory, experience level, and position | Duplicate:inward:MC-4600:Lan world progress save failure | Duplicate:inward:MC-44064:"Open To Lan" game will overwrite player data | Duplicate:inward:MC-52929:Player 2 given Player 1's inventory, location, XP | Blocks:inward:MC-124027:Default singleplayer player data is not written or read to level.dat anymore | Duplicate:inward:REALMS-2173:Spawning with wrong inventory

## Description

The bug
For singleplayer worlds the player data is written to the level.dat file as well (called "default player data" in the following) and always used when someone opens the world. This creates the following two unwanted situations.
Cannot start with empty inventory in a world of someone else
Because the default player data is always used you cannot play in the world of someone else with new player data but instead start where the player who last played left and have the same items.
Default player data is used even if player data exists after playing in LAN
When you played in LAN before and an entry in the playerdata folder exists for a player the default player data is used anyways.
Imagine the following: Player 1 hosted the world and player 2 joined. After that player 2 opens the world, even though a player data entry exists he gets player 1's player data (=default player data) which even overwrites player 2's player data entry when he leaves the world.
Outdated default player data is used after loading world on a dedicated server
When a singleplayer world is loaded by a dedicated server and the default player data player joins, their playerdata entry is updated, but their default player data is not. Therefore when they load the world in singleplayer again, they have the old outdated player data.
Possible solution
See this reddit post for a discussion.
Have the game perform these steps when loading a world:
- If the default player data exists and for the same UUID a playerdata entry exists, overwrite the default player data with that. This is needed for the case where a singleplayer world was loaded by a dedicated server and therefore the default player data became outdated.
Then continue with the following steps:

- If the default player data exists, but the UUID does not match the UUID of the current player:
Possibly offer a checkbox to determine whether the default player data should be overwritten by the current player.
Provide these options:
- Offer to continue where that player last left

- Offer to use own player data (in case playerdata entry exists) or otherwise with empty inventory at world spawn

- Otherwise: If the default player data exists and the UUID matches the UUID of the current player, use that data

- Otherwise: If no default player data exists use the matching playerdata entry or, in case that does not exist, start with an empty inventory at world spawn

Workaround
Keep in mind that this is a bug tracker and not a discussion forum or a help desk. For questions, ask for example on reddit, the Minecraft Forum, or on other platforms.
 Create a backup of your world before trying the following workaround. Otherwise you might loose data or your world can become corrupted.
The following steps require an NBT editor. Make sure it is up to date and supports changes to NBT structure introduced in the latest versions. You can use for example NBTExplorer version 2.8.0(+).
- Open the level.dat file of the world with an NBT editor

- Delete the Data > Player entry

- Save the file

## Comments (46)

### Comment 1: Ezekiel (2012-10-26T06:34:21.052-0700)

This is somewhat serious, however I can not confirm because I don't have access to a copy of Minecraft at the moment. It makes sense, however.

### Comment 2: migrated (2012-11-19T01:47:26.110-0800)

Confirmed,only in LAN not multiplayer, they should make separate inventories for lan worlds and separate EnderChests.

### Comment 3: migrated (2013-02-15T11:49:13.303-0800)

I've seen this once, but that was because the minecraft servers were down and player two was called 'player' that's why he will get the same NBT data from the level.dat instead of it's own player.dat

### Comment 4: migrated (2013-03-28T08:15:57.013-0700)

Is this still a concern in the current Minecraft version? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 5: migrated (2013-07-02T12:10:06.229-0700)

Yes, this is still a concern with LAN play.
(edit:  And it concerns all facets of a character to include inventory and enderchests, despite the title)
When a player with a different username logs into Minecraft from my computer and pulls up the world we play together:  her inventory, location, enderchest, etc. are all replaced with the original 'main character' values, which then overwrite her .dat file.
I thought that was strange, because she already had a .dat file, but the game rewrote her to be me.
(We lost a ton of enchanted armor she had just made, and duped several silk touch items I had this way.  To top it all off, because I was mapping, she ended up displaced about 5km.)
edit:  This was around 13w25a  (Sorry to not have exact; it was after zombie AI changes and before 1.6 pre-release, but I haven't seen anything regarding SSP/LAN save structure in patch notes, so I bet it's still in live).

### Comment 6: migrated (2013-07-03T00:59:33.591-0700)

so... the player that logged in wasn't just called 'player' ?

### Comment 7: migrated (2013-07-03T12:51:39.126-0700)

@Jesper Unlike your issue, the Minecraft servers were fine.  The thing that caused this was player 2 logging on to player 1's machine and loading this world, which copied player 1's .dat file (possibly from the level.dat instead of "player1".dat or "player2".dat as you mentioned) and replaced player 2's permanently.  Until opened to LAN, there is no one to see what another player is called, so I don't have the answer to your question.

### Comment 8: migrated (2013-07-04T01:54:15.654-0700)

hmm... if the player that logged in was called 'player' then it would make a bit sense, then you would use all the properties from the level.dat but in your case it's just weird

### Comment 9: CubeTheThird (2013-09-25T19:17:35.389-0700)

Is this still a concern in the current Minecraft version 1.6.4 / Launcher version 1.2.5 ? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 10: migrated (2014-01-02T13:36:31.628-0800)

Can confirm that this is an issue in 1.6.4 and 1.7.4 both.

### Comment 11: migrated (2014-01-05T09:29:56.890-0800)

Please send this to Dinnerbone so he fixes it.
Yes it is a problem in 1.7.4 and it ruined my experince with my sister. I got really sad that it hapenned, does anyone knows how she can access her ender chest again?

### Comment 12: migrated (2014-02-22T04:16:55.226-0800)

I don't know if the Reporter of the bug will update the post, but I tested it and THIS IS STILL A PROBLEM IN THE LATEST SNAPSHOT.

### Comment 13: Ezekiel (2014-02-24T06:11:01.977-0800)

Ok

### Comment 14: Ezekiel (2014-07-24T19:01:39.417-0700)

Is this still a concern in the latest Minecraft version 14w30c? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 15: migrated (2014-08-08T14:58:38.671-0700)

Affects 1.7.10 & 14w32d.
Also, could anyone with the ability change the title of this ticket to reflect the broader nature of the bug? You don't need Ender Chests at all to see this.
I'm kind of surprised this ticket hasn't gotten more attention. It's essentially game-breaking for groups of 2 or more who only own 1 computer, but still want to collaborate.

### Comment 16: migrated (2014-10-01T09:26:13.637-0700)

There are at least a half dozen bug reports on this issue, going back at least to v1.4.6. All of them have been marked "Duplicate" except MC-5405, which has been marked "Invalid". The net result is that the moderators keep saying this is a non-issue, when in fact this continues to be a debilitating issue years after it was initially reported. The bug prohibits multiple players from playing on a single computer. It is open and it needs to be fixed.

### Comment 17: migrated (2014-10-24T12:20:48.195-0700)

Yup it's there in 1.8.1-pre3

### Comment 18: galaxy_2alex (2014-10-24T12:26:11.975-0700)

Reopened, thanks.

### Comment 19: FaRo1 (2016-06-09T11:43:24.764-0700)

Confirmed for 1.10.
The fact that it also happens with the inventory is mentioned in the comments and in most of the duplicates, but not in the description here. Might need a general overhaul, because it's hard to understand.

### Comment 20: FaRo1 (2016-06-22T14:25:02.916-0700)

Confirmed for 1.10.1.

### Comment 21: migrated (2016-06-25T13:32:40.246-0700)

The best workaround/prevention tip I can come up with right now to this issue is to backup your saves.
For all we know, the fix could come whenever Jeb, Dinnerbone, Grumm, or someone else decides to change the save format, which might be a while

### Comment 22: FaRo1 (2016-06-25T13:59:27.414-0700)

I don't think so. As far as I understand it, if you play in a SP world, the last saved inventory or the standard one or whatever gets copied to something linked to your UUID inside the saves folder. If that wouldn't happen, but it would just use the standard one while playing and also for the host in a LAN world, the inventories for UUIDs that get used on the LAN server would work normally and don't interfere with the normal SP playing. When it gets opened in LAN again later, there are the per-UUID inventories again ready to use.

### Comment 23: marcono1234 (2017-01-02T07:18:35.587-0800)

Would the title "Opening singleplayer world uses default player data even if playerdata for user exists after playing in LAN before" describe this bug better? That is based on MC-44064

### Comment 24: Michael Wobst (2017-01-02T07:24:30.081-0800)

: aye, sounds better to me.

### Comment 25: migrated (2018-01-09T14:38:53.300-0800)

Still an issue in 1.12.2 LAN. Affected ender chest, location, armour, inventory. When a second player opens tge world in single player mode they are given the first player's stuff. Also overwrote player 2 advancements.

### Comment 26: TheTamedWolf (2018-01-20T21:58:05.588-0800)

Is there a ticket for this issue for Bedrock Edition? I can;t find it when I search but I'm having this issue too but for MCPE. It makes it difficult for the host to transfer to another host. (like if your device can't handle it anymore or something) It opens the world as you and not the other player (who already has playerdata for that world).

### Comment 27: migrated (2018-09-16T13:37:56.544-0700)

Is there even a workaround for this? Like if I find the default player data and remove it before loading the world?
Trying to swap host machines for a LAN hosted world. 1.12.2

### Comment 28: FaRo1 (2018-09-16T13:58:32.377-0700)

Yes, just delete the inventory. Or, if you want to preserve the players' inventories, you have to move the inventories into the folders for the correct UUIDs.

### Comment 29: migrated (2018-09-16T14:02:56.834-0700)

Fabian, I have tried swapping the filenames (UUIDs?) of the two .DAT files within the /playerdata folder  -  this did not work, should it have? what file would i need to delete?

### Comment 30: FaRo1 (2018-09-16T14:19:55.551-0700)

From what I can see, it should work. Try it with two non-hosting inventories (A hosts LAN world, B and C join, you swap B and C).

### Comment 31: migrated (2018-09-16T14:42:35.596-0700)

I will try again, but someone said that when launching the world the default (single player) host data will overwrite the UUID playerdata file.
If this is true I need to find the default host data file(s) and delete or overwrite before launching the world.

### Comment 32: marcono1234 (2018-09-17T14:41:50.472-0700)

@, I added a workaround to the description. This should hopefully work.

### Comment 33: Jack McKalling (2018-10-18T14:37:46.630-0700)

I experienced this too, when I opened my world to lan, and later opened it under their account. From the description I understand this really is a bug, I imagined it might just be intended how the world is saved between single/multiplayer. I hope this gets fixed somehow sometime!

### Comment 34: pulpetti (2020-07-06T10:55:39.176-0700)

Confirmed in 20w27a

### Comment 35: migrated (2021-01-04T10:09:18.307-0800)

Confirmed in 1.16.4.
This bug was reported on the first day the issue tracker was open and still hasn't been fixed more than 8 years later.

### Comment 36: migrated (2021-03-07T14:30:29.337-0800)

I've gotten many emails about new comments here, but when I come to the page they're gone – is a mod deleting them?

### Comment 37: Jack McKalling (2021-03-07T14:52:57.231-0800)

Yes, don't worry.

### Comment 38: migrated (2021-03-07T18:02:49.436-0800)

A while back somebody said they were self-assigning this, and I saw their name under "Assignee" but now it's back to "Unassigned." What gives?

### Comment 39: migrated (2021-06-07T11:31:47.566-0700)

I can confirm for 1.17 release candidate 2, Assuming this is what I experienced. I logged on to a world on my main account, logged off, and back on with my second account using the same PC. We shared inventories. I then hosted a LAN world on my main and joined the LAN world on my alt, the alt had the same inventory as it did before, therefore, I was able to dupe items an infinite amount of times with this as the alt account's inventory changed to my main's every time I logged on to it in singleplayer. when you log onto a world in single player the inventory becomes the same as the last time the world was loaded, regardless of which account. This allows for duplicating an entire inventory as many times as you want as long as you have 2 accounts open on the same device. Although if your looking to dupe items and your using LAN to do so, its easier to just turn on cheats with LAN and go into creative mode.

### Comment 40: Brain81505 (2023-01-14T06:13:18.485-0800)

Can confirm in 1.19.3

### Comment 41: Brain81505 (2023-01-18T06:24:28.468-0800)

Can confirm in 23w03a

### Comment 42: Brain81505 (2023-01-24T23:20:27.267-0800)

Can confirm in 23w04a

### Comment 43: Brain81505 (2023-02-01T08:04:26.630-0800)

Can confirm in 23w05a

### Comment 44: Brain81505 (2023-02-11T07:29:54.940-0800)

Can confirm in 23w06a

### Comment 45: tryashtar (2026-02-03T10:54:21.170-0800)

Some changes were made to the handling of player data loading in 26.1-snapshot-6

### Comment 46: [Mod] ManosSef (2026-03-12T13:55:09.006-0700)

This issue was fixed in 26.1 Snapshot 6.
