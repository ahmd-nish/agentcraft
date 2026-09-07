# MC-275790: Non-existent entries in certain tags that are not required causes validation error

**Mojira URL:** [https://bugs.mojang.com/browse/MC-275790](https://bugs.mojang.com/browse/MC-275790)

## Report details

- **Mojira categories:** Data Packs
- **Project:** MC
- **Issue key:** MC-275790
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2024-08-21T10:35:37.877-0700
- **Updated:** 2025-04-26T16:23:23.496-0700
- **Resolution date:** 2024-09-27T05:44:21.691-0700
- **Affects versions:** 24w34a; 24w35a; 24w36a; 24w37a; 24w38a; 24w39a
- **Fix versions:** 24w40a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** deobf_latest.log; latest.log; MC-275790.zip
- **Issue links:** Duplicate:inward:MC-276140:Required:false not working in any tag list

## Description

If a biome, structure, enchantment, or loot table tag is included in a data pack, which includes an entry with required set to false, and that biome/structure/enchantment/loot_table ID is not present in any data packs, the data pack fails to validate and the game tries to launch in Safe Mode. The output log produces this error (example with biome tag):
deobf_latest.log

```
[Render thread/ERROR]: Registry loading errors:
> Errors in registry minecraft:root:
>> Errors in element minecraft:worldgen/biome:
java.lang.IllegalStateException: Unbound values in registry ResourceKey[minecraft:root / minecraft:worldgen/biome]: [test:test]
	at net.minecraft.core.MappedRegistry.net.minecraft.core.Registry freeze()(MappedRegistry.java:333)
	at net.minecraft.resources.RegistryDataLoader.void lambda$load$6(java.util.Map,net.minecraft.resources.RegistryDataLoader$Loader)(RegistryDataLoader.java:188)
	at java.base/java.lang.Iterable.forEach(Iterable.java:75)
	at net.minecraft.resources.RegistryDataLoader.net.minecraft.core.RegistryAccess$Frozen load(net.minecraft.resources.RegistryDataLoader$LoadingFunction,java.util.List,java.util.List)(RegistryDataLoader.java:185)
	at net.minecraft.resources.RegistryDataLoader.net.minecraft.core.RegistryAccess$Frozen load(net.minecraft.server.packs.resources.ResourceManager,java.util.List,java.util.List)(RegistryDataLoader.java:164)
	at net.minecraft.resources.RegistryDataLoader.void lambda$load$2(net.minecraft.server.packs.resources.ResourceManager,net.minecraft.resources.RegistryDataLoader$Loader,net.minecraft.resources.RegistryOps$RegistryInfoLookup)(RegistryDataLoader.java:164)
	at net.minecraft.server.WorldLoader.java.util.concurrent.CompletableFuture load(net.minecraft.server.WorldLoader$InitConfig,net.minecraft.server.WorldLoader$WorldDataSupplier,net.minecraft.server.WorldLoader$ResultFactory,java.util.concurrent.Executor,java.util.concurrent.Executor)(WorldLoader.java:41)
	at net.minecraft.client.gui.screens.worldselection.CreateWorldScreen.void applyNewPackConfig(net.minecraft.server.packs.repository.PackRepository,net.minecraft.world.level.WorldDataConfiguration,java.util.function.Consumer)(CreateWorldScreen.java:574)
	at net.minecraft.client.gui.screens.worldselection.CreateWorldScreen.void tryApplyNewDataPacks(net.minecraft.server.packs.repository.PackRepository,boolean,java.util.function.Consumer)(CreateWorldScreen.java:564)
	at net.minecraft.client.gui.screens.worldselection.CreateWorldScreen.void lambda$openDataPackSelectionScreen$8(net.minecraft.server.packs.repository.PackRepository)(CreateWorldScreen.java:536)
	at net.minecraft.client.gui.screens.packs.PackSelectionModel.void commit()(PackSelectionModel.java:56)
	at net.minecraft.client.gui.screens.packs.PackSelectionScreen.void onClose()(PackSelectionScreen.java:94)
	at net.minecraft.client.gui.screens.packs.PackSelectionScreen.void lambda$init$1(net.minecraft.client.gui.components.Button)(PackSelectionScreen.java:124)
	at net.minecraft.client.gui.components.Button.void onPress()(Button.java:96)
	at net.minecraft.client.gui.components.AbstractButton.void onClick(double,double)(AbstractButton.java:43)
	at net.minecraft.client.gui.components.AbstractWidget.boolean mouseClicked(double,double,int)(AbstractWidget.java:141)
	at net.minecraft.client.gui.components.AbstractWidget.void updateWidgetNarration(net.minecraft.client.gui.narration.NarrationElementOutput)(AbstractWidget.java:141)
	at net.minecraft.client.gui.components.events.ContainerEventHandler.boolean mouseClicked(double,double,int)(ContainerEventHandler.java:38)
	at net.minecraft.client.gui.components.events.ContainerEventHandler.void setFocused(net.minecraft.client.gui.components.events.GuiEventListener)(ContainerEventHandler.java:38)
	at net.minecraft.client.MouseHandler.void lambda$onPress$0(boolean[],net.minecraft.client.gui.screens.Screen,double,double,int)(MouseHandler.java:111)
	at net.minecraft.client.gui.screens.Screen.void wrapScreenError(java.lang.Runnable,java.lang.String,java.lang.String)(Screen.java:429)
	at net.minecraft.client.MouseHandler.void onPress(long,int,int,int)(MouseHandler.java:111)
	at net.minecraft.client.MouseHandler.void lambda$setup$4(long,int,int,int)(MouseHandler.java:189)
	at net.minecraft.util.thread.BlockableEventLoop.void execute(java.lang.Runnable)(BlockableEventLoop.java:110)
	at net.minecraft.client.MouseHandler.void lambda$setup$5(long,int,int,int)(MouseHandler.java:189)
	at org.lwjgl.glfw.GLFWMouseButtonCallbackI.null callback(null)(GLFWMouseButtonCallbackI.java:43)
	at org.lwjgl.system.JNI.null invokeV(null)(JNI.java)
	at org.lwjgl.glfw.GLFW.null glfwWaitEventsTimeout(null)(GLFW.java:3509)
	at com.mojang.blaze3d.systems.RenderSystem.void limitDisplayFPS(int)(RenderSystem.java:178)
	at net.minecraft.client.Minecraft.void runTick(boolean)(Minecraft.java:1327)
	at net.minecraft.client.Minecraft.void run()(Minecraft.java:898)
	at net.minecraft.client.main.Main.void main(java.lang.String[])(Main.java:256)
[Render thread/WARN]: Failed to validate datapack
java.util.concurrent.CompletionException: net.minecraft.ReportedException: Registry Loading
	at java.base/java.util.concurrent.CompletableFuture.encodeThrowable(CompletableFuture.java:332) ~[?:?]
	at java.base/java.util.concurrent.CompletableFuture.uniApplyNow(CompletableFuture.java:674) ~[?:?]
	at java.base/java.util.concurrent.CompletableFuture.uniApplyStage(CompletableFuture.java:662) ~[?:?]
	at java.base/java.util.concurrent.CompletableFuture.thenApply(CompletableFuture.java:2200) ~[?:?]
	at net.minecraft.client.gui.screens.worldselection.CreateWorldScreen.void applyNewPackConfig(net.minecraft.server.packs.repository.PackRepository,net.minecraft.world.level.WorldDataConfiguration,java.util.function.Consumer)(CreateWorldScreen.java:604) ~[24w34a.jar:?]
	at net.minecraft.client.gui.screens.worldselection.CreateWorldScreen.void tryApplyNewDataPacks(net.minecraft.server.packs.repository.PackRepository,boolean,java.util.function.Consumer)(CreateWorldScreen.java:564) ~[24w34a.jar:?]
	at net.minecraft.client.gui.screens.worldselection.CreateWorldScreen.void lambda$openDataPackSelectionScreen$8(net.minecraft.server.packs.repository.PackRepository)(CreateWorldScreen.java:536) ~[24w34a.jar:?]
	at net.minecraft.client.gui.screens.packs.PackSelectionModel.void commit()(PackSelectionModel.java:56) ~[24w34a.jar:?]
	at net.minecraft.client.gui.screens.packs.PackSelectionScreen.void onClose()(PackSelectionScreen.java:94) ~[24w34a.jar:?]
	at net.minecraft.client.gui.screens.packs.PackSelectionScreen.void lambda$init$1(net.minecraft.client.gui.components.Button)(PackSelectionScreen.java:124) ~[24w34a.jar:?]
	at net.minecraft.client.gui.components.Button.void onPress()(Button.java:96) ~[24w34a.jar:?]
	at net.minecraft.client.gui.components.AbstractButton.void onClick(double,double)(AbstractButton.java:43) ~[24w34a.jar:?]
	at net.minecraft.client.gui.components.AbstractWidget.boolean mouseClicked(double,double,int)(AbstractWidget.java:141) ~[24w34a.jar:?]
	at net.minecraft.client.gui.components.AbstractWidget.void updateWidgetNarration(net.minecraft.client.gui.narration.NarrationElementOutput)(AbstractWidget.java:141) ~[24w34a.jar:?]
	at net.minecraft.client.gui.components.events.ContainerEventHandler.boolean mouseClicked(double,double,int)(ContainerEventHandler.java:38) ~[24w34a.jar:?]
	at net.minecraft.client.gui.components.events.ContainerEventHandler.void setFocused(net.minecraft.client.gui.components.events.GuiEventListener)(ContainerEventHandler.java:38) ~[24w34a.jar:?]
	at net.minecraft.client.MouseHandler.void lambda$onPress$0(boolean[],net.minecraft.client.gui.screens.Screen,double,double,int)(MouseHandler.java:111) ~[24w34a.jar:?]
	at net.minecraft.client.gui.screens.Screen.void wrapScreenError(java.lang.Runnable,java.lang.String,java.lang.String)(Screen.java:429) ~[24w34a.jar:?]
	at net.minecraft.client.MouseHandler.void onPress(long,int,int,int)(MouseHandler.java:111) ~[24w34a.jar:?]
	at net.minecraft.client.MouseHandler.void lambda$setup$4(long,int,int,int)(MouseHandler.java:189) ~[24w34a.jar:?]
	at net.minecraft.util.thread.BlockableEventLoop.void execute(java.lang.Runnable)(BlockableEventLoop.java:110) ~[24w34a.jar:?]
	at net.minecraft.client.MouseHandler.void lambda$setup$5(long,int,int,int)(MouseHandler.java:189) ~[24w34a.jar:?]
	at org.lwjgl.glfw.GLFWMouseButtonCallbackI.callback(GLFWMouseButtonCallbackI.java:43) [lwjgl-glfw-3.3.3.jar:build 5]
	at org.lwjgl.system.JNI.null invokeV(null)(JNI.java) ~[lwjgl-3.3.3.jar:build 5]
	at org.lwjgl.glfw.GLFW.glfwWaitEventsTimeout(GLFW.java:3509) [lwjgl-glfw-3.3.3.jar:build 5]
	at com.mojang.blaze3d.systems.RenderSystem.limitDisplayFPS(SourceFile:178) [24w34a.jar:?]
	at fil.c(SourceFile:1327) [24w34a.jar:?]
	at fil.f(SourceFile:898) [24w34a.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:256) [24w34a.jar:?]
Caused by: net.minecraft.ReportedException: Registry Loading
	at net.minecraft.resources.RegistryDataLoader.net.minecraft.ReportedException createReportWithBriefInfo(java.util.Map)(RegistryDataLoader.java:267) ~[24w34a.jar:?]
	at net.minecraft.resources.RegistryDataLoader.net.minecraft.ReportedException logErrors(java.util.Map)(RegistryDataLoader.java:232) ~[24w34a.jar:?]
	at net.minecraft.resources.RegistryDataLoader.net.minecraft.core.RegistryAccess$Frozen load(net.minecraft.resources.RegistryDataLoader$LoadingFunction,java.util.List,java.util.List)(RegistryDataLoader.java:199) ~[24w34a.jar:?]
	at net.minecraft.resources.RegistryDataLoader.net.minecraft.core.RegistryAccess$Frozen load(net.minecraft.server.packs.resources.ResourceManager,java.util.List,java.util.List)(RegistryDataLoader.java:164) ~[24w34a.jar:?]
	at net.minecraft.resources.RegistryDataLoader.void lambda$load$2(net.minecraft.server.packs.resources.ResourceManager,net.minecraft.resources.RegistryDataLoader$Loader,net.minecraft.resources.RegistryOps$RegistryInfoLookup)(RegistryDataLoader.java:164) ~[24w34a.jar:?]
	at net.minecraft.server.WorldLoader.java.util.concurrent.CompletableFuture load(net.minecraft.server.WorldLoader$InitConfig,net.minecraft.server.WorldLoader$WorldDataSupplier,net.minecraft.server.WorldLoader$ResultFactory,java.util.concurrent.Executor,java.util.concurrent.Executor)(WorldLoader.java:41) ~[24w34a.jar:?]
	at net.minecraft.client.gui.screens.worldselection.CreateWorldScreen.void applyNewPackConfig(net.minecraft.server.packs.repository.PackRepository,net.minecraft.world.level.WorldDataConfiguration,java.util.function.Consumer)(CreateWorldScreen.java:574) ~[24w34a.jar:?]
	... 22 more
Caused by: java.lang.IllegalStateException: Failed to load registries due to errors
	at net.minecraft.resources.RegistryDataLoader.net.minecraft.ReportedException createReportWithBriefInfo(java.util.Map)(RegistryDataLoader.java:251) ~[24w34a.jar:?]
	at net.minecraft.resources.RegistryDataLoader.net.minecraft.ReportedException logErrors(java.util.Map)(RegistryDataLoader.java:232) ~[24w34a.jar:?]
	at net.minecraft.resources.RegistryDataLoader.net.minecraft.core.RegistryAccess$Frozen load(net.minecraft.resources.RegistryDataLoader$LoadingFunction,java.util.List,java.util.List)(RegistryDataLoader.java:199) ~[24w34a.jar:?]
	at net.minecraft.resources.RegistryDataLoader.net.minecraft.core.RegistryAccess$Frozen load(net.minecraft.server.packs.resources.ResourceManager,java.util.List,java.util.List)(RegistryDataLoader.java:164) ~[24w34a.jar:?]
	at net.minecraft.resources.RegistryDataLoader.void lambda$load$2(net.minecraft.server.packs.resources.ResourceManager,net.minecraft.resources.RegistryDataLoader$Loader,net.minecraft.resources.RegistryOps$RegistryInfoLookup)(RegistryDataLoader.java:164) ~[24w34a.jar:?]
	at net.minecraft.server.WorldLoader.java.util.concurrent.CompletableFuture load(net.minecraft.server.WorldLoader$InitConfig,net.minecraft.server.WorldLoader$WorldDataSupplier,net.minecraft.server.WorldLoader$ResultFactory,java.util.concurrent.Executor,java.util.concurrent.Executor)(WorldLoader.java:41) ~[24w34a.jar:?]
	at net.minecraft.client.gui.screens.worldselection.CreateWorldScreen.void applyNewPackConfig(net.minecraft.server.packs.repository.PackRepository,net.minecraft.world.level.WorldDataConfiguration,java.util.function.Consumer)(CreateWorldScreen.java:574) ~[24w34a.jar:?]
	... 22 more
```
And then lists the IDs that were listed, but are missing.
Expected behavior is that if these IDs are not present among any loaded data packs, because they are not required, the game will ignore them for these tags and validate without them.
Steps to recreate:
- Create a tag in <namespace>/tags/worldgen/biome

- Make this tag include at least one biome that does not exist, as an object with "required": false. For example, "test:test"

- Attempt to load the data pack in a world

- Observe that the game attempts to load the world in Safe Mode, and the output log has produced the above error.

- Perform the same test in 1.21.1 and note that the data pack validates as expected.

Example tag for convenience:

```
{
  "values": [
    "minecraft:plains",
    {
      "id": "test:test",
      "required": false
    }
  ]
}
```

## Comments (10)

### Comment 1: migrated (2024-08-21T10:35:37.877-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: Jarl-Penguin (2024-08-22T12:19:06.452-0700)

Attached a sample data pack that can be used to reproduce the issue.

### Comment 3: kanokarob (2024-08-28T09:07:53.243-0700)

Bug persists in 24w35a

### Comment 4: jacobsjo (2024-08-28T17:20:47.255-0700)

This affects other types of tags too. It appears to affect all tags of registries whose entries are controlled through datapacks. Specifically, I've tested tags/worldgen/structure, tags/enchantment, and tags/loot_table.
Other tags are working as expected. Specifically, I've tested tags/block.

### Comment 5: migrated (2024-09-04T08:19:30.110-0700)

Bug persists in 24w36a

### Comment 6: Ellivers (2024-09-09T01:33:12.701-0700)

Could you change the title to show that it is also caused by other types of tags?

### Comment 7: migrated (2024-09-12T02:05:28.922-0700)

Bug persists in 24w37a

### Comment 8: migrated (2024-09-15T04:24:34.726-0700)

Are there any news on this one? If this persists it will prevent us from making a lot of data packs compatible with others.

### Comment 9: migrated (2024-09-19T04:06:01.710-0700)

Bug persists in 24w38a

### Comment 10: migrated (2024-09-25T07:17:15.043-0700)

Bug persists in 24w39a
