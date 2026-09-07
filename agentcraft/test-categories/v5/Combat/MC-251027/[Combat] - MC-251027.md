# MC-251027: Wearing a helmet doesn't reduce the damage of falling anvils or stalactites by 1⁄4

**Mojira URL:** [https://bugs.mojang.com/browse/MC-251027](https://bugs.mojang.com/browse/MC-251027)

## Report details

- **Mojira categories:** Combat; Items
- **Project:** MC
- **Issue key:** MC-251027
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-04-28T04:15:34.878-0700
- **Updated:** 2025-04-11T10:36:37.294-0700
- **Resolution date:** 2023-12-08T01:48:43.570-0800
- **Affects versions:** 1.18.2; 1.20.1; 1.20.2
- **Fix versions:** 23w51a
- **Area:** Gameplay
- **Game mode:** Survival
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** 1.png; 2.png; 3.png; 4.png; 5.png; 6.png
- **Issue links:** Relates:outward:MC-243085:Anvils no longer cause extreme durability damage to helmets

## Description

Helmets do not reduce the damage taken from falling anvils or stalactites by 1/4. They still reduce the damage by a small amount, but not more than wearing any other armor piece, despite still taking twice the durability damage as other armor pieces.
Steps to Reproduce:
- Setblock an anvil or summon a falling block above you.
- This may be easier to visualize if you spawn the anvil higher to deal more damage and disable the "natural regeneration" gamerule.

- Observe the damage taken.

- Restore yourself to full health, and repeat the previous steps while wearing only a helmet.

- Repeat the test again but with a different single armor piece instead of the helmet.

The helmet only provides a small damage reduction in line with what would be normally expected from armor pieces; chestplaces and leggings provide more damage reduction due to having more defense points. However, the helmet still takes increased durability damage.

## Comments (3)

### Comment 1: migrated (2022-04-28T04:15:34.878-0700)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: ampolive (2022-04-28T04:40:59.680-0700)

The images show that the helmet still reduces the damage, just not as much as 1.16.5. The durability not being reduced as much is intended as per MC-243085.

### Comment 3: Sonicwave (2023-08-21T21:35:51.489-0700)

Reopened and confirmed as I believe this to be a different issue than MC-243085. In LivingEntity:hurt() the damage value is multiplied by 0.75, but only after the damage has been dealt to the player, so it has no effect. It does seem to change the amount of damage passed to the minecraft:entity_hurt_player advancement trigger however.
Also, the helmet still takes twice the durability damage as normal, though not nearly as much as described in MC-243085, despite providing no more damage reduction than other armor pieces.
