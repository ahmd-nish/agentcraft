# MC-251919: Equipping a player head, skull or carved pumpkin displays the generic "Gear equips" subtitle

**Mojira URL:** [https://bugs.mojang.com/browse/MC-251919](https://bugs.mojang.com/browse/MC-251919)

## Report details

- **Mojira categories:** Sound
- **Project:** MC
- **Issue key:** MC-251919
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2022-05-19T07:28:40.273-0700
- **Updated:** 2025-04-11T12:51:41.471-0700
- **Resolution date:** 2023-02-08T09:19:12.466-0800
- **Affects versions:** 1.19 Pre-release 1
- **Fix versions:** 1.19 Pre-release 2
- **Labels:** reused-sound-event; subtitles
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2022-05-19_15.18.57.png; 2022-05-19_15.19.15.png; MC-251919.mp4; MC-251919.png
- **Issue links:** Relates:inward:MC-259789:Subtitle for equipping a shield in the offhand is generic | Relates:outward:MC-98316:Wrong subtitles caused by missing distinction

## Description

The bug
Objects which can be equipped in armor slots will play sounds and show subtitles when this happens. The majority of these cases have specially tailored subtitles to fit the material of the object in question, however heads and carved pumpkins point to the generic equipping sound event, which results in the unintuitive "Gear equips" subtitle being displayed.
As death by falling from certain climbable blocks using a generic death message was considered a bug (, , and hopefully ), and the death message from falling stalactites was changed in 20w49a to also not use the generic falling block death message, I am led to believe that the current subtitle behaviour here is also a bug.
How to reproduce
- Equip any piece of armor, or elytra

- Equip a head or carved pumpkin

Expected results
The armor/elytra and head/carved pumpkin would display a subtitle indicating what is being equipped.
Actual results
The armor/elytra equipping shows subtitles which indicate what is being equipped, however equipping a head or a carved pumpkin just gives the vague "Gear equips".

## Comments (2)

### Comment 1: migrated (2022-05-19T07:28:40.273-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: ampolive (2022-05-19T07:44:56.892-0700)

Relates to .
