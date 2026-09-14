# MC-267955: Breezes that are not moving cannot deflect non-arrow and non-trident projectiles

**Mojira URL:** [https://bugs.mojang.com/browse/MC-267955](https://bugs.mojang.com/browse/MC-267955)

## Report details

- **Mojira categories:** Mob behaviour; Parity; Projectiles
- **Project:** MC
- **Issue key:** MC-267955
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2024-01-18T08:56:11.754-0800
- **Updated:** 2025-04-29T10:44:20.033-0700
- **Resolution date:** 2024-02-15T05:01:18.263-0800
- **Affects versions:** 24w03b; 24w04a; 24w06a
- **Fix versions:** 24w07a
- **Area:** Expansion B
- **Labels:** breeze
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2024-02-15_17.25.12.png; 2024-02-15_17.25.12-1.png; 2024-02-15_17.25.19.png; MC-267955.png
- **Issue links:** Relates:outward:MC-268080:When the projectiles are reflected from the breeze, the projectiles will deflect in the opposite direction in Bedrock, but in Java they will always deflect downward | Relates:inward:MC-268563:Snowballs, eggs, experience bottles, and ender pearls are destroyed instead of being deflected when hitting breezes | Duplicate:inward:MC-268079:Snowballs, eggs and ender pearls break when hitting breeze

## Description

The Bug:
Breezes that are not moving cannot deflect non-arrow and non-trident projectiles.
The 24w03a article states that breezes can now deflect all projectiles, however, breezes that are not moving cannot deflect non-arrow and non-trident projectiles. Breezes can only deflect non-arrow and non-trident projectiles while moving.
Steps to Reproduce:
- Summon a breeze and obtain some snowballs.

- While the breeze isn't moving, throw some snowballs at it.

Observed Behavior:
Breezes that are not moving cannot deflect non-arrow and non-trident projectiles.
Expected Behavior:
Breezes that are moving or not moving would be able to deflect non-arrow and non-trident projectiles.

## Comments (6)

### Comment 1: migrated (2024-01-18T08:56:11.754-0800)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: syarumi (2024-01-18T11:49:31.679-0800)

Confirmed. This deflecting behavior of breezes doesn't seem to be working correctly, as it is extremely hard to get it working, so one would assume they just don't deflect them at all (aside from arrows/tridents). This is also supported by the fact that the "Breeze deflects" sound sometimes isn't played.
Most of the time, most projectiles just get destroyed instead of being deflected, such as:
- Snowballs

- Eggs

- Ender pearls (you are teleported to the entity)

- Small fireballs

- Shulker bullets

Fishing rod's bobber gets "deflected" but not towards the direction of the shooter, the breeze just blocks it. Llama spits don't get deflected but instead go through the breeze without damaging it.

### Comment 3: 4ebugger (2024-01-25T00:20:57.854-0800)

This is also a party issue, in Bedrock Edition it works correctly.

### Comment 4: Avoma (2024-02-14T08:55:43.341-0800)

This issue has been fixed in 24w07a.

### Comment 5: 4ebugger (2024-02-15T01:24:06.069-0800)

Still not fixed.

### Comment 6: Avoma (2024-02-15T04:45:14.961-0800)

that is a different issue () so I'll be keeping this ticket resolved as Fixed. We know that breezes now deflect snowballs, experience bottles, eggs, and ender pearls in 24w07a because the "Breeze deflects" sound is now produced, which wasn't the case in 24w06a. The problem that you're experiencing is that snowballs, experience bottles, eggs, and ender pearls are destroyed when deflected by breezes which is being tracked at .
