# MC-239900: Upgrading custom world to 21w43a ignores min_y and height

**Mojira URL:** [https://bugs.mojang.com/browse/MC-239900](https://bugs.mojang.com/browse/MC-239900)

## Report details

- **Mojira categories:** Custom Worlds
- **Project:** MC
- **Issue key:** MC-239900
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2021-10-27T17:40:40.803-0700
- **Updated:** 2025-03-25T12:37:07.086-0700
- **Resolution date:** 2021-11-22T09:01:31.253-0800
- **Affects versions:** 21w43a
- **Fix versions:** 1.18 Pre-release 6
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 21w42a-height4064.json; image-2021-10-28-02-40-21-449.png

## Description

The bug
If you open this custom world
 in 21w43a after you generated it in 21w42a results in all terrain below -64 disappearing and any blocks being placed above 320 / max_y.
How to reproduce
- Open Minecraft in 21w42a

- Create a world using the custom world settings in

-  Enter spectator mode, and observe that the world bottom is lower than Y=-64 and world top is higher than Y=320 (e.g. by placing a block above it)

- Open Minecraft in 21w43a

- Play the world you created previously to upgrade it
 The terrain previously generated below Y=-64 has been removed, and the bottom of the world is now found at Y=-64.
 Blocks above Y=320 are removed, and the top of the world is now found at Y=320

Expected behaviour
- The upgraded world would not have all terrain below Y=-64 and above Y=320 removed, the dimension's bounding boxes / min_y and height should stay unchanged.

Error

```
Couldn't load chunk [11, -4]
java.lang.ArrayIndexOutOfBoundsException: Index 58 out of bounds for length 24
	at cow.a(SourceFile:350)
	at cow.a(SourceFile:290)
	at cps.a(SourceFile:202)
	at abu.m(SourceFile:579)
	at java.base/java.util.concurrent.CompletableFuture$AsyncSupply.run(CompletableFuture.java:1764)
	at atg.c(SourceFile:151)
	at acf$b.c(SourceFile:534)
	at atg.y(SourceFile:125)
	at acf$b.y(SourceFile:543)
	at acf.d(SourceFile:278)
	at net.minecraft.server.MinecraftServer.be(SourceFile:763)
	at net.minecraft.server.MinecraftServer.y(SourceFile:751)
	at atg.c(SourceFile:134)
	at net.minecraft.server.MinecraftServer.x(SourceFile:736)
	at net.minecraft.server.MinecraftServer.b(SourceFile:497)
	at net.minecraft.server.MinecraftServer.f_(SourceFile:329)
	at fcg.e(SourceFile:72)
	at net.minecraft.server.MinecraftServer.w(SourceFile:655)
	at net.minecraft.server.MinecraftServer.a(SourceFile:269)
	at java.base/java.lang.Thread.run(Thread.java:831)
```

## Comments (2)

### Comment 1: migrated (2021-10-27T17:40:40.803-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: slicedlime (2021-11-22T09:01:31.253-0800)

Note that upgrading experimental worlds is not supported. The fix here is simply that the game is now slightly better at telling you so.
