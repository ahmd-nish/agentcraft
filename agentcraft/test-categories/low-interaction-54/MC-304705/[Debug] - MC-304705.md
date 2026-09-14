# MC-304705: The E value in entity_render_stats in the debug overlay doesn't work

**Mojira URL:** [https://bugs.mojang.com/browse/MC-304705](https://bugs.mojang.com/browse/MC-304705)

## Report details

- **Mojira categories:** Debug; UI
- **Project:** MC
- **Issue key:** MC-304705
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2025-12-01T23:48:46.851-0800
- **Updated:** 2026-03-11T03:53:02.664-0700
- **Resolution date:** 2026-01-07T01:09:56.999-0800
- **Affects versions:** 1.21.11 Pre-Release 4; 1.21.11 Release Candidate 2; 1.21.11; 26.1 Snapshot 1
- **Fix versions:** 26.1 Snapshot 2
- **Area:** Platform G
- **Votes:** 24
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** 202512021547.mp4
- **Issue links:** Duplicate:inward:MC-304904:Entity Counter (the number behind E:) in the F3 menu always shows 0 | Duplicate:inward:MC-304953:Entity Scanning isn't working | Duplicate:inward:MC-304996:E-ray stuck at 0 again | Duplicate:inward:MC-305097:Debug screen shows E: 0/x despite visible entities | Duplicate:inward:MC-305256:Entity render stats in 1.21.11 are not working | Duplicate:inward:MC-305325:F3 menu does not display proper entity render stats | Duplicate:inward:MC-305367:Entity Render Stats Not Showing Rendered Entities | Duplicate:inward:MC-305393:The first count in E for the debug screen is displaying 0 even if there are entities in the player's FOV. | Duplicate:inward:MC-305465:F3 Debug entity_render_stats is always 0 | Duplicate:inward:MC-305490:0 entities | Duplicate:inward:MC-305638:The entity render stats does not count the number of entytis on my pov and this happens on other players is like E: 0/97 | Cloners:outward:MC-300235:First number in E counter is always stuck at 0 | Duplicate:inward:MC-305803:MacOS - Debug Option entity_render_stats always shows 0 | Duplicate:inward:MC-305873:1.21.11 - Entity counter broken in the f3 menu | Duplicate:inward:MC-306026:The “E” value in the F3 debug screen (Entity count) is not showing correctly.

## Description

The E value in entity_render_stats in the F3 debug screen don't show the entities rendered in view, only show the total amount of entities.
Steps to reproduce:
1.F3+F6, turn on “entity_render_stats”.
2.Press F3, look around or onto an entity, and look at the E value on the F3 screen.
Expected result:
The E value should show the amount of entities in view/Total entities, such as “39/104”.
Actual result:
The E value only shows the total entities, the amount of entities in view keep at 0 even if you are directly looking onto an entity, e.g. “0/104”.
Note:
This happens since 25w45a.

## Comments (2)

### Comment 1: COMETC2021A1 (2025-12-01T23:48:47.466-0800)

This comment contained multiple media attachments (2), please login to view the attachments.

### Comment 2: Jaden allen (2025-12-23T18:41:49.219-0800)

the entity count seems to be cleared before the debug screen tries to get the entity statistics. i was able to make a simple mod that just stores the rendered entity count and used that to replace the E value. Hopefully this gets fixed soon
