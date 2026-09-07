# MC-249431: The server occasionally fails to save chunks

**Mojira URL:** [https://bugs.mojang.com/browse/MC-249431](https://bugs.mojang.com/browse/MC-249431)

## Report details

- **Mojira categories:** Save Data
- **Project:** MC
- **Issue key:** MC-249431
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2022-03-24T13:30:17.511-0700
- **Updated:** 2025-04-26T14:19:13.089-0700
- **Resolution date:** 2024-08-26T03:15:22.317-0700
- **Affects versions:** 22w12a
- **Fix versions:** 22w13a
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-249431.png; MC-249431 - Server Console Log.log
- **Issue links:** Relates:inward:MC-275981:Server is constantly failing to save chunks

## Description

The Bug:
The "Failed to save chunk" error is sometimes logged in the server console, thus indicating that the server occasionally fails to save chunks.
This issue was not present in 1.18.2 or 22w11a.
The following message was printed into the server console shortly after teleporting a far distance away and then running the "/kill" command. The full server log has also been attached which can be found below.
[^MC-249431 - Server Console Log.log]

```
[18:22:28] [Server thread/ERROR]: Failed to save chunk -16,-11
java.lang.NullPointerException: Cannot invoke "java.util.UUID.getMostSignificantBits()" because "$$0" is null
    at hi.a(SourceFile:27) ~[server-22w12a.jar:?]
    at hi.b(SourceFile:13) ~[server-22w12a.jar:?]
    at com.mojang.serialization.Encoder$1.encode(Encoder.java:25) ~[datafixerupper-4.1.27.jar:?]
    at com.mojang.serialization.Codec$2.encode(Codec.java:76) ~[datafixerupper-4.1.27.jar:?]
    at com.mojang.serialization.Encoder.encodeStart(Encoder.java:14) ~[datafixerupper-4.1.27.jar:?]
    at com.mojang.serialization.codecs.FieldEncoder.encode(FieldEncoder.java:24) ~[datafixerupper-4.1.27.jar:?]
    at com.mojang.serialization.MapCodec$1.encode(MapCodec.java:39) ~[datafixerupper-4.1.27.jar:?]
    at com.mojang.serialization.MapCodec$3.encode(MapCodec.java:181) ~[datafixerupper-4.1.27.jar:?]
    at com.mojang.serialization.codecs.RecordCodecBuilder$Instance$8.encode(RecordCodecBuilder.java:379) ~[datafixerupper-4.1.27.jar:?]
    at com.mojang.serialization.codecs.RecordCodecBuilder$2.encode(RecordCodecBuilder.java:112) ~[datafixerupper-4.1.27.jar:?]
    at com.mojang.serialization.MapCodec$MapCodecCodec.encode(MapCodec.java:96) ~[datafixerupper-4.1.27.jar:?]
    at com.mojang.serialization.Encoder.encodeStart(Encoder.java:14) ~[datafixerupper-4.1.27.jar:?]
    at com.mojang.serialization.codecs.OptionalFieldCodec.encode(OptionalFieldCodec.java:42) ~[datafixerupper-4.1.27.jar:?]
    at com.mojang.serialization.codecs.OptionalFieldCodec.encode(OptionalFieldCodec.java:17) ~[datafixerupper-4.1.27.jar:?]
    at com.mojang.serialization.codecs.RecordCodecBuilder$Instance$6.encode(RecordCodecBuilder.java:295) ~[datafixerupper-4.1.27.jar:?]
    at com.mojang.serialization.codecs.RecordCodecBuilder$2.encode(RecordCodecBuilder.java:112) ~[datafixerupper-4.1.27.jar:?]
    at com.mojang.serialization.MapCodec$MapCodecCodec.encode(MapCodec.java:96) ~[datafixerupper-4.1.27.jar:?]
    at com.mojang.serialization.Encoder.encodeStart(Encoder.java:14) ~[datafixerupper-4.1.27.jar:?]
    at cqe.b(SourceFile:51) ~[server-22w12a.jar:?]
    at cpf.o(SourceFile:84) ~[server-22w12a.jar:?]
    at cpf.m(SourceFile:64) ~[server-22w12a.jar:?]
    at cto.g(SourceFile:380) ~[server-22w12a.jar:?]
    at cuc.a(SourceFile:345) ~[server-22w12a.jar:?]
    at ads.a(SourceFile:828) ~[server-22w12a.jar:?]
    at ads.d(SourceFile:792) ~[server-22w12a.jar:?]
    at ads.b(SourceFile:531) ~[server-22w12a.jar:?]
    at ads.a(SourceFile:486) ~[server-22w12a.jar:?]
    at aed.a(SourceFile:326) ~[server-22w12a.jar:?]
    at aef.a(SourceFile:314) ~[server-22w12a.jar:?]
    at net.minecraft.server.MinecraftServer.b(SourceFile:903) ~[server-22w12a.jar:?]
    at adg.b(SourceFile:322) ~[server-22w12a.jar:?]
    at net.minecraft.server.MinecraftServer.a(SourceFile:847) ~[server-22w12a.jar:?]
    at net.minecraft.server.MinecraftServer.w(SourceFile:693) ~[server-22w12a.jar:?]
    at net.minecraft.server.MinecraftServer.a(SourceFile:271) ~[server-22w12a.jar:?]
    at java.lang.Thread.run(Thread.java:833) [?:?]
```
Steps to Reproduce:
- Start a server running 22w12a.

- Teleport a far distance away and then run the "/kill" command in order to make some chunks unload.

```
/tp @s ~10000 ~ ~
```

```
/kill @s
```
- Respawn and watch the server console closely.

- Take note as to whether or not the server occasionally fails to save chunks.

Observed Behavior:
The server fails to save chunks.
Expected Behavior:
The server would not fail to save chunks.

## Comments (7)

### Comment 1: migrated (2022-03-24T13:30:17.511-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: MMK21 (2022-03-25T10:24:46.527-0700)

According to MC-249444, it looks like this is also a chunk corruption bug, not just a logspam issue.

### Comment 3: Avoma (2022-03-25T11:32:21.461-0700)

Thank you, I've updated this ticket accordingly.

### Comment 4: Avoma (2022-04-06T06:21:02.391-0700)

This issue may have been fixed in 22w13a, although I'm not entirely sure so please don't take my word for it. After playing on a server running 22w13a for multiple hours and whilst exploring numerous amount of chunks during this time, this error was never logged in the server console.

### Comment 5: Panda4994 (2022-04-19T07:53:35.689-0700)

Can confirm, this has been fixed in 22w13a.

### Comment 6: Avoma (2022-04-19T09:57:05.411-0700)

I thought it might have been; thank you!

### Comment 7: Nicoder (2024-08-24T13:23:06.446-0700)

This bug still affects me on 1.21
[13:22:30] [IO-Worker-1940/ERROR]: Failed to save chunk 14,-1
java.util.concurrent.CompletionException: java.io.IOException: Operation timed out
at java.base/java.util.concurrent.CompletableFuture.encodeRelay(CompletableFuture.java:368) ~[?:?]
at java.base/java.util.concurrent.CompletableFuture.completeRelay(CompletableFuture.java:377) ~[?:?]
at java.base/java.util.concurrent.CompletableFuture$UniRelay.tryFire(CompletableFuture.java:1097) ~[?:?]
at java.base/java.util.concurrent.CompletableFuture.postComplete(CompletableFuture.java:510) ~[?:?]
at java.base/java.util.concurrent.CompletableFuture.completeExceptionally(CompletableFuture.java:2194) ~[?:?]
at dwl.a(SourceFile:270) ~[server-1.21.jar:?]
at dwl.b(SourceFile:256) ~[server-1.21.jar:?]
at bpm$b.run(SourceFile:60) ~[server-1.21.jar:?]
at bpk.h(SourceFile:91) ~[server-1.21.jar:?]
at bpk.a(SourceFile:146) ~[server-1.21.jar:?]
at bpk.run(SourceFile:102) ~[server-1.21.jar:?]
at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1144) ~[?:?]
at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:642) ~[?:?]
at java.base/java.lang.Thread.run(Thread.java:1583) [?:?]
Caused by: java.io.IOException: Operation timed out
at java.base/sun.nio.ch.UnixFileDispatcherImpl.pwrite0(Native Method) ~[?:?]
at java.base/sun.nio.ch.UnixFileDispatcherImpl.pwrite(UnixFileDispatcherImpl.java:71) ~[?:?]
at java.base/sun.nio.ch.IOUtil.writeFromNativeBuffer(IOUtil.java:135) ~[?:?]
at java.base/sun.nio.ch.IOUtil.write(IOUtil.java:102) ~[?:?]
at java.base/sun.nio.ch.IOUtil.write(IOUtil.java:72) ~[?:?]
at java.base/sun.nio.ch.FileChannelImpl.writeInternal(FileChannelImpl.java:1028) ~[?:?]
at java.base/sun.nio.ch.FileChannelImpl.write(FileChannelImpl.java:1012) ~[?:?]
at dwp.a(SourceFile:423) ~[server-1.21.jar:?]
at dwp$a.close(SourceFile:396) ~[server-1.21.jar:?]
at java.base/java.util.zip.DeflaterOutputStream.close(DeflaterOutputStream.java:249) ~[?:?]
at java.base/java.io.FilterOutputStream.close(FilterOutputStream.java:190) ~[?:?]
at java.base/java.io.FilterOutputStream.close(FilterOutputStream.java:190) ~[?:?]
at dwq.a(SourceFile:83) ~[server-1.21.jar:?]
at dwl.a(SourceFile:266) ~[server-1.21.jar:?]
... 8 more
