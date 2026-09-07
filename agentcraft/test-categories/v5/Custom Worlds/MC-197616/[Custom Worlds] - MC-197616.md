# MC-197616: Certain custom biome settings cause game to spam "Received invalid biome id: -1" in the console, causing major lag or freeze

**Mojira URL:** [https://bugs.mojang.com/browse/MC-197616](https://bugs.mojang.com/browse/MC-197616)

## Report details

- **Mojira categories:** Custom Worlds; Performance
- **Project:** MC
- **Issue key:** MC-197616
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2020-08-10T06:53:28.445-0700
- **Updated:** 2025-05-29T09:15:59.286-0700
- **Resolution date:** 2022-06-02T10:41:13.272-0700
- **Affects versions:** 1.16.2 Release Candidate 2; 1.16.2; 1.16.3; 1.16.4 Pre-release 1; 1.16.4; 20w46a; 20w49a; 1.16.5; 21w06a; 21w08a; 21w11a; 21w13a; 21w14a; 21w15a; 21w16a; 21w17a
- **Fix versions:** 21w18a
- **Labels:** data-pack; performance
- **Watchers:** 2
- **Attachments:** 11
- **Attachment filenames:** 2020-08-10_14.58.41.png; 21w06a.png; after_unfreeze.png; Caves&Cliffs(NoBiomeFix).zip; debugDP.zip; den.zip; den-1.zip; dimp2n14.zip; MC-197616.zip; Minecraft_14-08-2020_20-15.mp4; unknown.png
- **Issue links:** Duplicate:inward:MC-223846:Data packs are sometimes not checked when a custom world is loaded for the second time

## Description

The bug
When teleporting to a dimension with custom biomes the client sometimes freezes or experiences major lag, with warnings in the output log "Received invalid biome id: -1".  In some cases the chunks eventually load, but then some chunks appear to have the ID "null" while other chunks appear to have the ID "minecraft:ocean". At this point crossing chunk borders will cause more chunks in the distance to generate and more warnings to be spamming in the log.
How to reproduce
- Download the attached data pack

-  and add it to a newly created world

- After spawning in, fly up a bit and teleport to the mc:197616 custom dimension

```
/execute in mc:197616 run tp @s ~ ~ ~
```

- The chunks load correctly with the correct biome in F3

- Teleport back to the overworld

```
/execute in minecraft:overworld run tp @s ~ ~ ~
```

- Move away a few chunks and then teleport back to the mc:197616 dimension

```
/execute in mc:197616 run tp @s ~ ~ ~
```

- The client freezes and lots of warnings appear in the output log (more than 1000 per second)

- If this doesn't happen (the world loads correctly) repeat steps 4 and 5. This seems to be related to render distance and world generation speed.

## Comments (83)

### Comment 1: migrated (2020-08-10T06:53:28.445-0700)

This comment contained multiple image attachments (11), please login to view the attachments.

### Comment 2: galaxy_2alex (2020-08-10T06:55:12.163-0700)

Please provide a screenshot of your game with the F3 debug screen enabled, please also provide the datapack in question.

### Comment 3: migrated (2020-08-10T06:55:22.786-0700)

world is in zip

### Comment 4: migrated (2020-08-10T06:57:22.264-0700)

if it loads lol

### Comment 5: anthony cicinelli (2020-08-10T06:58:21.577-0700)

You can do this on any world not just the buffet world (Provide the screenshot with F3)

### Comment 6: migrated (2020-08-10T07:00:30.691-0700)

its called den I made it as a test

### Comment 7: migrated (2020-08-11T04:35:10.161-0700)

sorry my files are the same name

### Comment 8: FX - PR0CESS (2020-08-12T20:55:27.344-0700)

Would like to mention that loading a superflat world with no mods and no datapacks on version 1.16.2 still causes the console to be spammed with invalid biome -1

### Comment 9: [MOD] Greymagic27 (2020-08-13T02:34:11.012-0700)

I can also reproduce this on a server that I play on.

### Comment 10: migrated (2020-08-14T20:20:24.545-0700)

This issue happens on a server I manage. All players are spammed with `Received invalid biome id: -1` in their clientside log; the serverside log does not contain any errors.
The world is default vanilla, not custom. It was generated in Minecraft version 1.16.1, and updated to 1.16.2 when the version was released.
Whilst ingame, it seems that certain biomes (not sure which exactly) will cause this spam. If you log out during the spam, or get kicked due to your client locking up, attempting to log back into the server will cause your clientside log to be spammed with this error and prevent you from logging in. I'll attach an example video, showcasing the spam happening during a server login attempt.

### Comment 11: ishland (2020-08-17T06:06:32.314-0700)

I can also reprduce this issue and it lags forever for some players on my creative server.

### Comment 12: ishland (2020-08-17T21:42:51.630-0700)

The lag comes from the logger logging this warning. As the logger do synchronized disk io and notifying the launcher log, it lags a lot.

### Comment 13: migrated (2020-11-18T11:55:59.812-0800)

I can confirm this is still an issue in 1.16.4's final release.

### Comment 14: Nate101 (2021-03-17T17:29:29.367-0700)

can confirm for 21w11a, this happens even if the base biomes have any little change to them, via color change or addition of already existing generations.

### Comment 15: Nate101 (2021-03-17T18:08:00.686-0700)

note, this isn't even from updating worlds to the latest snapshot, it can already exist if the world has any form of biome generation or customization in the existing datapack.

### Comment 16: Misode (2021-03-19T06:16:04.162-0700)

This appears to have gotten worse in 21w11a. It's reliability reproducible by having a biome with a custom configured structure feature.

### Comment 17: migrated (2021-03-21T08:38:57.828-0700)

In 21w11a game crashes before even entering the world.

### Comment 18: gnembon (2021-03-23T19:32:03.826-0700)

a renamed biome to a new one causes that as well - don't need to have a configured structure feature.
With this one / attached happens almost immediately and spams render thread:

```23:26:07.812
ckt
Render thread
Received invalid biome id: -1
23:26:07.812
ckt
Render thread
Received invalid biome id: -1
23:26:07.812
ckt
Render thread [^dimp2n14.zip]
Received invalid biome id: -1
23:26:07.812```
Attached dimp2n14.zip datapack with renamed biome with one configured feature to replicate.

### Comment 19: Nate101 (2021-04-01T12:30:10.783-0700)

Can confirm 21w13a

### Comment 20: Nate101 (2021-04-07T10:11:40.904-0700)

can confirm for 21w14a, the world has been doing fine until a certain amount of time while flying through the world caused the log to get spammed once more.

### Comment 21: migrated (2021-04-09T21:52:26.520-0700)

From my testing and debugging, this appears to be specifically caused by the json biome having any structures added to it and the user loads up an already generated chunk with that biome. The instructions about exiting and re-entering the dimension is not needed. Just fly forward in the dimension for a few seconds, turn around, and fly back and the issue will present itself.
I was helping someone with their mod and they were using json biomes/json dimensions for their mod and they got this issue because their biome has structures in it. When I ran the debugger, their biome source was using the correct dynamic registry instance and was returning the correct biome instance. But within SChunkDataPacket class, it had the exact same dynamic registry so that was good. But the biome being returned from the chunk is a completely new biome instance that is not present in the dynamic registry at all. And that is what causes the massive lag spike as the game starts writing the error to the log like crazy. So as far as I can tell, the biome source is not the issue here. The chunk receives the correct biome as well as it doesn't error upon first generation. Rather, the issue seem to lie in how the chunk either saves the biome to memory or retrieves the biome from memory. But only when structures are present in the biome.
Very odd situation but hopefully this digging I did helps

### Comment 22: migrated (2021-04-10T14:54:57.662-0700)

I've checked with someone who has such a case in a modded environment. Simply we loaded the world, then put a breakpoint on the Biome class' constructor and replicated it like telepathic grunt did above.

What I noticed looking through the debugger is that when structures are loaded, what yarn calls `RegistryOps` will attempt to load the biome from json and decode the biome. This occurs somewhere in the call site of `RegistryOps.of(...)`. This occurs in the constructor of `PoolStructurePiece` which occurs as a result of loading structure starts.

Yarn names of course, cannot recall what mojang's official names call these.

### Comment 23: Nate101 (2021-04-14T08:39:18.878-0700)

Can confirm for 21w15a, with THE CAVES & CLIFFS PROTOTYPE DATA PACK being used.

### Comment 24: migrated (2021-04-15T03:37:33.254-0700)

Seems to be happning on 21w15a world as well.
only without this datapack, and it seems to be triggereing when traveling from the nether to the overworld. but it does use the Caves & cliffs preview datapack.

### Comment 25: migrated (2021-04-15T05:55:15.316-0700)

this is exactly what happens when I fly around with the new 21w15a world gen datapack.

### Comment 26: migrated (2021-04-15T06:25:45.107-0700)

Can reproduce here in my world too with the Caves & Cliffs preview datapack, hope this will be fixed soon!

### Comment 27: migrated (2021-04-15T20:30:16.805-0700)

Can also reproduce here with 21w15a with the Caves and Cliffs datapack.
I suppose that there's no stopgap workarounds for this... :|

### Comment 28: AgentM (2021-04-16T06:46:40.131-0700)

I don't think it's intended to spam 1 million (without exaggeration) lines of LOG messages in 25 seconds time, basically freezing the client in place.
I ran this on a server, there is a huge spike when I teleported to world spawn. This happened twice and both times it was about 1 million messages like these:

```[22:21:49] [Render thread/WARN]: Received invalid biome id: -1```
Once from timestamp 22:07:57 til 22:10:25 and once from 22:21:49 til 22:22:14.
These log messages were sent to the client, the server logs seem to not contain any of these messages (since it's a renderer log message)

### Comment 29: migrated (2021-04-16T07:10:38.622-0700)

It would be nice if Mojang gave us options for tuning the verbosity of Minecraft's logging output, including being able to disable it entirely.

### Comment 30: migrated (2021-04-17T01:19:23.981-0700)

Note: it seems that it is most notable at spawn chunks. The lag seems to be a lot better once you go further from spawn, but it's still there as far as I know.

### Comment 31: migrated (2021-04-20T04:40:23.207-0700)

Same issue using this datapack. Is there any way I can help ?
I loaded the datapack and went into my custom dismension. Then I traveled throw it to check the generation and the error occuerend when I U-turned to kill a ghast (yeah I know poor creature ...). Now if I load the save it directly crashes like nothing can be loaded anymore.

### Comment 32: wilmerkardell (2021-04-21T11:21:21.443-0700)

Ran into this exact issue on 21w16a, using the co-current official Cliffs & Caves preview datapack. (Not a custom datapack.)
Seed: -5012719132029526681
X: 2327 Y:1245 (Dim: Overworld)
Going further west crashes the game (when a desert biome is loading.)

### Comment 33: migrated (2021-04-22T00:08:09.740-0700)

Unfortunately its hard to give a example to show because putting the exact seed and place doesn't give the same outcome. I've tried every time its crashed to get the seed and go back so I can give a example but for some reason this problem is completely random. it happens a lot though but usually when flying around in creative. Just tested the 21w16a datapack same bug occurs.

### Comment 34: migrated (2021-04-22T04:18:31.719-0700)

After testing this issue in several scenarios, can confirm in 21w16a. However it is rather inconsistent as @Willber mentioned...

Some points worth mentioning:

- I can say for sure in all scenarios the log line is being written... "Received invalid biome id: -1"
- However, having said that ... there are times when some kind of binary data is written to the latest.log, this causes a "lockup" of sorts, then subsequent attempts to write to the file appear to fail – i.e. the log file stops growing in size BUT the "Minecraft game output" GUI console ... continues to show logs for "Received invalid biome id: -1".

- At this stage ...  the world appears fine ... no lag, no freeze, (probably because no more logs being written)

- When you do get the lag/freeze ... that's when the log keeps getting written... keeps growing... likely Disk IO causing the lag/freeze.

- This only happens when crossing chunk boundaries... moving up and down in a chunk causes no lag/freeze issues as no chunks are being (un)loaded, no logs being written.

- For the same worlds  that are freezing.... (as @Frostrix mentioned) far away from spawn (for example @ 10000 ~ 10000), no logs, and no freezing...
- But again ... having said this, if you look carefully when at these distances, the log file grows for a short time... then seems to reach the "lockup" moment mentioned before (log file stops growing) ... which means you don't experience lag anymore.

- Now this is where the FUN part comes in .... If I /tp back to spawn.... and the log file comes out of it's "lockup" and starts writing to disk ... causing the lag/freezing in game to start up again !?? very confusing.

Really hope this info helps the devs  - this problem is very bad for an SSD with so many writes, and makes the current datapack somewhat unusable

All tests done on varying seeds with no obvious pattern (except for the points above) as to when the log file "lockup" would happen and when it wouldn't.

### Comment 35: migrated (2021-04-22T09:37:08.198-0700)

It happen to me as well. Latest snapshot, official Cliffs & Caves preview datapack. It happen after some time of playing (1h+). World starts lagging a lot and was unplayable. Restart does not help. So I delete the region folder and re-generated all chunks. Again. No issue, but after another hour world starts lagging again.
I can provide save if needed.

### Comment 36: migrated (2021-04-24T00:29:33.995-0700)

Set the file latest.log to "Read only" to solve this problem perfectly

### Comment 37: kanokarob (2021-04-24T11:21:48.441-0700)

No it doesn't, wayne, you're not helping.
Even if it reduces the lag when crossing chunk borders (which I did not find to be the case, at least not any more significantly than just exploring with the output log closed instead of open), the biomes still become null in-game.

### Comment 38: migrated (2021-04-24T11:47:05.536-0700)

So I've created a new world (random seed). Played for about three hours - no issue. Then I've logged, jumped to water, big lag that ended by my drowning

```[Info: 2021-04-24 18:38:32.318348239: GameCallbacks.cpp(162)] Game/clt (Render thread) Warn Received invalid biome id: -1
[Info: 2021-04-24 18:38:32.318385734: GameCallbacks.cpp(162)] Game/clt (Render thread) Warn Received invalid biome id: -1
[Info: 2021-04-24 18:38:32.318432171: GameCallbacks.cpp(162)] Game/clt (Render thread) Warn Received invalid biome id: -1
[Info: 2021-04-24 18:38:32.318465836: GameCallbacks.cpp(162)] Game/clt (Render thread) Warn Received invalid biome id: -1
[Info: 2021-04-24 18:38:32.318499183: GameCallbacks.cpp(162)] Game/clt (Render thread) Warn Received invalid biome id: -1
[Info: 2021-04-24 18:38:32.318531245: GameCallbacks.cpp(162)] Game/clt (Render thread) Warn Received invalid biome id: -1
[Info: 2021-04-24 18:38:32.318563047: GameCallbacks.cpp(162)] Game/clt (Render thread) Warn Received invalid biome id: -1
[Info: 2021-04-24 18:38:32.318595503: GameCallbacks.cpp(162)] Game/clt (Render thread) Warn Received invalid biome id: -1
[Info: 2021-04-24 18:38:32.318628453: GameCallbacks.cpp(162)] Game/clt (Render thread) Warn Received invalid biome id: -1
[Info: 2021-04-24 18:38:32.318660883: GameCallbacks.cpp(162)] Game/clt (Render thread) Warn Received invalid biome id: -1
[Info: 2021-04-24 18:38:32.318698185: GameCallbacks.cpp(162)] Game/clt (Render thread) Warn Received invalid biome id: -1
[Info: 2021-04-24 18:38:32.318730838: GameCallbacks.cpp(162)] Game/clt (Render thread) Warn Received invalid biome id: -1
[Info: 2021-04-24 18:38:32.344878018: GameCallbacks.cpp(162)] Game/dwb (Render thread) Info [CHAT] Hráč xmky02 utonul
^C```

And this is how it started:

```[Info: 2021-04-24 18:37:17.982335975: GameCallbacks.cpp(162)] Game/ezl (Server thread) Info Starting integrated minecraft server version 21w16a
[Info: 2021-04-24 18:37:17.986853727: GameCallbacks.cpp(162)] Game/net.minecraft.server.MinecraftServer (Server thread) Info Generating keypair
[Info: 2021-04-24 18:37:18.968733020: GameCallbacks.cpp(162)] Game/net.minecraft.server.MinecraftServer (Server thread) Info Preparing start region for dimension minecraft:overworld
[Info: 2021-04-24 18:37:23.203248724: GameCallbacks.cpp(162)] Game/abu (Render thread) Info Příprava výchozí oblasti: 0 %
[Info: 2021-04-24 18:37:23.203430091: GameCallbacks.cpp(162)] Game/abu (Render thread) Info Příprava výchozí oblasti: 0 %
[Info: 2021-04-24 18:37:23.203526497: GameCallbacks.cpp(162)] Game/abu (Render thread) Info Příprava výchozí oblasti: 0 %
[Info: 2021-04-24 18:37:23.203594823: GameCallbacks.cpp(162)] Game/abu (Render thread) Info Příprava výchozí oblasti: 0 %
[Info: 2021-04-24 18:37:23.203656154: GameCallbacks.cpp(162)] Game/abu (Render thread) Info Příprava výchozí oblasti: 0 %
[Info: 2021-04-24 18:37:23.204441182: GameCallbacks.cpp(162)] Game/abu (Render thread) Info Příprava výchozí oblasti: 0 %
[Info: 2021-04-24 18:37:23.207208730: GameCallbacks.cpp(162)] Game/abu (Render thread) Info Příprava výchozí oblasti: 0 %
[Info: 2021-04-24 18:37:23.207490545: GameCallbacks.cpp(162)] Game/abu (Render thread) Info Příprava výchozí oblasti: 0 %
[Info: 2021-04-24 18:37:23.207666080: GameCallbacks.cpp(162)] Game/abu (Render thread) Info Příprava výchozí oblasti: 0 %
[Info: 2021-04-24 18:37:23.678794290: GameCallbacks.cpp(162)] Game/abu (Render thread) Info Příprava výchozí oblasti: 3 %
[Info: 2021-04-24 18:37:24.272231446: GameCallbacks.cpp(162)] Game/abu (Render thread) Info Příprava výchozí oblasti: 31 %
[Info: 2021-04-24 18:37:24.672528561: GameCallbacks.cpp(162)] Game/abu (Render thread) Info Time elapsed: 5614 ms
[Info: 2021-04-24 18:37:24.974781086: GameCallbacks.cpp(162)] Game/ezl (Server thread) Info Changing view distance to 21, from 10
[Info: 2021-04-24 18:37:27.628770610: GameCallbacks.cpp(162)] Game/adz (Server thread) Info xmky02[local:E:10813043] logged in with entity id 5 at (-1610.664300010871, 64.0, 134.99084079997692)
[Info: 2021-04-24 18:37:27.718101833: GameCallbacks.cpp(162)] Game/net.minecraft.server.MinecraftServer (Server thread) Info Hráč xmky02 se připojil do hry
[Info: 2021-04-24 18:37:28.852599064: GameCallbacks.cpp(162)] Game/net.minecraft.server.MinecraftServer (Server thread) Warn Can't keep up! Is the server overloaded? Running 2164ms or 43 ticks behind
[Info: 2021-04-24 18:37:29.097362863: GameCallbacks.cpp(162)] Game/ezl (Server thread) Info Saving and pausing game...
[Info: 2021-04-24 18:37:29.193369855: GameCallbacks.cpp(162)] Game/net.minecraft.server.MinecraftServer (Server thread) Info Saving chunks for level 'ServerLevel[21w16a_ore_veins_II]'/minecraft:overworld
[Info: 2021-04-24 18:37:29.877669595: GameCallbacks.cpp(162)] Game/ae (Render thread) Info Loaded 291 advancements
[Info: 2021-04-24 18:37:31.621556610: GameCallbacks.cpp(162)] Game/net.minecraft.server.MinecraftServer (Server thread) Info Saving chunks for level 'ServerLevel[21w16a_ore_veins_II]'/minecraft:the_nether
[Info: 2021-04-24 18:37:31.622520015: GameCallbacks.cpp(162)] Game/net.minecraft.server.MinecraftServer (Server thread) Info Saving chunks for level 'ServerLevel[21w16a_ore_veins_II]'/minecraft:the_end
[Info: 2021-04-24 18:38:00.592485006: GameCallbacks.cpp(162)] Game/clt (Render thread) Warn Received invalid biome id: -1
[Info: 2021-04-24 18:38:00.592815656: GameCallbacks.cpp(162)] Game/clt (Render thread) Warn Received invalid biome id: -1
[Info: 2021-04-24 18:38:00.593312986: GameCallbacks.cpp(162)] Game/clt (Render thread) Warn Received invalid biome id: -1
[Info: 2021-04-24 18:38:00.593966302: GameCallbacks.cpp(162)] Game/clt (Render thread) Warn Received invalid biome id: -1
[Info: 2021-04-24 18:38:00.594443655: GameCallbacks.cpp(162)] Game/clt (Render thread) Warn Received invalid biome id: -1
[Info: 2021-04-24 18:38:00.594787136: GameCallbacks.cpp(162)] Game/clt (Render thread) Warn Received invalid biome id: -1```

### Comment 39: migrated (2021-04-26T04:42:18.572-0700)

I just went to "Edit" and hit "Optimize World," and it helped a little bit. Although the glitch still occurs (sadly), it can temporarily help if you're stuck in a crash loop when loading up the world.

### Comment 40: SeaOfPixels (2021-04-27T10:50:28.640-0700)

Since this now effects the Caves & Cliffs datapack (V1 and V2), I'd consider it a major bug that needs top prioritization.

### Comment 41: migrated (2021-04-27T11:19:51.423-0700)

I posted a bug report about this with the caves and cliffs datapack, when leaving the nether from teleporting/dying it turns the entire spawn region or more into ocean, it makes it completely unplayable with the lag/corruption and I hope this gets fixed soon!

### Comment 42: Nate101 (2021-04-28T09:04:00.850-0700)

can confirm for 21w17a

### Comment 43: migrated (2021-04-28T09:58:55.248-0700)

Does anyone know how to disable logging to preserve SSD health?  And perhaps where to edit a Biome Id?
This makes the game unplayable in 21w16a and 21w17a.

### Comment 44: migrated (2021-04-28T09:59:48.362-0700)

Yes, 21w17a, latest Caves&Cliffs datapack. I've created a brand new world, played it about 1 hour, then exited the game. After new start I've created a backup as game suggested and opend the World. I didn't move, only open a furnance GUI. Then game lags again and world is corrupted

### Comment 45: migrated (2021-04-28T12:54:58.203-0700)

I can confirm it is possible to edit the attributes to read only. This will stop the log from being used but the lag will still happen. It doesn't appear to be related to the log or to Disk IO.

### Comment 46: migrated (2021-04-28T23:51:19.440-0700)

I don't know if "Important" is the highest priority but I really advice you to make this issue the biggest possible.
Now the problem event show when youtubers want to show snapshot updates that is stragically a bad thing for Mojang
Ii.e with Aypierre here : https://youtu.be/MPcfoHC6DCI?t=517

### Comment 47: migrated (2021-04-29T02:20:37.807-0700)

I agree with increasing the priority of the task, however not for Candelaresi's reasons. Sorry, but this is a snapshot release, no one cares (in a way that would damage Mojang's reputation) if it is not working perfectly, it is not the mainstream stable release, teething is to be expected in snapshot releases - especially datapacks like this one, because of the primary purposes of improving development and looking after the health of the Mojang team.
Having said that - and without insinuating there should be more pressure on the team - the last two releases are actually unusable, sort of defeating the purpose of releasing more snapshots if you can't even test them and provide feedback ... so it does make it high priority in the sense of a "broken snapshot" that can't be properly used or tested.
I imagine a great deal of players don't have SSD's or copious amounts of RAM, so this isn't going to take an hour or two to crash, my own machine with SSD and 16G RAM (intermittently) will crash within 5-10 minutes of spectator mode with the latest datapack ... this means testing isn't really feasible, and is (at least slightly) damaging to SSD's as well with the writes, so this (IMO) should take higher priority to be fixed.

### Comment 48: migrated (2021-04-29T05:05:45.699-0700)

Agree with@Kai , I prefer mojang to spend several weeks on fixing it. We can wait for a more stable snapshot so that we can test it and feedback.

### Comment 49: migrated (2021-04-29T07:30:06.498-0700)

I think that the other commenters are correct, as well; at the very least, we need a way to disable this specific error from spamming the log. I really want to play on this datapack, but I don't want my motherboard's SSD to end up getting damaged by doing so. We really need a 21w17b datapack that doesn't crash the game or literally damage players' hardware...

### Comment 50: migrated (2021-04-30T10:45:23.937-0700)

This edited Caves&Cliffs preview pack should fix the issue! : )
It removes the custom biomes that cause the bug, although that means the updated 1.18 ore distribution won't happen. However, the dripstone clusters, caves, geodes, etc. work just fine! I hope this is good enough until the datapack biome bug gets fixed!
(Note: The ores still generate below Y leve 0, which is a good plus for this datapack! Also means deepslate coal is common with it)
Update: The bug still occurs, although much more tamed. Thankfully it avoids the null biome bug.

### Comment 51: migrated (2021-04-30T18:35:28.021-0700)

Thanks @Lunade Lunade!  I see you deleted the Biomes folder- I suppose that means the Lush Caves are gone?  Does Mojang take on volunteer bug hunters?  If so, I'd be down to sign an NDA and spend a few days digging through the codebase to squash this one.

### Comment 52: migrated (2021-05-01T04:05:32.768-0700)

I believe adding a custom dimension bypass this bug at least on one biome

### Comment 53: migrated (2021-05-01T12:06:48.421-0700)

note it doe not work

### Comment 54: migrated (2021-05-01T13:13:45.310-0700)

better fix it soon i hope snapshots are a pain with it like this

### Comment 55: migrated (2021-05-01T14:46:51.497-0700)

Someone mentioned, that this is connected to structures. So I've created a new world without structures and I'm not able to reproduce the invalid biome issue. But no villages, mine shafts…

### Comment 56: KirbAvion (2021-05-02T03:04:00.016-0700)

I can also confirm that my dimension stopped experiencing null biome errors after I removed my custom structures from the biome "starts" field. I cannot, however, offer any explanation as to why.

### Comment 57: migrated (2021-05-03T04:34:25.668-0700)

i think the lag only happens when its in a datapack so the thing to do would be bypass the datapack system

### Comment 58: migrated (2021-05-03T06:16:04.819-0700)

My noise cave nether datapack works fine must be a height based thing
Here’s my planet minecraft link as I can’t link it right now to try my pack https://www.planetminecraft.com/data-pack/noise-cave-nether/

### Comment 59: migrated (2021-05-04T06:14:27.740-0700)

I ended up living in the nether to avoid it

### Comment 60: SirDaddicus (2021-05-04T08:16:25.778-0700)

Ticket MC-224767 was "resolved" (by a bot) as a duplicate of this ticket. MC-224767 has absolutely nothing to do with this ticket. Please re-open MC-224767.

### Comment 61: anthony cicinelli (2021-05-04T08:19:25.060-0700)

this is not the place to request re-opens please go to the Mojira subreddit for request like these, not other peoples reports.

### Comment 62: SirDaddicus (2021-05-04T11:02:34.708-0700)

You don't handle your own tickets? What kind of "support" is this?
Just forget it. It's clear bug reporting isn't important to the development of new features at Mojang. I'll just wait until a future snapshot comes out and try again.

### Comment 63: kanokarob (2021-05-04T12:21:22.391-0700)

@Jim Also this bug is actually the cause of that one you requested to be reopened, maybe pay a little attention and do some actual troubleshooting to determine where the two add up.

### Comment 64: SirDaddicus (2021-05-04T18:42:31.787-0700)

And you know that how?

### Comment 65: migrated (2021-05-04T18:45:59.573-0700)

@dan hop, your datapack doesn't modify or create any biomes. That's why it works fine.

### Comment 66: kanokarob (2021-05-04T19:20:15.026-0700)

@Jim Because your description of the problem, how it presents and steps to recreate match with the troubleshooting that's been done by myself and others in pursuit of understanding this bug. You just didn't think hard enough and look far enough before deciding to complain that Mojang was being "unacceptable."

### Comment 67: SirDaddicus (2021-05-04T20:16:52.088-0700)

Custom biome? Invalid biome id? Custom dimension? Those are symptoms prominently mentioned in this ticket, yet I never listed (nor have I seen). I'm in a vanilla world, and I see the problem (sometimes) VERY early in the game (like, within the first 2 minutes). Other times, it takes hours.
A technical support team should look at the logs to find out if this is indeed the same problem. From your comments, it's plausible, but certainly not at the top of the list. Valid tech support verifies the problem rather than just guessing (as you have done, as well) that the problem is the same.

### Comment 68: migrated (2021-05-04T22:22:52.452-0700)

Sorry Jim, you are still on the wrong track. Claiming its vanilla, and installing the Data Pack for 21w17a.... Means you're missing an important point (one that is described when you load the data pack by the way)... You are running a custom world! Hence read more carefully from start to finish, this whole case, and you will hopefully see where you misunderstood. You'll be happy to know your problem of freezing/lagging, etc will be looked at when they fix this bug.

As a side note, this case was originally opened only for custom worlds, but when the data pack was released - because it was installing custom biomes - it became linked to this case.

### Comment 69: migrated (2021-05-04T23:13:42.134-0700)

@Jim Gersetich, that datapack modifies all biomes in overworld to fit new height.

### Comment 70: slicedlime (2021-05-05T00:41:31.251-0700)

The main cause of this is now fixed. There may be other issues remaining that cause the same error message - if so please post new specific issues identifying the settings that still cause the error.

### Comment 71: migrated (2021-05-05T12:08:57.254-0700)

much better still jumpy but the custom worlds dont crash

### Comment 72: migrated (2021-05-05T15:01:00.968-0700)

Does this mean Mojang's CavesAndCliffsPreview.zip is finally safe to use? Or at least the week 18 one?

### Comment 73: migrated (2021-05-06T00:23:48.790-0700)

It still jumpy but you can use it

### Comment 74: SirDaddicus (2021-05-06T14:57:04.078-0700)

Do we need to download a new copy of the datapack to test this fix?

### Comment 75: SirDaddicus (2021-05-06T16:11:14.323-0700)

It appears you all may be correct: I haven't experienced the slowdown in an hour or so of playing.
Kai: The message mentions nothing about custom biomes or dimensions. It merely says "experimental", which might be interpreted that way, IF one knew that it was even possible.
I contend that the Description field should have been updated at the time you say they discovered it applied to the datapack they are trying to get us to test.

### Comment 76: migrated (2021-05-07T01:21:30.186-0700)

Good to hear it's working for you @Jim, working for me too .
Yeup, in this case, the data pack makes/modifies biomes (thus becoming custom biomes) which don't exist in vanilla (like noise or lush caves, etc), therefore falling into experimental.
More often than not, because it's extremely time consuming for moderators to explain their actions in detail, and update fields constantly to match new findings ... the easier thing is to read the tasks. I truly understand it can be a pain, as this task had A LOT of content to read, but it frees up moderators to handle cases as quickly as possible and they're working for us at the end of the day. Then viola, it gets fixed
Hope you enjoy!

### Comment 77: SirDaddicus (2021-05-07T08:13:10.501-0700)

Kai:
It shouldn't be a moderator that makes such a change. It should be a developer, or perhaps a moderator operating under development instructions.
I know NOW that experimental = custom, and it makes sense. But, this is a bug report mechanism, and nobody (official) should ever assume that posters know what certain constructions mean. Above all things, a bug reporting mechanism must be fully understandable to EVERYBODY who uses it. No prior knowledge should be expected.
This is because it is primarily the newbies who are going to find the problems. By definition, they don't know what should and should not be issues or why. The mechanism by which they report issues should be almost bulletproof to them.
Experts can chime in to explain things, but the descriptive text of anchor tickets (tickets under which duplicates are held in stasis) needs to properly reflect the bulk of the information needed to figure out whether a new ticket fits or not. Perhaps a new section near the top should exist, titled "Moderator Notes" or "Development Notes" or something like that.
I searched for tickets using all the keywords I could think of that would apply. And, I even came across this ticket in those searches. But, the description was so far from what my experience was that I couldn't envision it being the same problem.
Two things could have been added that would have helped. First, the description could have mentioned the word performance or lockup or something similar. This would have indicated to me that the ticket could be a match.
Second, the description (or another proper field, but always near the top) should mention HOW one can check the logs to find out if this problem is indeed what they are experiencing. Even a link to a wiki page would be acceptable for this purpose.
Finally, I still don't actually know how to look at the logs. I know they must exist, but even now, knowing the problem was my problem, I don't know experientially how to tell for certain that this was true. I found a Crash Report page on the wiki, but the game wasn't crashing, only hanging for periods of time. So, if a similar problem happened again, I would be at a loss to figure out whether something was being spammed into the log file.

### Comment 78: kanokarob (2021-05-07T09:58:24.795-0700)

Bro, can you shut up @Jim? You misunderstood the cause of your bug, the moderation team's quite intentional and reasonable manner of response to it, the purpose and intent of this bug, and the actual state of experimental custom world features. But that's okay, no one was holding it against you until now. Quit while you're behind and move on with everyone's lives.

### Comment 79: [MOD] Greymagic27 (2021-05-07T14:02:22.106-0700)

Please remember the bug tracker is not a discussion forum and any discussion about a bug should take place outside of the bug tracker, such as on our reddit and/or our discord server.
Quick Links:
📓 Bug Tracker Guidelines – 💬 Community Support – 📧 Mojang Support
📓 Project Summary – ✍️ Feedback and Suggestions – 📖 Game Wiki

### Comment 80: migrated (2021-05-12T06:43:56.251-0700)

I'm experiencing a similar bug in 21w19a even without the datapack, every chunk border causes lag
I don't know if I should report it or not because I don't understand the causes/technical things behind it, but just wanted to get it out there.

### Comment 81: migrated (2021-05-12T07:13:03.416-0700)

You using any datapack that makes the chunk height bigger
if so check out MC-225178

### Comment 82: migrated (2021-05-12T17:36:08.897-0700)

Actually I found out my problem, it's a weird solution but someone talked about it before.
I gave it 4GB of RAM, and I guess since it takes longer to clear, it caused lag. Once I gave it only 2GB of RAM, it was fine.
I don't know why I didn't think of that earlier

### Comment 83: migrated (2021-05-20T08:23:40.163-0700)

Once, I Tried To Make An End Noise Nether. So, There Is A Nether Waste Cutting The Crimson Forest And Warped Forest. The Game Lag, Then Crash. When I Reload The World, The Nether Waste, A Bit Of Crimson Forest, And A Bit Of Warped Forest Turn Into Ocean Biome. Such A Weird Bug.
