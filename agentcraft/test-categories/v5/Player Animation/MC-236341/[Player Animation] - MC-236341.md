# MC-236341: You can feed hay bales to adult donkeys, horses or mules, but hand animation and animal eating animation/sounds are not played

**Mojira URL:** [https://bugs.mojang.com/browse/MC-236341](https://bugs.mojang.com/browse/MC-236341)

## Report details

- **Mojira categories:** Mob behaviour; Player Animation; Sound
- **Project:** MC
- **Issue key:** MC-236341
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-09-11T10:43:23.561-0700
- **Updated:** 2025-04-26T13:50:42.834-0700
- **Resolution date:** 2024-11-17T15:16:13.562-0800
- **Affects versions:** 1.17.1; 21w37a; 21w38a; 21w39a; 21w40a; 21w41a; 21w42a; 21w43a; 21w44a; 1.18 Pre-release 1; 1.18 Pre-release 2; 1.18 Pre-release 4; 1.18 Pre-release 5; 1.18 Pre-release 6; 1.18 Pre-release 8; 1.18 Release Candidate 3; 1.18; 1.18.1 Release Candidate 2; 1.18.1; 22w03a; 22w06a; 1.18.2 Pre-release 1; 22w11a; 22w17a; 22w18a; 1.19 Pre-release 1; 1.19; 1.19.1 Pre-release 5; 1.19.2; 22w42a; 22w46a; 23w06a; 1.20 Release Candidate 1; 1.20; 1.20.1; 1.20.2
- **Fix versions:** 23w41a
- **Area:** Platform
- **Labels:** animation; donkey; feeding; hand-animation; hay_bale; horse; mule; sound
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2021-07-28 10-21-35.mp4; image-2023-02-10-18-33-20-449.png
- **Issue links:** Relates:outward:MC-201599:When the horse, donkey, mule, llama & trader llama no longer needs food, it will not make a neighs or angrily sound | Relates:outward:MC-278375:Feeding wheat or hay bale to llama or trader llama with maximum Temper causes item stack to be desynced | Duplicate:inward:MC-264303:Feed horse infinitely

## Description

The bug
You can feed hay bales to adult donkeys, horses or mules, but hand animation and animal eating animation/sounds are not played.
The distinction of this issue from MC-93825 is that it is NOT a desync, and it is not  as it happens regardless of the animal's temper value, and no other food exhibits this behavior, only hay bales. Also unlike , this does not affect llamas.
To reproduce
1. Summon a donkey, horse or mule.
2. Feed the animal hay bales.
3.  The hay bales will be consumed, but no animations or sounds are played.
Expected result
Animations and sounds should be played when you feed hay bales to adult donkeys, horses and mules, or adult donkeys, horses and mules should not consume hay bales to begin with, in line with how they used to behave in the past (see this comment).
Code analysis (tentative)
If adult donkeys, horses and mules should consume the hay bales:
There appears to be a missing line in AbstractHorse.java:
net.minecraft.world.entity.animal.horse.AbstractHorse.java (Mojang mappings, 1.18-pre1)

```
...
protected boolean handleEating(Player $$0, ItemStack $$1) {
        boolean $$2 = false;
        float $$3 = 0.0f;
        int $$4 = 0;
        int $$5 = 0;
        if ($$1.is(Items.WHEAT)) {
            $$3 = 2.0f;
            $$4 = 20;
            $$5 = 3;
        }
        ...
        else if ($$1.is(Blocks.HAY_BLOCK.asItem())) {
            $$3 = 20.0f;
            $$4 = 180;
            /** There should be a $$5 here? */
        }
        ...
        else if ($$1.is(Items.GOLDEN_CARROT)) {
            $$3 = 4.0f;
            $$4 = 60;
            $$5 = 5;
            ...
        }
        ...
        if ($$5 > 0 && ($$2 || !this.isTamed()) && this.getTemper() < this.getMaxTemper()) {
            $$2 = true;
            if (!this.level.isClientSide) {
                this.modifyTemper($$5);
            }
        }
       if ($$2) {
            this.eating();
            this.gameEvent(GameEvent.EAT, this.eyeBlockPosition());
        }
```
The variable $$5 appears to control the Temper and the eating event, and it is missing for the hay bale. Llamas override this method in their own class, which would explain why they are not affected.
If they should not consume the hay bales:
Code analysis by  can be found in this comment.

## Comments (10)

### Comment 1: migrated (2021-09-11T10:43:23.561-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: ampolive (2021-09-11T10:43:48.789-0700)

Closely relates to MC-93825 and .

### Comment 3: ampolive (2021-11-14T10:11:49.478-0800)

And I think the reason llamas are not affected is because they override this method in their own class.

### Comment 4: migrated (2022-05-13T17:29:58.974-0700)

Dupe of

### Comment 5: ampolive (2022-05-14T10:36:06.824-0700)

It's not a duplicate. I stated in the description the reason why they are separate issues. They are marked as related.

### Comment 6: BugCrusherszz (2023-02-10T15:36:41.431-0800)

I looked into this issue more, and it turns out the handleEating method returns correctly (it returns if the feeding action succeeded), so the error is caused by fedFood. See below how the ItemStack always decrements regardless if the feeding action succeeds or not. This affects all llamas, donkeys, mules, and horses, tamed or untamed.
This bug is also the cause of  and .

### Comment 7: ampolive (2023-02-10T16:12:12.002-0800)

I see, but that does not explain why only hay bales are affected in this case. Your analysis explains  and , but I'm quite confident that the root cause of this particular issue is the missing variable in handleEating.

### Comment 8: BugCrusherszz (2023-02-11T13:19:37.797-0800)

On the Minecraft wiki it states that horses, mules, and donkeys cannot accept hay bales if untamed. If this is intended, then $$5 should be excluded from hay bales, meaning that the issue here is that the hay bales were incorrectly consumed, as a result of the analysis I attached.

### Comment 9: ampolive (2023-02-11T13:32:38.662-0800)

The Minecraft wiki is not a source for intended behavior, as it is not considered an official source anymore. However, you could be right that it might be intended. I'll add this to the summary.

### Comment 10: ampolive (2023-10-11T08:38:28.133-0700)

This has been fixed in 23w41a with the fix of .
