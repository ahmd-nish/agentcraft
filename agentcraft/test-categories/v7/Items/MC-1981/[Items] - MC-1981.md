# MC-1981: All arrow types lose their name/NBT data when shot and picked up

**Mojira URL:** [https://bugs.mojang.com/browse/MC-1981](https://bugs.mojang.com/browse/MC-1981)

## Report details

- **Mojira categories:** Entities; Items
- **Project:** MC
- **Issue key:** MC-1981
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2012-11-02T14:31:58.541-0700
- **Updated:** 2025-04-29T11:53:40.582-0700
- **Resolution date:** 2023-10-25T01:42:44.189-0700
- **Affects versions:** Minecraft 1.4.2; Minecraft 1.4.6; Minecraft 1.4.7; Snapshot 13w05b; Minecraft 1.5; Minecraft 1.5.1; Minecraft 1.5.2; Snapshot 13w18c; Snapshot 13w19a; Minecraft 13w39a; Minecraft 13w39b; Minecraft 1.7.4; Minecraft 14w03b; Minecraft 14w05b; Minecraft 14w06b; Minecraft 14w07a; Minecraft 14w08a; Minecraft 1.7.5; Minecraft 14w10b; Minecraft 14w10c; Minecraft 1.8-pre2; Minecraft 1.8; Minecraft 1.8.1; Minecraft 15w31a; Minecraft 15w42a; Minecraft 15w44b; Minecraft 1.9.4; Minecraft 1.10; Minecraft 1.10.1; Minecraft 1.10.2; Minecraft 16w32a; Minecraft 16w32b; Minecraft 16w33a; Minecraft 16w40a; Minecraft 16w41a; Minecraft 16w44a; Minecraft 1.11 Pre-Release 1; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 1.12 Pre-Release 5; Minecraft 1.12 Pre-Release 6; Minecraft 1.12; Minecraft 1.12.1; Minecraft 1.12.2; Minecraft 17w50a; Minecraft 18w07c; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 19w04b; Minecraft 19w05a; Minecraft 19w06a; Minecraft 1.14.1; 1.14.4; 19w34a; 19w35a; 20w12a; 20w18a; 20w19a; 1.16 Pre-release 2; 1.16; 1.16.1; 20w27a; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Release Candidate 1; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w11a; 21w14a; 21w15a; 21w17a; 1.17; 1.17.1; 21w44a; 1.18.1; 1.18.2; 1.19; 1.19.1; 1.19.2; 1.19.3; 23w04a; 23w05a; 23w06a; 1.19.4; 23w14a; 1.20 Release Candidate 1; 1.20; 1.20.1; 23w31a; 1.20.2; 23w41a
- **Fix versions:** 23w43a
- **Area:** Platform
- **Labels:** anvil; arrow; display-Name; item-renaming; shooting
- **Watchers:** 1
- **Attachments:** 5
- **Attachment filenames:** MC-1981.mp4; MC-1981 - Stage 1.png; MC-1981 - Stage 2.png; MC-1981 - Stage 3.png; MC-1981 - Stage 4.png
- **Issue links:** Duplicate:inward:MC-15916:Arrow's names change when fired by bow | Duplicate:inward:MC-48805:Arrow | Duplicate:inward:MC-50823:Arrows lose their dataTag info once shot from a bow | Duplicate:inward:MC-160295:Arrow custom name bug | Duplicate:inward:MC-180226:arrow name | Duplicate:inward:MC-181422:arrow name | Duplicate:inward:MC-182746:arrow name | Duplicate:inward:MC-187621:Renamed arrow changed back to normal | Duplicate:inward:MC-199579:enchented arrow is unenchanted? | Relates:outward:MC-91005:Some Entities/BlockEntities don't store item data correctly | Relates:inward:MC-209:Blocks don't retain their names, enchantments, or attributes after being placed and picked up again | Relates:inward:MC-48812:Snowball Entities | Relates:inward:MC-249408:Boats with Chests lose their name when placed

## Description

The bug
Arrows lose their name and NBT data when shot and picked up.
How to reproduce
- Obtain a bow and give yourself an arrow with a custom name:

```
/give @s minecraft:arrow{display:{Name:'{"text":"MC-1981"}'}}
```

- Shoot the arrow on the ground using the bow

- Pick up the arrow
 The arrow no longer has a custom name

Expected behavior
Arrows would not lose their NBT data when shot and picked up.
Note
Other issues previously tracked in this ticket are now reported in ,  and . See this discussion for details.

## Comments (52)

### Comment 1: migrated (2012-11-02T14:31:58.541-0700)

This comment contained multiple image attachments (5), please login to view the attachments.

### Comment 2: migrated (2012-12-08T08:44:29.348-0800)

same for boats and minecarts

### Comment 3: migrated (2012-12-31T13:33:12.494-0800)

I think this works as intended. As annoying as it is, entities are not currently capable of retaining information from their item state.

### Comment 4: migrated (2013-03-24T17:27:44.974-0700)

Well I imagine it could work just like spawn eggs do, actually it would be pretty cool if boats displayed their names like mobs do.

### Comment 5: migrated (2013-09-29T13:51:45.192-0700)

Minecarts have been fixed, but arrows from a dispenser, etc. haven't.

### Comment 6: migrated (2014-02-24T02:11:58.515-0800)

Confirmed for 08a

### Comment 7: migrated (2014-03-12T06:47:46.425-0700)

Confirmed 14w10a,b,c
Arrows shot from bows, snowballs thrown at friends...

### Comment 8: qmagnet (2014-08-25T14:32:35.515-0700)

Command blocks are affected as well. They retain their NBT data but their name gets replace by [@]

### Comment 9: migrated (2014-09-24T14:36:10.080-0700)

At least cakes have been fixed in 1.8.

### Comment 10: migrated (2014-12-26T05:41:51.323-0800)

This happens for banners as well. It happens in 1.8.1. Maybe it's intended. But, please, make sure the names (given by using the anvil) are saved even after you have placed the banner in the world.

### Comment 11: migrated (2014-12-28T15:49:35.440-0800)

also happens to saddles on pigs(annoying when you get the achievement via a named saddle)

### Comment 12: migrated (2015-07-30T01:16:40.343-0700)

the tipped arrows work for this in 15w31a, yet normal arrows don't

### Comment 13: marcono1234 (2015-10-31T06:23:36.500-0700)

Confirmed for
- 15w44b as the entity TippedArrow does not longer exist (arrows have now only the tag Potion) they are also affected

### Comment 14: migrated (2015-10-31T11:53:07.290-0700)

So basically all arrows are now affected?

### Comment 15: migrated (2015-10-31T13:27:39.627-0700)

Yes

### Comment 16: FaRo1 (2016-06-12T11:57:38.878-0700)

Confirmed for 1.10.

### Comment 17: FaRo1 (2016-06-22T14:29:07.494-0700)

Confirmed for 1.10.1.

### Comment 18: migrated (2016-07-04T16:06:32.048-0700)

Confirmed for 1.10.2

### Comment 19: JUE13 (2017-05-23T00:20:35.646-0700)

Confirmed for 1.12-pre5

### Comment 20: migrated (2017-07-20T12:36:24.965-0700)

I named some arrows Bullet and picked them up. They were named "Arrow." That was in a snap shot for 1.8.

### Comment 21: FaRo1 (2017-07-20T13:10:48.054-0700)

Currently only version 1.12 is supported. 1.8 snapshots are almost 3 years old, you should really update! What do you even use to start these? They are not in the regular launcher.

### Comment 22: [Mod] bemoty (2017-08-12T06:18:17.869-0700)

Can confirm for MC 1.12.1.

### Comment 23: migrated (2018-08-24T01:21:43.957-0700)

Affects 1.13.1

### Comment 24: migrated (2019-05-16T06:41:25.748-0700)

Affects 1.14.1

### Comment 25: migrated (2020-03-19T14:09:20.760-0700)

Affects 20W12A

### Comment 26: pulpetti (2020-07-06T10:03:48.129-0700)

Affects 1.16.1

### Comment 27: pulpetti (2020-07-06T10:03:59.383-0700)

Affects 20w27a

### Comment 28: FaRo1 (2020-07-07T03:11:50.256-0700)

It's usually not very useful to confirm something for every past snapshot, only for the current one and the latest release. If you want, you can check which version introduced a bug, but I don't know if Mojang looks at that.
You can also look at this list and the reply to it if you want to do more: https://www.reddit.com/r/Mojira/comments/gr54ik/mojira_ama/fww0akd/

### Comment 29: pulpetti (2020-07-21T16:17:07.227-0700)

Affects 20w29a

### Comment 30: Avoma (2020-11-25T11:30:53.862-0800)

Can confirm in 20w48a.

### Comment 31: Avoma (2020-12-02T11:37:49.175-0800)

Can confirm in 20w49a.

### Comment 32: Avoma (2021-01-22T02:53:41.457-0800)

Can confirm in 21w03a.

### Comment 33: Avoma (2021-02-03T11:12:02.494-0800)

Can confirm in 21w05a.

### Comment 34: Avoma (2021-02-04T10:29:19.835-0800)

Can confirm in 21w05b.

### Comment 35: ArmouredMonkey (2021-02-10T10:48:28.742-0800)

Can confirm in 21w06a

### Comment 36: Avoma (2021-02-18T10:36:53.174-0800)

Can confirm in 21w07a. Video attached.

### Comment 37: Avoma (2021-03-18T02:54:22.453-0700)

Can confirm in 21w11a.

### Comment 38: Avoma (2021-04-11T07:15:15.298-0700)

Can confirm in 1.16.5 and 21w14a.

### Comment 39: Avoma (2021-04-19T00:46:07.556-0700)

Can confirm in 21w15a.

### Comment 40: Avoma (2021-04-30T05:53:57.481-0700)

Can confirm in 21w17a.

### Comment 41: Avoma (2021-06-16T11:55:09.342-0700)

Can confirm in 1.17.

### Comment 42: ampolive (2021-07-19T15:13:17.520-0700)

Can confirm in 1.17.1.

### Comment 43: Avoma (2021-11-07T02:22:54.764-0800)

Can confirm this in 21w44a. Here are some extra details regarding this problem.
The Bug:
Arrows lose their NBT data when shot and picked up.
Steps to Reproduce:
- Obtain a bow and give yourself an arrow with a custom name.

```/give @s minecraft:arrow{display:{Name:'{"text":"MC-1981"}'}}```
- Shoot the arrow on the ground using the bow.

- Pick up the arrow and take note as to whether or not it retains its custom name.

Observed Behavior:
Arrows lose their NBT data when shot and picked up.
Expected Behavior:
Arrows would not lose their NBT data when shot and picked up.

### Comment 44: Avoma (2021-12-14T09:40:52.317-0800)

Can confirm in 1.18.1.

### Comment 45: Avoma (2022-03-02T06:04:03.054-0800)

Can confirm in 1.18.2.

### Comment 46: Avoma (2022-06-08T05:32:22.764-0700)

Can confirm in 1.19.

### Comment 47: Avoma (2022-07-28T06:16:18.822-0700)

Can confirm in 1.19.1.

### Comment 48: Avoma (2022-08-06T11:56:06.807-0700)

Can confirm in 1.19.2.

### Comment 49: Brain81505 (2023-01-24T23:26:11.387-0800)

Can confirm in 23w04a

### Comment 50: Brain81505 (2023-02-01T08:06:07.362-0800)

Can confirm in 23w05a

### Comment 51: Brain81505 (2023-02-11T07:33:35.515-0800)

Can confirm in 23w06a

### Comment 52: Brevort (2023-06-14T15:48:51.305-0700)

Affects 1.20.1.
