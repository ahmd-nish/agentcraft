# MC-244739: Goat eating sounds aren't played when feeding them the last item of wheat within a stack

**Mojira URL:** [https://bugs.mojang.com/browse/MC-244739](https://bugs.mojang.com/browse/MC-244739)

## Report details

- **Mojira categories:** Items; Mob behaviour; Sound
- **Project:** MC
- **Issue key:** MC-244739
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2021-12-05T06:23:46.095-0800
- **Updated:** 2025-04-26T14:08:13.200-0700
- **Resolution date:** 2024-12-10T05:45:09.926-0800
- **Affects versions:** 1.18; 1.18.1; 22w03a; 22w05a; 22w06a; 1.18.2 Pre-release 1; 1.18.2; 22w15a; 22w17a; 22w18a; 1.19; 1.19.1; 1.19.2; 1.19.3; 23w07a; 1.19.4; 1.20.1; 1.20.2; 1.21
- **Fix versions:** 24w33a
- **Area:** Gameplay
- **Labels:** goat
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-244739.mp4; MC-244739.png
- **Issue links:** Relates:inward:MC-260219:Sniffer eating sounds aren't played when feeding them the last item of torchflower seeds within a stack

## Description

The Bug:
Goat eating sounds aren't played when feeding them the last item of wheat within a stack.
Steps to Reproduce:
- Obtain two pieces of what and ensure that they occupy the same hotbar slot.

- Summon two goats and switch into survival mode.

- Feed one of the goats a piece of wheat and take note of how goat eating sounds are played.

- Feed the other goat the remaining piece of wheat and listen closely as you do this.

- Take note as to whether or not goat eating sounds are played when feeding them the last item of wheat within a stack.

Observed Behavior:
Goat eating sounds aren't played.
Expected Behavior:
Goat eating sounds would be played.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.20.1 using MCP-Reborn.
net.minecraft.world.entity.animal.Goat.java

```
public class Goat extends Animal {
   ...
   public InteractionResult mobInteract(Player player, InteractionHand interactionHand) {
      ItemStack itemstack = player.getItemInHand(interactionHand);
      if (itemstack.is(Items.BUCKET) && !this.isBaby()) {
         player.playSound(this.getMilkingSound(), 1.0F, 1.0F);
         ItemStack itemstack1 = ItemUtils.createFilledResult(itemstack, player, Items.MILK_BUCKET.getDefaultInstance());
         player.setItemInHand(interactionHand, itemstack1);
         return InteractionResult.sidedSuccess(this.level().isClientSide);
      } else {
         InteractionResult interactionresult = super.mobInteract(player, interactionHand);
         if (interactionresult.consumesAction() && this.isFood(itemstack)) {
            this.level().playSound((Player)null, this, this.getEatingSound(itemstack), SoundSource.NEUTRAL, 1.0F, Mth.randomBetween(this.level().random, 0.8F, 1.2F));
         }
         return interactionresult;
      }
   }
   ...
```
In the Goat.java class there is the Goat#mobInteract method. We see two important methods; super#mobInteract which is a method of a superclass called Animal. This method handles the decrementing of the held itemstack's amount.
The problem with the line after Goat#mobInteract is that we check if the itemstack is food via the method this#isFood, but since the player has one of that itemstack, the method removes that last amount, and then checks if the itemstack is food. Then it would return false as the itemstack is now AIR. Therefore the eating sound doesn't emit globally.
Fix:
To fix this, we can temporarily store a variable called flag which saves the itemstack's value of being food or not in a true or false matter. Then we can handle the mob interaction using super#mobInteract and then use the stored variable, flag, in our "if" statement.
Current "else" statement:

```
} else {
   InteractionResult interactionresult = super.mobInteract(player, interactionHand);
   if (interactionresult.consumesAction() && this.isFood(itemstack)) {
      this.level().playSound((Player)null, this, this.getEatingSound(itemstack), SoundSource.NEUTRAL, 1.0F, Mth.randomBetween(this.level().random, 0.8F, 1.2F));
   }
   return interactionresult;
}
```
Fixed "else" statement:

```
} else {
   boolean flag = this.isFood(itemstack);
   InteractionResult interactionresult = super.mobInteract(p_149379_, p_149380_);
   if (interactionresult.consumesAction() && flag) {
      this.level().playSound((Player)null, this, this.getEatingSound(itemstack), SoundSource.NEUTRAL, 1.0F, Mth.randomBetween(this.level().random, 0.8F, 1.2F));
   }
   return interactionresult;
}
```

## Comments (4)

### Comment 1: migrated (2021-12-05T06:23:46.095-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: Avoma (2023-02-16T04:11:22.866-0800)

Relates to MC-260219.

### Comment 3: Viradex (2024-09-29T03:34:02.482-0700)

Cannot reproduce in 24w39a.

### Comment 4: Avoma (2024-12-10T05:44:53.966-0800)

This issue was present in 1.21.1 but no longer occurs in 24w33a. This issue has been fixed in 24w33a.
