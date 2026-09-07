# MC-188602: In non-natural custom dimensions, if "bed_works" is set to true, beds cannot be used to skip the night or set the spawn point

**Mojira URL:** [https://bugs.mojang.com/browse/MC-188602](https://bugs.mojang.com/browse/MC-188602)

## Report details

- **Mojira categories:** Custom Worlds
- **Project:** MC
- **Issue key:** MC-188602
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2020-06-11T00:49:23.671-0700
- **Updated:** 2025-10-16T06:20:56.798-0700
- **Resolution date:** 2025-10-16T06:20:56.438-0700
- **Affects versions:** 1.16 Pre-release 3; 1.16 Pre-release 4; 1.16 Pre-release 6; 1.16 Pre-release 7; 1.16 Pre-release 8; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w27a; 20w28a; 1.16.2; 1.16.3; 1.16.5; 21w18a; 1.18 Pre-release 4; 22w15a; 22w17a; 1.19 Pre-release 2; 1.19; 1.19.1 Pre-release 6; 1.19.1; 1.19.2; 22w42a; 22w43a; 22w44a; 22w46a; 1.19.3 Pre-release 1; 1.19.3; 23w03a; 1.19.4 Pre-release 1; 1.19.4; 23w16a; 23w18a; 1.20 Pre-release 1; 1.20 Pre-release 2; 1.20 Pre-release 5; 1.20 Pre-release 6; 1.20; 1.20.1; 23w32a; 23w35a; 1.20.2 Pre-release 1; 1.20.2 Release Candidate 1; 1.20.2; 23w40a; 23w41a; 23w42a; 23w43a; 23w44a; 1.20.3 Pre-Release 2; 1.20.3; 1.20.4; 24w07a; 24w09a; 24w10a; 1.21 Pre-Release 1; 1.21.3; 1.21.4; 1.21.5; 1.21.9
- **Fix versions:** 25w42a
- **Area:** Platform
- **Watchers:** 2
- **Attachments:** 5
- **Attachment filenames:** 1.18-pre4_respawn_points_reversed.json; Bad respawn points.mp4; MC-188602.zip; respawn_points_reversed_21w18a.json; respawn_points_reversed.json
- **Issue links:** Duplicate:inward:MC-194479:Using bed in custom world with bed_works and fixed_time does nothing | Relates:inward:MC-235035:Sleeping in a custom dimension with "natural" set to false causes crash

## Description

In a custom dimension, if the dimension type has natural set to false and bed_works set to true, using a bed does not explode, but it does not skip the night or set the player's spawn point either.
How to reproduce:
- Create a new world with the attached data pack (

- ).

- Go to the nether or the end.

- Place a bed down.

- Use the bed.

Expected result:
The bed would set my spawn point, but probably not skip the night as the dimension has "natural" set to false.
Observed result:
The bed did not do anything.
Original description:
I made a custom world where what I expected to happen was:
- In the Overworld, beds explode and respawn anchors set your spawn point.

- In the Nether, beds set your spawn point and respawn anchors explode.

- In the End, beds and respawn anchors set your spawn point.

However, what actually happened was:
- In the Overworld, beds exploded and respawn anchors did nothing (1.16.5)/actually set your spawn point (21w18a).

- In the Nether, beds did nothing and respawn anchors exploded.

- In the End, beds did nothing and respawn anchors did actually set my spawn point.

I have attached the world settings and a video that shows some of the results.
Additionally, these errors appear in the output log when attempting to set your spawn (1.16.5)

```
Error executing task on Client
java.lang.NullPointerException
	at afr.a(SourceFile:128)
	at afr.a(SourceFile:142)
	at dkv.b(SourceFile:1202)
	at dkv.a(SourceFile:1216)
	at dwu.a(SourceFile:870)
	at pb.a(SourceFile:41)
	at pb.a(SourceFile:11)
	at ol.a(SourceFile:21)
	at ol$$Lambda$4750/782440233.run(Unknown Source)
	at aob.c(SourceFile:144)
	at aof.c(SourceFile:23)
	at aob.y(SourceFile:118)
	at aob.bl(SourceFile:103)
	at djz.e(SourceFile:1015)
	at djz.e(SourceFile:681)
	at net.minecraft.client.main.Main.main(SourceFile:215)
```

## Comments (5)

### Comment 1: migrated (2020-06-11T00:49:23.671-0700)

This comment contained multiple image attachments (5), please login to view the attachments.

### Comment 2: migrated (2020-08-16T03:06:22.199-0700)

In the
 I have found these parts:
For bed not working in oveworld and RA working:
Line 151 and 152
"type":{
.
.
.
"respawn_anchor_works": true,
"bed_works": false,
.
.
.
}
For bed working in nether and RA not:
Line 357 and 358
"type":{
.
.
.
"respawn_anchor_works": false,
"bed_works": true,
.
.
.
}

So there is no bug, it is intended, you can change these settings through importing correct settings to your world

### Comment 3: [Mod] ManosSef (2020-08-16T23:24:05.682-0700)

I will import a data pack I made to reproduce the bug in 1.16.2 later today.

### Comment 4: migrated (2022-07-21T05:35:12.022-0700)

Stupidly enough, bed works only controls whether it explodes; natural is checked for actual sleeping/setting spawn.
This seems like an oversight.

### Comment 5: [Mod] ManosSef (2025-10-16T06:20:56.493-0700)

This issue was fixed in 25w42a.
