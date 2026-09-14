# MC-101376: Elytra appearance doesn't update in 1st person mode; only in 3rd person

**Mojira URL:** [https://bugs.mojang.com/browse/MC-101376](https://bugs.mojang.com/browse/MC-101376)

## Report details

- **Mojira categories:** Player Animation
- **Project:** MC
- **Issue key:** MC-101376
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2016-04-27T17:40:07.575-0700
- **Updated:** 2025-04-26T04:59:52.258-0700
- **Resolution date:** 2024-11-30T04:08:35.032-0800
- **Affects versions:** Minecraft 1.9.2; Minecraft 1.9.4; Minecraft 16w20a; Minecraft 1.10 Pre-Release 1; Minecraft 1.10; Minecraft 1.10.2; Minecraft 16w32a; Minecraft 16w32b; Minecraft 1.12; Minecraft 1.13.1; 1.16.1; 20w27a; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 20w48a; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w07a; 21w11a; 1.17.1; 1.18.1; 1.19.2; 22w42a; 1.19.3; 1.19.4; 1.20.1; 1.20.2; 23w43b; 1.21
- **Fix versions:** 24w33a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** MC-101376.mp4
- **Issue links:** Relates:inward:MCPE-188694:The Elytra animation only plays in 3rd person, not 1st person

## Description

The bug
If you're gliding in 1st person mode with elytra, and change to 3rd person, it will then update the elytra appearance to gliding. Then, if you land in 1st person and then switch to 3rd person, it will also then update the elytra appearance to still.
How to reproduce
- Stand on a block

- Go to 3rd person view, then back to 1st person

- Start gliding

- Go to 3rd person view
(If you glide, do step 2, land, and then do step 4, it will present the same issue)

Whenever I do this, doing step 4 causes the wings to spread apart (or draw back together). This means that the elytra are only updating when you are looking at yourself, even though they should already be in the correct position when you switch to 3rd person view (the very tick you switch to switch to 3rd person it should be in the correct position ).
NOTE: This bug could be invalid due to how entity rendering and updates work (in 1st person the player is not being rendered yet)

## Comments (11)

### Comment 1: migrated (2016-04-27T17:40:07.575-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: migrated (2016-06-04T11:04:02.943-0700)

I've encountered this problem in the first pre-release for 1.10.

### Comment 3: migrated (2016-08-05T16:53:57.372-0700)

One more day until it's a hundred days old without Mojang acknowledgement, which tells you that many bugs are being reported and the Minecraft team is cooking up some great ideas at the office, while I am making grammatically accurate sentences that many would deem to be too long.

### Comment 4: migrated (2016-08-16T23:44:10.518-0700)

Yeah, I hate it when I craft a perfectly correct sentence, but people call it a run-on because it's a paragraph long. Very annoying.

### Comment 5: TheDoctorLink (2017-08-04T02:43:34.631-0700)

Version 1.12 is also affected, and this bug also occurs in Multiplayer.

### Comment 6: migrated (2018-09-14T06:31:17.903-0700)

Confirmed for 1.13.1, i've also added a slowmo video.

### Comment 7: j_p_smith (2020-07-04T23:52:15.608-0700)

Confirmed in 1.16.1 and 20w27a.

### Comment 8: Avoma (2021-02-07T03:47:19.366-0800)

Can confirm in 21w05b.

### Comment 9: Avoma (2021-02-14T06:00:08.816-0800)

Can confirm in 21w06a.

### Comment 10: Avoma (2021-02-22T04:48:47.690-0800)

Can confirm in 21w07a.

### Comment 11: Avoma (2021-03-22T06:47:05.590-0700)

Can confirm in 21w11a.
