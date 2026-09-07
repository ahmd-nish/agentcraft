# MC-197241: Players can change the color of a wolf's collar even if they're not its owner

**Mojira URL:** [https://bugs.mojang.com/browse/MC-197241](https://bugs.mojang.com/browse/MC-197241)

## Report details

- **Mojira categories:** Items; Mob behaviour
- **Project:** MC
- **Issue key:** MC-197241
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2020-08-06T09:45:34.491-0700
- **Updated:** 2025-04-30T05:07:41.348-0700
- **Resolution date:** 2023-03-22T01:30:12.376-0700
- **Affects versions:** 1.16.1; 1.16.3; 1.16.4; 20w46a; 20w48a; 20w51a; 21w06a; 21w08a; 21w08b; 21w11a; 1.17; 1.17.1; 21w41a; 1.18.1; 1.18.2; 22w19a; 1.19; 1.19.2; 1.19.3; 1.19.4
- **Fix versions:** 23w12a
- **Area:** Gameplay
- **Labels:** wolf
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** MC-197241.mp4; MC-197241 - Current Code.png; MC-197241 - Fixed Code.png
- **Issue links:** Relates:inward:MC-220469:You cannot use items while looking at wolves owned by other players

## Description

The Bug:
Players can change the color of a wolf's collar even if they're not its owner.
It's important to note that this concept is exclusive to wolves and cannot be seen with cats. This issue isn't present with cats because the isOwnedBy() method is called appropriately with this entity, therefore preventing other players from being able to interact with them.
Steps to Reproduce:
- Obtain any color dye and summon a wolf that is not your owner by using the command provided below.

```
/summon minecraft:wolf ~ ~ ~ {Owner:"Notch"}
```

- Attempt to change the color of the wolf's collar by using the dye.

- Take note as to whether or not players can change the color of a wolf's collar even if they're not its owner.

Observed Behavior:
Players can change the color of a wolf's collar even if they're not its owner.
Expected Behavior:
Players would not be able to change the color of a wolf's collar if they're not its owner.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.19.2 using MCP-Reborn.
net.minecraft.world.entity.animal.Wolf.java

```
public class Wolf extends TamableAnimal implements NeutralMob {
   ...
   public InteractionResult mobInteract(Player player, InteractionHand interactionHand) {
      ItemStack itemstack = player.getItemInHand(interactionHand);
      Item item = itemstack.getItem();
      if (this.level.isClientSide) {
         ...
      } else {
         if (this.isTame()) {
            ...
            DyeColor dyecolor = ((DyeItem)item).getDyeColor();
            if (dyecolor != this.getCollarColor() && this.isOwnedBy(player)) {
               this.setCollarColor(dyecolor);
               if (!player.getAbilities().instabuild) {
                  itemstack.shrink(1);
               }
               return InteractionResult.SUCCESS;
            }
            ...
```
If we look at the above class, we can see that there are two checks that are carried out before allowing the color of a wolf's collar to be changed. One of these checks is to see if the wolf is tamed and the other is to see if the player is holding a dye that's not already the same color as the wolf's collar at the time of the interaction. If these two requirements are met, the color of the wolf's collar can be changed. The game doesn't check if the player carrying out the interaction is the wolf's owner before allowing the color of its collar to be changed, therefore resulting in this problem occurring.
Fix:
Simply altering the appropriate existing "if" statement within this piece of code to check if the player carrying out the interaction is the wolf's owner before allowing the color of its collar to be changed will resolve this problem.
Current "if" statement:

```
if (dyecolor != this.getCollarColor())
```
Fixed "if" statement:

```
if (dyecolor != this.getCollarColor() && this.isOwnedBy(player))
```

## Comments (14)

### Comment 1: migrated (2020-08-06T09:45:34.491-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: anthony cicinelli (2020-08-06T09:51:35.054-0700)

I think the bug here is about tamed wolfs not the cats. Since you are not allowed to interact with with other peoples pets. Can you change the description of the report to reflect this.

### Comment 3: ItsTinay (2020-08-06T23:10:20.988-0700)

Done

### Comment 4: migrated (2020-10-01T09:35:28.219-0700)

Can confirm. You don’t even need to play multiplayer to test this. Just use this command:

```/summon wolf ~ ~ ~ {Owner:[I;123,123,123,123]}```
(If the dog is actually yours, which is very, very, very unlikey, just change one of the numbers in the command.)

### Comment 5: Avoma (2021-01-15T06:59:37.416-0800)

Can confirm in 20w51a.

### Comment 6: Avoma (2021-02-14T03:46:53.344-0800)

Can confirm in 21w06a.

### Comment 7: Avoma (2021-02-28T09:18:24.320-0800)

Can confirm in 21w08b. Video attached.

### Comment 8: Avoma (2021-03-24T08:12:55.268-0700)

Can confirm in 21w11a.

### Comment 9: Avoma (2021-06-20T11:21:04.171-0700)

Can confirm in 1.17.

### Comment 10: Avoma (2021-07-20T10:02:46.753-0700)

Can confirm in 1.17.1.

### Comment 11: Avoma (2021-10-16T04:22:21.302-0700)

I am able to confirm this in 21w41a. The expected behavior would be that only the owner of the dog would be able to change the collar color.

### Comment 12: Avoma (2022-02-18T03:31:21.305-0800)

I can confirm this in 1.18.1 and 22w07a.
It's important to note that this concept is exclusive to wolves and cannot be seen with cats. This issue isn't present with cats because the isOwnedBy() method is called appropriately, therefore preventing other players from being able to interact with them.
Here's a code analysis along with a potential fix regarding this issue.
Code Analysis:
The following is based on a decompiled version of Minecraft 1.18.1 using MCP-Reborn.
net.minecraft.world.entity.animal.Wolf.java

```public class Wolf extends TamableAnimal implements NeutralMob {
   ...
   public InteractionResult mobInteract(Player $p, InteractionHand $ih) {
      ItemStack itemstack = $p.getItemInHand($ih);
      Item item = itemstack.getItem();
      if (this.level.isClientSide) {
         ...
      } else {
         if (this.isTame()) {
            ...
            DyeColor dyecolor = ((DyeItem)item).getDyeColor();
            if (dyecolor != this.getCollarColor()) {
               this.setCollarColor(dyecolor);
               if (!$p.getAbilities().instabuild) {
                  itemstack.shrink(1);
               }

               return InteractionResult.SUCCESS;
            }
         ...```
If we look at the above class, we can see that only two checks are carried out before the game allows the color of a wolf's collar to be changed. These two checks are as follows:
- The wolf must be tamed.

- The player must interact with the wolf whilst holding a dye that's not already the color of their collar.

If these two requirements are met, the setCollarColor() method is called, which changes the color of the wolf's collar. Since the game doesn't check whether or not the player interacting with the wolf is its owner, this results in all players being allowed to change the color of a tamed wolf's collar.
Potential Fix:
Simply altering the appropriate "if" statement or adding a new one altogether to check the call the isOwnedBy() method before allowing players to change the color of a wolf's collar, should resolve this problem. The following line of code could be used in order to fix this:

```if (this.isOwnedBy($p))```

### Comment 13: Avoma (2022-05-14T10:44:16.997-0700)

Can confirm in 1.18.2 and 22w19a. You can use the following command in order to more easily reproduce this issue.

```/summon minecraft:wolf ~ ~ ~ {Owner:"Notch"}```

### Comment 14: Avoma (2022-10-15T11:10:04.774-0700)

Following on from my code analysis, I've double-checked my proposed fix and I can confidently confirm that it's fully functioning and works as expected, so I've attached two screenshots to this report, one of which shows the current code and the other that shows the fixed code. I feel this information may be quite insightful hence my reasoning for providing it.
