# MC-270539: The blast protection enchantment, when applied to horse armor, no longer diminishes the knockback effect from explosions on horse

**Mojira URL:** [https://bugs.mojang.com/browse/MC-270539](https://bugs.mojang.com/browse/MC-270539)

## Report details

- **Mojira categories:** Commands; Enchantments
- **Project:** MC
- **Issue key:** MC-270539
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2024-04-08T11:08:23.900-0700
- **Updated:** 2025-05-29T09:07:08.538-0700
- **Resolution date:** 2024-05-14T23:54:33.188-0700
- **Affects versions:** 24w14a; 1.20.5 Pre-Release 1
- **Fix versions:** 24w20a
- **Area:** Platform
- **Watchers:** 2
- **Attachments:** 2
- **Attachment filenames:** blast protection 4.mp4; blast protection 7.mp4
- **Issue links:** Relates:outward:MC-259573:Blast Protection does not reduce explosion knockback in creative game mode | Cloners:outward:MC-269779:The blast protection enchantment is ineffective when applied to horse armor

## Description

This problem was introduced in 24w05a due to the change that horse armor is stored in body_armor_item instead of ArmorItems[2].
A clone of MC-269779, previously marked as "Cannot Reproduce" due to invalid reproduction steps being utilized despite a comment outlining the correct reproduction process. This bug report will reiterate the correct steps for reproduction. The Blast Protection enchantment effectively reduces damage but does not mitigate knockback. At each level, the blast protection enchantment decreases knockback by 15%. Consequently, at level 7, it completely prevents knockback from explosions, simplifying the reproduction of the issue. (To obtain an item with blast protection level 7, you can execute the following command:

```
/give @p netherite_helmet[enchantments={levels:{"minecraft:blast_protection":7}}] 1
```
This issue is related to MC-198809, MC-259573, , MC-268934, MC-270301 and .
steps to reproduce
-

```
/summon horse ~ ~ ~ {Tame:1b,body_armor_item:{id:"minecraft:diamond_horse_armor",count:1,components:{"minecraft:enchantments":{levels:{"minecraft:blast_protection":7}}}},SaddleItem:{id:"minecraft:saddle",Count:1b}}
```

-

```
/summon creeper ~ ~ ~ {Fuse:0,ignited:1b}
```

Observed: Despite being equipped with blast protection 7, the horse experienced knockback from the creeper explosion.
Expected: The horse should be immune to knockback from the explosion as a result of the blast protection enchantment at level 7.
If you're hesitant to utilize blast protection beyond level 4 because of , you can alternatively follow these steps:
-

```
/summon horse ~ ~ ~ {Tame:1b,Tags:["BugBlast"],body_armor_item:{id:"minecraft:diamond_horse_armor",count:1},SaddleItem:{id:"minecraft:saddle",Count:1b}}
```

-

```
/summon horse ~ ~ ~ {Tame:1b,Tags:["BugBlast"],body_armor_item:{id:"minecraft:diamond_horse_armor",count:1,components:{"minecraft:enchantments":{levels:{"minecraft:blast_protection":4}}}},SaddleItem:{id:"minecraft:saddle",Count:1b}}
```

-

```
/effect give @e[tag=BugBlast] minecraft:slowness infinite 6 true
```

-

```
/execute at @e[tag=BugBlast] run summon creeper ~ ~ ~ {Fuse:0,ignited:1b}
```

Observed: Both horses experienced identical knockback from the explosion, flying to the same height.
Expected: The horse equipped with blast protection 4 armor should undergo 60% less knockback from the explosion.

## Comments (3)

### Comment 1: migrated (2024-04-08T11:08:23.900-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: Neliz (2024-04-09T00:50:17.585-0700)

I can confirm this in 24w14a.

### Comment 3: [Mod] EVGENSYPERPRO (2024-04-13T15:20:01.830-0700)

This is not an issue in 1.20.4. The command to summon a horse with blast protection 7 in 1.20.4 is

```/summon horse ~ ~ ~ {ArmorItem:{id:"minecraft:diamond_horse_armor",Count:1b,tag:{Enchantments:[{id:"minecraft:blast_protection",lvl:7s}]}},Tame:1b}```
The horse will not take knockback from the explosion.
