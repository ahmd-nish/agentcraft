# MC-240513: Pandas do not spawn in bamboo jungles with Default world

**Mojira URL:** [https://bugs.mojang.com/browse/MC-240513](https://bugs.mojang.com/browse/MC-240513)

## Report details

- **Mojira categories:** Mob spawning
- **Project:** MC
- **Issue key:** MC-240513
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-11-03T13:09:13.550-0700
- **Updated:** 2025-04-29T21:02:05.022-0700
- **Resolution date:** 2021-11-24T17:29:10.146-0800
- **Affects versions:** 21w44a; 1.18 Pre-release 1; 1.18 Pre-release 5
- **Fix versions:** 1.18 Pre-release 6
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** 2021-11-03_13.46.16.png; 2021-11-05_11.17.56.png; 2021-11-23_11.31.25.png; 2021-11-23_11.38.27.png; image-2021-11-09-09-41-30-741.png; image-2021-11-09-09-42-12-039.png
- **Issue links:** Duplicate:inward:MC-241276:Pandas spawns rate are extremely low in the 1.18 first pre-release | Duplicate:inward:MC-241985:Pandas no longer spawn naturally | Relates:outward:MC-236756:Biome-exclusive mob spawn rates are reduced

## Description

The bug
Eventhough marked as resolved, this bug isn't. Pandas don't spawn in 1.18 snapshots. Hope anyone can proof me wrong or that it's clientside; remarks in resolved bugreport get ignored it seems.
I wonder, it looks a lot like the issue with foxes and wolves: MC-238062
Steps to reproduce
- Create a Default world

- Use the following command to find the bamboo jungle:

```
/locatebiome minecraft:bamboo_jungle
```

- Teleport to the bamboo jungle

- Use the following command to apply the effect to nearby pandas:

```
/effect give @e[type=panda] glowing 1000
```

- Every jungle biome (not matter what the seed) no pandas, no entity was found

## Comments (13)

### Comment 1: migrated (2021-11-03T13:09:13.550-0700)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: anthony cicinelli (2021-11-03T13:47:07.491-0700)

I could not reproduce in 21w44a see the attached screenshot.

### Comment 3: Mr_Quasi (2021-11-03T13:50:52.444-0700)

Can you give me the seed of that world, start to think it's something clientside then.

### Comment 4: [Mod] bemoty (2021-11-05T03:18:58.729-0700)

Can confirm, I think. I generated a single biome jungle world and wasn't able to find any pandas at all. It seems like they do spawn in bamboo jungles however.

### Comment 5: anthony cicinelli (2021-11-08T08:18:32.399-0800)

This is intended. "Pandas spawn natuarlly in the new bamboo forest biome" no mention that they should spawn in Jungles from the 18w43a changelog

### Comment 6: migrated (2021-11-09T00:42:15.343-0800)

Panda trying hard to hide in the jungle.

### Comment 7: Mr_Quasi (2021-11-09T01:50:44.350-0800)

So now pandas are more rare than a blue axelotl? No matter what seed and/or command I use to locate them, I can't find pandas nor do they spawn during my countless atemps to adventure through the bamboo jungles...  As I mentioned earlier, is this something clientside by now?

### Comment 8: Mr_Quasi (2021-11-11T09:25:44.367-0800)

Confirmed for 1.18 pre-release 1

### Comment 9: ampolive (2021-11-12T09:18:00.283-0800)

According to MC-241276, pandas do spawn, but they're incredibly rare. This makes me think that this issue is a specific case of MC-236756.

### Comment 10: Mr_Quasi (2021-11-12T09:31:26.020-0800)

Can't be intentional, i've spend hours in serveral seeds and didn't find a single panda. Think the example screenshots where from a single biome world?
Before they also spawned in groups and/or alone.

### Comment 11: Mr_Quasi (2021-11-20T02:50:37.367-0800)

It's resolved, not sure who added the pre release 5.

### Comment 12: [Mod]Les3awe (2021-11-22T19:41:11.054-0800)

This issue has been fixed in 1.18-pre6.

### Comment 13: migrated (2021-11-24T17:29:10.146-0800)

tysm lol pandas are my favorite mob <3
