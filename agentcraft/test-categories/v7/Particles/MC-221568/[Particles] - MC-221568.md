# MC-221568: Inconsistency: Barriers and structure voids produce particles when broken, but light blocks do not

**Mojira URL:** [https://bugs.mojang.com/browse/MC-221568](https://bugs.mojang.com/browse/MC-221568)

## Report details

- **Mojira categories:** Particles
- **Project:** MC
- **Issue key:** MC-221568
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-03-31T10:35:19.401-0700
- **Updated:** 2025-04-11T12:40:25.998-0700
- **Resolution date:** 2023-05-15T07:40:20.727-0700
- **Affects versions:** 21w13a; 21w14a; 21w15a; 21w16a; 21w17a; 1.17; 1.17.1; 1.18.1; 22w12a; 1.19; 1.19.1 Pre-release 5; 1.19.2
- **Fix versions:** 22w42a
- **Labels:** barrier; invisible-block-manipulation; invisible-blocks; invisible-blocks-not-invisible; light_block; structure_void; unnecessary-particles
- **Watchers:** 1
- **Attachments:** 7
- **Attachment filenames:** 2021-03-31_18.31.59.png; 2021-03-31_18.32.00.png; 2021-03-31_18.32.03.png; 2021-03-31_18.32.04.png; 2021-03-31_18.32.21.png; 2021-03-31_18.32.22.png; MC-221568.mp4
- **Issue links:** Relates:outward:MC-221864:Iron golems produce walking particles for light blocks | Relates:inward:MC-249384:Warden can create light, barrier and structure void particles when digging

## Description

Relates to
When broken by a Creative mode player, the command-exclusive barrier and structure block both produce dedicated block breaking particles. 21w13a introduces light blocks, which are similar in them being command-exclusive and having special functionality when the item is held. The light block, however, does not produce particles when broken, unlike the other two, leading me to believe this is a bug.
The expected behaviour would be that barriers and structure voids should not produce particles when broken, as they are meant to be fully invisible in gameplay outside of special circumstances. This should also be true in other circumstances where particles are produced, such as falling on the block from a height, sprinting on the block, punching the block, and having an iron golem walk on it.

## Comments (13)

### Comment 1: migrated (2021-03-31T10:35:19.401-0700)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: Avoma (2021-03-31T10:35:42.727-0700)

Can confirm.

### Comment 3: Avoma (2021-04-02T06:19:50.938-0700)

Video attached.

### Comment 4: Avoma (2021-04-08T04:01:25.302-0700)

Can confirm in 21w14a.

### Comment 5: migrated (2021-04-09T03:02:23.255-0700)

I think the bug here is light blocks not producing breaking particles.

### Comment 6: Avoma (2021-04-14T10:46:48.660-0700)

Can confirm in 21w15a.

### Comment 7: Avoma (2021-04-22T01:38:57.351-0700)

Can confirm in 21w16a.

### Comment 8: Avoma (2021-04-28T10:42:31.004-0700)

Can confirm in 21w17a.

### Comment 9: Avoma (2021-06-09T06:16:40.820-0700)

Can confirm in 1.17.

### Comment 10: Avoma (2021-07-17T10:16:22.724-0700)

Can confirm in 1.17.1.

### Comment 11: Avoma (2021-12-17T02:26:30.742-0800)

Can confirm in 1.18.1.

### Comment 12: Avoma (2022-07-17T07:43:03.591-0700)

Can confirm in 1.19.

### Comment 13: Avoma (2022-09-01T04:56:23.516-0700)

Can confirm in 1.19.2.
