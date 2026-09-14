# MC-249664: Warden despawns when far away

**Mojira URL:** [https://bugs.mojang.com/browse/MC-249664](https://bugs.mojang.com/browse/MC-249664)

## Report details

- **Mojira categories:** Mob behaviour
- **Project:** MC
- **Issue key:** MC-249664
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2022-03-28T12:37:01.031-0700
- **Updated:** 2025-04-30T08:08:15.835-0700
- **Resolution date:** 2022-05-23T01:39:23.187-0700
- **Affects versions:** 22w12a; 22w13a; 22w14a; 22w15a; 22w16a; 22w17a; 22w18a
- **Fix versions:** 22w15a; 22w19a
- **Labels:** warden
- **Watchers:** 1
- **Attachments:** 5
- **Attachment filenames:** Minecraft 22w12a Warden Despawning.mp4; Minecraft 22w15a - Multiplayer Warden Despawning.mp4; Minecraft 22w18a - Singleplayer 2022-05-06 09-11-57_Trim.mp4; Minecraft 22w18a Warden Despawns.mp4; screenshot-1.png

## Description

This might be intentional as many mobs follow this rule, but it seems odd for the Warden.

The bug:
If the Warden is far away, the Warden has a chance to just despawn, even if you keep distracting it from a distance. The Warden is not digging down to despawn and it is instead just disappearing.
Steps to reproduce:
- Summon a warden

- /tp @s ~-130 ~ ~ -90 0

- /tp @s ~130 ~ ~ -90 0 (Or you can just fly back to where the warden was summoned)

Observed results:
The warden has despawned immediately because the warden is over 128 blocks away.
It can also despawn randomly if it is in between 32 blocks and 128 blocks away as seen in the picture above.
Expected results:
The Warden should only despawn when digging into the ground.

## Comments (16)

### Comment 1: migrated (2022-03-28T12:37:01.031-0700)

This comment contained multiple image attachments (5), please login to view the attachments.

### Comment 2: slicedlime (2022-04-06T16:33:04.681-0700)

Behavior is still exactly the same as described.

### Comment 3: muzikbike (2022-04-13T10:09:19.319-0700)

Still seems to be the case even in 22w15a - I can anger a warden, have it chase me for a few minutes as I sprint away, and it has a chance to despawn without a trace even during pursuit.

### Comment 4: Eometheous (2022-04-14T14:23:25.565-0700)

Can confirm in 22w15a. This bug is still happening exactly as described. Here is a new video I have displaying the issue in 22w15a

### Comment 5: Avoma (2022-04-15T01:27:46.999-0700)

I can also confirm that this issue is still present in 22w15a.

### Comment 6: migrated (2022-04-28T16:34:07.978-0700)

This may not be a bug, but I find it odd that the warden despawns like that (since I consider it a [unofficial] boss, and bosses don't despawn, unlike regular mobs). As you said, it should only despawn when it digs in (and it won't dig in if there is noise). Removing the distance-dependent despawn also would not hurt the game, as the warden will despawn naturally anyway.

In conclusion, this definitely needs to be fixed (or changed, depending on whether or not you think it is a bug). Also yeah, confirmed in 22w17a.

### Comment 7: migrated (2022-04-29T02:52:11.650-0700)

Maybe Mojang should make it so the warden doesn't despawn like pop, but so it automatically digs underground when it would normally despawn?
It's just a suggestion I don't expect Mojang to take me seriously

### Comment 8: Erik Broes (2022-05-06T00:24:07.257-0700)

That is in fact that happens.
Can someone provide some steps to reproduce this behavior if it is still happening?

### Comment 9: Eometheous (2022-05-06T09:07:16.446-0700)

@[Mojang] Grum (Erik Broes). These are the steps to reproduce:
- Summon a warden

- /tp @s ~-130 ~ ~ -90 0

- /tp @s ~130 ~ ~ -90 0 (Or you can just fly back to where the warden was summoned)

Here is a video showing these steps

Observed Results:
The warden has despawned immediately because the warden is over 128 blocks away.
It can also despawn randomly if it is in between 32 blocks and 128 blocks away as seen in the picture above.
Expected Results:
The Warden should only despawn when digging into the ground.

### Comment 10: Eometheous (2022-05-06T09:16:24.588-0700)

Here is this behavior happening when I am just 48 blocks away.
- Summon a warden

- /tp @s ~-48 ~ ~ -90 0

- Wait some time (it's random so it can take some time, I found that setting the time to night made if faster since more mobs were spawning)

Observed Results:
The warden despawned
Expected Results:
The Warden should only despawn when digging into the ground.

### Comment 11: syarumi (2022-05-06T09:39:09.588-0700)

From my testing, wardens summoned with spawn eggs or /summon don't have PersistanceRequired, which is why they despawn. However, wardens summoned from sculk shriekers do have the tag, so they don't despawn until they dig down.

### Comment 12: migrated (2022-05-07T14:15:58.003-0700)

No I think they still despawn even if they are spawned by a shrieker. How to reproduce:
1.) Spawn a shrieker high up in the air with the tag can_summon set to true. By high I mean very high, prefferably max height.
2.) Make a drop all the way down to a low height like bedrock level. Place a dripstone on the bottom to see if it despawned by seeing if there is a sculk catalyst or not.
3.) Activate the shrieker until the warden spawns and somehow make it drop into the hole; then wait on the platform for a few seconds.
4.) If it didn't despawn on the way down there should be a catalyst at the bottom, but there isn't.
5.) Next do the same thing you did the last time, but follow the warden down. You will see it die (assuming you made the drop long enough) and drop a catalyst.

### Comment 13: Erik Broes (2022-05-09T02:47:51.992-0700)

Awesome thank you so much for the repro-cases, I'll dig (no pun intended) into this and see what is going on!

### Comment 14: Erik Broes (2022-05-10T01:48:36.780-0700)

: I am unable to reproduce what you said, the warden survived a fall from max-height perfectly fine.
: I found that too, from now on the flag is set always unless you pass in NBT manually (then you become responsible)

### Comment 15: migrated (2022-05-14T22:53:21.965-0700)

Weird, I did the thing successfully; did you make the drop long enough / Is the dripstone on the bedrock at the bottom of the world?

But oh well it says fixed so it's ok

### Comment 16: Erik Broes (2022-05-23T01:39:23.187-0700)

I ended up putting a breakpoint in the 'hurt' method of the warden, if it would take fall-damage it wouldn't have despawned and then dropped it from max-height (no custom world) in a normal flatworld. So I think the fall was ~384-6 blocks total.
