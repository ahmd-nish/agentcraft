# MC-74984: Client continues to connect to server after canceling on 'Connecting to server' screen

**Mojira URL:** [https://bugs.mojang.com/browse/MC-74984](https://bugs.mojang.com/browse/MC-74984)

## Report details

- **Mojira categories:** Networking
- **Project:** MC
- **Issue key:** MC-74984
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2014-12-01T12:42:26.527-0800
- **Updated:** 2025-04-26T03:56:02.543-0700
- **Resolution date:** 2024-12-08T13:52:42.297-0800
- **Affects versions:** Minecraft 1.8; Minecraft 1.8.1; Minecraft 1.8.3; Minecraft 1.8.4; Minecraft 1.8.7; Minecraft 1.8.8; Minecraft 1.8.9; Minecraft 1.9.1; Minecraft 1.9.2; Minecraft 1.9.4; Minecraft 1.10; Minecraft 1.11.2; Minecraft 17w16b; Minecraft 1.12; Minecraft 1.12.2; Minecraft 1.13; Minecraft 18w31a; Minecraft 1.13.1; 1.14.4; 1.15.2; 20w13b; 1.16 Pre-release 5; 1.16.1; 1.16.2; 1.16.3; 1.16.4; 20w51a; 1.16.5 Release Candidate 1; 1.16.5; 1.19
- **Fix versions:** 1.20 Pre-release 5
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 16
- **Attachment filenames:** 2014-12-01_21.25.56.png; 2014-12-01_21.26.08.png; 2014-12-01_21.29.31.png; 2015-12-30_20.59.40.png; 2020-12-10_19.20.14.png; 2020-12-10_19.20.17.png; 2020-12-10_19.20.20.png; 2020-12-10_19.20.36.png; 2020-12-10_19.30.17.png; 2020-12-10_19.49.16.png; 2020-12-10_19.55.18.png; image-2021-08-27-11-15-30-269.png; image-2022-07-04-15-06-29-652.png; IMG_5051.mov; latest.log; Untitled video - Made with Clipchamp.mp4
- **Issue links:** Relates:inward:MC-128953:Connection to server not closed after continuing after an OutOfMemory error | Relates:inward:MC-133757:Day and Night Flash | Duplicate:inward:MC-120072:Server chat merges when connecting to another server | Duplicate:inward:MC-227783:Being connected to 2 servers at once. | Duplicate:inward:MC-223001:Canceling a connection to a Realm causes desink between client and realm | Duplicate:inward:MC-221137:Multiplayer-singleplayer weird bug | Duplicate:inward:MC-220566:Joining server + realm at same time allows player to get effected by gamemode commands and fly on any server. | Duplicate:inward:MC-218188:Aborting connection to a server quickly allows to connect to multiple servers | Duplicate:inward:MC-217487:It has been observed that one player is on multiple servers. | Duplicate:inward:MC-217226:Joining servers too quickly causes your client to be in 2 servers at once. | Duplicate:inward:MC-77819:Returning To Server-list And Not Main Menu | Duplicate:inward:MC-214284:Killed on a Realm server while in a single player world | Duplicate:inward:MC-212374:Connected to two servers at once | Duplicate:inward:MC-212019:1.16.5 Realms/Singleplayer bug | Duplicate:inward:MC-211372:Cancel joining a realm won't fully cancel the joining of the realm | Duplicate:inward:MC-210104:Trying to join a multiplayer server and cancelling right after, gives you the items inside of a singleplayer world. | Duplicate:inward:MC-96306:I am in 2 servers at a time | Duplicate:inward:MC-159329:Chat Bug | Relates:outward:MC-12989:Chat from a server connected to using direct connect sometimes remains in chat when joining another server. | Duplicate:inward:MC-95139:Client can connect to 2 servers at once | Duplicate:inward:MC-93790:Chat from one server shows on another | Duplicate:inward:MC-121210:Connecting to 2 servers at the same time | Duplicate:inward:MC-90327:Playing on two servers at once | Relates:inward:MC-78113:Disconnecting after death on hardcore mode server does not close connection to server | Duplicate:inward:MC-201222:Online Server Chat loaded in Singleplayer | Duplicate:inward:MC-199683:The teleportation problem about joining the server | Duplicate:inward:MC-199622:weird server bug | Duplicate:inward:MC-199554:Singleplayer and Multiplayer Loading issue | Duplicate:inward:MC-195177:Two worlds loading at once Xray bug | Duplicate:inward:MC-192726:Joined to 2 servers at once | Duplicate:inward:MC-194209:Minecraft Realms and Multiplayer Combination | Duplicate:inward:MC-193519:Collision breaks after canceling a connection to a multiplayer server, and joining a singleplayer world after | Duplicate:inward:MC-189592:Cancel connection to the server, don't cancel it. | Duplicate:inward:MC-186451:Inventory and map get carried over to a second server when rapidly switching servers | Duplicate:inward:MC-178732:I got into 2 minecraft servers at once | Duplicate:inward:MC-176812:Pressing cancel when logging into a server does not cancel joining the server | Duplicate:inward:MC-168999:2 servers merged into 1? | Duplicate:inward:MC-168846:Canceling joining server and then joining singleplayer-world does wired stuff | Duplicate:inward:MC-151614:Game thinks I'm on a different world | Duplicate:inward:MC-137115:In two servers at the same time | Duplicate:inward:MC-103846:Summary Connected to local and external server at the same | Duplicate:inward:MC-129533:Server "combination" issues | Duplicate:inward:MC-127677:Render Glitch changing servers | Relates:inward:MC-124615:Overworld terrain generation in Nether | Duplicate:inward:MC-108646:Connected to multiple servers at once | Duplicate:inward:MC-116504:Canceling entry to a server does not work. | Duplicate:inward:MC-113526:multiple people on a singleplayer world without lan | Relates:inward:MC-88299:Client freezes then disconnects with java.io.IOException: Error while write(...) when trying to join a server | Duplicate:inward:MC-103951:Multiplayer login issue | Duplicate:inward:MC-100686:Client can connect to multiple servers at once | Duplicate:inward:MC-96985:Client's server list can be lightly spammed and break joining servers | Duplicate:inward:MC-87667:double clicking a server before joining a server results in minecraft attempting to connect to both servers | Duplicate:inward:MC-93545:Join server multiple times on double click | Duplicate:inward:MC-94663:Attempting to join a server, canceling, connecting to another server cancelling then connecting to the first server, but ending up in the second server. | Duplicate:inward:MC-75183:Multiple instances (different to double instances due to lag) | Duplicate:inward:MC-81678:confusing chat | Duplicate:inward:MC-80226:Connecting to two servers at once | Duplicate:inward:MC-79627:Connecting to multiple servers at the same time | Duplicate:inward:MC-80144:Loading two servers with one Minecraft instance. | Duplicate:inward:MC-78448:Join Multiple Servers with ONE Client | Duplicate:inward:MC-76663:Connected to multiple servers simultaneously on the same client. | Relates:outward:REALMS-5078:Realms "Cancel Join" button does not stop the client from joining the realm | Duplicate:inward:REALMS-5531:After clicking on a realm and clicking cancel, sometimes it will send you to the realm while you are on the server select screen. | Relates:inward:REALMS-1178:Try to cancel loading a realm

## Description

I am on one server and i can read the chat from both of them.
Steps to Reproduce:
1. I started Minecraft 1.8
2. I joined a multiplayer server and while it was loading to found out that i joined the wrong one (CubeKrowd)
3. While it was still loading i cancled
4. I clicked on the right server and joind a world where only a few things where and i was in spectator mode although I should have only been in creative. At that point i could read both chats.
5. I disconnected and logged back in and now the world was normal but still there where both chats
And even if i disconnect again the cubekrowd chat is still there. I tested going to a few different servers but the chat was always there.
When i restarted the game it was gone

Being connected to two servers at a time (MC-74984) can be exploited:
- Illegal movement (e.g. "phasing" through blocks), to some extent

- Item transfer when in Creative mode

- X-ray

See https://www.youtube.com/watch?v=EEG_c3ycDg4

## Comments (27)

### Comment 1: migrated (2014-12-01T12:42:26.527-0800)

This comment contained multiple image attachments (16), please login to view the attachments.

### Comment 2: migrated (2014-12-01T13:18:54.721-0800)

ivalid, modded server, the chat and plots say it all

### Comment 3: migrated (2014-12-01T13:29:15.280-0800)

The server i took thr pics on is a vanilla one....the plots were generated using commandblocks but you are right the chat is from cubekrowd

### Comment 4: migrated (2014-12-01T13:40:36.395-0800)

IF the plots are made with command blocks, it is still invalid because of the chat messages
"Entering new CubeKrowd Lobby!"
and in front of the names: [M], [R], [T], [G]

### Comment 5: migrated (2014-12-01T14:23:15.546-0800)

CubeKrowd is modded, you will need to contact them if you want any support on that server.

### Comment 6: migrated (2015-02-20T14:43:26.830-0800)

Confirmed on vanilla.

### Comment 7: migrated (2015-04-17T13:06:14.749-0700)

MC-78113 is related to/a duplicate of this one, but it contains a lot of information that might be useful.

### Comment 8: migrated (2015-04-19T10:33:00.025-0700)

This is not a duplicate issue to mine reported at MC-78113 as my issue CAN NOT be created in clients below 1.8.3 unlike what is described here. Related maybe but not a duplicate.

### Comment 9: migrated (2015-06-10T15:35:10.988-0700)

Here is a way of easy reproduction with any client and any server:
1. Increase your lookup-time for a servers DNS/IP (see start of the video)
(This can be done by using a proxyserver and forcing DNS-Lookups via the proxy)
2. Use "REFRESH" to mark all servers as "unknown" for a little while
3. Connect to two servers shortly after another.
Video:
https://www.youtube.com/watch?v=OpsrZB0x17I
- Refreshing to show the resolve-latency

- Connecting with a little delay (second connect 200ms later)

- Visibly connection to two servers shortly after another

- Flickering sky as one server has night and one has daytime

- Commands upto 2015-06-11 00:18:13 are only registered on Server 1

- "/chunk vd 5" forces a world-Change-Event with a 5-chunk viewdistance this forces a disconnect somehow from server 1

- All additionall commands are registered by Server 2

- TAB-Shows other players

Serverlog Server 1:

```[2015-06-11 00:17:37 INFO]: Kademlia[5] logged in with entity id 5850 at ([world]920.5143804149387, 68.0, 2184.500539235966)
[2015-06-11 00:17:38 WARN]: Kademlia moved too quickly! -904.3122679052309,9.0,-1787.1306913904555 (904.3122679052309, 9.0, 1787.1306913904555)
[2015-06-11 00:17:52 INFO]: Kademlia issued server command: /v
[2015-06-11 00:17:54 INFO]: Kademlia issued server command: /lag
[2015-06-11 00:17:56 INFO]: Kademlia issued server command: /list
[2015-06-11 00:18:04 INFO]: Kademlia issued server command: /w spawn
[2015-06-11 00:18:13 INFO]: Kademlia issued server command: /chunk vd 5
[2015-06-11 00:18:16 INFO]: Saved 1 players in 1 MS.
[2015-06-11 00:19:01 INFO]: Kademlia lost connection: Disconnected```
Serverlog Server 2:

```2015-06-11 00:17:38] [Server thread/INFO]: Kademlia[1] logged in with entity id 5997165 at ([world]16.202112509707884, 77.0, 397.36984784551026)
[2015-06-11 00:18:14] [Server thread/WARN]: Kademlia moved too quickly! -126.60349590885434,-12.0,249.28627572675515
[2015-06-11 00:18:25] [Server thread/INFO]: Kademlia issued server command: /chunk vd 15
[2015-06-11 00:18:40] [Server thread/INFO]: Kademlia issued server command: /w spawn```

### Comment 10: marcono1234 (2015-06-21T05:43:29.000-0700)

Confirmed for
- 1.8.7 However I cannot reproduce it in the way  did

How to reproduce:
- Open server list

- Press F5 until the servers are all marked as "pinging" and it stays like this for a while

- Click on the "Play" arrow on one of the server images and press ESC at the same time (You should now be in the main menu of Minecraft)

- Click "Multiplayer" and select any other server

Note: The client doesn't even cancel the updates when leaving the latest server and entering singleplayer but instead uses the same packages which causes the player to be teleported for example
Some error messages

```java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
	at bcy.a(SourceFile:964) ~[1.8.7.jar:?]
	at gq.a(SourceFile:45) ~[1.8.7.jar:?]
	at gq.a(SourceFile:10) ~[1.8.7.jar:?]
	at fh$1.run(SourceFile:13) ~[1.8.7.jar:?]
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.run(FutureTask.java:266) ~[?:1.8.0_25]
	at g.a(SourceFile:60) ~[1.8.7.jar:?]
	... 3 more
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
	at bcy.a(SourceFile:600) ~[1.8.7.jar:?]
	at hu.a(SourceFile:41) ~[1.8.7.jar:?]
	at hu.a(SourceFile:8) ~[1.8.7.jar:?]
	at fh$1.run(SourceFile:13) ~[1.8.7.jar:?]
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.run(FutureTask.java:266) ~[?:1.8.0_25]
	at g.a(SourceFile:60) ~[1.8.7.jar:?]
	... 3 more
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
[14:41:33] [Client thread/FATAL]: Error executing task
java.util.concurrent.ExecutionException: java.lang.NullPointerException
	at java.util.concurrent.FutureTask.report(FutureTask.java:122) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.get(FutureTask.java:192) ~[?:1.8.0_25]
	at g.a(SourceFile:61) [1.8.7.jar:?]
	at ave.av(SourceFile:880) [1.8.7.jar:?]
	at ave.a(SourceFile:325) [1.8.7.jar:?]
	at net.minecraft.client.main.Main.main(SourceFile:124) [1.8.7.jar:?]
Caused by: java.lang.NullPointerException
	at bcy.a(SourceFile:964) ~[1.8.7.jar:?]
	at gq.a(SourceFile:45) ~[1.8.7.jar:?]
	at gq.a(SourceFile:10) ~[1.8.7.jar:?]
	at fh$1.run(SourceFile:13) ~[1.8.7.jar:?]
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511) ~[?:1.8.0_25]
	at java.util.concurrent.FutureTask.run(FutureTask.java:266) ~[?:1.8.0_25]
	at g.a(SourceFile:60) ~[1.8.7.jar:?]
	... 3 more
[14:41:33] [Client thread/FATAL]: Error executing task```
This relates to:
- MC-81649

### Comment 11: MobileCrafter (2015-07-02T13:04:15.276-0700)

I reproduced the Error Messages by just playing on a Server.
The Server uses the 1.8 Spigot Protocol Hack.
Here the log: http://pastebin.com/3grZPM47

### Comment 12: GoodKingFilms (2016-06-13T09:36:17.276-0700)

Still an issue in 1.10! Could a mod please update the affected versions to 1.10? Thank you

### Comment 13: pokechu22 (2016-07-22T20:45:18.256-0700)

Feels related to [MC-86947] or [MC-92079] (though that was fixed, I believe it's the same type of issue, joining multiple instances at once).

### Comment 14: migrated (2016-11-06T03:10:05.265-0800)

Is this still an issue in the latest snapshot 16w44a? If so please update the affected versions.
This is an automated comment on any open or reopened issue with out-of-date affected versions.

### Comment 15: migrated (2017-07-21T15:17:11.083-0700)

This bug happened to me while connecting to a vanilla 1.12 server after being disconnected from a restarting server.

### Comment 16: RimaNari (2018-02-07T00:27:19.188-0800)

This appears to be similar to a bug Xisumavoid showcased on Youtube. He demonstrates how this can be exploited to change the actual player position in a singleplayer world:
- In a singleplayer world you are at coordinates x, y, z.

- Log into a server (or possibly also another singleplayer world?) where you are at coordinates x', y', z'.

- Before loading has finished, quickly cancel joining the server and instead open the singleplayer world again.

- The client renders the server you were trying to join before canceling, however the actual block positions are different.

- Leaving and re-opening the singleplayer world removes render glitches - you see the singleplayer world again, but you remain at the coordinates of the server, effectively teleporting you from x, y, z to x', y', z' in the singleplayer world.

This bug can not only be exploited but can happen by chance easily. Additionally there may be further things that can be exploited about this.

### Comment 17: pokechu22 (2018-02-07T09:02:33.122-0800)

Yeah, this is the same bug, or else this is the same family of bugs.  (It could also be one of the ones marked as related, even the ones marked as fixed, as the weird loading is a symptom of some other underlying problem of being on two servers/worlds/something like that).

### Comment 18: RimaNari (2018-02-07T10:21:29.735-0800)

Wouldn't it be a good idea to update the description of the bug then? Currently it only explains the issue of the chat being shared across two servers. If this bug is to represent all symptoms that are caused by the same underlying bug of the connection not getting cancelled, a more general description would be appropriate.
Maybe a new description could contain both the current version explaining the issue with chat and my description of the teleporting. Then it would be clear that this is not only a single symptom (or even only a "minor" issue with the chat - the teleporting seems more important to me), but in fact an issue with a broad spectrum of symptoms.

### Comment 19: migrated (2019-09-23T22:13:31.998-0700)

I managed to reproduce this on 1.14.4 (by accident, of course)

### Comment 20: migrated (2020-09-08T09:54:12.821-0700)

I reproduce this on 1.16.1

### Comment 21: Avoma (2020-11-25T07:28:08.054-0800)

Relates to REALMS-5078.

### Comment 22: migrated (2020-12-15T04:27:14.506-0800)

Moved from MC-12989
I've reproduced this issue on Minecraft 1.16.4. The chat, bossbar and tab screen are from the previous server, while the world, gamemode and position are of the current server (possibly other stuff belongs to one server or the other, this is what I could find so far; previous server is the server I joined, but quickly cancelled and current server is the server I joined after the cancellation of the first server). A side effect of this glitch is that I'm in "noclip"-mode: I can go through the terrain as if it's not there, while still seeing the terrain and being in creative mode.
Reproduction steps:
- Join one server via Direct Connection and quickly press the Cancel button

- Join a different server from the server list and wait until you're in the server

- The two servers are merged in the way as stated above

While doing this I had the client game log screen opened (enabled from within the launcher), so the game log printed there can be found in the latest.log I've attached to this issue. I've also taken multiple screenshots while in this mode which I've also attached, showing various effects caused by this.
The "noclip"-mode allowing me to go directly into the ground
The chat: the top lines are from the previous server, while everything below is from the current server
The tab screen from the previous server
The bossbar from the previous server
In all these images, the world that can be seen in the background is of the current world.
Edit: Some more information. I cannot interact with the world in any way: I cannot place or breaks blocks, spawn entities via spawn eggs, bonemeal grass blocks, use flint and steal, shoot arrows (the animation plays, but no arrow is shot), use a trident or interact with doors, beds, chests and shulker boxes; hitboxes for blocks are missing. The client does seem to know where blocks are, because when trying to use a spawn egg, it correctly shows the arm swing animation when looking at a block, while not showing this animation when right clicking the air. Chunks don't load as normal: I can move through the world, but after a certain amount of chunks, they stop loading completely. When going too far outwards (roughly half an unloaded chunk), all chunks that were visible disappear completely. The permissions from the previous server also carry over to this one, I am operator level 4 in the current server, yet I can't execute commands which require such an op level. The only commands I can use are commands from the previous server. Trying to execute those commands doesn't (visually) do anything. Chatting doesn't show my chat message. The social interactions screen also shows the players from the previous server, but shows the current server as the host name.
My armor of the previous server is also transferred over to this server. I've amended a screenshot to show this. (The effects are from the current server after eating an enchanted golden apple, this is as intended.)
After rejoining my armor items and items in my inventory (I put one piece of armor in my normal inventory, left two in my armor slots) stay in my inventory. This is potentially problematic, as then I can transfer armor from one server to another. (I could for example, get myself overpowered netherite armor from a creative server to a survival server.) This might warrant raising the priority of this issue or making this private.

### Comment 23: migrated (2021-08-27T07:18:04.769-0700)

I managed to reproduce this on accident on 1.16.5, though I didn't cancel the joining, I just joined mineclub while opening my minecraft server on localhost and managed to join both servers at once, actionbars and chat were updated at real time from the other server and this kept on even after relogging from my minecraft server, and I couldn't join mineclub because it said I was already there.

It was constantly flickering between mine and their actionbar and mine and their time on the minecraft world, so it was going night and day constantly and I managed to join with their server texture;
So basically I'd get a very weird buggy relay from their minecraft server.

### Comment 24: migrated (2021-12-02T19:41:19.724-0800)

1.18
My game previously crashed and I tried to rejoin my friend's realm
I was denied twice
I went to Hypixel to see if it was my computer or the realm
It dropped me in the realm with the gui and collision of Hypixel
I left and tried to join the realm
It worked but the Hypixel Chat was still there and flickering between day and night
I got shot by a skeleton and was sent to the AFK Hub in Hypixel from the realm
Got shot again and was sent to a Hypixel Lobby
Started to fly away and finally died
I couldn't respawn and left the server for it to finally fix itself
the entire time I had my gear from the realm.

### Comment 25: plumparrot71568 (2022-07-04T13:03:03.161-0700)

Can confirm in 1.17.1 (Hypixel + my private server)

### Comment 26: plumparrot71568 (2022-07-04T13:33:50.596-0700)

This appears to have been fixed in version 1.18, as I cannot reproduce the issue in any version that is 1.18 or newer.

### Comment 27: migrated (2022-07-05T06:29:50.878-0700)

I encountered this years ago but didn't think nothing of it until I saw a video by "TheMisterEpic" released July 2 2022. Video here: https://www.youtube.com/watch?v=EEG_c3ycDg4 I still have my old screenshot so I'm adding it. I was on Thesevensaints and geovillage and was getting server info from both servers. Sevensaints was sending info in the chat and geovillage was sending in the tab screen although was showing players from sevensaints.
