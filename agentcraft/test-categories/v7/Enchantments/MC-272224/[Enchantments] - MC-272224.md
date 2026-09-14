# MC-272224: 'in_bounding_box' vertical position for 'spawn_particles' effect is anchored incorrectly

**Mojira URL:** [https://bugs.mojang.com/browse/MC-272224](https://bugs.mojang.com/browse/MC-272224)

## Report details

- **Mojira categories:** Enchantments; Particles
- **Project:** MC
- **Issue key:** MC-272224
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2024-05-19T11:42:28.874-0700
- **Updated:** 2025-04-29T09:03:40.810-0700
- **Resolution date:** 2024-05-31T02:55:27.399-0700
- **Affects versions:** 24w20a; 24w21b; 1.21 Pre-Release 1
- **Fix versions:** 1.21 Pre-Release 2
- **Area:** Platform
- **Labels:** enchant; enchantement; enchantment-effect
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 2024-05-19_20.29.00.png; 2024-05-29_20.07.09.png; bug.zip

## Description

While working on a project of mine, I noticed that when I set the 'vertical_position' config in the 'spawn_particles' effect in the 'post_attack' component, particles weren't spawning in the upper half of attacked mob's bounding box. After a few tests, I discovered that the missing particles were spawning below the hit mob, and the maximum downwards distance from the entity's bounding box was equal to half the height of its hitbox. This likely suggests that the particles are anchored at the attacked mob's feet rather than the center of its bounding box.
This does not happen with 'horizontal_position' or with any other effect component.

EDIT: after further further testing in 1.21-pre1, I can confirm that this happens with EVERY effect component. I don't know if its always been the case and I can't test it
Steps to reproduce
Below I have attached a data pack with a singular enchantment that can be applied to a Diamond Sword with '/enchant @s bug:particle_post_damage'. Simply apply the enchantment to the sword and attack any mob. Notice that no particles are spawning in the upper part of its bounding box, and if done over see-through blocks (Glass, Barriers, etc.), some particles spawn underground, below hit entity.

I have also attached a screenshot of the issue. Notice how a lot of particles spawn under the attacked Husk, but none spawn near its head (or generally in the upper part of its hitbox, as I have previously mentioned), but some spawn below the Iron Block floor. The Husk had had its scale attribute set to 3 for showcase purposes, but the issue also happens if the scale is set to 1 (default). I set my entity_interaction_range attribute to 100 so that I can attack it from a distance to make the particles as visible as possible

## Comments (3)

### Comment 1: migrated (2024-05-19T11:42:28.874-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: kohara (2024-05-19T11:44:13.845-0700)

I haven't tested it on versions earlier than 24w20a, but I am quite sure that this has been an issue since 24w18a, when the enchantments were made data-driven

### Comment 3: kohara (2024-05-29T11:10:43.966-0700)

UPDATE: I can confirm it still being that way in 1.21-pre1. Furthermore, I can confirm that this issue wasn't limited to just the 'post_attack' component, as it actually affects every effect component
