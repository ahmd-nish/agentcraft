# MC-19690: Reducing maxHealth / max_health can cause fake death

**Mojira URL:** [https://bugs.mojang.com/browse/MC-19690](https://bugs.mojang.com/browse/MC-19690)

## Report details

- **Mojira categories:** Player
- **Project:** MC
- **Issue key:** MC-19690
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2013-06-28T19:37:43.902-0700
- **Updated:** 2026-04-11T06:08:59.358-0700
- **Resolution date:** 2022-08-09T05:46:39.401-0700
- **Affects versions:** Minecraft 1.6.1; Minecraft 1.6.2; Minecraft 13w39b; Minecraft 14w20b; Minecraft 1.7.10; Minecraft 14w30c; Minecraft 14w31a; Minecraft 14w33c; Minecraft 14w34a; Minecraft 14w34b; Minecraft 14w34c; Minecraft 14w34d; Minecraft 1.8-pre1; Minecraft 1.8-pre2; Minecraft 1.8; Minecraft 1.8.1; Minecraft 1.8.3; Minecraft 15w44b; Minecraft 15w46a; Minecraft 1.8.9; Minecraft 16w02a; Minecraft 16w03a; Minecraft 16w06a; Minecraft 1.9 Pre-Release 2; Minecraft 1.9 Pre-Release 3; Minecraft 1.9 Pre-Release 4; Minecraft 1.9; Minecraft 1.9.1 Pre-Release 1; Minecraft 1.9.1 Pre-Release 3; Minecraft 1.9.1; Minecraft 1.9.2; Minecraft 16w15b; Minecraft 1.10.2; Minecraft 16w41a; Minecraft 16w42a; Minecraft 16w43a; Minecraft 16w44a; Minecraft 1.11 Pre-Release 1; Minecraft 1.11; Minecraft 16w50a; Minecraft 1.11.1; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 17w13b; Minecraft 17w15a; Minecraft 17w16b; Minecraft 17w17a; Minecraft 17w18b; Minecraft 1.12 Pre-Release 2; Minecraft 1.12; Minecraft 1.12.1; Minecraft 1.12.2; Minecraft 18w05a; Minecraft 18w15a; Minecraft 1.13-pre7; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 1.14.1; 1.14.4; 19w42a; 1.15.2; 20w06a; 20w17a; 20w18a; 20w19a; 20w20b; 20w22a; 1.16 Pre-release 2; 1.16.1; 20w27a; 20w29a; 1.16.2 Pre-release 1; 1.16.2 Pre-release 2; 1.16.2 Pre-release 3; 1.16.2 Release Candidate 1; 1.16.2; 1.16.3; 1.16.4 Release Candidate 1; 1.16.4; 20w51a; 1.16.5; 21w05b; 21w06a; 21w07a; 21w10a; 21w11a; 21w14a; 21w17a
- **Fix versions:** 1.17 Pre-release 1
- **Labels:** animation; attribute; death-screen; interface; max_health
- **Watchers:** 1
- **Attachments:** 14
- **Attachment filenames:** 2013-06-28_20.52.50.png; 2013-06-28_21.29.51.png; 2013-06-28_21.29.52_2.png; 2013-06-28_21.29.52.png; 2013-06-28_21.30.50.png; 2016-04-01_16.05.10.png; 2016-04-01_16.05.21.png; 2016-04-01_16.05.27.png; 2016-04-01_16.05.32.png; 2016-04-01_16.05.34.png; 2016-04-01_16.06.05.png; 2016-04-01_16.07.50.png; 2020-07-11_23.12.16.png; MC-19690.mp4
- **Issue links:** Relates:inward:MC-16345:Reducing the player's base max health using /attribute does not always reduce their current health | Duplicate:inward:MC-222930:Undead player

## Description

It's possible to have higher maximum health than actual health (see ) because the helth doesn't adequately update server-side when an attribute stops being applied.
In this state, when the player takes more damage than its max health, the client will show the death screen. However, since the maximum health has not actually been updated yet on the server side, the player doesn't die server-side. When the player then clicks "Respawn", the game continues as if the player hadn't died.
This is a client-server desync where on the client-side, the player dies, but server-side, it doesn't.
To reproduce
- Place a wither rose

- Switch into survival mode

- Give yourself this item:

```
/give @p dirt{AttributeModifiers:[{AttributeName:"generic.max_health",Name:"generic.max_health",Amount:20d,Operation:0,UUID:[I;0,1,2,3],Slot:"mainhand"}]}
```

- Select the dirt block

- Run this command to fill your health:

```
/effect give @p minecraft:instant_health 1 3
```

- Deselect the dirt block

- Walk into the wither rose
→  You die immediately (because the server sends to the client "decrease health by 20 because max health changed")
→  On the death screen, you continue to take damage

- Click "Respawn"
→  You don't respawn, but are still at the same location as if nothing happened

These actions can also cause this bug from being triggered, apart from being damaged by a wither rose:
- Instant health effect

- Instant damage effect

- Poison effect

- Suffocation

- Drowning

- Starvation (Hunger)

- Hitting a wall with elytra

## Comments (51)

### Comment 1: migrated (2013-06-28T19:37:43.902-0700)

This comment contained multiple image attachments (14), please login to view the attachments.

### Comment 2: migrated (2013-06-29T08:16:27.007-0700)

Seems like a combination of MC-18027 and the issue where getting healed at the same time as you die causes you to turn sideways (which I can't seem to find).

### Comment 3: migrated (2013-08-24T05:14:56.552-0700)

It's still happening in Minecraft 1.6.2. Check MC-29319 for simpler repro steps.

### Comment 4: marcono1234 (2014-07-29T07:15:17.670-0700)

Confirmed for
- 14w30c

- 14w31a

- Minecraft 1.8-pre 1

Form MC-33827:
- Give yourself an item with the max health attribute

```/give @p dirt 1 0 {AttributeModifiers:[0:{AttributeName:"generic.attackDamage",Name:"generic.attackDamage",Amount:10000,Operation:0,UUIDLeast:894654,UUIDMost:2872},1:{AttributeName:"generic.movementSpeed",Name:"generic.movementSpeed",Amount:2.5,Operation:1,UUIDLeast:111113,UUIDMost:1111},2:{AttributeName:"generic.maxHealth",Name:"generic.maxHealth",Amount:40,Operation:0,UUIDLeast:111113,UUIDMost:1111}],display:{Name:"GodSword 2.1",Lore:["The Ultimate Power","By Vengeur69"]}}```

- Give yourself constantly the instant health effect by a clock or just use this command:

```/effect @p instant_health 300000 5```

- Get hurt (this doesn't always work on the first try, the best way is to use this command; seems not to be necessary)

```/effect @p instant_damage 300000 1```

- And now select and deselect the item with the max healt attribute very often

I know some of the steps here use other bugs, but this also works without using these bugs

### Comment 5: migrated (2014-12-05T20:30:18.259-0800)

I am able to reproduce this, while healing with Regeneration, as I took damage, it showed I died, but my health is still full. And my health is still Regenerating. Once I hit the respawn button, I went all sideways (half dying animation). I'm playing on 1.8.1

### Comment 6: migrated (2015-03-07T19:42:59.695-0800)

The more you do it, the lower the player gets

### Comment 7: migrated (2015-03-07T19:45:54.150-0800)

Also it is only visible to you, not anybody else

### Comment 8: marcono1234 (2015-11-13T09:30:47.521-0800)

Confirmed for
- 15w46a

Please include a way to reproduce:
- Give yourself an item with the max health attribute

```/give @p dirt 1 0 {AttributeModifiers:[{AttributeName:"generic.maxHealth",Name:"generic.maxHealth",Amount:40d,Operation:0,UUIDLeast:111113,UUIDMost:1111,Slot:"mainhand"}]}```

- Give yourself constantly the instant health effect by a clock or just use this command:

```/effect @p instant_health 300000 5```

- Get hurt (this doesn't always work on the first try, the best way is to use this command; seems not to be necessary)

```/effect @p instant_damage 300000 1```

- And now select and deselect the item with the max healt attribute very often

### Comment 9: migrated (2016-01-21T12:49:35.321-0800)

It's still working in 16w03a.

### Comment 10: SunCat (2016-02-11T00:59:14.361-0800)

Still in 16w06a

### Comment 11: migrated (2016-02-22T10:48:12.205-0800)

Still in 1.9 pre-realase 2.

### Comment 12: SunCat (2016-02-24T10:15:10.532-0800)

Still in 1.9-pre3

### Comment 13: SunCat (2016-02-27T03:17:31.377-0800)

Still in 1.9-pre4

### Comment 14: migrated (2016-03-01T13:41:25.713-0800)

Still in release 1.9

### Comment 15: SunCat (2016-03-09T11:35:20.612-0800)

Still in 1.9.1-pre1

### Comment 16: SunCat (2016-03-12T10:29:56.795-0800)

Still in 1.9.1-pre3

### Comment 17: migrated (2016-04-01T13:04:36.055-0700)

Can confirm for 1.9.1 & 1.9.2, you can tell it is a fake death, because it does not show up on statistics.

### Comment 18: SunCat (2016-04-14T12:47:07.338-0700)

Still in 16w15b

### Comment 19: migrated (2016-06-30T23:28:16.702-0700)

Having a health value above your maxHealth attribute and then taking certain types of damage cause the false death.
fire, poison, suffocation, and drowning cause false death.
melee, fall, momentum damage do not cause false death

### Comment 20: migrated (2016-10-16T13:58:52.720-0700)

confirmed for 16w41a

### Comment 21: SunCat (2016-10-16T14:20:45.789-0700)

, 16w41a is already marked as affected

### Comment 22: [Mod] bemoty (2017-08-12T06:27:09.755-0700)

Can confirm for MC 1.12.1.

### Comment 23: migrated (2018-02-02T16:06:52.331-0800)

@colton Jelsema, More specifically, If health is greater than or equal to 2*maxhealth, the fake death occurs upon updating your health. This is likely do to the game causing damage to the player equal to (health-maxhealth) (when maxhealth<health) upon a health update occurring, and with the condition I gave above, the game would consider this damage to be a fatal hit to a player (health=2*maxhealth, damage=2*maxhealth-maxhealth=maxhealth), thus triggering the death screen. However, since the player's health (now equal to maxhealth) is still greater than 0, no death actually occurs.

### Comment 24: migrated (2019-05-15T05:29:43.752-0700)

confirmed for MC 1.14.1

### Comment 25: Doc (2019-06-09T20:55:27.836-0700)

confirmed for MC 1.14.2

### Comment 26: migrated (2019-07-25T21:27:20.549-0700)

confirmed for MC 1.14.3

### Comment 27: migrated (2019-07-25T21:30:56.173-0700)

confirmed for MC 1.14.4

### Comment 28: migrated (2020-01-22T02:40:08.021-0800)

Confirmed for MC 1.15 and MC 1.15.2

### Comment 29: migrated (2020-05-22T21:20:39.412-0700)

This issue could easily be resolved by updating the players maxHealth value to match the attribute when it is modified
Really hard to believe this is still an issue after all of these years
So many closed duplicates...

### Comment 30: migrated (2020-05-30T10:19:38.480-0700)

It's really too bad that this is marked low priority. This would be a simple fix, and causes a big headache to many map makers. With the addition of the new /attribute command introduced in 20w17a, this could be a great opportunity to finally take care of this bug.

### Comment 31: pulpetti (2020-07-06T11:25:28.820-0700)

Affects  1.16.1

### Comment 32: pulpetti (2020-07-06T11:25:36.913-0700)

Affects 20w27a

### Comment 33: migrated (2020-07-08T21:06:02.443-0700)

for any one heaving problems with this bug
if you want to control player heath
heath boost is a good work around
it will display to hafe heart and dosent glitch
effect give @s minecraft:health_boost 1 3 true
attribute @s[scores={health=1}] minecraft:generic.max_health base set 1
X20

effect clear @s minecraft:health_boost
attribute @s minecraft:generic.max_health base set 20

### Comment 34: migrated (2020-07-11T19:24:51.395-0700)

i was messing with this bug and i noticed something: the more times you repeat the glitch the more inclined the player gets, so i thought, can i get the player to be upside down?, well, unfortunately, no, you can't, however i managed to get the player stuck in a infinite respawn screen, if immediateRespawn is active you can interact with the world, but you cannot move. As usual, relogging fixes the infinite respawn screen.

### Comment 35: pulpetti (2020-07-17T05:49:32.832-0700)

Can confirm for 20w29a.

### Comment 36: pulpetti (2020-08-05T06:43:35.273-0700)

In 1.16.2 Pre-1

### Comment 37: migrated (2020-08-14T05:48:41.415-0700)

Confirmed on 1.16.2.

### Comment 38: SunCat (2020-08-14T08:09:43.394-0700)

already added to the affected versions

### Comment 39: migrated (2020-09-01T14:38:11.392-0700)

How to fix
look at attribute command
attribute @s generic.max_health modifier add 22e67162-454c-4125-9ff5-cb71365a41a8 "mat.damage" -15 add
effect give @s instant_health
will not do fake death.
If my max health is below 20 when i take damage higher than my health it will create "fake death"
For example
5 max hp.
20 hp (hp not reduced to max, because i don't get any heal or damage)
effect give @s intant_healt - take 15 damage to reduce my health to maximum.
How to fix - always reduce health to maximum

### Comment 40: migrated (2020-09-01T14:48:24.092-0700)

bug -
if hp>maxHp
then "damage on client side"="real damage"+hp-maxHp
else "damage on client side"="real damage"
fix -
if hp>maxHp then hp=maxHp

### Comment 41: migrated (2020-11-03T06:33:46.483-0800)

If you do /attribute @s minecraft:generic.max_health base set 1 and take any damage, I think the client(or the server, I don't know so much about this) will think that you are half a heart, but the server(or the client) will think will are 1 heart, causing this bug to happen.

### Comment 42: migrated (2020-12-07T11:54:21.555-0800)

I can get this to work by just

```/attribute @p minecraft:generic.max_health base set 10```
which should set my max health to 5 hearts

```/data get entity @p Health```
shows I have 20 health
now, I set up a dispenser with arrows hooked up to a pressure plate, should be 3 damage
It does the fake death, click respawn, everything back to normal, 5 hearts
this is on 1.16.4

edit this doesn't trigger when zombies attack and it seems like health is correctly 10

### Comment 43: Avoma (2021-01-15T05:44:28.808-0800)

Can confirm in 20w51a.

### Comment 44: Avoma (2021-02-06T03:47:56.877-0800)

Can confirm in 21w05b.

### Comment 45: Avoma (2021-02-12T05:25:59.533-0800)

Can confirm in 21w06a.

### Comment 46: Avoma (2021-02-18T11:16:43.457-0800)

Can confirm in 21w07a. Video attached.

### Comment 47: mtmjnb (2021-03-20T03:16:26.632-0700)

Can confirm in 21w11a
but if modifying health with the /attribute command you have to specify your name (@s doesnt work)

### Comment 48: Avoma (2021-04-30T06:27:31.752-0700)

Can confirm in 21w17a.

### Comment 49: migrated (2021-05-22T05:51:24.298-0700)

I see this is "In Progress". Perhaps fix it and make it also a feature somehow?

### Comment 50: migrated (2021-05-27T08:31:08.078-0700)

Fixed!

### Comment 51: Jianyou Zheng (2026-04-11T06:08:59.358-0700)

You cannot respawn while you install “Physics Mod”
