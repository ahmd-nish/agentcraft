# MC-299770: Chunks loaded by ender pearls permanently unload upon player death even when enderPearlsVanishOnDeath is set to false

**Mojira URL:** [https://bugs.mojang.com/browse/MC-299770](https://bugs.mojang.com/browse/MC-299770)

## Report details

- **Mojira categories:** Chunk loading; Entities
- **Project:** MC
- **Issue key:** MC-299770
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2025-07-15T20:58:55.871-0700
- **Updated:** 2025-07-31T02:26:40.508-0700
- **Resolution date:** 2025-07-31T02:26:40.432-0700
- **Affects versions:** 1.21.7; 1.21.8 Release Candidate 1; 1.21.8; 25w31a
- **Fix versions:** 25w32a
- **Area:** Platform
- **Votes:** 3
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** Pearls not loading chunks death.zip
- **Issue links:** Relates:inward:MC-289348:Ender pearls stop loading chunks in The End after relog, if there are no players in that dimension

## Description

This bug is related to , as it gets the ender pearl in a bugged state where they no longer load chunks at all even when the player associated with it is online. (the pearl gets deloaded).

What happens is the pearl is temporarily not loading chunks when the player is dead. If you don’t rapidly respawn (click the respawn button within 2 seconds after death) the chunk the pearl is within will deload. And not reload when you respawn (which would be expected, as pearls should load chunks.). The only way to get the pearl to load these chunks again is to manually load them by walking to the chunk.

When enderPearlsVanishOnDeath is set to false, pearls still vanish on death. They just reappear when you respawn. A simple fix to this bug would be to make sure pearls continue to load the chunk they are in when they are in this temporary vanished state.

I have attached a simple world that allows you to see this bug in action. I made sure to set spectatorsGenerateChunks to false so you can see when your ender pearl is loading chunks.

Repro steps when in example world:
- Click the button that sets you to spectator mode and teleports you to your ender pearl location. Observe how the chunk your pearl is in is loaded.

- Teleport back to your spawn location /execute in minecraft:overworld run tp @s -6.49 63.00 10009.60 359.33 39.47

- Exit spectator mode.

- Run the /kill command, make sure to wait for more than two seconds before clicking respawn. (chunks pearl is in will deload)

- Click the button. You will see your pearl is not loading any chunks even though you have respawned.

To see how it should work, kill your player in step 4, but rapidly click the respawn button so you respawn in under two seconds. (preventing the chunks from deloading) You will see your pearl is still loading chunks.

## Comments (9)

### Comment 1: John (2025-07-15T20:58:56.384-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: John (2025-07-17T15:30:45.733-0700)

With  being fixed, it should be tested to see if whatever fix was made also fixed this issue.

### Comment 3: Savvvage_ (2025-07-18T16:28:15.034-0700)

Can replicate

### Comment 4: [MOD] Greymagic27 (2025-07-20T07:07:32.437-0700)

Is this still an issue for you? When clicking the button now, the chunk doesn’t appear loaded until I change out of spectator mode.

### Comment 5: John (2025-07-20T07:18:40.987-0700)

The intended behavior is the chunks SHOULD be loaded when you teleport in spectator mode. The death of your player is causing your pearls chunks to permanently deload, and they don’t reload upon your respawn. (you teleport in spectator mode to see if they are loaded with spectatorsGenerateChunks set to false).
Since they are not loaded for you, you have successfully replicated the issue.

### Comment 6: [MOD] Greymagic27 (2025-07-20T07:36:01.407-0700)

Thanks

### Comment 7: John (2025-07-20T07:38:29.864-0700)

End credits can also cause ender pearl chunks to permanently unload. Likely cause of

### Comment 8: John (2025-07-20T08:50:46.455-0700)

Can you please update the confirmation status of this issue?

### Comment 9: John (2025-07-29T17:14:00.880-0700)

Confirmed this bug is still present in 25w31a. The fix for   does not fix this bug.
