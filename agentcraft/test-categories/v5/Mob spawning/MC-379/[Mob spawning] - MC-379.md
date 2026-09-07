# MC-379: spawn-animals and spawn-npcs=false removes all villagers and prevents summoning new mobs

**Mojira URL:** [https://bugs.mojang.com/browse/MC-379](https://bugs.mojang.com/browse/MC-379)

## Report details

- **Mojira categories:** Mob spawning
- **Project:** MC
- **Issue key:** MC-379
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2012-10-25T00:55:35.504-0700
- **Updated:** 2025-04-26T01:53:41.412-0700
- **Resolution date:** 2024-09-03T12:25:45.122-0700
- **Affects versions:** Minecraft 1.4.2; 20w14a; 1.16.3; 21w05b; 21w06a; 21w07a; 21w08a; 21w08b; 21w10a; 21w11a; 21w13a; 21w14a; 21w15a; 21w16a; 21w17a; 21w18a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17 Pre-release 2; 1.17 Pre-release 3; 1.17 Pre-release 4; 1.17 Pre-release 5; 1.17; 1.17.1; 21w37a; 21w38a; 21w39a; 21w40a; 21w41a; 21w43a; 1.18; 1.18.1; 22w06a; 1.18.2; 22w13a; 22w16b; 1.19 Pre-release 4; 1.19.3; 23w03a; 23w04a; 1.20.4; 24w12a
- **Fix versions:** 24w33a
- **Area:** Platform
- **Labels:** npc; server; villager
- **Watchers:** 1
- **Attachments:** 0
- **Issue links:** Duplicate:inward:MC-63676:summon does not override server.properties with  spawn-animals and spawn-npcs=false | Duplicate:inward:MC-52087:SMP - Passive Mobs (Animals) can't be spawned with spawn egg if spawn-animals=false | Duplicate:inward:MC-20766:Horses despawning immediately after spawning

## Description

Setting spawn-npcs=false in server.properties disables villagers completely
Setting spawn-animals=false prevents any mob from being spawned by commands or mob spawners.
What I expected to happen was...
Villagers and animals to stop naturally spawning.
Mobs to still be allowed to be summoned via commands
What actually happened was...
ALL Villagers, including pre-existing ones in the world, or ones newly placed via spawn eggs, disappear instantly.
Steps to Reproduce:
- Run a server

- Change server.properties to:

```
spawn-npcs=false
spawn-animals=false
spawn-monsters=false
```

- Join the server and execute the following commands

```
/summon villager
/summon wolf
/summon zombie
```

With difficulty on non-peaceful, you can see the Zombie summons fine.  But the Villager and Wolf do not stay in the world.
For custom maps, commands should override any server.properties as it does with hostile mobs.

## Comments (13)

### Comment 1: migrated (2012-10-25T06:25:57.258-0700)

The option functions as intended. It disables the mob completely. This is how the other mobs a work as well.

### Comment 2: migrated (2012-10-25T06:38:44.625-0700)

Even if it is intended, the option name is misleading - it should be enable-npcs, not spawn-npcs.

### Comment 3: migrated (2012-11-06T09:20:57.915-0800)

Other settings named along the same lines (spawn-animals, spawn-monsters) works the same way.

### Comment 4: migrated (2021-02-04T10:59:30.758-0800)

Affects 21w05b

### Comment 5: migrated (2021-07-12T17:52:15.572-0700)

I experience the same as OP where spawn-monsters still allows hostile mobs to exist in the world while spawn-npcs and spawn-animals immediately delete their respective entities. There is definitely unintentional behavior going on here. Did these options all get added in the same update?

### Comment 6: migrated (2021-09-05T19:42:23.490-0700)

uhhhhh
how to spawn a mob when spawn-monsters off?
I don't want natural generated mobs, just custom ones

### Comment 7: migrated (2021-09-05T23:56:36.753-0700)

/summon or spawn egg.

### Comment 8: Brain81505 (2023-01-14T06:11:21.146-0800)

Can confirm in 1.19.3

### Comment 9: Brain81505 (2023-01-18T06:23:56.212-0800)

Can confirm in 23w03a

### Comment 10: Brain81505 (2023-01-24T23:19:43.731-0800)

Can confirm in 23w04a

### Comment 11: Brain81505 (2023-02-01T08:04:05.913-0800)

Can confirm in 23w06a

### Comment 12: Brain81505 (2023-07-05T08:53:13.375-0700)

Can confirm in 1.20.1

### Comment 13: migrated (2024-09-03T12:21:52.282-0700)

Wait what....
You resolved spawn-animals bug option by just removing the feature altogether?
We have been using this feature for 10+ years. How would we disable animals now?
