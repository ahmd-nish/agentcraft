# MC-269963: Bad Omen is not removed when experimental features are disabled

**Mojira URL:** [https://bugs.mojang.com/browse/MC-269963](https://bugs.mojang.com/browse/MC-269963)

## Report details

- **Mojira categories:** Raids
- **Project:** MC
- **Issue key:** MC-269963
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2024-03-27T11:58:58.180-0700
- **Updated:** 2025-04-29T10:07:18.412-0700
- **Resolution date:** 2024-04-08T02:23:22.811-0700
- **Affects versions:** 24w13a
- **Fix versions:** 1.20.5 Pre-Release 1
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 0
- **Issue links:** Duplicate:inward:MC-270020:Bad omen does not disappear when entering the village | Relates:outward:MC-270026:Raid omen of lower level is displayed in the GUI indefinitely after a raid has started with a higher omen level

## Description

In previous versions, bad omen was immediately removed when the raid began. As of 24w13a it is not removed when the 1.21 experimental features are disabled. This means that any amount of omen causes infinite raids, as it restarts as soon as the previous raid ends.

## Comments (1)

### Comment 1: Invisible826 (2024-03-27T12:14:10.486-0700)

Can confirm.
