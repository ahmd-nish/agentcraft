# MC-307407: Vertical velocity after bouncing does not take drag into consideration

**Mojira URL:** [https://bugs.mojang.com/browse/MC-307407](https://bugs.mojang.com/browse/MC-307407)

## Report details

- **Mojira categories:** Player
- **Project:** MC
- **Issue key:** MC-307407
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Community Consensus
- **Mojang priority:** Normal
- **Created:** 2026-04-09T04:23:21.643-0700
- **Updated:** 2026-05-05T02:59:06.588-0700
- **Resolution date:** 2026-05-05T02:59:06.520-0700
- **Affects versions:** 26.2 Snapshot 1; 26.2 Snapshot 2; 26.2 Snapshot 3
- **Fix versions:** 26.2 Snapshot 6
- **Area:** Expansion A
- **Votes:** 11
- **Watchers:** 3
- **Attachments:** 1
- **Attachment filenames:** bounce (64646c88-0ad1-42e8-a995-e60d8d5ce28f).mp4

## Description

26.2-snapshot-1 introduced new physics for bouncing meant to consistently retain the players ‘momentum’ after a bounce. Previously when bouncing on a slime or bed your vertical delta movement was just mirrored, whereas now there is a new gravityCompensation factor given by (movement.y / currentMovement.y) * this.getEffectiveGravity()that gets added additionally. The idea here is that the velocity after the bounce should be continuously increasing depending on the height you’re falling from, but this fails (especially noticable with high values of air_drag_modifier) because this calculation doesn’t consider the role of drag. If portionWithMovement = movement.y / currentMovement.y is very close to 1, then we would want the resulting velocity to be very similar to the velocity after an extra tick of falling. If we denote the velocity before bouncing with v (disregarding - sign), then the current code gives a resulting velocity of close to v + this.getEffectiveGravity(), whereas falling an extra tick would result in the velocity 0.98 * (v + this.getEffectiveGravity()) with usual air drag. A correct implementation would also need to use portionWithMovement to approximate the drag factor of 0.98 or whatever the value needs to be for different air_drag_modifier attribute values.
I have attached a video bounce.mp4 in which the effects of this are clearly noticable when using air_drag_modifier 3.0. Even though I am jumping from almost a block higher, the resulting bounce does not reach as high.
This is related to MC-307398, but I believe that report has been prematurely resolved and a potential fix would probably be greatly appreciated by a lot of players.

## Comments (6)

### Comment 1: Automation for Jira (2026-04-09T04:23:32.831-0700)

Thank you for helping us improve Minecraft! We saved your files:

### Comment 2: Mrdoggy (2026-04-09T16:14:25.606-0700)

Can confirm in 26.2-snapshot-2

### Comment 3: [MCQA] Baslod (2026-04-15T05:08:50.388-0700)

Thank you for your report!
However, this issue has been temporarily closed as Awaiting Response.
To make your bug report as effective as possible, please try and include the following steps to reproduce the problem:
Steps to Reproduce:
1.
2.
3.
Observed Results:
(Briefly describe what happens)
Expected Results:
(Briefly describe what should happen)
This ticket will automatically reopen when you reply.
Quick Links:
📓 Issue Guidelines – 💬 Mojang Support – 📧 Suggestions – 📖 Minecraft Wiki

### Comment 4: Z0rty (2026-04-15T10:02:50.365-0700)

@[MCQA] Baslod
My attached video shows a clear setup that is very easy to reproduce and the problem should be extremely obvious. I already went through a lot of effort to point out the exact issue and I have absolutely no clue what further you want from me.

### Comment 5: Evandyrr (2026-04-15T12:49:14.390-0700)

can reproduce in 26.2 snapshot 3

- place two towers next to eachother, 6 blocks tall, one has a chest on top to make it 7 blocks tall

- in front of the towers, place 4 blocks of slime as a square

- in front of the slime, place two 3 block tall towers with the third block being enchantment tables

- run the command

```/attribute @s air_drag_modifier base set 3```

- jump onto the slime

on the shorter tower without the chest, you can land on the enchantment table
on the taller tower with the chest, you cannot bounce high enough to make it to the enchantment table

### Comment 6: gnembon (2026-04-30T14:20:05.089-0700)

I believe portion of the drag to compensate would be:

```effectiveDrag = Mth.lerp(portionWithMovement, 1.0f, getAirDrag());```
as it should be  → 1 with portion → 0 and → air_drag when portion → 1
then applied to the simulated path traveled:

```(gravityCompensation - currentMovement.y) * effectiveDrag * restitution```
With the repro it seems to work just fine. Will push it out next snap and you can test it out.
