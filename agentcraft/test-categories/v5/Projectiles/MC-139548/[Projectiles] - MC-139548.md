# MC-139548: Projectiles are rendered incorrectly if their Motion tag was recently changed

**Mojira URL:** [https://bugs.mojang.com/browse/MC-139548](https://bugs.mojang.com/browse/MC-139548)

## Report details

- **Mojira categories:** Commands; Projectiles
- **Project:** MC
- **Issue key:** MC-139548
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2018-11-17T12:10:23.746-0800
- **Updated:** 2026-04-18T22:15:27.614-0700
- **Resolution date:** 2026-04-18T22:14:56.485-0700
- **Affects versions:** Minecraft 18w45a; Minecraft 18w46a; 1.20.1; 23w33a; 24w14a; 1.21; 1.21.2 Pre-Release 3; 1.21.3
- **Fix versions:** 24w44a
- **Area:** Platform
- **Votes:** 3
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** image-2023-08-30-17-02-02-652.png; Minecraft 1.21.3 - Singleplayer 2024-10-25 22-05-25.mp4
- **Issue links:** Duplicate:inward:MC-273888:Recently Summoned Projectiles have visual Desync when motion is modified | Relates:outward:MC-80142:The acceleration of wither skulls, small/dragon fireballs and wind charges is not synced correctly, leading to stuttering during flight | Duplicate:inward:MC-277599:Wind Charges summoned with motion lag visually | Relates:inward:MC-277549:Arrows summoned with custom motion don't render correctly | Duplicate:inward:MC-265084:Entity position is not visually accurate when Motion NBT tag is changed too early after the entity is summoned | Relates:outward:MC-299627:Entity interpolation for high speed projectiles is wildly inaccurate

## Description

The bug
NOTE: This is not a duplicate of MC-124197 or any bugs listed within.  This is new as of the 1.14 snapshots.  It didn't occur in 1.13.2.
It affects all projectile entities (e.g. arrows, fireballs, potions, enderpearls, snowballs, eggs, etc.) but not other entities such as tnt or mobs.  Every ~20 ticks it updates the position to where it's supposed to be, and if the entity changes state (such as an arrow's inGround tag becoming true) it updates immediately.  It also affects other entities properly even while not being rendered in the correct location.  For the Power[0,1,2] data, the projectile renders with a trajectory that curves towards the negative X, Y, and Z directions but actually travels and impacts as it should.
A video's worth a thousand pictures, so here's a video showing the bug in action

In case you need more details, this is using a convoluted raycasting system I set up.  The projectiles are being fired in the direction of an invisible armorstand summoned 0.1 blocks in front of the player by setting the Motion or Power tags equal to the difference between the coordinates of the armorstand and the player, stored as a scoreboard value, via /data merge.  When I summon them regularly with a /summon command such as /summon minecraft:fireball ~ ~ ~ {direction:[0.0,0.0,0.0],power:[0.123,-0.123,0.246]} they render just fine.  As far as I can tell, it only occurs with /data merge.  I'm not sure if it only affects /data merge with the "from" argument, or all /data merge commands.
How to reproduce
- Enter the following commands into active repeating command blocks:

```
/summon snowball ~ ~1 ~ {Motion:[1.0,1.0,0.0]}
```

```
/execute as @e[type=snowball,tag=!edited] run data merge entity @s {Motion:[0.0,1.0,1.0],Tags:[edited]}
```
→  The newest snowballs appear to travel the wrong direction

## Comments (11)

### Comment 1: migrated (2018-11-17T12:10:23.746-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: tryashtar (2018-11-17T12:16:54.415-0800)

If this is only observed using NBT-modifying commands, the precedent is "Won't Fix/Working as Intended" as per 's comment here: https://bugs.mojang.com/browse/MC-66943?focusedCommentId=188032#comment-188032

### Comment 3: TheRedstoneBlaze (2018-11-17T12:44:45.593-0800)

I would hope that this precedent can be excepted here, because otherwise this means in 1.14 and on it will be impossible to launch a projectile on the player's look vector

### Comment 4: tryashtar (2018-11-17T17:31:56.461-0800)

Please comment if you can reproduce a desync without using NBT commands

### Comment 5: Fantastime (2023-08-30T00:03:28.121-0700)

Is this still an issues in latest releases?

### Comment 6: j_p_smith (2023-08-30T02:10:47.450-0700)

Arrows seem to have been fixed, but snowballs, eggs, etc. are still affected.

### Comment 7: migrated (2023-08-30T04:48:04.534-0700)

Per the duplicate, "dragon fireball, egg, ender pearl, experience bottle, experience orb, eye of ender, falling block, fireball, item, llama spit (which is even stranger), potion, [and] small fireball", note items aren't projectiles.

### Comment 8: clamlol (2024-04-03T12:15:04.253-0700)

Affects 24w14a. Highly related to , and these issues combined are likely the cause of the initial stuttering these projecties experience shortly after creation. Also, this issue can be observed when a wind charge explosion changes the velocity of a nearby projectile.

### Comment 9: migrated (2024-11-02T11:05:20.196-0700)

I can confirm this still exists in version 1.21.3, but NOT in 1.21.1. The projectile after data modification will still follow its intended path and collide with anything along it, but it appears to go straight down. I've tested this with arrows, snowballs, eggs, and tridents, and they all suffer from this bug.

### Comment 10: ampau (2025-07-26T09:21:23.115-0700)

I am unable to reproduce in 1.21.8

### Comment 11: ampau (2025-07-28T02:51:24.124-0700)

Realized my last comment was a bit vague… After investigating a little I’ve determined the fix version to be 24w44a.
