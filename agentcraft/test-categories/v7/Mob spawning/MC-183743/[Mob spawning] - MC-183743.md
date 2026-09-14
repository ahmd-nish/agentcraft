# MC-183743: Iron golem overpopulation

**Mojira URL:** [https://bugs.mojang.com/browse/MC-183743](https://bugs.mojang.com/browse/MC-183743)

## Report details

- **Mojira categories:** Mob spawning
- **Project:** MC
- **Issue key:** MC-183743
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2020-05-13T04:57:32.953-0700
- **Updated:** 2025-04-11T12:48:22.526-0700
- **Resolution date:** 2023-04-05T19:32:11.214-0700
- **Affects versions:** 20w19a; 20w20b; 1.16 Pre-release 7; 1.16 Release Candidate 1; 1.16; 1.16.1
- **Fix versions:** 20w27a
- **Labels:** mojang_internal_1
- **Watchers:** 1
- **Attachments:** 11
- **Attachment filenames:** 2020-05-09_10.59.39.png; 2020-05-12_11.17.10.png; 2020-05-13_07.50.04.png; 2020-06-10_14.29.42.png; 2020-06-23_10-37-39_Village Test.zip; 2020-06-23_11.07.02.png; 2020-07-10_22.54.29.png; 2023-04-05_17.47.26.png; 2023-04-05_17.47.28.png; 2023-04-05_17.47.32.png; golems.JPG
- **Issue links:** Duplicate:inward:MC-184201:Villagers spawning too many Iron Golems | Duplicate:inward:MC-191903:Villagers gossip golem spawn | Duplicate:inward:MC-192391:Too many iron Golems spawning | Duplicate:inward:MC-192783:Way too many iron golems in their house | Duplicate:inward:MC-205895:Golem excessive overpopulation | Relates:outward:MC-158542:Iron Golems don't stop spawning | Relates:inward:MC-193217:Villagers don't reset their golem spawning timer when reloaded

## Description

I settled a small village of 7 villagers (1 Farmer, 1 Cleric, 5 Librarians) at my base, and after AFKing for a while in a farm nearby there are loads of golems both inside and outside of the main building (but mostly outside, there's not a whole lot of room for them to spawn inside). I've been culling their population pretty regularly as a source of iron so I didn't think much about their spawn rate, but this made me think that there might be something off.
The area around is well lit and hemmed in by berries and fencing, so I don't think they're spawning from the villagers panicking due to hostile mobs.
E: Forgot to mention that all seven of the villagers have been zombified and subsequently cured. Also, there are five unemployed villagers in a spawning room nearby (the small netherraack building) that also seem to be spawning some of their own golems. The unemployed villagers have not been zombified/cured.

## Comments (23)

### Comment 1: migrated (2020-05-13T04:57:32.953-0700)

This comment contained multiple image attachments (11), please login to view the attachments.

### Comment 2: [Mod] violine1101 (2020-05-13T05:06:42.321-0700)

Are you sure the iron golems spawned in 20w19a and not earlier? This was supposed to be fixed in 20w19a, see MC-158542

### Comment 3: migrated (2020-05-13T05:30:08.204-0700)

Yeah, they spawned as I left the game on overnight. Here's a screengrab from yesterday.

### Comment 4: migrated (2020-05-13T05:34:18.770-0700)

Also a screengrab from the 9th showing I was on 20w19a before.

### Comment 5: migrated (2020-05-29T15:18:59.275-0700)

I can confirm that this is still an issue in my test village I created in a superflat world.  In my case it seams an extra iron golems spawn when the chunk is reloaded.  I can reliably get extra iron golems to spawn by setting the time to 09000 (the time when villagers gather) and then reloading the world.
I created the village in 1.15.2 and tested that iron golems still spawned in 20w19a and 20w22a.
If it will be helpful I can provide a backup of my test world, as there is not much else in the world.  I would prefer to do so privately if possible.

### Comment 6: migrated (2020-06-01T10:44:49.274-0700)

Copying my comment from a duplicate ticket:
Experimenting in an empty flat peaceful world in 20w20b, I confirmed you only require 5 villagers that have slept in order to spawn a golem. They don't need to have worked, and they don't need to have seen a zombie, even though the wiki says they need both of these things to spawn one.

### Comment 7: migrated (2020-06-10T06:23:01.599-0700)

I can confirm this too. It happens on my personal survival world too. It's on the latest 1.16 pre-release 2 version.

### Comment 8: migrated (2020-06-17T07:26:29.313-0700)

Affects 1.16 pre-release-7

### Comment 9: Adrian Östergård (2020-06-18T00:09:27.785-0700)

Please provide a download of a world where you have this issue.

### Comment 10: migrated (2020-06-18T08:46:56.160-0700)

Note: The wiki now describes this new behavior, so maybe this change was intended and is not a bug? If so, I'll simply comment that it's kind of annoying as a large base will slowly fill up with golems if you've got any villagers in it, but at least it'll make iron farms easier
I was able to reproduce in RC-1.
World download: https://gofile.io/d/uASqth
This is just a peaceful, flat world with 5 villagers and beds. Golems begin spawning once they've slept and a new one appears once all the existing ones have wandered away.

### Comment 11: Michael Wobst (2020-06-18T08:51:35.710-0700)

The wiki describes whatever can be seen in in the game. No matter if it's a bug or intentional behavior.

### Comment 12: migrated (2020-06-21T14:02:28.811-0700)

I think there are three separate issues.
The first and what I thought what this bug was about is that Iron golems keep spawning in spite of the fact that they are clearly Iron golems still within 16x13x16 box centered on the block the villager as described in the Wiki.  This seams to happen, at least for me, when the chunk is reloaded.
The second is that they keep spawning because they wonder away, the fact that they wonder away may be a bug, but the fact that they keep spawning because of it is consistent with the Wiki.
The third is that Golems now spawn even though they don't have Job sites.  I believe this is now the intended behavior as release 20w19a has this note in the changelog: "Villagers can now spawn iron golems regardless of their profession status or latest working time".

### Comment 13: migrated (2020-06-23T08:13:05.388-0700)

Here is a cleaned up backup of my world:
  It is a villager trading hall I was experimenting with in creative mode.  There are two golem buried underground, which according to the Wiki should prevent any new ones from spawning as there always is a golem within 16x13x16 box of a villager.  It doesn't work.
To reproduce the problem enter the structure and wait for the villagers to gather (use "/set time 09000") then reload the world.  A new golem will spawn.  Do this enough times and structure will soon be overflowing with golems.

### Comment 14: migrated (2020-06-25T14:59:45.543-0700)

Thanks, that was a very useful test world. Think I found and fixed the bug, stay tuned.

### Comment 15: migrated (2020-06-29T17:24:22.254-0700)

Kevin Atkinson, what you are talking about is the same thing that is happening to me

### Comment 16: migrated (2020-07-11T10:30:59.490-0700)

Let me back you up with my own issue on a server world, there is definitely a 3-1 golem/villager ratio in my village which is walled off and meticulously lit. And this is about 4 in game days after I culled and only left about 8 of them. Ive scoured for a solution but cant find any.

### Comment 17: migrated (2020-08-24T17:49:55.371-0700)

Still not fixed:

https://www.reddit.com/r/Minecraft/comments/ig16p0/so_many_golems_spawn_now_its_crazy/

### Comment 18: migrated (2020-08-25T01:46:50.281-0700)

I'm in agreement, in our village @ spawn, the bug is definitely not fixed, however our server is "upgraded", so not a "new map", but still, I can't just reset a live server   - everyone will lose their progress.

I have found it's possible that unloaded chunks - that have now been loaded with villages in them - don't overpopulate the golems... indicating that the problem might be fixed on 'new maps' ---- but again, I can't be expected to reset my server? There must be a way to patch loaded chunks — this is not a "block state" issue, it's a 'villager-logic' issue ?

Please consider patches to existing chunks — or share patches we can apply manually to existing chunks  – this is a painful bug

### Comment 19: migrated (2020-08-25T01:46:59.139-0700)

Can you please attach the world where this happens?

### Comment 20: migrated (2020-08-28T02:16:35.938-0700)

Alright, as it turns out I may have been wrong .... it appears to affect new chunks also... My understanding is only 1 iron golem should spawn per village ? I cannot find any reference (includeing gamepedia ?) indicating the number allowed to spawn per village - regardless of "panic" or not. But I have more than one in the new loaded chunks, so I believe this problem is not fixed even for new chunks in an old map.

Affects 1.16.2

### Comment 21: migrated (2020-08-30T06:27:42.253-0700)

Java edition: 1.16.2
Hi Thommy Siverman,
That isn't necessary, it happens in any game-mode that generate villages, in any seed that has villages generating, in any village.
the longer you stay around the village, the more will spawn.

### Comment 22: migrated (2020-08-31T00:44:51.321-0700)

We've been plagued with this bug on our Realms server for a while. We had over 80 villagers in one village and the number of golems got that high as well, so I had to regularly purge them. After updating to 1.16.2, I did my last purge so far and the number of golems has been stable at 32 since then (with a villager count of 91). This is the only village that is pretty much permanently loaded (next to my base, used to be in spawn chunks before I moved spawn). I didn't check the other villages, but at least in the next village that is at least sometimes loaded, there doesn't seem to be a crazy amount of golems spawning anymore either.
So for me this bug seems to be fixed and it doesn't happen in all villages anymore. Providing the (or a) world where this still happens could thus be helpful...
(In case it matters: world was created in 1.13.2 and subsequently updated to 1.14, 1.14.4, 1.15.2 and 1.16.2, skipping the in-between versions.)

### Comment 23: migrated (2023-04-05T19:32:11.214-0700)

This is still an issue on 1.19.4
