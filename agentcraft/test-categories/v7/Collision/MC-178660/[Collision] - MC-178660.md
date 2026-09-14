# MC-178660: Player jitters when landing on a bed with the slow falling effect

**Mojira URL:** [https://bugs.mojang.com/browse/MC-178660](https://bugs.mojang.com/browse/MC-178660)

## Report details

- **Mojira categories:** Collision; Player
- **Project:** MC
- **Issue key:** MC-178660
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2020-04-14T07:20:22.627-0700
- **Updated:** 2025-04-26T09:47:04.724-0700
- **Resolution date:** 2024-12-12T09:42:36.154-0800
- **Affects versions:** 1.15.2; 20w15a; 20w30a; 20w49a; 21w03a; 1.16.5; 21w08b; 21w15a; 1.17; 1.17.1; 21w42a; 21w44a; 1.18.2; 1.19.2; 1.19.4; 1.20.1; 23w43a
- **Fix versions:** 24w33a
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** MC-178660.mp4; MC-178660.png; Minecraft 24w33a - Singleplayer 2024-12-12 14-21-38.mp4
- **Issue links:** Relates:inward:MC-151706:Player jitters when landing on a slime block with the slow falling effect | Duplicate:inward:MC-264960:Players who drink the Slow Falling Potion will keep jumping on the bed. | Duplicate:inward:MC-241033:Slowfalling on Bed | Duplicate:inward:MC-233956:Player jitters up and down when sleeping in a bed with the Slow Falling effect

## Description

The Bug
If an entity (player, mob, armor stand...) falls on a bed/slime block while having the Slow Falling effect, it will bounce much less than normal, and that's OK, but when it finishes bouncing a weird shaking animation starts. This animation ends when the entity walks off the block or when the Slow Falling effect lasts. However, this issue will not occur when a player with Slow Falling falls on a bed/slime block while pressing Shift.
Steps to Reproduce
- Place down a bed and give yourself the slow falling effect.

```
/effect give @s minecraft:slow_falling 100 0
```

-  Jump on top of the bed and watch your screen closely.

- Take note as to whether or not players jitter when landing on beds with the slow falling effect.

Observed Behavior
Players jitter when landing on beds with the slow falling effect.
Expected Behavior
Players would not jitter when landing on beds with the slow falling effect.

## Comments (14)

### Comment 1: migrated (2020-04-14T07:20:22.627-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: migrated (2020-07-24T16:57:18.389-0700)

Confirmed in 20w30a.

### Comment 3: Avoma (2020-12-03T10:43:20.825-0800)

Can confirm in 20w49a.

### Comment 4: Avoma (2021-01-31T03:23:11.019-0800)

Can confirm in 21w03a.

### Comment 5: Avoma (2021-03-06T06:37:12.292-0800)

Can confirm in 1.16.5 and 21w08b. Video attached.

### Comment 6: Avoma (2021-04-18T10:24:27.470-0700)

Can confirm in 21w15a.

### Comment 7: Avoma (2021-06-13T09:58:38.817-0700)

Can confirm in 1.17.

### Comment 8: Avoma (2021-07-23T07:11:39.839-0700)

Can confirm in 1.17.1.

### Comment 9: Avoma (2021-10-23T05:24:32.294-0700)

Can confirm in 21w42a. Here are some extra details regarding this problem.
The Bug:
Players jitter when landing on beds with the slow falling effect.
Steps to Reproduce:
- Place down a bed and give yourself the slow falling effect.

```/effect give @s minecraft:slow_falling 100 0```
- Jump on top of the bed and watch your screen closely.

- Take note as to whether or not players jitter when landing on beds with the slow falling effect.

Observed Behavior:
Players jitter when landing on beds with the slow falling effect.
Expected Behavior:
Players would not jitter when landing on beds with the slow falling effect.

### Comment 10: migrated (2021-11-09T09:31:34.631-0800)

Can confirm in 21w44a

### Comment 11: Avoma (2022-03-09T11:47:46.236-0800)

Can confirm in 1.18.2.

### Comment 12: Avoma (2022-09-06T10:48:07.986-0700)

Can confirm in 1.19.2.

### Comment 13: Brain81505 (2023-04-18T05:09:36.185-0700)

Can confirm in 1.19.4

### Comment 14: yalming22 (2024-12-11T21:23:35.854-0800)

This issue was fixed in 24w33a with .
