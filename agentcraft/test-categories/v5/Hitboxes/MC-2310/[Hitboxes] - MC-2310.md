# MC-2310: Wrong attack radius calculation damages/kills entities through blocks and corners

**Mojira URL:** [https://bugs.mojang.com/browse/MC-2310](https://bugs.mojang.com/browse/MC-2310)

## Report details

- **Mojira categories:** Entities; Hitboxes
- **Project:** MC
- **Issue key:** MC-2310
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2012-11-05T01:19:57.616-0800
- **Updated:** 2025-04-29T12:17:07.494-0700
- **Resolution date:** 2023-09-22T06:57:32.811-0700
- **Affects versions:** Minecraft 1.4.3; Snapshot 13w05b; Minecraft 1.5.1; Minecraft 1.5.2; Minecraft 1.6.1; Minecraft 1.6.2; Minecraft 1.7.2; Minecraft 1.7.5; Minecraft 14w11b; Minecraft 1.7.6-pre1; Minecraft 1.7.6-pre2; Minecraft 14w18b; Minecraft 1.8-pre1; Minecraft 1.8-pre2; Minecraft 1.8; Minecraft 1.8.1; Minecraft 1.8.3; Minecraft 1.8.8; Minecraft 15w33b; Minecraft 15w33c; Minecraft 15w47c; Minecraft 15w49a; Minecraft 1.8.9; Minecraft 15w50a; Minecraft 16w02a; Minecraft 16w05b; Minecraft 16w06a; Minecraft 1.9 Pre-Release 2; Minecraft 1.9 Pre-Release 3; Minecraft 1.9 Pre-Release 4; Minecraft 1.9; Minecraft 1.9.1 Pre-Release 1; Minecraft 1.9.1 Pre-Release 3; Minecraft 1.9.2; Minecraft 1.9.4; Minecraft 1.10; Minecraft 1.10.2; Minecraft 16w32a; Minecraft 16w32b; Minecraft 16w33a; Minecraft 16w35a; Minecraft 16w40a; Minecraft 16w41a; Minecraft 16w44a; Minecraft 1.11 Pre-Release 1; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 1.12 Pre-Release 2; Minecraft 1.12 Pre-Release 6; Minecraft 1.12; Minecraft 1.12.1; Minecraft 1.12.2; Minecraft 18w03b; Minecraft 18w07c; Minecraft 18w21b; Minecraft 1.13-pre3; Minecraft 1.13; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w43c; Minecraft 18w47b; Minecraft 18w50a; Minecraft 19w04b; Minecraft 19w05a; Minecraft 19w11b; Minecraft 19w12b; Minecraft 19w13a; Minecraft 19w14a; Minecraft 1.14 Pre-Release 1; Minecraft 1.14 Pre-Release 2; Minecraft 1.14 Pre-Release 4; Minecraft 1.14 Pre-Release 5; Minecraft 1.14; Minecraft 1.14.1; Minecraft 1.14.2 Pre-Release 1; Minecraft 1.14.2 Pre-Release 2; Minecraft 1.14.2; Minecraft 1.14.3; Minecraft 1.14.4 Pre-Release 1; Minecraft 1.14.4 Pre-Release 3; Minecraft 1.14.4 Pre-Release 4; Minecraft 1.14.4 Pre-Release 5; Minecraft 1.14.4 Pre-Release 6; 1.14.4; 19w34a; 19w35a; 19w36a; 19w37a; 19w38b; 19w39a; 19w40a; 19w41a; 19w42a; 19w45b; 19w46b; 1.15 Pre-release 1; 1.15 Pre-Release 2; 1.15 Pre-release 3; 1.15 Pre-release 4; 1.15 Pre-release 5; 1.15 Pre-release 6; 1.15 Pre-release 7; 1.15; 1.15.1; 1.15.1 Pre-release 1; 1.15.2 Pre-Release 1; 1.15.2 Pre-release 2; 1.15.2; 20w06a; 20w07a; 20w08a; 20w09a; 20w10a; 20w11a; 20w13a; 20w13b; 20w15a; 20w17a; 20w18a; 20w19a; 20w20a; 20w20b; 20w21a; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 6; 1.16 Pre-release 7; 1.16 Pre-release 8; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Pre-release 2; 1.16.2 Pre-release 3; 1.16.2 Release Candidate 1; 1.16.2 Release Candidate 2; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4 Pre-release 1; 1.16.4 Pre-release 2; 1.16.4 Release Candidate 1; 1.16.4; 20w45a; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w08b; 21w10a; 21w11a; 21w13a; 21w14a; 21w20a; 1.17 Pre-release 2; 1.17 Release Candidate 1; 1.17; 1.17.1; 21w39a; 21w40a; 1.18 Pre-release 1; 1.18 Pre-release 5; 1.18; 1.18.1 Pre-release 1; 1.18.1; 22w05a; 22w06a; 1.18.2; 22w12a; 22w14a; 22w17a; 1.19; 1.19.1 Release Candidate 1; 1.19.1 Pre-release 5; 1.19.2; 1.19.3; 1.19.4; 23w13a; 1.20.1; 23w32a
- **Fix versions:** 23w33a
- **Area:** Platform
- **Labels:** attack; damage; kill
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** 2016-05-28_21.13.28.png; after.png; attack_through_a_wall.gif; before.png; ravager-headbutt-through-door.gif; ravager-range-bug-slowmo.gif
- **Issue links:** Relates:inward:MC-116644:Filled water or powder snow cauldron extinguishes burning arrows that hit either side of the cauldron | Duplicate:inward:MC-167398:make the fence a complete block | Duplicate:inward:MC-245806:Wither skeleton can hit the player through walls | Duplicate:inward:MC-15127:Zombies can Hit NPCs Through Doors. | Duplicate:inward:MC-18326:Hit by mob through solid wall | Duplicate:inward:MC-20142:Zombies hit me through doors | Duplicate:inward:MC-23919:Baby Zombies can attack through doors. | Duplicate:inward:MC-24069:zombie glitch | Duplicate:inward:MC-29270:Zombies can damage the player when breaking doors | Duplicate:inward:MC-29292:Zombies can damage villagers through doors. | Duplicate:inward:MC-40354:Door & Zombie bug | Duplicate:inward:MC-40987:Zombies attack through doors | Duplicate:inward:MC-50668:Mobs' Hitbox disregards Blocks | Duplicate:inward:MC-63435:Zombies can attack villagers trough doors | Duplicate:inward:MC-63965:Zombies can Attack Villagers through Fences | Duplicate:inward:MC-69551:Zombies turn/harm villagers through iron doors | Duplicate:inward:MC-70772:Zombies attack through doors | Duplicate:inward:MC-71235:Baby Zombie hit player through door. | Duplicate:inward:MC-71834:Video: Cave Spiders attack through solid floors when aggro on player | Duplicate:inward:MC-73341:In mine craft, if a zombie is behind a door, and if you attack another npc near the zombie behind the door, it will walk up to the door, and is able to attack you from behind the door. | Duplicate:inward:MC-74629:zombie through doors | Duplicate:inward:MC-74905:mobs can interact with each other through doors,fences, and glass panes | Duplicate:inward:MC-74907:Iron Golems can hurt players and mobs through walls | Duplicate:inward:MC-77499:Spiders can attack through blocks and at a high distance when crowded | Duplicate:inward:MC-79382:Zombies turning villagers through doors | Duplicate:inward:MC-88647:Glitchy spiders hitting through wall | Duplicate:inward:MC-92896:Mobs can STILL be hit through corners | Duplicate:inward:MC-96693:Unable to attack mobs through closed doors, though there are holes in them. | Duplicate:inward:MC-96860:Mobs continue to attack player when a villager closes door | Duplicate:inward:MC-99135:Villagers dying in blocked doors. | Duplicate:inward:MC-100083:Enemies with sword can attack through walls | Duplicate:inward:MC-100129:Zombies can attack through the corners of blocks | Duplicate:inward:MC-106854:zombies attacking through blocks | Duplicate:inward:MC-106966:Zombies can attack through corners | Duplicate:inward:MC-107078:Glitches | Duplicate:inward:MC-110408:Certain mobs can attack diagonally | Duplicate:inward:MC-116039:Cave spiders can hit the player through the floor. | Duplicate:inward:MC-125826:Zombies can attack through doors | Duplicate:inward:MC-126046:The spiders can attack you under a block that is below you | Duplicate:inward:MC-129797:dolphins can hit | Duplicate:inward:MC-131846:Phantoms can hit you through blocks. | Duplicate:inward:MC-136341:Zombies Attack/Turn Villagers through doors | Duplicate:inward:MC-137849:Illager Beast can attack through blocks | Duplicate:inward:MC-138903:Pillager Beast | Duplicate:inward:MC-139210:The "illager beast" can hit players through walls | Duplicate:inward:MC-140962:new village style lets mobs kill villagers! | Duplicate:inward:MC-143305:Zombies see and attack residents through the corner of the house. | Duplicate:inward:MC-146425:Iron golem and ravager can attack their targets through walls. | Duplicate:inward:MC-146545:a 1.14 Bug and it needs to be fixed fast | Duplicate:inward:MC-147211:Enderman can hit you through the slab in survival. | Duplicate:inward:MC-147928:Ravager can hit you through 1 block wall | Duplicate:inward:MC-148521:Mini Zombies can attack you through closed doors | Duplicate:inward:MC-151950:Ravagers are able to attack player through blocks from a distance of at least 3 blocks away | Duplicate:inward:MC-152319:Ravanger can hit players through blocks | Duplicate:inward:MC-152893:Spiders | Duplicate:inward:MC-154751:Cave Spiders can hit you from a block | Duplicate:inward:MC-154789:Pufferfish Deal damage through blocks | Duplicate:inward:MC-154877:Mobs hitting through corners of walls. | Duplicate:inward:MC-155446:Ravagers hit through blocks | Duplicate:inward:MC-156313:Spider deals damage through half slabs | Duplicate:inward:MC-158868:Ravager can hit and see through walls and hit box causes insane issue when trying to hit it. | Duplicate:inward:MC-159479:Bees sting through Glass Panes | Duplicate:inward:MC-161491:The Ravager is able to kill players thru buildings | Duplicate:inward:MC-162382:Bees sting through glass panes | Duplicate:inward:MC-162849:Iron golems can hurt players and mobs through walls | Duplicate:inward:MC-164394:Pandas can attack through a full solid block | Duplicate:inward:MC-167784:Bees can attack through slim blocks | Duplicate:inward:MC-168686:Died to Ravager in my home through wood blocks | Duplicate:inward:MC-169158:Bee stung through glass pane | Duplicate:inward:MC-169800:Iron Golem deals damage through the wall | Duplicate:inward:MC-171356:Zombies can hit through doors | Duplicate:inward:MC-172294:Bees sting through glass panes again (1.15.2) | Duplicate:inward:MC-172863:Enderman hitting though wall | Duplicate:inward:MC-172864:Enderman hitting though wall | Duplicate:inward:MC-172939:Iron Golem attack not just through door, but a good 2.5-3 blocks through | Duplicate:inward:MC-175374:Spider can hit up through blocks | Duplicate:inward:MC-177256:Spiders beat the player through half blocks | Duplicate:inward:MC-179312:Mobs hitting through walls | Duplicate:inward:MC-181047:Pufferfish attacks through wall | Duplicate:inward:MC-184710:Some mobs don't have appropriate "stopping ranges" when attempting to attack an enemy. | Duplicate:inward:MC-186969:AFK bug or Alt+tab glitch | Duplicate:inward:MC-188523:iron golem can hit the player from 1 block {if u in the house} | Duplicate:inward:MC-190029:zombie atack villager through block | Duplicate:inward:MC-192705:Bug where you can hit people with arrows through walls. | Duplicate:inward:MC-192895:Zombies can attack through player-built cobblestone | Duplicate:inward:MC-194971:Enemies can hit through blocks. | Duplicate:inward:MC-195335:Zombified Piglin can attack through block corner | Duplicate:inward:MC-196923:zombies can punch through fences | Duplicate:inward:MC-198114:spiders can attack players through blocks | Duplicate:inward:MC-198395:Bug in spiders | Duplicate:inward:MC-198476:The Sweeping Attack can hit through corners | Duplicate:inward:MC-199687:Spiders can hit through blocks | Duplicate:inward:MC-201532:Spiders can be shot if they are right up against glass panes | Duplicate:inward:MC-202151:so piglin brutes can hit through walls. | Duplicate:inward:MC-202426:Zombies can hit through blocks | Duplicate:inward:MC-207383:Damage Through Walls | Duplicate:inward:MC-209036:Mobs able to get you through corners | Duplicate:inward:MC-211507:Mobs are able to hit you through blocks | Duplicate:inward:MC-211695:Mobs can hit you through walls with no blocks as a corner | Duplicate:inward:MC-211873:mobs | Duplicate:inward:MC-215294:Magma Cubes are Deadly | Duplicate:inward:MC-217006:Iron Golems can hit you through blocks. | Duplicate:inward:MC-217360:Zombies are hitting me through blocks when I crawl. | Duplicate:inward:MC-218016:Mobs Hitting Players Through Walls | Duplicate:inward:MC-218423:Endermen are broken. Please fix | Duplicate:inward:MC-220315:zombie and the door bug | Duplicate:inward:MC-220665:Attacked by zombified piglin through a wall | Duplicate:inward:MC-224513:Endermen can attack diagonally through solid blocks | Duplicate:inward:MC-227326:Spiders can attack player through slabs | Duplicate:inward:MC-227631:Iron golems can hit you through wall | Duplicate:inward:MC-228635:zombies hits me right through block | Duplicate:inward:MC-229284:Spiders attacks through walls | Duplicate:inward:MC-230134:i was play the new 1.17 when i found that spiders can hit me through solid blocks | Duplicate:inward:MC-230627:Cave Spider Reach | Duplicate:inward:MC-231751:Spiders can hit me through doors | Duplicate:inward:MC-231753:Iron Golems can hit me Through walls | Duplicate:inward:MC-233245:Spiders can hit the player from beneath a block | Duplicate:inward:MC-241510:Spiders can go through walls | Duplicate:inward:MC-241648:dead | Duplicate:inward:MC-250268:Bees can sting you through doors and slabs | Duplicate:inward:MC-253264:Ravagers can kill me through walls | Duplicate:inward:MC-253637:Spiders can hit trough slabs/ground. | Duplicate:inward:MC-258640:Ravagers hit through walls | Duplicate:inward:MC-261497:Spiders being able to attack through Stairs | Duplicate:inward:MC-261906:iron golems kill zombie villagers and zombies throught walls | Relates:outward:MC-108937:Attack ranges for certain mobs are incorrect | Relates:inward:MC-3059:Projectiles can pass through thin surfaces | Relates:inward:MC-97042:Villagers not opening the correct door. | Relates:inward:MC-1297:You can attack and be attacked through glass panes | Relates:inward:MCPE-162607:Polar bears can hit / attack players through blocks | Relates:inward:MCPE-66294:Creatures can attack through glass panes

## Description

The bug
Mobs can attack you through blocks and corners due to miscalculation of attack radius.
How to reproduce
- Build a completely sealed off house with no windows or doors from opaque blocks like planks or cobblestone or the like, leave some blocks in the inventory for you to place in step 7.

- Make a two-block tall one-block wide empty doorway in the wall for you to go through and to seal off with blocks in step 7.

- Outside the house, spawn a Ravager.

- Switch to survival mode.

- The Ravager should start going for you.

- Run in the house, let it hit you once through the empty doorway.

- Seal off the doorway with two blocks.

Result: The Ravager is still able to hit the player, from about two blocks away, with a complete wall every possible place in between.
Expected: The Ravager can't attack the player any more.
Example
An example can be seen in this comment.
Old example
I just created a villager in MCEdit with the Create Shops filter to have a custom shop. I saved it and launched MC. The villager started to run around normally in his house but then he went to the door where a zombie was knocking at (wooden door on normal difficulty) and the villager blinked red and got damage and after a few hits he died. The zombie killed him through a closed door and the villager did not run away he always came back to the door until he died.
Additional informations
From :
There are a number of bug reports about attack radius that are all very similar. MC-2310, MC-18326, MC-50668, MC-63965, MC-71834, and MC-74907 are all about the attack radius of mobs extending through blocks. (Some mobs are more bugged than others, but it’s the same basic problem).
There are also a few related issues:
-  is the same as the above, but for players.

-  is the same as the above, but for arrows.

Code analysis
Based on 1.11.2 decompiled using MCP 9.35 rc1
The problem seems to be the method net.minecraft.entity.ai.EntityAIAttackMelee.checkAndPerformAttack(EntityLivingBase, double) and methods overriding it. They all only test if the mob to attack is in a certain radius to the attacker without testing if blocks are between them.
Possible solutions
Bounding box check
The current behavior would be replaced by only allowing mobs to attack other mobs when their bounding boxes intersect.
Ray casting
The current behavior would be extended to require a ray cast from the attacker to the mob to attack (excluding liquids and blocks without collision box) to return no colliding blocks. Possible use y + height / 1.5 as attack height or have a method for mobs to define their attack height(s?). The height at which the mob to attack will be attacked could for example be y + height / 2 or with multiple tries depending on the height of the mob, for example

```
for (int attackFraction = 0; attackFraction < height / 2; attackFraction++) {
    double attackHeight = y + height * ((attackFraction + 1.0) / (height / 2.0 + 1.0))
}
```

## Comments (100)

### Comment 1: migrated (2012-11-05T01:19:57.616-0800)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: migrated (2012-12-05T13:35:42.190-0800)

I know I'm not a mod but I think I know the problem. Zombies can't hit mobs but can break doors when they are closed. If the door is open, the zombie can hit mobs but can't break it down. If you place the door sideways, then put it in the open position, zombies can hit mobs (like the villager) through doors. Th other problem might be that Createshops filter was messing it up. If the zombie is making the banging noises than Createshops is the problem. If not it could be either one. I may also be completely wrong.

### Comment 3: migrated (2013-06-23T13:07:07.448-0700)

We're seeing this on naturally generated villages in our vanilla server.

### Comment 4: migrated (2013-07-09T01:08:38.917-0700)

This can sometimes happen to players (tested 1.6.2) and will always occur with baby zombies.

### Comment 5: migrated (2013-08-22T13:01:07.556-0700)

This is a really annoying problem which I hope is fixed soon. Confirmed to still be an issue on Mineraft 1.6.2 with Java 7 update 25 64-bit.

### Comment 6: migrated (2013-10-31T03:49:02.779-0700)

Maybe this issue should be re-opened. I ran some tests in a creative world and it appears that villagers seem to crowd,mostly around the door, in one or several houses at night.
Because the zombies group before the door and then start hitting the villagers through the door somehow, if one villager turns into a zombie, your whole villager population is killed in one sweep.

### Comment 7: migrated (2013-10-31T08:36:46.804-0700)

Reopened? It was never resolved in first place.

### Comment 8: migrated (2014-01-23T09:28:28.561-0800)

This is still an issue in all versions up to and including 14w04a.

### Comment 9: migrated (2014-02-16T21:32:06.836-0800)

Got attacked through an iron door by a Zombie Pigman earlier using snapshot version 14w07a.

### Comment 10: migrated (2014-04-04T13:40:31.766-0700)

This bug is observed in 14w11b.

### Comment 11: migrated (2014-05-07T13:15:54.913-0700)

is this problem being fixed? cause i"m now in snapshot 14w18b and zombies can hit me trough doors.
never had this problem before this snapshot though :S ...
oh and btw: zombies don't break down doors anymore, maybe its related.

### Comment 12: migrated (2014-05-07T14:23:27.941-0700)

This old a bug and none of you noted how it happens? This is old news. If a mob is standing in the block that the door is on ("in the alcove") they can hit through the door. This can be fixed by removing the door and replacing it so the alcove is on the inside of the house. I often go through newly found villages fixing the doors and changing the location of the doorway on the blacksmith (if you add a door in the old location it kills villagers, as they mistake the outside for the inside. The mods here have declared it "not a bug because Mojang doesn't intend players to fix up villages").
Also zombies break down doors on hard only. They half-break the doors on normal and easy (bang on the door causing it to crack but never get further than halfway broken).
Also related: Players can hit baby zombies through the door from the alcove. Only instance I know of where players get to hit through the door. Normally it's only monsters.
EDIT: if the alcove is on the inside and zombies are still getting kills through the door it's probably that other glitch. If multiple villagers are pushing each other and one is in the alcove they can be slightly pushed through the door. It corrects itself (like animals being pushed through fences usually corrects itself) but for a second the villager is vulnerable to hits from zombies outside. I think that's the same way wolves get kills on fenced in sheep.

### Comment 13: migrated (2014-05-08T06:54:12.358-0700)

Only some zombies spawn with the ability to break doors, most of them can't break them.

### Comment 14: migrated (2014-08-22T08:10:27.256-0700)

I can confirm this is still an issue on the 1.8-pre1 release. Zombies are able to kill villagers, as well as players, through any door when close enough to the closed door.

### Comment 15: migrated (2014-09-03T21:54:14.090-0700)

I created a new singe player game, in which a village was close by.
During the night, I heard the "oomph!" sound of a villager being damaged, so I went out of the building and saw a zombie on the outside and villager on the inside. I killed the zombie and went inside with the villager. Another zombie came and as the villager went by the door, it was hurt. I could hear other villagers hurt in another building. I protected my one villager until morning and I went to check on the other villagers.
There were no more villagers, but 6 new 'zombies' were let out of the building the villagers had been in and were promptly killed.
These were all spawned villages and it seems as though normal doors do not prevent villager/zombie damage. Im bummed because I only have 1 villager now.

### Comment 16: migrated (2014-09-04T12:13:30.393-0700)

Using a splash potion of weakness then a regular golden apple should turn a villager zombie back into a normal villager. So instead of killing the zombies, you could have left them for when you got the potions and golden apples and you would have 7 villagers left. This might end up costing far too much gold though.

### Comment 17: migrated (2014-09-04T12:31:53.850-0700)

There are quite a few problems with blocks that don't take up the whole 1m by 1m area. For doors, being attacked by mobs or being shot by an arrow through the door is probably possible because the player or entity's hitbox ends up outside of the door, allowing interaction with it. This has also occasionally happened with regular blocks in a corner where you can see the mob's arm, allowing you to kill a zombie through solid blocks.
PS Zombies will no longer break down doors on any gamemode or difficulty and it is intended to be that way.

### Comment 18: Sonicwave (2014-10-16T00:24:33.857-0700)

Confirmed for 1.8.1-pre1/pre2.

### Comment 19: migrated (2014-12-29T13:55:21.199-0800)

the problem is the hitbox of a zombie.
the hitbox of a zombie (which can be see by pressing F3 + B) can sometimes glitch in the hitbox of  a door. however, i do believe this is just a directional glitch.
when the hitbox of a zombie and something it wants to hit collide, the zombie can actually hurt it.

### Comment 20: migrated (2015-01-04T12:19:17.888-0800)

I got killed by a baby zombie going through a IRON DOOR!!!!

### Comment 21: migrated (2015-01-04T12:21:09.580-0800)

Edit: baby zombie bypassing the iron door is for 1.8,1.8.1 now this bug has ben fixed for 1.8.2 and it started after upgradeing from 1.7.10

### Comment 22: migrated (2015-01-06T10:11:00.149-0800)

I also have this problem, my villagers keep dying and I have to block the house entrances with dirt until the morning (damn it...).

### Comment 23: migrated (2015-02-17T13:45:42.939-0800)

http://minecraft.gamepedia.com/Zombie
At "Behavoir" they say zombies are able to deal damage through a closed door.

### Comment 24: migrated (2015-02-17T14:24:17.083-0800)

The Minecraft Wiki isn't considered a reliable source for bug reports. It basically documents the current behavior of the game.

### Comment 25: migrated (2015-06-26T12:32:57.917-0700)

I think this relates to  because what is probably happening in both is that the attack IN GENERAL is just going through the door.

### Comment 26: Sonicwave (2015-08-14T18:56:27.855-0700)

Confirmed for 15w33c. It doesn't help that the villagers often press themselves against the door, even if a zombie is trying to break it - _ -

### Comment 27: migrated (2015-11-20T21:46:25.075-0800)

Confirmed for 15w47c

### Comment 28: migrated (2015-12-02T14:03:03.870-0800)

Confirmed for 15w49a

### Comment 29: migrated (2015-12-09T10:15:52.426-0800)

Confirmed for 15w50a

### Comment 30: migrated (2016-01-19T21:51:29.982-0800)

confirmed 16w02a , through closed door and diagonally through corners of blocks and both at same time

### Comment 31: migrated (2016-02-07T10:16:19.568-0800)

This is confirmed for 16w05b, and it's also unfair how the Player is unable to attack through closed doors. My friend created an issue about the Player being unable to attack through closed doors. See MC-96993

### Comment 32: migrated (2016-02-13T15:42:33.860-0800)

Confirmed for 16w06a

### Comment 33: SunCat (2016-02-23T11:44:01.511-0800)

Confirmed for 1.9-pre2

### Comment 34: SunCat (2016-02-24T10:21:25.573-0800)

Still in 1.9-pre3

### Comment 35: SunCat (2016-02-27T03:24:24.243-0800)

Still in 1.9-pre4

### Comment 36: migrated (2016-03-07T05:57:22.655-0800)

Has anyone had the problem in 1.9 where you cover up the door with blocks and the villagers still die?  It used to keep them safe, but I lost most of a village yesterday.  I guess I'll have to build a whole little room in front of each door until I get the village walled and lit.

### Comment 37: SunCat (2016-03-09T11:10:15.369-0800)

Still in 1.9.1-pre1

### Comment 38: SunCat (2016-03-12T10:38:20.772-0800)

Still in 1.9.1-pre3

### Comment 39: migrated (2016-03-16T23:23:04.079-0700)

There are a number of bug reports about attack radius that are all very similar. , MC-18326, MC-50668, MC-63965, MC-71834, and MC-74907 are all about the attack radius of mobs extending through blocks. (Some mobs are more bugged then others, but it’s the same basic problem). There are also a few related issues:
 is the same as the above, but for players.
 is the same as the above, but for arrows.
Most or all of these reports should be consolidated into one, as they are all caused by the same base issue.

### Comment 40: migrated (2016-04-23T20:52:04.440-0700)

Confirmed in 1.9.2.
I just died in a new hardcore world because a zombie was able to hit me through the corner of a wall.

### Comment 41: SunCat (2016-06-08T09:05:37.275-0700)

Still in 1.10

### Comment 42: migrated (2016-06-14T03:28:35.465-0700)

An arrow can also hit living entities through corners.

### Comment 43: migrated (2016-06-23T09:27:55.718-0700)

Confirmed for 1.10 and 1.10.2.

### Comment 44: migrated (2017-01-07T15:18:06.831-0800)

Confirmed for 1.11.2.

### Comment 45: migrated (2017-02-08T02:39:40.219-0800)

I myself tested and confirmed for 1.9.4, 1.10.2, 1.11.2 both:
- adult zombies hit through corners of a (diagonal) wall (sometimes an arm can be seen) and

- adult zombies hit through a closed door.

Maybe it's not attack radius but something like hitbox or gaps or solidity of the object(s) between attacker an mob/player. (Seed -5821562820736002727 on 1.11.2 generates a village near the spawn - all villagers die because in the houses they are not safe against zombies.)
For similar description see the duplicates (whose problems are not solved, but there status is "resolved" only because they are duplicates).
My details: I tested with zombies on one side and villagers and player on the other side of a wall. I tested some types of stone and wood - all the same result. Hitting through the door is not affected by the orientation (inside/outside) of the door.
X = block of the wall
D = door (tested in both directions)
Z = zombie
V = villager (same with player)
o = nothing special (monospace did not work here)
oZXZo
ZXVXZ
XVoVX zombies hit villagers
ZXVXZ
oZXZo
ZZZZZZ
ZXXXXZ
ZXVVXZ zombies do not hit villagers
ZXVVXZ
ZXXXXZ
ZZZZZZ
XXXX
XoVDZ zombie hits villager if both near the door
XXXX
(Many villagers were harmed during this test.)

### Comment 46: marcono1234 (2017-02-21T06:49:20.184-0800)

Added a code analysis and possible solutions I could come up with. Feel free to add own solutions as well.

### Comment 47: migrated (2017-05-17T06:29:00.837-0700)

Confirmed for 1.12 Pre Release 2

### Comment 48: migrated (2017-05-30T13:19:58.703-0700)

this bug is apperntly also in mc10 C++/PE as well not sure if i should find a report already or what

### Comment 49: FaRo1 (2017-05-31T00:43:03.451-0700)

MCBC and MCJava have two separate trackers. You can filter by using "project" in the search options. If you find a report there or, if there is none, make one, can you please comment here with the number of it so that it can be linked as related?

### Comment 50: migrated (2017-08-08T14:42:04.138-0700)

Confirmed for 1.12.1. Zombies killed me even though I was boxed into a 1x2x1 hole. Hit diagonally through corners.

### Comment 51: migrated (2017-09-26T01:39:32.306-0700)

Confirmed in 1.12.2

### Comment 52: JochCool (2018-01-21T09:01:04.175-0800)

Confirmed for 18w03b

### Comment 53: migrated (2018-02-20T16:48:50.799-0800)

I like the ray cast solution, simple and elegant and the mechanisms are already in place

### Comment 54: migrated (2018-07-24T15:25:57.343-0700)

Confirmed for 1.13.

### Comment 55: migrated (2018-07-27T09:51:36.246-0700)

This potentially is caused by the same issue, as the Drowned attack radius while they are in the swimming animation extends to about 2 blocks away. Only occurs if they are 'horizontal', otherwise attack radius is normal. This becomes very bad if they get in a boat, as they are stuck in swim animation and have a large attack radius.

### Comment 56: migrated (2018-10-28T07:38:07.381-0700)

Can confirm for 18w43c - the zombie hurts the villager and does not attack the door between them.

### Comment 57: migrated (2018-11-29T05:44:03.441-0800)

Confirmed for 18w47b

### Comment 58: migrated (2018-12-12T15:44:19.784-0800)

The villagers can also be damaged through diagonal wall spaces of the new huts usually ther 5x5 ones. appears in 18w50a

### Comment 59: migrated (2018-12-12T18:15:31.443-0800)

Confirmed for 18w50a, the majority of the villages are almost empty because all the villagers are being killed by that.

### Comment 60: migrated (2019-01-30T08:47:17.530-0800)

Still happening in 19w05a

### Comment 61: ZeNico13 (2019-03-22T09:58:09.978-0700)

Still in 19w12b

### Comment 62: ZeNico13 (2019-03-27T12:54:44.851-0700)

Still in 19w13a

### Comment 63: ZeNico13 (2019-04-03T11:53:09.825-0700)

Still in 19w14a

### Comment 64: ZeNico13 (2019-04-10T12:36:46.458-0700)

Still in 19w14b and 1.14 Pre-Release 1

### Comment 65: ZeNico13 (2019-04-12T12:45:04.381-0700)

Still in 1.14 Pre-Release 2

### Comment 66: ThePinkHacker (2019-04-17T16:09:49.885-0700)

it still happens in 1.14 Pre-Release 3 and 4

### Comment 67: ZeNico13 (2019-04-19T02:15:56.348-0700)

Still in 1.14 pre-5

### Comment 68: ZeNico13 (2019-04-23T12:00:26.606-0700)

Still in 1.14 Release

### Comment 69: ZeNico13 (2019-05-13T08:34:52.799-0700)

Still in 1.14.1 Release

### Comment 70: ZeNico13 (2019-05-17T11:11:03.747-0700)

Still in 1.14.2 Pre-Release 1 and 1.14.2 Pre-Release 2

### Comment 71: migrated (2019-07-19T15:32:20.671-0700)

Still in 1.14.4

### Comment 72: anthony cicinelli (2019-10-27T06:38:11.808-0700)

Confirmed for 19w42a

### Comment 73: TheBoy358 (2019-11-08T07:16:19.678-0800)

Confirmed in 19w45b.

### Comment 74: AGriggs191 (2019-12-09T18:48:19.017-0800)

It's very disappointing that this is still a bug 7 YEARS after being reported. I was very hopeful that it would be fixed before 1.15 comes out, but it doesn't look like that's going to happen.

### Comment 75: migrated (2019-12-30T13:50:41.297-0800)

Still in 1.15.1
Got stung by bee through glass pane (bee died)
For details: MC-169158

### Comment 76: migrated (2020-02-12T15:47:24.508-0800)

I'm having the same problem in the Nintendo Switch version of this game. Clean through the f[redacted]ing walls, 40 f[redacted]ing levels are gone now. I'll be honest, I expect these types of malfunctions from Bethesda but Mojang really dropped the ball here.

### Comment 77: marcono1234 (2020-02-13T06:22:02.348-0800)

@, this issue is only for the Java Edition. Please search if this issue has already been reported for Bedrock Edition (MCPE), which includes the Nintendo Switch version, and if not create a new report. Note that there is already MCPE-48401 which sounds similar, but not quite the same.

### Comment 78: migrated (2020-04-01T04:37:16.042-0700)

This bug is extremely conspicuous with ravagers. I'm getting killed (on hard difficulty if I don't have full health) standing 2+ blocks away from a ravager, with a door in between. Its range is bigger than the player's!

### Comment 79: [Mod] violine1101 (2020-04-04T13:06:16.424-0700)

Technical difficulties... this ticket will be reopened as soon as Arisa will let us ^^

### Comment 80: Uriel Salischiker (2020-04-04T14:35:30.642-0700)

Ticket has been reopeend

### Comment 81: RedCMD (2020-04-04T15:12:20.666-0700)

Golems can attack through over 1.5m solid thick walls

### Comment 82: migrated (2020-05-27T08:18:47.493-0700)

made a comment on MC-147516 that these issues relating to the attack ranges of mobs could be related to this issue.
https://streamable.com/hph3g1
https://streamable.com/omr8d9
https://streamable.com/fj1dqj
I attempted to make an individual issue to the bug shown in the video. MC-184710
If you think that this issue does not address the above, you should reopen my issue. Now that it seems this issue might be fixed in 1.16 (It was assigned to Searge 4 hours ago) you might as well get to fixing the issue in the videos as its very similar.

### Comment 83: migrated (2020-09-22T15:58:02.120-0700)

Ravegers are killing me 2 blocks away (me, block block, raveger) inside a building. I am playing on normal difficulty. Even with full iron armor and a shield I am dead in 2 hits and they instantly counter attack when hit. Finally, I can only escape them if I run straight, any deviation they will catch and kill me. This is too much for normal difficulty. I was also killed 23 time because the thing spawn camped me. I literally could not leave my hut. It doesn't help that I also had to deal with a mach 5 evoker spawning vexes like crazy, but that's a different ticket. I did not have this difficulty before 1.16. A raveger with a guy on top will stop to shoot giving me a chance to run at least. I had to use the other pillagers to kill this raveger.

### Comment 84: migrated (2020-10-20T11:18:34.754-0700)

I'm not sure if the villager problem relates to hitboxes but I think if the door was placed incorrectly (on the block next to the doorway) then the villager keeps walking to it (I had it too). I had zombies outside an iron door incorrectly placed and the villager kept running there and died.

### Comment 85: migrated (2020-12-19T16:07:46.098-0800)

Seriously how long does it take to implement three lines of code?
How about stop adding stuff and start fixing stuff?
This bug is game ending. Like quitting playing the game ending.
Look at that Ravenger gif above. How is that fair after all the grinding the player has done to get to that point?
We have to abide by the rules so why can't the rest of MC?

Honestly? Shame on you guys.

### Comment 86: migrated (2021-07-16T12:03:22.266-0700)

Can confirm in 1.17.1

### Comment 87: migrated (2021-07-29T13:24:21.887-0700)

Can confirm in 1.17.1
Ravagers can attack you through a completely sealed off wall if they are still targeting you behind it.
Steps to reproduce:
- Build a completely sealed off house with no windows or doors from opaque blocks like planks or cobblestone or the like, leave some blocks in the inventory for you to place in step 7.

- Make a two-block tall one-block wide empty doorway in the wall for you to go through and to seal off with blocks in step 7.

- Outside the house, spawn a Ravager.

- Switch to survival mode.

- The Ravager should start going for you.

- Run in the house, let it hit you once through the empty doorway.

- Seal off the doorway with two blocks.

Result: The Ravager is still able to hit the player, from about two blocks away, with a complete wall every possible place in between.
Expected: The Ravager can't attack the player any more.

### Comment 88: ampolive (2021-10-03T15:47:43.710-0700)

Can confirm in 21w39a.

### Comment 89: migrated (2022-04-29T14:27:55.353-0700)

Can confirm 22w17a, 22w16a, and 22w15a.

### Comment 90: migrated (2022-06-22T19:40:25.714-0700)

Can confirm in 1.19.1-pre1
Especially the Ravager can be very annoying due to this bug
I made 2 new small clips to show the issue (One is also with F3 if that helps the devs)
Edit: Apparently my videos don't work on this website (although they are normal mp4), so I uploaded them to Imgur...here is the link

### Comment 91: NBG-bootmgr (2022-07-20T03:51:58.313-0700)

test and confirm in 1.19.1-pre5

### Comment 92: NBG-bootmgr (2022-08-19T02:54:54.209-0700)

Can confirm in 1.19.2

### Comment 93: migrated (2022-11-12T22:36:59.889-0800)

Tested in 1.18 thru 1.19.2
I've noticed that this happens once a mob has already started attacking, not before that.  I have a villager zombification/curing station wherein a villager in a minecart is in the corner and a zombie is on the outside of the corner.  With the flick of a lever, the blocks on one side of the corner are pulled away, allowing the zombie to attack.  If I deactivate the lever and push the zombie back outside BEFORE he attacks the villager, he will go idle, but if I let him attack the villager even one time before pushing him outside, he continues to attack the villager through the corner until the villager is zombified.  See attached screenshots: when the wall is open, the villager is being attacked.  Even after I close the wall, the zombie continues attacking over and over.

### Comment 94: Brain81505 (2023-02-01T08:07:17.544-0800)

Can confirm in 23w06a

### Comment 95: Brevort (2023-06-14T15:38:20.576-0700)

Affects 1.20.1.

### Comment 96: migrated (2023-08-14T10:30:23.172-0700)

OMG NO WAY THEY FINALLY FIXED IT
After almost 11 years, against all odds, someone at Mojang finally fixed one of the most annoying issues in the game.
Whoever is the dev that fixed it: https://imgur.com/a/xFoTlWQ
We need to get this guy a dev of the year award.

### Comment 97: migrated (2023-08-14T13:05:50.969-0700)

In 23w32a

### Comment 98: windwend (2023-08-14T17:33:54.852-0700)

Finally, zombies can't hit you through doors anymore. Good job Gnembon!

### Comment 99: migrated (2023-08-14T18:02:13.386-0700)

Woah, amazing to see this fixed.

### Comment 100: FaRo1 (2023-08-19T07:03:02.713-0700)

Still happens sometimes in 23w33a with spiders.
