# MC-211096: Entities in cobwebs clip though pistons

**Mojira URL:** [https://bugs.mojang.com/browse/MC-211096](https://bugs.mojang.com/browse/MC-211096)

## Report details

- **Mojira categories:** Collision; Entities
- **Project:** MC
- **Issue key:** MC-211096
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-01-10T13:44:02.279-0800
- **Updated:** 2026-03-22T19:25:57.218-0700
- **Resolution date:** 2025-10-02T04:33:52.992-0700
- **Affects versions:** 1.16.4; 1.16.5; 21w05b; 21w13a; 1.19.4; 23w14a; 1.21.3; 24w45a
- **Fix versions:** 1.21.10 Release Candidate 1
- **Area:** Platform HC
- **Labels:** cobweb; entity; piston; piston-extension
- **Votes:** 2
- **Watchers:** 2
- **Attachments:** 9
- **Attachment filenames:** Minecart_clipping.mp4; Minecart_clipping.mp4; mynd-20260323-022337.png; Setup1.png; Setup1.png; Setup2.png; Setup2.png; Setup3.png; Setup3.png
- **Issue links:** Duplicate:inward:MC-278255:Pistons fail to push entities when these are inside cobweb/powder snow

## Description

The bug:
The entity is moved up ~0.05 blocks (established using carpets mod's tick freeze) and becomes stuck in the piston head. On versions 1.2.1-1.19.4, when the piston is retracted, the entity clips into the piston body and sinks through the cobweb.
Expected Result:
The piston to push the entity up a full block and the entity to sink through the cobweb.
Steps to Reproduce:
- Place piston, facing upwards

- Place rail on top of piston

- Place cobweb to the top and left of the piston

- Place minecraft on the rail and break the rail

- Nudge the minecart into the cobweb

- Ensure there are no block underneath the cobweb

- Power and de-power the piston (slowly)

See the video and photos for more information on how to setup this glitch.
Responses:
Now tested for all spawn egg mobs (in response to Marty Mcfly):
- Doesn't affect Spiders / Cave spiders, as these mobs are not slowed by cobwebs.

- Doesn't affect flying mobs (Bees, Bats, Ghasts, Phantoms) or mobs summoned with

```
/summon minecraft:creeper ~ ~ ~ {NoGravity:1b}
```

Now tested for short duration pulses (in response to Gnamf Jojo):
- Works for all pulses, down to 0-tick pulses (make sure there's no block under the cobweb)

Updates:
When a player is pushed within the cobweb, they are put into swim mode.
This glitch also affects Minecarts that are still on rails.
Code analysis
Code analysis by  can be found in this comment.

## Comments (14)

### Comment 1: migrated (2021-01-10T13:44:02.279-0800)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: migrated (2021-01-10T13:44:02.279-0800)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 3: migrated (2021-02-07T09:04:47.735-0800)

Can confirm.
Affects 21w05b

### Comment 4: migrated (2021-02-07T09:04:47.735-0800)

Can confirm.
Affects 21w05b

### Comment 5: migrated (2021-02-07T12:12:40.293-0800)

This seems to affect all entities.

### Comment 6: migrated (2021-02-07T12:12:40.293-0800)

This seems to affect all entities.

### Comment 7: migrated (2021-02-09T08:00:10.581-0800)

Agree. Affects all entities. Can reproduce. Does not work if using an impules to power piston

### Comment 8: migrated (2021-02-09T08:00:10.581-0800)

Agree. Affects all entities. Can reproduce. Does not work if using an impules to power piston

### Comment 9: Avoma (2021-04-02T04:31:53.678-0700)

Can confirm in 21w13a.

### Comment 10: haykam (2023-03-26T20:20:32.553-0700)

Can confirm in Minecraft 1.19.4. It also affects powder snow (when moving horizontally) and sweet berry bushes.
Code analysis (Yarn mappings)
Cobwebs, powder snow, and sweet berry bushes use the Entity#slowMovement method as well to affect movement. This method sets a multiplier field which is used to multiply the movement distance when the Entity#move method is called. Typically, this allows a multiplier to be set for when the entity updates its position in the next tick.
However, additional movement can be applied from other sources, such as pistons and shulkers. In these cases, the movement multiplier affects the external source of movement rather than the entity's own movement.
To fix this issue, the Entity#move method should simply check the MovementType before applying the movement multiplier.

### Comment 11: haykam (2023-04-11T11:03:20.183-0700)

This behavior still exists in Minecraft snapshot 23w14a.

### Comment 12: migrated (2024-11-13T02:34:55.320-0800)

Can confirm in 24w45a.
This bug is related to this bug report too: MC-278182
It is crucial to fix this bug for proper, consistent behavior from item entities when moved by pistons
's bug solution would be valid, as explained here: MC-278255
Furthermore, powder snow can cause the same bug too (1.17+ as the block was introduced back then)

### Comment 13: migrated (2024-11-13T02:34:55.320-0800)

Can confirm in 24w45a.
This bug is related to this bug report too: MC-278182
It is crucial to fix this bug for proper, consistent behavior from item entities when moved by pistons
's bug solution would be valid, as explained here: MC-278255
Furthermore, powder snow can cause the same bug too (1.17+ as the block was introduced back then)

### Comment 14: AshleyRedstone (2026-03-22T19:25:57.218-0700)

fixing this “issue“ affects an extremely common setup used for powering pressure plates/strings with a long delay, the carts clipping inside the pistons is due to the carts being slowed down and thus the piston cannot push it any further up, over half of creations in the door community have broken due to this change and many of them are impossible to fix
