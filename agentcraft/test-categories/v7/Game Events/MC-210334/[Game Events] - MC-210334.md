# MC-210334: Sculk sensors are not activated upon sheep being dyed

**Mojira URL:** [https://bugs.mojang.com/browse/MC-210334](https://bugs.mojang.com/browse/MC-210334)

## Report details

- **Mojira categories:** Game Events
- **Project:** MC
- **Issue key:** MC-210334
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-01-02T12:43:35.219-0800
- **Updated:** 2025-04-30T05:37:57.229-0700
- **Resolution date:** 2023-02-07T06:18:25.855-0800
- **Affects versions:** 20w51a; 21w03a; 21w08b; 21w10a; 21w14a; 21w15a; 21w17a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17 Release Candidate 1; 1.17; 1.17.1 Pre-release 1; 1.17.1; 21w37a; 21w38a; 21w40a; 1.18 Pre-release 5; 1.18; 1.18.1; 1.18.2; 22w14a; 1.19 Pre-release 1; 1.19 Pre-release 3; 1.19 Pre-release 5; 1.19 Release Candidate 2; 1.19; 1.19.2; 22w45a; 1.19.3
- **Fix versions:** 23w06a
- **Labels:** sculk_sensor; sheep
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-210334.mp4; MC-210334.png
- **Issue links:** Relates:inward:MC-214619:Sculk sensors cannot detect application of ink sacs to signs | Relates:inward:MC-212278:Sculk sensors do not detect signs being dyed | Relates:outward:MC-210484:Sculk sensors are not activated upon a sheep changing from blue to red, through the use of an evoker

## Description

The Bug:
Sculk sensors are not activated upon sheep being dyed.
Steps to Reproduce:
- Place down a sculk sensor and summon a sheep nearby by using the command provided below.

```
/summon minecraft:sheep ~ ~ ~ {NoAI:1b}
```

- Apply any kind of dye to the sheep, and watch the sculk sensor closely as you do this.

- Take note as to whether or not sculk sensors are activated upon sheep being dyed.

Observed Behavior:
Sculk sensors aren't activated.
Expected Behavior:
Sculk sensors would be activated.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.18.2 using MCP-Reborn.
net.minecraft.world.level.item.DyeItem.java

```
public class DyeItem extends Item {
   ...
   public InteractionResult interactLivingEntity(ItemStack $is, Player $p, LivingEntity $le, InteractionHand $ih) {
      if ($le instanceof Sheep) {
         Sheep sheep = (Sheep)$le;
         if (sheep.isAlive() && !sheep.isSheared() && sheep.getColor() != this.dyeColor) {
            sheep.level.playSound($p, sheep, SoundEvents.DYE_USE, SoundSource.PLAYERS, 1.0F, 1.0F);
            if (!$p.level.isClientSide) {
               sheep.setColor(this.dyeColor);
               $is.shrink(1);
            }

            return InteractionResult.sidedSuccess($p.level.isClientSide);
         }
      }

      return InteractionResult.PASS;
   }
   ...
```
If we look at the above class, we can see that sheep being dyed simply isn't registered as a game event as the gameEvent() method is never called, thus not detecting this action as a vibration.
Potential Fix:
Simply calling the gameEvent() method where appropriate within this piece of code should resolve this problem. I feel as if a new game event tag would be expected to be used here as none of the currently existing ones seem to fit this action accordingly.

## Comments (4)

### Comment 1: migrated (2021-01-02T12:43:35.219-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: ampolive (2021-09-22T14:35:04.557-0700)

Can confirm in 21w37a.

### Comment 3: ampolive (2021-10-11T05:40:44.575-0700)

Can confirm in 21w40a.

### Comment 4: muzikbike (2022-05-24T05:47:17.943-0700)

Interestingly, dyeing wolf collars does produce vibrations.
