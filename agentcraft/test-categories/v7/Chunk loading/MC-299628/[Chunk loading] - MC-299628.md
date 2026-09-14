# MC-299628: Mounted players/mobs trigger sculk sensors on world load

**Mojira URL:** [https://bugs.mojang.com/browse/MC-299628](https://bugs.mojang.com/browse/MC-299628)

## Report details

- **Mojira categories:** Chunk loading; Game Events
- **Project:** MC
- **Issue key:** MC-299628
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2025-07-10T21:53:57.992-0700
- **Updated:** 2025-07-23T00:39:42.936-0700
- **Resolution date:** 2025-07-23T00:39:42.853-0700
- **Affects versions:** 1.21.7
- **Fix versions:** 25w31a
- **Area:** Platform
- **Votes:** 1
- **Watchers:** 0
- **Attachments:** 0

## Description

The minecraft:entity_mount game event, which triggers nearby sculk sensors with a vibration frequency of 6, is normally caused by an entity mounting another entity. However, the event appears to also be triggered by already-mounted entities when the world is loaded, unexpectedly triggering nearby regular and calibrated sculk sensors.
Steps to reproduce
With a player
- Place one sculk sensor and one calibrated sculk sensor. Feed a redstone signal strength of 6 into the calibrated sculk sensor’s input port.

- Summon a mountable mob or other mountable entity (e.g. minecart, boat, horse, happy ghast) within the radius of the sculk sensors.

- While located within the radius of the sculk sensors, disconnect from the world, then reload.
-  sculk sensors are not triggered

- Mount on the mob/other entity.
-  both sculk sensors are triggered as the player has mounted on the mob/other entity

- While seated on the mob/other entity, disconnect from the world, then reload.
-  both sculk sensors are triggered again

- Expected result: the sculk sensors do not trigger again, as the player is already mounted on the mob/other entity

With mobs/other entities
- Place one sculk sensor and one calibrated sculk sensor. Feed a redstone signal strength of 6 into the calibrated sculk sensor’s input port.

- Summon two entities within the radius of the sculk sensors. Ensure one entity can be ridden by the other.

- Disconnect from the world, then reload.
-  sculk sensors are not triggered

- Use the /ride command to make one entity ride the other. Ensure the entities are within the radius of the sculk sensors.
-  both sculk sensors are triggered as an entity has mounted upon another entity

- Disconnect from the world, then reload.
-  both sculk sensors are triggered again

- Expected result: the sculk sensors do not trigger again, as the entities were already mounted on each other

## Comments (0)

No comments were available in the downloaded comment corpus.
