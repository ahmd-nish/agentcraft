# MC-16345: Reducing the player's base max health using /attribute does not always reduce their current health

**Mojira URL:** [https://bugs.mojang.com/browse/MC-16345](https://bugs.mojang.com/browse/MC-16345)

## Report details

- **Mojira categories:** Data Packs
- **Project:** MC
- **Issue key:** MC-16345
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2013-05-23T22:57:58.553-0700
- **Updated:** 2025-04-29T09:33:14.127-0700
- **Resolution date:** 2024-05-07T04:40:20.270-0700
- **Affects versions:** Snapshot 13w21a; Minecraft 1.6.1; Minecraft 1.6.2; Minecraft 1.7.4; Minecraft 14w02c; Minecraft 14w03a; Minecraft 14w03b; Minecraft 1.7.10; Minecraft 14w30c; Minecraft 14w31a; Minecraft 14w33c; Minecraft 14w34a; Minecraft 14w34b; Minecraft 14w34c; Minecraft 14w34d; Minecraft 1.8-pre1; Minecraft 1.8.2-pre4; Minecraft 1.8.8; Minecraft 15w37a; Minecraft 1.10.2; Minecraft 16w41a; Minecraft 16w43a; Minecraft 16w44a; Minecraft 1.11 Pre-Release 1; Minecraft 1.11; Minecraft 16w50a; Minecraft 1.11.1; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 17w13b; Minecraft 17w15a; Minecraft 17w16b; Minecraft 17w17a; Minecraft 17w18b; Minecraft 1.12 Pre-Release 2; Minecraft 1.12.2; Minecraft 18w15a; Minecraft 1.13.1; Minecraft 1.14.2; 1.14.4; 19w45b; 1.15.2; 20w17a; 20w18a; 20w19a; 20w20b; 20w21a; 1.16 Pre-release 1; 1.16 Pre-release 2; 1.16 Release Candidate 1; 1.16; 1.16.1; 1.16.2 Pre-release 1; 1.16.2 Pre-release 2; 1.16.2 Release Candidate 1; 1.16.2; 1.16.4; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w07a; 21w11a; 21w14a; 21w15a; 21w16a; 21w17a; 1.17 Pre-release 1; 1.17; 1.17.1; 21w39a; 21w43a; 1.18; 1.18.1; 1.18.2; 22w18a; 1.19; 1.19.2; 1.19.3 Release Candidate 3; 1.19.3; 23w03a; 1.19.4; 23w18a; 1.20.1; 23w31a; 23w32a; 23w35a; 1.20.2 Pre-release 1; 23w44a; 24w04a; 1.20.5; 1.20.6
- **Fix versions:** 24w19a
- **Area:** Platform
- **Game mode:** Survival
- **Labels:** attribute; health; max_health
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** health.png; MC-16345.mp4; MC-16345.png
- **Issue links:** Relates:outward:MC-19690:Reducing maxHealth / max_health can cause fake death | Duplicate:inward:MC-18965:Switching from or to items that change maxhealth do not update health until damage is taken | Duplicate:inward:MC-19688:Max Health Attribute Does Not Automaticly Update | Duplicate:inward:MC-28127:Health doesnt update with negative maxhealth | Duplicate:inward:MC-55117:Scoreboard health/ atributted skull bug | Duplicate:inward:MC-67856:.maxHealth doesn't reset health | Duplicate:inward:MC-81307:Health Boost from AttributeName:generic.maxHealth having wrong amount. | Duplicate:inward:MC-154228:Ghost Health is created when having negative maxHealth attributes | Duplicate:inward:MC-171047:Player max health float values won't decrease from generic.maxHealth on items | Duplicate:inward:MC-179852:Player health doesn't sync properly with /attribute minecraft:generic.max_health | Duplicate:inward:MC-179962:Health does not update when minecraft:generic.max_health is set to 1 | Duplicate:inward:MC-180001:Reducing max health using /attribute does not reduce current health | Duplicate:inward:MC-183423:max_health attribute sets value but doesn't update health | Duplicate:inward:MC-184215:generic.max_health affecting fall damage | Duplicate:inward:MC-187386:Changing generic.max_health doesn't change current health | Duplicate:inward:MC-188160:Setting max health to the player having half a heart would always get rounded to the next full heart | Duplicate:inward:MC-190590:Attribute command can't set current health to half a heart which leads to other issues | Duplicate:inward:MC-196591:Abnormal behavior related to the generic.max_health attribute | Duplicate:inward:MC-199741:/attribute hearts don't visually update until relog | Duplicate:inward:MC-212696:Health does not actually update when holding an item with the max health attribute. | Duplicate:inward:MC-226495:Life is not well displayed when your max life is an odd number | Duplicate:inward:MC-233301:Attributes and Command Block Bug | Duplicate:inward:MC-233859:Attribute "generic.maxHealth" doesn't subtract health values from players properly | Duplicate:inward:MC-237985:Custom Max Health Armor and /attribute | Duplicate:inward:MC-237991:attribute health doesnt work unless you take damage | Duplicate:inward:MC-240209:max hp remove bug | Duplicate:inward:MC-258616:The "/attribute @p minecraft:generic.max_health base set x" command not working properly for lower values of x.. | Duplicate:inward:MC-264644:If a players generic.max_health is set to a base of 1 every game tick, the game doesn't set the players health data to 1.0 when the player respawns | Duplicate:inward:MC-265367:"attribute max_health" command malfunctioning at low values | Relates:inward:MC-64311:Attribute (Bug?)

## Description

The bug
When the player's base max health is reduced using /attribute, their current health (stored on the server) is not always reduced accordingly. (There have been reports in the past that this bug occurs whenever the player's total max health is reduced, including using attribute modifiers, but as of the 1.20.2 snapshots I can only reproduce this by modifying the base value using /attribute.)
Reproduction
Setup
This bug occurs inconsistently and can be hard to detect when it occurs unless you're paying close attention, so it's preferable to have a dedicated testing setup. Let's start with a few of commands:

```
/gamerule doImmediateRespawn true
/gamerule keepInventory true
/gamerule naturalRegeneration false
/spawnpoint @s ~ ~ ~
```
Now let's make our current health value visible in the sidebar:

```
/scoreboard objectives add health health
/scoreboard objectives setdisplay sidebar health
/kill @s
```
And, for extra visibility, let's make particles emanate from ourselves when our current health exceeds our max health. First we run the following:

```
/scoreboard objectives add temp dummy
```
Then we put the following in a powered repeating command block:

```
execute as @p store result score @s temp run attribute @s minecraft:generic.max_health get 1.0
```
And the following in an unconditional, always-active chain command block pointing away from the repeating one:

```
execute as @p at @s if score @s health > @s temp run particle minecraft:glow ~ ~ ~ 0.2 0 0.2 0.2 10
```
Now let's set up some impulse command blocks which can cause the bug to occur. Place a button on each one, and make sure they aren't adjacent to each other.

```
attribute @p minecraft:generic.max_health base set 1
attribute @p minecraft:generic.max_health base set 20
attribute @p minecraft:generic.max_health base set 30
```
Finally, we need a command block to heal ourselves to full in case we've failed to repro and want to try again. Place a button on this one too.

```
effect give @p minecraft:instant_health 1 20 true
```
Reproducing the bug
Go into survival mode. Using the command blocks you just set up, set your base max health to 30 and heal yourself to full. Try reducing your max health, first to 20, then to 1. If you get particles and notice that the health value in the sidebar exceeds the hearts on your screen, the bug has occurred! If not, start over from the beginning of this paragraph.
Once you've repro'd successfully, set your max health to 30 again. As the particles cease, note how while you do regain some black hearts, the amount of red hearts remains unchanged. I assume this is because the client is sent an "update max health" packet but the server sees no need to send an "update current health" packet since it did not know the client was out of sync.
Being hurt or healed while the bug is occurring will fix it.
Remarks
NBT state has no effect
Due to , the player's NBT does not accurately reflect the state of their attributes. This does not seem to affect whether or not the bug occurs at a particular point in time, but if desired, you can run /kill @s to trigger that issue and , removing the max health attribute from your NBT and starting over again with 20 health.
Attribute modifiers have no effect (anymore)
Some past reports indicate that it was possible to get the player's current health to be higher than their max health using attribute modifiers. I tried to reproduce this by playing around with the following items during the tests mentioned above, but ultimately I did not encounter any inexplicable behavior.

```
/give @s stick{AttributeModifiers:[{AttributeName:"minecraft:generic.max_health",Name:"health-",Slot:"mainhand",Amount:-10,Operation:0,UUID:[I;0,1111,0,111111]}],display:{Name:'"Health Reduction"'}}
/give @s blaze_rod{AttributeModifiers:[{AttributeName:"minecraft:generic.max_health",Name:"health+",Slot:"mainhand",Amount:10,Operation:0,UUID:[I;0,1111,0,111112]}],display:{Name:'"Health Boost"'}}
/give @s golden_helmet{AttributeModifiers:[{AttributeName:"minecraft:generic.max_health",Name:"health++",Slot:"head",Amount:20,Operation:0,UUID:[I;0,1111,0,111113]}],display:{Name:'"Mega Health Boost"'}}
```

## Comments (28)

### Comment 1: migrated (2013-05-23T22:57:58.553-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: migrated (2013-05-27T05:46:04.790-0700)

Note, that once you delesected the item and fall back under 20 Health, it will stop increasing your health at 20.

### Comment 3: Ezekiel (2014-07-26T12:12:32.443-0700)

Is this still a concern in the latest Minecraft version 14w30c? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 4: marcono1234 (2014-07-29T07:25:31.340-0700)

Relates to: MC-19690
Confirmed for
- 14w30c

- 14w31a

- Minecraft 1.8-pre 1
How to reproduce:

- Perform this command

```/scoreboard objectives add Health health```

- Then this

```/scoreboard objectives setdisplay sidebar Health```

- Give yourself an item with the max healt attribute and select it

```/give @p dirt 1 0 {AttributeModifiers:[0:{AttributeName:"generic.attackDamage",Name:"generic.attackDamage",Amount:10000,Operation:0,UUIDLeast:894654,UUIDMost:2872},1:{AttributeName:"generic.movementSpeed",Name:"generic.movementSpeed",Amount:2.5,Operation:1,UUIDLeast:111113,UUIDMost:1111},2:{AttributeName:"generic.maxHealth",Name:"generic.maxHealth",Amount:40,Operation:0,UUIDLeast:111113,UUIDMost:1111}],display:{Name:"GodSword 2.1",Lore:["The Ultimate Power","By Vengeur69"]}}```

- Your Health score should now be 60, now deselect it

Your Health score is still 60, the game changes this back to 20 as soon as you get damage, but does NOT reduce your health lower than 20 because of the damage
I know some people could say that this is a bug with the scoreboard, but it is not, you can proof this with programmes like the "NBT-Explorer" this shows you the same like the scoreboard does

### Comment 5: migrated (2015-01-26T14:59:02.185-0800)

Confirmed for 1.8.2 pre-4. Also occurs when using an item that lowers your max health.

### Comment 6: marcono1234 (2015-09-12T05:52:01.283-0700)

Confirmed for
- 15w37a

### Comment 7: j_p_smith (2020-05-27T14:08:49.451-0700)

Confirmed in 1.15.2 and 20w21a.

### Comment 8: pulpetti (2020-08-05T06:51:04.632-0700)

In 1.16.1

### Comment 9: Avoma (2021-01-14T05:17:21.645-0800)

Can confirm that this issue is still present in 20w51a. Here are the updated reproduction steps, as the steps provided by @Marcono1234 no longer work.
Steps to Reproduce:
- Create a health scoreboard.

```/scoreboard objectives add Health health```
- Set the scoreboard to display on the sidebar.

```/scoreboard objectives setdisplay sidebar Health```
- Switch to survival mode.

```/gamemode survival @s```
- Give yourself an item with the max health attribute and select it.

```/give @p dirt{AttributeModifiers:[{AttributeName:"minecraft:generic.attack_damage",Name:"AttackDamage",Amount:10000,Operation:0,UUID:[I;0,2872,0,894654]},{AttributeName:"minecraft:generic.movement_speed",Name:"MovementSpeed",Amount:2.5,Operation:1,UUID:[I;0,1111,0,111113]},{AttributeName:"minecraft:generic.max_health",Name:"MaxHealth",Amount:40,Operation:0,UUID:[I;0,1111,0,111112]}],display:{Name:'{"text":"GodSword 2.1"}',Lore:['{"text":"The Ultimate Power"}','{"text":"By Vengeur69"}']}}```
- Give yourself regeneration so that the scoreboard updates and your health is set to 60.

```/effect give @p minecraft:regeneration 4 255```
- Deselect the item.
→  Notice how your Health score is still 60. The game will change this back to 20 as soon as you get damaged, but does NOT reduce your health lower than 20 because of the damage.

Thanks to @Dhranios for the assistance with the reproduction steps.

### Comment 10: marcono1234 (2021-01-14T15:22:43.144-0800)

Thanks, I have included the reproduction steps (slightly modified) in the description now and have rewritten the description.

### Comment 11: Avoma (2021-01-28T06:36:38.284-0800)

Can confirm in 21w03a.

### Comment 12: Avoma (2021-02-05T11:39:09.634-0800)

Can confirm in 21w05b.

### Comment 13: Avoma (2021-02-12T05:22:12.412-0800)

Can confirm in 21w06a.

### Comment 14: Avoma (2021-02-18T11:12:45.877-0800)

Can confirm in 21w07a. Video attached.

### Comment 15: Avoma (2021-03-27T03:34:13.406-0700)

Can confirm in 21w11a.

### Comment 16: Avoma (2021-04-11T03:54:23.331-0700)

Can confirm in 21w14a.

### Comment 17: Avoma (2021-04-19T02:33:34.745-0700)

Can confirm in 21w15a.

### Comment 18: Avoma (2021-04-22T02:19:21.523-0700)

Can confirm in 21w16a.

### Comment 19: Avoma (2021-04-30T06:25:29.239-0700)

Can confirm in 21w17a.

### Comment 20: Avoma (2021-06-16T12:08:40.712-0700)

Can confirm in 1.17.

### Comment 21: Avoma (2021-08-24T05:12:22.991-0700)

Can confirm in 1.17.1.

### Comment 22: ampolive (2021-10-28T15:49:23.162-0700)

Can confirm in 21w43a.

### Comment 23: Avoma (2021-12-08T05:00:47.129-0800)

Can confirm in 1.18.

### Comment 24: Avoma (2021-12-14T09:03:28.350-0800)

Can confirm in 1.18.1.

### Comment 25: Avoma (2022-05-10T09:48:52.548-0700)

Can confirm in 1.18.2 and 22w18a.

### Comment 26: Avoma (2022-06-13T03:25:44.369-0700)

Can confirm in 1.19.

### Comment 27: migrated (2022-08-05T11:34:54.984-0700)

Can confirm in 1.19.2

### Comment 28: clamlol (2023-08-05T20:16:26.701-0700)

As of 23w31a this bug seems to only happen when modifying the base health to a value less than 20 with /attribute, and even then somewhat infrequently. I've performed the same steps over and over and cannot discern any pattern behind the occurences.
Additionally, it seems that when this bug does occur and the attribute command is run again to  reset the player's max health to 20, the heart meter will remain stuck at the lower value until the next time the player takes damage; any healing effects will not be reflected, probably because the server sees no reason to send such a packet to the client when the health is already full.
