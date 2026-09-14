# MC-169498: Empty top subchunks don't update skylight in some cases

**Mojira URL:** [https://bugs.mojang.com/browse/MC-169498](https://bugs.mojang.com/browse/MC-169498)

## Report details

- **Mojira categories:** Lighting
- **Project:** MC
- **Issue key:** MC-169498
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2020-01-05T12:18:54.477-0800
- **Updated:** 2025-04-30T04:51:31.781-0700
- **Resolution date:** 2023-04-12T01:35:30.477-0700
- **Affects versions:** 1.15.1; 1.15.2; 20w06a; 20w18a; 20w20b; 20w22a; 1.16 Pre-release 3; 1.16.2; 1.17.1; 1.18; 1.19.4; 23w12a
- **Fix versions:** 23w16a
- **Labels:** mojang_internal_1
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** picture-1.png; picture-2.png; picture-3.png; picture-4.png; picture-5.png; showcase.mp4
- **Issue links:** Relates:outward:MC-170010:Sky-lightmaps not properly initialized

## Description

The bug
In some rare cases, sky light can remain after breaking a block.
How to reproduce
All steps are also demonstrated in the
 video.
- Get a flat surface at a sub chunk. A superflat world with only the first 16 blocks works great.

- Make sure no blocks are in this subchunk or in the neighboring subchunks at the same level or higher.

- Place a solid block with one air block between the surface. This is shown in "picture-1.png".

- After removing this block, notice that the darker light level remains. See "picture-2.png". This is more clear with "Smooth Lighting: OFF", which you can see in "picture-3.png".

- Now place a block directly on top of the surface, and place a solid block with an air block between the surface near it. This is the setup shown in "picture-4.png".

- Removing this block, the light level updates correctly. See "picture-5.png"

The exact place that surrounding blocks affect whether or not the sky light is updated, is unclear to me. There is also a zone where having blocks won't update the skylight, but replacing blocks in that zone will update the skylight.

## Comments (6)

### Comment 1: migrated (2020-01-05T12:18:54.477-0800)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: [Mod] violine1101 (2020-01-05T12:39:43.022-0800)

Confirmed. Easiest to see with lighting set to moody.

### Comment 3: PhiPro (2020-01-17T14:17:13.204-0800)

An analysis and solution is given in .
This is simply a rendering issue: the bottom chunk is not marked for rerendering. Causing any block update in that chunk or reloadong the world will fix the issue.
The actual skylight as shown in F3 is correct.

### Comment 4: migrated (2020-09-06T02:37:42.723-0700)

Yep, can confirm as well!
Interesting rendering issue.

### Comment 5: ampolive (2021-08-20T17:42:38.156-0700)

Can confirm in 1.17.1.

### Comment 6: Lunarian (2023-03-25T13:46:30.416-0700)

Can confirm: 23w12a

Video: YouTube
