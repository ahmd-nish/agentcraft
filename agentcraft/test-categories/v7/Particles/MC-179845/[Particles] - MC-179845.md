# MC-179845: Rain falls through any blocks in some spots

**Mojira URL:** [https://bugs.mojang.com/browse/MC-179845](https://bugs.mojang.com/browse/MC-179845)

## Report details

- **Mojira categories:** Particles
- **Project:** MC
- **Issue key:** MC-179845
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2020-04-22T08:12:23.065-0700
- **Updated:** 2025-05-29T09:18:41.921-0700
- **Resolution date:** 2022-02-24T06:27:18.140-0800
- **Affects versions:** 20w17a
- **Fix versions:** 20w18a
- **Watchers:** 2
- **Attachments:** 8
- **Attachment filenames:** 2020-04-22_11.11.18.png; 2020-04-22_11.18.28.png; 2020-04-22_11.27.35.png; 2020-04-22_17.31.30.png; 2020-04-22_20.33.41.png; 2020-04-22_22.26.24.png; 2020-05-12_00.53.07.png; image-2020-05-15-17-26-18-726.png
- **Issue links:** Duplicate:inward:MC-13842:When you ride a horse tied to a block the rope breaks, but the rope on the block doesn't | Cloners:inward:MC-239902:Weather effects appear in caves and structures in 1.17.1 worlds loaded in 21w43a | Duplicate:inward:MCL-13842:Maps show stone pattern despite it not being there and rain under solid blocks | Duplicate:inward:MCL-13881:Rain/weather

## Description

Moderator note
For anyone who opened their world in 20w17a and is still experiencing this issue in versions after 20w17a:
Try optimizing the world:
- Client:
- Select the world on the world selection screen

- Press the "Edit" button

- Select "Optimize World"

- Check "Erase cached data"

- Press "Create backup and load"

- Server: Start with --forceUpgrade --eraseCache

If you are still experiencing this issue after trying the steps above, please create a new ticket and attach the world (in the version before you opened it in the latest version of the game) as a zip file.
Rain goes through random blocks. It was raining in a y-level 30 cave and my house in my snapshot server.

## Comments (35)

### Comment 1: migrated (2020-04-22T08:12:23.065-0700)

This comment contained multiple image attachments (8), please login to view the attachments.

### Comment 2: migrated (2020-04-22T08:25:46.291-0700)

I had this issue too, but only in certain areas underground. I checked biome edges and chunk bonders to see if there was any consistency in where it would rain, but I didn't get a pattern with those.

### Comment 3: migrated (2020-04-22T08:32:24.094-0700)

Same here

### Comment 4: migrated (2020-04-22T08:34:20.462-0700)

it also goes through trapdoors in my xp farm but not through solid blocks like cobblestone

### Comment 5: migrated (2020-04-22T08:40:39.529-0700)

I had updated my server with the new snapshot and... now it's raining in the house

### Comment 6: migrated (2020-04-22T10:43:27.555-0700)

It goes through everything, I have a wall 13 blocks high in the area of the rain and it passes straight through them down 6 floors 6 blocks high. I have found that replacing the upper most blocks seem to resolve it, but then it starts leaking somewhere else that I have missed so I have spent the morning patching my roof.

### Comment 7: Gerrygames (2020-04-22T12:26:11.513-0700)

Should be caused by MC-179952

### Comment 8: migrated (2020-04-22T12:39:16.650-0700)

Relates to MC-149791

### Comment 9: migrated (2020-04-22T12:49:05.641-0700)

Confirmed.

### Comment 10: migrated (2020-04-22T13:13:14.407-0700)

You can resolve this problem by running
```--forceUpgrade --eraseCache```

it no longer rains though blocks.

### Comment 11: migrated (2020-04-22T23:59:18.036-0700)

Snow also goes through blocks. Should this be added to the ticket or should I create a new ticket?

### Comment 12: loqk (2020-04-23T18:25:15.419-0700)

I had a tree grow through cobble yesterday, I assume it's the same bug. I tried to suffocate myself in stone, and i could, so if the problem is that the blocks have been marked as transparent, they aren't universally transparent

### Comment 13: [MOD] Greymagic27 (2020-04-24T03:45:34.824-0700)

Sounds like MC-180238 Peter

### Comment 14: migrated (2020-04-25T06:43:17.082-0700)

MC-180100 and MC-180114 are different from this. Can someone reopen them?

### Comment 15: [Mod] violine1101 (2020-04-29T09:45:38.469-0700)

As far as I'm aware, worlds opened in 20w17a will continue to be affected by this issue. Optimizing the world will probably fix that for worlds opened in that version.

### Comment 16: migrated (2020-04-29T10:49:09.214-0700)

Update: Running 20w18a, I attempted optimization on the world for my server (Started in 20w14a), running Windows 10, 64-bit, and the world still has the rain issue. It seems to be the same issue as the maps, as well as what is causing my ice farm to grow in weird lines, and certain blocks won't even have any rain at all. I attempted the world optimization twice now, still no dice. This bug is still present.

### Comment 17: [Mod] violine1101 (2020-04-29T11:17:50.179-0700)

Does the issue happen if you upgrade a world from 1.15.2 or create a new world? If not, the issue no longer exists. Worlds in snapshots may become broken beyond repair.

### Comment 18: migrated (2020-04-29T11:20:35.165-0700)

20w18a still has such issue.

### Comment 19: migrated (2020-04-29T11:28:59.885-0700)

Got another update! We got it FIXED! Solution is to optimize the world, but it is very important to check the "Erase cached data" box when you do it. @Scott, try this and let us know if it works!

### Comment 20: migrated (2020-04-29T11:30:47.594-0700)

violine1101, this was happening with any world from previous versions loaded in last week's snapshot due to (if I remember reading correctly) changes in certain block data as well as heightmaps, which is why maps were acting strange, and why my ice farm was generating in weird lines. Now it's working perfectly.

### Comment 21: migrated (2020-04-29T14:42:06.639-0700)

Confirmed, adding "--forceUpgrade --eraseCache" temporarily to JVM launch arguments for my server completed the upgrade successfully and resolve the rain indoors issue. Take a backup first!

### Comment 22: migrated (2020-04-30T00:41:02.649-0700)

Upgraded to 20w18a and followed the recommended steps here but this issue still persists (on server).

### Comment 23: [Mod] violine1101 (2020-04-30T11:40:20.690-0700)

If so, then please create a new ticket and attach the affected world file there.

### Comment 24: migrated (2020-05-01T02:35:36.556-0700)

If you do use the above mentioned method, for me at least it took around 16hrs to do

### Comment 25: migrated (2020-05-01T14:38:59.621-0700)

still happens

### Comment 26: [Mod] violine1101 (2020-05-02T09:18:16.878-0700)

, worlds opened in 20w17a will remain broken and need to be fixed manually. Please read the yellow box in the description of this ticket for instructions on how to do that.

### Comment 27: migrated (2020-05-16T09:32:28.562-0700)

I am using cubecoder's AMP to run my server and cannot use the java command to start it. How do I delete the cache manually from a world file?

### Comment 28: [Mod] violine1101 (2020-05-16T09:53:56.391-0700)

Download the world file, load it into your singleplayer save folder, follow the steps for singleplayer, and upload the world to the server again.

### Comment 29: migrated (2020-05-18T08:16:32.740-0700)

Still experiencing this issue with the 20w20b snapshot. As I am using a host server I shall try the single player method.

### Comment 30: migrated (2020-05-30T14:22:47.790-0700)

Still finding this problem in 20w21a. I just hope someone see this bug and fix it immediately.

### Comment 31: migrated (2020-05-30T16:27:16.615-0700)

This issue is fixed, you will need to do as mentioned in the Moderator note

### Comment 32: migrated (2020-06-13T12:15:43.341-0700)

The issue is not fixed. I am experiencing it in pre5 and the world has been created in pre3. I do not currently have access to the world.

### Comment 33: migrated (2020-06-13T14:20:21.277-0700)

I can assure you it is indeed fixed. TO completely finish the fix, the person whom has access to the world needs to run the steps provided above and it will fix remaining issues

### Comment 34: migrated (2020-06-14T01:35:17.407-0700)

It might be that the person directing me here did so by accident because it does not look precisely the same to me.
https://imgur.com/VzRcGQt
Can a mod please unmark MC-189380 as being resolved? It really looks different to me and I've explained it there further.

### Comment 35: [Mod] violine1101 (2020-06-16T14:37:19.453-0700)

, I've reresolved your ticket, it is a duplicate of MC-163575 instead.
