# MC-275298: Blocks with special collision behavior have a larger detection range than previously

**Mojira URL:** [https://bugs.mojang.com/browse/MC-275298](https://bugs.mojang.com/browse/MC-275298)

## Report details

- **Mojira categories:** Collision
- **Project:** MC
- **Issue key:** MC-275298
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-08-15T12:39:01.861-0700
- **Updated:** 2025-04-28T12:00:38.301-0700
- **Resolution date:** 2024-09-09T03:32:59.275-0700
- **Affects versions:** 24w33a; 24w34a
- **Fix versions:** 24w36a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 11
- **Attachment filenames:** 2024-08-15_14.34.29.png; 2024-08-15_14.35.48.png; 2024-08-15_14-37-38.mp4; 2024-08-15_14-51-54.mp4; 2024-08-20 191529.png; 2024-08-20 191600.png; 2024-08-20 193640.png; Minecraft 2024.08.16 - 14.47.10.03.mp4; Minecraft 2024.08.16 - 14.52.12.04.mp4; photo_2024-08-20_19-05-57.jpg; photo_2024-08-20_19-07-37.jpg
- **Issue links:** Relates:outward:MC-275437:Fast moving entities freeze the server which causes watchdog crash | Duplicate:inward:MC-275251:Nether Portal's effect range is larger than a complete block now | Duplicate:inward:MC-275250:Player can be lit on fire by a lava cauldron when standing next to it | Duplicate:inward:MC-275320:Lava cauldrons burn you while standing outside | Duplicate:inward:MC-275337:Lava cauldrons deal damage to players next to it | Duplicate:inward:MC-275342:colliding with an edge of a block that has a block with no collision box on top to still be affected by it's properties | Duplicate:inward:MC-275376:Lava cauldron has bigger hurt box | Duplicate:inward:MC-275385:You can take campfire damage  in a block. | Duplicate:inward:MC-275390:Players can enter the nether portal outside the portal | Duplicate:inward:MC-275420:When the player is standing on the block next to a bubble colomn he start shaking. | Duplicate:inward:MC-275472:Entities travel through portals even if standing outside the portal frame | Duplicate:inward:MC-275495:you can go up without touching to soul sand water | Duplicate:inward:MC-275522:Player's hitbox collides with stuff it shouldn't collide with | Duplicate:inward:MC-275590:Portal Block Hitbox is bigger than one block | Duplicate:inward:MC-275768:Player hitbox interaction through corner blocks with water bubble column | Duplicate:inward:MC-275785:Entities can travel through blocked off nether portals | Duplicate:inward:MC-275788:Player can pass through nether portal by touching the portal frame | Duplicate:inward:MC-275812:Items thrown against the side of a lava cauldron are destroyed | Duplicate:inward:MC-275841:Player will hit the block even player should not hit it | Duplicate:inward:MC-276002:When you touch the obsidian border of a nether portal, you will go straight to the portal | Duplicate:inward:MC-276125:Lava cauldrons, campfires and wither roses cause damage when touching the side of the block | Duplicate:inward:MC-276135:Lava Cauldron Burns On Touching The Sides | Duplicate:inward:MC-276149:Player hitbox is too large | Duplicate:inward:MC-276227:Liquids inside Cauldrons affect the player touching the outside of the cauldron. | Duplicate:inward:MC-276256:Not sure what exactly happened, but my pigs were destroyed. | Relates:inward:MC-276375:It's possible to get slowed down by unreachable cobwebs

## Description

Blocks with special collision behavior have wider ranges than before in 1.21.1 when standing up against these blocks.
Affected Blocks:
(Comment for any I missed)
- Honey block

- Fire

- Powder snow

- Nether portals

- Cauldrons

- Bubble Columns

- Cobwebs

- Soul Fire

- End Gateways

- Sweet Berries

- Big Dripleaf

Steps to Reproduce:
- Recreate this simple setup:

- Place down any of the affected blocks on top of the red wool

- Stand half against the white concrete, and half against the affected block

Expected Result:
None of the blocks would have their respective behaviors occur and affect the player, as this did not occur in 1.21.1, and the player is not actually inside of the block.
Observed Behavior:
The blocks will output their behaviors onto the player when standing against the concrete and affected block.
This also is not directional, as using an example where the player isn't standing next to a block, but above it, the same issue occurs:

Screenshots/Videos:

## Comments (11)

### Comment 1: migrated (2024-08-15T12:39:01.861-0700)

This comment contained multiple image attachments (11), please login to view the attachments.

### Comment 2: COMETC2021A1 (2024-08-15T19:46:22.835-0700)

This also affects:
Cobwebs
Soul Fire
End Gateways

### Comment 3: COMETC2021A1 (2024-08-15T19:59:36.187-0700)

And precisely, these blocks' detection range is 0.00001001192067636 blocks wider than a full block on each side.

### Comment 4: muzikbike (2024-08-16T02:34:28.927-0700)

Relates to:

### Comment 5: Ikiroux (2024-08-16T10:11:09.078-0700)

Can confirm, also affect water columns with soul sand when the player stand next to it.
Edit : it seem to affect the player even if he stands above and to the side, see the attached videos.

Can you pin my comment ?

### Comment 6: migrated (2024-08-17T09:57:20.574-0700)

it also affects sweet berries

### Comment 7: COMETC2021A1 (2024-08-20T09:01:41.120-0700)

Affected blocks+:
Campfire
Soul Campfire

### Comment 8: Savvvage_ (2024-08-20T09:11:07.292-0700)

Here is a full list of affected blocks:

This issue lies within the method that collects the block positions for collision. Previously entity hitbox was contracted by 10^-7 blocks so that if the entity intersected the block space of an interactable block by a tiny bit it didnt include it in the collision calculation, and since 24w33a the entity hitbox gets infltated instead which causes the issue
Old code:

New code:

### Comment 9: COMETC2021A1 (2024-08-21T08:16:57.443-0700)

Still in 24w34a

### Comment 10: migrated (2024-08-23T06:04:14.864-0700)

>COMETC2021A1
just a little question: how did you calculate that?

### Comment 11: migrated (2024-08-28T11:30:11.531-0700)

Also affects Wither Rose.
