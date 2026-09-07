# MC-236682: Large and continuous lag spikes sometimes occur when loading/reloading into a world in 21w37a

**Mojira URL:** [https://bugs.mojang.com/browse/MC-236682](https://bugs.mojang.com/browse/MC-236682)

## Report details

- **Mojira categories:** Performance
- **Project:** MC
- **Issue key:** MC-236682
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2021-09-15T12:16:23.152-0700
- **Updated:** 2025-05-02T01:02:07.366-0700
- **Resolution date:** 2021-09-24T09:44:20.208-0700
- **Affects versions:** 21w37a
- **Fix versions:** 21w38a
- **Watchers:** 1
- **Attachments:** 7
- **Attachment filenames:** 2021-09-16_21_16_39-21w37a-21w37a.zip; 2021-09-16_21_58_26-New World 3-21w37a.zip; 2021-09-16_21.29.25.png; MC-236682.mp4; MC-236682.png; MC-236682 - Behavior during creation of performance profile.mp4; MC-236682 - Performance Profile.zip
- **Issue links:** Relates:outward:MC-236646:Major performance decrease when exploring chunks in 21w37a

## Description

The Bug:
Large and continuous lag spikes sometimes occur when loading/reloading into a world in 21w37a.
This issue did not occur in 1.17.1. This may be quite difficult to reproduce as this does not happen all of the time.
Steps to Reproduce:
- Create a new world in 21w37a.

- Exit the world.

- Join the world again.

- →  Notice how large and continuous lag spikes sometimes occur when loading/reloading into a world in 21w37a.

Expected Behavior:
The expected behavior would be that no large and continuous lag spikes would sometimes occur when loading/reloading into a world in 21w37a.

## Comments (13)

### Comment 1: migrated (2021-09-15T12:16:23.152-0700)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: Avoma (2021-09-15T12:16:45.024-0700)

Please note that this isn't the same as . This issue () occurs even when not loading chunks.

### Comment 3: winauer (2021-09-15T12:36:53.297-0700)

Seems like the game is out of available memory (94% in your screenshot) and stalling to wait for the GC. Try allocating more RAM.

### Comment 4: ampolive (2021-09-15T12:48:45.836-0700)

This might be a separate issue actually. The game is using more RAM than in 1.17.1.

### Comment 5: winauer (2021-09-15T12:54:25.680-0700)

@ampolive The game needing more RAM is not surprising, it has to hold more block data due to the extended height.

### Comment 6: Adrian Östergård (2021-09-16T00:11:51.752-0700)

Please attach a performance profile by using the key combination F3+L in the game.

### Comment 7: [Mod]Les3awe (2021-09-16T06:22:53.407-0700)

It can be confirmed that the loading world in the snapshot is more lagging than 1.17.
But due to the computer configuration, my lag is not so serious.
My performance profile,

### Comment 8: Avoma (2021-09-16T10:45:39.937-0700)

As requested, I've attached a performance profile along with an additional video of what I was experiencing in-game whilst the debug profile was being created. Please let me know if any other information is required in order to figure out what the problem is here.

### Comment 9: ampolive (2021-09-16T17:59:36.120-0700)

Also attached a profile.

### Comment 10: Ceresjanin123 (2021-09-17T06:11:21.087-0700)

This is a duplicate of MC-236665

### Comment 11: anthony cicinelli (2021-09-23T09:19:41.472-0700)

This appears fixed in 21w38a

### Comment 12: [Mod] Neko (2021-09-23T13:08:42.331-0700)

can you confirm this is fixed as well?

### Comment 13: Avoma (2021-09-24T08:11:44.580-0700)

Hi . Yes, I'm also able to confirm that this issue has been fixed in 21w38a.
