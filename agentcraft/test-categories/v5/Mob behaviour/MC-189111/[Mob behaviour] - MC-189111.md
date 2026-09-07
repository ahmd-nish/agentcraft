# MC-189111: Bees get stuck on non-full blocks

**Mojira URL:** [https://bugs.mojang.com/browse/MC-189111](https://bugs.mojang.com/browse/MC-189111)

## Report details

- **Mojira categories:** Mob behaviour
- **Project:** MC
- **Issue key:** MC-189111
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2020-06-12T12:34:48.692-0700
- **Updated:** 2025-04-29T08:13:08.908-0700
- **Resolution date:** 2024-07-20T21:35:43.637-0700
- **Affects versions:** 1.15.2; 1.16 Pre-release 5; 1.17.1; 1.18.2; 22w17a; 22w18a; 1.19 Pre-release 1; 1.19 Pre-release 2; 1.19 Pre-release 3; 1.19; 1.19.2
- **Fix versions:** 1.19.3 Pre-release 2
- **Area:** Gameplay
- **Labels:** bee; pathfinding
- **Watchers:** 1
- **Attachments:** 10
- **Attachment filenames:** 2020-06-12_15.30.35.png; 2020-06-12_15.31.05.png; 2020-06-12_16.03.51.png; 2020-06-12_16.06.25.png; 2020-06-12_16.09.30.png; 2020-06-12_17.56.08.png; 2020-06-12_17.58.22.png; 2022-05-05_10.29.25.png; 2022-05-05_14.07.03.png; MC-189111 - 1.19 Pre-release 3.png
- **Issue links:** Duplicate:inward:MC-231695:Bees getting stuck under fence | Duplicate:inward:MC-251100:bee frozen on the fence | Duplicate:inward:MC-251716:Bees are stuck in some blocks. | Duplicate:inward:MC-254398:If Bees fly into big field of Bamboo, made by the player(without space in between) they only stay at there position and do nothing | Duplicate:inward:MC-256131:Bees get stuck on multiple blocks | Duplicate:inward:MC-256181:Bee loses AI and animation when wedged between two blocks | Duplicate:inward:MC-257665:Bee AI issue | Duplicate:inward:MC-261336:Bees get stuck in Bamboo | Relates:outward:MC-159447:Bees occasionally get stuck on fences, fence gates, and walls

## Description

The bug
Bees can get stuck inside non-full blocks, such as fences.
Affected blocks
Slim blocks:
- Bamboo

- Chain

- Door

- End rod

- Fence

- Fence gate

- Glass pane

- Grindstone

- Iron bars

- Lightning rod

- Pointed dripstone

- Sea pickle

- Slab

- Stained glass pane

- Wall

Other blocks:
- Cauldron

- Composter

- Scaffolding

To reproduce
- Execute the following command:
/fill ~20 ~-20 ~20 ~ ~ ~ minecraft:acacia_fence hollow

- Summon bees inside and outside the fence cube.

Expected result
The bees should be able to pathfind around the fences.
Observed result
The bees get stuck inside the fences.
Original description
I saw some reports of this issue for earlier versions, and in this report ( MC-159447) the issue was supposedly fixed. I didn't know what to do to report a bug and when trying to sign in my minecraft.net account info did not work so I made a new account to post this bug report. After seeing many snapshots talking about all these fixes I did not see any talk about fixing bees being stuck to fences. Hope I'm not the only one dealing with this. I have a couple screenshots and I put in blocks from 1.16 in it to show that was the version I was playing (1.16 pre5 specifically).
Hope this issue can be resolved before 1.16 officially releases.

## Comments (18)

### Comment 1: migrated (2020-06-12T12:34:48.692-0700)

This comment contained multiple image attachments (10), please login to view the attachments.

### Comment 2: galaxy_2alex (2020-06-12T12:40:15.195-0700)

Please be absolutely certain that this can be reproduced in a 1.16 Pre-5 world, also one that was not open in previous Pre-releases.

### Comment 3: migrated (2020-06-12T12:58:12.018-0700)

Will do so now. this is my first bug report so apologies in advance if I did something wrong

### Comment 4: galaxy_2alex (2020-06-12T13:00:06.089-0700)

No worries, take the time you need

### Comment 5: migrated (2020-06-12T13:11:30.000-0700)

I was able to re create the environment and I did not see any bees get stuck. However using the /fill command with the fence blocks caused the fence blocks already there to look separated and I had to update the fence blocks by placing another block against it. So thats a small side thing I guess.

### Comment 6: migrated (2020-06-12T13:12:46.237-0700)

Also the screenshot with the bees looking stuck were due to the flowers that spawned. is there any way to fix an issue like this with a pre existing 1.15.2 world that this problem happened in? Like will the bees get fixed and fly without being stuck if i loaded the world in 1.16 when it comes out officially?

### Comment 7: galaxy_2alex (2020-06-12T13:15:14.360-0700)

Check if doing "Optimise world" in the "Edit World" screen on the saves menu helps with it.

### Comment 8: migrated (2020-06-12T13:56:24.548-0700)

on it now

### Comment 9: migrated (2020-06-12T14:58:40.263-0700)

Alright. So I optimized the world and it seems as though it worked. I had to use a Lead to pull the Bees out of the ceiling but after that they flew around and I saw them bonk into the ceiling near where the fence and the wood touched (on the perimeter of the circle) and not get stuck. I hope people can find this thread useful if they have this same issue.
EDIT: I saw a couple still get stuck. but it still seems to be an improvement. Not sure only time will tell. My best guess is that the Bees "sense" that they can go outside (in their AI with how they move, like their path) because fences are not full blocks. So they basically see through them.

Added 2 more images.

### Comment 10: anthony cicinelli (2021-07-25T08:18:37.180-0700)

We do not have enough information to find the cause of this issue.
Please record a video of this happening and attach it to this report.
If you are on Windows, you can use Windows+Alt+R to open a built-in app for recording game footage.
If you are on Mac (Mojave or later), you can use Shift+Command+5 to open a built-in app for recording your screen.
In case you don't have a program to record videos, we recommend using the free recording software OBS.
In case the resulting video file is too large to be uploaded to the bug tracker directly, please upload it elsewhere (e.g. as unlisted video on YouTube) and link to it here.
This issue is being temporarily closed as Awaiting Response. Once the requested information has been delivered, the report will be reopened automatically.
Quick Links:
📓 Bug Tracker Guidelines – 💬 Community Support – 📧 Mojang Support
📓 Project Summary – ✍️ Feedback and Suggestions – 📖 Game Wiki

### Comment 11: migrated (2021-08-05T14:32:07.571-0700)

I can confirm in 1.17.1

### Comment 12: pulpetti (2022-05-25T03:41:37.415-0700)

In 1.19 Pre-2.

### Comment 13: ampolive (2022-05-25T06:20:10.243-0700)

This seems to be fixed in 1.19 Pre-release 3.
Edit: nevermind, I was able to still reproduce it in 1.19 Pre-release 3 as well.

### Comment 14: Avoma (2022-05-25T06:33:08.121-0700)

I am still able to reproduce this issue in 1.19 Pre-release 3. In other words, this hasn't been fixed in 1.19 Pre-release 3.

### Comment 15: migrated (2022-07-29T09:37:09.345-0700)

can confirm the same problem with both bees and allays in 1.19.1
Plus flower pots can also stop the pathfinding of bees.

### Comment 16: Avoma (2022-09-17T02:21:23.396-0700)

Can confirm in 1.19.2.

### Comment 17: migrated (2022-11-15T12:00:03.072-0800)

I've noticed bees trying to pathfind through glass panes, slabs, campfires, as well as just full blocks sometimes.

### Comment 18: 7salad3salad (2024-07-20T21:35:43.637-0700)

This bug is occuring with me in 1.21, bees are getting stuck in glowberry cave vine blocks.
