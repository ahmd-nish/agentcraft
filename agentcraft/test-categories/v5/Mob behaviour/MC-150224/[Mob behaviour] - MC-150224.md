# MC-150224: Rabbits can occasionally get stuck on the edges of blocks

**Mojira URL:** [https://bugs.mojang.com/browse/MC-150224](https://bugs.mojang.com/browse/MC-150224)

## Report details

- **Mojira categories:** Mob behaviour
- **Project:** MC
- **Issue key:** MC-150224
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2019-04-28T13:07:51.879-0700
- **Updated:** 2025-04-26T07:57:03.042-0700
- **Resolution date:** 2024-11-08T05:06:22.739-0800
- **Affects versions:** Minecraft 19w12b; Minecraft 1.14 Pre-Release 2; Minecraft 1.14 Pre-Release 3; Minecraft 1.14 Pre-Release 4; Minecraft 1.14 Pre-Release 5; Minecraft 1.14; Minecraft 1.14.1 Pre-Release 2; 1.14.4; 19w37a; 19w39a; 19w42a; 1.15 Pre-release 1; 1.15 Pre-Release 2; 1.15.1; 1.15.2; 1.16 Release Candidate 1; 1.16; 1.16.1; 1.16.2 Pre-release 3; 1.16.2; 1.16.3; 1.16.4; 20w45a; 20w51a; 1.16.5; 21w06a; 21w07a; 21w16a; 21w19a; 1.17 Pre-release 2; 1.17 Release Candidate 1; 1.17; 1.17.1 Pre-release 1; 1.17.1; 21w38a; 21w40a; 21w42a; 1.18 Pre-release 1; 1.18 Pre-release 5; 1.18; 1.18.1 Pre-release 1; 1.18.1; 22w03a; 22w05a; 22w07a; 1.18.2; 22w17a; 1.19 Pre-release 1; 1.19; 1.19.2; 22w42a; 22w43a; 1.19.3; 23w03a; 23w07a; 1.19.4; 23w16a; 23w18a; 1.20 Pre-release 7; 1.20; 1.20.1; 1.20.2 Pre-release 1; 1.20.2 Pre-release 2; 1.20.4; 23w51b; 24w03b; 24w14a; 1.20.5 Pre-Release 1; 1.20.5 Pre-Release 4; 1.20.5 Release Candidate 2; 1.20.5; 1.20.6; 1.21; 1.21.1; 24w37a; 1.21.2 Pre-Release 3; 1.21.3
- **Fix versions:** 24w46a
- **Area:** Gameplay
- **Votes:** 1
- **Watchers:** 1
- **Attachments:** 15
- **Attachment filenames:** 2019-04-28_07.43.17.png; 2019-04-28_08.15.36.png; 2019-04-28_08.17.37.png; 2019-04-28_13.55.25.png; 2019-04-28_14.10.05.png; 2019-05-11_23.28.51.png; 2019-05-11_23.28.52.png; 2019-05-11_23.29.17_2.png; 2019-05-11_23.29.17.png; 2022-09-14_15.41.22.png; MC-150224-FixShowcase.mp4; MojiraRabbit.mov; rabbitstuck.mp4; setup.png; UAdkMbO78f.mp4
- **Issue links:** Duplicate:inward:MC-274052:Desert rabbits are getting stuck! | Duplicate:inward:MC-273934:Rabbit pathfinding bug | Relates:outward:MC-277500:Rabbits usually fail to raid carrot crops | Duplicate:inward:MC-270958:Rabbit AI Glitch: Rabbits get stuck by one-block-high obstacles | Duplicate:inward:MC-252735:rabbits get stuck in trap door | Duplicate:inward:MC-268062:Rabbit Pathfinding Broken | Duplicate:inward:MC-264195:Rabbits keep getting stuck and have too little health | Duplicate:inward:MC-263070:Rabbits can't jump up blocks | Duplicate:inward:MC-263076:rabbit does not jump blocks. | Duplicate:inward:MC-262293:Rabbit often bugs when he wants to jump on the block. | Duplicate:inward:MC-262092:rabbits don't jump well | Duplicate:inward:MC-262046:The rabbit can't jump on a block, but only in place | Duplicate:inward:MC-259225:Rabbits Hitboxes getting stuck | Duplicate:inward:MC-238263:Rabbit AI breaks on iron bars | Duplicate:inward:MC-237492:Rabbits cannot jump over one block | Duplicate:inward:MC-150528:Rabbits get stuck in fence/jump over fence | Duplicate:inward:MC-164953:rabbit jumping not working properly | Duplicate:inward:MC-232958:Rabbits getting stuck on stairs and iron bars. | Duplicate:inward:MC-233014:Rabbits get stuck under azalea saplings | Duplicate:inward:MC-232705:Bunnies get stuck under Azaleas | Duplicate:inward:MC-199753:rabbit can't/don't want to jump on a block | Duplicate:inward:MC-146616:Baby rabbits can't always jump up blocks | Duplicate:inward:MC-230389:Rabbits get stuck jumping up a block | Duplicate:inward:MC-229644:Rabbits stuck on glass panes | Duplicate:inward:MC-192317:Rabbits cannot find a way while being pushed into an iron fence | Duplicate:inward:MC-227673:Rabbits get stuck in walls | Duplicate:inward:MC-225616:rabbits get stuck under azalea bushes | Duplicate:inward:MC-210733:rabbits get stuck hopping in one place when on lower stair | Duplicate:inward:MC-190394:Rabbit jump bug | Duplicate:inward:MC-214785:Bunnies cant really jump on blocks anymore/ glitched animation | Duplicate:inward:MC-203226:Rabbit stuck in north west corner of fence under water and drown | Duplicate:inward:MC-189603:Rabbits stuck on blocks' side | Duplicate:inward:MC-169178:Rabbits get stuck in slabs | Duplicate:inward:MC-168332:Baby rabbits sometimes get stuck when right next to corner fences | Duplicate:inward:MC-166462:Rabbits have trouble path-finding when on a half most most part of a stair, on the side of a block, under an upper slab. | Duplicate:inward:MC-157927:A bug with the rabbits | Duplicate:inward:MC-150061:Rabbit stuck in slab & stair | Duplicate:inward:MC-149969:Rabbits were trapped by fences | Duplicate:inward:MC-148289:Rabbits stuck on fences

## Description

The Bug:
Rabbits can occasionally get stuck on the edges of blocks.
Steps to Reproduce:
- Build the setup as shown in the attachment below.

- Summon multiple rabbits on any of the diamond blocks.

- Switch into survival mode and approach the rabbits so that they will run away from you.

- Pay close attention to the behavior of the rabbits as they try to jump over blocks.

- Take note as to whether or not rabbits can occasionally get stuck on the edges of blocks.

Observed Behavior:
Rabbits can occasionally get stuck on the edges of blocks.
Expected Behavior:
Rabbits would not occasionally get stuck on the edges of blocks.

## Comments (44)

### Comment 1: migrated (2019-04-28T13:07:51.879-0700)

This comment contained multiple image attachments (15), please login to view the attachments.

### Comment 2: Sonicwave (2019-05-09T18:16:50.358-0700)

Can confirm, though for me it also affects doors, trapdoors in the open (vertical) position, and rabbits under closed trapdoors placed on the top half of a block.

### Comment 3: migrated (2019-05-28T07:55:40.302-0700)

can confirm. for me they are getting stuck either to the top of the fence post, or the side of the glass. i'm not sure. either way, they're getting crushed/suffocated, and cannot escape. same effect happens horizontally, on the side of the fence post, instead of above it.

### Comment 4: migrated (2019-09-10T19:51:39.917-0700)

For me they would just stop moving, but not suffocated.

### Comment 5: migrated (2019-11-30T08:52:00.491-0800)

Can confirm for 1.14.4 and under half slabs

### Comment 6: anthony cicinelli (2020-01-31T08:25:54.282-0800)

Can confirm stairs for 1.15.2

### Comment 7: [Mod] violine1101 (2020-06-15T08:33:47.285-0700)

Is this still an issue in 1.16-pre5 or later? MC-172531 got fixed.

### Comment 8: markderickson (2020-06-26T19:29:06.271-0700)

Hi there!
This is still present in 1.16.1.

### Comment 9: markderickson (2020-07-01T21:20:15.951-0700)

Hi there!
Can confirm in 20w27a. I'll attach a video as proof.

### Comment 10: Avoma (2020-12-25T07:09:14.234-0800)

Can confirm in 20w51a.

### Comment 11: Niknokinater (2021-02-06T02:32:51.445-0800)

1.16.5

### Comment 12: Avoma (2021-02-23T08:15:09.780-0800)

Can confirm in 21w07a.

### Comment 13: Avoma (2021-03-29T11:34:55.766-0700)

Can confirm in 21w11a.

### Comment 14: migrated (2021-06-07T03:21:14.387-0700)

Can confirm in 1.17-Release-Candidate1.

### Comment 15: migrated (2021-06-07T07:55:40.156-0700)

can confirm in 1.17-rc2.

### Comment 16: migrated (2021-07-23T14:41:52.673-0700)

Still an issue. Please fix.

### Comment 17: ampolive (2021-09-28T15:21:09.860-0700)

Can confirm in 21w38a.

### Comment 18: ampolive (2021-10-09T13:03:51.482-0700)

Can confirm in 21w40a.

### Comment 19: Kokonut (2021-10-18T16:19:36.840-0700)

can confirm in 1.17.1

### Comment 20: ampolive (2021-10-18T16:33:10.339-0700)

1.17.1 is already marked as affected.

### Comment 21: ampolive (2021-10-23T03:42:36.348-0700)

Can confirm in 21w42a.

### Comment 22: ampolive (2021-11-13T09:17:17.891-0800)

Can confirm in 1.18 Pre-release 1.

### Comment 23: Avoma (2021-11-19T11:07:22.365-0800)

I'd like to request ownership of this ticket since the current reporter has been inactive since September of 2019.

### Comment 24: migrated (2021-12-23T05:39:51.485-0800)

Hi, there!
I'd like to add to this that the rabbit gets stuck (1.18.1) on blocks or even up stairs, when you get it to follow you using carrots or even using a lead. It's quite annoying when you have a house up the mountains and is trying to bring rabbits there.

### Comment 25: migrated (2022-03-14T11:54:44.725-0700)

Can confirm on 1.18.1 and 1.18.2, rabbit's gyrate when they go on stairs

### Comment 26: migrated (2022-07-11T12:03:23.488-0700)

I can confirm rabbits still get stuck on the edges of blocks, stairs seem to be the most common. Version Java 1.19.1

### Comment 27: ampolive (2022-07-11T16:36:56.797-0700)

1.19.1 is not out yet. Do you mean a pre-release?

### Comment 28: migrated (2022-09-14T12:42:35.512-0700)

On 1.19.2 this bug is still a problem.

### Comment 29: migrated (2023-02-15T09:14:59.235-0800)

confirmed for 23w07a

### Comment 30: migrated (2023-06-01T07:02:02.469-0700)

I can confirm for 1.20 pre-release 7 that rabbits get stuck on blocks, Actually I found out that they cannot even jump up any blocks. I made a 1 block deep pit and the rabbit got stuck in it for the remainder of the play session.

### Comment 31: migrated (2023-06-25T13:14:42.579-0700)

still happens in 1.20.1

### Comment 32: migrated (2023-09-07T16:54:55.222-0700)

In 1.20.2 Pre-Release 2

### Comment 33: migrated (2023-09-27T18:32:08.594-0700)

1.20.1 and rabbits still get stuck in open trapdoors and some seem too stupid to jump one block up. Wonder when this will be fixed, because it ruins things

### Comment 34: migrated (2023-10-11T13:45:38.530-0700)

23w41a rabbits still can't jump up full blocks unless panicking.

### Comment 35: bdm68 (2024-02-09T18:20:52.443-0800)

Affects 1.20.4.
Rabbits get stuck on full blocks if they are right next to the block, but they can jump up onto a block if they are at least half a block away from it.

### Comment 36: batbrain55 (2024-04-02T07:30:54.249-0700)

Can confirm in 24w13a.

### Comment 37: akozm (2024-04-05T21:13:20.230-0700)

Can confirm in 24w14a. I really hate this bug. Mojang, fix it quickly.

### Comment 38: migrated (2024-04-17T05:52:08.032-0700)

This bug seem to also affect bedrock edition... Some of my rabit are stuck on iron bar.

### Comment 39: migrated (2024-04-22T06:04:34.443-0700)

Possible Cause:
This may be caused by the unique behavior when rabbits move. They jump low instead of walk. They don't always jump high when they need to jump onto blocks.
Possible Solution:
Rabbits should jump low where other mobs will walk, and they should jump high when other mobs will jump.

### Comment 40: batbrain55 (2024-04-23T13:47:44.270-0700)

Can confirm in 1.20.5.

### Comment 41: muzikbike (2024-09-13T06:53:49.424-0700)

Seems to affect 24w37a

### Comment 42: litetex (2024-10-02T16:31:35.269-0700)

There are multiple problems inside rabbit pathfinding and related code causing this issue:
1. The calculation of the jump height/velocity is incorrect and poorly implemented. This results in too small jumps for climbing over a block (hops aren't high enough).
2. Rabbits sometimes "stall" (no horizontal movement) during jumps - due to this they just jump upwards in the same place when trying to climb a block.
3. Rabbits are stuck / try to wander around forever:
- The root cause is that PathNavigation#doStuckDetection sets its timeouts based on movement speed. If the movement speed is 0 (this is the case when a rabbit/mob is "stuck"), the timeout is also 0... and if the timeout is 0 it's ignored and therefore it's executed forever (or until interrupted by something external like another goal).

- Rabbits only have a single goal when idle: WaterAvoidingRandomStrollGoal/RandomStrollGoal. Most other entities also use RandomLookAroundGoal. Thus the above mentioned infinite navigation is likely never stopped in favor of executing another goal like in most other mobs.

- RabbitMoveControl#tick constantly updates the rabbits speed (Rabbit#setSpeedModifier). While doing this it also indirectly executes moveControl#setWantedPosition thus the rabbit always tries to reach it's last target even when it shouldn't do that.

Further helpful links:
- Video comparison showcasing the problems in more detail

- Reference implementations of the fixes

See also: MC-277500

### Comment 43: CreeperMagnet_ (2024-10-11T20:18:16.848-0700)

Affects 1.21.2-pre3.

### Comment 44: tryashtar (2024-10-17T00:23:25.050-0700)

Although this ticket is as old as 1.14, this issue got significantly worse in 1.20, specifically in 1.20-pre1, where rabbits seem to have completely lost their ability to do medium jumps during normal pathfinding. I think this is a genuinely new issue. However, new tickets describing the new issue continue to be resolved as duplicates of this ticket.
While this ticket describes rare or temporary issues where rabbits could get stuck in novel block arrangements, rabbits currently are incapable of jumping up a block unless panicking, so wild rabbits are found hopping uselessly into the side of a block nearly 100% of the time now within seconds.
I think that since this issue was triaged before 1.20-pre1 where the issue became significantly worse, either it should be re-triaged or a new ticket should be created.
