# MC-80032: Horses can suffocate when going through nether portals

**Mojira URL:** [https://bugs.mojang.com/browse/MC-80032](https://bugs.mojang.com/browse/MC-80032)

## Report details

- **Mojira categories:** Hitboxes
- **Project:** MC
- **Issue key:** MC-80032
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2015-05-02T06:59:37.121-0700
- **Updated:** 2025-04-30T04:43:58.063-0700
- **Resolution date:** 2023-04-26T07:55:35.564-0700
- **Affects versions:** Minecraft 1.8.4; Minecraft 1.9 Pre-Release 4; Minecraft 1.9; Minecraft 1.9.1 Pre-Release 2; Minecraft 1.9.1; Minecraft 1.9.2; Minecraft 1.9.4; Minecraft 1.10.2; Minecraft 1.11; Minecraft 1.11.2; Minecraft 1.12.1; Minecraft 1.12.2; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 19w11b; Minecraft 1.14.1; 1.15 Pre-release 1; 1.15.2; 20w07a; 1.16.3; 1.16.5; 22w15a
- **Fix versions:** 20w28a; 22w45a
- **Area:** Expansion B
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 2016-08-10_02.14.08.png; 2016-08-10_02.14.20.png; Minecraft 1.16.2 - Singleplayer 2020-09-02 18-00-00.mp4
- **Issue links:** Relates:inward:MC-262115:Large hitbox mobs having inconsistent exit position and can suffocate in surrounding blocks depending on some factors | Relates:inward:MC-13734:Horses - Killed With Nether Portal | Duplicate:inward:MC-97868:horses die when traveling through Nether Portals | Duplicate:inward:MC-116939:Horse takes damage from nether portal frame | Duplicate:inward:MC-166314:Entities with big hitbox often die in portals | Duplicate:inward:MC-173224:horses suffocate when going into nether portal | Duplicate:inward:MC-214929:Donkey with chest full of items traveled through portal, suffocated, died, left no items | Duplicate:inward:MC-250230:Horse suffocated when going through a nether portal MC-250228 | Relates:outward:MC-121098:Entering a tall portal that takes you to a short portal from the top causes you to take suffocation damage

## Description

Everytime I push a horse through a nether portal and it comes to the other dimension, it suffocate in obsidian or in surrounding blocks. Sometime, I can't get out of it an dies.
Note that this may actually be three bugs:
- Horses can suffocate from walls because they are partially teleported into them

- Players can push horses into the obsidian wall after portal teleport

- Horse size is not accounted for when placing horse inside the portal (MC-121098)

This ticket only describes the first two bugs, which should be properly tested and split into two tickets at some point.

## Comments (33)

### Comment 1: migrated (2015-05-02T06:59:37.121-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: migrated (2015-07-29T23:37:56.775-0700)

I've had this happen to both horses and villagers.  I keep the walls set far back from the portals now to prevent them landing inside those, but that doesn't help with glitching into the obsidian of the portal frame itself.
It seems to happen more often when transporting multiple through at once (pushing each other into the blocks?) and/or when the portal they enter through is wider than the one they arrive at.  Trying those together might increase the odds of reproducing it.

### Comment 3: migrated (2015-10-08T11:08:08.592-0700)

I'm fairly sure it's because when the nether chunk is loading when you step through, your hitbox pushes the horse into the frame of the portal. This should be impossible - perhaps it's because the horse loads before the surrounding terrain or the horse gets shifted because the game tries to avoid two entities taking up the same location. In any case, it sucks.

### Comment 4: migrated (2016-02-26T12:37:28.380-0800)

I can confirm that this bug has been present in 1.9 Pre 1, 1.9 Pre 2, and  1.9 Pre 3.
Steps to recreate:
1. Tame any horse or donkey.
2. Ride into Nether Portal
3. Dismount (Horse will teleport through portal)
4. Enter portal
5. Horse will be suffocating or dead nearly 100% of the time with traditional 2 wide x 3 high portals.
They appear within frame of portal. Happens both in Overworld > Nether, and Nether > Overworld portals.
6. Horses may still end up within portal frame for larger portals.

### Comment 5: migrated (2016-02-26T12:52:35.020-0800)

Confirmed in Minecraft 1.9 Pre-Release 4

### Comment 6: migrated (2016-03-02T03:38:43.191-0800)

confirmed for the 1.9 as downloaded today (02Mar). horses going through portal receive suffocation damage from the portal frames for the most part. i had this problem in both overworld and nether.

### Comment 7: migrated (2016-03-10T13:05:53.694-0800)

Confirmed in Minecraft 1.9.1-pre2
Created new 1.9.1-pre2 world, tested issue in both directions (Overworld <-> Nether). Horse "materializes" within side frame of portal and suffocates / dies.
This happens 100% of the time with standard portals (the 2 wide x 3 high type.)

### Comment 8: migrated (2016-04-08T20:49:53.041-0700)

Confirmed in latest release (1.9.2).  This happens both when 1) you lead the horse through the portal with a lead, or 2) you ride the horse into the portal and then dismount to initiate transport of the horse.  As near as I can tell, the horse's head seems to enter the obsidian after I travel through the portal following the horse - it seems to occur as a result of my knocking the horse out of the portal itself and into the portal frame. In 1.8.9 this does not happen - I seem to be able to co-ccupy the same space as the horse until it walks out of the portal.
This is a major bug, severely limiting the utility of horses/mules.  One of the main reasons I have mules is to enable rapid transport of myself and materials through the Nether to various remote regions of my world!  Under the current version, I must either build all new (larger) portals, or place mules outside every Nether transport station (like taxis) to handle local transport needs.  Ugh!
Please, please, please figure out how to enable players to ride horses through Nether portals while mounted! This seems like an obvious feature that should have been built into the game since introducing horses into the game in the first place!

### Comment 9: migrated (2016-05-03T06:31:09.114-0700)

Confirmed for me too. This is really infuriating and has never been a problem for me previously. I've had a couple of horses killed by this now when I'm a large distance (through the Nether and Overworld) from anywhere with new horses to be tamed. It's a massive inconvenience and I would agree would be best improved by enabling passage through portals while mounted.

### Comment 10: migrated (2016-06-01T04:36:37.078-0700)

the same happened to me in 1.9.4 vanilla with an iron golem in std 2x3 portal. when you follow your critter through the portal you probably push its hitbox into obsidian

### Comment 11: migrated (2016-06-27T00:18:45.880-0700)

Confirmed in Minecraft 1.10.2.
Just recently happened to me in my survival world.

### Comment 12: migrated (2016-08-09T23:04:45.361-0700)

Confirmed in Minecraft 1.10 and 1.10.2.
Widening portals to 3 or 4 blocks wide lessened the chance that it would happen, but did not eliminate the problem. I generally dismount my horse and then push it into the portal, but have the same problem that the horse spawns on the other side stuck in the obsidian frame potentially dying from suffocation damage if not quickly mounted and moved away. In a related phenomena, I have also had a horse die of suffocation damage while swimming (alone and unmounted) in a small lake. The lake had a dirt overhang in one part and the horse swam under it and got stuck inside the block and suffocated to death. So this seems to be a reoccurring issue with horses and suffocation damage in blocks. I have noticed that the horse seems more likely to get stuck in the obsidian frame of a portal if it is moving while it teleports to the other side. It seems as though the horse keeps moving during transit and walks into a location that is then occupied by the obsidian block when the world loads. Perhaps an error in the movement code for horses?
Possible solutions:
1. Allow player and horse to enter portal together while mounted (may or may not fix error, depending on cause).
2. Remove suffocation damage in solid blocks. Suffocation damage almost always happens as a glitch of some sort. Damage taken from gravel or sand falling onto a player's/entity's location makes sense, or from entering low clearances while on a minecart maybe. But there have been reoccurring issues since beta minecraft of entities dying from block suffocation getting stuck in walls, corners, fences, etc. Furthermore mechanics while riding a horse under low clearance are implemented poorly, especially in jagged terrain. Even just slightly walking over a chest in a room with only a 3 block height will result in this "head" damage, and in caves a player can easily become hopelessly stuck in a wall taking damage with a black screen. It is incurred far to frequently and easily, and furthermore makes little sense. The horse mounted player should be stopped from entering the space rather than magically phasing his head inside a solid rock and then being hurt by it (or, you know, maybe add a head ducking animation). One must ask, for the preponderance of glitches, accidental mob/player deaths, and poorly designed mechanics, what is the purpose for taking damage in this way? The game, in theory, should never allow you or any other entity to phase inside of a solid block in survival mode in the first place, so why punish players because the game made an error?

### Comment 13: migrated (2016-08-09T23:26:52.153-0700)

Horse taking damage inside Obsidian frame after travelling through portal (Survival Server, although I was temporarily in Creative mode to spawn in a horse to sacrafic.)
Second picture show there was open space around the portal (and the same issue has occurred with much larger open spaces than shown here). It is less common with wider portals (i.e. 3x3 in place of standard 2x3) but can still occur. With standard sized portals it seems to occur the majority of the time.

### Comment 14: migrated (2016-12-07T12:53:51.926-0800)

Occurring in 1.11 official release.
Occurrence, every time.
Happens by horse contact with portal and on lead.
Horse appears stuck in obsidian on the side of the portal, quickly right clicking the horse to mount and jumping frees the horse, only if you are fast.
Mode: Survival
Older versions 1.8 and previous were run with the same nether portal configuration and never hit this issue.  There was a falling through the blocks beneath the portal into lava (not fun) in pre-1.8 but not this suffocating condition.

### Comment 15: migrated (2016-12-31T14:58:17.632-0800)

I can confirm this with 1.11.2.
it even happens if you widen the portals on both sides, or if you change the orientation of one/both of the portals.
this is an EXTREMELY annoying bug since good horses are so hard to find/breed and there's seemingly no way to prevent it happening.
please, at the very least, ensure that the hose is oriented so its head is sticking OUT of the portal, and not into the portal block.

### Comment 16: migrated (2016-12-31T18:19:37.466-0800)

If I make the portal opening both in the nether and in the real world 5 blocks wide (blocks you can stand on) / 7x7 including the obsidian, and I make sure I am in the middle block (block 3) when I dismount my horse, it does arrive safely in the other dimension, as long as the destination portal is that same size.
I have an elaborate nether world full of portals, changing to this configuration took more hours than I care to admit.

### Comment 17: gnembon (2017-09-24T09:09:16.703-0700)

Adjusting the offset when spawning the entity in the portal accounting for that entity width would fix the issue. Currently if the portals have different widths exit portal position may cause AABB to intersect with the Obsidian frame. Still even if mobs are placed in the middle of the portal, player can still push them into the obsidian somehow, but that's another story.

### Comment 18: migrated (2017-09-24T10:11:20.476-0700)

Yes. The glitch seems to be caused by player pushing horse. It's intended for horse to bump against obsidian, but collision check doesn't work. Why is that?

### Comment 19: migrated (2017-10-13T02:48:25.764-0700)

Confirmed in 1.12.2.
This is happening consistently and repeatably for me. I've done some testing with another player - whether pushing the horse into the nether, pulling them in with a lead, or just waiting for them to wander in of their own free will, this will happen.
It is also unaffected by whether a player is there on the other side or not - every time we tested this, the horse spawned inside the portal walls on the other side, even if no player was nearby or followed the horse through (I was watching from a distance on the other side as my accomplice sent the horse through the portal).

### Comment 20: migrated (2017-10-31T13:58:27.594-0700)

Still happening in 1.12.1. I used to bring horses through the nether all the time in 1.8 and before. Spent some time away from Minecraft and now, my first attempt to bring horses home, and even after making the portals all wider, I've had 4 deaths and only 1 successful transport – and that one was a very near miss; I was able to push him out of the portal with half a heart of health remaining! This is VERY frustrating, given how far you often need to transport horses to bring them home in the first place.

### Comment 21: migrated (2018-09-12T17:05:22.362-0700)

Confirmed for 1.13.1.

### Comment 22: migrated (2019-03-16T13:20:13.159-0700)

This still happens in both 1.13.2 and in the 1.14 snapshots. Being such an old bug it baffles me that there's still no response from devs.

### Comment 23: migrated (2019-05-16T18:41:08.216-0700)

Still happening in 1.14.1. It's very frustrating!

### Comment 24: dscheJ-Ouh (2019-06-13T12:38:55.489-0700)

Still in 1.14.2 - genocide for the entire horse and donkey population?
[EDIT]:
Following a hunch, I just had a look at the hitboxes of horses and donkeys – they're massive!
No other mobs I've ever seen (well, except ravagers, which are a little bit bigger, and bosses) have such incredibly huge hitboxes in comparison to their body size, especially considering the hitboxes of cows or even iron golems, that look almost tiny… – and the hitboxes of donkeys are only marginally smaller than those of horses, even when donkeys are a little bit smaller than cows(?!?)
– No wonder horses suffocate at each opportunity, even when their bodies aren't really next to a wall; the trouble with hitboxes that don't turn according to the viewpoint, when an animal's body length is considerably bigger than its body width….

### Comment 25: migrated (2019-07-08T08:18:00.390-0700)

This is the bug that killed PewDiePie's horse.
https://youtu.be/YuihlgsgNSo?t=7m19s

### Comment 26: migrated (2019-07-12T08:58:30.054-0700)

Rip Joergen

### Comment 27: numeritos (2020-07-02T02:22:26.543-0700)

Affects 1.16, 1.16.1 and 20w27a

### Comment 28: migrated (2020-09-02T15:00:33.843-0700)

Cannot reproduce in 1.16.2

### Comment 29: pokechu22 (2020-10-23T12:47:07.159-0700)

This bug seems to have been fixed with some portal changes in 20w28a, along with MC-121098.

### Comment 30: Jeuv (2020-10-23T12:51:04.700-0700)

Not true, I almost lost my horse yesterday in a portal in 1.16.3.

### Comment 31: pokechu22 (2020-10-23T13:14:24.050-0700)

I probably tested it improperly, then. (I rode a horse into the corner of a portal, got off, and teleported; the horse wasn't inside of the portal frame nor did it get pushed in by me.  But there possibly are other ways it could happen; can you elaborate on what happened to your horse?)

### Comment 32: Jeuv (2020-10-23T13:28:57.555-0700)

The portal I pushed it through had a wall on one side, which it then got stuck in.

### Comment 33: migrated (2021-01-12T18:00:06.400-0800)

Playing on 1.16.1 and I had this issue as well
My Neither Portal was surrounded by walls on all sides except for a 2x3 corridor going up to it. Horse goes in, horse suffocates on the other side.
