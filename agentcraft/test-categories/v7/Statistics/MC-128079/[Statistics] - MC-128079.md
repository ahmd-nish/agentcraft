# MC-128079: Statistic for using shears doesn't increase when mining certain blocks

**Mojira URL:** [https://bugs.mojang.com/browse/MC-128079](https://bugs.mojang.com/browse/MC-128079)

## Report details

- **Mojira categories:** Statistics
- **Project:** MC
- **Issue key:** MC-128079
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2018-04-06T14:49:15.703-0700
- **Updated:** 2025-04-26T06:28:52.513-0700
- **Resolution date:** 2025-01-07T06:21:24.148-0800
- **Affects versions:** Minecraft 18w14b; Minecraft 18w15a; Minecraft 18w16a; Minecraft 18w20c; Minecraft 18w21a; Minecraft 18w22c; Minecraft 1.13-pre1; Minecraft 1.13; Minecraft 18w30b; Minecraft 18w31a; Minecraft 18w32a; Minecraft 18w33a; Minecraft 1.13.1-pre1; Minecraft 1.13.1-pre2; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w43b; Minecraft 18w43c; Minecraft 18w44a; Minecraft 18w45a; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 19w12b; Minecraft 19w13b; Minecraft 19w14a; Minecraft 1.14 Pre-Release 2; Minecraft 1.14 Pre-Release 3; Minecraft 1.14 Pre-Release 4; Minecraft 1.14 Pre-Release 5; Minecraft 1.14; Minecraft 1.14.1; Minecraft 1.14.2 Pre-Release 2; Minecraft 1.14.2 Pre-Release 3; Minecraft 1.14.2; Minecraft 1.14.3 Pre-Release 1; Minecraft 1.14.3 Pre-Release 3; Minecraft 1.14.3; Minecraft 1.14.4 Pre-Release 3; Minecraft 1.14.4 Pre-Release 4; Minecraft 1.14.4 Pre-Release 5; Minecraft 1.14.4 Pre-Release 6; 1.14.4; 1.15.2; 20w18a; 1.16.4; 20w48a; 1.16.5; 21w05b; 21w06a; 21w14a; 21w18a; 21w20a; 1.17.1; 1.18.2; 1.19; 1.19.3; 1.20.1; 1.20.4; 1.20.6; 24w21b
- **Fix versions:** 25w02a
- **Area:** Platform
- **Game mode:** Survival
- **Labels:** carpet; durability; shears; statistics; tool
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-128079.mp4; MC-128079.png
- **Issue links:** Duplicate:inward:MC-272521:Shears item use statistic ignores tool component

## Description

Add a scoreboard with shears being used as the criteria:

```
/scoreboard objectives add shear minecraft.used:minecraft.shears
```
Display it in the sidebar:

```
/scoreboard objectives setdisplay sidebar shear
```
This scoreboard objective doesn't increase when mining carpet with shears and the other mentioned blocks.
If you use the criteria "minecraft.used:minecraft.diamond_pickaxe" and use said diamond pickaxe to mine carpet the score for the pickaxe increases, so why wouldn't it with shears?
Another Argument on why this is a bug is that the durability decreases in both cases, so the tools are clearly being used!
I think it might be good to have a list of blocks where it does not work. For the reason that you need to have the block mined with shears to actually collect an item, but where the criteria does not tick up.
- tall_grass

- large_fern

- seagrass

- tall_seagrass

- nether_sprouts

## Comments (9)

### Comment 1: migrated (2018-04-06T14:49:15.703-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: bluecrab2 (2020-11-25T22:11:38.094-0800)

Confirmed in 20w48a

### Comment 3: Avoma (2021-02-09T01:18:22.128-0800)

Can confirm in 21w05b.

### Comment 4: Avoma (2021-02-17T03:50:04.836-0800)

Can confirm in 21w06a.

### Comment 5: Avoma (2021-04-11T07:17:18.043-0700)

Can confirm in 1.16.5 and 21w14a.

### Comment 6: Avoma (2021-08-21T06:37:26.257-0700)

Can confirm in 1.17.1. Video attached.

### Comment 7: Avoma (2022-03-08T10:33:36.806-0800)

Can confirm in 1.18.2.

### Comment 8: Avoma (2022-06-22T06:35:08.675-0700)

Can confirm in 1.19.

### Comment 9: Brain81505 (2023-01-18T03:10:23.035-0800)

Can confirm in 1.19.3
