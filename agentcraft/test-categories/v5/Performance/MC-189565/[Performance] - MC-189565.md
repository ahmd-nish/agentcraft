# MC-189565: Some entities do not render inside of spawners and producing error log spam in console, potentially causing lag

**Mojira URL:** [https://bugs.mojang.com/browse/MC-189565](https://bugs.mojang.com/browse/MC-189565)

## Report details

- **Mojira categories:** Performance; Rendering
- **Project:** MC
- **Issue key:** MC-189565
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2020-06-13T23:47:04.987-0700
- **Updated:** 2025-04-30T07:00:54.911-0700
- **Resolution date:** 2022-08-30T08:38:56.131-0700
- **Affects versions:** 1.16 Pre-release 5; 1.16 Pre-release 6; 1.16 Pre-release 7; 1.16 Pre-release 8; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w27a; 20w28a; 20w30a; 1.16.2 Pre-release 1; 1.16.2; 1.16.4; 1.16.5
- **Fix versions:** 20w45a
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** Elder Guardian.png; Zombified Piglin.png
- **Issue links:** Relates:inward:MC-199429:Evoker Fangs don't render in Spawners

## Description

Mob Spawners do not render a "mini" mob visual for the following entities:
- Bee

- Enderman

- Polar Bear

- Wolf

- Zombified Piglin

- Evoker Fangs

See attached images for expected (Elder Guardian) vs unexpected (Zombified Piglin). When the game attempts to render them but fails, it also produces an error message in the console over and over again, which can potentially cause a lot of lag in the world, especially when lots of spawners are used.

```
[01:00:15] [Render thread/WARN]: Exception loading entity:
s: Loading entity NBT
	at aol.f(SourceFile:1642) ~[1.16-pre5.jar:?]
	at aop.a(SourceFile:467) ~[1.16-pre5.jar:?]
	at aop$$Lambda$4201/93583133.accept(Unknown Source) ~[?:?]
	at v.a(SourceFile:401) ~[1.16-pre5.jar:?]
	at aop.a(SourceFile:466) ~[1.16-pre5.jar:?]
	at aop.b(SourceFile:529) [1.16-pre5.jar:?]
	at aop.a(SourceFile:510) [1.16-pre5.jar:?]
	at bpc.d(SourceFile:256) [1.16-pre5.jar:?]
	at eei.a(SourceFile:22) [1.16-pre5.jar:?]
	at eei.a(SourceFile:12) [1.16-pre5.jar:?]
	at edw.a(SourceFile:107) [1.16-pre5.jar:?]
	at edw.b(SourceFile:96) [1.16-pre5.jar:?]
	at edw$$Lambda$4990/1816104835.run(Unknown Source) [1.16-pre5.jar:?]
	at edw.a(SourceFile:128) [1.16-pre5.jar:?]
	at edw.a(SourceFile:96) [1.16-pre5.jar:?]
	at ebx.a(SourceFile:1236) [1.16-pre5.jar:?]
	at ebs.a(SourceFile:717) [1.16-pre5.jar:?]
	at ebs.a(SourceFile:540) [1.16-pre5.jar:?]
	at dlx.e(SourceFile:1021) [1.16-pre5.jar:?]
	at dlx.d(SourceFile:654) [1.16-pre5.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:215) [1.16-pre5.jar:?]
Caused by: java.lang.ClassCastException: dym cannot be cast to zc
	at ayk.a(SourceFile:260) ~[1.16-pre5.jar:?]
	at aol.f(SourceFile:1633) ~[1.16-pre5.jar:?]
	... 20 more
```
What I expected to happen was...:
A "mini" version of the mob to be rendered in the middle of the spawner cube.
What actually happened was...:
No "mini" version of the mob is rendered inside the cage.
Steps to Reproduce:
- Place down a spawner

- Modify the spawner's block data to the desired mob (can be done through commands or by right-clicking on the cage with the desired mob spawn egg).

Note: The spawner does spawn the desired mob. The issue is only visual – you cannot tell what kind of spawner it is just by looking at it.
Code analysis
See this comment.

## Comments (14)

### Comment 1: migrated (2020-06-13T23:47:04.987-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: tryashtar (2020-06-14T00:00:54.350-0700)

Confirmed, also the log is spammed with this:

```[01:00:15] [Render thread/WARN]: Exception loading entity:
s: Loading entity NBT
	at aol.f(SourceFile:1642) ~[1.16-pre5.jar:?]
	at aop.a(SourceFile:467) ~[1.16-pre5.jar:?]
	at aop$$Lambda$4201/93583133.accept(Unknown Source) ~[?:?]
	at v.a(SourceFile:401) ~[1.16-pre5.jar:?]
	at aop.a(SourceFile:466) ~[1.16-pre5.jar:?]
	at aop.b(SourceFile:529) [1.16-pre5.jar:?]
	at aop.a(SourceFile:510) [1.16-pre5.jar:?]
	at bpc.d(SourceFile:256) [1.16-pre5.jar:?]
	at eei.a(SourceFile:22) [1.16-pre5.jar:?]
	at eei.a(SourceFile:12) [1.16-pre5.jar:?]
	at edw.a(SourceFile:107) [1.16-pre5.jar:?]
	at edw.b(SourceFile:96) [1.16-pre5.jar:?]
	at edw$$Lambda$4990/1816104835.run(Unknown Source) [1.16-pre5.jar:?]
	at edw.a(SourceFile:128) [1.16-pre5.jar:?]
	at edw.a(SourceFile:96) [1.16-pre5.jar:?]
	at ebx.a(SourceFile:1236) [1.16-pre5.jar:?]
	at ebs.a(SourceFile:717) [1.16-pre5.jar:?]
	at ebs.a(SourceFile:540) [1.16-pre5.jar:?]
	at dlx.e(SourceFile:1021) [1.16-pre5.jar:?]
	at dlx.d(SourceFile:654) [1.16-pre5.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:215) [1.16-pre5.jar:?]
Caused by: java.lang.ClassCastException: dym cannot be cast to zc
	at ayk.a(SourceFile:260) ~[1.16-pre5.jar:?]
	at aol.f(SourceFile:1633) ~[1.16-pre5.jar:?]
	... 20 more```

### Comment 3: migrated (2020-06-20T15:31:39.463-0700)

Well, this bug appears for all mobs that have their readAdditionalSaveData(CompoundTag) method overriden + a call to readPersistentAngerSaveData which casts the Level to a ServerLevel. As renderers are client sided executing this method's code causes a ClassCastException (ClientLevel cannot be cast to ServerLevel).
A simple server side check should fix the bug.

### Comment 4: Hound4oo4 (2020-07-23T12:12:37.920-0700)

can confirm for 20w30a

### Comment 5: anthony cicinelli (2020-07-25T20:08:41.818-0700)

Evoker Fangs & Experience Orbs are also affected

### Comment 6: migrated (2020-08-19T10:21:03.641-0700)

@Algeseven – could you possibly clarify in which class the server-side check needs to be implemented? I've been patiently waiting for a fix for this but it seems like we're not getting one until 1.17 which is unacceptable in my opinion. I'm trying to create a patch to fix this myself as some features on my server depend on some of these spawners, and I'm having trouble determining where this check should go. Thanks in advance.

### Comment 7: migrated (2020-08-19T13:43:00.599-0700)

@Mike - A modder named Draylar made a mod on fabric to patch this bug. Using mixins, he added a check to make sure the world is not a client world before angerFromTag method gets called (yarn mapping names)
You can either use his mod or check his code to create a fix for your server. As for Mojang devs reading this, this is all that is needed to fix the bug and so far, I have not seen any side-effects of this patch as I use it with my own mods as well.
https://github.com/Draylar/angerable-patch

### Comment 8: mgatland (2020-09-01T04:19:28.313-0700)

I have fixed this but the fix does not include Evoker Fangs or Experience Orbs, which have a different cause and do not cause log spam. Please raise a separate issue for them.

### Comment 9: anthony cicinelli (2020-09-01T07:16:21.565-0700)

I have created a report for Evoker Fangs. See  Experiance Orbs are not affected but just really small. See:

### Comment 10: MODKILLER1001 (2020-10-15T08:16:47.635-0700)

Issue still happens in 1.16.4 pre 1

### Comment 11: migrated (2020-10-30T19:20:35.972-0700)

This should be fixed for 1.16.4, not 1.17. It is critical.

### Comment 12: migrated (2020-11-10T22:36:35.957-0800)

This bug still affects release 1.16.4 (vanilla client and server) using the following custom spawner:

```/setblock ~ ~-1 ~ minecraft:spawner\{SpawnData:{id:iron_golem},SpawnCount:3,SpawnRange:4,RequiredPlayerRange:25,Delay:20,MinSpawnDelay:9600,MaxSpawnDelay:9600,MaxNearbyEntities:25} replace```
Spamming the client logs with thousands of warnings about:

```Exception loading entity: u: Loading entity NBT at aqa.f(SourceFile:1663) at aqe.a(SourceFile:473) at x.a(SourceFile:402) at aqe.a(SourceFile:472) at aqe.b(SourceFile:535) at aqe.a(SourceFile:516) at bqz.d(SourceFile:254) at ecp.a(SourceFile:22) at ecp.a(SourceFile:12) at ecd.a(SourceFile:107) at ecd.b(SourceFile:96) at ecd.a(SourceFile:128) at ecd.a(SourceFile:96) at eae.a(SourceFile:1260) at dzz.a(SourceFile:727) at dzz.a(SourceFile:546) at djz.e(SourceFile:1048) at djz.e(SourceFile:681) at net.minecraft.client.main.Main.main(SourceFile:215) Caused by: java.lang.ClassCastException: class dwt cannot be cast to class aag (dwt and aag are in unnamed module of loader 'app') at bai.a(SourceFile:170) at aqa.f(SourceFile:1654) ... 18 more```
As a consequence, user logs can grow very large.

### Comment 13: migrated (2021-01-27T22:46:36.833-0800)

Still affects 1.16.5

### Comment 14: pokechu22 (2021-01-27T23:55:13.345-0800)

Added, but note that 20w45a is a 1.17 snapshot, and fixes from those aren't present in 1.16.5; that you can reproduce in 1.16.5 doesn't mean that the bug isn't fixed.
