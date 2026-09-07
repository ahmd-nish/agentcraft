# MC-213349: Certain mobs that can melee can't use the Fire Aspect enchantment

**Mojira URL:** [https://bugs.mojang.com/browse/MC-213349](https://bugs.mojang.com/browse/MC-213349)

## Report details

- **Mojira categories:** Commands; Data Packs; Enchantments
- **Project:** MC
- **Issue key:** MC-213349
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2021-01-29T14:55:09.376-0800
- **Updated:** 2025-04-29T09:44:38.530-0700
- **Resolution date:** 2024-04-30T01:47:55.149-0700
- **Affects versions:** 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w08b; 21w10a; 21w11a; 21w13a; 21w14a; 21w15a; 21w16a; 21w17a; 21w18a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17 Pre-release 2; 1.17 Pre-release 3; 1.17 Pre-release 4; 1.17 Pre-release 5; 1.17 Release Candidate 1; 1.17 Release Candidate 2; 1.17; 1.17.1 Pre-release 1; 1.17.1 Pre-release 2; 1.17.1 Release Candidate 1; 1.17.1; 21w37a; 21w38a; 21w39a; 21w40a; 21w41a; 21w42a; 21w43a; 21w44a; 1.18 Pre-release 1; 1.18 Pre-release 5; 1.18; 1.18.1 Pre-release 1; 1.18.1; 1.18.2; 22w13a; 22w14a; 22w15a; 22w17a; 1.19 Pre-release 1; 1.19 Pre-release 2; 1.19; 1.19.2; 22w43a; 1.19.3; 23w04a; 1.19.4; 1.20 Pre-release 1; 1.20.1; 1.20.4
- **Fix versions:** 24w18a
- **Area:** Platform
- **Labels:** CanPickUpLoot; attack; enchantment; fire_aspect; mob
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-213349.mp4; MC-213349.png

## Description

The Bug
Some mobs that are able to melee and are given an item (by setting their NBT tag 'CanPickUpLoot' to true) that is enchanted with Fire Aspect do not set their target on fire when they attack with said item. While these mobs do not have the ability to pick up items in survival, others mobs which normally can't pick up items nor render the item being held (such as Spiders, Silverfish, Endermen, etc.) the Fire Aspect enchantment works as expected.
Affected Mobs
- Bee

- Cat

- Dolphin (Always drop item it 'holds' anyway)

- Goat

- Hoglin

- Iron Golem

- Magma Cube

- Ocelot

- Polar Bear

- Rabbit (The Killer Bunny)

- Slime

- Wolf

- Zoglin

Steps to Reproduce
-     Summon any of the affected entites listed above, who are holding a sword enchanted with fire aspect, for example, a zoglin.

```
/summon minecraft:zoglin ~ ~ ~ {HandItems:[{Count:1b,id:"minecraft:wooden_sword",tag:{Enchantments:[{id:fire_aspect,lvl:1}]}}]}
```

-     Double-check to see whether or not the zoglin is holding a sword enchanted with fire aspect.

```
/data get entity @e[type=minecraft:zoglin,limit=1,sort=nearest] HandItems
```

-     Summon a pig nearby so that the zoglin will attack it.

-     As the zoglin attacks the pig, take note as to whether or not the pig is ignited.

Observed Behavior
Several entities that have melee attacks can't use the fire aspect enchantment.
Expected Behavior
Several entities that have melee attacks would be able to use the fire aspect enchantment.

## Comments (8)

### Comment 1: migrated (2021-01-29T14:55:09.376-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: FivesBlue (2021-01-29T17:44:38.871-0800)

Can confirm, was able to test all except cat, dolphin, and ocelot, none of the mobs trigger the player to burn as they should

### Comment 3: chumbanotz (2021-01-29T17:53:44.084-0800)

You can test the cat by spawning a rabbit for it to attack, and for the ocelot you can spawn a chicken. The dolphin really can't even be tested, but I thought I would include it anyway from my findings.

### Comment 4: Avoma (2021-02-28T10:58:28.249-0800)

Can confirm in 1.16.5.

### Comment 5: Avoma (2021-10-27T03:02:27.634-0700)

Can confirm this behavior in 21w42a. Here are some extra details regarding this problem.
The Bug:
Several entities that have melee attacks can't use the fire aspect enchantment.
Steps to Reproduce:
- Summon any of the affected entites listed above, who are holding a sword enchanted with fire aspect, for example, a zoglin.

```/summon minecraft:zoglin ~ ~ ~ {HandItems:[{Count:1b,id:"minecraft:wooden_sword",tag:{Enchantments:[{id:fire_aspect,lvl:1}]}}]}```
- Double-check to see whether or not the zoglin is holding a sword enchanted with fire aspect.

```/data get entity @e[type=minecraft:zoglin,limit=1,sort=nearest] HandItems```
- Summon a pig nearby so that the zoglin will attack it.

- As the zoglin attacks the pig, take note as to whether or not the pig is ignited.

Observed Behavior:
Several entities that have melee attacks can't use the fire aspect enchantment.
Expected Behavior:
Several entities that have melee attacks would be able to use the fire aspect enchantment.

### Comment 6: Avoma (2022-05-23T01:59:42.687-0700)

Can confirm in 1.18.2 and 1.19 Pre-release 1.

### Comment 7: Avoma (2022-09-01T07:32:33.335-0700)

Can confirm in 1.19.2.

### Comment 8: ouroya (2022-10-29T22:20:24.037-0700)

can confirm in 22w43a
