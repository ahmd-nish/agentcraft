# MC-299196: Waypoints fade out when an advancement is granted

**Mojira URL:** [https://bugs.mojang.com/browse/MC-299196](https://bugs.mojang.com/browse/MC-299196)

## Report details

- **Mojira categories:** Advancements; UI
- **Project:** MC
- **Issue key:** MC-299196
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2025-06-27T09:28:19.377-0700
- **Updated:** 2025-10-06T15:15:13.305-0700
- **Resolution date:** 2025-10-06T05:05:22.706-0700
- **Affects versions:** 1.21.6; 1.21.7 Release Candidate 2; 1.21.7; 1.21.8; 25w31a; 25w32a; 25w33a; 25w34b; 25w35a; 25w36b; 25w37a; 1.21.9 Pre-Release 2; 1.21.9 Pre-Release 4; 1.21.9 Release Candidate 1; 1.21.9; 1.21.10 Release Candidate 1
- **Fix versions:** 25w41a
- **Area:** Expansion A
- **Votes:** 7
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** Waypoint bug.mp4

## Description

This happens in Survival or Adventure mode.
Waypoints will fade out when unlocking advancements that don't have XP associated with them.

- Steps to reproduce the issue

- Viewing Waypoints.
/summon armor_stand ~ ~ ~ {attributes:[{id:"minecraft:waypoint_transmit_range",base:100}]}

- Unlock advancements in Survival or Adventure mode.
/advancement grant @s only minecraft:recipes/brewing/blaze_powder
/advancement grant @s only minecraft:husbandry/plant_seed
etc.

- Expected result
Waypoints remain visible.

- Actual result
The waypoint fades out and the experience bar appears.

## Comments (3)

### Comment 1: KZK1945 (2025-06-27T09:28:20.254-0700)

This comment contained multiple media attachments (2), please login to view the attachments.

### Comment 2: Automation for Jira (2025-08-24T06:17:57.851-0700)

Please edit your report to change the Affected Version to the version shown on the Minecraft title screen

### Comment 3: Daniel99j (2025-10-06T15:15:13.305-0700)

Duplicate of MC-298745
