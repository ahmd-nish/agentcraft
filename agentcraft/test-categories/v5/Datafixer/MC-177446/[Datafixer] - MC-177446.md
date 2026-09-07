# MC-177446: "RootVehicle" tag in playerdata entry is not upgraded

**Mojira URL:** [https://bugs.mojang.com/browse/MC-177446](https://bugs.mojang.com/browse/MC-177446)

## Report details

- **Mojira categories:** Datafixer
- **Project:** MC
- **Issue key:** MC-177446
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2020-04-04T15:37:53.562-0700
- **Updated:** 2025-03-25T13:24:40.809-0700
- **Resolution date:** 2023-11-07T04:26:15.654-0800
- **Affects versions:** 20w14a; 1.17 Pre-release 2
- **Fix versions:** 23w45a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** 1.10 world.zip

## Description

The bug
It appears that the RootVehicle tag of playerdata entries is not upgraded. This can cause missing or malformed NBT data for the vehicle and even prevent loading the vehicle at all if its entity id changed in newer versions. Other tags might be affected as well.
This does however not affect the Player tag of the level.dat file. Therefore this can usually only be observed when upgrading worlds created by a dedicated server (server.jar), or when manually removing the Player tag from the level.dat file of a singleplayer world.
How to reproduce (singleplayer world)
- Download and extract the world

-  and place it in the saves folder of your installation

- Open the world in the latest version
 You fall through the ground and the following warning is logged:
20w14a

```
Exception loading entity:
t: Non [a-z0-9/._-] character in path of location: minecraft:Boat
	at tr.<init>(SourceFile:38)
	at tr.<init>(SourceFile:43)
	at ang.a(SourceFile:490)
	at ang.a(SourceFile:461)
	at ang.b(SourceFile:514)
	at ang.a(SourceFile:495)
	at aav.a(SourceFile:205)
	at ze.c(SourceFile:111)
	at ze.b(SourceFile:63)
	at ly.a(SourceFile:230)
	at zb.c(SourceFile:171)
	at net.minecraft.server.MinecraftServer.b(SourceFile:864)
	at net.minecraft.server.MinecraftServer.a(SourceFile:791)
	at ell.a(SourceFile:128)
	at net.minecraft.server.MinecraftServer.run(SourceFile:650)
	at java.lang.Thread.run(Thread.java:745)
```

How to reproduce (server)
- Download a 1.10.2 server (link can be found on the Wiki)

- Join the server

- To verify that upgrading of other tags works correctly:
- Spawn some mobs around you with spawn eggs

- Put some items in your hotbar whose ids changed in newer versions, e.g. andesite

- Place a boat and enter it

- While sitting in the boat, leave the server

- Stop the server, download a the server .jar of the latest version and start it with the same world

- Join the server
 You are not riding a boat anymore and the following warning is logged:
20w14a

```
[00:19:25 WARN]: Exception loading entity:
t: Non [a-z0-9/._-] character in path of location: minecraft:Boat
	at tr.<init>(SourceFile:38) ~[20w14a.jar:?]
	at tr.<init>(SourceFile:43) ~[20w14a.jar:?]
	at ang.a(SourceFile:490) ~[20w14a.jar:?]
	at ang.a(SourceFile:461) ~[20w14a.jar:?]
	at ang.b(SourceFile:514) [20w14a.jar:?]
	at ang.a(SourceFile:495) [20w14a.jar:?]
	at aav.a(SourceFile:205) [20w14a.jar:?]
	at ze.c(SourceFile:111) [20w14a.jar:?]
	at ze.b(SourceFile:63) [20w14a.jar:?]
	at ly.a(SourceFile:230) [20w14a.jar:?]
	at zb.c(SourceFile:171) [20w14a.jar:?]
	at net.minecraft.server.MinecraftServer.b(SourceFile:864) [20w14a.jar:?]
	at xk.b(SourceFile:345) [20w14a.jar:?]
	at net.minecraft.server.MinecraftServer.a(SourceFile:791) [20w14a.jar:?]
	at net.minecraft.server.MinecraftServer.run(SourceFile:650) [20w14a.jar:?]
	at java.lang.Thread.run(Thread.java:834) [?:?]
```

## Comments (1)

### Comment 1: migrated (2020-04-04T15:37:53.562-0700)

This comment contained an image attachment, please login to view the attachment.
