# MC-186075: GPU usage in latest snapshot significantly higher than before, causing lag or crash for some users

**Mojira URL:** [https://bugs.mojang.com/browse/MC-186075](https://bugs.mojang.com/browse/MC-186075)

## Report details

- **Mojira categories:** Performance
- **Project:** MC
- **Issue key:** MC-186075
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2020-05-29T06:12:01.047-0700
- **Updated:** 2025-05-29T09:16:29.660-0700
- **Resolution date:** 2022-11-13T13:26:41.092-0800
- **Affects versions:** 20w22a
- **Fix versions:** 1.16 Pre-release 1
- **Watchers:** 2
- **Attachments:** 22
- **Attachment filenames:** 2020-05-29_11.49.34.png; 2020-05-29_15.24.42.png; 2020-05-29_20.00.31.png; 2020-05-30_01.18.36.png; 2020-05-30_16.31.45.png; 2020-05-30_17.08.06.png; 2020-05-31_14.21.09.png; 2020-05-31_14.32.59.png; 2020-05-31_14.34.47.png; 2020-05-31_14.41.48.png; 2020-06-01_18.46.30.png; 2020-06-01_18.47.38.png; debug-report-2020-05-29_16.10.31.zip; image-2020-05-30-00-54-12-004.png; image-2020-05-30-01-17-36-203.png; lag-20w22a.png; MC-186075 Shader Patch r2.zip; MC-186075 Shader Patch r3.zip; MC-186075 Shader Patch r4.zip; profile-results-2020-05-29_16.10.27.txt; Screenshot 2020-05-29 at 15.36.25.png; Screenshot 2020-05-29 at 15.42.29.png
- **Issue links:** Duplicate:inward:MC-186411:Horrible performance using Intel HD Graphics 3000 on Ubuntu 20.04 and several other issues

## Description

Workaround
There is a resource pack by  and  attached to this ticket which may mitigate the performance issues introduced in 20w22a by applying some changes to the built-in shaders that Minecraft uses.
You can install it just like any other resource pack. Here's a tutorial if you don't know how to do that: https://minecraft.gamepedia.com/Tutorials/Loading_a_resource_pack
This is the latest version of the resource pack:
There are no guarantees from the mod team or Mojang that it works, but many people in the comments of this ticket have confirmed that it improves the game's performance significantly in this snapshot.
Please note that since the rendering changes are experimental and may be changed or removed altogether in future snapshots, the resource pack patch may stop working in in the future.
If you're interested in the source code, here's the GitHub repo for the resource pack.
In the latest Snapshot, 20w22a, GPU usage has significantly increased, causing many users to experience decreased performance, with some being unable to even start the game.
Analysis by
It looks like the culprit of this massive increase in GPU usage comes down to the new framebuffer blending technique used to resolve some translucency issues between render layers (i.e. items behind fluids).

## Comments (100)

### Comment 1: migrated (2020-05-29T06:12:01.047-0700)

This comment contained multiple image attachments (22), please login to view the attachments.

### Comment 2: [Mod] violine1101 (2020-05-29T06:16:47.869-0700)

What are your system specs (CPU, graphics card...)?

### Comment 3: migrated (2020-05-29T06:38:28.637-0700)

2.5 GHz Intel Core i5
8 GB 1333 MHz DDR3
AMD Radeon HD 6750M 512 MB

I know, my computer is getting a bit old haha, but it's still a bit interesting to see such a big difference between two snapshots

### Comment 4: [Mod] violine1101 (2020-05-29T07:19:32.675-0700)

Okay, that's still in the supported hardware range though, I think. There were a bunch of rendering changes in the last snapshot, so that's probably why it got so much worse.

### Comment 5: migrated (2020-05-29T07:30:50.499-0700)

you are lucky, im getting literally 10-11fps in 20w22a

### Comment 6: galaxy_2alex (2020-05-29T07:42:46.879-0700)

I can confirm the significant increase in GPU usage, about 10% in 20w21a compared to 80% in 20w22a.

### Comment 7: migrated (2020-05-29T07:52:36.172-0700)

I went from 30 fps to like 1-2 fps, my specs are:

Intel Core i5-4300U CPU @1.90 GHz
4 GB 1600 MHz DDR3
Intel HD Graphics Family

Is this still within the supported hardware range?

### Comment 8: CreeperMagnet_ (2020-05-29T07:53:44.042-0700)

Also experiencing this issue. My specs:

```MacOS
MacBook Pro (Retina, 13-inch, Mid 2014)
2.6 GHz Dual-Core Intel Core i5
16 GB 1600 MHz DDR3
Intel Iris 1536 MB```

### Comment 9: migrated (2020-05-29T08:05:39.278-0700)

I am having the same problem, my specs are:

Windows 10
Intel Core i5-4210U CPU @ 1.70GHz
8 GB
Intel HD Graphics Family

### Comment 10: migrated (2020-05-29T08:08:44.099-0700)

Same here. My specs:

```macOS High Sierra
Version 10.13.6
MacBook Pro (Retina, 13-inch, Mid 2014)
Processor 3 GHz Intel Core i7
Memory 16 GB 1600 MHz DDR3
Graphics Intel Iris 1536 MB```

### Comment 11: migrated (2020-05-29T08:29:17.242-0700)

I have the same issue.

```Windows 10
CPU Intel Core i7-5500U 2.40 GHz
Memory 12 GB 1600 MHz DDR3
GPU Nvidia GeForce 920M```

### Comment 12: lastchaos26200 (2020-05-29T08:54:11.475-0700)

I have the same issue.

```Windows 10 Home 64 Bit
CPU Intel Core i5 760 2.80 GHz
Memory 8 GB 1333 MHz DDR1
GPU Nvidia GAINWARD 9500GT 512MB DDR2```

### Comment 13: migrated (2020-05-29T09:01:19.025-0700)

What I want to know is how were you getting 120fps before?! I have a brand new Mac and I rarely get above 40fps, and this was on previous snapshot as well.
MacBook Pro 16" 2019
MacOS 10.15.4
Intel Core i7 6-Core 2.6GHz, 16GB RAM, AMD Radeon Pro 5300M 4GB

### Comment 14: migrated (2020-05-29T09:07:39.451-0700)

My FPS with Vsync ON is locked on 20 and without Vsync to 30 ..
FPS before the 20w22a - Stable 60 with Vsync ON and about 80+- with Vsync OFF

```Windows 10
CPU - Intel Pentium G3220
Ram- 8GB
Ram allocated to the game - 3
GPU -Intel Integrated 4000```

### Comment 15: migrated (2020-05-29T09:08:39.890-0700)

Gavin, I don't know, I usually turn some settings to fast, but not render distance or some other small ones. I've never tried texture packs or shaders on this computer.

I've never built anything big so I don't how it would perform with a lot of objects and blocks around.

Amplified gamemode doesn't give me issues though.

My FPS is pretty stable at 120.

### Comment 16: migrated (2020-05-29T09:18:00.761-0700)

Same problem, but also noticed that usage jumps from average 80% to 100% between 14 and 15 chunks of render distance

```Windows 10 Home
CPU Intel Core i5-8400 2.80 GHz
Memory 8 GB 2133 MHz DDR4
GPU Nvidia GeForce GTX 1060 3GB```

### Comment 17: migrated (2020-05-29T09:28:40.533-0700)

Junhani, I think I figured it out. I'm running at almost 4K resolution and have Vsync, which is probably my source of lower fps. Updating snapshots did not have an effect for performance for me however.

### Comment 18: migrated (2020-05-29T09:31:54.714-0700)

Can confirm this issue on macOS Mojave with 4 GB RAM

### Comment 19: migrated (2020-05-29T09:43:33.541-0700)

Same, I get around 3 fps in 20w22a but I was getting around 30-60 frames per second in 20w21a. Please, Mojang Studios I want a good fps.
My specs are : Intel core i3-2120 3.3Ghz, Intel HD graphics and 2 gb of ram allocated to Minecraft.

### Comment 20: migrated (2020-05-29T10:03:49.395-0700)

i had 20-30 fps in 20w21 which was good enough for me but as soon as i got to the latest i now got 3 or even lower, mojang please fix this
also i have 8 GB of ram and an ATI Radeon 3100 Graphics just in case someone asks

### Comment 21: migrated (2020-05-29T10:05:51.003-0700)

Same problem. I have max 9 fps. They have to fix this either today or tomorrow. This is a serious bug which may be devastating for some users especially for hardcore players. I had up to 70 fps at normal last snapshot but never had this low normally.

### Comment 22: migrated (2020-05-29T10:11:54.473-0700)

Do you happen to have discord or saomething? we can talk about this and another issue that i have but a mod said i didnt provide enough information, im just hoping at least for an answer

### Comment 23: migrated (2020-05-29T10:18:23.148-0700)

Same problem for me. I'm getting around 8 fps in 20w22a. I was getting around 60 with 20w21. Now my game play is so laggy I simply can't play. MAC - Processor 3.2 GHz Intel Core i3, Memory 4 GB 1333 MHz DDR3, Graphics ATI Radeon HD 5670 512 MB.  ...How soon can this be fix?

### Comment 24: migrated (2020-05-29T10:53:50.918-0700)

Yesss!! Before on 20w21a I was getting around 120-140 fps, now on 20w22a I'm getting 40-60 fps and a some weird lag input, my pc is old, and I hope they fix it, I don't have the money to upgrade my pc now

### Comment 25: migrated (2020-05-29T11:01:36.282-0700)

i feel you buddy, i upgraded a year ago, i cannot do anymore upgrades due to my mum not getting any money or just saying no about it, god i hope mojang fix this aswell as a nether related issue that i have, you can check it if you want

### Comment 26: migrated (2020-05-29T11:07:23.909-0700)

I had about 40 fps in 20w21a, which is enough and good for me. Now my average framerate is about 18. It isn't fun to play, please do something about this. Not every Minecraft player has a very strong PC.
My processor: Intel(R) Core(TM) i5-8250U CPU @ 1.60 GHz, 1800MHz
My RAM: 7.88 GB
My graphics card: Intel(R) UHD Graphics 620

### Comment 27: migrated (2020-05-29T11:07:26.959-0700)

Same issue for me with a GT705 GPU

### Comment 28: migrated (2020-05-29T11:09:12.238-0700)

Seeing GPU power consumption and utilization doubled between 20w22a and the previous snapshot on my workstation machine. My game's overall frame rate has not changed due to a CPU bottleneck caused by the number of chunk draw calls, but the GPU is much more busy when playing in fullscreen (1080p) than before. I'm not locked to v-sync here despite the misleading frame rates.
GPU stats
Version     VRAM Allocated   GPU TDP    GPU Utilization   Frame rate
20w21a      312MiB           36W        37%               59 fps
20w22a      423MiB           63W        71%               59 fps
System Specs
Arch Linux (5.6.14 kernel)
AMD FX-8370 (8 cores) @ 4.3GHz
24GB DDR3 RAM (2x8GB + 2x4GB)
GTX 960 (2GB VRAM)
1920x1080 Display
It looks like the culprit of this massive increase in GPU usage comes down to the new framebuffer blending technique used to resolve some translucency issues between render layers (i.e. items behind fluids). I've made a small resource patch which applies some optimizations to the shader in question in order to help reduce GPU usage. Primarily, it eliminates the secondary indexing table used to sort the fragments on each frame buffer and uses a faster insertion sort algorithm. The blend code itself accounts for a very small amount of the overall shader's execution time.
On my machine, this patch (in a different scene) makes a considerable improvement to GPU utilization at a render distance of 16 chunks and brings it much closer to 20w21a.
GPU stats with attached resource pack
                    GPU TDP     GPU Utilization   Frame rate
20w11a (Vanilla)    54W         38%               123fps
20w22a (Vanilla)    66W         95%               100fps
20w22a (w/ Patch)   54W         45%               118fps
I've uploaded a resource pack to this issue with the optimized shader code that can be used to help improve performance on affected machines, but it does not fully eliminate the added overhead of this new render pass.

### Comment 29: migrated (2020-05-29T11:24:50.896-0700)

you basically say that its something that wont be fixed???

### Comment 30: migrated (2020-05-29T11:26:32.845-0700)

I am having this issue as well. I have an old i5-3550, Intel HD 2500 and 8gb ram. On 20w21a with low gfx settings (render distance still 12) I get on average 30 fps and the game has been perfectly playable. This snapshot I get 7-8 fps and chunk rendering is glacial.

### Comment 31: migrated (2020-05-29T11:27:38.218-0700)

Same issue on my  machine.

```Intel Core I5 660 @ 3,3Ghz
8Gb 1333Mhz DDR3 Ram
AMD Radeon HD6450 - 2Gb```
From 50-60 FPS in snapshot 20w21a to 8-10FPS in this (20w22a) snapshot

### Comment 32: migrated (2020-05-29T11:32:16.707-0700)

your resource pack made my game run like crap.. With your pack instead of locked 20FPS i get like below 10FPS ..
Might be patch for someone with a bit more powerful VCard but for me .. it does nothing positive ..

### Comment 33: migrated (2020-05-29T11:53:35.163-0700)

Same problem.  Performed well in previous snapshot, but frame rate in 20w22a is unplayable on my son's older laptop:
Windows 10 1909
NVidia NVS 3100M  driver 21.21.13.4201
Core i5 M560 @ 2.67 GHz
8 GB RAM

### Comment 34: migrated (2020-05-29T11:53:40.508-0700)

Before applying the shader fix you've provided: 140~ FPS
After: 200~ FPS
I am using a GTX 1050 Ti on a laptop.

### Comment 35: Checkmate128 (2020-05-29T11:53:54.385-0700)

I have Intel UHD Graphics 617 and the game is barely playable for me.

### Comment 36: migrated (2020-05-29T11:59:08.318-0700)

i say we need perfomance improvements in the next update

### Comment 37: Jofroop (2020-05-29T12:27:18.404-0700)

intel iris 6200, imac mid 2015, when playing on 1080p im usually around 150 170 fps, im down to 20 now.

### Comment 38: migrated (2020-05-29T12:32:19.282-0700)

I'm experiencing this on a 2017 15 inch MacBook Pro, with a 3.1 GHz Intel Core i7 and a Radeon Pro 560 (4 GB VRAM). Mac in particular is likely to be hit hard due to weird 2x resolution scaling on retina displays, which Minecraft doesn't account for causing Minecraft to render at higher resolutions, which exasperates this bug.

### Comment 39: migrated (2020-05-29T12:32:55.585-0700)

Same for me, with an iMac from 2013. The game is basically umplayable. Now I have to go back to 20w21a with a world I just opened in 20w22a. I hope it won't suffer corruption.
Mac form 2013,
Intel Iris Pro 1536 Mo
8 Go 1600 MHz DDR3

### Comment 40: migrated (2020-05-29T13:03:44.728-0700)

If anyone has a workaround solution, please reply to this comment.

### Comment 41: gegy (2020-05-29T13:11:41.826-0700)

I added an alternative patched resource pack to the one that JellySquid posted here. For the most part they're the same, however some people have reported that this one performs a lot better (on my computer, they're equivalent). Could be a false positive, but I hope it's useful to try anyway!

### Comment 42: migrated (2020-05-29T13:42:43.210-0700)

Same issue for me on the default game with no resource packs. I notice significant spikes in frame times. Nothing pops out on the debug pie.

### Comment 43: migrated (2020-05-29T14:16:57.212-0700)

still unplayable even with the alt, i guess i have to hope that Mojang fix this ASAP

### Comment 44: migrated (2020-05-29T14:29:24.067-0700)

How long does it take for Mojang to fix something like this? A couple of days? Or will we be waiting until the next Snapshot release?  Will it even be fixed with the next release? I've never had an issue with minecraft before and I'm not sure what to plan for? Anyone have any experience with issues and their resolution time?

### Comment 45: migrated (2020-05-29T14:40:57.975-0700)

Same performance Drop for me on a Mid 2015 MacBook Pro with Intel Iris 5100 16GB Intel i7 2.2Ghz 16GB RAM. I had constant 30fps with 14 chunks render distance. Now I can barely play with 6 chunks all video settings set to lowest possible quality / fastest option available. Please undo the experimental render changes or fix them for the 1.16 release or I will be a very sad person.

### Comment 46: migrated (2020-05-29T14:42:16.216-0700)

@JustBoyann Can you try the updated resource pack? It should perform better on Intel graphics cards.
@DieselDorky16 There is a resource pack included as an attachment
 which might help you. Any feedback with it would be useful.

### Comment 47: migrated (2020-05-29T15:16:19.578-0700)

@JellySquid  It performs pretty well.. My performance still isnt as before this update but its playable this time..

### Comment 48: migrated (2020-05-29T15:20:07.047-0700)

@JellySquid, the Shader Patch r2 makes the game pretty playable between 25-55 FPS on my side, if you have another patch let me know.

### Comment 49: migrated (2020-05-29T15:35:37.952-0700)

Hey @JellySquid, tried the resource pack on both my usual single player save and a brand new world, minor improvement in both put still unplayable (around 10-12 fps compared to 6-8 without it).
I have an early 2014 macbook air with intel i5 1,4ghz, an Intel HD Graphics 5000 1536 MB graphic card and 4gb ram, which usually, with a 12 chunks render distance, allow for around 30-40 fps...
EDIT:
restarting my pc solved (partially) the problem, giving me, with the resource pack, around 20-25 fps, good job!
However my water/glass/reflection in general textures are a bit wonky now, showing white "cloud-like boxes" that move with my crosshair...

### Comment 50: migrated (2020-05-29T16:53:38.118-0700)

Same here.
In snapshot 20w21a like 60-70 FPS
In snapshot 20w22a like 10 FPS...
My specs:
Acer Aspire ES1-571
intel(R) Core(TM) i5-4210U CPU @ 1.70GHz
Intel(R) HD Graphics 4400
8 GB RAM
in Windows 10
Literally unplayable, i hope this change is fixed or removed...

### Comment 51: migrated (2020-05-29T17:06:16.103-0700)

Exactly, my game just froze. It can't be though, I usually get 60 fps, and all there is like 90 villagers, that's all. Ok, maybe some illagers and iron golems, but that's it. An underground village. This never happened in 20w21a.

### Comment 52: migrated (2020-05-29T17:29:01.545-0700)

Can confirm, during 20w21a I was getting 60 fps. Now I get 10 fps and if lucky 15 fps.

### Comment 53: migrated (2020-05-29T18:06:02.342-0700)

Same issue here. Nvidia Quadro M2200 tested on both Win10 and Ubuntu 18.04. Before, 50-60 fps at minimum, now 20fps at best.

### Comment 54: migrated (2020-05-29T20:22:47.266-0700)

@PitNox The issue you describe is caused by MC-186064 which is another bug with vanilla's new framebuffer blend code. This was incorrect, it was caused by a sporadic bug in my shader code and has since been fixed.

### Comment 55: migrated (2020-05-29T22:47:13.178-0700)

I have just tried the resource pack fix that is attached to this issues on my Intel Iris 5100 GPU and it is helping a ton.  It even is running better than Vanilla 20w21a before. Phew, thats great.

### Comment 56: gegy (2020-05-30T00:45:38.471-0700)

Looks like I accidentally introduced a sorting bug which affects the alt and r2 version. I hope that this is not the cause of the performance gains from r2 over r1. I've attached a new file that fixes this sorting bug, and makes some additional optimization (performing the insertion sort as layers are added to the array; removes need for an additional loop)
If you experienced better performance in r2 over r1, it'd be greatly appreciate to test this r3 version!

### Comment 57: migrated (2020-05-30T01:09:25.566-0700)

@gegy1000 solved both framerate and layering issues for me, amazing job!

### Comment 58: owlfalls35 (2020-05-30T03:59:03.905-0700)

Same here. my graphics, Radeon Pro 555X 2 GB, goes up to 100% when playing 20w22a. Although  don't experience any lag on lower render distances, it starts lagging when I turn the render distance up.

### Comment 59: migrated (2020-05-30T04:00:24.765-0700)

Prior to 20w22a  FPS rate 40-50 ..... as of 20w22a  FPS rate.... 2-4     Intel i5-2400 @3.1G  Intel HD Graphics 200 3.1.0 - build 9.17.10.4459

### Comment 60: migrated (2020-05-30T04:15:28.866-0700)

FPS dropped to 5-6 since 20w22a. Intel i5-3210M @2.5GHz Intel HD Graphics 4000. Previous snapshot ran perfectly on 40 FPS.

### Comment 61: migrated (2020-05-30T04:33:41.543-0700)

IMPORTANT: I've experienced PC reboots and I believe it is because of this bug. My computer works completely fine and I've never experienced a reboot like this from any program or GPU issue. Sometimes when I open up this latest snapshot my PC will reboot. I believe Minecraft 20w22a is the cause because it only happens right after I launch 20w22a, and whenever my PC starts back up I'm logged out of my accounts in the launcher as well as my launcher profiles are reset.
This has never happened before and only does it after I launch. Doesn't happen every time, but I kept closing and reopening and it happened. I recorded it and if the clip needs uploading I can do that.
GPU: Nvidia GeForce GTX 980.
Using the pack provided by gegy1000 improved my fps and GPU usage, but my GPU usage was still much higher than normal. Without the pack in 20w22a GPU usage was always at 90%+ and FPS around 250. With the pack my fps increased to around 500 with GPU usage around 60-70 with spikes up to 90+. My normal GPU usage in 20w21a is around 30 to 40% with FPS around 600-800.

### Comment 62: migrated (2020-05-30T04:35:38.022-0700)

The lag is significantly different. I used a laptop to play Minecraft which was a lot better than this...
Laptop specs:
CPU: Intel i3-6100U
GPU: Intel HD 520 (Mobile Skylake)
RAM: 6GB DDR3

And now I am using a desktop which (said by User benchmark) is a lot better than the laptop
Desktop specs:
CPU: Intel I5-7400
GPU: NVIDIA Geforce 750 TI
RAM: 8GB DDR4

Please fix this bug! I really don't like 10 fps!
Side note: Its not all the time it is little blips at a time that drop down to 5-10 fps if I'm walking or flying or breaking a block.

### Comment 63: migrated (2020-05-30T05:15:37.783-0700)

with intel graphics 4000, fps falls to 6 or 7..... impossible to use the game .....
please , fix it !!

### Comment 64: migrated (2020-05-30T06:35:20.447-0700)

Graphics Card: Intel (R) HD Graphics (Integrated)
Brand: Intel
Operating System: Windows 10 (Home)
CPU: Intel(R) Celeron(R) CPU N3150 @ 1.60GHz (4 Cores)
RAM: 4GB
All the same. Even on this hardware, I was given 30-60 FPS, but not now.

### Comment 65: migrated (2020-05-30T07:16:57.291-0700)

is this resolved or? I'm not familiar with being on here to see what the bugs are. the main problem I have is the lag which is said to be resolved but isn't for me. no idea what is happening, what has happened, or what's going to happen.

### Comment 66: migrated (2020-05-30T07:21:02.175-0700)

@JellySquid and @gegy1000 patch r3 improved my fps and my experience! You've saved my weekend. Thank you!
I can totally picture developers at Mojang looking away from this critical issue when it popped up on a Friday evening when they were about to close their computers and go home for the weekend.

### Comment 67: migrated (2020-05-30T07:55:42.502-0700)

I've never used a patch before, how does it work? Is it better to wait till Mojang fixes this issue? How does a patch effect later Snapshot updates?

### Comment 68: [Mod] violine1101 (2020-05-30T08:07:49.945-0700)

The "patch" that was made by  and  is just a resource pack that you can install just like any other resource pack. Here's a tutorial: https://minecraft.gamepedia.com/Tutorials/Loading_a_resource_pack
This is the latest version of the resource pack:
I have not tested the resource pack myself and there are no guarantees from the mod team or Mojang that it works, but many people in this ticket have confirmed that it improves the game's performance significantly in this snapshot.
Please note that since the rendering changes are experimental and may be changed or removed altogether in future snapshots, the resource pack patch may stop working in future snapshots.
Edit: I have now tested the resource pack myself and it seems to improve the performance quite a bit. It doesn't make too much of a difference for me though since I've already got a good mid-tier graphics card and vanilla is running pretty smoothly even without the patch.

### Comment 69: migrated (2020-05-30T08:11:51.903-0700)

Thank you [Mod] violine101 so much for comment!
Also this resource pack is the same minecraft but boost your fps!
This resource pack help me a lot from 10-20 fps to 40-50!

### Comment 70: migrated (2020-05-30T09:22:27.732-0700)

I literally have 1-2 fps at all times while playing this snapshot, I'm not even exaggerating, my f3 screen actually says 1 fps or 2 fps at all times. I hope that a 20w22b comes out today to fix this.

### Comment 71: migrated (2020-05-30T09:57:41.824-0700)

I really appreciate the efforts by  and  with their resource pack. I gave it a try, following the instructions posted by  . My fps went from 8 to 13 with with an allocation 16 spike. My game play is still too laggy to play.  It's crazy frustrating and I really miss how smooth things ran with 20w21a. I'm still hoping Mojang will official correct this issue. Based on the comments I guess I'll have to wait till the next Snapshot update to see if they fix it. What if they don't?

### Comment 72: migrated (2020-05-30T12:02:07.820-0700)

I've created a GitHub repository to manage future releases of the shader code optimization resource pack in order to avoid additional clutter on this thread. Any issues caused by it should be reported on its respective issue tracker. I've just published the r3 pack attached to this issue as version 1.1.1 which you can now download from here.
For Mojangsters looking at this issue: I have explicitly licensed the shader code here (with permission from @gegy1000 for their additional fixes) under the CC0 Public Domain license. Feel free to use what's there.

### Comment 73: migrated (2020-05-30T12:51:13.489-0700)

The resource pack got my FPS back up to 30, but the CPUs and GPU were still close to 100°C (13" MacBook Pro 2019), and I don't want to risk causing damage.  Hope it gets fixed soon!

### Comment 74: JuniorJedi256 (2020-05-30T13:04:46.369-0700)

Laptop computer, Windows 10
Intel(R) HD Graphics 620
CPU: 4x Intel(R) Core(TM) i3-7100U CPU @ 2.40GHz according to a debug crash report
20w20b gets ~10 FPS when chunks are generating and 30 ± 10 FPS when the world is fully loaded.
20w22a gets ~10 FPS when (already generated) chunks are loading and 20 ± 10 FPS otherwise, with or without the resource pack.
TL:Doctor The resource pack doesn't help me, but my FPS is already so low that the difference between versions is nearly within the margin of error.

### Comment 75: migrated (2020-05-30T13:28:51.228-0700)

I got really scared since my GPU usage spiked from 30/40% since I had my fps looked at 60 down to like 40 with 100% GPU usage.
My specs:
i7 second-gen
gtx 560m (2gb VRAM)
16gb ram
and the game runs from a Samsung Evo SSD
I hope this gets resolved.
I do have to admit frames are more stable next to my storage system (it has li 100+ item frames) dropping only 10 fps when next to it and cpu usage seemed to go down so if the problem gets addressed would be great since Minecraft doesn't seem to need more GPU power than GTAV...

### Comment 76: migrated (2020-05-30T13:49:24.175-0700)

Even with the resource pack its way too unplayable, i really just want the next snapshot to remove the experimental features or whatever if they are really the cause.

### Comment 77: migrated (2020-05-30T14:55:17.315-0700)

I'm on a 2018 Mac mini with a fast-ish 3.2 GHz Intel Core i7 processor, 16 GB RAM and 20w22a is crazy laggy compared to happily playable a snapshot or two ago.  My mini feels like a hot-plate after playing 20w22a.  I don't install resource packs or mods, so hopefully this issue will get worked out.

### Comment 78: migrated (2020-05-30T15:00:19.823-0700)

it doesnt matter even if you put a resource pack, i tested it and even on default isnt any better

### Comment 79: migrated (2020-05-30T15:16:05.618-0700)

On my macOS it is max 9 fps and least 3 fps but on my Windows 10 it is max 6 fps and least 0 fps.

### Comment 80: migrated (2020-05-30T16:07:52.532-0700)

I have found out that not doing it in full screen increases the fps, but the bigger you make the screen, the lower your fps will be. It was running really smoothly, but that was only because the screen was really small.

### Comment 81: migrated (2020-05-30T21:14:35.085-0700)

My sons laptop is getting about 1-2 fps trying to play on our snapshot server.
System Specs:
Intel Core i5-3230M @ 2.60GHz
8GB Ram
NVIDIA GeForce GT 650M

### Comment 82: migrated (2020-05-31T01:22:41.821-0700)

Adding the shader resource pack increased the fps from 3-5 to 14-16 and presented a mostly black screen.
This error also occurred:
04:06:25.407
Could not find uniform named InSize in the specified shader program.
Turning off the clouds resolved the cloud issue.

### Comment 83: gegy (2020-05-31T05:20:10.350-0700)

Did some further testing on an Intel UHD 630 GPU and managed to make some fairly significant optimisation there. It doesn't seem to have a broad improvement for all GPUs, but definitely an improvement in some cases.
I've attached another resource pack which might be worth trying if you're using an Intel GPU:

### Comment 84: migrated (2020-05-31T06:32:34.038-0700)

I play Minecraft Java Edition in my computer, which has Windows 10 64-bit as OS, an Intel Core i5-8265U as CPU, 8GB RAM and a Intel UHD Graphics 620 as GPU. In snapshot 20w21a the framerate was stable around 30 or 35 fps. In the latest snapshot, 20w22a, the framerate is always around 12 and 21 fps and it lag every while, making the game unplayable. To have a decent framerate, I must set the render distance 2 chunks and minimum graphics. In older snapshots, I used maximum graphics and 16 chunks render distance. I don't use any resource pack

### Comment 85: Michael Wobst (2020-05-31T06:47:15.709-0700)

, I removed your screenshot as it has nothing todo with the bug itself. It is misleading others, maybe even the developers as they might think that what can be seen there is caused by the bug described in this ticket. If you want to show something about the attached resource pack, please get in touch with the creator directly as it is off-topic here.

### Comment 86: migrated (2020-05-31T06:47:50.569-0700)

I've also lost a lot of FPS with 20w22a. Here are the screenshots of F3 in 20w21a, 20w22a and 20w22a with the recommended resource pack (which helps a tiny bit)
My graphics card is NVIDIA GeForce GTX 860M

### Comment 87: migrated (2020-05-31T09:50:37.367-0700)

can't Mojang just squeeze out an update focused on this specific issue, im sorry if this sounds dumb but i dont want my Minecraft days to be all over because of this specific issue

### Comment 88: Michael Wobst (2020-05-31T10:02:00.425-0700)

, use the latest stable version which is 1.15.2. Snapshots are experimental development versions which are not stable and can be full of bugs. These are for testing only.

### Comment 89: migrated (2020-05-31T15:09:10.212-0700)

I tested with 10,000 glass blocks in a newly generated world in 20w22a, and with or without the blocks, the game ran at around 16 mspt, and 30 fps, so glass isn't a solo lag causer.

(I chose glass because I heard that glass had some changes.)

### Comment 90: migrated (2020-05-31T19:05:23.045-0700)

can confirm it ussualy getting 50-70 FPS at 1080p 12 Chunks but now im always getting 20-25FPS the exeptions are windowed default resolution and full screen 240p. away from that there is only 20-25FPS in any resolution both windowed and full screen if it helps here are my specs
CPU:Intel Celeron G1820 2.70Ghz
GPU:Nvidia GeForce GT 730 2GB
RAM:8GB DDR3
Storage:SSD kingston A400

### Comment 91: migrated (2020-06-01T00:36:41.523-0700)

Should we expect this issue to be resolved? I used to be able to play the game with a relatively alright computer... Is this how demanding will the game be from now on, in terms of performance, or should I hope I'll be able to play again?

### Comment 92: galaxy_2alex (2020-06-01T07:25:31.278-0700)

: At this moment, we do not know - however, so far, there have not been any announcements about changing system requirements for 1.16, and there are many people experiencing this to an unplayable degree whose system does meet those (though many users that do complain about the unplayability do not meet the requirements). That is all the information we have at this moment however.

### Comment 93: migrated (2020-06-01T09:05:27.374-0700)

Operating System: Ubuntu 20.04
KDE Plasma Version: 5.18.5
KDE Frameworks Version: 5.68.0
Qt Version: 5.12.8
Kernel Version: 5.4.0-33-generic
OS Type: 64-bit
Processors: 2 × Intel® Core™2 Duo CPU P8400 @ 2.26GHz
Memory: 2.9 GiB
Swap: 7.6 GiB
Graphics Processor: GeForce 9600M GT
NVIDIA Driver Version: 340.108
Display: 1440×900
SSD (100 MiB/s)
5 launches were made.
Version 1.14.4
Just render chunks, upload. Waiting for a full load of chunks. I turn it off.
Version 1.14.4
39 fps
Waiting time for all chunks: 17:00.00+
Version 1.14.4 and optifine
37 fps and a minimum: 28 fps, it looks smooth
Waiting time for all chunks: 2:36.68
Version 1.15.2
35 fps, but look bad compared to 1.14.4 optofine
Waiting time for all chunks: 2:19.00
Version 20w22a
7 fps
Waiting time for all chunks: 2:13.00

### Comment 94: migrated (2020-06-01T11:31:16.808-0700)

I can confirm 20w22a is lagging on macOS.

macOS 10.15.5 (latest)
iMac (Retina 4K, 21.5-inch, 2017) (iMac18,2)
Intel i5 7400 (3.0GHz, 4C 4T)
8GB DDR4 2400MHz
Radeon Pro 555 2GB

I noticed considerable system slowdown on macOS, something which a GPU intensive application can cause.

Approximately 28FPS (60FPS 4096x2304 monitor), Fancy Graphics, 16 chunks Render Distance, Fullscreen.

### Comment 95: migrated (2020-06-01T13:14:07.799-0700)

Are You Added At Least 6GB Memory To Your Minecraft? (-Xms & -Xmx)
If No, You Must Add it In Launcher.

Try Using Optifine Client With VBO's Enabled.

Disable Entity Shadows.
Set Particles To Minimal
Also Check Your Graphics Driver (In Windows & Linux "If you have linux you must install nvidia graphics driver with add-on repository otherwise it won't work.")
Disable V-Sync

### Comment 96: migrated (2020-06-01T17:16:23.717-0700)

I can also confirm that this is causing a very large FPS decrease on my machine as well.

Machine Specs:
macOS 10.15.5
MacBook Pro 16 (2019)
Intel(R) Core(TM) i9-9980HK CPU @ 2.40GHz
64GB DDR4 RAM
Radeon Pro 5500M 8GB

Before 20w22a, I was able to run Minecraft fullscreen at 4k 60FPS (32 chunk render distance). Now, I'm only able to run the game at 30 FPS. Decreasing the render distance or adjusting any other performance settings doesn't improve (or degrade) the FPS at all.
I used the above resource pack and was able to gain an additional 10FPS, however, this is still a far cry from the previous performance before this snapshot.
It would be great if this was addressed in the next patch please!
Thank you!

### Comment 97: migrated (2020-06-01T20:10:20.610-0700)

In 20w21a, i had normal frames (40-60), but in the latest, it dropped to only four frames and was almost unplayable. The resolution shouldnt be an addon pack, but a change to the change in 22a.

### Comment 98: migrated (2020-06-02T00:46:40.143-0700)

's resource pack reduces my GPU usage to 67% of what it was before applying it.  Not noticed any downsides to it.  geforce 2060 super

### Comment 99: Adrian Östergård (2020-06-03T00:04:48.836-0700)

If a new or similar issue related to this appears in the next snapshot, please open a new bug that highlights the specific issue.

### Comment 100: migrated (2020-06-03T10:02:14.235-0700)

Just wanted to put it in writing that this bug was marked resolved 10 hours ago.  I don't see it specifically mentioned in the comments so I wanted to mention it.  I see a lot of people asking if it'll be fixed in the next release and since there are a lot of people running the snapshot, I think it's a fair question to ask.  Adrian, is it safe to assume this fix will land on the next snapshot?  I was going to offer up some specific details about the various machines (some brand new Macs) that this occurs on but I'd rather hold off if it's purported as fixed.
