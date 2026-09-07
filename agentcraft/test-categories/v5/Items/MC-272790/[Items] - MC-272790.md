# MC-272790: Shulker boxes and other blocks in the end exit portal when it changes state are not dropped as items

**Mojira URL:** [https://bugs.mojang.com/browse/MC-272790](https://bugs.mojang.com/browse/MC-272790)

## Report details

- **Mojira categories:** Items
- **Project:** MC
- **Issue key:** MC-272790
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-05-31T03:33:01.547-0700
- **Updated:** 2025-04-26T15:46:03.981-0700
- **Resolution date:** 2025-01-13T07:06:07.178-0800
- **Affects versions:** 1.20.6; 1.21 Pre-Release 1; 1.21.3
- **Fix versions:** 25w03a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 10
- **Attachment filenames:** 2024-05-31_11.21.04.png; 2024-05-31_11.21.27.png; 2024-05-31_11.21.33.png; 2024-05-31_11.23.57.png; 2024-05-31_11.27.02.png; 2024-05-31_11.28.13.png; 2024-05-31_11.28.17.png; 2024-05-31_11.28.21.png; 2024-05-31_11.28.44.png; 2024-05-31_11.28.52.png
- **Issue links:** Relates:outward:MC-902:The end obsidian platform resets every time entities go through the end portal, which can cause blocks to be deleted | Relates:outward:MC-273945:Unlike end portals, nether portals do not drop replaced blocks, which can result in major item loss

## Description

The bug
1.21 pre-release 1 finally fixed MC-902 by making the replaced blocks drop as items rather than outright deleted as previously. However, this behaviour does not apply to blocks placed within or around the exit end portal when the dragon is killed or resummoned.
The other kind of end portal is also affected, which is reported under .
How to reproduce
- Enter the End

- Place your precious shulker boxes inside the end fountain

- Kill the dragon

Expected results
As the end portal activates, the blocks replaced by the end portal would be dropped as items and would be sent through the portal.
Actual results
Your items are now gone forever. Well done!
Further notes
Also happens when the portal deactivates during the summoning ritual.

## Comments (6)

### Comment 1: migrated (2024-05-31T03:33:01.547-0700)

This comment contained multiple image attachments (10), please login to view the attachments.

### Comment 2: BugTracker_ (2024-05-31T04:12:30.209-0700)

Can confirm.

### Comment 3: Minecraft386882 (2024-11-09T20:44:18.211-0800)

Confirmed in 1.21.3

### Comment 4: Ray (2025-01-08T15:22:56.595-0800)

this doesn't seem to be fixed in 25w02a snapshot

### Comment 5: dovisutu (2025-01-08T18:36:53.429-0800)

Seems not fixed in 25w02a. EndPodiumFeature.java didn't receive changes like it was for EndPlatformFeature.java for MC-902 (namely, calling destroyBlock before setBlock). Also confirmed to be not fixed in game.

### Comment 6: Ray (2025-03-14T13:27:41.462-0700)

Still doesnt drop blocks when summoning new dragon.
