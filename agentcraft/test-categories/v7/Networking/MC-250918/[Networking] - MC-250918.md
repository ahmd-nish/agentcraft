# MC-250918: Players are disconnected from servers when opening command blocks that consist of large numbers of characters within the previous output field

**Mojira URL:** [https://bugs.mojang.com/browse/MC-250918](https://bugs.mojang.com/browse/MC-250918)

## Report details

- **Mojira categories:** Networking
- **Project:** MC
- **Issue key:** MC-250918
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2022-04-27T02:39:28.134-0700
- **Updated:** 2025-04-30T07:41:30.763-0700
- **Resolution date:** 2022-07-05T04:14:53.828-0700
- **Affects versions:** 1.18.2; 22w16b; 22w17a; 22w19a; 1.19 Pre-release 1; 1.19 Pre-release 2; 1.19 Pre-release 3
- **Fix versions:** 1.19 Pre-release 4
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** latest.log; MC-250918.mp4; MC-250918.png

## Description

The Bug:
Players are disconnected from servers when opening command blocks that consist of large numbers of characters within the previous output field.
It's important to note that this issue doesn't occur in singleplayer.
The full server console log regarding this has been attached and can be found below.
Stack Trace:
[^latest.log]

```
[10:32:06] [Netty Server IO #2/ERROR]: Error receiving packet 7
io.netty.handler.codec.EncoderException: java.io.UTFDataFormatException: encoded string ({"extra"...2:06] "}) too long: 331525 bytes
    at qn.a(SourceFile:443) ~[server-22w16b.jar:?]
    at sh.a(SourceFile:44) ~[server-22w16b.jar:?]
    at qp.a(SourceFile:45) ~[server-22w16b.jar:?]
    at qp.encode(SourceFile:14) ~[server-22w16b.jar:?]
    at io.netty.handler.codec.MessageToByteEncoder.write(MessageToByteEncoder.java:107) ~[netty-all-4.1.68.Final.jar:4.1.68.Final]
    at io.netty.channel.AbstractChannelHandlerContext.invokeWrite0(AbstractChannelHandlerContext.java:717) ~[netty-all-4.1.68.Final.jar:4.1.68.Final]
    at io.netty.channel.AbstractChannelHandlerContext.invokeWriteAndFlush(AbstractChannelHandlerContext.java:764) ~[netty-all-4.1.68.Final.jar:4.1.68.Final]
    at io.netty.channel.AbstractChannelHandlerContext.write(AbstractChannelHandlerContext.java:790) ~[netty-all-4.1.68.Final.jar:4.1.68.Final]
    at io.netty.channel.AbstractChannelHandlerContext.writeAndFlush(AbstractChannelHandlerContext.java:758) ~[netty-all-4.1.68.Final.jar:4.1.68.Final]
    at io.netty.channel.AbstractChannelHandlerContext.writeAndFlush(AbstractChannelHandlerContext.java:808) ~[netty-all-4.1.68.Final.jar:4.1.68.Final]
    at io.netty.channel.DefaultChannelPipeline.writeAndFlush(DefaultChannelPipeline.java:1025) ~[netty-all-4.1.68.Final.jar:4.1.68.Final]
    at io.netty.channel.AbstractChannel.writeAndFlush(AbstractChannel.java:306) ~[netty-all-4.1.68.Final.jar:4.1.68.Final]
    at ql.a(SourceFile:213) ~[server-22w16b.jar:?]
    at ql.b(SourceFile:205) ~[server-22w16b.jar:?]
    at io.netty.util.concurrent.AbstractEventExecutor.safeExecute(AbstractEventExecutor.java:164) [netty-all-4.1.68.Final.jar:4.1.68.Final]
    at io.netty.util.concurrent.SingleThreadEventExecutor.runAllTasks(SingleThreadEventExecutor.java:469) [netty-all-4.1.68.Final.jar:4.1.68.Final]
    at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:500) [netty-all-4.1.68.Final.jar:4.1.68.Final]
    at io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:986) [netty-all-4.1.68.Final.jar:4.1.68.Final]
    at io.netty.util.internal.ThreadExecutorMap$2.run(ThreadExecutorMap.java:74) [netty-all-4.1.68.Final.jar:4.1.68.Final]
    at java.lang.Thread.run(Thread.java:833) [?:?]
```
Steps to Reproduce:
- Launch a server running 22w16b that has command blocks enabled and join it.

- Unlock all recipes within the game by executing the command provided below.

```
/recipe give @s *
```
- Summon a repeating command block nearby that will constantly get the data of your player.

```
/setblock ~ ~ ~3 minecraft:repeating_command_block{auto:1b,Command:"data get entity @p"}
```
- Open the command block and take note as to whether or not you are disconnected from the server.

Observed Behavior:
Players are disconnected from servers.
Expected Behavior:
Players would not be disconnected from servers.

## Comments (8)

### Comment 1: migrated (2022-04-27T02:39:28.134-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: Avoma (2022-04-27T02:51:36.121-0700)

This ticket closely relates to MC-250919.

### Comment 3: pulpetti (2022-05-17T04:46:05.357-0700)

In 22w19a.

### Comment 4: Avoma (2022-05-20T09:06:17.998-0700)

Sometimes as a result of this issue occurring, MC-220067 is also experienced.

### Comment 5: pulpetti (2022-05-24T06:24:26.243-0700)

In 1.19 Pre-2.

### Comment 6: pulpetti (2022-05-30T04:45:34.954-0700)

In 1.19 Pre-3.

### Comment 7: Avoma (2022-05-30T09:39:57.836-0700)

This issue has been fixed in 1.19 Pre-release 4 very likely due to the fix of MC-220067.
While the player is no longer disconnected from the server when reproducing this issue, errors regarding NBT string writing failures are logged in the game output and server console, and I've created a new ticket for this (MC-252353) since it's a different issue.

### Comment 8: Avoma (2022-06-27T01:54:47.186-0700)

I cannot reproduce this issue in 1.19. See my above comment.
