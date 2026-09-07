# MC-109346: Newly rendered players always look south until they move their head

**Mojira URL:** [https://bugs.mojang.com/browse/MC-109346](https://bugs.mojang.com/browse/MC-109346)

## Report details

- **Mojira categories:** Networking; Player
- **Project:** MC
- **Issue key:** MC-109346
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2016-10-28T12:25:42.034-0700
- **Updated:** 2025-04-29T12:22:30.176-0700
- **Resolution date:** 2023-09-06T00:35:29.930-0700
- **Affects versions:** Minecraft 1.10.2; Minecraft 16w42a; Minecraft 1.12.1; Minecraft 1.12.2; Minecraft 18w21b; Minecraft 18w22a; Minecraft 18w22b; Minecraft 18w22c; Minecraft 1.13-pre1; Minecraft 1.13-pre2; Minecraft 1.13-pre4; Minecraft 1.13-pre5; Minecraft 1.13-pre7; Minecraft 1.13; Minecraft 18w30b; Minecraft 1.13.1; Minecraft 1.13.2-pre1; Minecraft 1.13.2; Minecraft 18w45a; Minecraft 18w46a; Minecraft 19w08b; Minecraft 19w09a; Minecraft 19w12b; Minecraft 19w13a; Minecraft 1.14 Pre-Release 2; Minecraft 1.14 Pre-Release 3; Minecraft 1.14 Pre-Release 4; Minecraft 1.14 Pre-Release 5; Minecraft 1.14.2; Minecraft 1.14.3 Pre-Release 2; Minecraft 1.14.3; Minecraft 1.14.4 Pre-Release 3; Minecraft 1.14.4 Pre-Release 4; 1.15.2; 20w08a; 20w09a; 20w10a; 20w11a; 20w12a; 20w18a; 20w19a; 1.16 Pre-release 3; 20w46a; 21w10a; 21w11a; 21w13a; 21w15a; 21w17a; 21w18a; 1.17; 1.17.1; 21w37a; 21w40a; 1.18 Pre-release 1; 1.18; 1.18.1; 22w05a; 1.18.2; 22w13a; 22w18a; 22w19a; 1.19 Pre-release 2; 1.19 Pre-release 3; 1.19 Pre-release 4; 1.19 Pre-release 5; 1.19; 1.19.1; 1.19.2; 1.19.3 Pre-release 2; 1.19.3; 23w03a; 23w04a; 1.19.4; 1.20 Pre-release 1; 1.20.1; 23w33a
- **Fix versions:** 1.20.2 Pre-release 2
- **Labels:** client-side; facing; head; player; server
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** demo.mp4; MC-109346.mp4; MC-109346 - Analysis.png
- **Issue links:** Relates:inward:MC-173603:Ender dragons with their "NoAI" NBT tag set to "1b" always face north | Relates:outward:MC-11141:Minecraft player head rotation not working when entity being spawned | Duplicate:inward:MC-130411:Idle players heads face south when going out of render distance or when they connect to the server | Duplicate:inward:MC-154119:LAN Worlds Head Positions | Duplicate:inward:MC-154445:Player heads off | Duplicate:inward:MC-156499:Player model defaults to looking south | Duplicate:inward:MC-237037:After death, all players appear to be facing south until they adjust their head rotation | Duplicate:inward:MC-264811:Character problem

## Description

The bug
When another player is newly rendered on a server (e.g. joining in the server, getting in your render distance (MC-130411), or respawning (MC-237037)), they will look south until they move their head. This can look pretty strange if the body of the player is facing, for example, north.
Steps to Reproduce
Get two players and label them, "Player A" and "Player B".
- Let player A enter.

- Let player B enter.

- Let player A face north.

- Let player B move far away (beyond render distance) and back.

Observed Behavior
"Player B" sees "Player A" now facing south when actually "Player A" is still facing north, therefore indicating that when newly rendered by the client, all players appear to be facing south until they adjust their head rotation.
Expected Behavior
The expected behavior would be that when players get rendered, all players would appear to be facing the correct direction.
Code Analysis
The following is based on a decompiled version of Minecraft 1.10 using MCP 9.30.
It looks like the method net.minecraft.entity.Entity.setPositionAndRotation(double, double, double, float, float) which is called when a player is spawned client-side only sets the body rotation. This could be fixed as well by sending a net.minecraft.network.play.server.SPacketEntityHeadLook.SPacketEntityHeadLook(Entity, byte) packet after the spawn packet.

## Comments (14)

### Comment 1: migrated (2016-10-28T12:25:42.034-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: marcono1234 (2016-10-28T12:26:21.971-0700)

Might relate to MC-11141, but very likely only because of the topic, not the code

### Comment 3: migrated (2017-08-05T18:33:48.316-0700)

This bug still exists in Minecraft 1.11.2, 1.12.1.
Here is a GIF of the phenomenon, which I created using two accounts on a local vanilla server in 1.12.1.  (It was too large to upload here.)
Then just some other information.
If the player walks around without moving their head, it remains pointing south. (expected behavior)
If the player changes only the pitch of their head, it remains pointing south, though the pitch will change. (unexpected, as both yaw and pitch are sent in the entity look packet)
If the player changes the yaw of their head, it corrects to where it should be. (expected behavior)

### Comment 4: migrated (2018-09-14T06:19:49.605-0700)

Confirmed for 1.13.1.

### Comment 5: migrated (2020-02-25T06:56:26.887-0800)

Still an issue in 1.15.2 and 20w08a

### Comment 6: Tinsel (2020-02-27T16:03:45.911-0800)

and 20w09a

### Comment 7: Tinsel (2020-03-04T14:23:00.761-0800)

In 20w10a

### Comment 8: Tinsel (2020-03-11T14:19:05.071-0700)

In 20w11a

### Comment 9: Tinsel (2020-03-18T14:30:17.446-0700)

In 20w12a

### Comment 10: Tinsel (2020-04-29T10:47:41.238-0700)

In 20w18a

### Comment 11: marcono1234 (2020-04-29T11:54:27.860-0700)

@, do you want to become the reporter so you can update affected versions yourself?

### Comment 12: Tinsel (2020-05-06T11:41:09.104-0700)

Sure, I'd love to! (In 20w19a )

### Comment 13: Avoma (2022-07-29T02:50:51.717-0700)

Can confirm in 1.19.1.

### Comment 14: Avoma (2022-09-07T11:35:34.194-0700)

Can confirm in 1.19.2.
