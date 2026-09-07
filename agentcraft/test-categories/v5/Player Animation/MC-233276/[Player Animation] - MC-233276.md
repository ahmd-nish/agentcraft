# MC-233276: You can feed adult donkeys, horses, llamas or mules with maximum Temper value, and hand animation is not played

**Mojira URL:** [https://bugs.mojang.com/browse/MC-233276](https://bugs.mojang.com/browse/MC-233276)

## Report details

- **Mojira categories:** Mob behaviour; Player Animation
- **Project:** MC
- **Issue key:** MC-233276
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2021-07-28T06:16:42.584-0700
- **Updated:** 2025-05-31T02:00:05.269-0700
- **Resolution date:** 2024-11-17T15:16:13.542-0800
- **Affects versions:** 1.17.1; 21w37a; 21w38a; 21w39a; 21w40a; 21w41a; 21w42a; 21w43a; 21w44a; 1.18 Pre-release 1; 1.18 Pre-release 2; 1.18 Pre-release 4; 1.18 Pre-release 5; 1.18 Pre-release 6; 1.18 Pre-release 8; 1.18 Release Candidate 3; 1.18; 1.18.1 Release Candidate 2; 1.18.1; 22w03a; 22w06a; 1.18.2 Pre-release 1; 22w11a; 22w17a; 22w18a; 1.19 Pre-release 1; 1.19; 1.19.1 Pre-release 5; 1.19.2; 22w42a; 22w46a; 23w06a; 1.19.4; 23w18a; 1.20 Release Candidate 1; 1.20; 1.20.1; 1.20.2
- **Fix versions:** 23w41a
- **Labels:** animation; donkey; feeding; hand-animation; horse; llama; mule; sound; temper
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** 2021-09-11 14-49-17.mp4
- **Issue links:** Relates:inward:MC-201599:When the horse, donkey, mule, llama & trader llama no longer needs food, it will not make a neighs or angrily sound | Relates:outward:MC-278375:Feeding wheat or hay bale to llama or trader llama with maximum Temper causes item stack to be desynced | Relates:inward:MC-256738:Breedable entities can be fed again after receiving damage causing them to consume multiple items | Duplicate:inward:MC-262155:Horses infinitely eat golden carrots when creative mode used | Duplicate:inward:MC-265027:Feeding a horse while it is full health and full grown just deletes the food | Duplicate:inward:MC-264659:Llamas, mules, and donkeys can continue to feed even when they become saturated | Duplicate:inward:MC-262312:Can't feed horses and donkeys | Duplicate:inward:MC-262435:Hand Movement is nonexistant when feeding llamas multiple times

## Description

The bug
You can feed adult donkeys, horses or mules with maximum Temper value, and the hand animation is not played.
The distinction of this issue from MC-93825 is that it is NOT a desync, and it is not MC-236341 as it happens only with a high temper value, and all food exhibits this behavior. However, sometimes golden carrots do play animation and sounds on the first time.
To reproduce
- Summon a donkey, horse, llama or mule with a Temper value of 100, e.g.

```
/summon horse ~ ~ ~ {Temper:100}
```

- Give the animal any food.
 Very rarely, animations and sounds will be played one time.
 No animations and sounds are played.

- Notice how the food is actually consumed, i.e. it is not a desync.

Expected result
You should not be able to feed said animal; as per , it should show the hand animation but the animal should not consume the food (this was the behavior in 1.15.2).
Analysis (tentative)
Code analysis by  can be found in this comment.
I think that this is the piece of code that causes the issue, but I might be wrong.
net.minecraft.world.entity.animal.horse.AbstractHorse.java (Mojang mappings, 1.18-pre1)

```
...
protected boolean handleEating(Player $$0, ItemStack $$1) {
        boolean $$2 = false;
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
       ...
```
If the animal's temper is equal or more than its max temper and it is not tamed, $$2 is not set to true, so the game event and animations will not play. At least, this is what I understood.

## Comments (5)

### Comment 1: migrated (2021-07-28T06:16:42.584-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: ampolive (2021-07-28T06:17:29.676-0700)

Relates to MC-187419.

### Comment 3: ampolive (2021-07-28T06:24:24.660-0700)

I don't think this is a duplicate of MC-93825, because the items don't re-appear when the inventory is updated.

### Comment 4: ampolive (2021-09-11T10:45:53.921-0700)

Relates to MC-93825 and MC-236341.

### Comment 5: ampolive (2021-11-15T04:53:26.902-0800)

I think that the actual bug here could be that you are able to feed these animals with high Temper in the first place.
