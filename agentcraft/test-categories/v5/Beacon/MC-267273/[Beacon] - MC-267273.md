# MC-267273: Second beacon power for level 4 beacon flickers when player hovers the mouse pointer over it

**Mojira URL:** [https://bugs.mojang.com/browse/MC-267273](https://bugs.mojang.com/browse/MC-267273)

## Report details

- **Mojira categories:** Beacon; UI
- **Project:** MC
- **Issue key:** MC-267273
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2023-12-10T23:14:32.524-0800
- **Updated:** 2025-04-26T15:14:25.106-0700
- **Resolution date:** 2024-08-01T08:22:11.701-0700
- **Affects versions:** 1.20.4
- **Fix versions:** 24w03a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2023-12-11 15-55-40.mp4; beacon power.png

## Description

When the player chooses a beacon power on a full beacon and then hovers the mouse over the second level of that power, the description popup flickers rapidly. This does not happen with the other beacon powers.
To reproduce:
- Create a new world in creative mode. (This can also be reproduced in survival but creative mode is easier.)

- Create a full beacon (4 levels).

- Choose a beacon power (left side of beacon UI).

- Hover the mouse over the icon for level 2 of that power (right side of beacon UI). The description popup will flicker rapidly.

The flickering cannot be seen for the other six power icons.
A screenshot is attached showing where the problem will be seen.

## Comments (2)

### Comment 1: migrated (2023-12-10T23:14:32.524-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: KR_ (2023-12-11T00:01:33.545-0800)

Can confirm.
This seems to only affect versions 1.20.3 onwards.
