# MC-266289: Could not save data raids.dat and random_sequences.dat

**Mojira URL:** [https://bugs.mojang.com/browse/MC-266289](https://bugs.mojang.com/browse/MC-266289)

## Report details

- **Mojira categories:** Raids; Save Data
- **Project:** MC
- **Issue key:** MC-266289
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2023-11-01T09:46:33.658-0700
- **Updated:** 2025-04-11T10:39:32.293-0700
- **Resolution date:** 2023-11-06T03:08:18.551-0800
- **Affects versions:** 23w44a
- **Fix versions:** 23w45a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 0
- **Issue links:** Duplicate:inward:MC-266330:Loot Tables reset when reloading world | Relates:outward:MC-266287:Can't load .dat and .nbt files (server list & saved hotbar) | Duplicate:inward:MC-266325:Map data erased on restart | Duplicate:inward:MC-266332:Data files like raids, scoreboards, maps, etc. are not saved if they do not already exist | Duplicate:inward:MC-266375:Newly made maps won't save and throw exceptions to the log, when reloading into the save all affected maps are permanently blank. | Duplicate:inward:MC-266398:Maps cannot save

## Description

How to reproduce (output log)
- Open a world, pause the game and look in the output log

-  Notice there are error messages about saving raids.dat and random_sequences.dat

How to reproduce (raids not saving)
- Find a village and give yourself the bad omen effect

```
/locate structure #minecraft:village
/effect give @s minecraft:bad_omen
```

- The raid boss bar appears

- Leave and reopen the world

-  Notice that the raid has vanished

Error message in the log

```
Could not save data cfi@342b30ad
java.nio.file.NoSuchFileException: C:\Users\Username\AppData\Roaming\.minecraft\saves\23w44a\DIM-1\data\raids.dat
	at java.base/sun.nio.fs.WindowsException.translateToIOException(WindowsException.java:85)
	at java.base/sun.nio.fs.WindowsException.rethrowAsIOException(WindowsException.java:103)
	at java.base/sun.nio.fs.WindowsException.rethrowAsIOException(WindowsException.java:108)
	at java.base/sun.nio.fs.WindowsFileSystemProvider.newByteChannel(WindowsFileSystemProvider.java:236)
	at java.base/java.nio.file.spi.FileSystemProvider.newOutputStream(FileSystemProvider.java:484)
	at java.base/java.nio.file.Files.newOutputStream(Files.java:228)
	at sq.a(SourceFile:73)
	at eec.a(SourceFile:45)
	at een.b(SourceFile:122)
	at java.base/java.util.HashMap.forEach(HashMap.java:1421)
	at een.a(SourceFile:120)
	at ami.au(SourceFile:822)
	at ami.a(SourceFile:804)
	at net.minecraft.server.MinecraftServer.a(SourceFile:541)
	at net.minecraft.server.MinecraftServer.b(SourceFile:565)
	at gfy.a(SourceFile:92)
	at net.minecraft.server.MinecraftServer.w(SourceFile:682)
	at net.minecraft.server.MinecraftServer.a(SourceFile:269)
	at java.base/java.lang.Thread.run(Thread.java:833)
```

## Comments (1)

### Comment 1: migrated (2023-11-01T13:31:39.763-0700)

I'd suggest closing this as duplicate instead, it's caused by the same bit of code shown in that report.
