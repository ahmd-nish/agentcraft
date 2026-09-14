# MC-251889: io.netty.handler.codec.EncoderException when evaluating too many entity selectors in chat preview

**Mojira URL:** [https://bugs.mojang.com/browse/MC-251889](https://bugs.mojang.com/browse/MC-251889)

## Report details

- **Mojira categories:** Networking
- **Project:** MC
- **Issue key:** MC-251889
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2022-05-18T20:11:34.354-0700
- **Updated:** 2025-04-30T08:10:08.622-0700
- **Resolution date:** 2022-05-19T08:56:58.585-0700
- **Affects versions:** 1.19 Pre-release 1
- **Fix versions:** 1.19 Pre-release 2
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** 2022-05-18_22.43.31.png

## Description

The bug
When typing a command that causes the chat preview to respond with a message too large, the client disconnects from the server with an io.netty.handler.codec.EncoderException. This can be reproduced by preparing to send a command with a large number of entity selectors, such as /say @e @e @e @e @e @e @e @e @e @e in a normal world.
Relates to .
How to reproduce
- Create a server in the latest affected version with chat preview enabled

- Join the server, and type the command /say @e @e @e ...
 Continuing to type @e will eventually cause client to disconnect

Stack trace

```
Error receiving packet 12
io.netty.handler.codec.EncoderException: String too big (was 313058 characters, max 262144)
	at qx.a(SourceFile:617) ~[server-1.19-pre1.jar:?]
	at qx.a(SourceFile:425) ~[server-1.19-pre1.jar:?]
	at qx.a(SourceFile:258) ~[server-1.19-pre1.jar:?]
	at te.a(SourceFile:16) ~[server-1.19-pre1.jar:?]
	at qz.a(SourceFile:45) ~[server-1.19-pre1.jar:?]
	at qz.encode(SourceFile:14) ~[server-1.19-pre1.jar:?]
	at io.netty.handler.codec.MessageToByteEncoder.write(MessageToByteEncoder.java:107) ~[netty-codec-4.1.76.Final.jar:4.1.76.Final]
	at io.netty.channel.AbstractChannelHandlerContext.invokeWrite0(AbstractChannelHandlerContext.java:717) ~[netty-transport-4.1.76.Final.jar:4.1.76.Final]
	at io.netty.channel.AbstractChannelHandlerContext.invokeWriteAndFlush(AbstractChannelHandlerContext.java:764) ~[netty-transport-4.1.76.Final.jar:4.1.76.Final]
	at io.netty.channel.AbstractChannelHandlerContext.write(AbstractChannelHandlerContext.java:790) ~[netty-transport-4.1.76.Final.jar:4.1.76.Final]
	at io.netty.channel.AbstractChannelHandlerContext.writeAndFlush(AbstractChannelHandlerContext.java:758) ~[netty-transport-4.1.76.Final.jar:4.1.76.Final]
	at io.netty.channel.AbstractChannelHandlerContext.writeAndFlush(AbstractChannelHandlerContext.java:808) ~[netty-transport-4.1.76.Final.jar:4.1.76.Final]
	at io.netty.channel.DefaultChannelPipeline.writeAndFlush(DefaultChannelPipeline.java:1025) ~[netty-transport-4.1.76.Final.jar:4.1.76.Final]
	at io.netty.channel.AbstractChannel.writeAndFlush(AbstractChannel.java:306) ~[netty-transport-4.1.76.Final.jar:4.1.76.Final]
	at qv.a(SourceFile:213) ~[server-1.19-pre1.jar:?]
	at qv.b(SourceFile:205) ~[server-1.19-pre1.jar:?]
	at io.netty.util.concurrent.AbstractEventExecutor.safeExecute(AbstractEventExecutor.java:164) [netty-common-4.1.76.Final.jar:4.1.76.Final]
	at io.netty.util.concurrent.SingleThreadEventExecutor.runAllTasks(SingleThreadEventExecutor.java:469) [netty-common-4.1.76.Final.jar:4.1.76.Final]
	at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:503) [netty-transport-4.1.76.Final.jar:4.1.76.Final]
	at io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:986) [netty-common-4.1.76.Final.jar:4.1.76.Final]
	at io.netty.util.internal.ThreadExecutorMap$2.run(ThreadExecutorMap.java:74) [netty-common-4.1.76.Final.jar:4.1.76.Final]
	at java.lang.Thread.run(Thread.java:833) [?:?]
```

## Comments (3)

### Comment 1: migrated (2022-05-18T20:11:34.354-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: apple502j (2022-05-18T21:12:37.779-0700)

Duplicate of MC-45838

### Comment 3: markderickson (2022-05-19T04:08:50.763-0700)

That's possible, although I wasn't able to reproduce that issue because it gave a "Failed to send chat message" error. Therefore, I assumed this one has a different cause.
