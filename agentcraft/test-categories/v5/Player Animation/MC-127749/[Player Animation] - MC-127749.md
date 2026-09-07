# MC-127749: Cape is jittering; movement way sharper than in snapshot 18w03b

**Mojira URL:** [https://bugs.mojang.com/browse/MC-127749](https://bugs.mojang.com/browse/MC-127749)

## Report details

- **Mojira categories:** Player Animation; Rendering
- **Project:** MC
- **Issue key:** MC-127749
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2018-03-30T05:02:30.489-0700
- **Updated:** 2025-04-30T05:38:50.196-0700
- **Resolution date:** 2023-02-05T09:26:03.691-0800
- **Affects versions:** Minecraft 18w11a; Minecraft 1.13; Minecraft 18w30a; Minecraft 18w30b; Minecraft 18w31a; Minecraft 18w32a; Minecraft 18w33a; Minecraft 1.13.1; Minecraft 1.13.2-pre1; Minecraft 1.13.2-pre2; Minecraft 1.13.2; Minecraft 18w43b; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 19w04b; Minecraft 19w05a; Minecraft 19w12b; Minecraft 19w13b; Minecraft 19w14a; Minecraft 19w14b; Minecraft 1.14 Pre-Release 1; Minecraft 1.14.4 Pre-Release 3; Minecraft 1.14.4 Pre-Release 4; Minecraft 1.14.4 Pre-Release 5; Minecraft 1.14.4 Pre-Release 6; 1.14.4; 19w46b; 1.15; 1.15.1; 1.15.1 Pre-release 1; 1.15.2; 20w07a; 20w09a; 20w11a; 20w17a; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 6; 1.16 Pre-release 7; 1.16 Pre-release 8; 1.16 Release Candidate 1; 1.16; 1.16.1; 1.16.2 Release Candidate 1; 1.16.2 Release Candidate 2; 1.16.2; 1.16.3; 1.16.4; 20w46a; 1.16.5; 21w05b; 21w15a; 21w16a; 21w17a; 21w19a; 21w20a; 1.17 Release Candidate 1; 1.17.1; 21w40a; 21w41a; 21w43a; 21w44a; 1.18 Pre-release 5; 1.18 Pre-release 6; 1.18 Release Candidate 1; 1.18 Release Candidate 3; 1.18; 1.18.1; 22w03a; 22w05a; 1.18.2; 1.19 Pre-release 5; 1.19; 1.19.1 Pre-release 4; 1.19.2; 22w43a; 1.19.3 Pre-release 1; 1.19.3 Pre-release 3; 1.19.3
- **Fix versions:** 23w05a
- **Labels:** cape; jitter; strafing; walking
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2018-11-30 17-32-20.mp4; diff.png; MC-127749.mp4; MC-127749.png
- **Issue links:** Relates:inward:MC-238971:The capes of players shake violently after respawning in certain cases or when players enter your render distance | Relates:outward:MC-259722:Capes always tilt to the side slightly when moving and riding entities | Duplicate:inward:MC-128400:LAGGY CAPE ANIMATION | Duplicate:inward:MC-140353:Cape jitters weirdly while moving | Duplicate:inward:MC-156350:Cape animation broken while walking | Duplicate:inward:MC-175416:The 1.13 Cape Problem. No cape "Backstroke", creating unnatural cape movement. | Duplicate:inward:MC-259508:Cape stuttering

## Description

Steps To Reproduce:
- Join any Minecraft world

- Toggle perspective mode, so you can see your cape

- Now start walking with sprint and press W+A or W+D

- Move your mouse in the direction you're walking (it should look like you're walking in circles)

- Observe how weirdly the cape behaves

Expected Result: Smooth cape movement animation, just as it was before snapshot 18w05a
Actual Result: Cape animation is jittering
Video demonstrating the issue: YouTube Video
Additional Information:
After a few checks, I found that the first time when the bug appeared in a game was in a snapshot 18w05a, but before that version, there was a snapshot 18w03b where everything was fine with a cape.
Code Analysis:
Code analysis by  can be found in this comment.

## Comments (48)

### Comment 1: migrated (2018-03-30T05:02:30.489-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: migrated (2018-03-30T05:05:34.511-0700)

Could you explain what's different? I'm not seeing any difference.

### Comment 3: [Mod] bemoty (2018-03-30T05:06:33.757-0700)

Probably caused by the fix of

### Comment 4: migrated (2018-03-30T05:22:35.434-0700)

In 1.12.2 animation of cape more smoother, than in 18w11a

### Comment 5: migrated (2018-07-25T09:12:07.182-0700)

Confirmed for 18w30a.

### Comment 6: migrated (2018-07-26T14:23:27.647-0700)

Confirmed for 18w30b.

### Comment 7: migrated (2018-08-01T12:51:00.395-0700)

Confirmed for 18w31a.

### Comment 8: migrated (2018-08-08T07:44:59.746-0700)

Confirmed for 18w32a.

### Comment 9: migrated (2018-08-15T08:29:47.120-0700)

Confirmed for 18w33a.

### Comment 10: migrated (2018-08-22T13:05:20.623-0700)

Confirmed for 1.13.1.

### Comment 11: migrated (2018-10-16T10:50:19.878-0700)

Confirmed for 1.13.2-pre1.

### Comment 12: migrated (2018-10-19T09:23:24.937-0700)

Confirmed for 1.13.2-pre2.

### Comment 13: migrated (2019-07-09T10:31:33.139-0700)

I have just checked and I found out that this bug appeared on snapshot 18w05a and I couldn't see the issue on previous snapshot (18w03b).
Dear QA Team, if that somehow can help you - I guess you're free to test it.

### Comment 14: migrated (2019-07-09T11:38:52.730-0700)

I have just tested it on 1.14.4-pre3 — this issue is still thing there.
P.S. Yes, the comment above was made also by me, but I literally forgot that I already had an account on this site

### Comment 15: migrated (2019-07-10T10:05:31.145-0700)

Still can reproduce in 1.14.4-pre4

### Comment 16: migrated (2019-07-11T08:16:44.826-0700)

Still able to reproduce in 1.14.4-pre5

### Comment 17: migrated (2019-07-15T06:09:36.624-0700)

Still able to reproduce in 1.14.4-pre6

### Comment 18: migrated (2019-07-23T02:25:05.071-0700)

Still able to reproduce in release 1.14.4

### Comment 19: migrated (2019-11-16T01:00:16.488-0800)

Reproducible in snapshot-19w46b

### Comment 20: migrated (2019-12-14T00:12:04.859-0800)

Still able to reproduce in 1.15

### Comment 21: migrated (2019-12-14T00:14:37.484-0800)

Also still able to reproduce in 1.15.1-pre1

### Comment 22: migrated (2019-12-18T23:59:39.121-0800)

Still able to reproduce in 1.15.1

### Comment 23: migrated (2020-02-18T13:43:44.411-0800)

Same with 1.15.2 and 20w07a

### Comment 24: migrated (2020-02-27T14:46:47.040-0800)

Still in 20w09a. A lot of bugs has been fixed in the recent snapshot (Cape floating while sneaking), should be cool to fix the last bug.

### Comment 25: migrated (2020-03-12T05:23:45.682-0700)

Still reproduceable in 20w11a

### Comment 26: migrated (2020-04-22T08:46:47.148-0700)

Was able to reproduce on 20w17a

### Comment 27: migrated (2020-06-06T03:38:44.276-0700)

I was able to reproduce this bug in Minecraft 1.16-pre2

### Comment 28: migrated (2020-06-10T12:05:30.731-0700)

Confirmed in 1.16-pre3.

### Comment 29: migrated (2020-06-11T12:01:06.233-0700)

Confirmed in 1.16-pre4.

### Comment 30: migrated (2020-06-12T11:57:57.106-0700)

Confirmed in 1.16-pre5.

### Comment 31: migrated (2020-06-15T14:10:46.802-0700)

Confirmed in 1.16-pre6.

### Comment 32: migrated (2020-06-17T02:08:27.348-0700)

Confirmed in 1.16-pre7.

### Comment 33: migrated (2020-06-17T11:45:50.280-0700)

Reproduced in 1.16-pre8

### Comment 34: migrated (2020-06-18T05:11:03.776-0700)

: you are the reporter of the ticket. You can, therefore, update the affected versions yourself, no need to comment it

### Comment 35: migrated (2020-06-18T05:34:35.452-0700)

@conem I honestly just behaved like others here, didn't mean to break any rules or something.

### Comment 36: migrated (2020-06-19T07:13:48.335-0700)

Confirmed in 1.16-rc1.

### Comment 37: migrated (2020-06-24T09:22:04.932-0700)

Actually, OptiFine developer fixed this bug -> GitHub issue

### Comment 38: migrated (2021-04-20T20:00:46.327-0700)

Need to up this bug to fix it definitely and close this ticket. Still not fixed in 21w15a.

### Comment 39: ampolive (2021-10-08T12:47:30.471-0700)

Can confirm in 21w40a.

### Comment 40: ampolive (2021-10-14T07:52:56.123-0700)

Can confirm in 21w41a.

### Comment 41: ampolive (2021-10-27T18:37:18.754-0700)

Can confirm in 21w43a.

### Comment 42: ampolive (2021-11-03T15:37:29.896-0700)

Can confirm in 21w44a.

### Comment 43: migrated (2021-11-21T11:35:35.185-0800)

The bug is present in 1.18-pre5.

### Comment 44: Avoma (2021-12-11T05:31:28.783-0800)

Can confirm in 1.18.1.

### Comment 45: Avoma (2022-03-09T12:18:50.696-0800)

Can confirm in 1.18.2.

### Comment 46: LabyStudio (2022-07-15T09:17:18.881-0700)

Hey, this issue has been around for a while now, so I just want to explain how to fix it.
The cape is simply not interpolated correctly at a certain point in the code.
To fix this you only have to change one line in the following method:
net.minecraft.client.renderer.entity.layers.CapeLayer#render
Add the interpolation to the body rotation by multiplying the rotation with the partialTicks variable.
That's it! You can also take a look at my screenshot of my changes to the code:
!diff.png!
I really hope that helps to fix this issue!

### Comment 47: Avoma (2022-08-28T09:56:34.366-0700)

Can confirm in 1.19.2.

### Comment 48: migrated (2022-12-12T20:26:28.952-0800)

A speculation of why the solution proposed by @LabyStudio was not implemented yet, seems like it was caused by another issue.
At that point in code, if the entity is a passenger of another entity, "entity.yBodyRot" have its value clamped at between -360 and 360, while "entity.yBodyRotO" still have its normal value, outside that range.
So by that, doing the linear interpolation (lerp) as proposed, the final result would vary depending on how much the two rotation values differs.
