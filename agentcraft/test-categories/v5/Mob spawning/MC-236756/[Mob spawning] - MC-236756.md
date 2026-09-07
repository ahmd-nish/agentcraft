# MC-236756: Biome-exclusive mob spawn rates are reduced

**Mojira URL:** [https://bugs.mojang.com/browse/MC-236756](https://bugs.mojang.com/browse/MC-236756)

## Report details

- **Mojira categories:** Mob spawning
- **Project:** MC
- **Issue key:** MC-236756
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2021-09-15T20:33:43.071-0700
- **Updated:** 2025-04-29T21:12:43.412-0700
- **Resolution date:** 2021-11-19T13:20:43.757-0800
- **Affects versions:** 21w37a; 21w38a; 21w40a; 1.18 Pre-release 1
- **Fix versions:** 1.18 Pre-release 2
- **Watchers:** 1
- **Attachments:** 11
- **Attachment filenames:** 2021-09-15_16.34.12.png; 2021-09-15_16.34.16.png; 2021-09-15_16.35.32.png; 2021-09-15_16.41.47.png; 2021-09-15_16.41.50.png; 2021-09-15_17.26.45.png; 2021-09-15_17.26.49.png; 2021-09-15_17.35.33.png; 2021-09-15_17.35.36.png; 2021-09-15_17.39.55.png; 2021-09-15_17.39.58.png
- **Issue links:** Relates:inward:MC-240513:Pandas do not spawn in bamboo jungles with Default world | Relates:outward:MC-170551:Foxes can't spawn on podzol or coarse dirt | Duplicate:inward:MC-237297:Unique animals (fox, panda) rare spawning | Duplicate:inward:MC-238568:Ocelots are extremely rare in 21w40a | Duplicate:inward:MC-238773:No wolves or rabbit spawning at all | Duplicate:inward:MC-241453:Animals Not Spawning in plains, axolotls not spawning anywhere

## Description

Some biome exclusive mob spawn rates are seemingly reduced. I suspect this is due to the oddities that 3D biomes have introduced.
It's complicated to explain, but basically if you were to go to a Taiga for example you wouldn't see nearly as many foxes as before.
How to replicate
Using /kill for foxes in a taiga in 21w37a will range from "no entity was found" to "Killed 4 entities." Of course this varies but in general it seems to favor lower numbers. Likewise using it in 1.17 will immediately yield numbers such as 18 or 21.
The same can be said for parrots in jungles. Numbers drop from 25 in 1.17 to 10 in 21w27a.
I'm sure a large collection of tests in various seeds/locations would yield better results, and give a better idea of how MUCH this affects mob spawning. However even just exploring on foot in survival, it "feels" like there is less.
Mobs affected
Could relate to MC-236689, though in that bug Pandas aren't spawning at all. Foxes and parrots and the like still do spawn, just in lower numbers.
I don't know the exact extent of what biome exclusive mobs this affects if not all of them, but I also suspect ocelots, llamas, axolotls, and wolves. Completely untested for hostile mobs like Husks/Strays but could apply to them as well.
It also seems like Drowned are affected by this. Killing any naturally generated Drowned from ocean ruins, then letting them spawn back yields significantly less results than former versions.

What I expected to happen:
Biome-specific mob spawning to act as usual and spawn a decent amount of mobs in its specific environment.

## Comments (8)

### Comment 1: migrated (2021-09-15T20:33:43.071-0700)

This comment contained multiple image attachments (11), please login to view the attachments.

### Comment 2: gaspoweredpick (2021-09-16T12:24:20.513-0700)

Biome exclusive mobs also seem to be generating in the wrong biomes as well. From my observation in both the experimental snapshots and 21w37a, this issue only applies to animals that don't despawn.
To reproduce, use the seed -2350610002792544176 and run the following commands:

```/execute in minecraft:overworld run tp @p -24 101 192 -164 12```
Parrots in the middle of plains.

```/tp @p -1513 67 2055 -157 21```
Rabbits in the middle of a jungle edge.

### Comment 3: Tinsel (2021-09-16T20:24:27.646-0700)

Yes I've noticed that too, I made it a sperate report just in case and used your comment within the description with

### Comment 4: anthony cicinelli (2021-09-16T22:11:11.877-0700)

your experiencing

### Comment 5: anthony cicinelli (2021-09-30T21:25:21.293-0700)

This might be because of , MC-155496 & MC-170551

### Comment 6: Moesh (2021-11-04T03:49:42.375-0700)

This is still an issue in the latest snapshot?

### Comment 7: Kidfury (2021-11-12T04:36:30.370-0800)

Can confirm in 1.18 pre-1

### Comment 8: Mr_Quasi (2021-11-12T09:40:40.860-0800)

This fits with this this bugreport:
