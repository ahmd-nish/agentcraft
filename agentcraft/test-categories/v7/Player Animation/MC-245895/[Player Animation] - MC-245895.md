# MC-245895: View Bobbing stops working after long elytra flight

**Mojira URL:** [https://bugs.mojang.com/browse/MC-245895](https://bugs.mojang.com/browse/MC-245895)

## Report details

- **Mojira categories:** Player Animation; Rendering
- **Project:** MC
- **Issue key:** MC-245895
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2021-12-21T13:10:40.096-0800
- **Updated:** 2025-10-30T06:36:32.498-0700
- **Resolution date:** 2025-10-30T06:36:32.406-0700
- **Affects versions:** 1.18.1; 1.18.2; 22w18a; 22w19a; 1.19 Pre-release 3; 1.20 Pre-release 6
- **Fix versions:** 25w45a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 0
- **Issue links:** Relates:inward:MC-199467:Certain entity animations stop after they've existed in world for too long

## Description

After flying around with the elytra equipped generating chunks for about one to two hours, view bobbing stops working even when the view bobbing setting is on. It acts like if the view bobbing setting is turned off, indicated by the player's arms no longer moving as the player is walking.
What I expected to happen:
View bobbing still working after flying around with the elytra equipped generating chunks for about one to two hours. The player's arms still moves when the player is walking.
What actually happened:
View bobbing stopped working after flying around with the elytra equipped generating chunks for about one to two hours. The player's arms does not move when the player is walking.
Steps to reproduce:
- load up a creative mode world,

- turn view bobbing setting on in options,

- equip an elytra and have fireworks in inventory,

- fly around using the equipped elytra and fireworks in inventory to generate new chunks for about one to two hours,

- observe that the player's arms no longer moves as the player is walking (showing that view bobbing stopped working).

Below is a link to a Youtube video that I recorded to show the process to reproduce this bug. I have also added chapters on the video.
https://youtu.be/Et19RboaRCw

## Comments (2)

### Comment 1: Avoma (2023-05-28T08:07:25.848-0700)

I was actually able to confirm this. After around two hours of flying with my elytra, view bobbing indeed stopped working despite view bobbing being turned on in the video settings. After reloading the world, the problem was gone.

### Comment 2: ampolive (2023-07-11T17:11:20.434-0700)

Seems to be a case of . Marking as related.
