# MC-1429: When beacon power level is changed, the GUI doesn't update until closed and reopened

**Mojira URL:** [https://bugs.mojang.com/browse/MC-1429](https://bugs.mojang.com/browse/MC-1429)

## Report details

- **Mojira categories:** Beacon
- **Project:** MC
- **Issue key:** MC-1429
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2012-10-31T01:25:20.973-0700
- **Updated:** 2025-04-29T11:47:18.620-0700
- **Resolution date:** 2023-10-31T09:48:46.215-0700
- **Affects versions:** Minecraft 1.4.2; Snapshot 13w04a; Minecraft 1.6.2; Minecraft 1.7.4; Minecraft 14w02c; Minecraft 1.7.5; Minecraft 14w10c; Minecraft 1.7.10; Minecraft 14w30b; Minecraft 14w30c; Minecraft 14w32a; Minecraft 1.8; Minecraft 1.8.1; Minecraft 1.8.3; Minecraft 1.8.4; Minecraft 1.8.6; Minecraft 15w36d; Minecraft 15w42a; Minecraft 16w02a; Minecraft 1.10; Minecraft 1.10.1; Minecraft 1.10.2; Minecraft 16w32a; Minecraft 16w32b; Minecraft 16w33a; Minecraft 16w35a; Minecraft 17w06a; Minecraft 1.12.2; Minecraft 18w22c; 1.15.2; 20w21a; 1.16.1; 20w29a; 1.16.3; 1.19.3; 23w04a
- **Fix versions:** 21w20a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2012-10-31_01.24.24.png; mc-1429.nbt
- **Issue links:** Relates:outward:MC-2440:Beacons keep higher level effects when partially destroyed | Relates:inward:MC-44907:Beacon Interface Greyed Out

## Description

The bug
An open beacon GUI does not update whenever beacon power level or active state changes.
How to reproduce
- Place

-  structure file in .minecraft\saves\<world_name>\generated\minecraft\structures.

- Go in that world and run:

```
/setblock ~ ~ ~ structure_block{mode:"LOAD",name:"mc-1429",showboundingbox:1}
```

- Get an iron ingot, stand on the pressure plate and put the iron in the beacon.
→  After the beacon is deactived, you can still select an effect

## Comments (19)

### Comment 1: migrated (2012-10-31T01:25:20.973-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: kumasasa (2013-01-27T08:21:13.734-0800)

Confirmed.

### Comment 3: migrated (2013-01-28T19:48:49.382-0800)

Could not reproduce in 13w04a creative or survival — as soon as I've placed a beacon, I can right-click it and get the GUI regardless of whether the beam is active or a pyramid is underneath.

### Comment 4: kumasasa (2013-01-28T23:06:05.871-0800)

Yes, but before the beam kicks in there are the effects missing in the GUI.
The beacon block checks only every few seconds (I assume for performance reasions), if it is placed on a legit pyramid and what kind of pyramid, and depending on that result the icons for the effects are shown.
Possible fix: The beacon block should do an additional check for legit pyramid immideatly after placing.

### Comment 5: migrated (2014-01-14T13:39:23.394-0800)

The interface does not appear right regardless in 14w02c, even if you wait for beam to appear or replace the beacon. See bug
MC-44907

### Comment 6: migrated (2014-03-10T10:01:51.366-0700)

Still a concern in 1.7.5 and 14w10c

### Comment 7: Ezekiel (2014-07-26T11:43:31.483-0700)

Is this still a concern in the latest Minecraft version 14w30c? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 8: migrated (2014-07-26T12:29:43.157-0700)

The described behavior still occurs in 14w30c.

### Comment 9: migrated (2014-09-18T15:03:17.918-0700)

Still in 1.8

### Comment 10: migrated (2015-03-07T12:52:47.789-0800)

Confirmed in 1.8.3. Could someone update the description to something clearer, like "When beacon power level is changed, the GUI doesn't update until closed and reopened."?

### Comment 11: marcono1234 (2015-05-05T09:23:23.583-0700)

Confirmed for
- 1.8.4

### Comment 12: marcono1234 (2015-10-18T06:43:20.016-0700)

Confirmed for
- 15w42a

### Comment 13: _zombiehunter (2016-01-17T10:39:11.217-0800)

Still a problem in 16w02a

### Comment 14: migrated (2016-01-17T13:17:07.802-0800)

WAI, see MC-78446. Note that beacons now do power up straight away when placed.

### Comment 15: marcono1234 (2016-01-17T13:41:53.249-0800)

Are you sure that this is WAI? The reason is apparently a different one as the GUI will never update until you reopen it.

### Comment 16: migrated (2016-01-17T14:32:44.084-0800)

Oh, I misread the report. Reopening.

### Comment 17: FaRo1 (2016-06-10T14:14:19.385-0700)

I placed a beacon in 1.10 (just on normal ground) and quickly clicked on it. The GUI showed no choices (effects). Does that mean it's confirmed for 1.10?

### Comment 18: FaRo1 (2016-06-22T14:26:44.963-0700)

Confirmed for 1.10.1.

### Comment 19: pulpetti (2020-07-16T13:10:09.895-0700)

In 1.16.1 and 20w29a.
