# MC-212629: Leashes from two or more invisible entities connect to each other

**Mojira URL:** [https://bugs.mojang.com/browse/MC-212629](https://bugs.mojang.com/browse/MC-212629)

## Report details

- **Mojira categories:** Rendering
- **Project:** MC
- **Issue key:** MC-212629
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-01-23T12:05:30.532-0800
- **Updated:** 2025-04-30T08:45:58.188-0700
- **Resolution date:** 2022-04-08T05:00:52.933-0700
- **Affects versions:** 21w03a; 21w05b; 21w06a; 21w07a; 21w08b; 21w11a; 21w13a; 21w14a; 21w17a; 21w18a; 1.17; 1.17.1 Release Candidate 1; 1.17.1; 21w42a; 1.18.1; 22w12a
- **Fix versions:** 22w15a
- **Watchers:** 1
- **Attachments:** 7
- **Attachment filenames:** 2021-01-28_12.00.03.png; 2021-06-30_14.59.30.png; 2022-03-29_09.14.27.png; Buged Leash.png; image-2022-02-22-22-52-08-057.png; MC-212629.mp4; MC-212629.png

## Description

The Bug
The visual leash created when leading two or more invisible entities wether attached to the player or a fence connects to the endpoint of other leashes. This can easily be recreated by putting two cows in glass boxes then leading both and splashing them with invisibility.
Steps to Reproduce
-     Obtain two leads and summon two cows in front of you.

```
/summon minecraft:cow ~1 ~ ~-2.5 {NoAI:1b}
/summon minecraft:cow ~-1 ~ ~-2.5 {NoAI:1b}
```

-     Attach a lead to each of the cows and give both of them the invisibility effect.

```
/effect give @e[type=minecraft:cow,sort=nearest,limit=2] minecraft:invisibility 999 0
```

-     Look at the leashes carefully.

-     Take note as to whether or not leashes from two or more invisible entities connect to one another.

Observed Behavior
Leashes from two or more invisible entities connect to one another.
Expected Behavior
Leashes from two or more invisible entities would not connect to one another.

## Comments (21)

### Comment 1: migrated (2021-01-23T12:05:30.532-0800)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: Avoma (2021-01-28T04:00:59.464-0800)

Can confirm. I've attached an additional screenshot with the F3 debug screen enabled.

### Comment 3: Avoma (2021-02-05T11:22:41.817-0800)

Can confirm in 21w05b.

### Comment 4: Avoma (2021-02-14T09:17:01.896-0800)

Can confirm in 21w06a.

### Comment 5: Avoma (2021-02-27T10:27:41.009-0800)

Can confirm in 21w08b. Video attached.

### Comment 6: Avoma (2021-03-20T05:23:08.332-0700)

Can confirm in 21w11a.

### Comment 7: Avoma (2021-04-05T04:49:15.783-0700)

Can confirm in 21w13a.

### Comment 8: Avoma (2021-04-10T05:26:47.557-0700)

Can confirm in 21w14a.

### Comment 9: Avoma (2021-04-28T11:21:51.669-0700)

Can confirm in 21w17a.

### Comment 10: Avoma (2021-05-07T03:39:02.124-0700)

Just to clarify, this issue did not exist in 1.16.5. Also can confirm in 21w18a.

### Comment 11: KirbAvion (2021-06-09T19:37:19.878-0700)

Can confirm for release 1.17.

### Comment 12: migrated (2021-06-27T17:31:59.760-0700)

Definitely an annoying issue with Minecraft 1.17. When leads between invisible entities are used for cosmetic displays, the glitching looks really bad.

### Comment 13: KirbAvion (2021-07-03T00:15:52.496-0700)

Can confirm in 1.17.1 release candidate 1.

### Comment 14: migrated (2021-07-31T09:00:10.756-0700)

Glitches are not visible if you view in Spectator mode.

### Comment 15: migrated (2021-08-30T13:20:13.061-0700)

I've tape-fixed this bug with resource pack. Download there: https://www.dropbox.com/s/bmbufltqjxok3l3/leashFix.zip?dl=1
I'm sorry if this comment violates the rules or my pack doesn't work.

### Comment 16: Avoma (2021-10-27T02:46:01.627-0700)

Can confirm this behavior in 21w42a. Here are some extra details regarding this problem.
The Bug:
Leashes from two or more invisible entities connect to one another.
Steps to Reproduce:
- Obtain two leads and summon two cows in front of you.

```/summon minecraft:cow ~1 ~ ~-2.5 {NoAI:1b}
/summon minecraft:cow ~-1 ~ ~-2.5 {NoAI:1b}```
- Attach a lead to each of the cows and give both of them the invisibility effect.

```/effect give @e[type=minecraft:cow,sort=nearest,limit=2] minecraft:invisibility 999 0```
- Look at the leashes carefully.

- Take note as to whether or not leashes from two or more invisible entities connect to one another.

Observed Behavior:
Leashes from two or more invisible entities connect to one another.
Expected Behavior:
Leashes from two or more invisible entities would not connect to one another.

### Comment 17: migrated (2021-12-10T10:01:07.728-0800)

Can confirm this behavior in 1.18 and 1.18.1.

### Comment 18: migrated (2022-02-22T13:52:32.029-0800)

Can confirm this behavior in 1.19_deep_dark_experimental_snapshot-1

### Comment 19: KirbAvion (2022-03-29T05:06:37.795-0700)

This looks like it might be fixed in 22w12a, can anyone else confirm?

### Comment 20: ampolive (2022-03-29T05:13:14.882-0700)

Not fixed in 22w12a, it is just not visible from certain angles because of the way the lead is rendered.

### Comment 21: KirbAvion (2022-03-29T06:18:51.660-0700)

Oh, shoot, you know what, the resource pack in my test world still has Vlad's patched shader file in it. Well, at least we know that still works.
