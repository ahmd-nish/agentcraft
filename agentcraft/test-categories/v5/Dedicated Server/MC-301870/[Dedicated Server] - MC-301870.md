# MC-301870: Command feedback for successful /ban and /ban-ip commands with no specified reason can't be sent to the client

**Mojira URL:** [https://bugs.mojang.com/browse/MC-301870](https://bugs.mojang.com/browse/MC-301870)

## Report details

- **Mojira categories:** Commands; Dedicated Server
- **Project:** MC
- **Issue key:** MC-301870
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2025-09-04T08:58:16.604-0700
- **Updated:** 2026-03-11T03:57:15.928-0700
- **Resolution date:** 2025-09-08T02:26:42.642-0700
- **Affects versions:** 25w36b
- **Fix versions:** 25w37a
- **Area:** Platform EC
- **Votes:** 2
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** image-20250904-155711.png

## Description

When using the /ban and /ban-ip commands, an error message is shown in the chat and logs, but the ban works correctly. Other commands like /op work correctly.
Error message in the chat: Can’t deliver chat message; check server logs: Banned IP 1.1.1.1: null
Full Log:
Error message in console:

```
[17:51:33] [Netty Epoll Server IO #1/ERROR]: Error sending packet clientbound/minecraft:system_chat
io.netty.handler.codec.EncoderException: Failed to encode packet 'clientbound/minecraft:system_chat'
	at aad.a(SourceFile:61) ~[server-25w36b.jar:?]
	at aad.encode(SourceFile:14) ~[server-25w36b.jar:?]
	at wz.a(SourceFile:26) ~[server-25w36b.jar:?]
	at wz.encode(SourceFile:12) ~[server-25w36b.jar:?]
	at io.netty.handler.codec.MessageToByteEncoder.write(MessageToByteEncoder.java:107) ~[netty-codec-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.channel.AbstractChannelHandlerContext.invokeWrite0(AbstractChannelHandlerContext.java:893) ~[netty-transport-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.channel.AbstractChannelHandlerContext.invokeWrite(AbstractChannelHandlerContext.java:875) ~[netty-transport-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.channel.AbstractChannelHandlerContext.write(AbstractChannelHandlerContext.java:984) ~[netty-transport-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.channel.AbstractChannelHandlerContext.write(AbstractChannelHandlerContext.java:868) ~[netty-transport-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.handler.codec.MessageToMessageEncoder.write(MessageToMessageEncoder.java:113) ~[netty-codec-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.channel.AbstractChannelHandlerContext.invokeWrite0(AbstractChannelHandlerContext.java:893) ~[netty-transport-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.channel.AbstractChannelHandlerContext.invokeWrite(AbstractChannelHandlerContext.java:875) ~[netty-transport-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.channel.AbstractChannelHandlerContext.write(AbstractChannelHandlerContext.java:984) ~[netty-transport-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.channel.AbstractChannelHandlerContext.write(AbstractChannelHandlerContext.java:868) ~[netty-transport-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.channel.ChannelOutboundHandlerAdapter.write(ChannelOutboundHandlerAdapter.java:113) ~[netty-transport-4.1.118.Final.jar:4.1.118.Final]
	at wk$2.write(SourceFile:524) ~[server-25w36b.jar:?]
	at io.netty.channel.AbstractChannelHandlerContext.invokeWrite0(AbstractChannelHandlerContext.java:893) ~[netty-transport-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.channel.AbstractChannelHandlerContext.invokeWriteAndFlush(AbstractChannelHandlerContext.java:956) ~[netty-transport-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.channel.AbstractChannelHandlerContext.write(AbstractChannelHandlerContext.java:982) ~[netty-transport-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.channel.AbstractChannelHandlerContext.writeAndFlush(AbstractChannelHandlerContext.java:950) ~[netty-transport-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.channel.AbstractChannelHandlerContext.writeAndFlush(AbstractChannelHandlerContext.java:1000) ~[netty-transport-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.channel.DefaultChannelPipeline.writeAndFlush(DefaultChannelPipeline.java:974) ~[netty-transport-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.channel.AbstractChannel.writeAndFlush(AbstractChannel.java:305) ~[netty-transport-4.1.118.Final.jar:4.1.118.Final]
	at wk.c(SourceFile:350) ~[server-25w36b.jar:?]
	at wk.d(SourceFile:344) ~[server-25w36b.jar:?]
	at io.netty.util.concurrent.AbstractEventExecutor.runTask(AbstractEventExecutor.java:173) ~[netty-common-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.util.concurrent.AbstractEventExecutor.safeExecute(AbstractEventExecutor.java:166) ~[netty-common-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.util.concurrent.SingleThreadEventExecutor.runAllTasks(SingleThreadEventExecutor.java:472) ~[netty-common-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.channel.epoll.EpollEventLoop.run(EpollEventLoop.java:405) ~[netty-transport-classes-epoll-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:998) ~[netty-common-4.1.118.Final.jar:4.1.118.Final]
	at io.netty.util.internal.ThreadExecutorMap$2.run(ThreadExecutorMap.java:74) ~[netty-common-4.1.118.Final.jar:4.1.118.Final]
	at java.base/java.lang.Thread.run(Thread.java:1583) [?:?]
Caused by: io.netty.handler.codec.EncoderException: Failed to encode: This value needs to be parsed as component translation{key='commands.banip.success', args=[1.1.1.1, null]}
	at aac$10.a(SourceFile:347) ~[server-25w36b.jar:?]
	at com.mojang.serialization.DataResult$Error.getOrThrow(DataResult.java:287) ~[datafixerupper-8.0.16.jar:?]
	at aac$10.a(SourceFile:347) ~[server-25w36b.jar:?]
	at aac$10.encode(SourceFile:336) ~[server-25w36b.jar:?]
	at aae$16.encode(SourceFile:160) ~[server-25w36b.jar:?]
	at aae$13.a(SourceFile:101) ~[server-25w36b.jar:?]
	at aae$13.encode(SourceFile:91) ~[server-25w36b.jar:?]
	at aad.a(SourceFile:56) ~[server-25w36b.jar:?]
	... 31 more
```

## Comments (1)

### Comment 1: Julian Vennen (2025-09-04T08:58:17.422-0700)

This comment contained an image attachment, please login to view the attachment.
