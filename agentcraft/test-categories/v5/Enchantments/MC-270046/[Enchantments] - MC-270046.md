# MC-270046: Mace's unique enchant is ineffective or no further effect if the level higher than max level, and causes error to be logged for wind burst

**Mojira URL:** [https://bugs.mojang.com/browse/MC-270046](https://bugs.mojang.com/browse/MC-270046)

## Report details

- **Mojira categories:** Enchantments
- **Project:** MC
- **Issue key:** MC-270046
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-03-28T05:09:04.877-0700
- **Updated:** 2025-04-29T09:58:54.754-0700
- **Resolution date:** 2024-04-16T07:47:37.047-0700
- **Affects versions:** 24w13a; 24w14a
- **Fix versions:** 1.20.5 Pre-Release 1
- **Area:** Expansion B
- **Labels:** breach; density; mace; wind_burst
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** wind burst lvl3.mp4; wind burst lvl4.mp4
- **Issue links:** Duplicate:inward:MC-270212:The new enchantments do not work when used beyond their max levels | Duplicate:inward:MC-270407:Wind Burst levels above 3 have no effect | Relates:inward:MC-270004:Giving yourself an item with a Wind Burst enchantment level higher than 3, then hitting certain entities crashes the game

## Description

The bug
Using an item with a higher than default level of mace's unique enchant does not work as expected. Wind burst also causes an error to be logged.
To reproduce
- Enter the following command in the chat:

```
/give @s mace[minecraft:enchantments={levels:{'wind_burst':4}}]
```

```
/give @s mace[minecraft:enchantments={levels:{'density':6}}]
```

```
/give @s mace[minecraft:enchantments={levels:{'breach':5}}]
```

- Hold the mace given by these commands in main hand.

- Hit a mob or entity (except players and other entities which crash the game - see MC-270004) while falling from high enough to smash.

Observed result
For wind burst level 4, there is no Wind Burst sound, no gust particles, and you won't be launched upward.
The following is written to log:

```
[23:06:04] [Server thread/ERROR]: Failed to handle packet agy@3b74fb31, suppressing error
java.lang.ArrayIndexOutOfBoundsException: Index 3 out of bounds for length 3
	at czq.c(SourceFile:43) ~[24w13a.jar:?]
	at cza.a(SourceFile:150) ~[24w13a.jar:?]
	at clw.e(SourceFile:1361) ~[24w13a.jar:?]
	at aqn.e(SourceFile:1702) ~[24w13a.jar:?]
	at arm$1.a(SourceFile:1633) ~[24w13a.jar:?]
	at agy$1.a(SourceFile:174) ~[24w13a.jar:?]
	at agy.a(SourceFile:74) ~[24w13a.jar:?]
	at arm.a(SourceFile:1594) ~[24w13a.jar:?]
	at agy.a(SourceFile:61) ~[24w13a.jar:?]
	at agy.a(SourceFile:15) ~[24w13a.jar:?]
	at zh.a(SourceFile:24) ~[24w13a.jar:?]
	at alh.run(SourceFile:18) ~[24w13a.jar:?]
	at bok.d(SourceFile:162) ~[24w13a.jar:?]
	at boo.d(SourceFile:23) ~[24w13a.jar:?]
	at net.minecraft.server.MinecraftServer.b(SourceFile:837) ~[24w13a.jar:?]
	at net.minecraft.server.MinecraftServer.d(SourceFile:166) ~[24w13a.jar:?]
	at bok.A(SourceFile:136) ~[24w13a.jar:?]
	at net.minecraft.server.MinecraftServer.bt(SourceFile:819) ~[24w13a.jar:?]
	at net.minecraft.server.MinecraftServer.A(SourceFile:813) ~[24w13a.jar:?]
	at bok.bz(SourceFile:121) ~[24w13a.jar:?]
	at net.minecraft.server.MinecraftServer.v_(SourceFile:787) ~[24w13a.jar:?]
	at net.minecraft.server.MinecraftServer.y(SourceFile:692) ~[24w13a.jar:?]
	at net.minecraft.server.MinecraftServer.a(SourceFile:272) ~[24w13a.jar:?]
	at java.base/java.lang.Thread.run(Thread.java:833) [?:?]
```
Density level 6 does the same damage as a normal mace.
For breach levels above level 4, they act just like Breach Level 4.

## Comments (5)

### Comment 1: migrated (2024-03-28T05:09:04.877-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: migrated (2024-04-01T11:07:17.154-0700)

Also affects density levels above level 5. For breach levels above 4, it acts just like breach 4

### Comment 3: migrated (2024-04-11T04:54:27.170-0700)

This seems to be fixed in 1.20.5 Pre Release 1, at least for Wind Burst and Density.

### Comment 4: migrated (2024-04-12T00:25:33.856-0700)

DOOMHYDRA9999, Thank you. This is fixed in 1.20.5 Pre Release 1 for Wind Burst, in 24w14a for Density and Breach.

### Comment 5: CreeperFriend (2024-04-12T09:31:25.569-0700)

Btw, it is not needed that you add the (expected) resolution to the issue summary. Once the mods see the comments, they will resolve it anyway with the proper resolution.
