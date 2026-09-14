# MC-9568: Mobs suffocate / go through blocks when growing up near a solid block

**Mojira URL:** [https://bugs.mojang.com/browse/MC-9568](https://bugs.mojang.com/browse/MC-9568)

## Report details

- **Mojira categories:** Hitboxes
- **Project:** MC
- **Issue key:** MC-9568
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2013-02-10T08:16:25.417-0800
- **Updated:** 2025-04-29T09:27:48.646-0700
- **Resolution date:** 2024-05-13T01:52:51.429-0700
- **Affects versions:** Snapshot 13w06a; Snapshot 13w07a; Snapshot 13w09a; Snapshot 13w09b; Minecraft 1.5; Minecraft 1.5.1; Minecraft 1.5.2; Snapshot 13w17a; Snapshot 13w19a; Snapshot 13w21a; Minecraft 1.6.1; Minecraft 1.6.2; Minecraft 1.7.9; Minecraft 14w32d; Minecraft 1.8; Minecraft 15w44b; Minecraft 15w45a; Minecraft 15w46a; Minecraft 1.11.2; Minecraft 1.12; Minecraft 1.12.1; Minecraft 1.12.2 Pre-Release 1; Minecraft 1.12.2; Minecraft 18w01a; Minecraft 18w02a; Minecraft 18w03b; Minecraft 1.13-pre2; Minecraft 19w12a; Minecraft 1.14; 1.15.1; 1.15.2; 20w12a; 20w19a; 1.16.2; 1.16.3; 1.16.4; 20w48a; 20w51a; 21w03a; 21w05a; 21w05b; 21w07a; 21w11a; 1.17 Release Candidate 1; 1.17; 1.17.1; 1.18.1; 22w03a; 1.18.2; 1.19; 1.19.1 Pre-release 2; 1.19.1 Pre-release 3; 1.19.2; 1.19.4; 23w14a; 1.20 Pre-release 6; 1.20.6
- **Fix versions:** 21w05a; 24w19a
- **Area:** Gameplay
- **Labels:** baby; mob
- **Watchers:** 1
- **Attachments:** 7
- **Attachment filenames:** 2017-10-02_00.11.57.png; DpP41Mf.png; MC-9568 not fixed.mp4; MC-9568 Proposal.txt; MC-9568 Still not fixed.mp4; Minecraft 21w05a - Singleplayer.mp4; Video_2024-05-10_18-58-13.mp4
- **Issue links:** Duplicate:inward:MC-9435:Adult chicken die when you pushing them on a solid block | Duplicate:inward:MC-9540:Adult chickens eventually die if caged near solid blocks | Duplicate:inward:MC-9626:Glitching mob that kill them | Duplicate:inward:MC-9635:Baby chickens glitching into solid blocks and dying | Duplicate:inward:MC-9742:Mobs suffocating by walking into walls | Duplicate:inward:MC-9776:Chicken Suffocation | Duplicate:inward:MC-9805:Mobs walking into walls and suffocating | Duplicate:inward:MC-9838:Baby sheeps disappear | Duplicate:inward:MC-9976:Breaded animals (babies) are disappearing somehow and rare mob spawning | Duplicate:inward:MC-10012:Hitbox for child mobs error when growing up | Duplicate:inward:MC-10157:Animals suffocate in walls | Duplicate:inward:MC-10181:Dying animals | Duplicate:inward:MC-10229:Mobs suffocate in walls upon growing into adults | Duplicate:inward:MC-10268:Mob's collision boxed don't update when they grow, but their hit boxes do EDIT: sorry, its fixed on 07a | Duplicate:inward:MC-10287:Chickens randomly die. | Duplicate:inward:MC-10370:13w06a: Rare Baby Animal hitbox bug, grows up to die by suffocating itself in a wall | Duplicate:inward:MC-10552:Cows getting damage from blocks | Duplicate:inward:MC-10797:Random animal death | Duplicate:inward:MC-11492:Baby cows used to die in 13w snapshots and sometimes in 1.5 pre | Duplicate:inward:MC-11543:Chickens Phasing through walls or dying upon maturity | Duplicate:inward:MC-11727:Chickens crazy | Duplicate:inward:MC-12208:Animals !! get killd | Duplicate:inward:MC-12481:Chickens die as they grow to adult | Duplicate:inward:MC-13507:Animals glitching through blocks when changing from child stage to adult stage | Duplicate:inward:MC-16239:Horses in Walls | Duplicate:inward:MC-16603:Animals growing up outside of fences. | Duplicate:inward:MC-16950:Baby chickens can be pushed through fences | Duplicate:inward:MC-17096:Baby Chickens Hitboxes seem to be too small | Duplicate:inward:MC-19969:Baby chickens glitch in to blocks and die | Duplicate:inward:MC-22924:Baby chickens die when they grow | Duplicate:inward:MC-27175:Foal died randomly | Duplicate:inward:MC-28116:SHeep not regrowing wool, lambs disappearing | Duplicate:inward:MC-53646:Any nee villager get trapped in wall and die | Duplicate:inward:MC-68433:Animals that grow up near fences get out | Duplicate:inward:MC-72576:Mobs glitch into walls and suffocate | Duplicate:inward:MC-73317:Sheep suffocating in walls or appearing outside them | Duplicate:inward:MC-77304:Villagers Get Stuck In And Suffocate In Walls | Duplicate:inward:MC-92524:Growing up mobs can glitch through fence (south-east corner for most times) | Duplicate:inward:MC-150657:Baby animals suffocate when they grow up | Duplicate:inward:MC-168590:Baby Bees growing up and glitching through blocks | Duplicate:inward:MC-172571:Bee Glitching | Duplicate:inward:MC-183131:Spontaneously vanishing villagers and bees. | Duplicate:inward:MC-183139:Spontaneously vanishing villagers and bees. | Duplicate:inward:MC-183179:Baby Bees despawn when they grow up | Duplicate:inward:MC-185783:Bees clip through blocks when aging. | Duplicate:inward:MC-203318:bee | Duplicate:inward:MC-213951:Villagers teleporting through glass when they grow up | Duplicate:inward:MC-221452:Baby animal NoClip through fences when they grow up when pushed | Duplicate:inward:MC-227605:mobs still glitch out fences when growing | Duplicate:inward:MC-229065:When baby chickens grow up, they pop up outside(raw chicken farm) | Duplicate:inward:MC-230739:Mobs ghosting through solid blocks | Duplicate:inward:MC-232496:Chickens when growing from adults on a slab with a carpet above them no longer stay in origin block | Duplicate:inward:MC-241571:Cows glitching through fences | Duplicate:inward:MC-250012:Baby villagers when grown can grow into blocks and take damage/go through walls | Relates:outward:MC-1524:Baby mob collision boxes are too large. | Relates:inward:MC-212284:Crammed enitities pushed through blocks when growing to adults

## Description

The bug
Animals seem to suffocate when growing up near a solid block.
How to reproduce
- Create a one block large, two block high enclosure. Use solid blocks like cobble.

- Throw chicken eggs in it until 4 chickens have spawned

- Wait until all chickens are grown up

- Count the chicken

Most of the time all of the chickens have died, sometimes 1 or 2 survive. This happens not only in tight enclosure but also randomly near walls or blocks.
If the blocks are transparent (glass, fence) the animal just can walk through.
I think this is probably due to a smaller hitbox, that is immediately enlarged, when the animal grows up.
See this comment and ticket: https://bugs.mojang.com/browse/MC-1524?focusedCommentId=43968&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-43968
Also note
 which provides a concrete way to reproduce and an explanation.
Code analysis
Code analysis by  can be found in this comment.

## Comments (79)

### Comment 1: migrated (2013-02-10T08:16:25.417-0800)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: migrated (2013-02-13T07:40:15.115-0800)

This happens also in bigger areas, at least with cows. I created a 2 high sandstone wall with 4x8 area inside, and over 50% of cows died pretty much immediately after growing up.
Something else is wrong with the collision boxes even if the cows survive this. Rest of the cows that were originally small cows (spawned with eggs, but problem occurs also with the ones born "naturally"), died quite rapidly to suffocation when walking around the wall holding a wheat.

### Comment 3: migrated (2013-02-14T01:59:10.793-0800)

Noticed this on a SMP server.  Was breeding cows in a fairly large pen, and cows were pushing each other into the walls(2 high stone brick blocks) and suffocating.  There was plenty of room in the pen for the cows to go, but they tend to cluster around the sides. And if you have baby cows they will clump together around the closest adult cow, in which they typically force the adult against the wall and it dies.

### Comment 4: migrated (2013-02-14T02:41:32.177-0800)

See also: https://mojang.atlassian.net/browse/MC-9540

### Comment 5: migrated (2013-02-15T11:13:43.096-0800)

I have the same issue: (MC-9838)

### Comment 6: migrated (2013-03-02T12:09:08.099-0800)

This also still happens in 13w09c and another thing to note is when reloading chunks baby mobs will glitch out of the fence if the fence is intersecting in 3 points with a torch on top.
Sorry that I couldn't be more helpful,
jamesloon

### Comment 7: migrated (2013-03-05T00:53:43.600-0800)

Still an issue in 13w10a.
This issue exists because of the hitbox bug. The newly grown adult animal keeps the baby-sized hitbox for collision detection, but the adult-sized one for damage/suffocation until you relog. Adult animals with the baby-sized collision box can therefore walk into a wall and suffocate in it.

### Comment 8: migrated (2013-03-05T00:56:55.612-0800)

There are a lot of related bugs which are essentially duplicates. They are all related to the baby/adult collision box mix-up.

### Comment 9: migrated (2013-03-08T18:40:36.114-0800)

This is still happening in the 1.5 pre- release especially with chickens on top of hoppers for me
Edit: SO while I was sitting here typing the original post and a chicken pops up infrount of me. It apears they also are glitching through blocks (glass in my case)

### Comment 10: migrated (2013-03-11T07:54:49.160-0700)

This is related to my post of,,, MC-11349
https://mojang.atlassian.net/browse/MC-11349
which is aparently a duplicate of this according to mods.
https://mojang.atlassian.net/browse/MC-2025
These are also related to it , MC-18, , MC-1029, MC-1524, , MC-2037, MC-3140, MC-3753, MC-4707, MC-5187, MC-5230, MC-5369, MC-5401, MC-6115, MC-6393, MC-6396, MC-6398, MC-6465, MC-6653, MC-6707, MC-7392, MC-7462, MC-8390, MC-8707, MC-9039, MC-9393, MC-9476, MC-9483, MC-9503, MC-9525, MC-9540, , MC-9626 , MC-9635, MC-9742, MC-9753, MC-9772, MC-9777, MC-9805, MC-9838, MC-9894, MC-9926, MC-9976, MC-9988, MC-10012 , MC-10116, MC-10157, MC-10181, MC-10229, MC-10231, MC-10268, MC-10311, MC-10370, MC-10422, MC-10552, MC-10725, MC-10797, MC-10894, MC-11009, MC-11022, MC-11052, MC-11086, MC-11203, MC-11252 ....

### Comment 11: migrated (2013-03-11T08:31:47.808-0700)

Mark This as Duplicate.
Keep  Going downward through solid blocks, causing suffocation, death of entries, and entities escaping
Keep  Going forward through solid blocks, causing suffocation, death of entries, and entities escaping

### Comment 12: clipka (2013-04-26T17:23:00.509-0700)

still present in 13w17a

### Comment 13: migrated (2013-05-10T02:08:23.896-0700)

This is still happening in 1.5.2 full release.
Any and all animals which have a smaller hit box when they are babies than when they are adults, will begin to take suffocation damage when they grow, if they are next to a block.
This is because when they grow, their hit boxes embiggen, taking space inside the solid block.
The animal will become stuck and invariably die.
This will happen in ANY sized pen, not necessarily 1x1 boxes. Because the baby animal simply needs to be standing next to any block at the point of growth.

### Comment 14: migrated (2013-05-23T13:25:08.501-0700)

Stin in 13w21a. MUCH easier to reproduce with horses.

### Comment 15: migrated (2013-06-18T09:46:00.556-0700)

13w25b confirmation. Baby Horses are a pain to look after in a pen due to them getting pushed into solid blocks and suffocating or just walking through fences/non-solid blocks. I really thought that Mojang would have fixed this by now.

### Comment 16: migrated (2013-06-18T10:27:17.994-0700)

A fix for this seems to have been made by people here, on a related issue:
https://mojang.atlassian.net/browse/MC-2025

### Comment 17: migrated (2013-06-28T17:16:33.437-0700)

this seems to happen almost all the time with baby sheep growing up close to a wall and it ruins my sheep farm in survival

### Comment 18: migrated (2014-01-29T06:39:04.631-0800)

Not only does this still happen in 1.7.4, but it's a frightfully common bug and all mobs can do that, not just animals and not just babies. I have a zoo map where I have rooms with mobs of each kind, and each mob has PersistenceRequired:1 and Invincibility:1 tags. If a mob (let's say a cow) is near a thin wall (glass pane, iron bars, doors etc.) and then you quit and reload the world, in most cases it will already be on the other side of the wall. This can also happen if a mob pushes another one into a wall - mobs get stuck in it even if it's a solid thick wall made of 3 layers of stone. Thanks to invincibility tag, mobs didn't suffocate on my map and they were really stuck in the wall, with blackened colours. Squids and bats are especially prone to execute this bug.
Newest snapshot doesn't fix that yet either.

### Comment 19: migrated (2014-01-29T06:51:13.000-0800)

My horse was tethered outside my house and walked up against the wall and just started suffocating. It was free to walk away (not stuck) and the tether was even pulling it away from the wall, yet it stood there and died.
Can't you just make mob's hitboxes (for damage/suffocation) slightly smaller than their collision hitbox to allow room for error? ...or as with players, let them be pushed out of a block when inside it?

### Comment 20: migrated (2014-01-30T22:23:33.146-0800)

This still holds true for the current snapshot 14w05a. I've had a donkey and wolf both suffocate after I accidentally nudged them near a wall.

### Comment 21: migrated (2014-03-04T11:46:39.802-0800)

I just tested this in many versions from 1.6.2 to 14w08a, with 200 chickens in a 1x1 pit. Not even one chicken died when growing up. Can someone who noticed the bug before can test it on a recent snapshot?

### Comment 22: migrated (2014-04-05T00:51:56.077-0700)

This is definitely happening to me in 14w11b with both chickens and cows (haven't tested with pigs). My chickens have a smaller enclosure (2x2) and die more frequently (during gameplay, probably when chunk gets unloaded then loaded). The cows' enclosure is a larger one (approx 8x15) and they seem to only die when I log back into my world.

### Comment 23: migrated (2014-05-26T06:16:15.655-0700)

Not only are animals dying but so are villagers; suffocating or getting stuck in the stupidest spots. I can't stupid proof my village anymore than I already have!

### Comment 24: migrated (2014-07-10T23:10:28.498-0700)

This just happened to one of my donkeys.  Donkey got pushed inside a wall, suffocated, and died.  All the items inside the donkey's chest flew all over the place and I had no room to store them anywhere.

### Comment 25: migrated (2014-08-08T20:30:22.877-0700)

Happens in 14w32d. My baby cows keeps dying, and I can't repopulate!

### Comment 26: Niknokinater (2014-08-11T13:42:39.453-0700)

This could be my problem. I would have a Baby Cow in an area that has fence for the bottom block, and wood planks on top. I'd leave to do some mob killing and I would come back and discover a missing cow. When I see them grow up, they don't suffocate in the wall or something, but when I am gone and suppose they grow while I'm away, they disappear. There are no drops or evidence of them dying, but they could be despawning.

### Comment 27: migrated (2014-08-12T21:51:36.079-0700)

If your animal can walk a straight 20 blocks in any direction it will despawn. My issue appears to be fixed as of the last update, no more dead chickens! However I now have new issues I didn't have before, ones that were supposedly fixed with this update are now causing ME trouble. WTF

### Comment 28: migrated (2014-10-19T08:10:00.307-0700)

Animals randomly suffocate or appear outside the fence/solid block even when they are already grown.
It's really annoying. I have to breed my animals 2 times a day to prevent extinction.

### Comment 29: migrated (2014-10-19T10:21:19.695-0700)

It appears to be a bug in the loading of the coordinates of the mobs. I did a test in my survival world; I had cows in an underground area, so they were in an area encased by stone. When I logged back in, every single time (as I could see through parts of the world as it was loading, and entities always render before blocks), I saw that they were being damaged. Then, at another time, I had them above ground, enclosed with fences. When j logged back in, or came back from the Nether, some would be outside of the fences. So, I thinkmors a problem in their coordinate locations. Like off by a block, or they can walk through blocks for a bread moment upon loading, then die, or escape like with fences...

### Comment 30: migrated (2014-10-19T11:28:56.376-0700)

So this bug appears when entitles are rendering, nevermind if you've just started the server, logged in or came back from a journey. Please fix it ASAP

### Comment 31: migrated (2014-10-19T11:32:42.200-0700)

But it doesn't appear to happen with Item Frames, which are also entities

### Comment 32: migrated (2014-10-20T10:52:32.267-0700)

Because they kinda cant move

### Comment 33: migrated (2014-10-20T11:15:39.809-0700)

My guess is the problem is related to rounding errors and/or the hit box of the mobs.
Probably what happens is their location gets saved with a very precise floating point number and then when the chunk they're in gets re-loaded, that number gets rounded to something less precise and the mob is moved and they end up in a solid block or on the other side of a fence. The other thing could be that their hit box overlaps with other mobs and there's some sort of algorithm which attempts to keep all mobs a certain distance apart and their location is put to one of those unfavorable locations. The problem could also be a problem of those two things.
Just my two cents.

### Comment 34: migrated (2014-10-21T08:38:42.028-0700)

There might be many reasons. That should be fixed ASAP

### Comment 35: Michael Wobst (2015-10-30T11:27:59.966-0700)

Can this be confirmed 1.8.8 onwards? Should consider closing this bug for now until someone can confirm this with a more recent version.

### Comment 36: migrated (2015-10-30T11:30:11.927-0700)

Confirmed.

### Comment 37: migrated (2015-11-17T05:06:16.901-0800)

I have seen this also in 15w46a

### Comment 38: migrated (2016-03-18T02:47:26.143-0700)

This also happens with villagers.

### Comment 39: migrated (2016-06-21T10:54:03.260-0700)

Pigs, Cows, Chicken.... all disappearing frequently. I filled the whole ground of my enclosures with Hoppers to see wether they are despawning or dying.
Hoppers are filling with meat, leather, etc. so it seems they are indeed dying.
Pretty annoying... hope this gets fixed soon
After there was invested so much time to add many new features recently, I hope you will now get rid of some of the ancient nasty bugs like this one

### Comment 40: Michael Wobst (2016-11-01T11:17:46.927-0700)

Is this still an issue in the most recent versions (currently that is 1.10.2, or 16w43a) of Minecraft? If so, please update the affected versions and help us keeping this ticket updated from time to time. If you are the owner/reporter of this ticket, you can modify the affected version(s) yourself.

### Comment 41: migrated (2017-01-02T08:21:53.130-0800)

I can confirm that this is still an issue in 1.11.2.

### Comment 42: migrated (2017-09-24T14:50:23.700-0700)

Pokechu22 helped point out the code where mobs are resized. It happens in EntityAgeable.java in "setScale" (MCP code). This line is called when a mob changes size to an adult. This then calls a method "setSize" (MCP code) in Entity.java where the size is changed. Studying the code it shows clearly that the resizing is done in a very odd fashion.
If the resizing is done towards smaller then the entity simply shrinks without problems keeping the centre position as the reference point, no problems observed. If it's done towards expanding then its done differently and is the reason this problem happens. The expansion strictly expands the current hitbox towards the positive axies as shown here

```this.setEntityBoundingBox(new AxisAlignedBB(axisalignedbb.minX, axisalignedbb.minY, axisalignedbb.minZ, axisalignedbb.minX + (double)this.width, axisalignedbb.minY + (double)this.height, axisalignedbb.minZ + (double)this.width));```
"axisalignedbb.minX + (double)this.width". After the hitbox is resized its moved back by the total width amount.

```this.moveEntity(MoverType.SELF, (double)(f - this.width), 0.0D, (double)(f - this.width));.```
Basically moved back by a full expanded amount.
Two observed issues that can be seen by this is
A. The mob expands and shifts its original position.
B. As illustrated in the picture some edge cases results in mobs never being moved properly back and placing them inside other blocks.
https://i.imgur.com/DpP41Mf.png

### Comment 43: migrated (2017-09-24T15:18:38.182-0700)

The proposed fix is to simply change the size of the hitbox based on the centre position. Then check if the entity is overlapping any other hitbox. If its overlapping any other hitbox it should move the entity back out but only by first checking if its not overlapping with the old hitbox (the last check is to make sure that entity's aren't moved out of blocks they were previously occupying).
These two images shows a code proposal.
https://i.imgur.com/8sVcGr2.png
and
https://i.imgur.com/tdyxPtR.png

### Comment 44: migrated (2017-10-02T08:00:26.829-0700)

I had some issues with escapees syill when trying out the code provided by Xcom. I've built on his idea and come up with the attached. The screenshot shows a pen with a mix of iron bars, cobblestone walls, and full blocks in a ring shape, and all of the cows in the pen started as baby variants. I've managed to reproduce this a few times with various combinations of blocks without any animals escaping thus far.
The changed code first sends "null" as the first argument to "this.world.getCollisionBoxes" to prevent it sending nearby entity collision boxes. After that it walks through the list of all block collision boxes that intersect the new entity collision box that did not intersect the old one. It then checks the X and Z axis independently, and if the new collision box collides with the block collision box it moves the new entity collision box in the direction opposite of the relative position to the old entity collision box on that axis only if the old entity collision box completely clears the block collision box on that axis.
It's a bit of a mouthful, but it seems to work.

### Comment 45: migrated (2018-06-18T17:02:31.816-0700)

Affects 1.13-pre2

### Comment 46: migrated (2019-03-20T17:00:13.086-0700)

19w12a

### Comment 47: Tinsel (2020-03-18T15:03:06.114-0700)

In 20w12a

### Comment 48: numeritos (2020-06-24T03:24:13.155-0700)

Affects 1.16

### Comment 49: numeritos (2020-07-02T02:00:09.964-0700)

Affects 1.16.1 and 20w27a

### Comment 50: pulpetti (2020-07-16T14:51:21.870-0700)

Affects 20w29a

### Comment 51: Avoma (2020-12-01T09:51:53.751-0800)

Can confirm in 20w48a.

### Comment 52: Avoma (2020-12-24T03:12:15.573-0800)

Can confirm in 20w51a.

### Comment 53: migrated (2021-01-20T08:17:19.169-0800)

Not fixed in 21w03a

### Comment 54: migrated (2021-01-21T02:55:12.329-0800)

Indeed not fixed in 21w03a: Ilmango's snapshot video

### Comment 55: migrated (2021-01-29T13:46:45.509-0800)

Confirm for 20w51a

### Comment 56: migrated (2021-01-29T14:07:19.834-0800)

I have been subscribed to this bug for a VERY long time now..

How is it that it has been marked resolved twice now but not actually resolved ?
From the various videos it isn't hard to reproduce / test?
xisumavoid 21w03a https://youtu.be/P7PncU3lLfI?t=546

### Comment 57: slicedlime (2021-01-31T23:45:23.782-0800)

Please do not comment on the issue tracker if you do not have additional information to add.

### Comment 58: ISRosillo14 (2021-02-03T10:46:59.371-0800)

Not fixed in 21w05a

### Comment 59: migrated (2021-02-03T11:28:29.764-0800)

Can confirm, indeed still not fixed in 21w05a.

### Comment 60: Panda4994 (2021-02-03T13:07:33.562-0800)

Thank you for testing this!
When reproducing it in 21w05a, can you confirm that the mobs are not glitched into the blocks before growing up already?
I can currently only get the mobs to grow up into blocks or suffocate if
a) the mobs are partially inside blocks already or
b) there is not enough space to grow into.
For a) the conditions that lead to the mob already being inside blocks should be their own reports. I'm not sure what to do with b), but it at least shouldn't be part of this report.
If it still happens without a) or b) being the reason it would be great to get more precise reproduction steps, like the exact entity coordinates and block configuration.

### Comment 61: migrated (2021-02-03T14:27:48.700-0800)

@[Mojang] Panda
In my previous comment (link to comment) I linked to a video showing this bug happening. From what I can see neither A nor B is the reason that this is happening.

### Comment 62: tryashtar (2021-02-03T22:57:00.925-0800)

According to the updated video that issue is indeed fixed: https://youtu.be/syRAo-I_600?t=938

### Comment 63: migrated (2021-02-04T00:44:59.998-0800)

But it seems like it introduced a new performance issue along with the bug fix: https://youtu.be/H8PZgqm7fGc?t=678

### Comment 64: migrated (2021-02-04T06:46:32.419-0800)

Seems to depend on how close they are near the wall. If they are very close, they can still suffocate.
 If the mob is further away from the wall, it will move away from wall when growing up, preventing it from suffocating. Command I was using is

```/summon pig 112.82 78.00 158.25 {Age:-5}```

### Comment 65: Panda4994 (2021-02-04T07:29:17.434-0800)

If you summon it with a large negative age you can also push it into the wall before it growing up? I think baby pigs are 0.45 wide, so if it's at 0.82 that puts the side of it's AABB at 1.045, slightly into the wall.

### Comment 66: Avoma (2021-02-05T12:05:47.792-0800)

Can confirm in 21w05b.

### Comment 67: slicedlime (2021-02-08T00:07:31.724-0800)

If there are new issues introduced, please post new issues.

### Comment 68: migrated (2021-02-19T11:55:39.251-0800)

Affects 21w07a

### Comment 69: ampolive (2021-06-07T06:31:35.551-0700)

Affects 1.17 Release Candidate 1 per MC-227605.

### Comment 70: Avoma (2021-07-18T02:30:34.466-0700)

Can confirm in 1.17.1.

### Comment 71: migrated (2021-10-08T10:08:29.849-0700)

I noticed while trying to make a fox powered chicken cooker that this bug does not often happen for me under normal circumstances, however if there is a carpet on top of a slab that the chicken is growing up into, it moves into the wall and suffocates. the chicken is safely not suffocated if it merely grows up on a slab in an enclosed space without a carpet.
even with one chicken, it still gets shoved into the wall
EDIT: it appears that this is the case not only for carpets, but for mostly any block being above the slab the animal grows up on. it makes them move into the wall

### Comment 72: DLSDUFER (2022-04-09T19:51:54.590-0700)

Is this still an issue? Since I cannot reproduce it, although in my survival world, there is something going on with my animals, still researching and testing.

### Comment 73: migrated (2022-05-07T16:27:24.307-0700)

Cows growing up inside a 1x7 space teleport through the walls. They don't seem to suffocate as often as they just pop out the other side.

### Comment 74: NBG-bootmgr (2022-07-05T21:30:05.214-0700)

Can confirm in 1.19.1-pre2.

### Comment 75: NBG-bootmgr (2022-07-07T08:12:54.161-0700)

Can confirm in 1.19.1-pre3.

### Comment 76: Brevort (2023-04-06T20:02:52.504-0700)

Can confirm in 23w14a. This is extremely severe for frogs. They don't even try to escape the block they are stuck in and usually just die of suffocation.

### Comment 77: migrated (2024-05-10T16:45:49.579-0700)

i see this a lot whenever i breed a bunch of cows in fences. i'll get cows roaming around outside the fences because the children grow up near the fence and phase through it.

### Comment 78: tryashtar (2024-05-10T17:58:28.235-0700)

Is this really fixed?
EDIT: the pushing out seems to work okay when the mob is squished properly against the wall, with no suffocation. I think the change was just for tadpoles

### Comment 79: Panda4994 (2024-05-13T01:52:51.429-0700)

This report collected a lot of dust over the years.
The core of the issue has been fixed a while back, but it got reopened with changed repo steps.
So this time it was fixed according to the repo steps. Chickens did suffocate when spawned from eggs, because they would end up slightly in blocks. That's fixed, spawning chickens from eggs no longer does that.
Addionally MC-253791 (the frogs) and MC-252846 are fixed. Both were issues that were hidden in the duplicates of this issue and .
Which brings me to the reason for my little rant: If there is new repos for suffocating mobs showing up, please make sure this issue is not reopened, but they are reported as new issues. Otherwise easy to fix issues can get lost behind lots of outdated information of old reports. Thank you! (and thank you for testing if the fix worked!)
