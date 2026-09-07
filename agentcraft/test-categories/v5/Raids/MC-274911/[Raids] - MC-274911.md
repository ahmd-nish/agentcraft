# MC-274911: If the raid begins more than 112 blocks above the ground, all illagers will be summoned and the player wins

**Mojira URL:** [https://bugs.mojang.com/browse/MC-274911](https://bugs.mojang.com/browse/MC-274911)

## Report details

- **Mojira categories:** Raids
- **Project:** MC
- **Issue key:** MC-274911
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2024-08-04T07:24:20.844-0700
- **Updated:** 2025-05-29T09:05:07.317-0700
- **Resolution date:** 2024-08-27T01:07:41.619-0700
- **Affects versions:** 1.21; 1.21.1 Release Candidate 1; 1.21.1
- **Fix versions:** 24w33a
- **Area:** Expansion B
- **Watchers:** 3
- **Attachments:** 3
- **Attachment filenames:** 2024-08-05_14.30.48.png; 24w33a_274911_RaidInnermostRingBroken.mp4; javaw 2024-08-05 01-44-33-519.mp4
- **Issue links:** Relates:inward:MC-158389:Raid results in victory if it cannot find a valid spawn point | Relates:outward:MC-173524:Raiders travelling to another dimension does not remove them from the raid

## Description

Steps to Reproduce:
1) Teleport up 120 blocks using this command

```
/tp @s ~ ~120 ~
```
2) Place villagers in a small space and provide them with beds
3) Trigger a raid by drinking a bottle of bad omen
4) Watch as illagers start to spawn and fall to the ground
Observed Results:
You can see all the illagers being summoned to the ground without going through the waves.
Expected Results:
If there is no land within 112 blocks of the raid point, the raid must end without starting.

## Comments (11)

### Comment 1: migrated (2024-08-04T07:24:20.844-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: [MOD] Greymagic27 (2024-08-04T09:30:12.443-0700)

We do not have enough information to reproduce this issue.
Please include the following information to help us understand your problem:
Steps to Reproduce:
1. (Explain what needs to be done for the issue to happen)
2.
3.
Observed Results:
(Briefly describe what happens)
Expected Results:
(Briefly describe what should happen)
Please also attach any needed commands, datapacks, resourcepacks, screenshots, videos, or worlds needed to help reproduce this issue.
Refer to the Bug Tracker Guidelines for more information about how to write helpful bug reports. Bug reports with insufficient information may be closed as Incomplete.
This issue is being temporarily resolved as Awaiting Response. Once the requested information has been delivered, the report will be reopened automatically.
Quick Links:
📓 Bug Tracker Guidelines – 💬 Community Support – 📧 Mojang Support (Technical Issues) – 📧 Microsoft Support (Account Issues)
📓 Project Summary – ✍️ Feedback and Suggestions – 📖 Game Wiki

### Comment 3: [MOD] Greymagic27 (2024-08-04T09:52:40.853-0700)

Please update the 'steps to reproduce' section to have numbered steps for everything someone would need to do to reproduce this issue from scratch. This means any commands, etc

### Comment 4: ErfinderLabyrinth (2024-08-07T12:38:40.048-0700)

Please dont fix that, this mechanic will be used by raid farms

### Comment 5: mooing_cowmilk (2024-08-07T13:30:16.174-0700)

Speedrunners and raid farmers both use this to their advantage.
This has been the case since MC 1.14 when raids were added. Basically the raid wave spawning rules is various sizes of circles with top block (sky access) determining y height, forming a cylinder of locations. Mob detection range is a sphere, so like putting a ball down a tube, the space below and above the tube yields the results in the OG report.
CAUTION IF CHANGING CODE:
During the development of 1.14, there was tons of bugs regarding "endless" raids due to wave members falling into caves or wonder far in the opposite direction out of render/sim distance. The current setup was a patch to address that issue. So any new changes need to keep that in mind.
See MC-151014 for example (as well as the ringing bell highlight feature)

### Comment 6: [MCQA] krbaj (2024-08-16T05:33:32.748-0700)

Reopening the issue as it has been tested internally and was reproduced on the latest version 1.21.1

### Comment 7: Alex_light (2024-08-16T06:43:48.089-0700)

What do you mean? This is no longer reproducible
This is a fixed issue  24w33a

### Comment 8: Jack McKalling (2024-08-16T08:09:42.598-0700)

They meant it was reproduced in an internal version after 1.21.1 (and after 24w33a), not in 1.21.1 itself.

### Comment 9: litetex (2024-08-16T11:55:33.141-0700)

So I just had a look at this "bugfix" and I think it has a problem:
At first let's have a look at the code. It looks roughly like this:
Raid#findRandomSpawnPos(int proximity, int tries) looks like this

```int i = proximity == 0 ? 2 : 2 - proximity;
// ...
int y = this.world.getTopY(Heightmap.Type.WORLD_SURFACE, x, z);
if (MathHelper.abs(y - this.center.getY()) > 32 * i) continue;  // <-- this line is new and is the fix for this "bug" here```
Now to the code's behavior:
The changes effectively limit the vertical distance (Y) where a raid wave can spawn, limiting the "ring" like structure on the "top and bottom".
However the vertical distance is not hardcoded to the mentioned 112 blocks in the issue but instead dynamically derived from the proximity/"ring" of the spawn location.
The higher proximity the closer it spawns to the center of the raid.
Proximity
Y difference must be smaller or equal than
0
64
1
32
2
0
I think that these values e.g. for the are way to small and result in unexpected behavior, for example:
- When the proximity is 2 (innermost "ring") - which is btw what every raid farm uses - it's nearly impossible (spawnable blocks are picked at random in the "ring") to get a raid spawned as the y distance of the spawn location now has to be exactly 0.
Here's a showcase:

- Although very unlikely this might also affect normal villages that sometimes generate in very rough terrain (e.g. a cliff or on small islands in the ocean) which might cause all spawn attempts to fail - resulting in the raid just vanishing

I would propose the following solutions in preferred order:
1. If possible revert this change - Which naturally generated village is 112 blocks away from the ground in the first place?
2. If reverting is not an option: Make the innermost ring ignore the Y difference limit, to force the raid to spawn and not "vanish"
3. Increase the Y difference. At best to a static value like the mentioned 112 blocks in the issue.

### Comment 10: Alex_light (2024-08-16T12:28:58.701-0700)

No, that was even before the  report was resolved. That issue is MC-275279 and MC-275007

### Comment 11: litetex (2024-08-16T13:36:40.640-0700)

No, that was even before the  report was resolved. That issue is MC-275279 and MC-275007
This new code is not present in 1.21.1, so it's not possible that this happend before.
MC-275279 is affecting only 24w33a, so it's likely the same problem as I described below.
MC-275007 is likely working as intended as it has been this way for years. The behavior is also described in the wiki.
