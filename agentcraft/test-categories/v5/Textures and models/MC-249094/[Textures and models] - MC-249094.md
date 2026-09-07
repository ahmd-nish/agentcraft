# MC-249094: Unexpected culling of inner sculk shrieker faces

**Mojira URL:** [https://bugs.mojang.com/browse/MC-249094](https://bugs.mojang.com/browse/MC-249094)

## Report details

- **Mojira categories:** Textures and models
- **Project:** MC
- **Issue key:** MC-249094
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2022-03-16T10:34:20.305-0700
- **Updated:** 2025-04-26T14:16:45.745-0700
- **Resolution date:** 2024-09-10T04:25:12.558-0700
- **Affects versions:** 22w11a; 22w12a; 22w14a; 22w15a; 22w16b; 22w17a; 22w18a; 1.19 Pre-release 1; 1.19 Pre-release 2
- **Fix versions:** 22w15a; 1.19 Pre-release 3
- **Labels:** unnecessary-cullface
- **Watchers:** 1
- **Attachments:** 7
- **Attachment filenames:** 2022-03-16_17.32.24.png; 2022-03-16_17.32.25.png; MC-249094.mp4; MC-249094 - 22w15a.png; MC-249094 - With Block.png; MC-249094 - Without Block.png; sculk-shrieker-fix-22w18a-v1.0.zip

## Description

The resource pack attached offers a complete fix for this issue. Mojang have my full permission to (and are encouraged to) replace the affected vanilla model files with the contents of the resource pack.
Download resource pack:
- 22w18a:

The bug
The western bony structures extending from sculk shriekers have their side faces culled by blocks opposite from them.
How to reproduce
- Place a sculk shrieker

- Place a solid block to its east

Expected results
The tooth structures would not have any of their faces culled.
Actual results
They do.
How to fix
I've attached a resource pack that fixes this issue as well as MC-249097 by adding needed and removing unwanted cullface arguments where necessary from the sculk shrieker template model. This resource pack also cleans up the sculk shrieker model's code by introducing spacing and namespacing more consistent with other model files, ultimately reducing the file size considerably as well. As such, I'd recommend using this model file directly to fix these issues than attempting to fix both issues manually for quickness's sake as well as in the interests of readability.

## Comments (10)

### Comment 1: migrated (2022-03-16T10:34:20.305-0700)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: Avoma (2022-03-16T10:39:14.026-0700)

, this ticket has 21w11a marked as affected, thus making this report valid because 21w11a isn't an experimental snapshot.

### Comment 3: Avoma (2022-03-16T10:40:30.717-0700)

Can confirm.

### Comment 4: migrated (2022-03-16T10:43:59.540-0700)

Oh sorry I didn’t see that the Sculk stuff was included

### Comment 5: mbanders (2022-04-13T10:14:44.424-0700)

Not fixed in 22w15a.

### Comment 6: Avoma (2022-04-13T11:01:31.666-0700)

This issue is still present in 22w15a, therefore I'd like to request for this ticket to be reopened.

### Comment 7: slicedlime (2022-04-13T17:06:45.856-0700)

Issue is still present in 22w15a.

### Comment 8: migrated (2022-04-26T12:54:03.221-0700)

The issue remains in 22w16b

### Comment 9: migrated (2022-05-04T07:05:16.337-0700)

Issue remains in 22w17a.

### Comment 10: migrated (2022-05-24T07:53:23.427-0700)

Can confirm in 1.19 pre-release 2.
