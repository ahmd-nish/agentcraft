# MC-303704: Statistics are no longer saved if the folder they would save into doesn't exist yet

**Mojira URL:** [https://bugs.mojang.com/browse/MC-303704](https://bugs.mojang.com/browse/MC-303704)

## Report details

- **Mojira categories:** Save Data; Statistics
- **Project:** MC
- **Issue key:** MC-303704
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2025-10-28T12:02:52.608-0700
- **Updated:** 2026-03-11T03:44:26.676-0700
- **Resolution date:** 2025-10-30T04:25:55.646-0700
- **Affects versions:** 25w44a
- **Fix versions:** 25w45a
- **Area:** Platform HC
- **Votes:** 2
- **Watchers:** 0
- **Attachments:** 1
- **Attachment filenames:** latest.log

## Description

Minecraft no longer saves player stats to the world folder in newly created worlds, resulting in them being reset every time the player joins the world. This affects both servers and singleplayer worlds.
Steps to reproduce:
- Create a new world

- Break a few blocks

- Check statistics, broken blocks should be listed there

- Leave world and open it again

- Check statistics, previous stats are now gone

The following related error is logged when running “/save-all”:

```
[19:56:17] [Server thread/ERROR]: Couldn't save stats to ./world/stats/a0798455-f768-4abe-b2fc-da8478d04e02.json
java.nio.file.NoSuchFileException: ./world/stats/a0798455-f768-4abe-b2fc-da8478d04e02.json
	at java.base/sun.nio.fs.UnixException.translateToIOException(UnixException.java:92)
	at java.base/sun.nio.fs.UnixException.rethrowAsIOException(UnixException.java:106)
	at java.base/sun.nio.fs.UnixException.rethrowAsIOException(UnixException.java:111)
	at java.base/sun.nio.fs.UnixFileSystemProvider.newByteChannel(UnixFileSystemProvider.java:261)
	at java.base/java.nio.file.spi.FileSystemProvider.newOutputStream(FileSystemProvider.java:482)
	at java.base/java.nio.file.Files.newOutputStream(Files.java:228)
	at java.base/java.nio.file.Files.newBufferedWriter(Files.java:3001)
	at bdg.a(SourceFile:96)
	at bbz.a(SourceFile:310)
	at bbz.h(SourceFile:635)
	at net.minecraft.server.MinecraftServer.b(SourceFile:656)
	at aqi.a(SourceFile:32)
	at aqi.b(SourceFile:20)
	at com.mojang.brigadier.context.ContextChain.runExecutable(ContextChain.java:73)
	at hr.a(SourceFile:29)
	at hr.execute(SourceFile:13)
	at hm.a(SourceFile:8)
	at he.a(SourceFile:8)
	at hi.a(SourceFile:106)
	at eg.a(SourceFile:430)
	at eg.a(SourceFile:362)
	at eg.a(SourceFile:348)
	at arz.bA(SourceFile:449)
	at arz.K(SourceFile:439)
	at net.minecraft.server.MinecraftServer.c(SourceFile:1154)
	at net.minecraft.server.MinecraftServer.a(SourceFile:1026)
	at arz.a(SourceFile:318)
	at net.minecraft.server.MinecraftServer.A(SourceFile:781)
	at net.minecraft.server.MinecraftServer.a(SourceFile:303)
	at java.base/java.lang.Thread.run(Thread.java:1583)
```

The underlying issue seems to be that Minecraft no longer creates the “stats“ folder inside the world folder. This causes an error when trying to create a file inside the nonexistent folder.

## Comments (4)

### Comment 1: KurtThiemann (2025-10-28T12:02:53.242-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: KurtThiemann (2025-10-28T12:19:44.811-0700)

Full deobfuscated log:

### Comment 3: 216fd76053f04a95bba4a54794b9926b (2025-10-28T13:20:41.032-0700)

Can confirm

### Comment 4: KurtThiemann (2025-10-29T02:57:49.860-0700)

Not sure who changed the title, but the new one is incorrect. Statistics are not saved if the “stats“ folder does not exist yet. Whether the specific stats file already exists does not matter.
