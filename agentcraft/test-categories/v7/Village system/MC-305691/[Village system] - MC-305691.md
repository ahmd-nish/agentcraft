# MC-305691: Villagers have insomnia

**Mojira URL:** [https://bugs.mojang.com/browse/MC-305691](https://bugs.mojang.com/browse/MC-305691)

## Report details

- **Mojira categories:** Mob behaviour; Village system
- **Project:** MC
- **Issue key:** MC-305691
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2026-01-13T08:49:25.522-0800
- **Updated:** 2026-03-11T03:56:44.299-0700
- **Resolution date:** 2026-01-20T03:14:18.625-0800
- **Affects versions:** 26.1 Snapshot 3
- **Fix versions:** 26.1 Snapshot 4
- **Area:** Platform EC
- **Votes:** 5
- **Watchers:** 4
- **Attachments:** 1
- **Attachment filenames:** 2026-01-13.png
- **Issue links:** Duplicate:inward:MC-305846:Iron golem autocreation is out of control

## Description

This behavior was introduced in 26.1-snapshot-3.
The bug
At night, villagers try to sleep but fail to do so.
Steps to reproduce
- Create a world.

- Summon a villager and place a bed nearby. The villager will claim the bed, emitting green particles.

- Leave and reenter the area, or save and rejoin the world.

- Wait for night to fall, or set the time to night.

Observed behavior
The villager will approach the bed but will not lie down. When placing another bed nearby, the villager will emit green particles again and enter it.
Expected behavior
The villager would enter the bed.

## Comments (4)

### Comment 1: Ioannis Papadopoulos (2026-01-13T08:49:26.355-0800)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: eowyn36 (2026-01-14T01:35:13.063-0800)

Hello! We were not able to reproduce this in the 26.1-snapshot-3. Is there any reproduction steps that you can provide?

### Comment 3: MrMuskle (2026-01-14T08:17:02.274-0800)

The Environment field is supposed to only contain PC details.

### Comment 4: Ioannis Papadopoulos (2026-01-15T17:27:51.218-0800)

Yes of course, basically the beds were placed before the current snapshot (snapshot 3 26.1) and when it was night time, the villagers would only walk over to the beds and then leave. But after I had replaced the beds, the sleeping function returned so the villagers could sleep again. I am guessing this is the problem, with already existing beds not working for villagers?
