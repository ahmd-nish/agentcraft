# MC-1133: Whether or not a player experiences some effect is calculated based on the block under the center of the player

**Mojira URL:** [https://bugs.mojang.com/browse/MC-1133](https://bugs.mojang.com/browse/MC-1133)

## Report details

- **Mojira categories:** Hitboxes; Player
- **Project:** MC
- **Issue key:** MC-1133
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2012-10-29T04:51:45.576-0700
- **Updated:** 2025-05-29T09:20:52.807-0700
- **Resolution date:** 2024-11-13T06:29:05.699-0800
- **Affects versions:** Minecraft 1.4.1; Minecraft 1.4.2; Minecraft 1.4.6; Minecraft 1.4.7; Minecraft 1.5; Minecraft 1.5.1; Minecraft 1.5.2; Minecraft 1.6.2; Minecraft 1.6.4; Minecraft 13w38a; Minecraft 13w38b; Minecraft 13w38c; Minecraft 1.7.4; Minecraft 14w02c; Minecraft 14w03b; Minecraft 14w04a; Minecraft 14w04b; Minecraft 14w08a; Minecraft 1.7.5; Minecraft 14w10b; Minecraft 14w10c; Minecraft 1.7.9; Minecraft 1.7.10; Minecraft 14w27b; Minecraft 14w28a; Minecraft 14w28b; Minecraft 1.8; Minecraft 1.8.1-pre2; Minecraft 1.8.1; Minecraft 1.8.2-pre6; Minecraft 1.8.2; Minecraft 1.8.7; Minecraft 1.8.8; Minecraft 15w33b; Minecraft 15w33c; Minecraft 15w42a; Minecraft 15w44a; Minecraft 15w44b; Minecraft 15w45a; Minecraft 15w46a; Minecraft 1.8.9; Minecraft 15w51b; Minecraft 16w02a; Minecraft 1.9; Minecraft 1.9.1 Pre-Release 1; Minecraft 1.9.1 Pre-Release 2; Minecraft 1.9.1 Pre-Release 3; Minecraft 1.9.2; Minecraft 1.9.3 Pre-Release 3; Minecraft 1.9.4; Minecraft 16w20a; Minecraft 16w21a; Minecraft 16w21b; Minecraft 1.10 Pre-Release 1; Minecraft 1.10 Pre-Release 2; Minecraft 1.10; Minecraft 1.10.1; Minecraft 1.10.2; Minecraft 16w32a; Minecraft 16w32b; Minecraft 16w33a; Minecraft 16w35a; Minecraft 16w39c; Minecraft 16w44a; Minecraft 1.11; Minecraft 1.11.1; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 17w13a; Minecraft 17w14a; Minecraft 17w15a; Minecraft 17w16a; Minecraft 17w17b; Minecraft 1.12 Pre-Release 1; Minecraft 1.12; Minecraft 17w31a; Minecraft 1.12.1 Pre-Release 1; Minecraft 1.12.1; Minecraft 1.12.2; Minecraft 18w01a; Minecraft 18w11a; Minecraft 18w14a; Minecraft 18w14b; Minecraft 18w15a; Minecraft 18w16a; Minecraft 18w19a; Minecraft 18w19b; Minecraft 18w20a; Minecraft 18w20b; Minecraft 18w20c; Minecraft 18w21a; Minecraft 18w22a; Minecraft 18w22b; Minecraft 18w22c; Minecraft 1.13-pre1; Minecraft 1.13-pre2; Minecraft 1.13-pre3; Minecraft 1.13-pre4; Minecraft 1.13-pre5; Minecraft 1.13-pre6; Minecraft 1.13-pre7; Minecraft 1.13-pre8; Minecraft 1.13-pre9; Minecraft 1.13-pre10; Minecraft 1.13; Minecraft 18w30a; Minecraft 18w30b; Minecraft 18w31a; Minecraft 18w32a; Minecraft 18w33a; Minecraft 1.13.1-pre1; Minecraft 1.13.1-pre2; Minecraft 1.13.1; Minecraft 1.13.2-pre1; Minecraft 1.13.2-pre2; Minecraft 1.13.2; Minecraft 18w43b; Minecraft 18w43c; Minecraft 18w44a; Minecraft 18w45a; Minecraft 18w46a; Minecraft 18w47a; Minecraft 18w47b; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 19w02a; Minecraft 19w03a; Minecraft 19w03b; Minecraft 19w04a; Minecraft 19w06a; Minecraft 19w07a; Minecraft 19w08a; Minecraft 19w09a; Minecraft 19w11a; Minecraft 19w12a; Minecraft 19w12b; Minecraft 19w13a; Minecraft 19w13b; Minecraft 19w14a; Minecraft 19w14b; Minecraft 1.14 Pre-Release 1; Minecraft 1.14 Pre-Release 2; Minecraft 1.14 Pre-Release 5; Minecraft 1.14.2 Pre-Release 2; Minecraft 1.14.2 Pre-Release 3; Minecraft 1.14.3 Pre-Release 3; Minecraft 1.14.3 Pre-Release 4; Minecraft 1.14.4 Pre-Release 4; 1.14.4; 19w35a; 19w36a; 19w37a; 19w38b; 19w39a; 19w40a; 19w41a; 19w42a; 19w44a; 19w45a; 19w46b; 1.15 Pre-release 1; 1.15 Pre-Release 2; 1.15 Pre-release 3; 1.15 Pre-release 4; 1.15 Pre-release 5; 1.15 Pre-release 6; 1.15 Pre-release 7; 1.15; 1.15.1; 1.15.1 Pre-release 1; 1.15.2 Pre-Release 1; 1.15.2 Pre-release 2; 1.15.2; 20w06a; 20w07a; 20w08a; 20w09a; 20w10a; 20w11a; 20w12a; 20w13a; 20w13b; 20w14a; 20w15a; 20w16a; 20w17a; 20w18a; 20w19a; 20w20b; 20w21a; 20w22a; 1.16 Pre-release 1; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 4; 1.16 Pre-release 5; 1.16 Pre-release 7; 1.16 Pre-release 8; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w27a; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Pre-release 2; 1.16.2 Release Candidate 1; 1.16.2 Release Candidate 2; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4 Pre-release 1; 1.16.4 Pre-release 2; 1.16.4 Release Candidate 1; 1.16.4; 20w45a; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w08b; 21w10a; 21w11a; 21w13a; 21w14a; 21w15a; 21w16a; 21w17a; 21w18a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17 Pre-release 4; 1.17 Release Candidate 1; 1.17 Release Candidate 2; 1.17; 1.17.1 Pre-release 3; 1.17.1; 21w38a; 21w39a; 21w42a; 1.18 Pre-release 5; 1.18 Pre-release 7; 1.18; 1.18.1; 22w03a; 1.18.2; 22w11a; 22w12a; 22w13a; 22w15a; 22w17a; 1.19 Pre-release 3; 1.19 Pre-release 5; 1.19; 1.19.1; 1.19.2; 22w42a; 22w45a; 1.19.3 Pre-release 2; 1.19.3; 23w03a; 23w04a; 23w05a; 23w06a; 1.19.4 Pre-release 2; 1.19.4; 23w14a; 23w17a
- **Fix versions:** 23w18a
- **Labels:** edge; sound; walking
- **Watchers:** 3
- **Attachments:** 9
- **Attachment filenames:** 2014-07-10_08.02.44.png; 2014-07-10_08.02.50.png; 2019-10-12_18.08.35.png; 2021-03-06 20-56-08.mkv; 2021-03-06 21-01-22.mkv; 2021-11-23_00.49.52_3.png; 2021-11-23_00.50.52.png; MC-1133 - Example.mp4; Minecraft 20w20b - Singleplayer 2020-05-14 16-50-19_Trim.mp4
- **Issue links:** Relates:outward:MC-262777:Sprint-jumping on the edges of solid blocks can still produce the occasional incorrect sprint particle and/or create particles in midair | Relates:inward:MC-101950:Walking on shulker, boat/raft or boat/raft with chest doesn't play footsteps sound | Relates:inward:MC-178723:Fishing rod bobbers don't activate a target if shot on the very edge | Relates:inward:MC-197267:Guardians fail to make flopping sounds if they aren't centered on a solid block | Relates:inward:MC-199197:Fireworks shot up towards a target block don't always activate it on impact | Relates:inward:MC-212582:Walking inside of scaffolding that has air below it doesn't produce any footstep sounds or closed captions | Relates:inward:MC-262408:Players landing on the edge of farmland still sometimes does not trample the block into dirt, despite the MC-1133 fix | Relates:outward:MC-257269:Sculk sensor detects player walking between carpet and wool | Relates:inward:MC-262424:Sprinting particles on the edges of blocks are still incorrect | Duplicate:inward:MC-255580:Water particles seen when landing on edge of block next to water | Duplicate:inward:MC-205570:Jumping on the edge of powdered snow | Duplicate:inward:MC-130371:Footsteps from Structure Void | Relates:inward:MC-262363:Player can still gain a normal jump off of a honey block with precise timing | Duplicate:inward:MC-245528:Flowers and other non-solid blocks can generate sprinting particles | Relates:inward:MC-158154:Players can bounce on beds even when not directly touching it | Relates:inward:MC-74955:Fences play sound when jumping and walking/sprinting beside them | Relates:inward:MC-242105:When landing on some non-full blocks while touching a thin block, impact particles use the thin block's texture | Relates:inward:MC-207290:Sculk sensors don't detect vibrations while walking on the edge of a block | Relates:inward:MC-2604:Walking on non-solid blocks with no collision plays their respective walking sounds | Duplicate:inward:MC-261868:Walking or jumping on the edge of wools is detected by sculk sensor | Duplicate:inward:MC-259591:Jumping on Edge of Block while Directly Above Pointed Dripstone Still Deals Fall Damage | Duplicate:inward:MC-258426:If you fall on the edge of the slime, you take damage. | Duplicate:inward:MC-258432:Player doesn't bounce on the edge of slime blocks | Duplicate:inward:MC-258343:Ice isn't slippery on the edge | Duplicate:inward:MC-146836:Players that are launched upward by a slime block and piston take fall damage from slime block | Duplicate:inward:MC-240063:Taking damage on a Block next to dripstone | Duplicate:inward:MC-239215:Cobweb bug | Duplicate:inward:MC-235143:You can bounce even on honey blocks if you jump whilst standing on a honey block and a slime block. | Duplicate:inward:MC-235142:You cannot bounce on slime blocks if you're standing on a slime block and a honey block. | Duplicate:inward:MC-234825:Incorrect appearance of the particles when falling on the edge of the block | Duplicate:inward:MC-234873:Incorrect block particles next to fire | Duplicate:inward:MC-235433:stone makes wood noises when you walk over it | Relates:inward:MC-2591:Walking over the corner of lava deals damage | Duplicate:inward:MC-231674:Glitch | Duplicate:inward:MC-230881:fall damage taken when you hit a slimeblock on the edge | Duplicate:inward:MC-227517:Slime Block bounce bug | Duplicate:inward:MC-130222:Animation Bugs | Duplicate:inward:MC-223982:shower sand | Duplicate:inward:MC-222635:Slime block bounce doesn't work if you land on the edge of the block. | Duplicate:inward:MC-220874:standing with the center of your body over a block edge will not apply block conditions | Duplicate:inward:MC-219360:Step sounds do not play whilst walking on the very edge of blocks. | Duplicate:inward:MC-217940:Pixel wrong | Duplicate:inward:MC-215698:Magma block dont give dmg | Duplicate:inward:MC-214585:When landing on the edge of a block next to water/lava, landing particles appear | Duplicate:inward:MC-212856:Wrong Player drop particles | Duplicate:inward:MC-22889:Water Particles when sprinting on the edge of blocks / falling down besides water | Duplicate:inward:MC-206692:Soulsand edge issues | Duplicate:inward:MC-206786:Jumping on Waterlogged Dripstone Does Damage if Player is Also Touching Land | Duplicate:inward:MC-201796:Lava particles from landing on an adjacent block | Duplicate:inward:MC-116593:Animals die when they fall on slime blocks. | Duplicate:inward:MC-196222:Particles when landing next to a lava block. | Duplicate:inward:MC-194264:Soul sand and slime blocks problems | Duplicate:inward:MC-194939:Soul Speed not working on water surface | Duplicate:inward:MC-194377:Slime block problems | Duplicate:inward:MC-190238:I can't jump highly on honey block, but i can jump in corner of this block | Duplicate:inward:MC-190054:if you walk along the edge of the soul sand, its slowdown doesn't affect you. | Duplicate:inward:MC-186678:player moving edge of block, no step sound plays | Duplicate:inward:MC-174710:You can run fine on the side of soul sand without getting slowed down | Duplicate:inward:MC-174512:Soul Speed stops working next to lava | Duplicate:inward:MC-174483:Walking on the border of Soul Sand with Soul Speed dosen't work | Duplicate:inward:MC-173335:wrong block particles | Duplicate:inward:MC-167987:You can jump up a block on honey blocks | Duplicate:inward:MC-167053:Soulsand doesnt slow you down | Duplicate:inward:MC-166728:Slimeblocks have too-tiny of a spot where you'll bounce | Duplicate:inward:MC-166273:If you land on the edge of a slime block, you don't bounce | Duplicate:inward:MC-164932:Falling partway on slime doesn't trigger it | Duplicate:inward:MC-164032:Crouching on the edge of honey blocks while they are being pushed by pistons causes the player to fall off | Duplicate:inward:MC-164040:Water drops wrong particles | Duplicate:inward:MC-163594:You cannot descend on scaffolding when in the same block as a ladder | Duplicate:inward:MC-163559:You can jump normal on honey block | Duplicate:inward:MC-163449:Jumping off of honey blocks' edges makes the player jump high | Duplicate:inward:MC-163297:Normal jumps on Honey Blocks | Duplicate:inward:MC-163044:Jumping on the edge of honey block is possible. | Duplicate:inward:MC-163129:Jumping normally from honey block corners | Duplicate:inward:MC-160964:Scafolding Edge Bug | Duplicate:inward:MC-151284:Particle effect of the adjacent block shows up when touching down | Duplicate:inward:MC-149031:scafolding corner bug! | Duplicate:inward:MC-142672:Slime blocks Don't launch players from the side | Duplicate:inward:MC-139359:scaffholding glitch to walk in air | Duplicate:inward:MC-138185:Blue Ice is not slippery at edges | Duplicate:inward:MC-42042:Ice does not slide the player on the edge of the block | Duplicate:inward:MC-99500:Mobs getting hurt on slime blocks | Duplicate:inward:MC-44381:Slime block doesn't bounce on the edge and player/mob takes fall damage | Duplicate:inward:MC-108018:Slime block edge player dont bounce back | Duplicate:inward:MC-104737:lava particles.... NOT what you think. | Duplicate:inward:MC-103943:Magma Block not taking damage on edge of block | Duplicate:inward:MC-73276:Particles not showing when you fall on the side of a block in creative mode | Duplicate:inward:MC-85416:Wrong particles | Duplicate:inward:MC-66784:You Won't Bounce On Slime Blocks If On Very Edge | Duplicate:inward:MC-90704:Moving over torches plays walking on wood sound | Duplicate:inward:MC-90243:slimeblock bug | Duplicate:inward:MC-81147:Walking on edge of block makes no sound | Duplicate:inward:MC-55055:Fall impact particles negated | Duplicate:inward:MC-79542:Slimeblocks causing fall damage | Duplicate:inward:MC-77791:If you land on the edge of a slime block, you don't bounce and you take fall damage | Duplicate:inward:MC-29355:I was walking on the very edge of the wood at a farm from an NPC village and created no noise. | Duplicate:inward:MC-16439:Ice and Water edge glitch | Duplicate:inward:MC-16048:No sound played when walking on the edge a block | Relates:outward:MCPE-18063:The textures of falling/sprinting particles can sometimes use illogical blocks

## Description

Mod edit:
When the player stands at the very edge of a block so that the center of the player is over the edge of the block, the game calculates the actions of the player according to the (air) block below the center of the player but not to the block the player is standing on.
- walking completely silent

- walking speed on Ice edge is normal

- fall damage when falling on the edge of slime blocks

- no reduced fall damage when falling on edge of hay bale

- wrong/no fall particles when landing on the edge of a block (allows for MC-240028, MC-240029 and MC-122547 to be seen)

- no damage while standing on the edge of magma blocks

- can jump normally on the edge of honey blocks

- jumping while standing on the edge of farmland does not turn it into dirt

- redstone ore not activated when standing on the edge

- not being affected by soul speed when standing on the edge of soul sand/soil

- when landing on wool with the player center above air, sculk sensors are activated (MC-252389)

- when walking on the edge of blocks, sculk sensors do not detect vibrations (MC-207290)

- taking fall damage at the edge of powder snow

Walking at the very edge of a block, and I mean the longest out possible on a block, will make it silent since it is not registering the walking. You are still on the block, just that it is silent. This bug has existed since before alpha.

## Comments (100)

### Comment 1: migrated (2012-10-29T04:51:45.576-0700)

This comment contained multiple image attachments (9), please login to view the attachments.

### Comment 2: migrated (2012-10-29T07:12:59.665-0700)

Confirmed, this occurs on mac computers too.

### Comment 3: Nathan Adams (2012-10-29T07:52:36.086-0700)

Please don't mark an issue as affecting a future version; you can't have tested it already

### Comment 4: migrated (2012-12-25T10:20:01.167-0800)

Confirmed in 1.4.6.

### Comment 5: migrated (2013-02-02T13:20:47.606-0800)

I think the problem is that when you walk out oh the very edge of a block, you're actually no longer on the original block. If you go into 3rd person mode, you can see that you aren't actually on the block, and that you're actually on the air. It still registers that you are standing on the block, but not the part that makes noise.

### Comment 6: migrated (2014-03-07T05:09:21.573-0800)

Still a concern in 1.7.5, 14w08a and 10b, relates to MC-44381

### Comment 7: migrated (2014-03-07T07:32:48.578-0800)

still in 10c

### Comment 8: migrated (2014-07-10T08:04:24.278-0700)

Confirmed in 14w28b. It does have to do with the fact that you are not technically "standing" on the block. I will upload a couple pictures of the F3 menu showing this

### Comment 9: migrated (2014-07-10T08:07:53.356-0700)

These are two screenshots showing the bug. Please note the x values of "Block" and "Looking at". The ice is along x=1, but the "Block" value you are "standing" on is 0.

### Comment 10: rydian (2014-10-18T08:10:26.395-0700)

Confirmed in 1.8.1-pre2.

### Comment 11: migrated (2015-08-18T15:52:38.174-0700)

Confirmed for 1.8.8 & 15w33c.

### Comment 12: rydian (2015-10-14T10:15:15.872-0700)

Still happening in 15w42a.

### Comment 13: migrated (2015-10-28T06:43:07.484-0700)

Confirmed for 15w43c.

### Comment 14: migrated (2015-10-29T01:40:32.531-0700)

Confirmed for 15w44a.

### Comment 15: migrated (2015-11-06T13:49:36.612-0800)

Confirmed for 15w45a.

### Comment 16: migrated (2015-11-12T06:18:27.770-0800)

Confirmed for 15w46a

### Comment 17: migrated (2015-12-17T14:40:44.728-0800)

Minecraft 1.8.9 and 15w51b confirmed

### Comment 18: migrated (2016-01-13T14:59:12.239-0800)

Confirmed for 16w02a.

### Comment 19: migrated (2016-03-15T16:24:48.964-0700)

Confirmed for 1.9.1-pre3.

### Comment 20: migrated (2016-05-05T16:59:02.143-0700)

Confirmed for 1.9.3-pre3.

### Comment 21: migrated (2016-05-11T16:04:49.723-0700)

Confirmed for 1.9.4.

### Comment 22: migrated (2016-05-18T15:00:11.378-0700)

Confirmed for 16w20a.

### Comment 23: migrated (2016-05-25T16:02:28.741-0700)

Confirmed for 16w21a.

### Comment 24: migrated (2016-05-26T15:55:24.670-0700)

Confirmed for 16w21b.

### Comment 25: migrated (2016-06-02T18:43:40.304-0700)

Confirmed for 1.10-pre1.

### Comment 26: migrated (2016-06-07T15:54:15.803-0700)

Confirmed for 1.10-pre2.

### Comment 27: migrated (2016-06-08T14:37:11.922-0700)

Confirmed for 1.10.

### Comment 28: migrated (2016-06-22T10:03:16.304-0700)

Confirmed for 1.10.1.

### Comment 29: migrated (2016-06-23T09:09:31.519-0700)

Confirmed for 1.10.2.

### Comment 30: JUE13 (2017-04-27T22:49:55.730-0700)

Confirmed for 17w17b

### Comment 31: Lukeonia1 (2017-10-16T02:18:17.608-0700)

Confirmed for 1.12.2.

### Comment 32: muzikbike (2018-04-05T08:14:06.397-0700)

Affects 18w14b

### Comment 33: muzikbike (2018-04-11T08:48:04.753-0700)

Affects 18w15a

### Comment 34: muzikbike (2018-04-19T10:52:10.277-0700)

Affects 18w16a

### Comment 35: muzikbike (2018-05-08T11:29:20.728-0700)

Affects 18w19a

### Comment 36: muzikbike (2018-05-09T13:11:05.538-0700)

Affects 18w19b

### Comment 37: muzikbike (2018-05-15T07:48:47.297-0700)

Affects 18w20a

### Comment 38: muzikbike (2018-05-16T08:21:38.561-0700)

Affects 18w20b

### Comment 39: muzikbike (2018-05-17T08:05:23.200-0700)

Affects 18w20c

### Comment 40: muzikbike (2018-05-23T07:13:02.428-0700)

Affects 18w21a

### Comment 41: muzikbike (2018-05-29T18:33:10.051-0700)

Affects 18w22a

### Comment 42: muzikbike (2018-05-31T04:18:49.745-0700)

Affects 18w22b

### Comment 43: Michael Wobst (2018-05-31T04:20:41.006-0700)

, ticket is yours now

### Comment 44: muzikbike (2018-05-31T10:26:24.697-0700)

Affects 18w22c. Can a relates to be added for MCPE-18063?

### Comment 45: muzikbike (2018-07-20T10:37:54.556-0700)

It seems as though sprinting on the edges of water no longer shows water particles.

### Comment 46: SuperDyl (2018-07-21T13:45:38.531-0700)

Water particles probably don't show up with this bug because water is no longer really a block and is instead more of just a block tag.

### Comment 47: muzikbike (2018-07-21T14:36:29.831-0700)

Then why does it still show up upon falling?

### Comment 48: migrated (2018-10-06T19:39:01.888-0700)

This issue makes falling on slime blocks adjacent to air quite risky

### Comment 49: migrated (2018-11-08T11:17:54.162-0800)

This makes descending very dangerous! (see MC-139088)
When you're standing on the edge of a scaffolding tower and try to descend, you'll actually fall and take damage.
Video link (google drive): https://drive.google.com/file/d/1Pmc4Y5UvmTm5ncG6isO6HNf6qH_lztGu/view?usp=sharing

### Comment 50: migrated (2018-11-15T08:51:57.311-0800)

This bug allows you to stand on the edge of a magma block and not take any damage.

### Comment 51: [Mod] violine1101 (2019-09-12T09:19:26.415-0700)

Also affects scaffolding.

### Comment 52: migrated (2019-10-09T12:29:44.966-0700)

Also affects honey blocks.

### Comment 53: muzikbike (2019-10-09T12:36:55.940-0700)

Should this ticket be split into multiple smaller tickets? Granted they all originate to this same cause though, so maybe not.

### Comment 54: pokechu22 (2019-10-09T12:42:06.243-0700)

I don't think it would be useful to split this one, since there is one underlying cause that, if fixed, would be fixed for more or less all of the cases. (It would require pretty systemic changes, but also almost certainly wouldn't be fixed for only one of the cases without fixing the rest.)  Compare to, say, MC-9553, where the bug is composed of lots of individual interactions that each needed to be fixed individually; there, splitting made sense.

### Comment 55: migrated (2019-10-12T01:10:33.616-0700)

Allows you to jump onto iron block in attached picture if you stand on edge of honey block

### Comment 56: migrated (2020-03-11T14:01:57.203-0700)

This issue also affects blocks that have the climbable tag like for example ladders, vines. I am not sure if this is intended for these blocks but I believe that it's not.

### Comment 57: [Mod] violine1101 (2020-03-11T14:02:00.577-0700)

Soul Speed is affected as well, see MC-174483 for instance.

### Comment 58: migrated (2020-04-22T21:51:17.352-0700)

I did some testing planning to open my own issue specific to honey blocks, but luckily found this one so I do not duplicate. But I will put what I found here anyway.
Java Minecraft 1.15.2
I put a honey block at -56, 56, 29. When crouch walking off the edge a player (and I assume any mob) can jump as though they were not on a honey block. I teleported myself right to the very edge of the block, at -55.88, 57.00, 29.999. (landing at y = 56.93750 if that matters at all) At that location the player's jump IS affected by the honey. But then I teleported to -55.88, 57.00, 30.00. At this location the player can jump freely uninterrupted from the honey block.
I did some more testing. I discovered some unrelated facts, like that the coordinates 29.99999999999999, 29.999999999999993, and 29.999999999999996 are all valid, but all other coordinates in between and after are rounded. Also all of these coordinates on the honey block from the last paragraph still affect the player's jump height as though you are an the honey block, so all is working as intended here.
I would suggest the player's hit box determine if it is affected by a block or not. This could break things in ways that I couldn't possibly think up, but obviously not all of the physics in this game work based on what is directly below Steve. If it did, we couldn't crouch walk off the edge of a block and hang onto it. I imagine that the same bit of code that tells the game not to fling Steve to the ground if you manage to get your center of mass off a block by .01 could help us out here. But I am only learning Java. Not yet worthy to be called a programmer, so I don't really know.

### Comment 59: migrated (2020-05-01T07:39:39.247-0700)

Confirmed for 20w18a. This also affects magma blocks, but not damage of campfires. (normal and soul)

### Comment 60: migrated (2020-05-12T06:33:31.363-0700)

Awesome! This feels so sneaky!

### Comment 61: migrated (2020-05-14T08:37:26.055-0700)

Confirmed for 20w20b

### Comment 62: migrated (2020-05-14T13:51:08.771-0700)

Striders also get cold standing on the edge of falling lava. They also don't seem to travel upwards anymore. Think this also relates to this issue.

### Comment 63: FaRo1 (2020-05-15T03:23:59.926-0700)

That should be MC-181610. If you find a case where the center of the strider actually matters, please create a new report and say here that you did, so that it can be marked as related.

### Comment 64: migrated (2020-05-15T07:10:09.885-0700)

This bug also affects hay bale, so when you land on the edge of hay bale, it won’t reduce fall damage.

### Comment 65: migrated (2020-05-20T07:16:25.513-0700)

Confirmed for 20w21a

### Comment 66: migrated (2020-06-05T06:15:43.539-0700)

Confirmed for 1.16 Prerelease 1

### Comment 67: migrated (2020-06-05T07:02:55.971-0700)

Confirmed for 1.16 Pre-2

### Comment 68: migrated (2020-06-16T09:49:41.642-0700)

Confirmed for 1.16 pre-release 7

### Comment 69: migrated (2020-08-08T08:48:39.184-0700)

Also, only farmland that is under the center of the player gets turned into dirt when jumping.

### Comment 70: migrated (2020-11-04T11:31:11.341-0800)

Confirmed in Snapshot 20w45a.

### Comment 71: Avoma (2020-11-25T11:25:00.094-0800)

Can confirm in 20w48a.

### Comment 72: migrated (2020-12-13T16:48:22.172-0800)

This also affects cobwebs and my guess it also affects powdered snow although I haven't tested it

Also, this must be the oldest bug report still not resloved. Correct me if I am wrong

Also, confirmed for 1.16.4

### Comment 73: migrated (2020-12-14T15:27:39.185-0800)

There's no reason it wouldn't affect literally every block, if we understand it correctly. The issue is in the code that calculates whether a player is "on" a block or not for the purposes of any effect relating to standing on a block.
This is a major bug but it's also likely an extremely nontrivial fix; not only would the devs need to change the code that calculates whether a player is standing on a given block, they'd also need to add code to handle any potentially conflicting effects (such as if a player is standing on both soul soil and honey blocks while wearing soul speed boots, for example). While this could absolutely be done, there's no super obvious answer for how to go about it. Personally, what we'd do is just have the effects stack, and cancel out if they conflict? But that also means they'd have to make sure standing on the line between two blocks with the same effect doesn't cause the effect to be doubled!!
I do hope mojang is at least discussing how to handle this, though. It seems like something very much worth prioritizing once other major bugs have been handled.

### Comment 74: migrated (2020-12-18T05:19:21.759-0800)

In 20w49a, when Sculk Sensors were introduced, it was revealed that you are able to land on air, which triggers a Sculk Sensor. Best demonstrated when landing on a wool block, but your hitbox is more than 50% off the block.

### Comment 75: migrated (2021-01-19T05:51:10.449-0800)

I suggest either trying to make the hitbox the player's shape so its a bit more accurate or to limit the distance that you can sneak.

### Comment 76: Avoma (2021-02-03T11:07:57.797-0800)

Can confirm in 21w05a.

### Comment 77: Avoma (2021-02-04T10:25:31.823-0800)

Can confirm in 21w05b.

### Comment 78: gaspoweredpick (2021-03-31T13:11:53.231-0700)

This can now happen with powder snow when you're wearing leather boots.

### Comment 79: migrated (2021-04-03T11:29:00.751-0700)

Powder snow is like climbing powder snow when wearing leather boots works like scaffolding, that is why powder snow is affected by MC-139063.
This bug does not affect big dripleaf.

### Comment 80: migrated (2021-06-03T08:54:30.248-0700)

Confirmed in 1.17 pre-release 4
This bug also amusingly affects light blocks (landing on the corner of a solid with a light block under your center) causing yellow fall particles

### Comment 81: migrated (2021-06-03T15:34:55.745-0700)

Another effect is walking on the edge of powder snow doesn't slow you down, showcased in MC-227191

### Comment 82: ampolive (2021-07-01T08:24:16.645-0700)

Can confirm in 1.17.1 Pre-release 3.

### Comment 83: migrated (2021-07-07T02:18:31.702-0700)

Can confirm for 1.17.1.

### Comment 84: Creeper Juice (2021-07-29T12:39:18.813-0700)

This also prevents soul sand from slowing you down.

### Comment 85: MMK21 (2021-12-10T08:18:52.276-0800)

Affects 1.18.1

### Comment 86: migrated (2022-01-19T15:21:40.272-0800)

Can confirm as of 22w03a

### Comment 87: MMK21 (2022-02-28T12:10:54.562-0800)

Affects 1.18.2

### Comment 88: migrated (2022-03-11T19:35:28.697-0800)

How many People Tested this! it has like 200 Affects Versions lol and can confirm for 1.18.2.

### Comment 89: migrated (2022-03-20T15:21:18.500-0700)

Yeah, this has been a thing since beta (probably further back, but I haven't played earlier versions)

### Comment 90: isXander (2022-04-04T08:30:53.488-0700)

Code analysis (tentative)
This is probably because checks like this look directly below the center of the player to find what block the player is "standing" on. Instead, collision should track what blocks the player is colliding with and use that block instead.

### Comment 91: pulpetti (2022-04-30T03:20:34.190-0700)

In 22w17a.

### Comment 92: migrated (2022-07-28T10:03:42.044-0700)

MC-254644 might be related

### Comment 93: Avoma (2022-08-06T11:54:12.820-0700)

Can confirm in 1.19.2.

### Comment 94: migrated (2022-12-07T08:51:53.189-0800)

Can Confirm for 1.19.3 Release Candidate 3

### Comment 95: Brain81505 (2023-01-18T08:14:15.505-0800)

Can confirm in 23w03a

### Comment 96: Brain81505 (2023-01-24T23:23:11.262-0800)

Can confirm in 23w04a

### Comment 97: Brain81505 (2023-02-01T08:04:57.953-0800)

Can confirm in 23w05a

### Comment 98: Brain81505 (2023-02-11T07:31:53.903-0800)

Can confirm in 23w06a

### Comment 99: migrated (2023-05-25T21:57:42.277-0700)

Still not completely resolved in Minecraft 1.20 Pre-release 6 with scaffoldings. Scaffoldings are not included in the bug report. A duplicated bug report is MC-165067

With at least 4 scaffoldings, go to the top and hold shift at the edge of it to get fall damage.

Video of the bug being played in Minecraft 1.20 Pre-release 6: bug video

### Comment 100: ampolive (2023-05-26T05:08:15.238-0700)

That is MC-139063, which is a separate bug.
