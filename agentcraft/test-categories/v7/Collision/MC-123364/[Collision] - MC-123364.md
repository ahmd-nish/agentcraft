# MC-123364: Player-in-block checking happens after block collision events are done

**Mojira URL:** [https://bugs.mojang.com/browse/MC-123364](https://bugs.mojang.com/browse/MC-123364)

## Report details

- **Mojira categories:** Collision; Player
- **Project:** MC
- **Issue key:** MC-123364
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2017-12-17T22:01:07.644-0800
- **Updated:** 2026-04-18T03:04:27.488-0700
- **Resolution date:** 2026-04-18T03:03:50.613-0700
- **Affects versions:** Minecraft 1.12.2; Minecraft 17w50a; Minecraft 18w22c; Minecraft 1.13-pre1; Minecraft 1.13-pre2; Minecraft 1.13-pre3; Minecraft 1.13-pre4; Minecraft 1.13-pre5; Minecraft 1.13-pre6; Minecraft 1.13-pre8; Minecraft 1.13; Minecraft 18w30b; Minecraft 18w32a; Minecraft 1.13.1-pre1; Minecraft 1.13.1-pre2; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 1.14 Pre-Release 2; Minecraft 1.14 Pre-Release 3; Minecraft 1.14.4 Pre-Release 2; 1.15.2; 20w10a; 20w51a; 21w03a; 1.16.5; 21w05b; 21w08b; 21w13a; 21w17a; 1.17.1; 22w15a; 1.19.2; 1.20.6; 24w18a
- **Fix versions:** 24w21a
- **Area:** Platform
- **Labels:** collision; movement; player
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 2017-12-18_00.00.38.png; 2017-12-18_02.16.40.png; MC-123364.mp4
- **Issue links:** Relates:outward:MC-98153:Portals generate far-away chunks & set player on fire | Relates:outward:MC-89928:Portals not placing the player at correct coordinates causing them to take suffocation damage | Duplicate:inward:MC-223409:Opening a shulker box under an end portal causes you to go to the end, but with your overworld coords | Duplicate:inward:MC-222251:Wrong Warp to End Possible

## Description

The bug
The NetHandlerPlayServer.processPlayer (MCP name) function checks if the player's bounding box is intersecting any blocks, and if it is, reverts the player's position to the old one.
However, this check is done even if the player has been teleported by a portal block such as the end portal, which can lead to the following problem:
- A player somehow sends a move packet that places them halfway between an end portal block and an end portal frame block

- Even though the move is illegal, the end portal's collision function gets called and the player is teleported into the end (Bug 1)

- The collision checks whether the player's move was invalid and reverts the player's position, but not dimension change (Bug 2)

- The player is dropped into the end at their previous position, likely causing them to fall into the void and die

Doing this check before block collision functions are called (or at least also cancelling the dimension change) would solve the problem.
How to reproduce
- Use the following commands to make you intersect with a block and stand in front of an end portal

```
/setblock ~2 ~ ~ end_portal
/setblock ~1 ~ ~1 glass
/execute align xz run teleport @s ~1.7 ~ ~0.700005 -60 0
```

- Walk forward
→  You enter the end but at your original position instead of on the platform

## Comments (14)

### Comment 1: migrated (2017-12-17T22:01:07.644-0800)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: pokechu22 (2017-12-17T22:17:19.568-0800)

Do you have a way to reproduce this without modifying the client to send a custom packet?  I know it's possible for collision to behave poorly, I'm just not aware of a concrete way to reproduce this as-is (I'd like to try to reproduce on the snapshot, where sending other packets is rather difficult)
The portals/dimension change logic is definitely broken, though (see MC-98153).  Were that less broken, would this still be an issue?  I'm pretty sure it would still be, as the blocks would be triggered when they shouldn't be.

### Comment 3: migrated (2017-12-17T23:29:49.992-0800)

Yes, I just figured it out how to do it:
1. Build this:

2. Stand on the block right next to the corner of the end portal
3. Place a bed on the block you're standing on (so that its corner touches the corner of the end portal), and you should be inside the bed block (this is another bug, I'm guessing)
4. Sneak to the left edge (in the image) of the block the bed is on
5. Once you're right at the edge, try going back into the bed block, still sneaking. You should see your player jumping backwards while you hold W as the server cancels the move events.
6. Move along the bed's edge towards the portal (at an approximately 10-20 degree angle towards the bed). Make sure you keep getting the jumps back as you move which show the collision checking code is being activated.
7. When you eventually reach the portal block, you should get teleported into the end, but at your current coordinates. It might not happen on the first attempt.

### Comment 4: pokechu22 (2017-12-18T00:06:28.092-0800)

Thanks!  Can confirm.
The trick with the bed doesn't work in the snapshots anymore, but the goal of it is just to get you stuck inside of a block slightly, which can be done other ways.  Here's my setup:
- Build up this; note in particular the facing direction (needed for the teleport)

- Push yourself into the corner of the two glass blocks

- Run /tp @p ~ ~ ~-.01.  This should push you just barely inside the glass so that other movement is rejected

- Break the glass block on top of the portal

- Walk diagonally forward (so that you'd move "into" the other glass block)

- This bug should occur

### Comment 5: marcono1234 (2017-12-21T13:10:50.518-0800)

I added reproduction steps based on what both of you provided, I hope you are fine with that.

### Comment 6: pokechu22 (2020-03-08T19:47:03.044-0700)

Confirmed for 1.15.2; however, the command needs to be modified slightly: a teleportation of ~.700005 works for getting stuck in a block, but ~.75 no longer does.  1.14.2-pre4 changed the tolerance from 0.0625D to .00001F (this might have been related to MC-147715, but there was another change in Entity that's more likely for that).  (1.14.2-pre4 changed it in one instance, while 1.14.2 proper changed a second instance and moved both into a method I now have called isPlayerNotInBlock (func_223133_a).  .0625 is still used in several places though.  The whole hitbox shrinking thing is pretty weird and I don't know why it's done, but at least .00001 won't cause issues similar to MC-104259).

### Comment 7: Avoma (2020-12-26T08:22:35.512-0800)

Can confirm in 20w51a.

### Comment 8: Avoma (2021-02-01T06:33:50.061-0800)

Can confirm in 21w03a.

### Comment 9: Avoma (2021-02-08T01:37:23.058-0800)

Can confirm in 21w05b.

### Comment 10: Avoma (2021-03-02T00:59:01.970-0800)

Can confirm in 1.16.5 and 21w08b.

### Comment 11: Avoma (2021-08-22T08:55:25.988-0700)

Can confirm in 1.17.1. Video attached.

### Comment 12: jamesmoton (2022-04-18T04:27:30.695-0700)

Can confirm in 22w15a.

### Comment 13: Jeuv (2024-06-16T14:58:29.874-0700)

Can no longer confirm in 1.21.

### Comment 14: Xyme (2025-12-22T05:18:36.567-0800)

From my testing, this seems to no longer work since 1.20.5
