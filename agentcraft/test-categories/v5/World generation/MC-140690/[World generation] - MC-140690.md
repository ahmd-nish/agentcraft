# MC-140690: Giant Spruce Taiga Hills has no difference with Giant Spruce Taiga

**Mojira URL:** [https://bugs.mojang.com/browse/MC-140690](https://bugs.mojang.com/browse/MC-140690)

## Report details

- **Mojira categories:** World generation
- **Project:** MC
- **Issue key:** MC-140690
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2018-12-06T10:45:33.280-0800
- **Updated:** 2025-05-02T00:50:54.084-0700
- **Resolution date:** 2021-10-04T11:14:22.492-0700
- **Affects versions:** Minecraft 1.13.2; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 19w02a; Minecraft 19w03a; Minecraft 19w03b; Minecraft 19w03c; Minecraft 19w04a; Minecraft 19w04b; Minecraft 19w05a; Minecraft 19w06a; Minecraft 19w07a; Minecraft 19w08a; Minecraft 19w08b; Minecraft 19w09a; Minecraft 19w11a; Minecraft 19w11b; Minecraft 19w12a; Minecraft 19w12b; Minecraft 19w13a; Minecraft 19w13b; Minecraft 19w14a; Minecraft 19w14b; Minecraft 1.14 Pre-Release 1; Minecraft 1.14 Pre-Release 2; Minecraft 1.14 Pre-Release 3; Minecraft 1.14 Pre-Release 4; Minecraft 1.14 Pre-Release 5; Minecraft 1.14; Minecraft 1.14.1 Pre-Release 1; Minecraft 1.14.1 Pre-Release 2; Minecraft 1.14.1; Minecraft 1.14.2 Pre-Release 1; Minecraft 1.14.2 Pre-Release 2; Minecraft 1.14.2 Pre-Release 3; Minecraft 1.14.2 Pre-Release 4; Minecraft 1.14.2; Minecraft 1.14.3 Pre-Release 1; Minecraft 1.14.3 Pre-Release 2; Minecraft 1.14.3 Pre-Release 3; Minecraft 1.14.3 Pre-Release 4; Minecraft 1.14.3; Minecraft 1.14.4 Pre-Release 1; Minecraft 1.14.4 Pre-Release 2; Minecraft 1.14.4 Pre-Release 3; Minecraft 1.14.4 Pre-Release 4; Minecraft 1.14.4 Pre-Release 5; Minecraft 1.14.4 Pre-Release 6; 1.14.4; 19w34a; 19w35a; 19w36a; 19w37a; 19w38b; 19w38a; 19w39a; 19w40a; 19w41a; 19w42a; 19w44a; 19w45a; 19w45b; 19w46a; 19w46b; 1.15 Pre-release 1; 1.15 Pre-Release 2; 1.15 Pre-release 3; 1.15 Pre-release 4; 1.15 Pre-release 5; 1.15 Pre-release 6; 1.15 Pre-release 7; 1.15; 1.15.1; 1.15.1 Pre-release 1; 1.15.2 Pre-Release 1; 1.15.2 Pre-release 2; 1.15.2; 20w06a; 20w07a; 20w08a; 20w09a; 20w10a; 20w11a; 20w12a; 20w13a; 20w13b; 20w14a; 20w15a; 20w16a; 20w17a; 20w18a; 20w19a; 20w20a; 20w20b; 20w21a; 20w22a; 1.16 Pre-release 1; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 4; 1.16 Pre-release 5; 1.16 Pre-release 6; 1.16 Pre-release 7; 1.16 Pre-release 8; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w27a; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Pre-release 2; 1.16.2 Release Candidate 1; 1.16.2 Release Candidate 2; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4 Pre-release 1; 1.16.4 Pre-release 2; 1.16.4 Release Candidate 1; 1.16.4; 20w45a; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5 Release Candidate 1; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w08a; 21w08b; 21w10a; 21w11a; 21w13a; 21w14a; 21w15a; 21w16a; 21w17a; 21w18a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17 Pre-release 2; 1.17 Pre-release 3; 1.17 Pre-release 5; 1.17 Release Candidate 1; 1.17 Release Candidate 2; 1.17; 1.17.1 Pre-release 1; 1.17.1 Pre-release 2; 1.17.1 Pre-release 3; 1.17.1 Release Candidate 2; 1.17.1
- **Fix versions:** 21w37a
- **Labels:** biome; single-biome-only; world-generation
- **Watchers:** 1
- **Attachments:** 12
- **Attachment filenames:** image-2018-12-06-19-36-29-454.png; image-2018-12-06-19-43-50-502.png; image-2018-12-06-19-47-48-223.png; image-2018-12-06-22-19-25-371.png; image-2018-12-06-22-29-33-425.png; image-2018-12-07-15-07-09-880.png; image-2018-12-07-15-10-15-464.png; image-2018-12-07-15-11-14-086.png; image-2018-12-07-15-14-21-701.png; image-2018-12-07-15-14-42-430.png; image-2018-12-07-15-24-35-701.png; image-2018-12-07-15-24-57-386.png
- **Issue links:** Relates:inward:MC-188096:Gravelly Mountains+ is no different than Gravelly Mountains

## Description

The bug :
There is no difference beetween Giant Spruce Taiga Biome and Giant Spruce Taiga Hills Biome. The supposed hillier version is not. The problem is that the game isn't using correct values of setBaseHeight and setHeightVariation when generating the Giant Spruce Taiga Hills (Giant Spruce Taiga and Giant Spruce Taiga Hills are using the same values).
This bug exists since these biomes were added in the game, in 1.7.2.
It is not a feature suggestion, because it is clearly not intended. These biomes are coded exactly identical, only their name changes. Don't tell me that developpers intentionally added a "Hills" variant which is generating exactly like the non-Hill variant.
How to reproduce :
-Create a buffet world for each biome, and see that there is no difference beetween the two variants.
-Or create a new world with the seed : 3743090988927099363
Go at coordinates 0 ~ -2180. There is a river, with a Giant Spruce Taiga Hills on the north side and a Giant Spruce Taiga on the south side. You can see that there is no terrain's difference beetween them, Giant Spruce Taiga Hills isn't hillier.

Giant Spruce Taiga :

Giant Spruce Taiga Hills :

Relief difference : 0

If you're thinking it is a feature suggestion, see the code. There is differences beetween Giant Tree Taiga and Giant Tree Taiga Hills for example, but no difference at all beetween Giant Spruce Taiga and Giant Spruce Taiga Hills.

Source code of Giant Spruce Taiga and Giant Spruce Taiga Hills :

Comparison with source code of Giant Tree Taiga and Giant Tree Taiga Hills, which work as intended :

Exact location of the code + all the source code of these 2 biomes :
Location of Biome list :
.minecraft\versions\18w49a\18w49a.jar\bbv.class
We can see on this screenshot that "giant_spruce_taiga" is using the bcv.class file, and that "giant_spruce_taiga_hills" is using the bcw.class file.
We will comparate them to "giant_tree_taiga" and "giant_tree_taiga_hills" after, which use respectively bcx.class file and bcy.class file.

Location of Giant Spruce Taiga Biome code :
.minecraft\versions\18w49a\18w49a.jar\bcv.class

Location of Giant Spruce Taiga Hills Biome code :
.minecraft\versions\18w49a\18w49a.jar\bcw.class

We also can see that everything is exactly the same. The Giant Spruce Taiga Hills Biome will not generate as intended, there won't be any difference with the Giant Spruce Taiga Biome.
(You maybe noticed l.49, and thought that they were the wrong files. However, as we can see in the bbv.class.file, these bcv.class and bcw.class files are the ones used by Giant Spruce Biomes. I would guess that they use a part of Giant Tree Biomes files, which explains l.49)

Comparison with bcx.class and bcy.class (used by Giant Tree Taiga biomes) :

Here, the setBaseHeight value and the setHeightVariation value are correct. The Giant Tree Taiga Hills will generate as intended.

Edit (1.14.4 Pre-Release 1) :
In 1.14.4 Pre-Release 1, files names were changed (location is the same) :
- biomes are now listed in .minecraft\versions\1.14.4-pre1\1.14.4-pre1.jar\biq.class

- Giant Spruce Taiga Biome now uses .minecraft\versions\1.14.4-pre1\1.14.4-pre1.jar\bjq.class

- Giant Spruce Taiga Hills Biome now uses .minecraft\versions\1.14.4-pre1\1.14.4-pre1.jar\bjr.class

- Giant Tree Taiga Biome now uses .minecraft\versions\1.14.4-pre1\1.14.4-pre1.jar\bjs.class

- Giant Tree Taiga Hills Biome now uses .minecraft\versions\1.14.4-pre1\1.14.4-pre1.jar\bjt.class

- nothing else than locations changed, this is why I didn't update screenshots (that were taken in 18w49a)

How to fix the bug :
In the Giant Spruce Taiga Hills line code, change the value of setBaseHeight from 0.2F to 0.45F, and change the value of setHeightVariation from 0.2F to 0.45F
This won't change the global world generation, but only the way this specific biome is generated (and this biome is rare so it will not cause any issue of bad world generation caused by updating from an older version).
There is like 2 numbers to change, which will make more variety in Minecraft, as it was intended in the first place by creating Giant Spruce Taiga Hills in 1.7.2
I hope it will get fix as soon as possible, there is really not much to do in order to fix this bug !

## Comments (21)

### Comment 1: migrated (2018-12-06T10:45:33.280-0800)

This comment contained multiple image attachments (12), please login to view the attachments.

### Comment 2: Yellow01 (2018-12-06T12:35:01.357-0800)

100% sure this is a feature request.

### Comment 3: migrated (2018-12-06T13:02:02.328-0800)

Did you even read ? The way the Giant Spruce Taiga Hills is generating is not intended. It is not generating different relief than Giant Spruce Taiga. If it was intended, there shouldn't be 2 different biomes that generate exactly in the same way. If you look in the code, you'll see that there is absolutely no difference. And if you generate buffets, you'll see no difference either. What I'm trying to say is that it is not a "feeling". There isn't even MINOR differences beetween these biomes. If the Hills version was just a little bit difference that we couldn't see, it would be a feature suggestion. However there is not even a little one, even in the code.

### Comment 4: [Mod] Neko (2018-12-06T16:20:17.469-0800)

: Not a feature request.

### Comment 5: Yellow01 (2018-12-07T08:36:08.982-0800)

I thought it was a feature request because it sounded like the reporter was complaining about how there seemed to be no difference between the biomes. My bad.
Also, what does "Plausible" mean as a confirmation status?

### Comment 6: [Mod] Asteraoth (2018-12-07T08:38:38.628-0800)

Quote from a moderator:
When it seems likely to exist just from reading the issue, but we haven't actually reproduced it.

### Comment 7: migrated (2018-12-07T09:45:45.218-0800)

You can reproduce the bug easily by creating buffet worlds (or by going look in minecraft code).
By the way can you put older versions in affected versions (1.7.2, 1.8, 1.9, 1.10, 1.11, 1.12) ? (I can't, I don't know why)

### Comment 8: Yellow01 (2018-12-07T11:50:22.946-0800)

No. Affected versions added before they became unaccessible are put under "Archived versions" when editing affected versions.

### Comment 9: migrated (2018-12-12T15:06:34.450-0800)

Affects 18w50a. This bug should be confirmed.

### Comment 10: migrated (2019-01-09T12:18:54.986-0800)

Affects 19w02a

### Comment 11: migrated (2019-01-16T12:57:41.733-0800)

Affects 19w03a

### Comment 12: migrated (2019-01-18T05:02:48.550-0800)

Affects 19w03b and 19w03c

### Comment 13: migrated (2019-01-24T07:55:08.186-0800)

Affects 19w04a

### Comment 14: migrated (2019-03-14T08:43:53.746-0700)

Please do not mark unreleased versions as affected.
You don't have access to them yet.

### Comment 15: migrated (2019-05-13T06:31:53.561-0700)

Still not fixed in 1.14.1 release. Please confirm this 6 years old bug.

### Comment 16: migrated (2019-07-22T03:39:19.079-0700)

still not fixed in 1.14.4

### Comment 17: migrated (2020-01-24T06:16:37.504-0800)

still not fixed in 1.15.2
bmd.class
Rly too ez to fix it, i can to in max 10 min.

### Comment 18: SeaOfPixels (2020-04-21T20:05:52.765-0700)

Very detailed bug report. Hopefully this gets fixed soon.

### Comment 19: Humiebees (2020-08-04T12:23:09.120-0700)

please fix, in 1.16, 1.16.1, and 1.16.2 dev versions

### Comment 20: Arisa Bot (2020-11-04T09:54:07.821-0800)

Please do not mark Unreleased Versions as affected. You don't have access to them yet.
-- I am a bot. This action was performed automatically! Please report any issues in Discord or Reddit

### Comment 21: migrated (2021-02-14T09:47:55.369-0800)

For those of us bothered by this, I made a Forge mod that patches the game to fix this:
https://github.com/nevir/giant-spruce-taiga-hills-fix/releases/tag/1.0.0
