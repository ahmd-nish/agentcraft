# MC-232104: Minecarts cause chunks to be corrupted/reset when loading worlds from before 1.5 (13w02a)

**Mojira URL:** [https://bugs.mojang.com/browse/MC-232104](https://bugs.mojang.com/browse/MC-232104)

## Report details

- **Mojira categories:** Datafixer
- **Project:** MC
- **Issue key:** MC-232104
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2021-07-14T07:21:23.791-0700
- **Updated:** 2025-04-26T13:40:27.104-0700
- **Resolution date:** 2024-11-05T16:09:43.039-0800
- **Affects versions:** 20w21a; 1.17.1; 21w39a; 1.18.1; 1.18.2; 1.19.1 Release Candidate 2; 1.20.2; 24w12a
- **Fix versions:** 1.20.5 Pre-Release 4
- **Area:** Platform
- **Labels:** chunk-corruption; data-fixer
- **Watchers:** 1
- **Attachments:** 12
- **Attachment filenames:** 2021-07-14_14.28.16.png; 2021-07-14_14.50.37.png; 2021-07-14_14.51.13.png; 2021-07-14_14.52.00.png; 2021-07-14_15.02.24.png; 2021-07-14_15.03.12.png; 2021-07-14_15.10.31.png; 2021-07-14_15.10.54.png; 2021-07-14_15.14.54.png; 2022-03-31_11.21.17.png; 2022-03-31_11.22.06.png; 2024-09-06_00.44.21.png
- **Issue links:** Duplicate:inward:MC-243097:Converting a world from 1.2.5 can delete structures depending on the biome | Relates:outward:MC-239962:When upgrade the old world, the existing building is seriously damaged, and the new terrain occurs on the existing terrain.

## Description

May relate to MC-134115 due to 1.13 changes being the current suspect.
The bug
In 13w02a, changes were made to the minecart entity ID. World saves from this version onwards can be safely upgraded to the current version (1.18.2). However, worlds from 13w01b or earlier (back to 12w07a) will cause any chunk that contains a minecart to be completely reset.
How to reproduce
This is as simple as creating a world in 13w01b or earlier, placing a minecart, and then loading that world in the latest version.
Example case
The following is a link to a world save last played in Java Edition 1.4.7 (the file size is rather large so it may be worth making a dedicated world yourself):
http://www.mediafire.com/file/pp1h388kzu2n7p7/Dataless822s_Survival_World_v1.0.zip/file
When loaded up and played in version 1.4.7, it plays completely fine. However, when loaded in the latest supported version, several chunks in the world fail to load, and are replaced with newly generated chunks. In pre-13w02a, the game log also produces errors indicating this:
Example output

```
Couldn't load chunk [-19, 14]
java.lang.ClassCastException: class com.mojang.serialization.DataResult cannot be cast to class com.mojang.datafixers.util.Pair (com.mojang.serialization.DataResult and com.mojang.datafixers.util.Pair are in unnamed module of loader 'app')
	at com.mojang.datafixers.optics.Proj2.view(Proj2.java:7)
	at com.mojang.datafixers.optics.Lens.lambda$null$0(Lens.java:48)
	at com.mojang.datafixers.optics.Affine$Instance.lambda$null$0(Affine.java:45)
	at com.mojang.datafixers.optics.Optics$5.preview(Optics.java:117)
	at com.mojang.datafixers.types.templates.TaggedChoice$TaggedChoiceType$2.capPreview(TaggedChoice.java:283)
	at com.mojang.datafixers.types.templates.TaggedChoice$TaggedChoiceType$2.preview(TaggedChoice.java:278)
	at com.mojang.datafixers.types.templates.TaggedChoice$TaggedChoiceType$2.preview(TaggedChoice.java:271)
	at com.mojang.datafixers.optics.Affine.lambda$null$2(Affine.java:34)
	at com.mojang.datafixers.optics.Traversal$Instance$1.lambda$wander$0(Traversal.java:34)
	at com.mojang.datafixers.util.Pair$Instance.traverse(Pair.java:90)
	at com.mojang.datafixers.optics.profunctors.TraversalP$1.lambda$wander$0(TraversalP.java:50)
	at com.mojang.datafixers.optics.Traversal$Instance$1.lambda$wander$0(Traversal.java:34)
	at com.mojang.datafixers.optics.Traversal$Instance$1.lambda$wander$0(Traversal.java:34)
	at com.mojang.datafixers.Typed.updateCap(Typed.java:164)
	at com.mojang.datafixers.Typed.update(Typed.java:138)
	at com.mojang.datafixers.Typed.update(Typed.java:133)
	at akb.a(SourceFile:18)
	at com.mojang.datafixers.DataFix.lambda$null$3(DataFix.java:86)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at com.mojang.datafixers.util.Either.lambda$mapRight$1(Either.java:166)
	at com.mojang.datafixers.util.Either$Right.map(Either.java:99)
	at com.mojang.datafixers.util.Either.mapRight(Either.java:166)
	at com.mojang.datafixers.FunctionType$Instance.lambda$right$6(FunctionType.java:104)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at com.mojang.datafixers.util.Either.lambda$mapRight$1(Either.java:166)
	at com.mojang.datafixers.util.Either$Right.map(Either.java:99)
	at com.mojang.datafixers.util.Either.mapRight(Either.java:166)
	at com.mojang.datafixers.FunctionType$Instance.lambda$right$6(FunctionType.java:104)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at com.mojang.datafixers.util.Either.lambda$mapRight$1(Either.java:166)
	at com.mojang.datafixers.util.Either$Right.map(Either.java:99)
	at com.mojang.datafixers.util.Either.mapRight(Either.java:166)
	at com.mojang.datafixers.FunctionType$Instance.lambda$right$6(FunctionType.java:104)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at com.mojang.datafixers.util.Either.lambda$mapRight$1(Either.java:166)
	at com.mojang.datafixers.util.Either$Right.map(Either.java:99)
	at com.mojang.datafixers.util.Either.mapRight(Either.java:166)
	at com.mojang.datafixers.FunctionType$Instance.lambda$right$6(FunctionType.java:104)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at com.mojang.datafixers.util.Either.lambda$mapRight$1(Either.java:166)
	at com.mojang.datafixers.util.Either$Right.map(Either.java:99)
	at com.mojang.datafixers.util.Either.mapRight(Either.java:166)
	at com.mojang.datafixers.FunctionType$Instance.lambda$right$6(FunctionType.java:104)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Fold.lambda$null$2(Fold.java:48)
	at com.mojang.datafixers.FunctionType$Instance.lambda$first$1(FunctionType.java:81)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at com.mojang.datafixers.FunctionType$Instance.lambda$first$1(FunctionType.java:81)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at com.mojang.datafixers.util.Either.lambda$mapRight$1(Either.java:166)
	at com.mojang.datafixers.util.Either$Right.map(Either.java:99)
	at com.mojang.datafixers.util.Either.mapRight(Either.java:166)
	at com.mojang.datafixers.FunctionType$Instance.lambda$right$6(FunctionType.java:104)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.util.Either.lambda$mapRight$1(Either.java:166)
	at com.mojang.datafixers.util.Either$Right.map(Either.java:99)
	at com.mojang.datafixers.util.Either.mapRight(Either.java:166)
	at com.mojang.datafixers.FunctionType$Instance.lambda$right$6(FunctionType.java:104)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Fold.lambda$null$2(Fold.java:48)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.FunctionType$Instance.lambda$null$3(FunctionType.java:93)
	at com.mojang.datafixers.optics.ListTraversal.lambda$wander$0(ListTraversal.java:19)
	at com.mojang.datafixers.FunctionType$Instance.lambda$wander$4(FunctionType.java:94)
	at com.mojang.datafixers.util.Either.lambda$mapRight$1(Either.java:166)
	at com.mojang.datafixers.util.Either$Right.map(Either.java:99)
	at com.mojang.datafixers.util.Either.mapRight(Either.java:166)
	at com.mojang.datafixers.FunctionType$Instance.lambda$right$6(FunctionType.java:104)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at com.mojang.datafixers.FunctionType$Instance.lambda$first$1(FunctionType.java:81)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.FunctionType$Instance.lambda$first$1(FunctionType.java:81)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at com.mojang.datafixers.FunctionType$Instance.lambda$first$1(FunctionType.java:81)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at java.base/java.util.function.Function.lambda$compose$0(Function.java:68)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69)
	at com.mojang.datafixers.types.Type.capWrite(Type.java:167)
	at com.mojang.datafixers.types.Type.lambda$readAndWrite$9(Type.java:159)
	at com.mojang.serialization.DataResult.lambda$flatMap$10(DataResult.java:138)
	at com.mojang.datafixers.util.Either$Left.map(Either.java:38)
	at com.mojang.serialization.DataResult.flatMap(DataResult.java:136)
	at com.mojang.datafixers.types.Type.readAndWrite(Type.java:158)
	at com.mojang.datafixers.DataFixerUpper.update(DataFixerUpper.java:84)
	at nm.a(SourceFile:488)
	at cnk.a(SourceFile:37)
	at abe.i(SourceFile:831)
	at abe.l(SourceFile:508)
	at java.base/java.util.concurrent.CompletableFuture$AsyncSupply.run(CompletableFuture.java:1764)
	at aqv.c(SourceFile:151)
	at abp$a.c(SourceFile:528)
	at aqv.z(SourceFile:125)
	at abp$a.z(SourceFile:537)
	at abp.d(SourceFile:280)
	at net.minecraft.server.MinecraftServer.bf(SourceFile:776)
	at net.minecraft.server.MinecraftServer.z(SourceFile:764)
	at aqv.c(SourceFile:134)
	at net.minecraft.server.MinecraftServer.y(SourceFile:749)
	at net.minecraft.server.MinecraftServer.b(SourceFile:521)
	at net.minecraft.server.MinecraftServer.e_(SourceFile:353)
	at faq.e(SourceFile:71)
	at net.minecraft.server.MinecraftServer.x(SourceFile:670)
	at net.minecraft.server.MinecraftServer.a(SourceFile:270)
	at java.base/java.lang.Thread.run(Thread.java:831)
```
Indeed, chunk [-19, 14] is in fact corrupted:

Expected results
Upgrading world would work regardless of whether a given chunk contains a minecart or not. Upgrading worlds (especially pure vanilla Survival worlds) should be as safe of a process as possible and cause no unexpected damage unrelated to intended game mechanic changes.
Actual results
The chunks containing a minecart are just completely reset. No attempt is made to even keep the terrain and delete the entity, the whole chunk is just gone.
Workarounds
This can be avoided by loading the world in a slightly later version (probably 13w02a to 17w46a but I can't be sure of it; 1.6.4 definitely works though) before the latest version, as this should convert the minecarts over to the new format which the current version can understand.

## Comments (10)

### Comment 1: migrated (2021-07-14T07:21:23.791-0700)

This comment contained multiple image attachments (12), please login to view the attachments.

### Comment 2: migrated (2021-10-03T10:59:06.836-0700)

Can confirm in 21w39a

### Comment 3: migrated (2021-11-21T12:18:19.213-0800)

Can confirm, just corrupted my world, fantastic!!

### Comment 4: migrated (2022-01-12T12:22:54.779-0800)

Confirming this issue in release versions 1.17.1 and 1.18.1, when attempting to load chunks from a 1.2.5 world that contain minecart entities.
EDIT: Use DataConverter library (built into PaperMC) as a workaround - you can use your world on Vanilla after the conversion.
1.17.1 log:

```[18:23:33] [Server thread/ERROR]: Couldn't load chunk [35, 9]
java.lang.ClassCastException: class com.mojang.serialization.DataResult cannot be cast to class com.mojang.datafixers.util.Pair (com.mojang.serialization.DataResult and com.mojang.datafixers.util.Pair are in unnamed module of loader 'app')
	at com.mojang.datafixers.optics.Proj2.view(Proj2.java:7) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.optics.Lens.lambda$null$0(Lens.java:48) ~[minecraft_server.1.17.1.jar:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at com.mojang.datafixers.util.Either.lambda$mapRight$1(Either.java:166) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either$Right.map(Either.java:99) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either.mapRight(Either.java:166) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.FunctionType$Instance.lambda$right$6(FunctionType.java:104) ~[minecraft_server.1.17.1.jar:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at com.mojang.datafixers.FunctionType$Instance.lambda$first$1(FunctionType.java:81) ~[minecraft_server.1.17.1.jar:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at com.mojang.datafixers.util.Either.lambda$mapRight$1(Either.java:166) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either$Right.map(Either.java:99) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either.mapRight(Either.java:166) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.FunctionType$Instance.lambda$right$6(FunctionType.java:104) ~[minecraft_server.1.17.1.jar:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at com.mojang.datafixers.util.Either.lambda$mapRight$1(Either.java:166) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either$Right.map(Either.java:99) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either.mapRight(Either.java:166) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.FunctionType$Instance.lambda$right$6(FunctionType.java:104) ~[minecraft_server.1.17.1.jar:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either.lambda$mapRight$1(Either.java:166) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either$Right.map(Either.java:99) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either.mapRight(Either.java:166) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.FunctionType$Instance.lambda$right$6(FunctionType.java:104) ~[minecraft_server.1.17.1.jar:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either.lambda$mapRight$1(Either.java:166) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either$Right.map(Either.java:99) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either.mapRight(Either.java:166) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.FunctionType$Instance.lambda$right$6(FunctionType.java:104) ~[minecraft_server.1.17.1.jar:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either.lambda$mapRight$1(Either.java:166) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either$Right.map(Either.java:99) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either.mapRight(Either.java:166) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.FunctionType$Instance.lambda$right$6(FunctionType.java:104) ~[minecraft_server.1.17.1.jar:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Fold.lambda$null$2(Fold.java:48) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.FunctionType$Instance.lambda$first$1(FunctionType.java:81) ~[minecraft_server.1.17.1.jar:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at com.mojang.datafixers.FunctionType$Instance.lambda$first$1(FunctionType.java:81) ~[minecraft_server.1.17.1.jar:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at com.mojang.datafixers.util.Either.lambda$mapRight$1(Either.java:166) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either$Right.map(Either.java:99) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either.mapRight(Either.java:166) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.FunctionType$Instance.lambda$right$6(FunctionType.java:104) ~[minecraft_server.1.17.1.jar:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either.lambda$mapRight$1(Either.java:166) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either$Right.map(Either.java:99) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either.mapRight(Either.java:166) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.FunctionType$Instance.lambda$right$6(FunctionType.java:104) ~[minecraft_server.1.17.1.jar:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Fold.lambda$null$2(Fold.java:48) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.FunctionType$Instance.lambda$null$3(FunctionType.java:93) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.optics.ListTraversal.lambda$wander$0(ListTraversal.java:19) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.FunctionType$Instance.lambda$wander$4(FunctionType.java:94) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either.lambda$mapRight$1(Either.java:166) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either$Right.map(Either.java:99) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either.mapRight(Either.java:166) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.FunctionType$Instance.lambda$right$6(FunctionType.java:104) ~[minecraft_server.1.17.1.jar:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at com.mojang.datafixers.FunctionType$Instance.lambda$first$1(FunctionType.java:81) ~[minecraft_server.1.17.1.jar:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.FunctionType$Instance.lambda$first$1(FunctionType.java:81) ~[minecraft_server.1.17.1.jar:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at com.mojang.datafixers.FunctionType$Instance.lambda$first$1(FunctionType.java:81) ~[minecraft_server.1.17.1.jar:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at java.util.function.Function.lambda$compose$0(Function.java:68) ~[?:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.functions.Comp.lambda$null$5(Comp.java:69) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.types.Type.capWrite(Type.java:167) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.types.Type.lambda$readAndWrite$9(Type.java:159) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.serialization.DataResult.lambda$flatMap$10(DataResult.java:138) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.util.Either$Left.map(Either.java:38) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.serialization.DataResult.flatMap(DataResult.java:136) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.types.Type.readAndWrite(Type.java:158) ~[minecraft_server.1.17.1.jar:?]
	at com.mojang.datafixers.DataFixerUpper.update(DataFixerUpper.java:84) ~[minecraft_server.1.17.1.jar:?]
	at nm.a(SourceFile:488) ~[minecraft_server.1.17.1.jar:?]
	at cnk.a(SourceFile:37) ~[minecraft_server.1.17.1.jar:?]
	at abe.i(SourceFile:831) ~[minecraft_server.1.17.1.jar:?]
	at abe.l(SourceFile:508) ~[minecraft_server.1.17.1.jar:?]
	at java.util.concurrent.CompletableFuture$AsyncSupply.run(CompletableFuture.java:1768) ~[?:?]
	at aqv.c(SourceFile:151) ~[minecraft_server.1.17.1.jar:?]
	at abp$a.c(SourceFile:528) ~[minecraft_server.1.17.1.jar:?]
	at aqv.z(SourceFile:125) ~[minecraft_server.1.17.1.jar:?]
	at abp$a.z(SourceFile:537) ~[minecraft_server.1.17.1.jar:?]
	at aqv.c(SourceFile:134) ~[minecraft_server.1.17.1.jar:?]
	at abp.a(SourceFile:140) ~[minecraft_server.1.17.1.jar:?]
	at bwq.a(SourceFile:187) ~[minecraft_server.1.17.1.jar:?]
	at bwt.a(SourceFile:140) ~[minecraft_server.1.17.1.jar:?]
	at bwq.d(SourceFile:181) ~[minecraft_server.1.17.1.jar:?]
	at bwq.m(SourceFile:176) ~[minecraft_server.1.17.1.jar:?]
	at bwq.b_(SourceFile:407) ~[minecraft_server.1.17.1.jar:?]
	at atg.l(SourceFile:1258) ~[minecraft_server.1.17.1.jar:?]
	at atg.ai(SourceFile:472) ~[minecraft_server.1.17.1.jar:?]
	at atu.ai(SourceFile:342) ~[minecraft_server.1.17.1.jar:?]
	at atg.k(SourceFile:444) ~[minecraft_server.1.17.1.jar:?]
	at atu.k(SourceFile:2308) ~[minecraft_server.1.17.1.jar:?]
	at bke.k(SourceFile:274) ~[minecraft_server.1.17.1.jar:?]
	at abs.l(SourceFile:466) ~[minecraft_server.1.17.1.jar:?]
	at acj.b(SourceFile:212) ~[minecraft_server.1.17.1.jar:?]
	at oe.a(SourceFile:238) ~[minecraft_server.1.17.1.jar:?]
	at aci.c(SourceFile:183) ~[minecraft_server.1.17.1.jar:?]
	at net.minecraft.server.MinecraftServer.b(SourceFile:902) ~[minecraft_server.1.17.1.jar:?]
	at aas.b(SourceFile:335) ~[minecraft_server.1.17.1.jar:?]
	at net.minecraft.server.MinecraftServer.a(SourceFile:831) ~[minecraft_server.1.17.1.jar:?]
	at net.minecraft.server.MinecraftServer.x(SourceFile:697) ~[minecraft_server.1.17.1.jar:?]
	at net.minecraft.server.MinecraftServer.a(SourceFile:270) ~[minecraft_server.1.17.1.jar:?]
	at java.lang.Thread.run(Thread.java:833) [?:?]```

### Comment 5: muzikbike (2022-03-30T13:09:12.192-0700)

A world I prepared in 1.6.4 did not face this issue, meaning that this stops being a problem some time between 1.4.7 and 1.6.4. I suspect 1.5 may contain such a cutoff as it made plenty changes to minecarts.

### Comment 6: muzikbike (2022-03-31T03:08:17.963-0700)

I've tested a 1.5 world and it upgraded just as expected. I now suspect 13w02a to be the first version to upgrade correctly as it split the minecart entity into multiple entity IDs which were previously shared. Results hopefully coming soon.

### Comment 7: muzikbike (2022-03-31T03:22:52.524-0700)

Version confirmed:

### Comment 8: ampolive (2023-11-07T17:06:28.659-0800)

The chunks are still regenerated in 1.20.2, but the errors are no longer logged (MC-265252).

### Comment 9: Ceresjanin123 (2024-09-05T15:46:13.750-0700)

I cannot reproduce this as of 24w36a. The world upgrades as normal, there are no errors in the console the specified chunk does not reset
Are you still able to reproduce this?

### Comment 10: Ceresjanin123 (2024-09-05T16:05:22.839-0700)

The upgrade behaves correctly on 1.21.1 as well. If someone could find the exact fix version that'd be neat
