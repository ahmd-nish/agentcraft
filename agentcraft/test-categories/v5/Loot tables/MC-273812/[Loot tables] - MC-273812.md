# MC-273812: Intersection chests in trial chambers not generating correctly

**Mojira URL:** [https://bugs.mojang.com/browse/MC-273812](https://bugs.mojang.com/browse/MC-273812)

## Report details

- **Mojira categories:** Loot tables; Structures
- **Project:** MC
- **Issue key:** MC-273812
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2024-06-24T02:13:46.667-0700
- **Updated:** 2025-05-29T09:05:16.468-0700
- **Resolution date:** 2024-10-17T05:10:13.327-0700
- **Affects versions:** 1.21; 24w33a; 24w34a; 24w37a
- **Fix versions:** 1.21.2 Release Candidate 1
- **Area:** Expansion B
- **Votes:** 5
- **Watchers:** 2
- **Attachments:** 3
- **Attachment filenames:** intersectionchest.jpg; intersectionchest1.jpg; loot_command.jpg
- **Issue links:** Duplicate:inward:MC-273841:chest with cake always has same items

## Description

Moderator Note by [~zTxrbq]
If you are coming from Mogswamp, please refrain from commenting here and asking Mojang to fix this. Comments are meant to provide new information, not as a petition forum for content creators. Comments like "please fix this" are spam; all comments containing feedback, complaints, change requests, no new info, and the like will be removed. Repeated violations may result in consequences to your bug tracker account.
Intersection loot chests in trial chambers only spawn with iron blocks, diamond, and cake instead of from the intended loot table. When running the /loot command it generates correctly, but not in the structures (see attached images).
Steps to Reproduce:
- Generate the "corridor/end_1" trial chambers structure by using the command provided below.

```
/place template minecraft:trial_chambers/corridor/end_1
```

- Open the chest below the stairs and observe how an iron block, a cake, and a diamond always generates.

## Comments (14)

### Comment 1: migrated (2024-06-24T02:13:46.667-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: Viradex (2024-06-24T02:16:43.806-0700)

I can confirm. Visiting five Trial Chambers with the intersection all gave me the same loot in the same place.

### Comment 3: [Mod] ManosSef (2024-06-24T02:52:23.680-0700)

I assume that the cause of this issue is the block data of the chest inside the structure file containing the LootTableSeed tag.

### Comment 4: Invisible826 (2024-06-24T03:37:54.310-0700)

, the loot table appears to be entirely unused. To reproduce, run /place template minecraft:trial_chambers/corridor/end_2 and try to open the chest in spectator mode.

### Comment 5: [Mod] ManosSef (2024-06-24T03:51:41.325-0700)

Oh, I didn't know that. But then again my comment was just a bold assumption, I hadn't tested anything.

### Comment 6: migrated (2024-06-30T15:22:38.989-0700)

While this is a bug, i feel like there should still be a chance that the loot table generates this way. Maybe like a 10%, because i feel like it is a "intended" generation. (What are the chances that the chest happened to be exactly like that)

### Comment 7: migrated (2024-06-30T16:50:04.245-0700)

I think the intersection chests are intentionally set like that, because if not how do you explain the exact same thing happening on bedrock, and it looks intentional too, the items are all lined up and simetrical

### Comment 8: Viradex (2024-06-30T21:13:29.969-0700)

This is probably not intentional, as an unused loot table does exist for the intersection chest, which is accessible only through the /loot command. It's unlikely Mojang would add a loot table and then proceed to intentionally not use it.

### Comment 9: migrated (2024-07-01T02:49:11.588-0700)

@Viradex they probably forgot to delete it. Otherwise, they would have had to have the exact same bug on bedrock and get the exact same loot, because they can't just copy the structure from one game to the other as they're two completely different builds on different languages. The only way I can see it happen is if that exact loot generates from the seed 0 and there was the same issue in both games, which is very unlikely.

### Comment 10: migrated (2024-07-06T02:00:22.625-0700)

@psbpsbp I agree with @Viradex, why would they add the loot table if the chest was meant to always be like that? if you were going to say "oh, they probably had the idea later on" I find it very unlikely that a concept or idea would suddenly get completely changed.

### Comment 11: Chief_entity (2024-07-11T03:40:57.560-0700)

Apparently, this bug also happen in minecraft Bedrock Edition. When im researching if this bug happen in Bedrock edition, im go to 21 different trial chambers 11 of them have this intersection. And all 11 of them have the same loot, a iron block, a cake, and a diamond.
Sorry if my english are broken

### Comment 12: ZaCloud (2024-07-18T21:51:37.820-0700)

Could a developer building the structure have accidentally opened a chest, thus locking in the contents? And maybe both Java & Bedrock use the same structure file (or it was faithfully duplicated), thus why both versions have this characteristic?

### Comment 13: dovisutu (2024-08-16T01:29:47.142-0700)

Confirmed for 24w33a. Tested with corridor/end_2 sturcture.

### Comment 14: Chilenderino (2024-09-15T12:28:05.373-0700)

Can confirm 24w37a with command:

```/place template minecraft:trial_chambers/corridor/end_2```
And:

```/loot give @s loot minecraft:chests/trial_chambers/intersection```
