# MC-44514: Teleporting ridden entity in unloaded chunks does not cause chunks to load for riding player

**Mojira URL:** [https://bugs.mojang.com/browse/MC-44514](https://bugs.mojang.com/browse/MC-44514)

## Report details

- **Mojira categories:** Entities; Networking; Player
- **Project:** MC
- **Issue key:** MC-44514
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2014-01-10T08:56:30.116-0800
- **Updated:** 2025-04-29T08:47:41.334-0700
- **Resolution date:** 2024-06-13T13:50:00.989-0700
- **Affects versions:** Minecraft 14w02b; Minecraft 14w02c; Minecraft 14w03a; Minecraft 14w05a; Minecraft 14w07a; Minecraft 14w08a; Minecraft 14w10a; Minecraft 14w17a; Minecraft 14w19a; Minecraft 14w25a; Minecraft 14w28a; Minecraft 14w28b; Minecraft 14w30a; Minecraft 14w31a; Minecraft 14w32b; Minecraft 14w33a; Minecraft 14w34d; Minecraft 1.8-pre1; Minecraft 1.8-pre3; Minecraft 1.8; Minecraft 1.8.3; Minecraft 15w49b; Minecraft 16w33a; Minecraft 1.11.2; Minecraft 1.12.1; Minecraft 1.12.2; Minecraft 1.13-pre8; Minecraft 1.13; Minecraft 18w30b; Minecraft 18w31a; Minecraft 18w32a; Minecraft 18w33a; Minecraft 1.13.1-pre1; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w43b; Minecraft 18w45a; Minecraft 18w46a; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 19w04b; Minecraft 19w07a; Minecraft 19w12b; Minecraft 19w13b; Minecraft 19w14a; Minecraft 19w14b; Minecraft 1.14.3; 1.14.4; 1.15.2; 20w08a; 20w12a; 20w14a; 20w19a; 20w21a; 20w22a; 1.16 Pre-release 3; 1.16 Pre-release 5; 1.16 Pre-release 7; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w29a; 1.16.2; 1.16.4; 20w51a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 1.17; 1.18; 1.18.1; 1.19; 1.19.2; 23w04a
- **Fix versions:** 23w12a
- **Area:** Platform
- **Labels:** boat; chunk; horse; mount; riding; teleport; unloaded-chunks
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2019-06-24 13-58-18.mp4; after_relogging.png; after_teleporting.png; before_teleporting.png
- **Issue links:** Relates:outward:MC-269025:End Gateways don't load chunks when entities travel through them | Duplicate:inward:MC-77879:Horse and rider both glitch after /tp @e[type=EntityHorse] over long distances | Duplicate:inward:MC-80397:Player "Dismounts" When Mount is Teleported to Unrendered Area | Duplicate:inward:MC-82030:Far tp Horse stacking player error | Duplicate:inward:MC-91628:End gateway teleportation fails when player is passenger of boat or horse | Duplicate:inward:MC-100635:End Gateway (Block) | Duplicate:inward:MC-116139:Riding a minecart into an end gateway sends you to destination but never loads chunks | Duplicate:inward:MC-165514:Minecarts with players get stuck when teleported to unloaded chunks | Duplicate:inward:MC-183692:Teleporting Horses outside of chunks while riding freezes the player. | Duplicate:inward:MC-217371:Teleporting boats and minecarts to unloaded chunk while riding glitches | Relates:inward:MC-165589:Ridden entities can not be teleported to non-loaded chunks using an end gateway

## Description

The bug
Teleporting an entity which is ridden by a player into unloaded chunks teleports the player (client-side) but does not load the chunks.
In current versions, the player becomes stuck visually at their current position and their screen jitters, but the coordinates on the debug screen show that they moved some (but not the complete) distance.
In 1.18, the boat teleports but the player desyncs and cannot interact with anything that is not near the location where they typed the command.
As of 23w04a, teleporting the boat into unloaded chunks dismounts the player client-side. If the player tries breaking or placing blocks after running the command, these actions will generally be invalidated by the server, although in some circumstances they seem to work even though the server thinks the player is far away. The F3 coordinates seem to consistently reflect where the player appears to be (on the client). If the player runs /ride @s dismount or relogs, they will be teleported to the boat and will load the chunks around it.
How to reproduce
- Place a boat and enter it

- Use the following command

```
/tp @e[type=minecraft:boat,sort=nearest] ~ ~ ~5000
```

- Enable the debug information
→ You will see that you were teleported (client-side), but using for example commands which print the block coordinates like /execute if block ~ ~ ~ air run say @s show that server-side you have not moved

The screenshots show a mounted horse before teleporting at 0,1000; the "void" after teleporting the horse; and the mounted horse at 0,5000 right after relogging.
Code analysis
Based on 1.11.2 decompiled using MCP 9.35 rc1
The reason is the same one as for  and MC-108469: The method net.minecraft.world.World.updateEntityWithOptionalForce(Entity, boolean) does not update entities which are not in loaded chunks server-side. The problem here is that the riding player is not instantly moved with the ridden entity but instead when the method Entity.updateRidden() is called, which in this case never happens because the area around the ridden entity is not loaded.

## Comments (34)

### Comment 1: migrated (2014-01-10T08:56:30.116-0800)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: Torabi (2014-02-16T03:29:38.487-0800)

That is fascinating. What happens if you try to move? Dismount?

### Comment 3: migrated (2014-02-18T03:49:40.389-0800)

No, your actions appear to have no effect until relogging at which point you're back on the horse.

### Comment 4: migrated (2014-03-06T06:48:24.090-0800)

In 14w10a the horse vanishes instead of reappearing after relogging.

### Comment 5: migrated (2014-07-09T13:58:37.480-0700)

This problem still exists in 14w28a and the horse is still vanishing.

### Comment 6: migrated (2014-07-10T08:00:04.164-0700)

In 14w28b the horse reappears again after relogging but the basic issue still persists.

### Comment 7: migrated (2014-08-07T09:18:21.507-0700)

In 14w32b the player gets teleported but only half of the world loads before relogging. The part that's not loaded includes the player's position.

### Comment 8: migrated (2014-08-07T15:20:11.649-0700)

confirmed for 14w32b

### Comment 9: migrated (2014-08-21T09:04:01.105-0700)

In 14w34d loading the world after teleporting works from time to time but I'm floating over the ground and the horse is gone. As before, this is fixed by relogging.

### Comment 10: migrated (2014-08-22T06:25:49.572-0700)

This bug is still happening in the first pre-release, 8 months after submitting.

### Comment 11: migrated (2014-09-03T00:22:50.156-0700)

Great job Mojang, this was reported for the second snapshot and is still in the release.

### Comment 12: migrated (2015-03-19T02:11:51.444-0700)

I see this as well in 1.8.3, it occurs if you teleport the horse too far while riding it:
/tp @e[type=EntityHorse] ~81 ~ ~
OR
/tp @e[type=EntityHorse] ~-80 ~ ~
Anything less than those distances works fine as intended.
After teleporting, you can move but slowly and you'll hear your horse but it is invisible and you'll be back at ground level.  If you dismount, you can move fine, but your horse will be invisible until unknown conditions occur (or relogging).  Staying on the horse and relogging shows you fine on the horse.

### Comment 13: migrated (2015-03-19T02:41:32.767-0700)

It looks like in 14w10c (the same issue occurs at the same distances) that if I dismount the horse and move a couple blocks away the horse reappears, this is not the case in 1.8.3.

### Comment 14: migrated (2015-03-20T21:20:57.480-0700)

Tested the Y direction, works fine.
Also tried teleporting other mobs long distances and discovered that they disappear too!  At least until the player moves/looks around a bit.  For instance if I teleport a Spider Jockey 100 blocks away into the daylight near my position now, I'll hear him burning, but until I move a bit, I won't see him.
Seems like another bug or maybe related to this same issue?  Maybe related to MC-65040
It also appears that the horse teleports visually before the player does, I see the horse for a brief instance in the distance before I move, but then the horse is invisible.
As a player, you're stuck on the horse and get snapped back to its location if you try and move.  You can dismount, but the horse is still invisible.

### Comment 15: migrated (2015-03-21T03:24:47.567-0700)

Thanks for testing, I've updated the version. Btw, the Y axis is fine because it has no effect on chunk loading.

### Comment 16: migrated (2015-03-22T02:04:55.963-0700)

Thanks for updating the version.  I don't think it has as much to do with chunk loading as rendering.  Because you'll hear the mob still, so it knows it's there, you just can't see it.
I tested this out in multiplayer too.  On your own machine, you get stuck and the horse is invisible.  But if you see someone do it, you'll still see them on the horse (though sometimes it takes a bit or you have to look around a bit, probably related to MC-65040).  Of course, since they're stuck, you won't see them moving.
Leads me to believe it's a local-client issue as if another player sees things properly then the server must have the proper info.

### Comment 17: onnowhere (2015-12-07T14:18:23.453-0800)

Still occurring 15w49b. In the few tests I did, I so far got the following results on render distance 8:
- Teleported into unloaded chunks (I used ~200 ~ ~), world is not loading until relog which takes me back to where I was before getting on the horse because the world did not seem to have saved

- Teleported into unloaded chunks (I used ~200 ~ ~), world is not loading. Relogged, and now I'm on the horse in the right spot but I can't move or dismount until it is killed.

- Teleported into nearby chunks (I used ~100 ~ ~), I fell to the ground at the original spot, gameticks stop running for a second, then things update and now I'm back on the horse in the correct spot.

### Comment 18: migrated (2015-12-17T08:25:45.414-0800)

I think this behavior may be changed (but still broken in a slightly different way) in 15w51b

### Comment 19: migrated (2016-11-06T03:10:41.405-0800)

Is this still an issue in the latest snapshot 16w44a? If so please update the affected versions.
This is an automated comment on any open or reopened issue with out-of-date affected versions.

### Comment 20: [Mod] Asteraoth (2018-07-13T15:58:45.101-0700)

Confirmed for 1.13-pre8

### Comment 21: [Mod] Asteraoth (2018-07-18T12:25:47.860-0700)

Confirmed for 1.13

### Comment 22: [Mod] Asteraoth (2018-07-26T12:35:42.050-0700)

Confirmed for 18w30b

### Comment 23: [Mod] Asteraoth (2019-06-24T11:01:43.111-0700)

Note: Teleporting the boat in 1.14.3 caused
 to happen.

### Comment 24: [Mod] violine1101 (2020-02-25T15:38:51.838-0800)

Can confirm; the ticket's description is no longer up to date though. The player just gets stuck in the original location and isn't actually teleported.

### Comment 25: pulpetti (2020-07-06T11:37:13.890-0700)

Affects 1.16.1 and 20w29a

### Comment 26: markderickson (2021-01-14T13:47:33.440-0800)

Can confirm in 20w51a.

### Comment 27: Avoma (2021-01-29T12:05:44.457-0800)

Can confirm in 21w03a.

### Comment 28: Avoma (2021-02-06T05:41:37.238-0800)

Can confirm in 21w05b.

### Comment 29: Avoma (2021-02-12T05:51:11.059-0800)

Can confirm in 21w06a.

### Comment 30: migrated (2021-03-08T05:14:56.127-0800)

Maybe we could add the label "minecart" to this bug report, in addition to "boat" and "horse". Perhaps that would help get this issue noticed by Mojang. I've long wanted to extend my minecart system to include jumping from an overworld track to a track in the nether or the end, but this bug prevents that.

### Comment 31: Avoma (2022-02-16T08:08:40.224-0800)

Can confirm in 1.18.1.

### Comment 32: Avoma (2022-10-26T03:18:54.003-0700)

Can confirm in 1.19.2.

### Comment 33: clamlol (2023-01-24T17:45:38.116-0800)

As of 23w04a, teleporting the boat into unloaded chunks dismounts the player client-side. If the player tries breaking or placing blocks after running the command, these actions will generally be invalidated by the server, although in some circumstances they seem to work even though the server thinks the player is far away. The F3 coordinates seem to consistently reflect where the player appears to be (on the client). If the player runs

```/ride @s dismount```
or relogs they will be teleported to the boat and will load the chunks around it.

### Comment 34: clamlol (2024-06-13T13:00:42.239-0700)

This issue was fixed in 23w12a as part of the fix for [MC-201647]. However, passengers are not teleported instantaneously (as they are when teleporting them directly); it seems like the chunk they're being teleported to must finish loading first. I may decide to make a separate ticket for this.
