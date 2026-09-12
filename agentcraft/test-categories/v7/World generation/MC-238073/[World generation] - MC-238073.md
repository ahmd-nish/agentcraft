# MC-238073: Decorators are independent of world seed

**Mojira URL:** [https://bugs.mojang.com/browse/MC-238073](https://bugs.mojang.com/browse/MC-238073)

## Report details

- **Mojira categories:** World generation
- **Project:** MC
- **Issue key:** MC-238073
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2021-09-30T20:24:07.779-0700
- **Updated:** 2025-04-29T20:23:37.642-0700
- **Resolution date:** 2022-01-12T03:14:35.147-0800
- **Affects versions:** 21w10a; 1.17.1; 21w37a; 21w38a; 21w39a; 21w40a; 21w41a; 21w42a
- **Fix versions:** 21w43a
- **Labels:** world-generation
- **Watchers:** 1
- **Attachments:** 22
- **Attachment filenames:** 2021-03-12_12.21.08.png; 2021-03-12_12.21.49.png; 2021-10-01_21.57.29.png; 2021-10-01_22.03.07.png; 2021-10-01_22.17.28.png; 2021-10-01_22.21.49.png; 2021-10-01_22.29.40.png; 2021-10-01_22.32.58.png; 2021-10-02_11.46.37.png; 2021-10-02_11.47.53.png; 2021-10-02_11.48.43.png; 2021-10-02_11.49.41.png; 2021-10-05_10.03.27.png; 2021-10-05_10.04.43.png; 2021-10-07_17.05.56.png; 2021-10-07_17.07.05.png; 2021-10-13_18.53.22.png; 2021-10-13_18.56.56.png; 2021-10-23_19.02.45.png; 2021-10-23_19.14.41.png; 2021-10-27_12.16.37.png; 2021-10-27_12.17.19.png
- **Issue links:** Relates:inward:MC-240271:Dripstone Cave decorators are different each time ignoring world seed | Relates:inward:MC-219200:Lush Cave decorator is different each time ignoring the world seed

## Description

Description:
Decorators are inconsistent in worlds with the same seed
Steps to Reproduce:
1. Generate a world and copy its seed.
2. Make a new world with the same seed
3. Repeat as many times as you like
Expected Behavior:
Each world seed should generate with the same features down to the decorators
Observed Behavior:
Each instance of a seed has a different placement of decorators
World Seed: -8718622960759467126
Notes:
Possible link to

## Comments (22)

### Comment 1: migrated (2021-09-30T20:24:07.779-0700)

This comment contained multiple image attachments (22), please login to view the attachments.

### Comment 2: syarumi (2021-10-01T23:37:39.026-0700)

Can confirm, seems to be happening basically everywhere, even dripstone caves.

### Comment 3: ampolive (2021-10-02T04:59:35.151-0700)

Relates to .

### Comment 4: ampolive (2021-10-02T11:31:45.806-0700)

Actually this is a duplicate of .

### Comment 5: Brent101 (2021-10-02T11:53:41.812-0700)

I wouldn't say so, as  deals with chunk generation and block data. That issue is quite rare and difficult to reproduce but appears smaller in scale, whereas this issue and  deal with all decorators and is relatively easy to mass-produce.  does, however, lead to similar instances but on a smaller scale, usually one or two chunks. But if compounded could lead to a more significant difference within decorator or possibly terrain generation.

### Comment 6: Ceresjanin123 (2021-10-03T03:42:39.509-0700)

This is not a duplicate of  that bug occurs in rare cases and only affects a small area. The developers have probably made some change to the world generation that unintentionally made the surface builders use random seeds, this means this bug affects every seeds and every chunk.
I will see when this started happening

### Comment 7: Ceresjanin123 (2021-10-03T04:52:22.658-0700)

After doing some experiments I have gathered this information: The bug  was actually introduced in 20w49a (the same snapshot the first underground biome was added, dripstone caves) but I only noticed and reported it in 21w10a when lush caves were added. So  doesn't affect just lush caves but dripstone ones too altough for some reason it appears to be much more noticable for lush caves compared to dirpstone caves as those keep some parts of the cave unchanged.
But  bug did not occur above ground from the first 1.17 snapshot up untill the first 1.18 experimental snapshot ,the first snapshot 3d biomes were introduced (I also tested 1.17.1 with C&C preview), meaning the random surface builders are probably caused by 3D Biomes added in 1.18 Exp Snapshot 1.
My theory is that  and  are caused by different bugs since 219200 is a problem with underground biomes in general and 238073 is (probably) caused by 3D Biomes

### Comment 8: Moesh (2021-10-05T00:14:50.855-0700)

Dupe of

### Comment 9: migrated (2021-10-05T00:18:31.833-0700)

Not meaning any disrespect, but are you sure? They used to be consistent in older versions; and 55596 is more a rare event rather than being there every single time.

### Comment 10: ampolive (2021-10-05T15:35:23.385-0700)

This involves the entirety of decorators in all chunks, but  only says "some chunks". I think this is distinct enough for it to be not considered a duplicate.

### Comment 11: Ceresjanin123 (2021-10-06T06:11:52.983-0700)

Good thing this bug report was reopened

### Comment 12: Ceresjanin123 (2021-10-07T08:09:30.895-0700)

Can confirm in 21w40a

### Comment 13: Ceresjanin123 (2021-10-13T09:57:51.215-0700)

Can confirm in 21w41a

### Comment 14: migrated (2021-10-16T21:36:47.447-0700)

The reason this happens appears to be that the second parameter to "WorldgenRandom.setFeatureSeed()" is not consistent. I observed this while reversing the setFeatureSeed() parameters, from a feature that generated in-game. Each time I regenerated a world with the same seed, and reversed the second parameter using the same feature, the second parameter would be different. The first (seed) and third (GenerationStep) parameters are consistent. Due to the way the seeding is done, this often results in the first "WorldgenRandom.nextFloat()" when using "LegacyRandomSource" as the underlying PRNG (or just "WorldgenRandom.nextFloat()" in earlier versions), having a similar value, so the chance decorator will have a similar outcome, but the rest of the feature will be completely different.

### Comment 15: Ceresjanin123 (2021-10-17T04:40:07.613-0700)

Also this first appeared in Exp 1.18 snapshot 1 but affected only lush caves since 21w10a

### Comment 16: ampolive (2021-10-20T13:05:10.494-0700)

Can confirm in 21w42a.

### Comment 17: Ceresjanin123 (2021-10-23T03:23:33.627-0700)

MC-239247 is a duplicate but I encourage the devs to give it a read as it contains some usefull information even though most of it is already in the comment above by MrSpike

### Comment 18: Brent101 (2021-10-27T10:24:30.961-0700)

Seems to be somewhat fixed with less discrepancy as a whole but still major inconsistencies.

### Comment 19: syarumi (2021-10-27T11:29:23.647-0700)

check if what you're experiencing is not .

### Comment 20: Brent101 (2021-10-27T12:29:45.037-0700)

It appears that this issue is solved. The discrepancies noted appear to be .

### Comment 21: Ceresjanin123 (2021-10-27T12:41:12.986-0700)

I don't think so the discrepancies now are much more severe than before this bug was introduced

### Comment 22: ampolive (2021-11-01T10:05:44.258-0700)

and  lead me to believe that this bug wasn't fully fixed.
