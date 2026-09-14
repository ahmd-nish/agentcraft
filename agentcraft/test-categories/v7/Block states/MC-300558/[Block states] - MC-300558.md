# MC-300558: Copper golems can open locked chests without an appropriate key item

**Mojira URL:** [https://bugs.mojang.com/browse/MC-300558](https://bugs.mojang.com/browse/MC-300558)

## Report details

- **Mojira categories:** Block states; Commands; Entities
- **Project:** MC
- **Issue key:** MC-300558
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2025-08-02T07:13:17.599-0700
- **Updated:** 2025-08-29T05:16:31.859-0700
- **Resolution date:** 2025-08-29T05:16:31.799-0700
- **Affects versions:** 25w31a; 25w32a; 25w34b
- **Fix versions:** 25w36a
- **Area:** Expansion A
- **Votes:** 1
- **Watchers:** 2
- **Attachments:** 2
- **Attachment filenames:** CopperGolemLockDemo.mkv; CopperGolemLockDemo-Downscaled.mkv
- **Issue links:** Duplicate:inward:MC-300781:Copper Golems can open locked chests

## Description

If you set the lock block data of a chest to an item predicate, the chest should only be openable while holding a matching item.  However, copper golems can open the chest whether or not the item theyʼre holding matches the predicate.
This could be argued to be intended behavior (if the lock only applies to players), but it seems more consistent to have it apply to all entities that open chests.  It doesnʼt apply to hoppers, but hoppers arenʼt entities and cannot have items held in their hands.
Steps to Reproduce
- Create a copper golem with a copper chest, and put a wooden chest nearby.

- Set the chestʼs lock NBT value to a predicate, for example {items: "minecraft:trial_key"}

- (Optional) Verify lock mechanics for players: you can open the chest if and only if you have an item in your main hand that matches the predicate (in this example, a trial key).

- Put an item that does not match the predicate in the copper chest created in step 1

- Wait for the copper golem to attempt to put the item into the locked chest

Expected Result
The golem cannot open the chest, or possibly never even attempts to use it
Actual result
The golem opens the chest despite not having a matching key item.

## Comments (3)

### Comment 1: [MCQA] Zgajak (2025-08-04T01:46:52.829-0700)

Hi!
Could you please record and upload a video of this issue?
Also, just a reminder, to make your bug report as effective as possible, please try and include the following steps to reproduce the problem:
Steps to Reproduce:
-

-

-

Observed Results:
(Briefly describe what happens)
Expected Results:
(Briefly describe what should happen)
If your ticket does not look like the example given here, then it's likely to be closed as incomplete.
This ticket will automatically reopen when you reply.
Quick Links:
📓 Issue Guidelines – 💬 Mojang Support – 📧 Suggestions – 📖 Minecraft Wiki

### Comment 2: DHouck (2025-08-05T12:37:31.299-0700)

Iʼm sorry; I should have used that or a similar format already.  Iʼve updated the bug report.  (Your example issue link is broken, and the closest I could find is https://help.minecraft.net/hc/en-us/articles/4408887473421-Mojang-Bug-Tracker-Guidelines which does not have an example.  I tried to make it match the example you gave in your response instead.)
I think Iʼve attached the video demonstration to this reply.  Iʼm sorry for the video size; I didnʼt mean to record in so high quality but donʼt know how to easily downscale it.  Iʼm also sorry about the audio quality, but at least itʼs understandable.  My first attempt wasnʼt because there was far too much background noise.

### Comment 3: DHouck (2025-08-05T12:58:12.717-0700)

Downscaled video, and also re-encoded in a format that the website can play instead of needing to download it.
