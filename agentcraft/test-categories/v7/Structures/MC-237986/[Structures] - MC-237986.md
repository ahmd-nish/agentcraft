# MC-237986: Mobs specific to structures aren't spawning in their structures

**Mojira URL:** [https://bugs.mojang.com/browse/MC-237986](https://bugs.mojang.com/browse/MC-237986)

## Report details

- **Mojira categories:** Mob spawning; Structures
- **Project:** MC
- **Issue key:** MC-237986
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2021-09-30T00:38:25.834-0700
- **Updated:** 2025-04-30T06:41:35.747-0700
- **Resolution date:** 2022-10-17T13:42:22.606-0700
- **Affects versions:** 21w39a; 21w40a; 21w41a; 21w42a; 21w43a
- **Fix versions:** 21w44a
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 2021-11-04_11.23.03.png; Screenshot (35).png; Screenshot (36).png
- **Issue links:** Duplicate:inward:MC-238260:Pillagers not spawning at outpost, guardians not spawning in monuments, mob heads twitching

## Description

The Bug
Mob spawns specific to structures like Witches in Witch Huts & Guardians to Monuments aren't spawning there anymore
Affected Structures
- Monuments

- Witch Huts

- Pillager Outposts

Reproduce
- Create a new world

- Do /locate on any of the structures listed above

- Teleport there
 Notice none of the mobs spawn

Expected Result
The mobs spawns specific to those structures would spawn as normal
Original Description
I have found that mobs other than witches are spawning in witch huts. This is a newly created world and has not existed in any other versions.
As you can see in the pictures, I have been careful to only include the spawning area of the hut in the setups pictured. I was in creative mode. I hovered 115 blocks above the hut during the day to get these results.
There are also problems with witch farms migrated from 1.17.1.
One possible reason is the large distance from spawn that this location is in (>20 million). However, this did not cause issues in the world migrated from 1.17 before it was brought to the latest snapshot.
This is happening in two worlds - one freshly generated and one brought from 1.17. They are both on the same seed.

## Comments (37)

### Comment 1: migrated (2021-09-30T00:38:25.834-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: ampolive (2021-09-30T14:33:12.669-0700)

Relates to MC-238002.

### Comment 3: anthony cicinelli (2021-09-30T21:08:18.713-0700)

I can confirm this affects more than Witch Huts though. I've updated your report to reflect this

### Comment 4: MMK21 (2021-10-01T05:41:01.374-0700)

Could be related to structure bounding boxes not being upgraded properly

### Comment 5: ampolive (2021-10-01T10:41:04.047-0700)

I don't think that is the case, because newly created worlds are also affected by this bug.

### Comment 6: migrated (2021-10-05T08:32:01.382-0700)

Woodland mansions have no post-generation special mob spawning (AFAIK).

### Comment 7: tqz78 (2021-10-07T08:01:39.654-0700)

Can confirm in 21w40a.

```Seed: -4910909757403150144
Coords: -474 76 -2878```
Edited to enclose seed and coords in code.

### Comment 8: migrated (2021-10-08T09:45:49.215-0700)

I have the same issue in newest snapshot. I noted the coords of an ocean monument in 1.17 with datapack, and I know it generated the chunk at that time, and when I went there the other day there were no Guardians, only Elder Guardians.

### Comment 9: migrated (2021-10-10T13:24:19.973-0700)

I tested this on two newly created worlds in 21w40a - I have screenshots of two pillager outposts with no pillagers spawning and no iron golums in cages.

### Comment 10: tqz78 (2021-10-13T09:14:30.974-0700)

Can confirm in 21w41a.

```Seed: -4910909757403150144
Coords: -13 73 -2979```
The world is different due to the new random number generator implemented in this snapshot.

### Comment 11: migrated (2021-10-13T10:07:17.931-0700)

In 21w41a, I found a golem at an outpost, and elder guardians at a monument, but no pillagers or guardians.

### Comment 12: migrated (2021-10-13T14:48:28.468-0700)

Yes still happening in 21w41a

### Comment 13: migrated (2021-10-17T08:09:46.211-0700)

This may be unrelated, but pandas seem to not spawn as well.

### Comment 14: Mr_Quasi (2021-10-17T08:22:04.398-0700)

That's correct, pandas aren't spawning either. See this bugreport: MC-236689

### Comment 15: migrated (2021-10-17T08:30:44.445-0700)

Are Bastions not working properly aswell? Cause i have a sneaking suspicion only the initially placed piglin brutes appear there but no additional ones spawn after you kill all of them.

Or maybe it's just my luck.

### Comment 16: Sniper1.1 (2021-10-17T12:04:00.750-0700)

Piglin brutes only spawn once. Quoting the wiki: “A small number of piglin brutes spawn in bastion remnants only upon generation and in some rooms.”

### Comment 17: migrated (2021-10-17T12:25:38.109-0700)

What the heck? I could have sworn i see Piglin brutes re-appearing in same bastion i visited several times and cleared on 1.16 (It was my source of blackstone bricks)

### Comment 18: Sniper1.1 (2021-10-17T12:42:33.288-0700)

Interesting. Maybe normal piglins respawn but not brutes and you’re misremembering? I really don’t know.

### Comment 19: migrated (2021-10-17T13:11:42.307-0700)

Hmm maybe.

### Comment 20: Mr_Quasi (2021-10-20T09:08:44.088-0700)

Can confirm for 21w42a

### Comment 21: migrated (2021-10-21T12:41:37.571-0700)

In seed 5262073205950916288 at coordinates 201/-2276 in 21w42a, I found a pillager outpost with a golem but no pillagers... I hope it can help.

### Comment 22: migrated (2021-10-21T22:19:20.203-0700)

A patch to fix it: https://github.com/Linkin-Lab-Server/FIX-MC-237986

### Comment 23: Ceresjanin123 (2021-10-24T05:03:00.126-0700)

This is probably caused by reccurence of

### Comment 24: migrated (2021-10-24T10:32:37.326-0700)

But this happen for new worlds as well.

### Comment 25: Mr_Quasi (2021-10-24T11:48:10.728-0700)

It's strange that Elder guardians are spawning, maybe because they come with the structure when the world generates? Eitherway, a very important bug that still is not assigned...

### Comment 26: MMK21 (2021-10-24T13:15:50.527-0700)

Elder Guardians don't spawn post-generation

### Comment 27: migrated (2021-10-27T12:07:49.870-0700)

Can confirm for 21w43a, for the following structures and mobs:
- Ocean Monuments (Guardians do not spawn, Elder Guardians do)

- Pillager Outposts (Pillagers do not spawn, Iron Golems might, Pillagers do spawn in raids, I'm not sure if patrols still occur)

What DOES work:
- Bastion Remnants (Both Piglins and Piglin Brutes spawn, as well as Hoglins in Hoglin stables)

- End (The Ender Dragon spawns, as do the pillars with Ender Crystals)

- End Cities (Shulkers spawn)

- Fortresses (Zombified Piglins, Wither Skeletons, Blazes, and Magma Cubes all spawn)

- Igloos with Basements (both a Villager and a Zombie Villager spawn)

- Mansions (Vindicators and Evokers both spawn)

- Ocean Ruins (Drowned spawn)

- Raids (Vindicators, Evokers, Witches, Pillagers, and Ravagers can all spawn)

- Swamp Huts (Both a Witch and a black Cat spawn)

- Villages (Villagers spawn)

Grey Areas:
- Shipwrecks (I could swear Drowned spawn here before, but I might be mistaken)

### Comment 28: migrated (2021-10-27T13:48:05.761-0700)

The initial witch + black cat do spawn in witch huts as they are part of initial generation. The witches that should continue to spawn in witch huts as part of normal mob spawning cycles however do NOT spawn. Fortresses might only be spawning fortress specific enemies due to the rule about fortress enemies spawning on nether brick anywhere in the nether, while the fortress bounding box itself isn't doing anything. It would be good to verify which is occurring.

### Comment 29: migrated (2021-10-28T09:56:19.178-0700)

Also while not really caused by bug but still somewhat related. Would it be possible that something is done about Dark Forests aswell?
No hostile mobs are able to spawn during daytime there anymore because the light level is not low enough anymore.
Which is a shame the concept of Dark Forest being unique and dangerous having mob spawn even during daytime was pretty much erased with the new light level changes.

### Comment 30: migrated (2021-10-28T10:52:17.957-0700)

@Martin The changes to spawning based on light are only for block light, not sun light. Dark forests should still be able to spawn monsters during the day, however they are less likely to do so given the huge amount of caves underground basically filling up the mob cap. With so many more places for mobs to spawn, mobs are much less likely to spawn in any given spot. There definitely should be some tweaks to the mob cap, but also this is most definitely unrelated to this specific ticket.

### Comment 31: migrated (2021-10-28T12:14:02.062-0700)

@Peter Rabbit
I only know that so far Dark Forests are pretty much devoid of any hostile mobs during daytime for one reason or another. Personally i never encountered a single hostile mob so far in Dark Forests during daytime. (During night time they spawn normally there and everywhere else so not 100% sure if this is cave size related.)
While in 1.16.5 they were pretty plentiful there.
But yea you are right that's a talk for a different topic.

### Comment 32: migrated (2021-11-02T10:59:14.423-0700)

Ok yea something is definatley wrong with Dark Forests.
Mobs do not spawn under the canopies during daytime anymore on the snapshots.
This is not a mob cap issue cause i made sure nothing else spawned under me.

It acts like Sky Light level counts and not just Block Light and Sky Light cannot ever reach 0 in Dark Forests probably why absolutely no hostile mobs are ever able to spawn there during daytime.
Areas below sky light level 7 don't seem to work when spawning enemies. It must be Sky Light 0 for enemies to properly spawn now.

Dark forests work fine on 1.16.5 and 1.17.1 for example. Hostiles spawn properly in Dark Forests during day.

So if the light level changes for mob spawning supposed to by only for Block Light than its clearly not working as intended. Not sure if i should make a separate report or does this qualify as part of this bug report?

### Comment 33: migrated (2021-11-02T22:47:11.789-0700)

@Martin If sky light spawning was changed, then that is a bug based on what Mojang has communicated, in which case you should open a new ticket for that (as this bug is specifically for structures not generating structure specific enemies in their bounding boxes, which is entirely different)

### Comment 34: migrated (2021-11-04T11:27:09.836-0700)

This is still not fixed for me. Loaded up world generated in 1.17  in a chunk from 1.17.1  and witch hut still only spawning normal mobs

### Comment 35: migrated (2021-11-04T11:40:08.778-0700)

I'm on 21w44a and a monument which was generated in 21w43a is spawning guardians just fine. Maybe there is a bug with migrating structures in the world save data?

### Comment 36: migrated (2021-11-04T12:32:10.299-0700)

The bug for that issue is MC-240507

### Comment 37: migrated (2022-10-17T13:42:22.606-0700)

how exactly does it work?
