# MC-78314: (Marker) Armor stands create bubbles in water

**Mojira URL:** [https://bugs.mojang.com/browse/MC-78314](https://bugs.mojang.com/browse/MC-78314)

## Report details

- **Mojira categories:** Particles
- **Project:** MC
- **Issue key:** MC-78314
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2015-03-03T06:38:22.875-0800
- **Updated:** 2025-04-26T03:57:07.640-0700
- **Resolution date:** 2024-09-29T04:02:26.432-0700
- **Affects versions:** Minecraft 1.8.3; Minecraft 1.8.8; Minecraft 15w36c; Minecraft 15w47c; Minecraft 16w38a; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 1.12; Minecraft 1.12.1; Minecraft 1.12.2 Pre-Release 1; Minecraft 1.12.2 Pre-Release 2; Minecraft 1.12.2; Minecraft 17w43a; Minecraft 17w43b; Minecraft 17w45b; Minecraft 17w46a; Minecraft 17w47a; Minecraft 17w47b; Minecraft 17w48a; Minecraft 18w01a; Minecraft 18w03b; Minecraft 18w16a; Minecraft 18w19b; Minecraft 18w21a; Minecraft 18w21b; Minecraft 18w22a; Minecraft 1.13-pre1; Minecraft 1.13-pre2; Minecraft 1.13-pre3; Minecraft 1.13-pre4; Minecraft 1.13-pre6; Minecraft 1.13-pre7; Minecraft 1.13-pre8; Minecraft 1.13-pre9; Minecraft 1.13-pre10; Minecraft 1.13; Minecraft 18w30a; Minecraft 18w30b; Minecraft 18w31a; Minecraft 18w32a; Minecraft 18w33a; Minecraft 1.13.1-pre1; Minecraft 1.13.1; Minecraft 1.13.2-pre1; Minecraft 1.13.2-pre2; Minecraft 1.13.2; Minecraft 18w47b; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 19w02a; Minecraft 19w03b; Minecraft 19w03c; Minecraft 19w04b; Minecraft 19w05a; Minecraft 19w06a; Minecraft 19w07a; Minecraft 19w12b; Minecraft 19w13b; Minecraft 19w14a; Minecraft 19w14b; 1.15.2 Pre-Release 1; 1.15.2; 20w06a; 20w09a; 20w12a; 20w13a; 20w13b; 20w14a; 20w17a; 20w19a; 1.16 Pre-release 5; 1.16.1; 1.16.2 Pre-release 1; 1.16.2 Release Candidate 1; 1.16.4; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w07a; 21w11a; 21w18a; 1.17 Pre-release 3; 1.17; 1.17.1; 1.18.2; 22w13a; 22w14a; 22w18a; 1.19 Pre-release 1; 1.19; 1.19.1; 1.19.2; 1.19.3; 1.19.4 Pre-release 2; 23w33a
- **Fix versions:** 23w40a
- **Area:** Platform
- **Labels:** armor; armor-stand; armor_stand; bubble; eye-level; hitbox; marker; underwater
- **Watchers:** 1
- **Attachments:** 13
- **Attachment filenames:** 2015-03-03_15.36.51.png; 2015-03-03_15.37.42.png; 2017-06-24_23.26.04.png; 2018-05-09_20.07.47.png; 2018-05-09_20.47.35.png; 21w20a_noblock.png; 21w20a_structurevoid.png; armor_stand_bubbles.png; marker-false_air-constantly-plusvalue-300.png; marker-true_air-minusvalue-changing.png; MC78314.mp4; MC-78314.mp4; MC78314II.mp4
- **Issue links:** Relates:outward:MC-249622:Drowning bubbles still appear on living mobs underwater even when they have Water Breathing | Duplicate:inward:MC-131532:Armor stands can drown | Duplicate:inward:MC-113512:armorstand are bubbling in the water | Duplicate:inward:MC-80631:Invisible Armor Stands Make Bubble Particle Effect When Hitting Water

## Description

Since at least 21w20a, Marker-true-armor stands don't show bubbles if submerged into water as described below, in case there is a block below it. It doesn't matter if it's a full opaque or transparent block, and not only glass, but also e.g. slabs or a banner works.

 As soon as there is a block, Air replenishes immediately back to 300s, even if Air went already into negative values and thus bubble appeared prior.

 I don't know if this is WaI, I couldn't find anything in the Wiki's armor stand history, but the as-is status could be a potential workaround.
 Note to map/contraption makers: If you need the space below a water-submerged, invisible Marker-true-AS to be a nonobstructive void, a barrier block would of course not be an option, but you can use e.g. a structure void block (or e.g. the newish light block). You'll surely come up with better ideas as well.
 I don't know if it's WaI that Marker-false-AS still create bubbles if fully submerged in water as described below, and if the above workaround for Marker-true-AS is sufficient for mapmakers, or if they'd prefer a full fix.
 I hope Mojang can ask the mapmaking community for their requirements, and, dependent on that, this bugpost may be closed.
As long as this is not officially decided, I'll continue to update this bugpost.
Leaving the old bugpost text below for history and comprehension purposes.
Armor stands with Marker set to true create bubbles underwater which breaks immersion, as those marker-armor stands are only usable/producible in Creative and valuable mapmaker tools. Armor stands get this behaviour as they are part of EntityLiving. As soon as the armor stand's "eye height" is underneath water, bubbles appear after 300 ticks (15 seconds).
That's why an armor stand with Marker false does not create bubbles, as long as it's solely with its "feet" in water, but not with its "head" or rather at its eye height:

As soon as a Marker-false armor stand is underwater at eye height, it'll also create bubbles like the Marker-true armor stand:

As the Marker true armor stand got its tiny hitbox only at its "feet", bubbles appear in any case, when standing in water, after 300 ticks.
An easy way to solve this without ugly special cases could be to just let canBreatheUnderwater() return true for armor stands.
Summon command:

```
/summon minecraft:armor_stand ~ ~ ~ {Marker:1b}
```
Wait for 300 ticks on newly summoned armour stands for bubbles to appear.

## Comments (37)

### Comment 1: migrated (2015-03-03T06:38:22.875-0800)

This comment contained multiple image attachments (13), please login to view the attachments.

### Comment 2: Sonicwave (2015-03-16T20:40:28.469-0700)

Confirmed, also affects normal Armor stands.

### Comment 3: migrated (2015-11-26T11:59:24.108-0800)

Affects 15w47c
Slightly misleading title and description, as  stated above:
also affects normal Armor stands.
Summary change:
Armor stands create bubbles in water
Description change:
When an armor stand is under water bubbles appear as if it was a swimming mob or something similar.

### Comment 4: Michael Wobst (2017-02-12T10:20:03.061-0800)

Cannot reproduce in 1.11.2 and 17w06a. For me it only creates bubbles at the moment when it hits the water. Can someone verify if the issue has been fixed?

### Comment 5: SunCat (2017-02-12T14:23:21.985-0800)

Can reproduce both in 17w06a and 1.11.2. You need to wait a little for the bubbles to appear

### Comment 6: Michael Wobst (2017-09-15T12:31:27.490-0700)

Ticket is yours now,

### Comment 7: Panda4994 (2018-06-21T09:01:22.829-0700)

Can confirm for 1.13pre3.

### Comment 8: Panda4994 (2018-06-27T12:00:18.144-0700)

Confirmed for 1.13pre4.

### Comment 9: Panda4994 (2018-07-04T11:18:19.917-0700)

Confirmed for 1.13-pre6.

### Comment 10: Panda4994 (2018-07-13T03:53:27.146-0700)

Confirmed for 1.13-pre7.

### Comment 11: migrated (2018-07-13T05:46:44.561-0700)

Confirmed for 1.13-pre8 (tested it with normal armor stands).

### Comment 12: migrated (2018-07-17T02:43:15.593-0700)

Confirmed for 1.13-pre9 (tested it with normal armor stands).

### Comment 13: migrated (2018-07-18T03:42:21.001-0700)

Confirmed for 1.13-pre10 (tested it with normal armor stands).

### Comment 14: migrated (2018-07-18T14:02:13.127-0700)

Confirmed for 1.13 (tested it with normal armor stands).

### Comment 15: migrated (2018-07-25T08:51:36.938-0700)

Confirmed for 18w30a (tested it with normal armor stands).

### Comment 16: migrated (2018-07-26T13:49:35.840-0700)

Confirmed for 18w30b (tested it with normal armor stands).

### Comment 17: migrated (2018-08-01T09:13:48.608-0700)

Confirmed for 18w31a (tested it with normal armor stands).

### Comment 18: migrated (2018-08-08T07:36:14.971-0700)

Confirmed for 18w32a (tested it with normal armor stands).

### Comment 19: migrated (2018-08-15T08:17:50.134-0700)

Confirmed for 18w33a (tested it with normal armor stands).

### Comment 20: migrated (2018-08-16T18:14:42.871-0700)

Confirmed for 1.13.1-Pre-1

### Comment 21: migrated (2018-08-22T12:49:59.032-0700)

Confirmed for 1.13.1.

### Comment 22: migrated (2018-10-16T10:27:50.551-0700)

Confirmed for 1.13.2-pre1.

### Comment 23: migrated (2018-10-19T09:03:58.723-0700)

Confirmed for 1.13.2-pre2.

### Comment 24: Avoma (2021-01-11T01:31:27.939-0800)

Can confirm in 20w51a.

### Comment 25: Avoma (2021-01-23T03:50:27.783-0800)

Can confirm in 21w03a. Use the following command to reproduce this issue:

```/summon minecraft:armor_stand ~ ~ ~ {Marker:1b}```

### Comment 26: Avoma (2021-02-06T07:36:54.910-0800)

Can confirm in 21w05b.

### Comment 27: Avoma (2021-02-12T06:52:31.463-0800)

Can confirm in 21w06a.

### Comment 28: Avoma (2021-02-15T10:45:58.620-0800)

Video attached. Please note that when reproducing this, you must wait a while in order for the bubbles to appear.

### Comment 29: migrated (2021-02-15T11:09:18.656-0800)

Thank you, however, there are already 2 videos implemented, and with those also why it takes a bit until those bubbles appear in newly placed or summoned armour stands
But good call, it might still not be that directly obvious to everyone 300 ticks have to pass by, I will add that to the description.

### Comment 30: Avoma (2021-02-19T05:45:06.369-0800)

All good.  Can confirm in 21w07a.

### Comment 31: Avoma (2021-03-23T09:24:30.868-0700)

Can confirm in 21w11a.

### Comment 32: Avoma (2021-06-28T10:02:55.904-0700)

Can confirm in 1.17.

### Comment 33: Avoma (2021-07-12T11:25:25.432-0700)

Can confirm in 1.17.1.

### Comment 34: Avoma (2022-03-04T10:49:34.353-0800)

Can confirm in 1.18.2.

### Comment 35: KirbAvion (2022-04-02T17:38:21.746-0700)

Can confirm in 22w13a.

### Comment 36: ampolive (2022-05-18T17:39:10.153-0700)

Cannot reproduce in 1.19 Pre-release 1. Nevermind, I forgot that the armor stand needs to not have a block beneath it. This is still present in 1.19 Pre-release 1.

### Comment 37: migrated (2023-01-14T12:20:48.500-0800)

Can confirm in 1.19.3.
