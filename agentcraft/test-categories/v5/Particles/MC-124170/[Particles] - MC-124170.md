# MC-124170: Performance issue with particles causing lag

**Mojira URL:** [https://bugs.mojang.com/browse/MC-124170](https://bugs.mojang.com/browse/MC-124170)

## Report details

- **Mojira categories:** Particles; Performance
- **Project:** MC
- **Issue key:** MC-124170
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2018-01-11T09:53:44.707-0800
- **Updated:** 2025-05-29T09:20:53.665-0700
- **Resolution date:** 2024-01-05T11:18:19.192-0800
- **Affects versions:** Minecraft 18w02a; Minecraft 18w03b; Minecraft 18w05a; Minecraft 18w06a; Minecraft 18w07b; Minecraft 18w07c; Minecraft 18w08a; Minecraft 18w08b; Minecraft 18w11a; Minecraft 18w14a; Minecraft 18w15a; Minecraft 18w16a; Minecraft 18w19a; Minecraft 18w19b; Minecraft 18w20a; Minecraft 18w20c; Minecraft 18w21a; Minecraft 18w21b; Minecraft 1.13-pre4; Minecraft 1.13-pre5; Minecraft 1.13-pre6; Minecraft 1.13-pre7; Minecraft 1.13-pre8; Minecraft 1.13-pre9; Minecraft 1.13-pre10; Minecraft 1.13; Minecraft 18w30b; Minecraft 18w31a; Minecraft 18w32a; Minecraft 18w33a; Minecraft 1.13.1-pre1; Minecraft 1.13.1-pre2; Minecraft 1.13.1; Minecraft 1.13.2-pre1; Minecraft 1.13.2-pre2; Minecraft 1.13.2; Minecraft 18w43b; Minecraft 18w43c; Minecraft 18w44a; Minecraft 18w45a; Minecraft 18w46a; Minecraft 18w47a; Minecraft 18w47b; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 19w02a; Minecraft 19w04b; Minecraft 19w05a; Minecraft 19w06a; Minecraft 19w07a; Minecraft 19w08b; Minecraft 19w09a; Minecraft 19w11a; Minecraft 19w11b; Minecraft 19w12a; Minecraft 19w12b; Minecraft 19w13a; Minecraft 19w13b; Minecraft 19w14a; Minecraft 19w14b; Minecraft 1.14 Pre-Release 1; Minecraft 1.14 Pre-Release 2; Minecraft 1.14 Pre-Release 3; Minecraft 1.14 Pre-Release 4; Minecraft 1.14 Pre-Release 5; Minecraft 1.14; Minecraft 1.14.1 Pre-Release 1; Minecraft 1.14.1 Pre-Release 2; Minecraft 1.14.1; Minecraft 1.14.2 Pre-Release 1; Minecraft 1.14.2 Pre-Release 2; Minecraft 1.14.2 Pre-Release 3; Minecraft 1.14.2; Minecraft 1.14.3 Pre-Release 1
- **Fix versions:** Minecraft 1.14.3 Pre-Release 2
- **Labels:** lag; particles
- **Watchers:** 2
- **Attachments:** 16
- **Attachment filenames:** 1.13 Particles.png; 2018-01-11_18.50.08.png; 2018-01-11_18.50.38.png; 2018-01-11_18.55.57.png; 2018-01-11_18.57.54.png; 2018-01-14_14.02.12.png; 2018-01-14_14.06.05.png; 2018-01-14_14.45.36.png; 2018-01-14_14.48.32.png; 2018-01-14_14.51.41.png; 2018-10-25_08.30.35.png; 2019-02-06_18.41.27.png; 2019-05-16_21.06.15.png; chrome_2018-10-20_17-13-58.png; javaw_2018-10-10_02-37-04.png; javaw_2018-10-24_08-08-34.png
- **Issue links:** Duplicate:inward:MC-123776:Blockcrack particles are very laggy | Duplicate:inward:MC-126294:Brutal FPS drop near bubble columns over ocean ravines | Duplicate:inward:MC-133867:1.13 TNT performs worse than 1.12.2 TNT | Duplicate:inward:MC-134425:Performance issue with Particles | Duplicate:inward:MC-134569:Falling particles cause lag | Duplicate:inward:MC-135529:Small amounts of TNT causing massive frame drops. | Duplicate:inward:MC-135991:TNT causes your FPS to drop low since 17w47b | Duplicate:inward:MC-136688:Fireworks Cause drops to 5 or less FPS | Duplicate:inward:MC-136691:The particles such as Rain splashes create so much lag in 1.13 | Duplicate:inward:MC-136805:Particles kill fps | Duplicate:inward:MC-137216:Lag with fireworks | Duplicate:inward:MC-137864:Fireworks with "trail" cause lag spikes | Duplicate:inward:MC-139117:TNT Particles Lag The Game | Duplicate:inward:MC-139279:Lag is created when a firework explodes.... | Duplicate:inward:MC-139551:Scaffoldings is bugging the game when several are destroyed at the same time. | Duplicate:inward:MC-139840:Particles create an unusually large amount of lag unlike in older versions | Duplicate:inward:MC-141838:Extreme framerate drop while being around a spawner | Duplicate:inward:MC-143274:Campfire particles cause extreme lag when covered | Duplicate:inward:MC-144021:Too many Soul sand bubble column particles | Duplicate:inward:MC-144803:Extreme Tick Lag | Duplicate:inward:MC-145504:Bubbles and bad performance | Duplicate:inward:MC-147915:TNT explosion causes big  fps drop | Duplicate:inward:MC-152056:Multiple campfires cause exponential framelag | Duplicate:inward:MC-154676:A lot of frame loss for normal particles | Duplicate:inward:MC-155387:Colored dust/block particles are extremely laggy in 1.14 | Relates:outward:MC-123263:Light Update or Block Update FPS issue | Relates:inward:MC-147732:Endless firework and massive lag

## Description

Update:
Also affects my new pc:
CPU:  Intel(R) Core(TM) i5-4570 CPU @ 3.20 Ghz
RAM: 8 GB
GPU: GeForce GTX 1050 ti OC Edition
------------------------------------------------------------------------

Some fixed in 18w09a, but not all e.g dragon breath and rain particles.
I created a world and I went to the end to defeat enderdragon in survivalmode.
After than the dragon shot a fireball the game is stopped work well, because the area_effect_cloud partice is created many lag spikes.
After I summoned blazes and the fps decreased.
I tried it with every particles
Particle performances in 17w50a-18w11a:
In small render distance( 2 chunk), max. fps set 60, played 100 particles with a command(always active repeater command_block)
-angry_villager(100 particle) 33-35 fps
-barrier(100 particle) 33-35 fps
-bubble(100 paricles) 60 fps
-cloud(100 particles) 1-5 fps
-crit(100 particles) 49-52 fps
-damage_indicator(100 particles) 12-26 fps
-dragon_breath(100 particles) 55 fps
-effect(100 particles) 29 fps
enchant(100 particles) 60 fps
and more... Some not laggy and some very laggy
And very laggy some natural generated particles:
dragon_breath,cloud,blockcrack and smoke(blaze and fire)
So the performance with particles was way better in 1.12.2 than 1.13.2 and 1.14 snapshots.
Code analysis
See

## Comments (67)

### Comment 1: migrated (2018-01-11T09:53:44.707-0800)

This comment contained multiple image attachments (16), please login to view the attachments.

### Comment 2: migrated (2018-01-11T14:00:34.197-0800)

Possible clone of MC-122324. Probably not, that is still fixed.

### Comment 3: migrated (2018-01-14T02:28:36.581-0800)

Agreed, VERY laggy compared to 1.12.
Just a large firework which is red and orange with trails, and fades to black/dark gray brings me from 600 fps to like 30
- i5 6500

- GTX 1060 3gb

- -Xmx4G

### Comment 4: [Mod] violine1101 (2018-01-14T05:54:21.546-0800)

Confirmed. Performance with particles was way better in 1.12.2.

### Comment 5: [Mod] violine1101 (2018-01-18T09:10:39.323-0800)

Please use the preview feature (tiny blue card) to preview your changes instead of constantly editing this report, hence spamming the mail account of everyone who watches this ticket.

### Comment 6: [Mod] violine1101 (2018-03-01T08:32:34.751-0800)

Is this still an issue in 18w09a? The changelog mentions
Optimized particle rendering slightly

### Comment 7: migrated (2018-03-15T11:47:37.786-0700)

Some fixed in 18w09a, but not all. I cant't kill the dragon because the game is freezing. The dragon breathe is the most laggiest thing in 1.13 snapshots. And some other laggy particles: explosion, smoke, rain and blockcrack particles.

### Comment 8: migrated (2018-05-29T09:46:59.854-0700)

I think in 18w22a this bug fixed!

### Comment 9: Michael Wobst (2018-05-29T10:58:53.014-0700)

Please re-check to make sure it's really fixed.

### Comment 10: migrated (2018-06-24T05:06:59.807-0700)

can you confirm if this is fixed in newer snapshots/pre-releases ?

### Comment 11: migrated (2018-06-24T05:19:57.108-0700)

I think this bug fixed in the newest snapshots and prereleases.

### Comment 12: migrated (2018-06-26T07:28:08.868-0700)

It is again in 1.13-pre4.

### Comment 13: migrated (2018-07-22T09:19:14.319-0700)

Confirmed in 1.13

### Comment 14: migrated (2018-08-25T11:46:12.363-0700)

XP orb is considered a particle? because I tested my lag with xp orbs and really lags... I can throw 2x more Bottle o' Enchanting in 1.12.2 than in 1.13 before lag starts

### Comment 15: migrated (2018-08-25T11:50:02.607-0700)

XP Orbs are considered as entities. They are another thing to render and calculate.

### Comment 16: [MOD] Greymagic27 (2018-09-03T12:17:28.656-0700)

Firework Particles have this effect

### Comment 17: migrated (2018-09-08T11:30:13.200-0700)

Confirmed in 1.13.1

### Comment 18: [Mod] Asteraoth (2018-09-08T11:37:41.507-0700)

, Minecraft 1.13.1 is already an affected version.

### Comment 19: migrated (2018-10-09T19:51:31.705-0700)

I'd like to just comment, and say that it even affects complete overkill hardware in 1.13.1. I've attached an image above, showing the issue with an i7-7700k and a GTX 1080 Ti displayed in the F3 screen. Sorry if this comment is unneeded. I just figured someone may have come to the false conclusion that since the original reporter has low-end hardware, that may have been a factor.

### Comment 20: migrated (2018-10-20T10:16:50.170-0700)

Just want to mention that this issue persists in 1.13.2-pre2. Command used was /particle minecraft:firework ~ ~10 ~ 1 1 1 1 10000

### Comment 21: [Mod] violine1101 (2018-10-20T10:45:26.030-0700)

I might want to add that I've got this problem as well without needing to use /particle. If it rains, the game lags very much until I disable particles. (Nvidia GeForce GTX 1050 Ti)

### Comment 22: migrated (2018-10-20T11:54:17.281-0700)

Can confirm that some are very laggy compared to others without the particle command. Having enough blaze in one area really hurts due to the smoke even though I have a gtx 1060.

### Comment 23: migrated (2018-10-24T01:20:47.667-0700)

Sorry if this is spam at this point, but I'd like to comment again and show that it still exists in the full 1.13.2 release, this time even without the aforementioned particle command:

This is at a generic enderman farm that worked fine prior to 1.13+ versions.

### Comment 24: migrated (2018-10-25T05:43:09.066-0700)

I'm not certain exactly what is triggering it but when entering a cave if my particles are set any higher than minimal my game get a massive lag spike. any further in or out of the cave and it ceases. there are no mob farms or anything more advanced than 3 furnaces nearby. I'm hoping it's relevant in some way.

### Comment 25: migrated (2018-11-01T00:09:09.268-0700)

Am having insane lag from Blaze spawners in for a blaze farm in 1.13.2. Particles have to be turned down to minimal or I have to walk two chunks away.

### Comment 26: migrated (2018-11-03T14:58:02.159-0700)

I have a insane lag with soul sand burbles underwater, and i have a decent pc, i7, 8gb and a GTX 760, my fps drops from 200-300 to only 2-3 fps! I'm using 1.13.2

### Comment 27: migrated (2018-11-07T07:15:06.208-0800)

Is there a chance that this gets fixed soon? Already tried to play my SP & MP maps with 1.13 but it is not reliable. The issue is quite old and the particle performance is much better in 1.12.2.

### Comment 28: migrated (2018-11-10T03:14:01.110-0800)

In 1.13.2 the fps drops to 3- on my computer when lots of mobs are falling down and dying (killing them by hand won't cause the fps drop), which is unimaginable in 1.12.2. Turning particles to minimal seems to be the only solution now.

### Comment 29: migrated (2018-11-13T10:57:06.643-0800)

Well, it seems that sp614x (the OptiFine creator) discovered what was causing the issue. He explained what it was in his Discord server, so I simply took a screenshot of it. I'm not certain if I can link an invite to the Discord here. Although, here's what he said: https://i.imgur.com/9a9l1yo.png

### Comment 30: [Mod] Asteraoth (2018-11-13T11:04:01.006-0800)

Thanks, .

### Comment 31: migrated (2018-11-13T18:22:25.816-0800)

I was having trouble with fireworks on a server. The only way to stop it was to turn off firework particles with optifine.

### Comment 32: Makzevu (2018-12-08T08:04:38.237-0800)

Optifine E5 pre5, released three days ago, has an applied fixed for particle lag. Is there a way to implement that into the current snapshots?

### Comment 33: migrated (2018-12-08T09:31:17.410-0800)

Some particles are inherently laggy based on durtion, physics, etc..

### Comment 34: Jack McKalling (2019-01-28T13:55:25.747-0800)

I was able to get some weird behaviour with piston-pushed blocks above campfires, which influenced performance related to particles in MC-143274.
It was marked as duplicate of this issue but others apparently couldn't reproduce it there.

### Comment 35: Jack McKalling (2019-01-30T14:12:33.839-0800)

Confirmed for 19w05a

### Comment 36: Jack McKalling (2019-02-06T09:37:59.350-0800)

Confirmed for 19w06a

### Comment 37: Jack McKalling (2019-02-13T09:17:57.681-0800)

Confirmed for 19w07a

### Comment 38: Jack McKalling (2019-02-28T01:48:58.233-0800)

Confirmed for 19w09a

### Comment 39: Jack McKalling (2019-03-13T10:25:21.793-0700)

Confirmed for 19w11a

### Comment 40: Jack McKalling (2019-03-14T09:23:54.701-0700)

Confirmed for 19w11b

### Comment 41: Jack McKalling (2019-03-20T15:23:33.771-0700)

Confirmed for 19w12a

### Comment 42: Jack McKalling (2019-03-21T10:01:46.174-0700)

Confirmed for 19w12b

### Comment 43: Jack McKalling (2019-03-27T12:59:37.821-0700)

Confirmed for 19w13a

### Comment 44: Jack McKalling (2019-03-29T07:18:40.030-0700)

Confirmed for 19w13b

### Comment 45: Jack McKalling (2019-04-03T09:01:38.658-0700)

Confirmed for 19w14a

### Comment 46: Jack McKalling (2019-04-08T02:49:36.284-0700)

Confirmed for 19w14b

### Comment 47: Jack McKalling (2019-04-10T08:35:23.525-0700)

Confirmed for 1.14 pre-1

### Comment 48: Jack McKalling (2019-04-15T02:20:32.206-0700)

Confirmed for 1.14 pre-2

### Comment 49: Jack McKalling (2019-04-16T07:51:57.614-0700)

Confirmed for 1.14 pre-3

### Comment 50: Jack McKalling (2019-04-17T09:42:05.681-0700)

Confirmed for 1.14 pre-4

### Comment 51: Jack McKalling (2019-04-18T06:13:32.014-0700)

Confirmed for 1.14 pre-5

### Comment 52: Jack McKalling (2019-04-23T12:58:09.121-0700)

Confirmed for 1.14

### Comment 53: LogicalGeekBoy (2019-04-26T10:32:17.860-0700)

As others have said the particle lag is incredible. I'm testing out a "World Eater" (https://drive.google.com/drive/folders/1Qbeydk87OdmJV3nkVHzN0_XGxnCc5Sr_ from this YouTube video: https://www.youtube.com/watch?v=I7BOA5Hl6yE) in 1.14 to see how it handles it. The good news is that it works but if I'm within render range of the TNT explosion particles then my frames drop to 1 FPS. 1.12 never had these issues, please spend some time on a 1.14.x release focused just on performance and please include a fix for this issue. Thanks <3

### Comment 54: Jack McKalling (2019-05-07T09:24:55.353-0700)

Confirmed for 1.14.1 pre-1

### Comment 55: migrated (2019-05-07T15:33:47.902-0700)

Very much confirmed in 1.14.1. The game is currently unplayable. How has this issue not been fixed at all? A single tree on fire will drop me 100+FPS even down to 23FPS sometimes when walking around the tree on fire. Lighting the ground on fire causes stutter every time, a single piece of TNT causes a lag spike, and the same for any entities that have particles. It is terrible. I am running on a GTX 1070 with 5960X. Many players have this issue.

This doesn't happen on windows I am running Ubuntu 19.04 with the latest nvidia drivers. The same happens on my identicle system, and my other ryzen 3 1200 GTX 760 system. Anyone without a $1000+ cannot even play the game.

This has all started since the 1.14 release for me. 1.13 was much better, and 1.12 was the best performance. Optifine seems like a standard now. Looking like hytale really will be the replacement everyone can play.

### Comment 56: Jack McKalling (2019-05-09T08:31:11.051-0700)

Confirmed for 1.14.1 pre-2

### Comment 57: Jack McKalling (2019-05-13T06:34:41.230-0700)

Confirmed for 1.14.1

### Comment 58: ZeNico13 (2019-05-13T10:09:41.953-0700)

Can also confirm in 1.14.1 Release

### Comment 59: LogicalGeekBoy (2019-05-16T13:22:37.316-0700)

Confirmed in 1.13.2 and 1.14.2-pre1. If you run Optifine (1.13.2) with explosion animations turned off then this World Eater runs at normal FPS. It would be really good to fix the particle lag in general without the need for a client-side mod. Maybe at least an option to turn off particles all together rather than just the Minimal option that we currently have.

### Comment 60: ZeNico13 (2019-05-17T12:18:02.547-0700)

Still in 1.14.2 Pre-Release 2

### Comment 61: migrated (2019-05-23T21:03:32.294-0700)

The dust and smoke particles has also become significantly more laggier than when it was in 1.12, in 1.12 you could have 1000+ on a repeating command block and only have minor issues, in 1.13 with that many particles fps drops to 1. Extreme case, but only mentioning it because that is what my testing did
In my testing it also appeared that in 1.12 when a large amount of particles were displayed, their lifetime appeared to be shortened. Not sure if this is from lag or if it was intended, but I could not see this happening in 1.13. This may be contributing to the issue, but the main reason has been found above.

### Comment 62: Jack McKalling (2019-06-07T06:19:01.998-0700)

Confirmed fixed for 1.14.3-pre2. For at least my example instance of the issue (campfire particles)

### Comment 63: migrated (2019-06-14T14:07:13.069-0700)

how did you get the lagometer? did you use a mod like optifine? try removing the lagometer.

### Comment 64: Makzevu (2019-06-14T14:13:47.501-0700)

Pressing Alt + F3 enables the FPS and TPS chart in standard (vanilla) Minecraft. Optifine is not required to see that.
Also this bug is fixed.

### Comment 65: migrated (2019-07-27T08:49:34.229-0700)

Not sure if this is the same issue described here, but Blazes cause an extreme amount of lag in 1.14.4 when suffocating inside a wall (e.g. by a crusher trap) - 24 blazes cause very little lag by themselves, but once I start crushing them my framerate drops to 1-2fps. Other sources of damage (e.g. water) cause no issues.

### Comment 66: NickNackGus (2019-07-29T18:26:37.732-0700)

That sounds like it should be a new bug report, assuming other particles aren't causing issues.

### Comment 67: migrated (2019-07-29T20:23:52.825-0700)

Turns out it wasn't from them suffocating, but from being next to an extended East-facing piston (yes, it's THAT specific), and it happens with campfires too (and possibly any other rising particles) - see MC-158037.
