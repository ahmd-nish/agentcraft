# MC-289348: Ender pearls stop loading chunks in The End after relog, if there are no players in that dimension

**Mojira URL:** [https://bugs.mojang.com/browse/MC-289348](https://bugs.mojang.com/browse/MC-289348)

## Report details

- **Mojira categories:** Chunk loading
- **Project:** MC
- **Issue key:** MC-289348
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2025-03-10T17:40:02.987-0700
- **Updated:** 2025-07-20T09:19:05.466-0700
- **Resolution date:** 2025-07-17T08:31:38.809-0700
- **Affects versions:** 1.21.4; 1.21.5; 1.21.6 Pre-Release 2
- **Fix versions:** 25w31a
- **Area:** Platform
- **Votes:** 4
- **Watchers:** 3
- **Attachments:** 1
- **Attachment filenames:** image-20250605-180000.png
- **Issue links:** Relates:outward:MC-299770:Chunks loaded by ender pearls permanently unload upon player death even when enderPearlsVanishOnDeath is set to false

## Description

Pearls in The End dimension will stop loading chunks if the player who threw the pearl leaves the game and rejoins while there are no players in The End dimension.
Steps to reproduce:
- Create an ender pearl stasis chamber using bubble columns in The End and throw an ender pearl in it.

- Place a command block in the same chunk as the ender pearl that repeatedly prints a message to the chat.

- Leave The End dimension and then leave the game.

- Wait for all the players to leave The End, then rejoin the game.

- Notice that the command block will stop printing messages to the chat (and all other redstone devices stop working)

- The chunk will not load if The End dimension is loaded again unless that chunk is manually loaded by a player again.

Expected behavior:
The chunks in The End should continue to load by the thrown ender pearl, even if the dimension was fully unloaded.

## Comments (7)

### Comment 1: [MOD] Greymagic27 (2025-03-21T13:56:38.913-0700)

Please attach a setup that can be used to reproduce this issue

### Comment 2: gnembon (2025-06-04T05:28:40.657-0700)

Repro steps are present. Was able to reproduce

### Comment 3: Savvvage_ (2025-06-05T11:12:18.910-0700)

Code analysis:
When in a dimension there are no forceloaded chunks, no players, no active ender pearls and no entity entered that dimension through a portal for at least 300 gameticks, that dimension will stop processing the entities, block entities and the dragon fight in that dimension.
Obviously when the player logs of, their ender pearl disappears from the end dimension. When the player is logged off, after 300 gameticks, the End dimension will stop processing entities for the reason mentioned above. When the player logs back on, the ender pearl is re-created and placed in the End, but as the End no longer ticks entities, the pearl wont tick, thus its not able to place a chunkloading ticket, which makes the pearl unload.

The check is located in the ServerLevel.java in the tick() method. to be more precisely, here:

Please note, that this is not the only consequence of dimensions stopping processing entities and block entities. This issue also manifests in end gateway based chunkloaders (they break if players leave the End) and a couple more contrpations. Here i explain the issue in much more detail:

Moreover, when the game is frozen with /tick freeze command,  the dimension unloading timer is still running, this leads to nether portal based chunkloaders breaking after player unfreezes the game. (cus entity which is supposed to cycle between dimensions stops ticking, cus the dimension that it is in stops tickin entities) This makes the /tick freeze command intrusive (aka breaks contraptions).

I'd Suggest 2 possible fixes:
- Making the game call level.resetEmptyTime() each time the player’s pearls are added to the world, each time the game is unfrozen and each time an entity is teleported through an end gateway.

- Removing the behavior of dimensions stopping processing of entities and block entities entirely.

### Comment 4: Savvvage_ (2025-06-05T11:57:58.735-0700)

About the first suggested fix from my previous comment:
calling resetEmptyTime() after the game is unfrozen is a bad idea, instead making the game not inrement the emptyTime of the levels while the game is frozen makes more sense.
Calling the resetEmptyTime() after pearl is added to the dimension upon player loggin on and after entities teleport through end gateways still applies.

### Comment 5: John (2025-07-14T17:23:16.055-0700)

+1 am able to reproduce this issue. This bug is negatively impacting player experience.

### Comment 6: John (2025-07-20T06:57:03.227-0700)

Testing should be done to see if the fix for this issue also fixes MC-299770

### Comment 7: John (2025-07-20T07:46:51.288-0700)

Testing should be done to see if the fix for this issue also fixes MC-298184
