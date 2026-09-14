# MC-162253: Lag spike when crossing certain chunk borders

**Mojira URL:** [https://bugs.mojang.com/browse/MC-162253](https://bugs.mojang.com/browse/MC-162253)

## Report details

- **Mojira categories:** Performance
- **Project:** MC
- **Issue key:** MC-162253
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2019-09-29T10:31:08.934-0700
- **Updated:** 2025-05-29T09:20:56.086-0700
- **Resolution date:** 2024-03-09T20:30:16.542-0800
- **Affects versions:** 1.14.4; 19w39a; 19w40a; 19w41a; 1.15 Pre-release 1; 1.15.1; 1.15.2; 20w06a; 20w12a; 20w17a; 20w18a; 1.16 Pre-release 2; 1.16 Pre-release 4; 1.16 Pre-release 5; 1.16 Pre-release 8; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w27a; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.2; 1.16.3; 1.16.4 Pre-release 2; 1.16.4; 20w45a; 20w46a; 20w49a; 1.16.5; 21w06a; 21w08b; 21w11a; 21w15a; 21w16a; 21w18a; 21w20a; 1.17 Pre-release 4; 1.17 Pre-release 5; 1.17 Release Candidate 1; 1.17 Release Candidate 2; 1.17; 1.17.1 Pre-release 1; 1.17.1 Release Candidate 1; 1.17.1; 21w40a; 21w44a; 1.18 Pre-release 1; 1.18 Pre-release 5; 1.18 Release Candidate 3; 1.18; 1.18.1 Pre-release 1; 1.18.1; 22w07a; 1.18.2 Pre-release 1; 1.18.2; 22w12a; 22w17a; 22w18a; 1.19; 1.19.2; 1.19.3; 23w07a; 1.19.4
- **Fix versions:** 23w16a
- **Watchers:** 2
- **Attachments:** 7
- **Attachment filenames:** 2020-03-31_12.25.37.png; 2023-01-21_01_24_55-What A Crowded World!-1_19_3.zip; Danielps1818.zip; MC-162253.mp4; MC-162253.png; Minecraft 2023.01.21 - 01.23.46.04_Trim.mp4; projet-sans-nom_pWthAUOB.compressed-1.mp4
- **Issue links:** Relates:inward:MC-166005:Stuttering when crossing chunk borders/loading chunks | Duplicate:inward:MC-167553:Lag Spike if you go trough specific chunks in Amplified | Duplicate:inward:MC-168419:Massive frame drops caused by light update while crossing certain chunks | Duplicate:inward:MC-168904:FPS is drops unless i hold down a mouse button | Duplicate:inward:MC-168956:Moving across specific chunk borders causes a lag spike | Duplicate:inward:MC-169580:Lag spikes, between chunks | Duplicate:inward:MC-170809:When playing anything above 1.13, crossing a chunk border causes scheduled executable to jump up in use, causing fps drops | Duplicate:inward:MC-175907:Lag spike when moving between chunks | Duplicate:inward:MC-187877:Game Freezes For a Few Seconds when Crossing Chunk Borders | Duplicate:inward:MC-191436:When walking through chunks, cause lag spikes. | Duplicate:inward:MC-197794:Lag Spikes | Duplicate:inward:MC-199123:Chunk lag | Duplicate:inward:MC-205013:Chunk border fps freeze | Duplicate:inward:MC-207183:Chunk borders cause severe lag upon crossing them. | Duplicate:inward:MC-213646:Noticable freeze frame when walking through one specific chunk border | Duplicate:inward:MC-214826:Frame drops when switching chunk | Duplicate:inward:MC-217171:Lag spikes when going to a new chunk on the positive X or Z axis. | Duplicate:inward:MC-217175:sometimes entering new chunks causes frames to plummet | Duplicate:inward:MC-220227:Lag spike when crossing 2 loaded chunks | Duplicate:inward:MC-222997:Chunk Lag-Spikes | Duplicate:inward:MC-224176:FPS drop on specific coordinates. | Duplicate:inward:MC-224935:crossing chunkborders near worldspawn and in proximity to worldspawn in its direction cause severe server lag spikes when using caves and cliffs data pack | Duplicate:inward:MC-233172:Big frame drops while entering random sets of chunks (1.17-optifine) | Duplicate:inward:MC-241711:Weird Swamp Lag Spike | Duplicate:inward:MC-243095:Freeze lag for certain chunk | Duplicate:inward:MC-247637:Chunk Lag Spike | Duplicate:inward:MC-250587:Lag spike when entering in some chunks | Duplicate:inward:MC-251184:Versions above 1.8 stutter even with high FPS | Duplicate:inward:MC-251275:Huge frame rate drop after going from chunk to another chunk (it doesn't happen in all the chunks) | Duplicate:inward:MC-252805:lag peak | Duplicate:inward:MC-254750:Lag spike when entering some chunks | Duplicate:inward:MC-255037:i get extreme lag spikes when crossing chunk borders (1.19 java) | Duplicate:inward:MC-256397:FPS Drops entering certain chunks | Duplicate:inward:MC-261759:Lag spike when entering a new chunk | Duplicate:inward:MC-262423:Massive lagspike when crossing chunk borders | Relates:outward:MC-158672:Entering certain chunks causes FPS drops | Relates:inward:MC-188295:Placing fallling blocks using /setblock can cause a client-side lag spike in some circumstances

## Description

The bug
I've encountered some sort of lag spike which I narrowed down to be a floating structure. This structure can be a single block.
The lag spike seems to occur when I'm moving into the spawn chunks while an elevated block is placed on the opposite side of the spawn chunks. It occurs when the block is at Y96 or higher.
To replicate what I did on a 1.14.4 vanilla server:
- Create a default world with seed: -4952361208952771886

- Place a block at x 143 y 63 z -371 and another block at x 144 y 63 z -371. This is the location to test for the lag.

- Place a block at x 307 y 96 z -302. This will be the block to create the lag.

- Set the spawn point to x 227 y 66 z -376

- Walk back and forth over the two blocks you placed earlier.

- If you see a stutter, feel free to remove the block at x 307 y 96 z -302 and check again. Lag will be gone.

I cannot attach the video as the file size is slightly too large but you may watch it here: https://youtu.be/jmtq3jcXujo
I should note that it is not specific to my PC. It occurs on other clients on other devices.
Render distance will affect where the lagspike occurs in vanilla singleplayer, but is relative to the view-distance on servers. I believe it's distance + 1 in chunks, or there abouts.
Code analysis
Code analysis and further explanation by  can be found in this comment. There also exists a Fabric mod that fixes this issue: comment.

## Comments (100)

### Comment 1: migrated (2019-09-29T10:31:08.934-0700)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: migrated (2019-09-30T06:08:00.432-0700)

I have found another lag spot caused by the same floating block which prompted some further investigation.
I have discovered that if you place a block at Y96 or higher within the inner spawn chunks and then travel 11 chunks away (not including the chunk the block is in) and then cross between the 11th and 10th chunk, there will be a brief lag spike. This lag spike is worsened depending on how many blocks are in the sky it seems.
I haven't tested placing the block in the outer spawn chunks. I can say that my creeper farm in my real world does cause lag which is in the outer spawn chunks but I haven't counted how many chunks away that is. I think it's 13 chunks away as opposed to 11 like with a block within the inner spawn chunks but I haven't checked to be sure.
It does not occur if the block is placed outside of the spawn chunks.
I'm not sure why it's Y96 as the starting point - perhaps it varies on biome I'm not sure.

### Comment 3: [Mod] violine1101 (2019-09-30T09:26:39.698-0700)

Hmm, I can reproduce this in singleplayer with render distance 12, no matter whether the block is placed or not. That chunk border seems to cause lag in general. I tested it in 19w39a as well, so it can't be MC-158672.
I believe this might have something to do with light calculations across chunk borders, but I'm not too sure.

### Comment 4: migrated (2019-09-30T10:12:36.226-0700)

That may be a different issue to be honest as the lag caused by a block above Y96 will happen when render distance is set to 2 (meaning, the block isn't even close to being rendered in), and under the exact same conditions in single player it doesn't lag. In your case, it may be lighting but for me it seems to be something else.
The chunk borders are optional. The lag occurs when they aren't visible. I enabled them for the video just so we are aware that the lag occurs when crossing the chunk.

### Comment 5: migrated (2019-10-01T09:33:55.221-0700)

Can confirm that the lag occurs in vanilla 19w39a but one chunk further away than in realms (this matches up with paper, spigot and other non-vanilla servers) which is odd but no problem. For me using the server snapshot I had to move between the 12 and 11th chunk away from the placed block as opposed to 11 and 10 like on realms. Again, lag still persists without the chunk borders visible and no longer lags when the block is removed.

### Comment 6: migrated (2019-11-21T19:22:45.189-0800)

Still a problem in 1.15 Pre 1

### Comment 7: migrated (2019-12-17T13:28:28.913-0800)

This is still an issue in 1.15.1 and definitely does happen in single player too (I only play single player).

### Comment 8: migrated (2019-12-22T07:55:11.323-0800)

Can also confirm this happens in 1.15.1.

### Comment 9: migrated (2019-12-23T11:03:16.832-0800)

Can confirm this happens on my multiplayer server (for all players on the server too) on 1.14.4

### Comment 10: SPGoding (2019-12-23T11:06:57.042-0800)

As showed in my duplicate (MC-168419), this issue seems to be related to the Render Distance, the spawn chunk, the chunk player's in, and light update.

### Comment 11: migrated (2019-12-23T12:09:36.634-0800)

I disagree. I haven't tested this bug in the latest update but in 1.14...
- Render distance didn't affect the lag spike and even occurred on the lowest render distance.

- It's not the lighting as it's a block placed 150 or so blocks away in the sky, and isn't even rendered in when the render distance is low.

- It is however related to the spawn chunks. It occurs when the block is placed within the spawn chunks and the player moves between certain chunks. On realms, the lag will occur when crossing the 10th and 11th chunk away from the placed block. When hosting your own server, the lag occurs between the 12th and 11th chunk away from the placed block. This inconsistency also proves that it isn't the render distance or lighting because you would expect both instances to have the same lighting.

- Because it only occurs when the block is placed in the spawn chunks, that also eliminates lighting and render distance.

### Comment 12: SPGoding (2019-12-23T15:08:02.313-0800)

I hope you could see the table and the game log file in my duplicate (MC-168419) first.

### Comment 13: migrated (2019-12-24T07:16:29.050-0800)

I took a look at your bug report and was able to confirm that the lag spikes were being reported as light updates, and the chunks that lagged would differ depending on render distance.
I went to my world and did some further testing to see if I could find similarities. My lag spikes aren't anywhere near as bad which resulted in slightly different logs (There were not many light updates in the logs) but I'll get to that later.
I previously reported that single player didn't experience the lag I was experiencing in multiplayer. This stands true, but also false. I was able to find chunks that lagged but they were in a very different place than in multiplayer. Odd, right?
I'm able to confirm that in the following conditions, there is a lag spike in single player between chunks 15, -19 into 16, -19: render distance set to 2, a block placed in chunk 19, 6, -19 (Lower chunks do not seem to cause lag), world spawn set to chunk 14, 4, -24. Those chunks no longer lag when the render distance is raised. Occasionally, root.gameRenderer.level.light_updates will be reported in the logs but not very often.
I tested the chunks above in multiplayer and I can confirm that the lag is very minimal. It doesn't even show up in the logs but it is present. I also tested the chunks in your world in multiplayer and the same result applied - minimal lag if any at all. There is however a lag spike in my world from chunk 7, -24 into 8, -24. In realms, the chunks will be 8, -24 into 9, -24. These chunks do not lag in single player, and are NOT affected by render distance. Again, root.gameRenderer.level.light_updates does occasionally show up but not very often.
Why are my lag spikes not as bad as in your world? I cannot confirm my assumption, but I think it's because I'm testing with one floating block as opposed to many. The block placed in the sky for me doesn't lag if placed lower BUT in your world you have created a crater. Perhaps there's a lower chunk that also causes issues? I'm not sure.
Conclusion
The chunks where lag spikes are present are different depending on if it's a multiplayer server or single player. Render distance affects single player lag spikes but not multiplayer. It seems to be related to light updates due to the occasional appearance of such in my logs and the constant appearance of such in your logs. I'm not sure why the situation differs entirely depending on whether or not it's single player. Perhaps servers take over some of the load, not sure.

### Comment 14: migrated (2020-01-06T15:36:22.147-0800)

Happens REALLY often on my 1.15.1 Amplified server

### Comment 15: migrated (2020-01-08T04:56:58.527-0800)

For me, it doesn't happen in singleplayer but it is an issue in 1.15.1 on multiplayer

### Comment 16: migrated (2020-01-13T23:43:43.985-0800)

The problem continues in 1.15.1, I leave this video and download my world so I can analyze it completely.

https://www.youtube.com/watch?v=3kQnqypozKE
I left a poster and the character at the right time to reproduce the error.
 map download: https://www.mediafire.com/file/urm7entml9xerrx/Survival-1.15.1.rar/file

### Comment 17: migrated (2020-02-06T09:05:17.034-0800)

Still happens to every chunk, in 1.15.2 and the newest 20w06a snapshot, both singleplayer and multiplayer. The fps drops don't occur in 1.12.2 and versions below.

### Comment 18: migrated (2020-03-24T02:15:38.160-0700)

I've also encountered this issue. I was able to confirm that removing a sky building resolves the issue.  The lag spike happens when crossing the chunk border that results in loading the chunk with the sky building. y=96 does seem to be roughly where the issue begins. But I did not find it was relate to whether the block was "floating" or not.
I was also unable to reproduce the issue when opening the same world in singleplayer, even when using the "open to LAN" option.

Edit: Playing on 20w12a

### Comment 19: migrated (2020-03-30T10:15:29.563-0700)

Can confirm, on 1.15.2 server, we have 2 buildings that reach build limit. When crossing the chunk border where they are loaded there is a 1.5-2 second lag spike which happens for all players.

### Comment 20: Krimsar (2020-03-31T03:29:46.668-0700)

The lag spikes are very noticeable on the 10 Years of Minecraft map.
edit: Also, MC-175907 might be a duplicate of this?

### Comment 21: migrated (2020-04-04T18:12:40.952-0700)

I've also encountered this issue on a 1.15.2 server. The lag spikes are definitely noticeable and interfere greatly with combat, especially on low-end machines.

### Comment 22: migrated (2020-04-04T18:44:08.717-0700)

Still having this issue on 1.14.4 server (the issue is present even if I update to 1.15.2)

Proof: https://i.gyazo.com/12fc1f66914a2651aaa8811040255267.mp4

### Comment 23: migrated (2020-04-17T15:50:33.015-0700)

I have the same bug on one of my maps on a Vanilla / Spigot / Paper and Bukkit server in 1.14.4 and 1.15.1 and 1.15.2 with optifine or not and this for all players with and without plugins:
 Proof:

### Comment 24: migrated (2020-04-22T09:56:41.324-0700)

I and my server members having been having this issue between the last two snapshots. 20w16a and 20w17a.
It is causing severe lag when going between chunks, and seemingly when the chunks have redstone between them. It is not making it enjoyable

### Comment 25: migrated (2020-04-23T10:36:47.697-0700)

Can reproduce in 20w17a.
It's very bad in amplified worlds.

### Comment 26: migrated (2020-05-04T10:44:24.515-0700)

This bug is happening to me as well, using both the vanilla client and OptiFine, and using vanilla server software and Paper. This only happens when another player is in a "bad" chunk as I show in this video:
https://youtu.be/4KWEhn3y-rw

Also, it doesn't appear to be strictly an FPS or render issue, as other players actually see the stuttering player rubber band. Watch my friend rubberband going back and forth through a chunk border in this video:
https://youtu.be/3-rpttcUIm4

We reduced the RAM allocated to the server and that didn't fix it.

Happens on 1.15.2 vanilla and Paper as well, it's been present since at least 1.14.4.

This is, as LiquidDev put it, EXTREMELY bad in Amplified worlds.

### Comment 27: migrated (2020-05-04T11:14:09.631-0700)

I just re-tested this with someone else on a vanilla server, default world type. No stutter. We then pillared up with dirt blocks above y=96 and flew between chunk borders, and there was noticeable stutter. Very easy to reproduce.

### Comment 28: migrated (2020-05-05T14:21:43.524-0700)

I'm experiencing this on my amplified 20w18 world. It's quite severe and seems to happen every 4 or 5 chunks or so.

### Comment 29: migrated (2020-05-07T08:56:39.383-0700)

I'm also experiencing this on PaperSpigot-259 on 1.15.2 on an amplified world, but below the 96 y elevation

### Comment 30: migrated (2020-05-07T13:55:53.513-0700)

I also have this issue on 1.15.2 Paperspigot on a regularly generated world crossing several chunk boarders drops frames massively. It doesn't matter the elevation or y level it happens everywhere.

### Comment 31: migrated (2020-05-11T10:30:48.170-0700)

Also have this issue. Seems to happen with any block placed above y=96.
Found a reddit article about it from 1.14.4 that goes into great detail.
https://www.reddit.com/r/admincraft/comments/cog8wf/trying_to_eliminate_massive_fps_lag_spike_that/

### Comment 32: PhiPro (2020-05-12T06:32:18.830-0700)

Took me quite a while to fit all the puzzle pieces together, but I finally have a satisfying explanation for this bug with all its weird features.
Basically, it is caused by MC-170010 and my proposed fix for it will fix this issue as well.
Let me first explain what is causing the lagspikes. It is basically the same lagspike as experienced in the following issue:
- Create a new redstone-ready world

- /setblock 7 103 7 minecraft:glass

- Experience a clientside lagspike

This lagspike occurs whenever a block is placed high above the ground, where "ground" really means the topmost block of all neighbor chunks. As soon as there is only a single block above, the lag spike disappears. For example, if you /setblock 7 255 7 minecraft:glass then the above steps won't cause any lagspike.
The reason for this is MC-170010. As mentioned there, topmost skylight maps are not properly initialized to their previous values. Instead, they are created completely dark and then get relighted. Placing a block high above ground creates 27 new lightmaps. Due to the order of creating them bottom to top, all of them will be uninitialized and have to be relighted. So, although we place a glass block, which doesn't cause any light change at all, the client has to relight 27 subchunks at once due to this bug, which takes quite some time.
As soon as there is any block above, no (or fewer) lightmaps get created, hence avoiding the issue.
So, my proposed fix for this issue is my proposed fix for MC-170010.

While not really relevant for the solution, I think it is still interesting to explain why the bug doesn't occur in many situations and why it is related to spawnchunks and is also stateful. So, let's start by explaining how the previous lag spike relates to the one of this bug report.
The following easy setup is sufficient for triggering it:
- Create a new redstone-ready world

- Set the render distance to 2 (or 3)

- /setblock 7 103 7 minecraft:glass

- Move exactly 4 chunks in any cardinal direction, e.g. move to chunk (4 0)

- Move 1 chunk back, e.g. to (3 0), and experience a lag spike

When you move back from (4 0) to (3 0), the chunk (0 0) gets loaded on the client. This causes the lightmaps to be created around subchunk (0 6 0) and hence leads to the exact same issue as previously described. Namely, those lightmaps are created uninitialized and have to be relighted all at once, which costs too much time. (Actually, in this case not all of the 27 lightmaps are directly initialized, but only those in the already loaded chunks. Nevertheless, this seems to be enough to lag the client quite bad.)
Why does it happen only for certain chunk borders and not all of the time?
First of all, the issue relies on lightmaps being created upon loading chunks on the client. The lightmaps created for the newly loaded chunk are in fact initialized, namely to the data the client receives from the server. So those don't contribute. (Actually, the topmost lightmap of the newly loaded chunk is still thrown away and relighted in any case. But this single lightmap seems to have sufficiently small impact to not cause lag spikes all of the time. Nevertheless, this unnecessary relighting would be eliminated with my proposed solution as well.) So, a necessary condition for the issue is that the newly loaded chunk is much higher than its already loaded neighbors.
Nevertheless, even in this case, there are still a lot of awkward situations that avoid the bug:
- The bug doesn't occur if you move e.g. to (5 0) and then to (3 0)

- or if you reload the world at (4 0).

- Also, if you replace the block by air and then by glass again in the above steps, the issue doesn't occur either.

- If you move the spawnchunks far away from (0 0) the issue doesn't occur.

These strange stateful features of the bug were really giving me some headaches while hunting it down  The block isn't loaded on the client while at (4 0), so replacing it by air and then glass again shouldn't have any effect on the client state, yet it turns out that it avoids the lag spike.
The easiest case is what happens if you reload the world at (4 0). In this case, when the server sends the data for chunk (1 0), it also sends the lightmaps for (1 5 0), (1 6 0) and (1 7 0). Similarly for (1 -1) and (1 1). Those lightmaps are not directly added to the world, since there is no nearby block yet. Instead they are kept queued. Once we move to (3 0), the block at (0 6 0) creates all the surrounding lightmaps. Now, in this case, the lightmaps for (1 -1), (1 0) and (1 1) are not uninitialized, but are initialized from the queued up data that the client received from the server. That is why the bug does not occur in this case.
If we now move back to (4 0), the block at (0 6 0) and hence all the surrounding lightmaps get unloaded. Now, the neighbor chunks do not anymore have any queued up data from the server, and the server won't resend the data unless we move even further away to (5 0). So, when now crossing the chunk border to (3 0) once again, the lightmaps for chunk (1 -1), (1 0) and (1 1) will now indeed be uninitialized and have to be relighted, causing the lagspike.
What happens if you replace the block by air and then glass again while at (4 0)?
When replacing the block by air, the server deletes all the lightmaps. When afterwards spawning the glass block again, the server encounters exactly the same issue of MC-170010 and has to relight the uninitialized lightmaps. This will be detected as ligth changes, although the final light values actually haven't changed. Now, some other piece of code comes into play.
net.minecraft.server.world.ChunkHolder.java

```public void flushUpdates(WorldChunk worldChunk) {
    if (this.blockUpdateCount != 0 || this.skyLightUpdateBits != 0 || this.blockLightUpdateBits != 0) {
         ...
         if (this.skyLightUpdateBits != 0 || this.blockLightUpdateBits != 0) {
            this.sendPacketToPlayersWatching(new LightUpdateS2CPacket(worldChunk.getPos(), this.lightingProvider, this.skyLightUpdateBits & ~this.lightSentWithBlocksBits, this.blockLightUpdateBits & ~this.lightSentWithBlocksBits), true);```
What it does is to sync all light updates at the edge of the client's view area. Hence, the (wrongly) detected light updates cause the server to sync the lightmaps for (1 -1), (1 0), (1 1) to the client again, which basically puts us in the same starting point as in the previous case. Those synced lightmaps are used for initialization and hence the issue doesn't occur.
Finally, let us understand the role of spawn chunks. As it turns out, this is due to yet another effect, namely that the chunk tracking distance is 1 larger than the chunk loading distance. Concretely, this means the following:
- The chunk at (0 0) is unloaded from the client upon entering chunk (4 0) (the chunk tracking distance is capped at >= 3)

- Since the chunk loading distance by players is basically one less, i.e. 2, the chunk at (1 0) is already "unloaded" serverside at that time, but still loaded clientside. "Unloaded" means that it is demoted to a border chunk, so it is still loaded in some sense, but it is non-ticking and won't be sent to clients; however, it will be kept loaded on the client if already present.

- When moving to (3 0) the chunk at (1 0) becomes "loaded" again on the server, i.e. it is promoted to a ticking chunk.

- At this point, it will be resent to the client.

- The chunk at (0 0) will only be sent to the client upon moving to (2 0).

- However, as before, the client now has queued light maps, so the lag spike does not occur.

So the difference between spawn chunks and non-spawn chunks is that they are kept loaded on the server and hence shade this discrepancy between tracking and loading distance. This also means that the same rules apply to chunks loaded by any other means, e.g. other players.
Further remarks
As another suggestion, it might be useful to run the client lighting engine offthread as well, as is already done for the server. Of course, you want some way for the client thread to wait for light updates to finish before rendering, as even the slightest latency of light updates near the player usually feels very annoying. Such a way to wait for light updates to finish is needed anyway for MC-164281. Additionally, you probably also want to implement a fix for  such that updates near the player can be prioritized and the client thread only has to wait for those, rather than all pending updates. Nevertheless, even without a fix for , putting the clientside lighting engine offthread can help mitigating this issue further.
As a final remark, I really strongly recommend to implement my proposed solution for MC-170010 instead of putting more and more band-aid on it, as it makes it increasingly difficult to track down issues. This one already gave me a lot of headaches as it had so many strange fatures related to different code paths. (Admittedly, the challenge was also kindof fun )
Workaround for players
As a temporary workaround for player, you can place a ceiling of minecraft:barrier at y=255 above the whole map. As can be seen from the analysis, the issue arises from a height difference of neighbor chunks. Putting a ceiling above the world eliminates any height difference and reduces the issue to its minimal intensity of flat worlds. Putting the ceiling only above a small part of the world will simply push out the problematic chunk boundaries to the end of the ceiling, so for this workaround to work you need to cover all of the area you visit. While this is definitely not perfect, it should at least help in the case when you are moving in already generated chunks and not visiting new ones.

Best,
PhiPro

### Comment 33: migrated (2020-05-12T13:58:55.615-0700)

@PhiPro
This is a very good synopsis of the issue. I tested out your workaround, and I can confirm that it works exactly as written. Good work!

### Comment 34: PhiPro (2020-05-20T16:29:19.425-0700)

As a proof of concept and as a temporary workaround for players, I have implemented my proposed solution for MC-170010 as a fabric mod. As explained above, this also solves this performance issue. The code can be found at https://github.com/PhiPro95/mc-fixes/tree/mc-170010. Note that this requires the fabric mod loader.
Edit: Due to MC-196614 you also require https://github.com/PhiPro95/mc-fixes/tree/mc-196725 in order to avoid amplified versions of that bug.
A complete bundle of all required mods can be downloaded here
Also note that it is important to have this mod installed on the client in order to fix the lag spikes. (However, in order to fix MC-170010 itself, it is mainly important to have it installed on the server).

Best,
PhiPro

### Comment 35: migrated (2020-05-21T06:59:00.097-0700)

A lot of progress has definitely been made regarding this bug. It was a very confusing issue to begin with but with the help of many, we've reached a better understanding. Hopefully this all leads to an official fix. Amazing work.

### Comment 36: migrated (2020-06-05T01:56:13.826-0700)

It still happens in 1.16 Pre-release 1

### Comment 37: migrated (2020-06-06T01:35:36.063-0700)

Happens on 1.16 pre-release 2
This one makes capturing video of Minecraft impossible with my setup. Many missed frames when crossing chunks.

### Comment 38: migrated (2020-06-10T15:10:17.412-0700)

Can you reproduce this bug in 1.16 pre release 3?

### Comment 39: migrated (2020-06-11T18:25:35.815-0700)

Happens on 1.16 pre-release 4

### Comment 40: migrated (2020-06-12T22:05:04.434-0700)

confirmed for 1.16 pre-5

### Comment 41: migrated (2020-06-17T11:51:54.073-0700)

confirmed for 1.16 pre-8

### Comment 42: migrated (2020-06-18T11:27:18.638-0700)

confirmed for 1.16 rc-1

### Comment 43: migrated (2020-06-21T15:12:28.164-0700)

Also getting this bug as of 1.16 rc-1, so far I've only noticed this in the over-world. Not encountering it within the Nether on my end.

### Comment 44: migrated (2020-06-29T11:38:56.964-0700)

I've been having this issue as well, using a Nether portal or crossing some chunks in particular results in a full server crash with a StackOverflowError exception, wondering if it's related to MC-191659 at all?

### Comment 45: migrated (2020-06-30T16:34:30.503-0700)

same problem in 1.16.1

### Comment 46: migrated (2020-07-01T17:15:01.457-0700)

I have this problem on an smp server all around my base in random chunks, I keep on getting huge lag spikes when I cross certain borders, it only happens at my area no one else gets this problem... when I go to y 255 and set my render distance to 2 , all the lag disappears and lag spikes are no longer existent.. does anyone have a fix to this..?

### Comment 47: migrated (2020-07-01T17:17:45.684-0700)

Im so disappointed that a massive bug like this that people have been experiencing since 1.14 is still not resolved...

### Comment 48: migrated (2020-07-02T08:22:50.024-0700)

can confirm for 20w27a

### Comment 49: migrated (2020-07-05T09:13:36.074-0700)

i know that s not cool for the moderator or / dev but this bug is killing exploration and immersion

### Comment 50: migrated (2020-07-07T19:44:31.501-0700)

FYI This is patched (worked around) in Paper 1.15+ (https://papermc.io for those unaware).
The bug lies in the client, but we sent extra light data to the client to avoid this issue.
https://github.com/PaperMC/Paper/blob/b6925c36afa7565cac8f9fe9d3432fe658ca1f77/Spigot-Server-Patches/0496-Workaround-for-Client-Lag-Spikes-MC-162253.patch

### Comment 51: migrated (2020-07-08T03:38:31.760-0700)

im using paper in 1.16.1 and i still have the isue maybe i have to enable something but for me i still have severe lag

### Comment 52: migrated (2020-07-08T07:50:33.552-0700)

Pardiac, Paper definitely fixes the bug, are you sure it's not just a low spec PC or another issue? You shouldn't need to change any settings in paper.yml.

When Paper patched the bug in 1.15.2 and my server updated to the version the patch was introduced in, the chunk stutter was greatly reduced (500+ms down to maybe 20ms) for every single person on my server.

Obviously Mojang needs to still fix this on their end because switching from Paper to any other type of server software (Spigot, Forge, Fabric, or Vanilla) makes my server completely unplayable for all 20 people who play on it.

### Comment 53: migrated (2020-07-08T13:01:41.201-0700)

Happens on 20w28a

### Comment 54: migrated (2020-07-28T18:11:37.511-0700)

So severe on my server, almost makes it unplayable
Tried Paper 1.16.1 and that did not work sadly. (Specs of our computers are really good so that is not an issue.)
Also tried Phil's mods but that sadly did not work either.

### Comment 55: PhiPro (2020-07-28T23:25:41.870-0700)

@ You are experiencing some different issue in this case. Note that the lighting issue discussed here is not the only bug that can cause lag spikes when crossing chunk borders, but it seems to be a very common reason.
One other issue I know of is MC-65587. I dont know of a good workaround for that, though, other than removing all player skulls and see if that helps (after creating a backup of the world).

### Comment 56: migrated (2020-07-28T23:53:18.980-0700)

@Philipp Provenzano, I gotcha! I did not realize there were multiple causes, that makes sense.
I do really hope that Mojang can figure this out as this is a rather severe bug.

### Comment 57: migrated (2020-07-31T13:22:14.500-0700)

And how could I solve it momentarily in singleplayer?

### Comment 58: PhiPro (2020-08-03T14:03:02.865-0700)

Info to everyone using my mod as temporary workaround: There is a (vanilla) bug, see MC-196614, that caused basically all underground subchunks to become fully bright up to and including version mc-170010-v1.2.1. This issue is solved in https://github.com/PhiPro95/mc-fixes/tree/mc-196725.
A complete bundle of all required mods, including the fix for this issue, can be found here.
In order to repair already affected chunks you need to erase cached data, see  for further instructions.
Sorry for the inconvenience.
Best,
PhiPro

### Comment 59: migrated (2020-08-03T14:49:26.228-0700)

@Philipp Provenzano
Hey there, I'm not sure if you are aware if this already, but JellySquid's Phosphor mod in conjunction with your temporary workaround crashes the game with each other when trying to load into singleplayer or multiplayer. Possibly because both mods change the lighting engine if I had to take a guess. Just wanted to let you know.

### Comment 60: PhiPro (2020-08-03T15:03:43.743-0700)

@ Yes, I am aware of this. I need to get in contact with her and see what we can work out.
On another note, please post any issues regarding my bugfix mod on the Github bugtracker, if possible, in order to keep the discussion here on-topic.

### Comment 61: migrated (2020-08-24T16:19:49.216-0700)

@Philipp Provenzano I'm fairly new to messing with minecraft, and trying to fix bugs, but this bug has been affecting me badly. Was just wanting to know how to install this fix. I downloaded the jar file, but it wont open when I open with java. So could you tell me where to put the zip folder instead? thanks

### Comment 62: RedCMD (2020-08-24T22:16:00.210-0700)

@5amm https://bugs.mojang.com/browse/MC-162253?focusedCommentId=702303&page=com.atlassian.jira.plugin.system.issuetabpanels%3Acomment-tabpanel#comment-702303

### Comment 63: _BOBE (2020-09-08T12:02:26.705-0700)

I have this same issue but in many different spots.
Here is a video I made on it earlier this year. (Also more info in comments)
https://youtu.be/vrP_DMBWLKo

### Comment 64: Ray (2020-10-22T09:01:08.616-0700)

Still in 1.16.4 pre 1

### Comment 65: migrated (2020-10-27T22:33:30.801-0700)

@Philipp Provenzano
Hi Philipp. I just wanted to thank you for digging so thoroughly into this issue. It may have been a fun challenge for you, but it was a huge sigh of relief for me.
I only recently discovered Amplified world mode, and I fell in love with it immediately. However these lag spikes continued to drive me crazy. They seemed random at first. After noticing some patterns I did some searching and ended up here. Your workaround mod package seems to have eliminated my lag spikes, which made the game almost unplayable in this mode.
I really hope that the functionality oversights that cause this light-loading behaviour can soon be addressed in the base game, since I believe the amplified mode is one of the most interesting world types put out by Mojang.

FYI spikes were all happening in single player mode.
Edit: typos.

Regards,
Cale

### Comment 66: migrated (2020-11-04T05:57:16.443-0800)

i still experiencing chunk border lag crossing with 1.16.4 but 1.12.2 was the last running smoothly as like 1.8.9 for chunk border crossing. later i tested all versions from 1.13 to latest 1.16.4 and i can confirm it and i still suspect the bug.  what's going on with those updates it getting worst. please mojang don't update the minecraft java edition too fast because its been 2+ years since 1.13 release. the bug still not resolved i recommend to find bugs and fix to solve it completely before we going to 1.17
i apology for my english

### Comment 67: migrated (2020-11-04T14:07:08.374-0800)

Affects 20w45a

### Comment 68: migrated (2020-11-04T19:00:10.847-0800)

still present with 20w45a much worst performance

### Comment 69: migrated (2020-11-05T05:54:14.711-0800)

For those with the issue still, have you tried setting "sync-chunk-updates" to "false" in your server.properties? I think this fairly new setting (which is flipped to true in most cases by default) may be a culprit, as it was a cause in other similar slowness/lag issues. That being said, I tried this fix but it did not work until I loaded in the Paper mod which apparently has a fix for the unpatched lag/slowness, so the workaround might be a combination of two fixes.

### Comment 70: migrated (2020-12-11T14:37:35.971-0800)

This was reported for 1.14.4. and the issue is still there for 1.16.4! When can we expect a fix?

### Comment 71: migrated (2020-12-13T00:00:57.283-0800)

Yes, I have this issue in 1.16.4 as well. Definitely confirmed!

### Comment 72: migrated (2020-12-20T20:44:53.056-0800)

Just came across this issue also in 1.16.4. Only happens when crossing certain chunk borders but can be replicated almost every time for these certain chunks.

### Comment 73: migrated (2020-12-23T21:18:15.864-0800)

Same issue for me as well, however I haven't found (haven't searched for) the culprit block. I have a line on x coords which when I pass, it gives a huge lag spike.
1.6.4
edit: I've found the source for me, I hope it helps for some of you:
I have the "More Mob Heads" Vanilla Tweaks datapack added. Over the years I moved the map to a server, then to single player, then back to server, long story short, some mob heads are not displayed and I cannot fix it. I narrowed the lag source to one chunk, then I found that it was a tabby cat head, which wasn't displayed properly (Steve head instead)

### Comment 74: migrated (2021-01-13T13:20:59.681-0800)

Really hope this is fixed soon, it happens in multiple important places on my server and is very disruptive to me and players productivity

### Comment 75: migrated (2021-02-03T02:56:53.339-0800)

Also experiencing this. Please fix asap mojang. Its a game breaking experience for so many players.

### Comment 76: migrated (2021-02-03T11:24:24.582-0800)

I've been having this same issue in my server for a long time. The "lag wall" as I used to call it before realizing it was a lag zone was being caused by heads of very old players that do not exist anymore. This might be related to MC-65587.

### Comment 77: migrated (2021-02-03T16:26:17.702-0800)

I could not recreate this bug following your steps but I came across this in my own world and it affects an entire line of chunk borders (So a single line of chunk borders going from the west world border to the east). But the weird thing is that it only happens when my render distance is at 10 chunks. My ticket for extra information: MC-213646

### Comment 78: migrated (2021-02-05T04:30:29.151-0800)

I experienced the same thing I think. I discussed my issue in this reddit post. https://www.reddit.com/r/MinecraftHelp/comments/lcljv7/server_side_lag_chunkbordersjava1165/

### Comment 79: migrated (2021-02-08T16:11:42.158-0800)

I have the same issue:
https://www.youtube.com/watch?v=E3PS5VTJ25E&ab_channel=LukeOnTheYoutubes

Have noticed that this issue does not occur when I am the only person on the server?

Version 1.16.5, Spigot minecraft server

### Comment 80: Muchmu (2021-02-18T08:51:41.602-0800)

I have this kind of lag chunk border on my server and it seems to go on to the world border, I also have thousands in one of my single player worlds ( one on nearly every chunk ) it's driving me insane. Hope it gets resolved soon.

### Comment 81: migrated (2021-03-03T06:06:52.966-0800)

I also encounter this bug at my single player world in 1.16.4.

### Comment 82: migrated (2021-03-09T12:39:45.209-0800)

Been having the same bug consistently on multiple chunks on my 1.16.4 vanilla server.

### Comment 83: migrated (2021-03-28T07:18:34.508-0700)

I can also confirm this. On our Server it's so bad that in the main area of our village you cannot play as when moving between chunk borders the whole server stutters for a moment and players experience rubber-banding.
I've tried several workarounds already but none of them did actually work.
- Placed barrier block ceiling above area causing problems at y:255

- Removed all player heads

- Removed buildings from spawn chunk

- Used "Light Cleaner" plugin to relight chunks after world edit usage

- Used --forceUpgrade --eraseCache startup flags on server startup

Interestingly enough the stuttering starts 9 Chunks away from spawn and ends 16 chunks away from spawn.
So moving towards spawn causes massive stuttering and rubber-banding, moving away from spawn does not.
Here's a quick video I recorded that shows the issue:
https://www.youtube.com/watch?v=_YwphT9EXEM
I really hope this will get fixed as soon as possible as this is a known bug since Minecraft 1.14

### Comment 84: migrated (2021-03-29T07:40:55.628-0700)

Created an account to say this: It appears to be about loading some chunk far away, because 1) it only goes for movement in one direction, and 2) you can move which border will be the laggy one, by changing the render distance.

### Comment 85: migrated (2021-04-09T14:07:47.365-0700)

On Vanilla Servers, the command */setworldspawn* can avoid a lag spike at entering the position where the lag spike is occurring.

### Comment 86: migrated (2021-04-12T01:35:00.908-0700)

Still waiting for a fix since 2019, there are enough solutions by the community which are working.

### Comment 87: slicedlime (2021-04-12T05:08:48.916-0700)

Please do not spam the bug tracker. Only post comments if you have new information to add.

### Comment 88: migrated (2021-04-14T20:43:29.331-0700)

1.16.5 still present with the bug also the latest snapshot 21W15A

### Comment 89: migrated (2021-04-24T21:25:11.803-0700)

Present on latest snapshot, 21w16a. On a server hosted by Shockbyte, all players lag and ping goes up to 512ms with every chunk crossing.

### Comment 90: migrated (2021-04-24T21:29:24.876-0700)

UPDATE! It only seems to affect multiplayer in a very strange way. I found out that if one person enters a chunk, everyone will lag, but everyone else can then enter the chunk no problem. It only seems to lag if you enter any chunk WITHOUT a player in it. Enter any chunk WITH a player in it will not lag.

### Comment 91: migrated (2021-04-27T05:36:04.708-0700)

This is not directly related to floating blocks, but I do think that some of the people commenting here who are experiencing the same symptoms with the snapshot datapack are actually being affected by error log spam.

@kristiani posted about the "Received invalid biome id: -1" error causing lag spikes when crossing chunk borders in the 21w16a snapshot with the data pack enabled. It seemed to be directly connected to what others here are experiencing, and was quite insightful, so I'm sharing it below here in the hopes it will help.

After testing this issue in several scenarios, can confirm in 21w16a. However it is rather inconsistent as @Willber mentioned...

Some points worth mentioning:

- I can say for sure in all scenarios the log line is being written... "Received invalid biome id: -1"
- However, having said that ... there are times when some kind of binary data is written to the latest.log, this causes a "lockup" of sorts, then subsequent attempts to write to the file appear to fail – i.e. the log file stops growing in size BUT the "Minecraft game output" GUI console ... continues to show logs for "Received invalid biome id: -1".

- At this stage ...  the world appears fine ... no lag, no freeze, (probably because no more logs being written)

- When you do get the lag/freeze ... that's when the log keeps getting written... keeps growing... likely Disk IO causing the lag/freeze.

- This only happens when crossing chunk boundaries... moving up and down in a chunk causes no lag/freeze issues as no chunks are being (un)loaded, no logs being written.

- For the same worlds  that are freezing.... (as @Frostrix mentioned) far away from spawn (for example @ 10000 ~ 10000), no logs, and no freezing...
- But again ... having said this, if you look carefully when at these distances, the log file grows for a short time... then seems to reach the "lockup" moment mentioned before (log file stops growing) ... which means you don't experience lag anymore.

- Now this is where the FUN part comes in .... If I /tp back to spawn.... and the log file comes out of it's "lockup" and starts writing to disk ... causing the lag/freezing in game to start up again !?? very confusing.

Really hope this info helps the devs  - this problem is very bad for an SSD with so many writes, and makes the current datapack somewhat unusable

All tests done on varying seeds with no obvious pattern (except for the points above) as to when the log file "lockup" would happen and when it wouldn't.

@TelepathicGrunt also provided some information on why this error seems to be generated; it is in reference to dimension data packs, but I think that the issues may be related. Perhaps some of the cave biomes in the Caves and Cliffs datapack are behaving in a similar way to dimension biomes added in json datapacks.

From my testing and debugging, this appears to be specifically caused by the json biome having any structures added to it and the user loads up an already generated chunk with that biome. The instructions about exiting and re-entering the dimension is not needed. Just fly forward in the dimension for a few seconds, turn around, and fly back and the issue will present itself.
I was helping someone with their mod and they were using json biomes/json dimensions for their mod and they got this issue because their biome has structures in it. When I ran the debugger, their biome source was using the correct dynamic registry instance and was returning the correct biome instance. But within SChunkDataPacket class, it had the exact same dynamic registry so that was good. But the biome being returned from the chunk is a completely new biome instance that is not present in the dynamic registry at all. And that is what causes the massive lag spike as the game starts writing the error to the log like crazy. So as far as I can tell, the biome source is not the issue here. The chunk receives the correct biome as well as it doesn't error upon first generation. Rather, the issue seem to lie in how the chunk either saves the biome to memory or retrieves the biome from memory. But only when structures are present in the biome.
Very odd situation but hopefully this digging I did helps

@i509VCB added:

I've checked with someone who has such a case in a modded environment. Simply we loaded the world, then put a breakpoint on the Biome class' constructor and replicated it like telepathic grunt did above.

What I noticed looking through the debugger is that when structures are loaded, what yarn calls `RegistryOps` will attempt to load the biome from json and decode the biome. This occurs somewhere in the call site of `RegistryOps.of(...)`. This occurs in the constructor of `PoolStructurePiece` which occurs as a result of loading structure starts.

### Comment 92: migrated (2021-05-05T01:09:35.742-0700)

still present with 21w17a and my ms drastic increase 50-721

### Comment 93: migrated (2021-05-05T01:33:02.000-0700)

Still waiting on the 1.17+ release on the related bug that was mentioned by Snow (MC-197616) - showing it was fixed. As soon as it's out, I would test this issue again and see if it's resolved, it very much appears to be related (fingers crossed ).

### Comment 94: migrated (2021-05-22T10:45:33.065-0700)

Upgraded a copy of my world to 21w20a today and the lag when crossing certain chunks is still there

### Comment 95: migrated (2021-05-27T21:43:41.612-0700)

upgraded from 21w18a to 21w20a yeah still there

### Comment 96: migrated (2021-06-01T05:59:54.748-0700)

1.17-pre2 also has the chunk lag.
and i am pretty sure that we have this error until 1.18 or 1.19 because: 29/Sep/19 7:31 PM
this bug is so annoying wtf please pay attention to the community.
ITS UNPLAYABLE

### Comment 97: migrated (2021-06-01T09:41:04.216-0700)

Still affects 1.17-pre3

### Comment 98: migrated (2021-06-02T15:23:40.357-0700)

Still affects 1.17-pre4

### Comment 99: migrated (2021-06-03T07:28:59.599-0700)

This makes running a server incredibly hard. Sometimes freezes for 20s when crossing chunks...

### Comment 100: Technofied (2021-06-03T07:31:50.870-0700)

Can confirm with xEndeavour, on 1.16.5 and it seems to only be getting progressively worse, setting the max block height to barriers doesn't mitigate laggy chunks either.
