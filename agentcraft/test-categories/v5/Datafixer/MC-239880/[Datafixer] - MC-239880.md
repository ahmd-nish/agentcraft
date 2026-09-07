# MC-239880: Some chunks have missing blocks below 0

**Mojira URL:** [https://bugs.mojang.com/browse/MC-239880](https://bugs.mojang.com/browse/MC-239880)

## Report details

- **Mojira categories:** Datafixer; World generation
- **Project:** MC
- **Issue key:** MC-239880
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2021-10-27T12:46:51.564-0700
- **Updated:** 2025-04-29T21:06:38.061-0700
- **Resolution date:** 2021-11-22T07:25:17.792-0800
- **Affects versions:** 21w43a; 21w44a; 1.18 Pre-release 1; 1.18 Pre-release 2; 1.18 Pre-release 3; 1.18 Pre-release 4; 1.18 Pre-release 5
- **Fix versions:** 1.18 Pre-release 6
- **Watchers:** 1
- **Attachments:** 10
- **Attachment filenames:** 1-17-1-worldbug.png; Below 0 world bug.zip; bugimage1.png; bugimage2.png; image-2021-10-27-20-38-59-086.png; image-2021-10-27-20-43-29-347.png; image-2021-10-27-20-45-19-271.png; screenshot-1.png; screenshot-2.png; screenshot-4.png

## Description

The bug
I was exploring around with new biome blending and noticed a chunk formation underground, I went to it and it was all air below 0 and converted incorrectly. This is very rare to happen as I seen the other chunks are fine. I checked the logs are there are 3 errors that are all in the same minute, but this happened on my other world without any error in logs.
UPDATE: The cause of this issue is when caves are generated below old chunks, the chunk contains no bedrock so it won't attempt to place caves below this chunk since after testing around, the chunk must contain at least 1 block of bedrock at Y=0 in the world for it to fill the bottom with caves. The fix would be detecting if the chunk contains an block at Y=0 instead of detecting only Bedrock.
Steps to reproduce
1. Load a world from 1.17.1 or below on 1.18 Pre-release 5 (or load
)
2. Explore around next to the blended area (If on downloaded world do: /tp -1201 -9 -85)
3. You can notice missing chunks but It is rare.
Observed result
Empty chunks below 0
Expected behaviour
Chunks to generate like the other chunks around

## Comments (12)

### Comment 1: migrated (2021-10-27T12:46:51.564-0700)

This comment contained multiple image attachments (10), please login to view the attachments.

### Comment 2: anthony cicinelli (2021-10-27T20:49:11.101-0700)

Can you provide the world download of where this issue occured

### Comment 3: Erik Broes (2021-10-28T02:49:53.071-0700)

Ideally the worlddownload would be a backup before upgrading so we can try and replicate the issue.

### Comment 4: migrated (2021-10-28T04:14:05.449-0700)

1.17.1 download (load in 21w43a) (n/a)
1. /tp -853 -14 24
2. Check the logs if there is an error
Provided the wrong world download here, I'll fix this

### Comment 5: bdm68 (2021-11-02T21:43:37.674-0700)

Related to MC-239994.

### Comment 6: migrated (2021-11-16T10:27:49.530-0800)

Having the same issues again in another world but without the console errors this time
Version is pre release 2

### Comment 7: migrated (2021-11-16T14:55:48.517-0800)

Woah! That's weird!

### Comment 8: migrated (2021-11-17T08:18:00.197-0800)

New Fixed world download: https://easyupload.io/1313ow
Same coordinates: /tp -853 -14 24
After teleporting, check if there are missing blocks below this coordinate.
Still can reproduce on Pre release 3

### Comment 9: migrated (2021-11-20T02:41:39.829-0800)

World with 3 chunks with air below 0

Download:

Coordinates: /tp -1201 -9 -85
Tested on Pre-5

### Comment 10: migrated (2021-11-21T10:46:25.180-0800)

Update on this issue

After testing around a bit more on this issue, I've seen that these missing block chunks before upgrading to 1.18 have no bedrock layer at the bottom of the chunk (This seems to only happen on edge where a chunk is still not completely generated yet).
The cause of this issue is when caves are generated below old chunks, the chunk contains no bedrock so it won't attempt to place caves below this chunk since after testing around, the chunk must contain at least 1 block of bedrock at Y=0 in the world for it to fill the bottom with caves. The fix would be detecting if the chunk contains an block at Y=0 instead of detecting only Bedrock.
Here is an example of how this bug happens and what I was talking about above:

### Comment 11: migrated (2021-11-21T12:14:24.768-0800)

Can confirm

### Comment 12: migrated (2021-11-22T07:25:17.792-0800)

Seems like a bug with world generation and not world conversion. Are you sure this generates the same when using the seed?
