# MC-158205: Ender Dragon doesn't take damage from melee attacks unless hit a certain way

**Mojira URL:** [https://bugs.mojang.com/browse/MC-158205](https://bugs.mojang.com/browse/MC-158205)

## Report details

- **Mojira categories:** Combat; Entities; Hitboxes
- **Project:** MC
- **Issue key:** MC-158205
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2019-08-01T10:07:09.076-0700
- **Updated:** 2025-04-26T08:21:31.953-0700
- **Resolution date:** 2024-10-30T11:15:08.532-0700
- **Affects versions:** 1.14.4; 1.15.2; 20w06a; 20w09a; 20w11a; 20w22a; 1.16 Pre-release 8; 1.16.2; 1.16.3; 1.16.4; 20w45a; 20w46a; 20w51a; 1.16.5; 21w08a; 21w18a; 1.17 Pre-release 3; 1.17; 1.17.1 Pre-release 1; 1.17.1; 21w38a; 21w42a; 1.18 Pre-release 1; 1.18; 1.18.1 Pre-release 1; 1.18.1; 1.18.2; 22w12a; 22w16b; 1.19 Pre-release 2; 1.19 Pre-release 4; 1.19; 1.19.2; 1.19.3 Pre-release 2; 1.19.3 Pre-release 3; 1.19.3; 1.19.4 Pre-release 3; 1.19.4; 23w18a; 1.20 Release Candidate 1; 1.20; 1.20.1; 23w31a; 23w32a; 1.20.2 Release Candidate 2; 1.20.2; 23w40a; 23w43a; 1.20.4; 23w51b; 24w05b; 24w06a; 24w07a; 24w14a; 1.20.5 Pre-Release 1; 1.20.5; 1.20.6 Release Candidate 1; 1.21
- **Fix versions:** 24w44a
- **Area:** Platform
- **Votes:** 2
- **Watchers:** 1
- **Attachments:** 11
- **Attachment filenames:** 2021-02-24_17.53.32.png; 2021-02-24_17.53.33.png; 2021-02-24_17.53.35.png; 2021-02-24_17.54.02.png; 2021-02-24_17.54.18.png; center_hit-2.png; center_miss.png; hit.png; image-2021-06-18-19-26-40-879.png; image-2021-06-18-19-30-26-902.png; miss.png
- **Issue links:** Duplicate:inward:MC-274526:EnderDragonPart Entity ID Desync | Relates:outward:MC-269611:Not capable of performing critical attacks against ender dragons | Duplicate:inward:MC-201938:Ender Dragon hitbox is broken after 19w08b | Duplicate:inward:MC-155798:Dragon can only sometimes be damaged with diamond sword | Duplicate:inward:MC-190275:Ender Dragon is immune to damage while sitting on the Fountain | Duplicate:inward:MC-174590:Cannot hit Ender Dragon with Sword at the back section of the body | Duplicate:inward:MC-156522:Ender Dragon Hit Boxes Prevent Damage/ Only Damagable in Close Range | Duplicate:inward:MC-160262:The Ender Dragon can not be attacked with sword.

## Description

When fighting the ender dragon, melee attacks sometimes don't register at all.
On the middle hitbox where the torso is ubicated, hits don't register from the center of the model towards the tail. Instead, they are only registering near the head, and only on certain weird angles. From what i've seen, the other hitboxes where the head and tail are located seem to be unaffected. Another important thing to say is that wings don't ever register hits (more info in the comments).
Basically, melee attacks done facing to the back or middle of the model don't register, seems to depend on the dragon's or player's position. Arrows however, always register.
Code Analysis
Code analysis by  can be found in this comment.
This issue appears to be caused by two root problems:
- There is a desync between client and server for entity IDs for the small hitboxes the dragon is composed of due to an off-by-one error (see MC-274526)

- The hit detection used by the game does not account for the fact that due to its size, the dragon entity can be located in a chunk the player is not looking at (see MC-261638, also affects other entities with large hitboxes)

## Comments (36)

### Comment 1: migrated (2019-08-01T10:07:09.076-0700)

This comment contained multiple image attachments (11), please login to view the attachments.

### Comment 2: migrated (2019-08-01T15:05:48.918-0700)

this is intended the dragon will not be able to take damage for part of the landing stage of the fight

### Comment 3: migrated (2019-08-21T16:08:10.228-0700)

Try to get underneath it

### Comment 4: migrated (2019-12-03T10:55:50.424-0800)

Can confirm. The hitbox is buggy and weird. This also happens even when the dragon is not on the nest. Trying to fight it with a sword (for example by chasing it with elytra) is almost impossible as the hits don't register correctly. When you hit the dragon, the weapon makes a sound and you can see particles if the weapon is enchanted (see pictures), but no damage is dealt. I've seen videos where people were very frustrated by this, as it feels inconsistent and buggy when compared to how hits normally work.

### Comment 5: gaspoweredpick (2020-03-03T21:49:26.121-0800)

Confirmed. The ender dragon isn't taking damage from places it did before.

### Comment 6: SeaOfPixels (2020-03-03T22:01:51.525-0800)

Not to mention the way the dragon descends to the fountain is bugged

### Comment 7: syarumi (2020-08-11T17:04:41.490-0700)

Can i request ownership? user's last activity was august 2019.

### Comment 8: migrated (2020-08-12T01:41:34.223-0700)

in 1.15.2 there could be the problem where the dragon doesn't change state correctly, it will never activate the landing sequence.

### Comment 9: syarumi (2020-08-12T18:05:14.755-0700)

Ric, if you want the ticket back you can ask a mod and i'll accept, i just requested ownership to keep updating the affected versions. And about the dragon hitboxes, that's probably being tracked as .

### Comment 10: FaRo1 (2020-08-22T09:27:06.464-0700)

Seems like only the head and tail hitboxes work properly, the torso works sometimes, I couldn't really figure out when. The wing hitboxes don't seem to work at all.
(Confirmed in 1.16.1, but that doesn't help.)

### Comment 11: migrated (2020-09-27T13:46:17.508-0700)

This seems very inconsistent. I have killed the dragon 3 times in the same game (survival, 1.16.2). The first two times the fight went normally. The third time, I hit the dragon once with my sword, and after that no further melee hits registered. I had to finish the fight using only bow and arrows.
Edit: 4th fight
I upgraded my game to 1.16.3 and set up another dragon fight. Initially my sword did damage, but then it stopped when hitting the rear end. Hitting near the front seemed to work a little longer. I re-logged mid-fight and the sword started working again briefly, before stopping again. After a second re-log the sword came back to life and I finished the fight.
Edit #2: Subsequent Fights
I have now killed the dragon 4 more times. Most of the time the fight proceeded normally. A couple of occasions hits from the sword stopped working. I used the workaround, wait til the dragon sits on the pedestal, re-log and then continue. Worked every time.
TLDR: this seems to be an intermittent problem. A (risky) workaround is to re-log while the dragon is on top of the pedestal.

### Comment 12: SeaOfPixels (2020-10-12T10:09:25.882-0700)

These are the kinds of major bugs that baffle me when they're not fixed asap, while other trivial bugs are prioritized.

### Comment 13: SeaOfPixels (2020-11-07T22:40:44.872-0800)

**Can confirm this bug first appeared in 19w08b, alongside many other serious bugs with the Ender Dragon that are still in the latest version. These issues include its hitbox, the way it descends to the fountain, and just its AI in general.

### Comment 14: insane96mcp (2021-06-18T08:49:02.563-0700)

I'm pretty sure there's some kind of desync problem as sometimes when in creative you try to hit her (melee) you can't (with a weapon you see the Sharpness particles but no hit is registered).

EDIT: Found out MC-225055

### Comment 15: insane96mcp (2021-06-18T10:28:33.991-0700)

With mods magic I've managed to summon at the actual position of the ender dragon's parts (head, neck, wings and tail) some angry villager particles. (Tested in singleplayer) As you can see the client sees the dragon there (both hitboxes and actual model) while on the server she's ahead.
The tail parts:

### Comment 16: insane96mcp (2021-06-18T13:23:13.696-0700)

Finally after two hours of debugging I've found out why you can't hit the dragon sometimes. It has to do with where the dragon is (chunk wise) and where you're aiming at.
But first off, why can't you hit wings? Seems like they're swapped between client and server. So if right wing has Entity ID 1 and left wing has Entity ID 2 on the client, for the server it'll be Entity ID 2 for the right wing and Entity ID 1 for the left wing. With this the server thinks that you're hitting the far away wing so since there's a max range for the hit of 6 blocks you can't reach it and so the hit is registered on the client (MC-225055) but not on the server.
For the problems about not hitting her at all is a little bit more complicated.
The problem arises when you aim at any of the dragon's part: if you're aiming at the chunk in the direction where the center position of the dragon is you'll hit her, otherwise the hit will miss, that's because the ender dragon is not found in the chunks you're raycasting in so the hitboxes aren't checked at all.
Let's make an example.
Here the player, the ender dragon's head hitbox and the ender dragon position are all in chunk 0,0. When the player tries to hit the Ender Dragon's head he searches for the Ender dragon in Chunk 0,0 and -1,0 (the direction looking). The dragon is found in 0,0 so raycasts are made to find the head and in the end (pun intended), the attack lands, dealing damage to the dragon.
In this case the hit will not land as the Ender Dragon is searched for in chunks -1,0 and -1,-1, but she's in 0,0 thus not found, the finding of the head is not done and the hit fails.
"Why most of the times I can hit her while in the portal?"
Because the raycast actually starts from 2 blocks behind the player so most of the times 0,0 will be searched for the dragon.
While in this case your hitbox doesn't load 0,0 so the dragon is not found and the hits will not land

Note that in the examples the Ender Dragon center position is always in 0,0 but can be in any of the 4 chunks when slightly off.

### Comment 17: migrated (2021-10-27T07:21:50.933-0700)

Affects 21w42a

### Comment 18: migrated (2021-11-04T05:55:15.130-0700)

Maybe this issue is relative with that?
https://github.com/MinecraftForge/MinecraftForge/issues/8188

### Comment 19: SeaOfPixels (2022-11-30T02:50:49.902-0800)

Can confirm in 1.19.3 pre3. I think you should add to the report that this bug (as well as other ender dragon bugs like its fountain descent and pathfinding) all appeared due to a fix in 19w08b.

### Comment 20: SeaOfPixels (2023-05-04T03:43:13.613-0700)

Can confirm in 23w18a.

### Comment 21: SeaOfPixels (2023-06-07T05:03:46.014-0700)

Can confirm in 1.20 release canidate 1

### Comment 22: SeaOfPixels (2023-06-13T07:11:20.077-0700)

Can confirm in 1.20.1

### Comment 23: SeaOfPixels (2023-08-03T00:26:04.284-0700)

Can confirm in 23w31a.

### Comment 24: SeaOfPixels (2023-08-17T00:06:13.472-0700)

Can confirm in 23w32a.

### Comment 25: SeaOfPixels (2023-09-30T00:05:48.265-0700)

Can confirm in 1.20.2

### Comment 26: SeaOfPixels (2023-10-05T09:07:24.264-0700)

Can confirm in 23w40a

### Comment 27: SeaOfPixels (2023-10-26T03:05:18.390-0700)

In 23w43a.

### Comment 28: SeaOfPixels (2023-12-31T03:45:03.025-0800)

Can confirm in 23w51a/23w51b

### Comment 29: SeaOfPixels (2024-02-07T09:36:05.614-0800)

Can confirm in 24w06a, affects wind charges

### Comment 30: SeaOfPixels (2024-02-14T15:13:12.763-0800)

Confirmed in 24w07a

### Comment 31: syarumi (2024-02-14T18:55:46.834-0800)

Just a reminder, you don't need to comment "affects version" everytime there's a snapshot out, you'll just spam emails to those watching the issue. Just confirm an affected version when there's a significant change or bugfix that could be related to this bug.

### Comment 32: SeaOfPixels (2024-04-04T11:22:10.459-0700)

This is also a parity issue with Bedrock Edition (also can confirm in the latest versions).

### Comment 33: SeaOfPixels (2024-04-13T05:25:07.059-0700)

Confirmed in 1.20.5 pre1

### Comment 34: SeaOfPixels (2024-04-26T06:45:41.722-0700)

{*}{*}Can confirm in 1.20.6-rc1

### Comment 35: [Mod] violine1101 (2024-07-19T08:38:30.872-0700)

I've added a brief summary of the findings by  and from MC-274526 to the description.
The second issue with the raycast not working properly does not only affect the ender dragon but large mobs in general. With the recently added scale attribute, it is easily reproducible with other mobs too. I'll file a separate bug report about this for that reason. This has already been reported here: MC-261638.

### Comment 36: SeaOfPixels (2024-10-30T11:14:52.526-0700)

Relates to MC-271337, both issues appeared first in 19w08b.
