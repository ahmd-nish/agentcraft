# MC-177965: Putting on/taking off soul speed boots while standing on soul sand/soil does not properly give speed

**Mojira URL:** [https://bugs.mojang.com/browse/MC-177965](https://bugs.mojang.com/browse/MC-177965)

## Report details

- **Mojira categories:** Items
- **Project:** MC
- **Issue key:** MC-177965
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2020-04-08T18:58:07.132-0700
- **Updated:** 2025-04-29T09:44:23.812-0700
- **Resolution date:** 2024-04-30T01:47:56.276-0700
- **Affects versions:** 20w15a; 20w16a; 20w17a; 20w18a; 20w19a; 20w20a; 20w20b; 20w21a; 20w22a; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 4; 1.16 Pre-release 5; 1.16 Pre-release 6; 1.16 Pre-release 7; 1.16 Pre-release 8; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w27a; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Pre-release 2; 1.16.2 Pre-release 3; 1.16.2 Release Candidate 1; 1.16.2 Release Candidate 2; 1.16.2; 1.16.3; 1.16.4 Pre-release 2; 1.16.4 Release Candidate 1; 1.16.4; 20w48a; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w07a; 21w11a; 21w13a; 1.17 Pre-release 1; 1.17; 1.17.1; 21w42a; 1.18.1; 1.18.2; 22w11a; 1.19; 1.19.2; 1.19.4; 23w18a; 1.20.1
- **Fix versions:** 24w18a
- **Area:** Gameplay
- **Labels:** soul_speed
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** MC-177965.mp4; MC-177965.png; Minecraft 1.16 Pre-release 4 - Singleplayer 2020-06-11 23-13-00.mp4
- **Issue links:** Duplicate:inward:MC-188749:Taking off soul speed boots while standing on soul blocks doesn't remove the speed effect immediately | Relates:outward:MC-175911:Soul Speed lasts after leaving soul blocks

## Description

The Bug
Putting on soul speed boots while standing on soul blocks gives you no speed. Likewise, taking off soul speed boots while standing on soul blocks doesn't take away your speed until you move off of the block.
Steps to Reproduce
-     Replace the ground beneath you with some soul soil.

```
/fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 minecraft:soul_soil
```

-     Equip some boots enchanted with soul speed whilst standing on top of the soul soil.

```
/item replace entity @s armor.feet with minecraft:golden_boots{Enchantments:[{id:"soul_speed",lvl:3}]}
```
 →  Notice how the soul speed enchantment effect is not granted until you begin moving.

-     Remove the boots from your feet whilst the soul speed enchantment effect is active.

```
/item replace entity @s armor.feet with minecraft:air
```
 →  Notice how the soul speed enchantment effect is not removed until you begin moving.

Observed Behavior
Equipping or unequipping boots enchanted with soul speed whilst standing on soul blocks doesn't correctly grant or remove the soul speed enchantment effect.
Expected Behavior
Equipping or unequipping boots enchanted with soul speed whilst standing on soul blocks would correctly grant or remove the soul speed enchantment effect. Upon equipping some soul speed boots whilst standing on soul blocks, the soul speed enchantment effect should be immediately granted without having the need to move. Upon unequipping some soul speed boots whilst standing on soul

## Comments (17)

### Comment 1: migrated (2020-04-08T18:58:07.132-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: Avoma (2020-11-28T09:02:06.008-0800)

Can confirm in 20w48a. Here's a command so you can easily reproduce it.

```/give @s netherite_boots{Enchantments:[{id:soul_speed,lvl:3}]}```

### Comment 3: Avoma (2021-01-18T08:17:45.736-0800)

Can confirm in 1.16.5 and 20w51a.

### Comment 4: Avoma (2021-01-20T11:11:42.227-0800)

Can confirm in 21w03a.

### Comment 5: Avoma (2021-02-05T05:36:52.381-0800)

Can confirm in 21w05b.

### Comment 6: Avoma (2021-02-12T09:39:38.505-0800)

Can confirm in 21w06a.

### Comment 7: Avoma (2021-02-18T04:42:08.043-0800)

Can confirm in 21w07a.

### Comment 8: Avoma (2021-03-21T06:41:07.827-0700)

Can confirm in 21w11a.

### Comment 9: Avoma (2021-04-06T03:48:07.477-0700)

Can confirm in 21w13a.

### Comment 10: Brevort (2021-05-28T12:52:13.646-0700)

Can confirm in 1.17-pre1.

### Comment 11: Avoma (2021-06-24T08:09:02.795-0700)

Can confirm in 1.17.

### Comment 12: Avoma (2021-07-22T12:33:03.150-0700)

Can confirm in 1.17.1.

### Comment 13: Avoma (2021-10-22T11:02:07.608-0700)

Can confirm in 21w42a. Here are some extra details regarding this problem.
The Bug:
Equipping or unequipping boots enchanted with soul speed whilst standing on soul blocks doesn't correctly grant or remove the soul speed enchantment effect.
Steps to Reproduce:
- Replace the ground beneath you with some soul soil.

```/fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 minecraft:soul_soil```
- Equip some boots enchanted with soul speed whilst standing on top of the soul soil.

```/item replace entity @s armor.feet with minecraft:golden_boots{Enchantments:[{id:"soul_speed",lvl:3}]}```
- →  Notice how the soul speed enchantment effect is not granted until you begin moving.

- Remove the boots from your feet whilst the soul speed enchantment effect is active.

```/item replace entity @s armor.feet with minecraft:air```
- →  Notice how the soul speed enchantment effect is not removed until you begin moving.

Observed Behavior:
Equipping or unequipping boots enchanted with soul speed whilst standing on soul blocks doesn't correctly grant or remove the soul speed enchantment effect.
Expected Behavior:
Equipping or unequipping boots enchanted with soul speed whilst standing on soul blocks would correctly grant or remove the soul speed enchantment effect.
Upon equipping some soul speed boots whilst standing on soul blocks, the soul speed enchantment effect should be immediately granted without having the need to move. Upon unequipping some soul speed boots whilst standing on soul blocks, the soul speed enchantment effect should be immediately removed without having the need to move.

### Comment 14: Avoma (2021-12-19T05:56:58.608-0800)

Can confirm in 1.18.1.

### Comment 15: Avoma (2022-03-22T10:43:11.683-0700)

Can confirm in 1.18.2 and 22w11a.

### Comment 16: Avoma (2022-07-05T06:21:48.787-0700)

Can confirm in 1.19.

### Comment 17: Avoma (2022-09-06T10:32:17.810-0700)

Can confirm in 1.19.2.
