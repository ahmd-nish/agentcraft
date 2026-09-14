# MC-97423: Horse temporarily stuck in jump animation if dismounted

**Mojira URL:** [https://bugs.mojang.com/browse/MC-97423](https://bugs.mojang.com/browse/MC-97423)

## Report details

- **Mojira categories:** Mob behaviour
- **Project:** MC
- **Issue key:** MC-97423
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2016-02-17T18:05:32.977-0800
- **Updated:** 2025-05-20T02:11:32.401-0700
- **Resolution date:** 2025-05-13T03:08:44.888-0700
- **Affects versions:** Minecraft 1.9 Pre-Release 1; Minecraft 1.9 Pre-Release 2; Minecraft 1.9.1 Pre-Release 3; Minecraft 1.9.2; Minecraft 16w15b; Minecraft 1.9.3 Pre-Release 1; Minecraft 1.9.3 Pre-Release 2; Minecraft 1.9.3 Pre-Release 3; Minecraft 1.10; Minecraft 1.10.1; Minecraft 1.10.2; Minecraft 16w32a; Minecraft 16w32b; Minecraft 16w33a; Minecraft 16w35a; Minecraft 16w36a; Minecraft 16w39b; Minecraft 16w39c; Minecraft 16w41a; Minecraft 16w43a; Minecraft 16w44a; Minecraft 1.11 Pre-Release 1; Minecraft 1.11; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 1.12; Minecraft 1.12.1; Minecraft 1.12.2 Pre-Release 1; Minecraft 1.12.2 Pre-Release 2; Minecraft 1.12.2; Minecraft 17w43a; Minecraft 17w43b; Minecraft 17w45a; Minecraft 17w45b; Minecraft 17w46a; Minecraft 17w47a; Minecraft 17w47b; Minecraft 17w48a; Minecraft 17w49a; Minecraft 17w49b; Minecraft 18w10d; Minecraft 18w16a; Minecraft 1.13.1; Minecraft 1.14.2; 1.14.4; 19w37a; 1.15.2; 20w10a; 1.16 Pre-release 6; 1.16.2; 1.16.4; 20w48a; 21w03a; 21w05b; 1.17.1; 1.19.2; 25w09b; 1.21.5
- **Fix versions:** Minecraft 1.13; 25w20a
- **Area:** Gameplay
- **Labels:** animation; horse; jump
- **Votes:** 5
- **Watchers:** 2
- **Attachments:** 3
- **Attachment filenames:** 2016-02-17_18.53.02.png; 2022-09-29_13.53.04.png; Minecraft 16w35a horse jump animation bug video.mp4
- **Issue links:** Duplicate:inward:MC-280364:Jumping with a horse and then dismounting mid-air keeps playing the jumping animation after landing. | Duplicate:inward:MC-295712:Horses keep jump animation when dismounted in the jump sequence   | Duplicate:inward:MC-295875:Horse stuck in jump animation after dismount in air | Duplicate:inward:MC-295911:If you exit a horse, donkey or a mule in jumping animation, it won't stop playing the animation. | Duplicate:inward:MC-295995:Horse Rearing Stuck | Relates:inward:MC-256464:If a horse is not on the ground while the player jumps, it will still play the jump animation | Duplicate:inward:MC-296588:Horse remains in jump animation after dismounting immediately | Duplicate:inward:MC-175155:Horse animations | Duplicate:inward:MC-170428:Horse stays in the air after jumping and getting off | Duplicate:inward:MC-128782:Horse bug in the last snapshot | Duplicate:inward:MC-127222:When I get off the horse during the jump, the horse blocks the animation | Duplicate:inward:MC-123343:Horse stuck in mid air when dismounting | Duplicate:inward:MC-123261:dancing horse bug | Duplicate:inward:MC-123035:Exit horse while jumping in water pauses state until ai change | Duplicate:inward:MC-121894:Horse model becoming frozen in jump pose | Duplicate:inward:MC-121869:Horses are still in the jumping animation when players stop riding horses when the horse is jumping. | Duplicate:inward:MC-121761:Horse Bug 1.13 | Duplicate:inward:MC-121626:Riding and dismounting a horse will remain it to stay on its hind legs | Duplicate:inward:MC-108687:Horse Animation bug / Stored horse jump bug | Duplicate:inward:MC-106754:Horse jump animation bug | Duplicate:inward:MC-99365:Dismounting horse while jumping causes horse to stay on hind legs | Duplicate:inward:MC-296752:2-legged horse & mule | Duplicate:inward:MC-296947:Horse animation gets stuck after jumping into water | Duplicate:inward:MC-297177:Horse animation gets stuck after dismounting mid-air | Duplicate:inward:MC-297253:Horses use swimming animation on land | Duplicate:inward:MC-297349:Wrong animation when dismounting from a horse (all types), mule and donkey | Duplicate:inward:MC-297495:Horse/Donkey/Mule Stuck in Jump animation following Jump and Dismount | Duplicate:inward:MC-298069:Horse rear up for a long time

## Description

The bug
If you dismount a horse in mid jump, the horse will continue to do the jump animation even after landing on the ground for around 10 seconds. The horse will even start to walk away stuck in the animation until it ends.
How to reproduce
- Tame a horse and put a saddle on it

- Start riding it

- Hold the jump key (space)

- Release the jump key and at the same time press the dismount key (shift)
 The horse remains in the jump animation

The reason (by MC-104523)
The following is based on a decompiled version of Minecraft 1.9 using MCP 9.24 beta.
I assume that the reason for this is that rearing is only done client side. The method net.minecraft.entity.passive.EntityHorse.onUpdate() contains a part that causes the horse to stop rearing. The following conditions are used. Keep in mind that they are all required and in Java if one condition fails all following conditions are not tested.
- If controlling passenger is a player:
- True condition: Player is client player

- False condition: Code is run by server

- Horse is rearing for more than 0 ticks

- Add one to horse rearing time, new value has to be greater than 20

If all these conditions are met the rearing value is set to false. This means that as soon as the player dismounts the horse, the rearing time stops incrementing.
When the client receives a SPacketEntityMetadata packet, the rearing state updates, because the value if the horse is rearing or not is stored with other states in the data watcher as one value (single bits of the value representing the value of the states) and rearing is only client side.
Removing the condition that the controlling passenger has to be a player would probably fix this bug.

## Comments (20)

### Comment 1: migrated (2016-02-17T18:05:32.977-0800)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: JUE13 (2016-02-19T01:08:14.293-0800)

Confirmed for 1.9-pre2.

### Comment 3: SunCat (2016-03-12T08:08:16.851-0800)

Still in 1.9.1-pre3

### Comment 4: SunCat (2016-04-13T13:58:37.477-0700)

Still in 16w15b

### Comment 5: [Mod]Les3awe (2016-04-24T06:20:54.693-0700)

Confirmed for 1.9.3-pre1

### Comment 6: [Mod]Les3awe (2016-04-30T01:45:53.854-0700)

Confirmed for 1.9.3-pre2

### Comment 7: [Mod]Les3awe (2016-05-03T06:31:49.604-0700)

Confirmed for 1.9.3-pre3

### Comment 8: [Mod]Les3awe (2016-06-17T10:45:42.149-0700)

Confirmed for 1.10.

### Comment 9: [Mod]Les3awe (2016-06-22T10:52:53.701-0700)

Confirmed for 1.10.1.

### Comment 10: migrated (2016-07-07T07:54:20.852-0700)

Can confirm 1.10.2.
Also if timed perfectly, if you dismount right before the jump, the horse will get stuck in the animation but not jump until a player gets back on.

### Comment 11: marcono1234 (2016-09-03T03:20:48.443-0700)

Relates to MC-104523

### Comment 12: [Mod]Les3awe (2018-07-21T11:10:38.075-0700)

Seems to be fixed at 1.13.

### Comment 13: migrated (2018-10-08T10:45:58.178-0700)

Not fixed, still in 1.13.1. (Can take some time to get it)

### Comment 14: migrated (2020-03-05T01:17:32.307-0800)

Can still replicate in 1.15.2 https://youtu.be/fe3fUW-J084
Was reading incoming packets, and found this bug, i'm not modifying the packet at all, just reading, and it appears that when the client sends a dismount and jump boolean in the steer vehicle packet at the same time, the horse gets stuck in a jumping animation.

### Comment 15: migrated (2020-06-01T19:53:36.675-0700)

Can Confirm Java 1.15.2, the stuck state applies to both the player and the horse.
To explain, If I have the horse sprinting and dismount while it is, my PC remains in a constant sprinting state, even if I stop moving and start again.
The second scenario is if my horse is bucking and I dismount while it is in this animation, it continues to buck while strolling around.
In both cases, I jumped on the horse again within 8-10 seconds and jumped off and things returned to normal, although I didn't notice once or twice when i hopped off and was sprinting around easily without having to press extra buttons – double tap forward or ctrl.

### Comment 16: ItsTinay (2020-08-30T08:34:31.572-0700)

Confirmed for 1.16.2

### Comment 17: Avoma (2020-11-26T11:27:31.948-0800)

Can confirm in 20w48a.

### Comment 18: Avoma (2021-02-03T03:54:26.569-0800)

Can confirm in 21w03a.

### Comment 19: Avoma (2021-02-07T02:45:57.821-0800)

Can confirm in 21w05b.

### Comment 20: NicoVA (2025-03-26T22:31:23.227-0700)

Can confirm in 1.21.5
