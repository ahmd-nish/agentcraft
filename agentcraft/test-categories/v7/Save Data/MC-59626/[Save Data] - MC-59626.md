# MC-59626: Arrows lose their Punch enchantment property when unloaded

**Mojira URL:** [https://bugs.mojang.com/browse/MC-59626](https://bugs.mojang.com/browse/MC-59626)

## Report details

- **Mojira categories:** Entities; Save Data
- **Project:** MC
- **Issue key:** MC-59626
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2014-06-29T13:03:28.999-0700
- **Updated:** 2025-04-29T09:44:04.950-0700
- **Resolution date:** 2024-04-30T01:48:04.315-0700
- **Affects versions:** Minecraft 14w26c; Minecraft 1.7.10; Minecraft 14w28a; Minecraft 14w29b; Minecraft 14w32d; Minecraft 1.8.1; Minecraft 1.8.2-pre1; Minecraft 16w36a; Minecraft 16w40a; Minecraft 1.11.2; Minecraft 1.12.2; Minecraft 18w08a; Minecraft 1.13.1; 1.15.2; 20w22a; 1.16.3; 1.16.4; 20w51a; 1.19.3; 1.20.2
- **Fix versions:** 24w18a
- **Area:** Platform
- **Labels:** arrow; enchantment; punch; unload
- **Watchers:** 1
- **Attachments:** 0
- **Issue links:** Relates:inward:MC-270540:The prevention of fall damage from wind charges is not retained upon reloading the world | Relates:outward:MC-50319:Player owned projectiles lose their player ownership when exiting portals | Relates:inward:MC-254131:The wet state of wolves isn't saved to NBT | Relates:inward:MC-107138:Shot arrow loses its critical state after reloading

## Description

Arrows that were shot by a bow that is enchanted with a punch enchantment do not remember their punch property when being unloaded (for example by logging out).
How to reproduce:
1. Get yourself a Punch II Bow and some arrows

```
/give @s minecraft:bow{Enchantments:[{id:"minecraft:punch",lvl:2s}]}
/give @s minecraft:arrow 64
```
2. Place two dirt blocks beside each other in the air so that there are four blocks space between the floor and the blocks.
3. Go into survival mode if you aren't already
4. Shoot an arrow with the Punch II into the underside of each block.
5. Stand below the first block and mine it so that the arrow falls and hits you.
6. You will be thrown away quite a bit.
7. Log out.
8. Log back in and wait a few seconds because the player is invulnerable for a few seconds after login.
9. Stand below the second block and mine it so that the arrow falls and hits you.
10. When the arrow hits you, you will be knocked back only a little (as much as a normal Arrow does).
This behavior is expected since there is no NBT-Tag implemented in which the punch property is saved in.

## Comments (9)

### Comment 1: migrated (2014-06-30T08:39:05.094-0700)

— Get yourself a Power II Bow
A punch II bow, but the enchantment ID is right. (49=punch)

### Comment 2: migrated (2014-07-01T12:10:17.129-0700)

Thanks, I fixed it

### Comment 3: marcono1234 (2014-07-20T04:31:24.599-0700)

Confirmed for 14w29b
To see it a little bit better you can also set it to level 20

```/give @p minecraft:bow 1 0 {ench:[{id:49s,lvl:20s}]}```

### Comment 4: marcono1234 (2016-09-19T15:35:39.237-0700)

Confirmed for
- 16w36a

### Comment 5: migrated (2018-08-26T02:59:20.911-0700)

I tried to reproduce this for 1.13.1 but seems like in the log in you have invulnerability time so the arrow won't hit you.

### Comment 6: j_p_smith (2020-05-29T11:09:55.552-0700)

Confirmed in 1.15.2 and 20w22a.

### Comment 7: migrated (2020-09-27T09:16:02.505-0700)

Confirmed in 1.16.3.

### Comment 8: migrated (2023-01-11T05:39:49.782-0800)

Can confirm in 1.19.3.

### Comment 9: migrated (2024-03-03T07:27:17.601-0800)

Relates to , , , , ,  and .
