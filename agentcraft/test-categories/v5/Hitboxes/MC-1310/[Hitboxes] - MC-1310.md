# MC-1310: Dispensed boats and rafts get stuck inside of dispensers used to place them

**Mojira URL:** [https://bugs.mojang.com/browse/MC-1310](https://bugs.mojang.com/browse/MC-1310)

## Report details

- **Mojira categories:** Entities; Hitboxes
- **Project:** MC
- **Issue key:** MC-1310
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2012-10-30T06:35:54.587-0700
- **Updated:** 2025-05-27T07:46:39.804-0700
- **Resolution date:** 2023-05-16T01:11:39.237-0700
- **Affects versions:** Minecraft 1.4.2; Minecraft 1.4.5; Snapshot 13w05b; Snapshot 13w10a; Minecraft 1.6.2; Minecraft 1.7.4; Minecraft 14w02c; Minecraft 14w03a; Minecraft 14w03b; Minecraft 14w04b; Minecraft 1.8; Minecraft 1.8.1-pre3; Minecraft 15w36d; Minecraft 1.13.2; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 19w02a; Minecraft 19w03a; Minecraft 19w03b; Minecraft 19w03c; 1.14.4; 1.15 Pre-release 3; 1.15 Pre-release 4; 1.15 Pre-release 5; 1.15 Pre-release 7; 1.15; 1.15.1; 1.15.1 Pre-release 1; 1.15.2 Pre-Release 1; 1.15.2 Pre-release 2; 1.15.2; 20w06a; 20w07a; 20w08a; 20w09a; 20w10a; 20w11a; 20w12a; 20w13a; 20w13b; 20w14a; 20w15a; 20w16a; 20w17a; 20w18a; 20w19a; 20w20b; 20w21a; 20w22a; 1.16 Pre-release 1; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 4; 1.16 Pre-release 5; 1.16 Pre-release 7; 1.16 Pre-release 8; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w27a; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Pre-release 2; 1.16.2 Pre-release 3; 1.16.2 Release Candidate 1; 1.16.2 Release Candidate 2; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4 Pre-release 1; 1.16.4 Pre-release 2; 1.16.4 Release Candidate 1; 1.16.4; 20w45a; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w08b; 21w10a; 21w11a; 21w13a; 21w14a; 21w15a; 21w16a; 21w17a; 21w18a; 21w19a; 21w20a; 1.17 Release Candidate 2; 1.17; 1.17.1; 21w39a; 21w40a; 21w41a; 21w42a; 1.18; 1.18.1; 22w05a; 1.18.2 Release Candidate 1; 1.18.2; 22w12a; 22w14a; 1.19; 1.19.1; 1.19.2; 22w43a; 1.19.3; 23w03a; 23w04a; 1.19.4
- **Fix versions:** Minecraft 15w47a; 1.20 Pre-release 2
- **Labels:** boat; dispenser
- **Watchers:** 2
- **Attachments:** 8
- **Attachment filenames:** 2013-07-14_15.54.04.png; 2018-09-29_23.21.11.png; 2021-05-12_15.03.27.png; 94o4Dh.png; aE3wlh.png; MC-1310.mp4; setup.png; snXqqh.png
- **Issue links:** Relates:inward:MC-101334:Required space for placing a boat is too small | Relates:inward:MC-3709:Boats and Dispensers are wonky

## Description

The Bug:
Dispensed boats and rafts get stuck inside of dispensers used to place them.
Steps to Reproduce:
- Build the setup as shown in the attachment below.

- Place a boat inside the dispenser.

- Enable entity hitboxes by pressing "F3 + B".

- Use the lever to activate the dispenser.

- Look closely at where the boat comes in contact with the dispenser.

- Take note as to whether or not dispensed boats and rafts get stuck inside of dispensers used to place them.

Observed Behavior:
Dispensed boats and rafts get stuck inside of dispensers used to place them.
Expected Behavior:
Dispensed boats and rafts would not get stuck inside of dispensers used to place them. They should be dispensed a bit more forward in order to avoid this issue from occurring.

## Comments (23)

### Comment 1: migrated (2012-10-30T06:35:54.587-0700)

This comment contained multiple image attachments (8), please login to view the attachments.

### Comment 2: migrated (2012-10-30T11:01:00.458-0700)

Screenshots:
http://i.imgur.com/snXqqh.png
http://i.imgur.com/94o4Dh.png
http://i.imgur.com/aE3wlh.png

### Comment 3: kumasasa (2013-07-14T06:55:52.402-0700)

Secondary issue: Texture fighting

### Comment 4: Ezekiel (2014-01-22T07:56:15.204-0800)

Is this still a concern in the latest Minecraft version 14w03b? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 5: migrated (2014-01-22T08:36:27.525-0800)

Yes, it is. By the way: This bug is dependent on the orientation of the dispenser.

### Comment 6: Ezekiel (2014-07-26T11:40:48.701-0700)

Is this still a concern in the latest Minecraft version 14w30c? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 7: galaxy_2alex (2014-10-24T10:48:13.679-0700)

Issue is slightly resolved, however, boat is still in a block after dispensing.

### Comment 8: qmagnet (2015-09-10T04:49:30.985-0700)

Confirmed for 15w36d

### Comment 9: migrated (2015-11-18T14:15:45.639-0800)

As of 15w47a, boats are no longer stuck in the dispenser; they can be used, however, depending on orientation, the boat will still be placed on top of the block below it. The boat can still be used, however, as shown in this video: https://www.youtube.com/watch?v=Kb2jBrHlIfo&feature=youtu.be

### Comment 10: kumasasa (2015-11-18T14:37:08.068-0800)

Fix confirmed.

### Comment 11: migrated (2016-01-11T17:05:50.583-0800)

I'm a bit surprised this is marked as fixed, since this is happening to me right now on 1.8.9.
The boat gets placed half stuck in the dispenser: while the boat itself isn't stuck, as soon as you jump in, you will end up with your head in the dispenser, and start suffocating…

### Comment 12: migrated (2016-01-11T17:53:34.705-0800)

This is already fixed for 1.9.

### Comment 13: migrated (2018-09-29T14:21:52.589-0700)

i attached a screenshot, this problem still exists as of 1.13.1

### Comment 14: migrated (2019-05-17T07:42:23.025-0700)

Still in 1.14.1
The problem is that the boats are being placed slightly inside the dispenser block and thus they will stay on top of the block underneath the dispenser and its two neighbouring blocks.
I think this could have happend because the hitbox of the boats did change when they reworked them (maybe...?)

### Comment 15: Avoma (2020-11-25T11:27:01.338-0800)

Can confirm in 20w48a.

### Comment 16: Avoma (2021-01-22T02:51:13.302-0800)

Can confirm in 21w03a.

### Comment 17: Avoma (2021-02-03T11:09:40.852-0800)

Can confirm in 21w05a.

### Comment 18: Avoma (2021-02-04T10:26:40.789-0800)

Can confirm in 21w05b.

### Comment 19: Avoma (2021-03-14T06:30:18.704-0700)

Video attached.

### Comment 20: Avoma (2021-10-03T03:00:44.035-0700)

Can confirm this in 21w39a. Here are some extra details regarding this problem.
The Bug:
Dispensed boats get stuck inside of dispensers used to place them.
Steps to Reproduce:
- Build the setup as shown in the attachment below.

- Place a boat inside the dispenser.

- Enable entity hitboxes by pressing "F3 + B".

- Use the lever to activate the dispenser.

- Look closely at where the boat comes in contact with the dispenser.

Observed Behavior:
Dispensed boats get stuck inside of dispensers used to place them.
Expected Behavior:
Dispensed boats would not get stuck inside of dispensers used to place them. They should be dispensed a bit more forward in order to avoid this issue from occurring.

### Comment 21: Brain81505 (2023-01-18T08:14:38.339-0800)

Can confirm in 23w03a

### Comment 22: Brain81505 (2023-01-24T23:23:27.309-0800)

Can confirm in 23w04a

### Comment 23: Brain81505 (2023-02-01T08:05:07.185-0800)

Can confirm in 23w06a
