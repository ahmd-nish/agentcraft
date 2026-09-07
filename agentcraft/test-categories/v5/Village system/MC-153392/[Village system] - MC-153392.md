# MC-153392: Unable to remove villager gossips using /data remove

**Mojira URL:** [https://bugs.mojang.com/browse/MC-153392](https://bugs.mojang.com/browse/MC-153392)

## Report details

- **Mojira categories:** Commands; Village system
- **Project:** MC
- **Issue key:** MC-153392
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2019-05-29T17:09:49.069-0700
- **Updated:** 2025-04-26T08:05:40.139-0700
- **Resolution date:** 2025-02-12T04:55:53.106-0800
- **Affects versions:** Minecraft 1.14.2; 19w36a; 1.15.1; 20w15a; 20w16a; 1.16.4; 20w51a; 1.16.5; 1.18 Pre-release 6; 1.18.1; 1.18.2; 1.19; 1.19.1; 1.19.2; 1.19.3; 1.19.4; 23w43b; 1.21.3; 1.21.4 Pre-Release 1
- **Fix versions:** 25w07a
- **Area:** Platform
- **Labels:** /data-remove; mojang_internal_1; nbt; villager
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2019-05-29 19-52-56.mp4; MC-153392.png
- **Issue links:** Relates:inward:MC-135044:/data remove cannot remove attribute (modifier)s | Relates:outward:MC-122840:"/data remove" cannot delete beam_target tag in End Crystals

## Description

The bug
The /data remove command doesn't remove Gossips entries from villagers. I'm not sure if it matters, but this villager has a lot of Gossips entries, enough to where when you show chat and try scrolling up, the game won't let you scroll up enough to view all the entries.
How to reproduce
- Have a villager with Gossips entries

- Run /data remove command on said villager
→  Gossips entries will not be removed, as seen in the video file.

Observed Behavior
Villagers' "Gossips" tag cannot be removed by using the "/data remove" command.
Expected Behavior
Villagers' "Gossips" tag would be able to be removed by using the "/data remove" command.

## Comments (21)

### Comment 1: migrated (2019-05-29T17:09:49.069-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: migrated (2019-09-08T01:34:58.306-0700)

Confirmed for 19w36a

### Comment 3: KirbAvion (2019-12-29T00:42:14.253-0800)

Confirmed for release 1.15.1

### Comment 4: migrated (2020-04-11T01:50:39.288-0700)

Still present in 20w15a

### Comment 5: migrated (2020-04-17T21:43:55.903-0700)

Still present in 20w16a

### Comment 6: Avoma (2020-12-19T09:25:29.889-0800)

Can confirm in 20w51a.

### Comment 7: migrated (2021-02-01T21:25:38.116-0800)

Additionally, it seems no modifications whatsoever can be made to the Gossips data on Villagers and Zombie Villagers.

### Comment 8: migrated (2021-04-01T20:40:18.616-0700)

Still present in 1.16.5

### Comment 9: Avoma (2021-11-23T03:38:00.380-0800)

Can confirm this in 1.18 Pre-release 6. Here are some extra details regarding this problem.
The Bug:
Villagers' "Gossips" tag cannot be removed by using the "/data remove" command.
Steps to Reproduce:
- Summon a villager and attack it.

- Inspect the value of its "Gossips" tag by using the "/data" command and take note of how some data is present.

```/data get entity @e[type=minecraft:villager,limit=1,sort=nearest] Gossips```
- Attempt to use the "/data remove" command to remove its "Gossips" data.

```/data remove entity @e[type=minecraft:villager,limit=1,sort=nearest] Gossips```
- Inspect the value of its "Gossips" tag by using the "/data" command once again.

```/data get entity @e[type=minecraft:villager,limit=1,sort=nearest] Gossips```
- Take note as to whether or not villagers' "Gossips" tag can be removed by using the "/data remove" command.

Observed Behavior:
Villagers' "Gossips" tag cannot be removed by using the "/data remove" command.
Expected Behavior:
Villagers' "Gossips" tag would be able to be removed by using the "/data remove" command.

### Comment 10: Avoma (2022-01-05T10:56:35.430-0800)

Can confirm in 1.18.1.

### Comment 11: Avoma (2022-03-31T09:06:30.389-0700)

Can confirm in 1.18.2.

### Comment 12: migrated (2022-04-14T08:12:33.703-0700)

Dang how many votes does this issue need

### Comment 13: Avoma (2022-07-15T12:04:16.247-0700)

Can confirm in 1.19.

### Comment 14: connor135246 (2022-08-02T14:43:12.055-0700)

Can confirm in 1.19.1.

### Comment 15: Avoma (2022-09-24T03:04:43.899-0700)

Can confirm in 1.19.2.

### Comment 16: connor135246 (2022-12-18T16:17:24.090-0800)

Can confirm in 1.19.3.
Also: in 1.19.2, I was able to use "/data modify ... merge" to change gossip values. For example, I used the following to remove permanent curing discounts:
/data modify entity @e[type=villager,limit=1] Gossips[{Type:"major_positive"}] merge value {Value:0}
But as of 1.19.3, this no longer works.

### Comment 17: connor135246 (2023-04-01T19:35:41.233-0700)

Can confirm in 1.19.4.
As an addendum to my previous comment:
I've discovered that while Villager Gossips cannot be changed with /data, Zombie Villager Gossips can! So it's possible to prevent the permanent curing discount from stacking more than once by setting a Zombie Villager's "major positive" gossips back to 0.

### Comment 18: migrated (2023-04-08T17:14:19.885-0700)

Relates to , MC-179815, , MC-207605, , , MC-248264.

### Comment 19: migrated (2023-04-21T00:26:50.528-0700)

so i was doing some trial and error. i still need to verify but something happened when i set the value to 1. it eroded away and removed the specific gossip. so while /data remove did not want to work i actually got it to remove the major_positive.

```/data modify entity @e[ID] Gossips[{Type: "major_positive", Target: [I; UUID]}].Value set value 1```
what happened is that i was playing with commands and mistyped the UUID so it ended up being listed twice. not a huge deal but the OCD in me wanted the bogus one removed. you can set the value but not to zero. obviously use the entity ID and UUID specific to your world.

### Comment 20: KNIZE1007 (2023-08-03T01:16:37.665-0700)

Can confirm in 23w31a.

### Comment 21: migrated (2024-11-08T16:56:36.580-0800)

Can confirm for 1.21.3
