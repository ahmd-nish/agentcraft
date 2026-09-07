# MC-220067: Chunk corruption with command block full of certain Unicode characters

**Mojira URL:** [https://bugs.mojang.com/browse/MC-220067](https://bugs.mojang.com/browse/MC-220067)

## Report details

- **Mojira categories:** Chunk loading
- **Project:** MC
- **Issue key:** MC-220067
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2021-03-18T12:18:01.343-0700
- **Updated:** 2025-04-30T08:02:32.947-0700
- **Resolution date:** 2022-05-31T05:07:28.813-0700
- **Affects versions:** 1.16.5; 21w11a; 1.17 Release Candidate 2; 1.17; 1.17.1; 21w38a; 21w39a; 21w42a; 1.18.1; 1.18.2; 22w17a; 22w18a; 22w19a; 1.19 Pre-release 1; 1.19 Pre-release 2; 1.19 Pre-release 3
- **Fix versions:** 1.19 Pre-release 4
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** chunkfail.txt; latest.log

## Description

The bug
When a command block is full of characters that take more than 1 byte to store, the chunk that command block is in gets corrupted.
How to reproduce
- Place a command block down.

- Copy and paste this symbol "■" into the command block until the command block is full.

- Save and quit to title.

- Get back in the world.
→  The chunk the command block was in is re-generated; resetting everything in it

Note
■ is not the only character this works with.
Game output error message

```
Failed to store chunk [7, 1]
java.io.UTFDataFormatException: encoded string (■■■■■■■■...■■■■■■■■) too long: 97500 bytes
	at java.base/java.io.DataOutputStream.writeUTF(DataOutputStream.java:368)
	at java.base/java.io.DataOutputStream.writeUTF(DataOutputStream.java:332)
	at nq.a(SourceFile:65)
	at na.a(SourceFile:415)
	at na.a(SourceFile:104)
	at ng.a(SourceFile:81)
	at na.a(SourceFile:415)
	at na.a(SourceFile:104)
	at na.a(SourceFile:415)
	at na.a(SourceFile:104)
	at nk.a(SourceFile:95)
	at nk.a(SourceFile:83)
	at cnq.a(SourceFile:70)
	at cnm.a(SourceFile:153)
	at cnm.a(SourceFile:143)
	at ara$b.run(SourceFile:61)
	at aqy.g(SourceFile:91)
	at aqy.a(SourceFile:146)
	at aqy.run(SourceFile:102)
	at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1130)
	at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:630)
	at java.base/java.lang.Thread.run(Thread.java:831)
```
Video
https://youtu.be/C4t2avl0Dhw
(Video by Phoenix SC)

## Comments (16)

### Comment 1: migrated (2021-03-18T12:18:01.343-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: Dobbybro17 (2021-03-18T12:31:23.814-0700)

You are overloading the chunk with information. When you do this, it resets to its latest save.

### Comment 3: pine1needle (2021-03-18T18:22:51.219-0700)

I was able to reproduce this in both 21w11a and 1.16.5. Additionally, after you click "Done" on the command block, the launcher crashes. The game itself (Java) remains open. It's easiest to notice the launcher crashing if you have the launcher log open (by selecting "Open output log when Minecraft: Java Edition starts" in the launcher settings before you launch the game). However, even if you don't have the launcher log open, you can still observe the launcher crashing by watching Activity Monitor (on macOS) or Task Manager (on Windows).
Perhaps this report should be moved to the MCL project? Or maybe a separate MCL report should be created and linked to this report? I'm unsure whether the chunk resetting is a side-effect of the launcher crashing, or if it is a separate issue.

### Comment 4: pine1needle (2021-03-25T16:42:53.782-0700)

After discussing this on the Mojira Discord, I created a separate report about the launcher crash: .

### Comment 5: ampolive (2021-06-08T04:48:02.820-0700)

Can confirm in 1.17 Release Candidate 2.

### Comment 6: ampolive (2021-07-13T07:44:49.691-0700)

Can confirm in 1.17.1.

### Comment 7: ampolive (2021-07-13T08:16:45.945-0700)

After searching the logs, it looks like the game does not only fail to load the chunk, it fails to write the chunk as well.

### Comment 8: ampolive (2021-07-20T05:13:42.508-0700)

Can confirm that this also affects other Unicode characters (☃ is one of them).

### Comment 9: ampolive (2021-09-28T06:31:49.206-0700)

Can confirm in 21w38a.

### Comment 10: ampolive (2021-10-05T15:57:39.893-0700)

Can confirm in 21w39a.

### Comment 11: ampolive (2021-10-20T09:53:59.536-0700)

Can confirm in 21w42a.

### Comment 12: migrated (2022-02-25T08:49:11.126-0800)

Can confirm in 1.18.2 Pre-release 3.

### Comment 13: pulpetti (2022-05-17T04:45:36.805-0700)

In 22w19a and 1.18.2..

### Comment 14: Avoma (2022-05-18T10:45:46.629-0700)

I can confirm this in 1.19 Pre-release 1. I reproduced this issue using the steps provided in  and rebooting the server whilst the command block was still present in the world. Here's the server log.

### Comment 15: pulpetti (2022-05-24T06:23:44.280-0700)

In 1.19 Pre-2.

### Comment 16: DrageonDB (2022-05-29T21:42:16.140-0700)

Affect 1.19 pre 3
