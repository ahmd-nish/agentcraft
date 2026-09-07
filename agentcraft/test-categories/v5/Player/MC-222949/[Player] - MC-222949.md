# MC-222949: You can use tridents enchanted with Riptide while riding entities

**Mojira URL:** [https://bugs.mojang.com/browse/MC-222949](https://bugs.mojang.com/browse/MC-222949)

## Report details

- **Mojira categories:** Player
- **Project:** MC
- **Issue key:** MC-222949
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2021-04-11T06:12:30.905-0700
- **Updated:** 2026-03-24T12:12:05.132-0700
- **Resolution date:** 2026-02-23T02:58:23.697-0800
- **Affects versions:** 1.16.5; 21w14a; 21w15a; 21w16a; 21w17a; 21w18a; 21w19a; 21w20a; 1.17 Pre-release 4; 1.17 Pre-release 5; 1.17 Release Candidate 1; 1.17; 1.17.1 Pre-release 1; 1.17.1 Pre-release 2; 1.17.1 Pre-release 3; 1.17.1 Release Candidate 1; 1.17.1; 21w37a; 1.18.1; 22w05a; 22w06a; 1.18.2; 1.19; 1.19.1; 1.19.2; 22w43a; 1.19.3; 1.19.4; 1.20.1; 24w20a; 1.21; 1.21.3; 1.21.4; 1.21.7; 25w41a; 1.21.11
- **Fix versions:** 26.1 Snapshot 10
- **Area:** Expansion A
- **Labels:** riptide; trident
- **Votes:** 2
- **Watchers:** 2
- **Attachments:** 5
- **Attachment filenames:** MC-222949.mp4; MC-222949.png; MC-222949 - Current Code.png; MC-222949 - Fixed Code.png; Minecraft Riptide Trident bug with Nautilus.mp4
- **Issue links:** Duplicate:inward:MC-230308:Trident Bug | Duplicate:inward:MC-302964:Using a riptide trident while on a nautilus damages the nautilus | Duplicate:inward:MC-303046:When riding a nautilus, the Riptide trident deals damage. | Duplicate:inward:MC-304677:The player can damage their own mount with Riptide | Duplicate:inward:MC-304816:The Trident with the Riptide enchantment used by riding a Nautilus hurts it and propulse a little bit ourself even we are mouting | Duplicate:inward:MC-306981:Tamed nautilus takes damage from a trident with the Riptide enchantment while being ridden

## Description

The Bug:
You can use tridents enchanted with riptide while riding entities and in some cases, this can damage the entity you're riding.
Steps to Reproduce:
- Set the weather to "rain" and give yourself a trident enchanted with riptide by using the command provided below.

```
/give @s minecraft:trident[minecraft:enchantments={"minecraft:riptide":3}]
```

- Ride any entity and attempt to throw the riptide trident.

- Take note as to whether or not you can use tridents enchanted with riptide while riding entities.

Observed Behavior:
You can use riptide tridents.
Expected Behavior:
You would not be able to use riptide tridents.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.19.2 using MCP-Reborn.
net.minecraft.world.item.TridentItem.java

```
public class TridentItem extends Item implements Vanishable {
   ...
   public InteractionResultHolder<ItemStack> use(Level level, Player player, InteractionHand interactionHand) {
      ItemStack itemstack = player.getItemInHand(interactionHand);
      if (itemstack.getDamageValue() >= itemstack.getMaxDamage() - 1) {
         return InteractionResultHolder.fail(itemstack);
      } else if (EnchantmentHelper.getRiptide(itemstack) > 0 && !player.isInWaterOrRain()) {
         return InteractionResultHolder.fail(itemstack);
      } else {
         player.startUsingItem(interactionHand);
         return InteractionResultHolder.consume(itemstack);
      }
   }
   ...
```
If we look at the above class, we can see that there are two checks that are carried out before allowing the player to use a trident enchanted with riptide. One of these is to check if the player is actually holding a trident enchanted with riptide and the other is to check if they are in water or rain. The game doesn't check if the player is currently riding an entity before allowing them to throw a trident enchanted with riptide in the rain, therefore resulting in this problem occurring.
Fix:
Simply altering the appropriate existing "if" statement within this piece of code to check if the player is a passenger before allowing them to throw a trident enchanted with riptide in the rain, will resolve this problem. We can achieve this through the use of the isPassenger() boolean.
Current "if" statement:

```
else if (EnchantmentHelper.getRiptide(itemstack) > 0 && !player.isInWaterOrRain())
```
Fixed "if" statement:

```
else if (EnchantmentHelper.getRiptide(itemstack) > 0 && !player.isInWaterOrRain() || player.isPassenger())
```

## Comments (8)

### Comment 1: migrated (2021-04-11T06:12:30.905-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: migrated (2021-04-11T06:53:54.342-0700)

Can confirm

### Comment 3: migrated (2021-04-12T07:16:29.512-0700)

On bedrock edition this is fixed by making riptide not work at all when riding an entity. You are able to charge, when you let go of right click, it will not work.

### Comment 4: Avoma (2022-02-09T10:59:01.559-0800)

This ticket closely relates to MC-248106.

### Comment 5: Avoma (2022-10-08T06:01:18.400-0700)

Following on from my code analysis, I've double-checked my proposed fix and I can confidently confirm that it's fully functioning and works as expected, so I've attached two screenshots to this report, one of which shows the current code and the other that shows the fixed code. I feel this information may be quite insightful hence my reasoning for providing it.

### Comment 6: Loupieur (2025-12-06T03:15:19.429-0800)

Can confirm in 1.21.11-rc2, and it will hurt the entity that we are riding

### Comment 7: TheMightyTorch (2026-03-01T17:13:16.772-0800)

tested for Happy Ghast and Hrose in version 1.21.11 (release)
The action damages the mount when using a riptide trident.

### Comment 8: Jamie (2026-03-24T12:12:05.132-0700)

Fixed, but for future reference if the bug crops up again, it affected a zombie nautilus as well. Accidentally killed a coral zombie nautilus doing this.
