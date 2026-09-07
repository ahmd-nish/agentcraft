# MC-169969: The back faces of spawners do not render

**Mojira URL:** [https://bugs.mojang.com/browse/MC-169969](https://bugs.mojang.com/browse/MC-169969)

## Report details

- **Mojira categories:** Rendering; Textures and models
- **Project:** MC
- **Issue key:** MC-169969
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2020-01-16T19:57:17.009-0800
- **Updated:** 2025-04-29T11:42:08.422-0700
- **Resolution date:** 2023-11-08T07:11:23.831-0800
- **Affects versions:** 1.15.1; 1.15.2 Pre-release 2; 1.15.2; 20w18a; 1.16 Pre-release 1; 1.16 Pre-release 3; 1.16.3; 20w51a; 1.16.5; 21w06a; 21w07a; 21w08b; 21w13a; 21w14a; 21w15a; 21w16a; 21w17a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17 Pre-release 3; 1.17 Pre-release 4; 1.17 Pre-release 5; 1.17 Release Candidate 1; 1.17 Release Candidate 2; 1.17; 1.17.1 Pre-release 1; 1.17.1 Pre-release 2; 1.17.1 Pre-release 3; 1.17.1 Release Candidate 1; 1.17.1; 21w38a; 21w40a; 21w42a; 21w43a; 21w44a; 1.18; 1.18.1; 1.18.2; 22w14a; 1.19; 1.19.2; 22w45a; 1.20.2
- **Fix versions:** 23w45a
- **Area:** Platform
- **Labels:** missing-planes; vanilla-parity
- **Watchers:** 1
- **Attachments:** 5
- **Attachment filenames:** cube_all_inner.json; cube_w_inner.json; MC-169969.mp4; MC-169969.png; spawner.json
- **Issue links:** Relates:outward:MC-266252:The back faces of copper grates do not render | Relates:inward:MC-129108:The back faces of cacti do not render | Duplicate:inward:MC-167808:Inside textures of spawner are invisible | Duplicate:inward:MC-182523:Spawners and leaves doesn't show back faces | Duplicate:inward:MC-187443:Leaves fully transparent on sides not in direct view | Relates:inward:MC-34649:Glass panes, stained glass and ice show the texture in all faces

## Description

The resource pack attached to MC-237955 offers a complete fix for this issue. Mojang have my full permission to (and are encouraged to) replace the affected vanilla model files with the contents of the resource pack.
The bug
The back faces of spawner blocks do not render. This results in spawners looking rather odd, as only the faces closest to the player are visible, making it look like the block only has one to three faces total.
This can be considered a parity issue, as spawners in Bedrock Edition are not subject to this.
How to reproduce
- Obtain a spawner via commands (the Creative inventory will not work for this, see MC-132820):

```
/give @s minecraft:spawner
```

- Place down a single, isolated spawner block

- Observe how many faces are visible. Depending on the view direction, between one and three faces are able to be seen.

- Now go around to the other side of the spawner block

- Note how there are indeed faces there as well, despite the original view direction implying there are no faces with spawner bars.

Expected result
These back faces of the spawner would be visible from all faces.
Actual result
The spawner block just doesn't show the back faces, which looks very strange.
How to fix
The resource pack attached to  fixes this issue completely. A new "hollow cube" template model is created by it, based on the old powder snow model. Powder snow, spawners and both types of azalea leaves () are all pointed to this model, resulting in them having internal faces and fixing this issue.

## Comments (25)

### Comment 1: migrated (2020-01-16T19:57:17.009-0800)

This comment contained multiple image attachments (5), please login to view the attachments.

### Comment 2: tryashtar (2020-01-16T20:31:35.757-0800)

Pretty sure this is intended, as MC-34649 was fixed?

### Comment 3: migrated (2020-01-16T20:54:57.157-0800)

Relates to .

### Comment 4: migrated (2020-01-24T19:27:18.733-0800)

To fix. Spawners and leaves should render back faces, or changes to spawners and leaves to 3d texture.

### Comment 5: SunCat (2020-08-23T14:39:30.346-0700)

Split off leaves into

### Comment 6: muzikbike (2020-10-28T08:26:29.584-0700)

Models to fix this attached

### Comment 7: Avoma (2021-01-16T07:26:27.083-0800)

Can confirm in 20w51a.

### Comment 8: Avoma (2021-02-14T09:40:58.893-0800)

Can confirm in 21w06a.

### Comment 9: Avoma (2021-02-22T01:38:40.224-0800)

Can confirm in 21w07a.

### Comment 10: Avoma (2021-03-08T07:50:41.757-0800)

Can confirm in 1.16.5 and 21w08b.

### Comment 11: Avoma (2021-04-11T11:56:24.909-0700)

Can confirm in 21w14a. Requesting ownership as the reporter's account has been marked as inactive.

### Comment 12: migrated (2021-04-20T09:55:21.154-0700)

Duplicate of [MC-34751]

### Comment 13: migrated (2021-06-22T20:13:09.162-0700)

Powder snow have back face texture so they should have way to fix.

### Comment 14: migrated (2021-06-23T00:39:08.646-0700)

Is not a duplicate is a clone.

### Comment 15: ampolive (2021-10-08T15:25:27.522-0700)

Can confirm in 21w40a.

### Comment 16: muzikbike (2021-10-10T12:55:33.368-0700)

May I request ownership of this ticket as the owner of many other model tickets, including another ticket which entirely fixes this issue ()?

### Comment 17: Tanuki_Bakero (2021-10-21T10:56:31.792-0700)

Confirmed with 21w42a

### Comment 18: ampolive (2021-10-30T08:02:56.032-0700)

Can confirm in 21w43a.

### Comment 19: ampolive (2021-11-09T05:46:10.117-0800)

Can confirm in 21w44a.

### Comment 20: Avoma (2021-12-08T07:21:04.901-0800)

Can confirm in 1.18.

### Comment 21: Avoma (2021-12-12T07:08:29.240-0800)

Can confirm in 1.18.1.

### Comment 22: Avoma (2022-03-07T09:52:29.217-0800)

Can confirm in 1.18.2.

### Comment 23: Avoma (2022-06-24T09:08:57.266-0700)

Can confirm in 1.19.

### Comment 24: NBG-bootmgr (2022-08-15T22:10:18.023-0700)

Can confirm in 1.19.2.

### Comment 25: ampolive (2023-11-08T07:11:02.349-0800)

This has been fixed in 23w45a.
