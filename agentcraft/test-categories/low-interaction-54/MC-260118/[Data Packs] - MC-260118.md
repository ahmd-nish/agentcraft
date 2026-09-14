# MC-260118: Disabling experimental features on the world creation screen causes pack validation to fail

**Mojira URL:** [https://bugs.mojang.com/browse/MC-260118](https://bugs.mojang.com/browse/MC-260118)

## Report details

- **Mojira categories:** Data Packs; UI
- **Project:** MC
- **Issue key:** MC-260118
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2023-02-15T12:05:44.146-0800
- **Updated:** 2025-03-20T23:15:48.244-0700
- **Resolution date:** 2023-02-22T03:00:53.751-0800
- **Affects versions:** 23w07a
- **Fix versions:** 1.19.4 Pre-release 1
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2023-02-15_21.10.05.png; Minecraft 23w07a 2023-02-15 21-19-50.mp4

## Description

The bug
On the world creation screen, once experimental features have been enabled, they cannot be disabled again. This might be intentional. In this case, the button for disabling the feature should be greyed out, indicating that this action should not be performed.
To reproduce
- Go to the "Create New World" screen.

- Go to the Experiments tab.

- Turn both buttons on and click "Done".

- Go back to the "Create New World" screen.

- Go to the Experiments tab again.

- Try turning both buttons off and click "Done".

Observed result
You are unable to create the new world, because data pack validation fails. The following is logged:

```
[17:01:58] [Render thread/WARN]: Failed to validate datapack
java.util.concurrent.CompletionException: java.lang.IllegalStateException: Missing element ResourceKey[minecraft:worldgen/biome / minecraft:cherry_grove]
	at java.util.concurrent.CompletableFuture.encodeThrowable(CompletableFuture.java:332) ~[?:?]
	at java.util.concurrent.CompletableFuture.uniAcceptNow(CompletableFuture.java:747) ~[?:?]
	at java.util.concurrent.CompletableFuture.uniAcceptStage(CompletableFuture.java:735) ~[?:?]
	at java.util.concurrent.CompletableFuture.thenAcceptAsync(CompletableFuture.java:2191) ~[?:?]
	at exf.a(SourceFile:644) ~[23w07a.jar:?]
	at exf.a(SourceFile:604) ~[23w07a.jar:?]
	at exf.b(SourceFile:569) ~[23w07a.jar:?]
	at exi.j(SourceFile:100) ~[23w07a.jar:?]
	at exi.b(SourceFile:71) ~[23w07a.jar:?]
	at enx.c(SourceFile:94) ~[23w07a.jar:?]
	at eno.a(SourceFile:16) ~[23w07a.jar:?]
	at enu.a(SourceFile:220) ~[23w07a.jar:?]
	at epd.a(SourceFile:38) ~[23w07a.jar:?]
	at emd.b(SourceFile:96) ~[23w07a.jar:?]
	at esv.a(SourceFile:541) ~[23w07a.jar:?]
	at emd.a(SourceFile:96) ~[23w07a.jar:?]
	at emd.c(SourceFile:167) ~[23w07a.jar:?]
	at bcn.execute(SourceFile:102) ~[23w07a.jar:?]
	at emd.b(SourceFile:167) ~[23w07a.jar:?]
	at org.lwjgl.glfw.GLFWMouseButtonCallbackI.callback(GLFWMouseButtonCallbackI.java:43) ~[lwjgl-glfw-3.3.1.jar:build 7]
	at org.lwjgl.system.JNI.invokeV(Native Method) ~[lwjgl-3.3.1.jar:build 7]
	at org.lwjgl.glfw.GLFW.glfwPollEvents(GLFW.java:3403) ~[lwjgl-glfw-3.3.1.jar:build 7]
	at com.mojang.blaze3d.systems.RenderSystem.pollEvents(SourceFile:198) ~[23w07a.jar:?]
	at com.mojang.blaze3d.systems.RenderSystem.flipFrame(SourceFile:216) ~[23w07a.jar:?]
	at egf.e(SourceFile:310) ~[23w07a.jar:?]
	at emc.f(SourceFile:1247) ~[23w07a.jar:?]
	at emc.e(SourceFile:800) ~[23w07a.jar:?]
	at net.minecraft.client.main.Main.a(SourceFile:244) ~[23w07a.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:51) ~[23w07a.jar:?]
Caused by: java.lang.IllegalStateException: Missing element ResourceKey[minecraft:worldgen/biome / minecraft:cherry_grove]
	at hc.c(SourceFile:15) ~[23w07a.jar:?]
	at java.util.Optional.orElseThrow(Optional.java:403) ~[?:?]
	at hc.b(SourceFile:15) ~[23w07a.jar:?]
	at cnr$a.a(SourceFile:147) ~[23w07a.jar:?]
	at com.mojang.datafixers.util.Pair.mapSecond(Pair.java:68) ~[datafixerupper-5.0.28.jar:?]
	at cnr$a.a(SourceFile:142) ~[23w07a.jar:?]
	at cns.a(SourceFile:599) ~[23w07a.jar:?]
	at cns.c(SourceFile:393) ~[23w07a.jar:?]
	at cns.d(SourceFile:272) ~[23w07a.jar:?]
	at cns.a(SourceFile:197) ~[23w07a.jar:?]
	at cnr$a.a(SourceFile:142) ~[23w07a.jar:?]
	at cnr$a$3.apply(SourceFile:122) ~[23w07a.jar:?]
	at cnr$a.a(SourceFile:147) ~[23w07a.jar:?]
	at cnr$b.a(SourceFile:92) ~[23w07a.jar:?]
	at com.mojang.datafixers.util.Either$Left.map(Either.java:38) ~[datafixerupper-5.0.28.jar:?]
	at cnr.a(SourceFile:42) ~[23w07a.jar:?]
	at com.mojang.datafixers.util.Either$Left.mapBoth(Either.java:33) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.map(DataResult.java:110) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.MapDecoder$4.decode(MapDecoder.java:94) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.MapCodec$1.decode(MapCodec.java:34) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.KeyDispatchCodec.lambda$decode$1(KeyDispatchCodec.java:67) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.lambda$flatMap$10(DataResult.java:138) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.datafixers.util.Either$Left.map(Either.java:38) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.flatMap(DataResult.java:136) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.KeyDispatchCodec.lambda$decode$2(KeyDispatchCodec.java:58) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.lambda$flatMap$10(DataResult.java:138) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.datafixers.util.Either$Left.map(Either.java:38) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.flatMap(DataResult.java:136) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.KeyDispatchCodec.decode(KeyDispatchCodec.java:56) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.MapDecoder.lambda$compressedDecode$0(MapDecoder.java:52) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.lambda$flatMap$10(DataResult.java:138) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.datafixers.util.Either$Left.map(Either.java:38) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.flatMap(DataResult.java:136) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.MapDecoder.compressedDecode(MapDecoder.java:52) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.MapCodec$MapCodecCodec.decode(MapCodec.java:91) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.Decoder.parse(Decoder.java:18) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.FieldDecoder.decode(FieldDecoder.java:29) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.MapCodec$1.decode(MapCodec.java:34) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.RecordCodecBuilder$Instance$3.decode(RecordCodecBuilder.java:248) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.RecordCodecBuilder$2.decode(RecordCodecBuilder.java:107) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.KeyDispatchCodec.lambda$decode$1(KeyDispatchCodec.java:67) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.lambda$flatMap$10(DataResult.java:138) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.datafixers.util.Either$Left.map(Either.java:38) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.flatMap(DataResult.java:136) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.KeyDispatchCodec.lambda$decode$2(KeyDispatchCodec.java:58) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.lambda$flatMap$10(DataResult.java:138) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.datafixers.util.Either$Left.map(Either.java:38) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.flatMap(DataResult.java:136) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.KeyDispatchCodec.decode(KeyDispatchCodec.java:56) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.MapDecoder.lambda$compressedDecode$0(MapDecoder.java:52) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.lambda$flatMap$10(DataResult.java:138) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.datafixers.util.Either$Left.map(Either.java:38) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.flatMap(DataResult.java:136) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.MapDecoder.compressedDecode(MapDecoder.java:52) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.MapCodec$MapCodecCodec.decode(MapCodec.java:91) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.Decoder.parse(Decoder.java:18) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.FieldDecoder.decode(FieldDecoder.java:29) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.MapCodec$1.decode(MapCodec.java:34) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.RecordCodecBuilder$Instance$3.decode(RecordCodecBuilder.java:249) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.RecordCodecBuilder$2.decode(RecordCodecBuilder.java:107) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.MapDecoder.lambda$compressedDecode$0(MapDecoder.java:52) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.lambda$flatMap$10(DataResult.java:138) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.datafixers.util.Either$Left.map(Either.java:38) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.flatMap(DataResult.java:136) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.MapDecoder.compressedDecode(MapDecoder.java:52) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.MapCodec$MapCodecCodec.decode(MapCodec.java:91) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.Decoder.parse(Decoder.java:18) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.BaseMapCodec.lambda$decode$2(BaseMapCodec.java:31) ~[datafixerupper-5.0.28.jar:?]
	at java.util.stream.ReduceOps$1ReducingSink.accept(ReduceOps.java:80) ~[?:?]
	at java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:197) ~[?:?]
	at java.util.Iterator.forEachRemaining(Iterator.java:133) ~[?:?]
	at java.util.Spliterators$IteratorSpliterator.forEachRemaining(Spliterators.java:1845) ~[?:?]
	at java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:509) ~[?:?]
	at java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:499) ~[?:?]
	at java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:921) ~[?:?]
	at java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234) ~[?:?]
	at java.util.stream.ReferencePipeline.reduce(ReferencePipeline.java:667) ~[?:?]
	at com.mojang.serialization.codecs.BaseMapCodec.decode(BaseMapCodec.java:27) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.UnboundedMapCodec.lambda$decode$0(UnboundedMapCodec.java:38) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.lambda$flatMap$10(DataResult.java:138) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.datafixers.util.Either$Left.map(Either.java:38) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.flatMap(DataResult.java:136) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.UnboundedMapCodec.decode(UnboundedMapCodec.java:38) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.Decoder$2.decode(Decoder.java:63) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.Codec$2.decode(Codec.java:71) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.Decoder.parse(Decoder.java:18) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.FieldDecoder.decode(FieldDecoder.java:29) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.MapCodec$1.decode(MapCodec.java:34) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.RecordCodecBuilder$Instance$1.decode(RecordCodecBuilder.java:183) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.RecordCodecBuilder$2.decode(RecordCodecBuilder.java:107) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.RecordCodecBuilder$Instance$3.decode(RecordCodecBuilder.java:249) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.codecs.RecordCodecBuilder$2.decode(RecordCodecBuilder.java:107) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.MapDecoder.lambda$compressedDecode$0(MapDecoder.java:52) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.lambda$flatMap$10(DataResult.java:138) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.datafixers.util.Either$Left.map(Either.java:38) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.flatMap(DataResult.java:136) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.MapDecoder.compressedDecode(MapDecoder.java:52) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.MapCodec$MapCodecCodec.decode(MapCodec.java:91) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.Decoder.parse(Decoder.java:18) ~[datafixerupper-5.0.28.jar:?]
	at exf.a(SourceFile:630) ~[23w07a.jar:?]
	at com.mojang.serialization.DataResult.lambda$flatMap$10(DataResult.java:138) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.datafixers.util.Either$Left.map(Either.java:38) ~[datafixerupper-5.0.28.jar:?]
	at com.mojang.serialization.DataResult.flatMap(DataResult.java:136) ~[datafixerupper-5.0.28.jar:?]
	at exf.a(SourceFile:630) ~[23w07a.jar:?]
	at adt.a(SourceFile:42) ~[23w07a.jar:?]
	at exf.a(SourceFile:614) ~[23w07a.jar:?]
	... 24 more
```
This cannot be fixed by clicking the "Reset to Default" button on the "Data pack validation failed!" pop-up.
Expected result
You would be able to perform this action, or you could no longer access the Experiments tab once it had been turned on.

## Comments (4)

### Comment 1: migrated (2023-02-15T12:05:44.146-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: [Mod] violine1101 (2023-02-15T12:10:50.629-0800)

This screen mentions that they can't be turned off after world creation, so almost definitely intentional.

### Comment 3: ampolive (2023-02-15T12:13:39.245-0800)

Does this action actually create a world? This happens when you don't click the "Create New World" button, which is why I think this could be unintentional.

### Comment 4: [Mod] violine1101 (2023-02-15T12:21:00.080-0800)

Apologies, I misunderstood your bug report - I thought you were talking about disabling these features after world creation, not while still on the create world screen. I could confirm this.
Edit: Reworded the bug report slightly such that this is hopefully a bit clearer
