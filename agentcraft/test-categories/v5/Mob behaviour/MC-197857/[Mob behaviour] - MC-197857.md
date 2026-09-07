# MC-197857: Villagers trying to claim claimed beds

**Mojira URL:** [https://bugs.mojang.com/browse/MC-197857](https://bugs.mojang.com/browse/MC-197857)

## Report details

- **Mojira categories:** Mob behaviour
- **Project:** MC
- **Issue key:** MC-197857
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2020-08-12T13:07:03.053-0700
- **Updated:** 2025-05-29T09:16:25.731-0700
- **Resolution date:** 2025-01-04T11:16:39.000-0800
- **Affects versions:** 20w19a; 20w20a; 20w21a; 1.16.2; 1.16.4; 20w48a; 20w49a; 20w51a; 1.16.5; 21w08b; 21w11a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17 Pre-release 5; 1.17; 1.17.1 Pre-release 1; 1.17.1; 21w38a; 21w39a; 21w40a; 21w41a; 1.18 Pre-release 1; 1.18; 1.18.1 Pre-release 1; 1.18.1; 1.18.2; 1.19; 1.19.2; 22w44a; 22w45a; 22w46a; 1.19.3 Pre-release 1; 1.19.3 Pre-release 2; 1.19.3 Pre-release 3; 1.19.3 Release Candidate 1; 1.19.3 Release Candidate 2; 1.19.3; 23w03a; 23w04a; 23w05a; 23w06a; 23w07a; 1.19.4 Pre-release 1; 1.19.4 Pre-release 2; 1.19.4 Pre-release 3; 1.19.4 Pre-release 4; 1.19.4 Release Candidate 1; 1.19.4 Release Candidate 2; 1.19.4 Release Candidate 3; 1.19.4; 23w12a; 23w13a; 23w14a; 23w16a; 23w17a; 23w18a; 1.20 Pre-release 1; 1.20 Pre-release 2; 1.20 Pre-release 4; 1.20 Pre-release 5; 1.20 Pre-release 6; 1.20 Pre-release 7; 1.20 Release Candidate 1; 1.20; 1.20.1 Release Candidate 1; 1.20.1; 23w33a; 1.20.2; 1.20.4; 24w12a; 1.21; 1.21.1; 1.21.3; 24w46a
- **Fix versions:** 1.21.4 Pre-Release 2
- **Area:** Platform
- **Watchers:** 2
- **Attachments:** 7
- **Attachment filenames:** 2020-08-12_15.49.33.png; 2020-08-12_15.50.51.png; 2020-08-13_20.40.38.png; 2023-04-02_18.41.56.png; 24w46a MC-197857.mp4; a crowd of villagers.png; MC-197857_villagers claim claimed beds.mp4
- **Issue links:** Relates:inward:MC-157651:Vilager kids steal beds for sleeping from adults. | Relates:outward:MC-279093:Villagers can get on the same bed | Duplicate:inward:MC-253307:Villagers assign beds despite it being taken or not taken properly | Relates:outward:MC-145862:Villagers try to sleep in occupied beds | Duplicate:inward:MC-211757:Villagers keep on emitting Green particles | Duplicate:inward:MC-219306:When breaking a bed and replacing it, multiple villagers can claim the same bed. | Duplicate:inward:MC-182755:Villagers try to sleep in occupied beds | Duplicate:inward:MC-208278:Villager's AI can't see if there is an villager in the house structure. | Relates:inward:MC-152170:When a villager takes the bed of another villager then the bed's previous owner will not look for a new bed

## Description

The bug
Breaking and placing a claimed bed in the same place causes a second villager to claim it, even though the original owner had not forgotten his bed location. This causes one villager to sleep at night while the other tries to claim the same bed.
What I expected to happen was...:
When replacing the claimed bed, the original owner would either discard his claim or the second villager would not try to claim it.
What actually happened was...:
Two villagers claimed the same bed.
To reproduce:
- In Video Settings, set Particles to All

- Make a trench two blocks deep

- Place a bed and a villager

- Wait for the villager to claim the bed (it will emit green particles)

- Spawn another villager in the trench

- Break and place the bed in the same position

- Check if the second villager claims the bed (it will also emit green particles)

- If it happens, use this command:

```
/time set night
```

- You will see one villager sleeping in the bed, and the other constantly reclaiming the bed (with lots of green particles on his head

## Comments (31)

### Comment 1: migrated (2020-08-12T13:07:03.053-0700)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: galaxy_2alex (2020-08-12T15:22:18.906-0700)

Please provide a screenshot of the setup with the F3 debug screen enabled.

### Comment 3: migrated (2020-08-13T17:46:08.485-0700)

Ok just put the picture with the f3 on. hope it helps

### Comment 4: migrated (2020-09-05T10:20:25.790-0700)

im having the exact same issue so hopefully this is getting resolved soon. since they wont claim unclaimed beds the villagers still think theres available beds and now i have an overabundance of villagers...

### Comment 5: migrated (2020-12-26T01:14:12.634-0800)

Can confirm this for 20w51a.

### Comment 6: migrated (2021-03-26T08:35:09.082-0700)

This bug is still happening in 21w11a, and seems to be caused when a bed is broken or obstructed but the villager who owns the bed doesn't see it happen. It's like there's a disconnect between the game and the villagers in terms of which beds are seen as claimed and which aren’t.

### Comment 7: SoloAlguien (2021-05-15T17:50:20.045-0700)

Can confirm in 21w19a.
- How to Reproduce:

- Set time to noon:

```/time set noon```

- Place a bed and summon a villager, wait until the villager claims the bed.

- Lock up the villager and summon a second one.

- Break and place the bed in the same place, the second villager will claim it.

- Free the first villager and set the time to night:

```/time set night```

- One villager will sleep and the other will repeatedly try to claim the same bed.

- Attached a video which demonstrates this issue:

### Comment 8: SoloAlguien (2021-05-21T22:04:04.391-0700)

Can confirm in 21w20a.

### Comment 9: SoloAlguien (2021-05-28T11:43:35.753-0700)

Can confirm in 1.17 Pre-release 1.

### Comment 10: SoloAlguien (2021-05-31T13:39:57.306-0700)

Can confirm in 1.17 Pre-release 2.

### Comment 11: SoloAlguien (2021-06-01T15:56:40.489-0700)

Can confirm in 1.17 Pre-release 3.

### Comment 12: migrated (2021-06-04T05:20:38.705-0700)

can confirm in 1.16.3, 1.16.4, 1.16.5 and all the current 1.17 pre-releases

### Comment 13: SoloAlguien (2021-06-20T09:34:10.510-0700)

Can confirm in 1.17 and 1.17.1 Pre-release 1.

### Comment 14: SoloAlguien (2021-07-11T15:22:13.683-0700)

Can confirm in 1.17.1.

### Comment 15: migrated (2021-09-25T17:49:22.329-0700)

Can confirm in 21w38a

### Comment 16: SoloAlguien (2021-09-29T13:20:44.591-0700)

Can confirm in 21w39a.

### Comment 17: SoloAlguien (2021-10-07T10:11:56.251-0700)

Can confirm in 21w40a.

### Comment 18: SoloAlguien (2021-10-13T10:27:28.204-0700)

Can confirm in 21w41a.

### Comment 19: SoloAlguien (2021-11-11T11:55:27.567-0800)

Can confirm in 1.18 Pre-release 1.

### Comment 20: SoloAlguien (2021-12-03T16:25:55.619-0800)

Can confirm in 1.18 and 1.18.1 Pre-release 1.

### Comment 21: SoloAlguien (2021-12-17T23:18:49.152-0800)

Can confirm in 1.18.1.

### Comment 22: SoloAlguien (2022-03-01T14:08:26.933-0800)

Can confirm in 1.18.2.

### Comment 23: g5b (2022-07-26T20:11:36.162-0700)

Can confirm in 1.19.

### Comment 24: SoloAlguien (2022-11-02T17:55:25.818-0700)

Can confirm in 1.19.2.

### Comment 25: Brain81505 (2023-01-18T19:07:40.030-0800)

Can confirm in 23w03a

### Comment 26: migrated (2023-04-02T10:44:43.902-0700)

Can confirm in 1.19.4

### Comment 27: migrated (2023-09-30T02:30:49.958-0700)

Can confirm in 1.20.1

### Comment 28: migrated (2024-08-10T09:31:10.434-0700)

Can confirm in 1.21.1

### Comment 29: migrated (2024-08-26T07:13:28.105-0700)

Additionally, villagers may also think these beds are not occupied during breeding, which can lead to a large group of villagers crowding by the beds at night after days, like:

### Comment 30: Arisa Bot (2024-11-16T23:55:42.241-0800)

Please do not add Affected Versions to resolved reports.
Have a look at the Resolution and the comments to see why this ticket has been resolved. If you think this ticket has been resolved erroneously you can contact the Mojira staff on Discord or Reddit.
-- I am a bot. This action was performed automatically! If you think it was incorrect, please notify us on Discord or Reddit

### Comment 31: SoloAlguien (2024-11-17T00:37:26.056-0800)

Can reproduce in 24w46a, please reopen.
Video attached:
