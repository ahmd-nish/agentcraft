# MC-270540: The prevention of fall damage from wind charges is not retained upon reloading the world

**Mojira URL:** [https://bugs.mojang.com/browse/MC-270540](https://bugs.mojang.com/browse/MC-270540)

## Report details

- **Mojira categories:** Player; Save Data
- **Project:** MC
- **Issue key:** MC-270540
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2024-04-08T11:08:26.332-0700
- **Updated:** 2025-04-10T12:36:27.464-0700
- **Resolution date:** 2024-06-07T05:10:02.382-0700
- **Affects versions:** 24w14a
- **Fix versions:** 1.21 Pre-Release 4
- **Area:** Expansion B
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** fall damage after reloading world.mp4; reproduction step 5.mp4
- **Issue links:** Relates:outward:MC-59626:Arrows lose their Punch enchantment property when unloaded

## Description

When players are launched using wind charges (excluding breeze wind charges), they are protected from fall damage if they land at or above the Y-level where the explosion occurred. This protection also extends to scenarios where players gain additional vertical momentum after the wind charge detonates, such as when affected by effects like levitation. However, the problem outlined in this bug report is that the exemption, which should prevent fall damage when landing at or above the same Y-level after being propelled by a wind charge, is not preserved when the player re-enters the world. Consequently, players will take fall damage upon re-entry. Relates to MC-59626, , , , , , , ,  and .
steps to reproduce
- Position an impulse command block to face towards a chain command block

- Insert the following command into the impulse command block:

```
execute at @p run summon minecraft:wind_charge ~ ~ ~ {Motion:[0.0,-1.0,0.0]}
```

- Insert the following command into the chain command block:

```
effect give @p minecraft:levitation 3 40 true
```

- Be in survival mode

- Press the button to confirm that you do not incur fall damage upon landing (Due to another unidentified bug, there are instances where you might still experience fall damage even without reloading the world.)

- Press the button again

- Promptly exit the world (You must exit the world early enough because players are immune to damage for 2 seconds upon entering a world. Ensure that this invulnerability period expires before you land on the ground after re-entering the world.)

- Return to the world

Observed: Fall damage was taken despite being launched from a wind charge.
Expected: Fall damage should not occur because the player was launched from a wind charge.

## Comments (1)

### Comment 1: migrated (2024-04-08T11:08:26.332-0700)

This comment contained multiple image attachments (2), please login to view the attachments.
