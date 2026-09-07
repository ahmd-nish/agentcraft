# MC-64087: Revengeful zombies / Zombie reinforcements try to attack players in Creative mode

**Mojira URL:** [https://bugs.mojang.com/browse/MC-64087](https://bugs.mojang.com/browse/MC-64087)

## Report details

- **Mojira categories:** Mob behaviour
- **Project:** MC
- **Issue key:** MC-64087
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2014-07-27T19:46:06.458-0700
- **Updated:** 2026-03-22T09:29:57.678-0700
- **Resolution date:** 2025-12-09T09:05:44.343-0800
- **Affects versions:** Minecraft 14w30c; Minecraft 14w31a; Minecraft 14w32a; Minecraft 1.8; Minecraft 1.8.1; Minecraft 1.8.8; Minecraft 15w32b; Minecraft 15w35e; Minecraft 15w39a; Minecraft 15w47c; Minecraft 15w49b; Minecraft 1.8.9; Minecraft 15w50a; Minecraft 16w05b; Minecraft 1.10.2; Minecraft 16w41a; Minecraft 16w42a; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 17w17b; Minecraft 1.12 Pre-Release 6; Minecraft 1.12.1; Minecraft 1.12.2; Minecraft 17w43a; Minecraft 17w43b; Minecraft 17w45b; Minecraft 17w46a; Minecraft 18w03b; Minecraft 18w07c; Minecraft 18w08b; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 1.14 Pre-Release 5; 1.15.2; 20w12a; 20w13b; 1.16.4; 20w45a; 1.16.5; 21w07a; 21w17a; 1.17.1; 21w39a; 1.18 Pre-release 6; 1.18 Release Candidate 1; 1.18.1 Release Candidate 2; 1.18.1; 1.18.2; 22w19a; 1.19; 1.19.2; 1.19.3; 23w06a; 1.20.1; 1.20.4; 1.21.10; 25w45a
- **Fix versions:** Minecraft 14w32d; 26.1 Snapshot 1
- **Area:** Gameplay
- **Game mode:** Creative
- **Labels:** attack; reinforcement; zombie
- **Votes:** 1
- **Watchers:** 1
- **Attachments:** 7
- **Attachment filenames:** 2014-10-09_21.07.51.png; 2014-10-09_21.13.17.png; 2014-10-09_21.13.31.png; javaw 2014-07-30 16-56-19-40 (1).mp4; MC-64087.mp4; Sem título.jpg; Sem título2.jpg
- **Issue links:** Duplicate:inward:MC-176402:Zombified Piglins spawn recruitment zombies that pathfind towards the player when attacked by player in creative mode | Duplicate:inward:MC-175852:Zombie still spawn reinforcements even on Creative | Duplicate:inward:MC-135864:Reinforcement Zombies summoned by hurting Zombies try to attack creative mode players | Duplicate:inward:MC-109146:Natural spawned zombies will sometimes go for player in creative if near | Duplicate:inward:MC-96632:Reinforcement zombies will attack creative mode player. | Relates:inward:MC-15112:Zombies retaliate when only hitten in Creative Mode | Duplicate:inward:MC-93951:Reneforcement Zombies still attack the player in Creative Mode (You Must Read Description) | Duplicate:inward:MC-93240:Zombie's still hostile if you turn from survival to creative | Duplicate:inward:MC-88102:Hostile Zombie In Creative? | Duplicate:inward:MC-87583:Reinforcement Zombie follows Creative Player | Duplicate:inward:MC-75400:Zombie reinforcements are hostile to creative players | Duplicate:inward:MC-48703:Social spawned zombie will pathfind to you even in creative | Duplicate:inward:MC-50868:Social zombies go after players in creative mode | Duplicate:inward:MC-75826:Zombie from Reinforcements becomes hostile | Duplicate:inward:MC-303302:Zombies summoned by reinforcements attempt to attack players in Creative mode. | Duplicate:inward:MC-303798:Zombies in reinforcement attempt to attack player in creative mode

## Description

What I expected to happen
Reinforcement zombies to not be hostile towards players in creative mode.
What actually happened
Reinforcement zombies try to attack the player who attacked the zombie spawning the reinforcement zombies even if the player is in creative mode.
Steps to reproduce
- Spawn 3 or more zombies close to each other, while in creative mode;

- Walk back a little, and switch to survival mode;

- Hit one zombie, and make sure they DON'T hurt you (important);

- Quickly switch to creative mode;

- Some zombies will be chasing you.

Steps to reproduce with commands
- Set your gamemode to Creative

- Set the difficulty to "Hard"

```
/difficulty hard
```

- Set the gamerule doMobSpawning to true if it is not already

```
/gamerule doMobSpawning true
```

- Set the time to "midnight" or make sure there is no light in the area around you

```
/time set midnight
```

- Summon a zombie using the following command

```
/summon minecraft:zombie ~ ~ ~ {Attributes:[{Base:1.0,Name:"zombie.spawn_reinforcements"}]}
```

- Hit the zombie a few times

- Search for the spawned reinforcement zombies, if there are no other zombies you can use the following command

```
/execute as @e[type=zombie,sort=nearest,distance=..40] run data merge entity @s {Glowing:1b}
```

Code analysis
Based on 1.11.2 decompiled using MCP 9.35 rc1
Either the method net.minecraft.entity.EntityLiving.setAttackTarget(EntityLivingBase) should not set players in Creative or Spectator mode as target or the method net.minecraft.entity.monster.EntityZombie.attackEntityFrom(DamageSource, float) should test if the player is in Creative mode.

## Comments (30)

### Comment 1: migrated (2014-07-27T19:46:06.458-0700)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: migrated (2014-07-30T12:49:56.834-0700)

Cannot reproduce.

### Comment 3: migrated (2014-07-30T12:52:37.900-0700)

Fine. I'll record.

### Comment 4: migrated (2014-07-30T13:07:49.587-0700)

Done.

### Comment 5: migrated (2014-08-11T17:27:41.108-0700)

Fixed on 14w32d.

### Comment 6: Sonicwave (2014-10-09T21:07:46.405-0700)

Regressed in 1.8 release. To reproduce (I think):
Spawn zombies behind you (20-30 blocks away)
Spawn zombies in front of you, go into survival and quickly punch them, and go back into Creative.
Hitting the zombie/other zombies or going into Spectator does not fix the issue, but logging out/back in does.

### Comment 7: Sonicwave (2014-11-24T21:39:02.886-0800)

Regression also occurs in 1.8.1.

### Comment 8: Sonicwave (2015-08-06T15:48:05.251-0700)

Confirmed in 15w32b. Simply attacking zombies in Creative (I used bow and arrows from a distance, but I think any attack should work) will cause hostile zombies to spawn.

### Comment 9: Sonicwave (2015-08-28T11:54:34.040-0700)

Confirmed for 15w35d and 15w35e (MC-87583).

### Comment 10: migrated (2015-09-19T08:31:25.844-0700)

Confirmed for 15w38b. They REALLY need to fix this...

### Comment 11: migrated (2015-12-15T08:29:25.375-0800)

Yeah, pretty minor bug (it's creative mode  . No big deal. They can't kill you)... but really random... confirmed for 15w50a.

### Comment 12: Sonicwave (2017-04-27T10:34:35.041-0700)

Confirmed for 17w17b.

### Comment 13: Sonicwave (2017-10-28T22:15:26.901-0700)

Confirmed for 1.12.2 and 18w07c.

### Comment 14: migrated (2018-09-02T06:34:28.405-0700)

Unable to reproduce for 1.13.1.

### Comment 15: migrated (2020-11-08T05:06:27.544-0800)

Affects 20w45a

### Comment 16: migrated (2020-11-08T14:47:04.209-0800)

This seems to be caused by .

### Comment 17: marcono1234 (2020-11-08T15:08:02.151-0800)

Only marked it as related because that report requires switching gamemodes which is not necessary here.

### Comment 18: Avoma (2021-02-19T03:58:50.532-0800)

Can confirm in 21w07a.

### Comment 19: Avoma (2021-02-20T09:15:10.528-0800)

I've attached an updated video which demonstrates this issue.

### Comment 20: Avoma (2021-04-29T00:39:54.914-0700)

Can confirm in 21w17a.

### Comment 21: migrated (2021-05-23T14:52:56.061-0700)

Can confirm for 1.16.5

### Comment 22: Avoma (2021-08-28T06:05:23.811-0700)

Can confirm in 1.17.1.

### Comment 23: Avoma (2021-10-03T01:52:12.476-0700)

Can confirm in 21w39a.

### Comment 24: Avoma (2021-12-14T09:05:06.363-0800)

Can confirm in 1.18.1.

### Comment 25: Avoma (2022-03-05T11:17:52.659-0800)

Can confirm in 1.18.2.

### Comment 26: Avoma (2022-06-13T08:21:05.546-0700)

Can confirm in 1.19.

### Comment 27: Avoma (2022-08-07T04:07:42.309-0700)

Can confirm in 1.19.2.

### Comment 28: migrated (2025-02-05T14:09:01.335-0800)

Can confirm in 1.21.4.

### Comment 29: himazinn_Japan (2025-02-05T23:34:59.465-0800)

Relates to .

### Comment 30: Willy (2025-10-19T09:51:13.618-0700)

Can confirm in 25w42a
