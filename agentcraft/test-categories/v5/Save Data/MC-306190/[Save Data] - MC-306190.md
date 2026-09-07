# MC-306190: The game closes when upgrading a world fails

**Mojira URL:** [https://bugs.mojang.com/browse/MC-306190](https://bugs.mojang.com/browse/MC-306190)

## Report details

- **Mojira categories:** Datafixer; Save Data
- **Project:** MC
- **Issue key:** MC-306190
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2026-02-03T10:35:06.647-0800
- **Updated:** 2026-03-11T03:56:50.347-0700
- **Resolution date:** 2026-03-03T04:06:38.968-0800
- **Affects versions:** 26.1 Snapshot 6; 26.1 Snapshot 7
- **Fix versions:** 26.1 Snapshot 11
- **Area:** Platform EC
- **Votes:** 5
- **Watchers:** 1
- **Attachments:** 0

## Description

The bug
When attempting to upgrade and backup a world fails, a toast briefly appears and then the game closes. This does not appear to be a crash, but an error is logged.
How to reproduce
- Take a world from 1.21.11

- Add a file to the world directory that’s not owned by your user (e.g. sudo touch test)

- Try to upgrade and open the world in-game

Expected results
Graceful error message that lets you go back, like the one that appears when your world has symlinks.
Observed result
The game instantly closes and logs the following error:

```
[11:33:19] [Worker-Main-10] [ERROR] net.minecraft.util.filefix.virtualfilesystem.exception.CowFSCreationException: Cannot build copy-on-write file system, missing write access for file: /home/.../minecraft/snapshots/saves/New World (39)/test
        at net.minecraft.util.filefix.virtualfilesystem.CopyOnWriteFileSystem$1.checkAttributes(CopyOnWriteFileSystem.java:101)
        at net.minecraft.util.filefix.virtualfilesystem.CopyOnWriteFileSystem$1.visitFile(CopyOnWriteFileSystem.java:74)
        at net.minecraft.util.filefix.virtualfilesystem.CopyOnWriteFileSystem$1.visitFile(CopyOnWriteFileSystem.java:71)
        at java.base/java.nio.file.Files.walkFileTree(Files.java:2543)
        at java.base/java.nio.file.Files.walkFileTree(Files.java:2609)
        at net.minecraft.util.filefix.virtualfilesystem.CopyOnWriteFileSystem.buildFileTreeFrom(CopyOnWriteFileSystem.java:71)
        at net.minecraft.util.filefix.virtualfilesystem.CopyOnWriteFileSystem.<init>(CopyOnWriteFileSystem.java:54)
        at net.minecraft.util.filefix.virtualfilesystem.CopyOnWriteFileSystem.create(CopyOnWriteFileSystem.java:62)
        at net.minecraft.util.filefix.FileFixerUpper.fix(FileFixerUpper.java:73)
        at net.minecraft.util.filefix.FileFixerUpper.fix(FileFixerUpper.java:64)
        at net.minecraft.client.gui.screens.worldselection.WorldOpenFlows.lambda$upgradeAndOpenWorld$0(WorldOpenFlows.java:353)
        at java.base/java.util.concurrent.ForkJoinTask$RunnableExecuteAction.compute(ForkJoinTask.java:1750)
        at java.base/java.util.concurrent.ForkJoinTask$RunnableExecuteAction.compute(ForkJoinTask.java:1742)
        at java.base/java.util.concurrent.ForkJoinTask$InterruptibleTask.exec(ForkJoinTask.java:1659)
        at java.base/java.util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:511)
        at java.base/java.util.concurrent.ForkJoinPool$WorkQueue.topLevelExec(ForkJoinPool.java:1450)
        at java.base/java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:2019)
        at java.base/java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:187)
```

## Comments (1)

### Comment 1: Colin Crumpler (2026-02-04T18:41:14.481-0800)

It also happened for one of my worlds from 26.1 Snapshot 5
