# MC-250966: Dying to the warden's sonic boom doesn't count as the warden's kill

**Mojira URL:** [https://bugs.mojang.com/browse/MC-250966](https://bugs.mojang.com/browse/MC-250966)

## Report details

- **Mojira categories:** Statistics
- **Project:** MC
- **Issue key:** MC-250966
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2022-04-27T11:26:06.210-0700
- **Updated:** 2025-03-25T12:36:51.904-0700
- **Resolution date:** 2022-05-12T02:56:55.592-0700
- **Affects versions:** 22w17a; 22w18a
- **Fix versions:** 22w19a
- **Labels:** warden; warden-sonic-boom
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** MC-250966.mp4; MC-250966.png; warden kill.zip

## Description

The warden's sonic boom is not attributed to the warden. This means that advancements with the entity_killed_player trigger don't trigger, and the statistic for dying to wardens doesn't increment.
How to reproduce:
- Create a new world. (optional: add the attached datapack that adds an advancement for dying to a warden)

- Spawn a warden on the ground in creative mode.

- Pillar up 5 blocks with blocks around you so you don't fall.

- Give yourself a bow and arrow or a snowball.

- Switch to survival mode.

- Hit the warden with your projectile.

- When the warden comes to kill you, wait until it hits you with its sonic boom.

- Let it hit you with its sonic boom enough times to kill you.

- Respawn and look at your statistics and advancements.

What I expected to happen was:
The statistic for dying to a warden would increment by 1 and the advancement "Adventure" would be granted to me (plus the custom advancement from the datapack).
What actually happened was:
The statistic didn't increment and no advancements were granted to me.
Cause:
The warden's sonic boom uses the damage source "sonic_boom" which is an environmental damage type, like "cactus" or "hotFloor". If it was a player/mob damage type, like "mob" or "fireball", then it would count as the warden's damage. Before 22w17a, the sonic boom used the "mob" damage type, so it did count as the warden's damage.

## Comments (4)

### Comment 1: migrated (2022-04-27T11:26:06.210-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: migrated (2022-04-29T14:25:24.226-0700)

Affects 22w16a

### Comment 3: Avoma (2022-05-02T00:46:17.200-0700)

I can also confirm this behavior in 22w17a.
Here are some alternative steps to reproduce this issue without the need for data packs.
Steps to Reproduce:
- Create a scoreboard objective for tracking when players are killed by the warden and set it to display on the sidebar.

```/scoreboard objectives add KilledByWarden minecraft.killed_by:minecraft.warden```

```/scoreboard objectives setdisplay sidebar KilledByWarden```
- Summon a warden in an enclosed space so that it's forced to use its sonic boom attack on you.

- Die as a result of the warden's sonic boom attack and take note as to whether or not the scoreboard increases.

### Comment 4: [Mod] ManosSef (2022-05-05T13:30:58.117-0700)

I never said the datapack was needed, by the way.
