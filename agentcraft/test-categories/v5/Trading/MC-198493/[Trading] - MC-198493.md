# MC-198493: Villagers lose their discounts when relogging while it is a zombie villager

**Mojira URL:** [https://bugs.mojang.com/browse/MC-198493](https://bugs.mojang.com/browse/MC-198493)

## Report details

- **Mojira categories:** Trading
- **Project:** MC
- **Issue key:** MC-198493
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2020-08-20T08:49:43.465-0700
- **Updated:** 2025-04-30T06:26:06.199-0700
- **Resolution date:** 2022-11-04T04:41:54.441-0700
- **Affects versions:** 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4 Pre-release 1; 1.16.4 Pre-release 2; 1.16.4 Release Candidate 1; 1.16.4; 20w45a; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w08a; 21w08b; 21w10a; 21w11a; 21w13a; 21w14a; 21w15a; 21w16a; 21w17a; 21w18a; 1.17; 1.17.1; 1.18.1
- **Fix versions:** 22w43a
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** After turning into zombie villager and relogging.png; Before relogging.png; MC-198493.mp4

## Description

The bug
When you cure a zombie villager to get discounts, and then turn him back into a zombie villager and then relog and cure him again, it will lose the discounts. They only disappear upon relogging when he is a zombie villager.
How to reproduce
- Spawn a villager and make it link to a work station

- Make sure to play on hard difficulty

- Spawn a zombie to turn him into a zombie villager

- Cure him

- Use this to command to speed up the process:

```
/execute as @e[type=minecraft:zombie_villager,distance=..20] run data merge entity @s {ConversionTime:0}
```

- Turn him back into a zombie villager

- Relog

- Cure him again and use this command:

```
/execute as @e[type=minecraft:zombie_villager,distance=..20] run data merge entity @s {ConversionTime:0}
```
 The prices will be as they were before, because he lost all of its discounts and then got one single discount through the curing process.

## Comments (7)

### Comment 1: migrated (2020-08-20T08:49:43.465-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: markderickson (2020-09-11T10:15:02.795-0700)

Hi there!
I can confirm.

### Comment 3: migrated (2021-04-14T15:27:20.695-0700)

I think that this issue and  are related. Can someone add "related to" or "duplicat"?

### Comment 4: migrated (2022-05-14T21:23:49.695-0700)

This issue and  are duplicates. Both issues are saying zombie villagers lose their discount info when unloaded and reloaded. They are just saying it in different ways. I think discount info should be in the zombie villagers nbt tags.

### Comment 5: SuperLlama88888 (2022-07-13T00:07:50.881-0700)

Can confirm in Windows 10 1.19.20.
Villagers, after being cured either:
a) Do not provide a discount at all;
b) Provide a discount, but do not provide minor discounts for the curing of other villagers; or
c) Provide a discount, provide one or two minor discounts for the curing of other villagers, then do not provide any additional minor discounts for the curing of other villagers.
This can be really frustrating for new players, as they would waste a golden apple and a splash potion.

### Comment 6: migrated (2022-10-18T05:48:53.728-0700)

Took a look at the code for this bug. I found that the Gossips data for a zombie villager is being saved, as a List (nbt type 9) of Compounds (nbt type 10), in the entities/r.x.z.mca file.
But the code for reading the Gossips data in `net.minecraft.world.entity.monster.ZombieVillager` does not read it back correctly. That code looks like this:

```if (compoundTag.contains("Gossips", 10)) {
            this.gossips = compoundTag.getList("Gossips", 10);
        }```
Or in English, "if it contains a Gossips tag that is a Compound, read a List of Compounds from it".
That code should look like this instead:

```if (compoundTag.contains("Gossips", 9)) {
            this.gossips = compoundTag.getList("Gossips", 10);
        }```

### Comment 7: winauer (2022-10-29T04:19:43.918-0700)

I think this is a duplicate of MC-183977, in which case that report should be closed as Resolved too.
