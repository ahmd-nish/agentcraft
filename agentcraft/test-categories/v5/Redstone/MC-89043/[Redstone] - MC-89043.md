# MC-89043: Slime blocks moved by pistons often fail to bounce up the player

**Mojira URL:** [https://bugs.mojang.com/browse/MC-89043](https://bugs.mojang.com/browse/MC-89043)

## Report details

- **Mojira categories:** Player; Redstone
- **Project:** MC
- **Issue key:** MC-89043
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2015-09-18T18:06:18.116-0700
- **Updated:** 2025-04-26T04:16:07.904-0700
- **Resolution date:** 2024-11-27T21:02:28.719-0800
- **Affects versions:** Minecraft 15w38b; Minecraft 15w39b; Minecraft 15w39c; Minecraft 15w41b; Minecraft 15w42a; Minecraft 15w45a; Minecraft 15w46a; Minecraft 15w47a; Minecraft 15w47b; Minecraft 15w47c; Minecraft 15w49a; Minecraft 15w49b; Minecraft 15w50a; Minecraft 1.9 Pre-Release 2; Minecraft 1.9 Pre-Release 3; Minecraft 1.9 Pre-Release 4; Minecraft 1.9; Minecraft 1.9.1 Pre-Release 1; Minecraft 1.9.1 Pre-Release 2; Minecraft 1.9.1 Pre-Release 3; Minecraft 1.9.1; Minecraft 1.9.2; Minecraft 16w14a; Minecraft 16w15a; Minecraft 16w15b; Minecraft 1.9.3 Pre-Release 1; Minecraft 1.9.3 Pre-Release 2; Minecraft 1.9.3 Pre-Release 3; Minecraft 1.9.3; Minecraft 1.9.4; Minecraft 16w20a; Minecraft 16w21a; Minecraft 16w21b; Minecraft 1.10 Pre-Release 1; Minecraft 1.10 Pre-Release 2; Minecraft 1.10; Minecraft 1.10.2; Minecraft 16w43a; Minecraft 16w44a; Minecraft 1.11 Pre-Release 1; Minecraft 1.11; Minecraft 16w50a; Minecraft 1.11.1; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 1.12; Minecraft 1.12.1 Pre-Release 1; Minecraft 1.12.1; Minecraft 1.12.2 Pre-Release 1; Minecraft 1.12.2 Pre-Release 2; Minecraft 1.12.2; Minecraft 17w43a; Minecraft 17w43b; Minecraft 17w45a; Minecraft 17w45b; Minecraft 18w20b; Minecraft 1.13-pre1; Minecraft 1.13-pre2; Minecraft 1.13-pre3; Minecraft 1.13-pre4; Minecraft 1.13-pre6; Minecraft 1.13-pre7; Minecraft 1.13-pre8; Minecraft 1.13; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 19w02a; Minecraft 19w03c; Minecraft 19w04a; Minecraft 19w04b; Minecraft 19w05a; Minecraft 19w06a; Minecraft 19w07a; Minecraft 19w08b; Minecraft 1.14 Pre-Release 2; Minecraft 1.14 Pre-Release 3; Minecraft 1.14; Minecraft 1.14.2 Pre-Release 2; 1.14.4; 19w37a; 1.15 Pre-release 1; 1.15 Pre-Release 2; 1.15 Pre-release 3; 1.15 Pre-release 4; 1.15 Pre-release 5; 1.15 Pre-release 6; 1.15 Pre-release 7; 1.15; 1.15.1; 1.15.1 Pre-release 1; 1.15.2 Pre-Release 1; 1.15.2 Pre-release 2; 1.15.2; 20w06a
- **Fix versions:** 20w07a
- **Labels:** piston; player; slime_block
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 2015-09-25 17-57-28.flv; My Movie.mp4; My Movie.mp4
- **Issue links:** Relates:outward:MC-90063:Slime block propulsion | Duplicate:inward:MC-147224:game bag with a slime block and piston | Relates:outward:MC-88833:Pistons don't move/bounce entities | Duplicate:inward:MC-153726:Arrrows not always bounce on a moving slimeblock | Duplicate:inward:MC-152186:Slime blocks won't launch players who are moving | Duplicate:inward:MC-151715:When Running on Slime blocks pistons cant shoot you upwards on them | Duplicate:inward:MC-151528:block | Duplicate:inward:MC-149895:Inconsistent slime block piston launching | Duplicate:inward:MC-148423:Pistons pushing slime blocks don't make player jump up | Relates:inward:MC-44401:Falling on a Slime Block while holding the down the jump key will cause the player to NOT be launched high while still neglecting fall damage. | Duplicate:inward:MC-120662:Boats dont always launch up after getting pushed by a slimeblock. | Duplicate:inward:MC-98352:Slime blocks act as normal blocks, dont make you jump | Duplicate:inward:MC-93174:Slime Block | Duplicate:inward:MC-89124:Walking/sprinting near a slime block pushed in any orientation by a piston doesn't bounce players | Duplicate:inward:MC-90519:Players are not propelled by extending slime blocks | Duplicate:inward:MC-89537:Slime blocks don't push players up while moving | Duplicate:inward:MC-89382:pushed upwards slime blocks dont bounce players

## Description

The bug
When a piston moves a slime block players are not always launched.
How to reproduce
- Place a upwards facing sticky piston

- Place a slime block on top

- Place a redstone block on the side of the slime block

- Update the piston

- Jump on the slime block (which now moves up and down)
→  You will see that you just rarely get bounced up. For entities other than the player it works fine.

Example
This video shows it: https://www.youtube.com/watch?v=qgFt5L5f9jY
Additional information
It works fine for other entities, so it probably has to do with the client/server communication or similar.
Potential Fix
I noticed there is a flag called "velocityChanged" in MCP for entities. It is for example used when an entity is hit and needs to get knock back.
When the flag is set, the EntityTracker will send an extra packet containing the entities velocity.
Setting this flag when an entity is bounced by a slime block pretty much fixes this issue. (There is still an related one that if you fall on a moving slime block you don't get bounced which might have similar effects.)
Video with a comparison flag set vs flag not set: https://www.youtube.com/watch?v=VKHBJxtSlc0&t=2m42s

## Comments (33)

### Comment 1: migrated (2015-09-18T18:06:18.116-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: migrated (2015-09-18T18:09:38.769-0700)

IMO, most likely caused by the fix of (and possibly a regression of) MC-88833.

### Comment 3: Panda4994 (2015-09-18T18:13:01.121-0700)

Yeah, it definitely is caused by the (awesome!) recent changes to how pistons move entities.
I'm not sure where exactly this one is coming from yet, but I'm sure it can be resolved without backing off the previous fixes

### Comment 4: migrated (2015-09-21T14:21:53.418-0700)

Still confirmd in 15w38b & 15w39b

### Comment 5: SunCat (2015-09-24T06:24:10.771-0700)

Confirmed in 15w39c (MC-89382)

### Comment 6: migrated (2015-09-25T08:58:13.496-0700)

15w39c Confirmd.

### Comment 7: migrated (2015-10-19T07:00:17.712-0700)

Confirmed for 15w42a  - still not working
still not working correctly, works sometimes though
never got it working in the middle of grouped slime blocks

### Comment 8: migrated (2015-11-09T07:52:35.798-0800)

Confirmed in 15w45a. Even if it's wired to only push when you're on top of it (such as with a command block proximity detector), you only get pushed up about 25% of the time when walking over it. If you stand still on it, it works fine, but if you move, then it seems to depend on either your speed or the exact distance from the block before when it triggers.

### Comment 9: [Mod] Neko (2015-12-12T15:22:40.454-0800)

Confirmed for 15w50a

### Comment 10: migrated (2016-01-26T07:10:52.499-0800)

it might be a no brainer, but also confirmed in 1.8.9

### Comment 11: migrated (2016-02-22T15:15:36.879-0800)

If you are moving - it 5/7 times fails
If server tps is lower then 20 - it fails.
every version is imporving the reliability
- confrimd for 16w06 - 1.9pre1 - 1.9pre2

### Comment 12: migrated (2016-02-25T02:49:42.993-0800)

Singleplayer is fine -multplayer its like 85 / 100 times now working
1.9pre3

### Comment 13: migrated (2016-02-27T04:08:34.599-0800)

moving seems to be more bugged then pre3
standing still 100/100
- confirmed 1.9pre4

### Comment 14: migrated (2016-02-29T11:36:47.330-0800)

https://twitter.com/SeargeDP/status/704383283061202945
"No code changes between 1.9pre4 and 1.9"- SeargeDP
so, still confirmd 1.9 :/

### Comment 15: migrated (2016-03-30T12:20:57.981-0700)

Slime blocks still only occasionally launch the player in 1.9.2. Maybe about a third of all times for me.
Also, whether it works or not seems to somehow be tied to the game's performance. I tried it on another, better computer and slime blocks definitely launched me more often, maybe about 80% of the time. Anyway, that may be why people get different probabilities.

### Comment 16: migrated (2016-03-31T00:43:29.317-0700)

@Jelmer
I got fiberglass internet, and a super beafy server; and in multiplayer is more stable then single player on my laptop (when on lan)
so it's all relative
(Desktop is other way around)

### Comment 17: migrated (2016-04-10T14:19:51.857-0700)

I came here to report this and found this already existing report.
I never had issues before, but since 1.9 came out all my jump pads broke.

### Comment 18: migrated (2016-08-04T10:05:37.303-0700)

To add to my previous comment, I made two very interesting observations that may be helpful.
1) Whether the player is launched or not seems to not only be related to the performance, but to the frame rate itself. Now that sounds ridiculous and it probably shouldn't work like that, but I tested it several times by limiting the frame rate. At 10 FPS and probably lower successful launching rarely happens, above maybe 30 or 40 FPS it seems to succeed almost every time. All in all however it seems more reliable than it was in 1.9.
2) Other entities (tested with items and creepers) seem to be correctly launched every single time, even at a frame rate of 10 FPS.

### Comment 19: RimaNari (2016-08-04T10:20:26.782-0700)

Does lowering the FPS in SP give any constraints to the TPS of the internal server as well? I assume it does, so your observations would be in agreement with that. If not though, that would certainly be strange.

### Comment 20: migrated (2016-08-04T10:41:20.736-0700)

Apparently it does, but I'm pretty sure it shouldn't.

### Comment 21: migrated (2017-08-08T12:11:49.508-0700)

Confirmed for 1.12.1

### Comment 22: migrated (2018-09-16T17:31:29.470-0700)

Confirmed for 1.13.1.

### Comment 23: migrated (2019-04-17T03:56:10.386-0700)

This seems to have gotten way worse since the latest 1.14 snapshots. Now if a player is moving on them while the piston is extending, he almost never gets launched up.

### Comment 24: migrated (2019-04-17T03:58:49.934-0700)

Since 1.13 I never got up while moving
No worse or better experience for me

### Comment 25: migrated (2019-04-27T07:40:08.009-0700)

Got a lot worse in the official 1.14 release.

### Comment 26: migrated (2019-05-21T15:26:34.097-0700)

This is still a problem in 1.14.2 Pre-Release 2

### Comment 27: migrated (2019-07-22T20:29:13.176-0700)

This is still a huge problem in 1.14.4. Please fix this bug, it's so annoying for us redstoners

### Comment 28: migrated (2019-08-08T07:00:13.248-0700)

Significantly worse on 1.14.4 to the point of making slime block bounce mechanisms entirely unusable. Bounces almost never work on the first attempt now, and I've had periods of upwards of a minute of constant triggering where the block will never cause a bounce.

### Comment 29: migrated (2019-11-22T06:04:24.732-0800)

The cause of the bug seems to be moving whilst the slime block moves. If I stand perfectly still the bounce will work almost every time, but walking or falling as it moves causes it to fail to have any effect.

### Comment 30: migrated (2019-12-15T15:01:40.061-0800)

Confirmed in 1.15.
Seems to be related to movement of the player, as mentioned above, but occurs sporadically. I've been able to successfully chain upwards of 20 bounces while sprinting in a row, yet at other times I can't even manage a single one.

### Comment 31: Panda4994 (2020-02-14T07:53:29.289-0800)

This should be noticeably better in 20w07a, however it can still fail if the player falls onto the moving slime block because of MC-123217.

### Comment 32: migrated (2020-03-22T01:44:56.877-0700)

This is also a problem in Bedrock edition...

### Comment 33: migrated (2024-11-27T21:02:28.719-0800)

Issue seems to have reoccurred as of 1.20.3 but only when the player is in a boat.
- It doesn't effect other mobs in boats

- happens when moving or at a standstill as long as player is in it.

- Did not see any problems with launching myself on slimeblocks only when in a boat.

There was another post on this specifically but it was linked to this one as a duplicate so I'm commenting here.
Hope this is clear let me know if more info would be helpful
