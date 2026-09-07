# MC-214619: Sculk sensors cannot detect application of ink sacs to signs

**Mojira URL:** [https://bugs.mojang.com/browse/MC-214619](https://bugs.mojang.com/browse/MC-214619)

## Report details

- **Mojira categories:** Game Events
- **Project:** MC
- **Issue key:** MC-214619
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2021-02-09T04:23:05.123-0800
- **Updated:** 2025-04-11T12:40:38.035-0700
- **Resolution date:** 2023-08-29T07:12:10.153-0700
- **Affects versions:** 21w05b; 21w06a; 21w07a; 21w08b; 21w11a; 21w14a; 21w17a; 1.17; 1.17.1; 21w37a; 21w43a; 1.18.1; 22w03a; 1.18.2; 1.19 Pre-release 1; 1.19 Pre-release 2; 1.19 Pre-release 3; 1.19; 22w24a; 1.19.3; 23w05a; 23w06a; 1.19.4 Pre-release 4
- **Fix versions:** 23w12a
- **Labels:** sculk_sensor
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** 2021-02-09_12.22.13.png; 2021-02-09_12.22.15.png; 2022-05-19_15.56.23.png; 2022-05-19_15.56.28.png; 2022-05-19_15.56.31.png; MC-214619.mp4
- **Issue links:** Relates:outward:MC-210334:Sculk sensors are not activated upon sheep being dyed

## Description

The Bug
When applying an ink sac or glow ink sac to a sign, sculk sensors nearby won't detect that.
Steps to Reproduce
-     Summon a sign with some text on it.

```
/setblock ~ ~ ~ minecraft:dark_oak_sign{Color:"magenta",Text1:'{"text":"MC-214619"}'}
```

-     Place down a sculk sensor nearby and obtain some ink sacs and glow ink sacs.

-     Apply a glow ink sac to the sign.

-     Take note as to whether or not the sculk sensor activates.

-     Apply an ink sac to the sign.

-     Take note as to whether or not the sculk sensor activates.

Observed Behavior
Sculk sensors are not activated upon using ink sacs or glow ink sacs on signs.
Expected Behavior
Sculk sensors would be activated upon using ink sacs or glow ink sacs on signs.

## Comments (16)

### Comment 1: migrated (2021-02-09T04:23:05.123-0800)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: migrated (2021-02-09T08:01:01.966-0800)

Can confirm

### Comment 3: Avoma (2021-02-11T08:20:52.880-0800)

Can confirm in 21w06a.

### Comment 4: Avoma (2021-02-20T04:06:32.205-0800)

Can confirm in 21w07a.

### Comment 5: Avoma (2021-02-26T06:55:08.960-0800)

Can confirm in 21w08b.

### Comment 6: Avoma (2021-03-20T04:35:16.256-0700)

Can confirm in 21w11a.

### Comment 7: Avoma (2021-04-10T02:54:36.517-0700)

Can confirm in 21w14a.

### Comment 8: Avoma (2021-04-29T01:15:38.324-0700)

Can confirm in 21w17a.

### Comment 9: Avoma (2021-06-09T11:50:23.155-0700)

Can confirm in 1.17.

### Comment 10: Avoma (2021-07-23T02:40:41.942-0700)

Can confirm in 1.17.1.

### Comment 11: ampolive (2021-09-22T14:36:02.816-0700)

Can confirm in 21w37a.

### Comment 12: Avoma (2021-10-28T03:20:54.599-0700)

Can confirm this behavior in 21w43a. Here are some extra details regarding this problem.
The Bug:
Sculk sensors are not activated upon using ink sacs or glow ink sacs on signs.
Steps to Reproduce:
- Summon a sign with some text on it.

```/setblock ~ ~ ~ minecraft:dark_oak_sign{Color:"magenta",Text1:'{"text":"MC-214619"}'}```
- Place down a sculk sensor nearby and obtain some ink sacs and glow ink sacs.

- Apply a glow ink sac to the sign.

- Take note as to whether or not the sculk sensor activates.

- Apply an ink sac to the sign.

- Take note as to whether or not the sculk sensor activates.

Observed Behavior:
Sculk sensors are not activated upon using ink sacs or glow ink sacs on signs.
Expected Behavior:
Sculk sensors would be activated upon using ink sacs or glow ink sacs on signs.

### Comment 13: Avoma (2021-12-20T00:09:47.458-0800)

Can confirm in 1.18.1.

### Comment 14: Avoma (2022-03-06T10:49:45.687-0800)

Can confirm in 1.18.2.

### Comment 15: Avoma (2022-06-21T09:58:22.899-0700)

Can confirm in 1.19 and 22w24a.

### Comment 16: ampolive (2023-08-29T07:11:57.378-0700)

Fixed in 23w12a.
