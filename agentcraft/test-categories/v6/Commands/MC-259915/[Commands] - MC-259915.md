# MC-259915: Item display position interpolation not working

**Mojira URL:** [https://bugs.mojang.com/browse/MC-259915](https://bugs.mojang.com/browse/MC-259915)

## Report details

- **Mojira categories:** Commands; Entities
- **Project:** MC
- **Issue key:** MC-259915
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2023-02-10T21:55:00.016-0800
- **Updated:** 2025-04-26T14:48:28.557-0700
- **Resolution date:** 2024-09-10T02:07:52.304-0700
- **Affects versions:** 23w06a; 1.19.4 Pre-release 3; 1.19.4 Release Candidate 2; 1.19.4; 1.20 Pre-release 1; 1.20.1
- **Fix versions:** 23w07a; 23w31a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** javaw_EFaL3DCAjw.mp4
- **Issue links:** Relates:inward:MC-276459:Item display rotation wrapping does not interpolate cleanly

## Description

Want to start off this report by tipping my hats to the devs and expressing gratitude at how incredible of a feature this is for developers and will open up an unspeakable amount of new opportunities, thank you for giving this to the community.
While messing with the new feature after it came out, came to a disappointing realization that there seems to be no position interpolation (showcased in the video: https://youtu.be/H-_zwxMdP_U ). Based on the nature of this feature, I'm led to believe the lack of this would be a bug as it makes teleporting it quite jarring and not usable as a moving thing (which opens up so many more opportunities).
Some other notes that may be relevant as to this bug:
- because of the non-ticking nature of this entity, it doesn't have the built-in position interpolation that living entity has, though the usage properties of it make position interpolation very relevant.

- similar behavior can be seen with area effect clouds even though it is a ticking entity

- marker entity gets a pass to be non-ticking because it is completely server side and does not render on client side

- position interpolation can be mimicked with TRSR transformation, but the results are unstable and resource intensive. This was a tested alternative to this bug before reporting, but between this and the mounting not working we came to this conclusion. https://youtu.be/qD5JjeXNGvI

Tests were ran both through command blocks to achieve the teleporting to me, as well as verified on the latest versions of fabric as we're more comfortable doing that kind of development over the command system, but can verify it on both vanilla and fabric, as well as singleplayer and on a local server. This video shows a fabric version of the testing (compared to vanilla on the others) where you can see unstable results when pausing/unpausing the games and using frame perfect packets to move the entity: https://youtu.be/I_PKHfFJ_BY
Was doing some searching of the issues and found this issue MC-259816 which addresses it in a similar way, at this time you can't reliably mount these display items on other entities without it breaking, allowing for NO way to smoothly move these display items (as mounting an entity that does have that position interpolation would also be a "bandaid")
The expected behavior I would think to see with this feature would be that you can move the position/rotation (as in yaw/pitch) of these item displays and have them smoothly teleport, like other entities in the game. Allowing this, and fixing whatever is going on with the mounting of them would be so incredible!
Code/commands can be included if needed, although the behavior is replicable by moving it at all, so we figured that no specific case was required at this point.
Thanks for reading/checking this out!

## Comments (13)

### Comment 1: migrated (2023-02-10T21:55:00.016-0800)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: migrated (2023-03-02T10:09:23.923-0800)

This issue was marked as fixed in 23w07a however basic testing is showing this does not seem to be the case https://youtu.be/Qv2ROIIYblA can this be reopened potentially to be looked at again?

### Comment 3: migrated (2023-03-02T10:37:10.747-0800)

Not sure how to get a helper/mod to see this for visibility but I believe the "fixed" status on this is incorrect
https://youtu.be/kgN_f9VzlbY - Video directly on the snapshot that it is marked as fixed.
https://youtu.be/Qv2ROIIYblA - Latest Pre release 3 as well.
Both show the difference and that the interpolation doesn't seem to be a thing?

### Comment 4: syarumi (2023-03-07T00:40:10.618-0800)

Can confirm as well, not fixed.
That said, in the last pre-release mounting the display entity into other entities seems to work now and the smooth movements get preserved, but when using teleports the issue is still there.

### Comment 5: SnaveSutit (2023-03-13T19:24:01.706-0700)

Something to note, while mounting the display entity onto another entity "fixes" the position interpolation, it does not fix the rotation interpolation.
If the riding was updated to "fix" rotation interpolation I believe that would be an acceptable outcome. Having the option to either have instant or interpolated movement would be more useful than being locked into one or the other.
I wouldn't say no to a better solution, but this would be a great outcome.

### Comment 6: migrated (2023-03-14T12:37:20.628-0700)

If it's at all useful, there's an implementation of a fix here that we did in fabric: display-interpolation-fix/DisplayEntityMixin.java at main · Ticxo/display-interpolation-fix (github.com)
Interpolation isn't working because updateTrackedPositionAndAngles is directly setting position of the entity instead of setting the target location to interpolate towards (something that LivingEntities do). So we just implemented the same method LivingEntities use to fix the position lerping. For rotation since display entities handle it through the getFixedRotation method we just store the previous fixedRotation and return a rotation spherical-lerped between previous and current.

### Comment 7: SnaveSutit (2023-05-16T07:47:23.750-0700)

This issue was discussed with Boq in the Minecraft Commands discord server here

### Comment 8: migrated (2023-05-16T08:20:34.224-0700)

For those without an account, or those unwilling to enter a random server, it's better to attach the discussion's main points/responses as a file/image on the report.

### Comment 9: migrated (2023-06-23T15:21:20.518-0700)

1.20 and 1.20.1 are still affected

### Comment 10: migrated (2023-06-25T09:11:39.567-0700)

Display entities specifically got interpolation mechanics added, armor stands don't have that at all. Your argument makes no sense.

### Comment 11: migrated (2023-06-25T09:31:48.745-0700)

https://discord.com/channels/154777837382008833/593812273164976166/1107942425613312020
This thread from the Minecraft Commands discord addresses this issue (to some extent) https://discord.gg/QAFXFtZ and the final outcome seems to be that he agrees some version of a fix will be added, just wasn't a priority. Alot of the math and decisions went over my head but someone much smarter than me who is plagued by this issue said that thread proposal from Boq would fix it.

### Comment 12: syarumi (2023-08-03T18:59:33.838-0700)

With the addition of teleport_duration in 23w31a the described issues seem to have been addressed, can you confirm?

### Comment 13: r6653116 (2023-09-05T12:27:53.199-0700)

This seems to be fixed with the {teleport_duration} option in 1.20.2 pre 1
