# MC-190805: Ender dragon fight is hardcoded into custom world presets; can't actually be accessed without these presets

**Mojira URL:** [https://bugs.mojang.com/browse/MC-190805](https://bugs.mojang.com/browse/MC-190805)

## Report details

- **Mojira categories:** Custom Worlds
- **Project:** MC
- **Issue key:** MC-190805
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2020-06-20T21:22:37.484-0700
- **Updated:** 2026-01-21T01:22:43.407-0800
- **Resolution date:** 2026-01-21T01:22:43.293-0800
- **Affects versions:** 1.16 Release Candidate 1; 1.16; 1.16.1; 20w28a; 20w30a; 1.16.3 Release Candidate 1; 1.16.3; 1.16.5; 21w07a
- **Fix versions:** 22w12a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** mcDefaultTest.json; mcDefaultTest-1.json; mcDefaultTest-2.json
- **Issue links:** Relates:outward:MC-189214:Modifying the type compound of the end dimension erases the dragon fight

## Description

The bug
The ender dragon fight is hardcoded into the dimension type preset for the end. If you manually set all of the type values instead of using a preset, there's no way to make the ender dragon fight appear. This seems like it might be an oversight, since in the source code the flag for the ender dragon fight appears right next to all of the other flags which are configurable through JSON, even though the ender dragon fight isn't.
This is an issue because it makes it very difficult to customize the end without essentially breaking the game. Changing any of the type settings in the end requires not using a preset, which means that changing any of these settings will automatically remove the dragon fight from the world.
How to reproduce
Use the
 file attached to generate a world. This JSON file expands the dimension type field for each dimension and the noise generator settings field for the overworld with the game's default settings. Use "/setblock ~ ~ ~ minecraft:end_portal" to place an end portal at your current position and go to the end. Here, there is no ender dragon.

## Comments (7)

### Comment 1: migrated (2020-06-20T21:22:37.484-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: galaxy_2alex (2020-06-21T03:46:23.072-0700)

I have modified your ticket slightly, as the stronghold part has already been reported (MC-187357), so it just includes the ender dragon part now.

### Comment 3: migrated (2020-06-21T07:32:11.182-0700)

I took the stronghold parts out of the description too, it's just about the dragon fight now.

### Comment 4: migrated (2020-06-21T09:41:45.617-0700)

Looking at the source code, as far as I can tell the issue is that while the DimensionType class has a field for createDragonFight, it's not made accessible through any JSON field by DIRECT_CODEC. This should be a pretty simple thing to fix considering that the field already exists internally, it's just not accessible.

### Comment 5: galaxy_2alex (2020-06-22T02:26:45.772-0700)

Loading the .json provided me with a parsing error, just to let you know, but I can confirm that the dragon does not spawn.

### Comment 6: migrated (2020-06-22T06:51:43.230-0700)

That's actually another thing I noticed that might be a bug, it gives you a parsing error but if you ignore it the world generates just fine. It seems to happen whenever you modify the settings for the noise generator. I should probably look into that a little more.

### Comment 7: migrated (2021-02-19T17:37:37.383-0800)

A few things:
1) This file now has a critical parsing error; it is missing the required coordinate_scale property for type which prevents the dimensions from being loaded. I have attached an
2) Can confirm for 1.16.5, as well as 21w07a (even with effects set to minecraft:the_end). Testing on 21w07a requires a
3) This is marked as related to MC-189214 but as far as I can tell, this is the same issue. I recommend closing MC-189214 as a duplicate; despite it being older, this ticket is more detailed.
