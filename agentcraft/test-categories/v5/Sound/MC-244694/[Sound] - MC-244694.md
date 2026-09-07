# MC-244694: The sounds of goats stomping and ramming aren't controlled by the "Friendly Creatures" sound slider

**Mojira URL:** [https://bugs.mojang.com/browse/MC-244694](https://bugs.mojang.com/browse/MC-244694)

## Report details

- **Mojira categories:** Sound
- **Project:** MC
- **Issue key:** MC-244694
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-12-04T12:01:01.858-0800
- **Updated:** 2025-03-25T12:36:57.417-0700
- **Resolution date:** 2022-10-26T03:09:52.786-0700
- **Affects versions:** 1.18; 1.18.1; 22w05a; 22w06a; 1.18.2 Pre-release 1; 1.18.2; 1.19; 1.19.1; 1.19.2
- **Fix versions:** 22w43a
- **Labels:** goat
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-244694.mp4; MC-244694.png

## Description

The Bug:
The sounds of goats stomping and ramming aren't controlled by the "Friendly Creatures" sound slider and are instead controlled by the "Hostile Creatures" sound slider.
This is a problem and inconsistency because all mobs except goats have all their sounds assigned to one sound slider and not multiple of them. For example, friendly bee sounds and angry bee sounds are all controlled by one sound slider, that being "Friendly Creatures". Below I've constructed a table of all goat sounds and their assigned sound sliders for a visual comparison of the issue.
Affected Sounds:
Before reading the table, please note the following:
- Words colored in GREEN reflect the correct behavior.

- Words colored in RED reflect the incorrect behavior.

Goat / Screaming Goat Sound
Current Assigned Sound Slider
Expected Assigned Sound Slider
Notes
Milking sounds
Players
Players
See  for an explanation as to why goat milking sounds should be controlled by the "Players" sound slider and not the "Friendly Creatures" sound slider.
Ambient sounds
Friendly Creatures
Friendly Creatures

Death sounds
Friendly Creatures
Friendly Creatures

Eating sounds
Friendly Creatures
Friendly Creatures

Hurt sounds
Friendly Creatures
Friendly Creatures

Stepping sounds
Friendly Creatures
Friendly Creatures

Long jump sounds
Friendly Creatures
Friendly Creatures

Stomping sounds
Hostile Creatures
Friendly Creatures

Ramming sounds
Hostile Creatures
Friendly Creatures

Steps to Reproduce:
- Navigate to the "Music & Sounds" settings menu.

- Turn the "Friendly Creatures" sound slider to "OFF".

- Turn every other sound slider to "100%".

- Exit this menu, summon a goat, and switch into survival mode.

- Make the gam ram you by altering its NBT data.

```
/execute as @e[type=minecraft:goat,limit=1,sort=nearest] run data modify entity @s Brain.memories."minecraft:ram_cooldown_ticks".value set value 1
```
- Listen closely as the goat stomps and rams you.

- Take note as to whether or not the sounds of goats stomping and ramming can be heard, (are controlled by the "Hostile Creatures" sound slider instead of the "Friendly Creatures" sound slider).

Observed Behavior:
The sounds of goats stomping and ramming aren't controlled by the "Friendly Creatures" sound slider and are instead controlled by the "Hostile Creatures" sound slider.
Expected Behavior:
The sounds of goats stomping and ramming would be controlled by the "Friendly Creatures" sound slider.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.18 using MCP-Reborn.
net.minecraft.world.entity.ai.behavior.PrepareRamNearestTarget.java

```
public class PrepareRamNearestTarget<E extends PathfinderMob> extends Behavior<E> {
   ...
                  $$0.playSound((Player)null, $$1, this.getPrepareRamSound.apply($$1), SoundSource.HOSTILE, 1.0F, $$1.getVoicePitch());
                  ...
```
net.minecraft.world.entity.ai.behavior.RamTarget.java

```
public class RamTarget<E extends PathfinderMob> extends Behavior<E> {
   ...
         $$0.playSound((Player)null, $$1, this.getImpactSound.apply($$1), SoundSource.HOSTILE, 1.0F, 1.0F);
      ...
```
If we look at the above classes, we can see that the sounds of goats stomping and ramming are sourced from SoundSource.HOSTILE, otherwise known as the "Hostile Creatures" sound slider.
Fix:
Simply changing where the sounds of goats stomping and ramming are sourced from to SoundSource.NEUTRAL (the "Friendly Creatures" sound slider) will resolve this problem.

## Comments (1)

### Comment 1: migrated (2021-12-04T12:01:01.858-0800)

This comment contained multiple image attachments (2), please login to view the attachments.
