# MC-124365: Exiting world does not release file handle to zipped datapack / resourcepack

**Mojira URL:** [https://bugs.mojang.com/browse/MC-124365](https://bugs.mojang.com/browse/MC-124365)

## Report details

- **Mojira categories:** Data Packs; Save Data
- **Project:** MC
- **Issue key:** MC-124365
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2018-01-17T09:17:07.078-0800
- **Updated:** 2025-04-30T09:04:30.931-0700
- **Resolution date:** 2022-03-09T10:21:59.585-0800
- **Affects versions:** Minecraft 18w03b; Minecraft 18w20c; Minecraft 18w30b; Minecraft 18w31a; Minecraft 1.13.2; Minecraft 19w03c; 1.14.4; 19w42a; 1.15.2; 20w08a; 20w17a; 20w19a; 1.17.1
- **Fix versions:** 20w27a
- **Watchers:** 1
- **Attachments:** 0

## Description

open Minecraft
open a world that contains a zipped datapack in its datapacks directory
after world is loaded, save & exit back to title screen
in windows file explorer, navigate to datapacks directory and try to delete the .zip file of the datapack
EXPECTED:
file can be deleted
ACTUAL:
file cannot be deleted because it is still in use by java process (Minecraft sitting at title screen)
NOTES:
you can work around it by closing Minecraft, or by opening a different world (at which point MC seems to 'flush' its datapacks)
Ideally, Minecraft should only be using the file during load/reload - once loading is complete, it should release the file handle.  (for non-zip files, like functions in a datapack, you can delete each while the world is loaded)
Error 20w17a

```
Failed to delete world World
java.nio.file.FileSystemException: ###\saves\World\datapacks\my-datapack.zip: The process cannot access the file because it is being used by another process.

	at sun.nio.fs.WindowsException.translateToIOException(WindowsException.java:86)
	at sun.nio.fs.WindowsException.rethrowAsIOException(WindowsException.java:97)
	at sun.nio.fs.WindowsException.rethrowAsIOException(WindowsException.java:102)
	at sun.nio.fs.WindowsFileSystemProvider.implDelete(WindowsFileSystemProvider.java:269)
	at sun.nio.fs.AbstractFileSystemProvider.delete(AbstractFileSystemProvider.java:103)
	at java.nio.file.Files.delete(Files.java:1126)
	at czj$a$1.a(SourceFile:285)
	at czj$a$1.visitFile(SourceFile:280)
	at java.nio.file.Files.walkFileTree(Files.java:2670)
	at java.nio.file.Files.walkFileTree(Files.java:2742)
	at czj$a.f(SourceFile:280)
	at dsw$a.a(SourceFile:334)
	at dsw$a$$Lambda$4354/456574378.accept(Unknown Source)
	at dok.b(SourceFile:43)
	at dok$$Lambda$4355/1901085596.onPress(Unknown Source)
	at dmc.as_(SourceFile:20)
	at dlw.a(SourceFile:16)
	at dma.a(SourceFile:150)
	at dmz.a(SourceFile:27)
	at dks.b(SourceFile:86)
	at dks$$Lambda$2375/1247247257.run(Unknown Source)
	at dpj.a(SourceFile:416)
	at dks.a(SourceFile:86)
	at dks.c(SourceFile:150)
	at dks$$Lambda$2374/599726537.run(Unknown Source)
	at alp.execute(SourceFile:94)
	at dks.b(SourceFile:150)
	at dks$$Lambda$1747/1735688275.invoke(Unknown Source)
	at org.lwjgl.glfw.GLFWMouseButtonCallbackI.callback(GLFWMouseButtonCallbackI.java:36)
	at org.lwjgl.system.JNI.invokeV(Native Method)
	at org.lwjgl.glfw.GLFW.glfwPollEvents(GLFW.java:3101)
	at com.mojang.blaze3d.systems.RenderSystem.flipFrame(SourceFile:105)
	at dft.e(SourceFile:301)
	at dkr.e(SourceFile:1027)
	at dkr.d(SourceFile:630)
	at net.minecraft.client.main.Main.main(SourceFile:204)
```

## Comments (10)

### Comment 1: marcono1234 (2018-01-28T14:36:53.959-0800)

I can only speak about zipped resource packs, but they are closed when they are garbage collected (see net.minecraft.client.resources.FileResourcePack.finalize()). I am not sure if Minecraft really caches everything from data- and resourepacks. For example at least net.minecraft.client.gui.GuiWinGame appears to load the texts only when the GUI is displayed.

### Comment 2: migrated (2018-01-29T13:41:44.219-0800)

It seems to be that is makes the most sense for the game to load everything at once (to avoid blocking on disk I/O during gameplay at a later point in time), but I acknowledge that there are possible space-versus-time trade-offs here.

### Comment 3: migrated (2018-01-31T03:01:33.803-0800)

I have a feeling that Mojang isn't closing a zip stream. For regular resource packs, you can edit the files, but not a zip stream.

### Comment 4: migrated (2018-04-30T16:42:21.845-0700)

Also, they should probably extract everything from the Zipped resource pack into a temp dir. It will be much more efficient

### Comment 5: migrated (2018-07-31T15:53:03.280-0700)

18w30b seems to be affected. I had two Datapacks enabled in the world, then went to the title screen and I could only delete one.

### Comment 6: migrated (2018-08-01T08:08:56.393-0700)

18w31a is affected as well.

### Comment 7: migrated (2019-01-21T07:31:44.969-0800)

Confirmed for 19w03c. Just ran into it again while working on a data pack.

### Comment 8: Makzevu (2019-08-06T17:00:55.014-0700)

Confirmed for 1.14.4.
Leaving a world that has an active datapack then trying to delete it, through the game menu, tries 5 times before stopping.

### Comment 9: clamlol (2022-03-04T17:21:23.316-0800)

This appears to no longer be an issue in 1.18.2.
Also, my previous comment was incorrect- the issue I encountered in 1.17.1 (and still in 1.18.2) is separate and I'll make a new ticket for it shortly.

### Comment 10: Michael Wobst (2022-03-09T10:19:11.548-0800)

Actually this has been fixed in snapshot 20w27a. Unfortunately 1.17.1 can't be removed from the affected version list anymore.
