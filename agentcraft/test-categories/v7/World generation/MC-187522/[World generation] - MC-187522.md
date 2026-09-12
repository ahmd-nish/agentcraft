# MC-187522: Server doesn't generate amplified / large biome worlds

**Mojira URL:** [https://bugs.mojang.com/browse/MC-187522](https://bugs.mojang.com/browse/MC-187522)

## Report details

- **Mojira categories:** World generation
- **Project:** MC
- **Issue key:** MC-187522
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2020-06-04T21:04:55.314-0700
- **Updated:** 2025-04-29T21:03:05.757-0700
- **Resolution date:** 2021-11-23T17:34:59.346-0800
- **Affects versions:** 1.16 Pre-release 1
- **Fix versions:** 1.16 Pre-release 6
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 20w20b-server.log; 2f411e2bc7a217ac2c7568adc73d1e71-1.png; latest.log
- **Issue links:** Cloners:inward:MC-241277:Server can't generate amplified/large biomes worlds from scratch

## Description

What I expected to happen was...:
The server should've generated an amplified world with level-type=amplified set.
What actually happened was...:
It generates a default world instead.
Steps to Reproduce:
- Use the latest pre-release server .jar. (which can be found here)

- In server.properties, set level-type to amplified (server changes "AMPLIFIED" or "Amplified" to all lower-case on startup).

- Generate the world and behold a land strewn with defaultness.

Solutions I've tried:
- Setting server.properties to read-only to prevent the server from changing the level-type to lowercase.

- Generating the amplified world in singleplayer (which works, by the way) and copying the folder to the server (which doesn't work ).

- Messing around with the level.dat file to force the generator setting to amplified.

- Copying an old 1.15.2 amplified server world.

I'd like to note that none of the aforementioned solutions work.

## Comments (7)

### Comment 1: migrated (2020-06-04T21:04:55.314-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: migrated (2020-06-05T00:27:59.438-0700)

I noticed the same bug yesterday afternoon on version 20w22a, I couldn't generate amplified or largebiomes on a vanilla server. (Just like OP, tested in singleplayers and it worked just fine.)

### Comment 3: galaxy_2alex (2020-06-05T05:35:31.865-0700)

Please test if this is still an issue in Prerelease 2.

### Comment 4: migrated (2020-06-05T10:44:21.736-0700)

Bug seems to persist in 1.16-pre2, on a vanilla server with largebiomes. However, like before, it work just fine in singleplayer

### Comment 5: migrated (2020-06-05T16:17:28.699-0700)

I can attest that @Saiirod is correct. Amplified and largeBiomes don't generate on pre-release 2. HOWEVER, I can generate both world types on a 20w20b server. That was the last snapshot in which it worked.
On a positive note, `flat` works.

### Comment 6: migrated (2020-06-14T02:36:05.580-0700)

Yesterday I managed to get a largebiomes map to work and keep generating largebiomes on a vanilla server with 1.16-pre5.
It seems OP tried to do the very same but failed in the original post and in the version at the time (Unsure if anything changed but it does work now), the way I got it to work was to generate the map with the seed I wanted in largebiomes in singleplayer (1.16-pre5, like the server), then use that save as the map for the server, with its server.properties aligned with the choice made to generate the map in singleplayer.

it seems to work atm and there is no issue with the world generator, it seems to only happen when creating a map from scratch.

### Comment 7: migrated (2020-06-14T04:55:39.313-0700)

I can confirm that the server can generate the world type, it just can't generate one from scratch like @Saiirod said. Upon further digging, it looks like the server doesn't set the world generator type correctly if it makes one itself. It sets it to minecraft:overworld, even though level-type is set to AMPLIFIED. However, the singleplayer generator sets the world type to AMPLIFIED correctly, and the server can properly generate more of the world.
So world generation works in pre5, opposed to 20w21a where it didn't work at all.
