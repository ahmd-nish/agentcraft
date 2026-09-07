# MC-248272: Enchantment::doPostHurt and Enchantment::doPostAttack are called twice for players

**Mojira URL:** [https://bugs.mojang.com/browse/MC-248272](https://bugs.mojang.com/browse/MC-248272)

## Report details

- **Mojira categories:** Enchantments
- **Project:** MC
- **Issue key:** MC-248272
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-01-26T04:44:07.603-0800
- **Updated:** 2025-05-29T09:09:50.769-0700
- **Resolution date:** 2024-08-07T18:41:52.813-0700
- **Affects versions:** 1.18.1; 22w03a; 22w05a; 1.18.2; 1.19.2; 1.19.4 Pre-release 3; 1.20.1; 1.20.2
- **Fix versions:** 24w18a
- **Area:** Platform
- **Watchers:** 2
- **Attachments:** 1
- **Attachment filenames:** MC-248272.png
- **Issue links:** Duplicate:inward:MC-275013:Enchantment onTargetDamaged gets called twice for main hand items

## Description

The Enchantment::doPostHurt and Enchantment::doPostAttack functions are called twice for the player causing some bugs.
- The Bane of Arthropods enchantment gives the Slowness effect twice

- The Thorns enchantment deals damage to the attacker and the durability of the item with this enchantment twice.

The problem is that the EnchantmentHelper::doPostHurtEffects and EnchantmentHelper::doPostDamageEffects actually call these functions twice:
Vanilla code 1.18.1-1.20.1

```
public static void doPostHurtEffects(LivingEntity defender, Entity attacker) {
    EnchantmentVisitor consumer = (enchantment, lvl) -> enchantment.doPostHurt(defender, attacker, lvl);

    if (defender != null) {
        EnchantmentHelper.runIterationOnInventory(consumer, defender.getAllSlots());
    }
    if (attacker instanceof Player) {
        EnchantmentHelper.runIterationOnItem(consumer, defender.getMainHandItem());
    }
}
```

```
public static void doPostDamageEffects(LivingEntity attacker, Entity target) {
    EnchantmentVisitor consumer = (enchantment, lvl) -> enchantment.doPostAttack(attacker, target, lvl);

    if (attacker != null) {
        EnchantmentHelper.runIterationOnInventory(consumer, attacker.getAllSlots());
    }
    if (attacker instanceof Player) {
        EnchantmentHelper.runIterationOnItem(consumer, attacker.getMainHandItem());
    }
}
```
Fix suggestion

```
public static void doPostHurtEffects(LivingEntity defender, Entity attacker) {
    EnchantmentVisitor consumer = (enchantment, lvl) -> enchantment.doPostHurt(defender, attacker, lvl);

    if (defender != null) {
        EnchantmentHelper.runIterationOnInventory(consumer, defender.getAllSlots());
    } else if (attacker instanceof Player) {
        EnchantmentHelper.runIterationOnItem(consumer, defender.getMainHandItem());
    }
}
```

```
public static void doPostDamageEffects(LivingEntity attacker, Entity target) {
    EnchantmentVisitor consumer = (enchantment, lvl) -> enchantment.doPostAttack(attacker, target, lvl);

    if (attacker != null) {
        EnchantmentHelper.runIterationOnInventory(consumer, attacker.getAllSlots());
    } else if (attacker instanceof Player) {
        EnchantmentHelper.runIterationOnItem(consumer, attacker.getMainHandItem());
    }
}
```

## Comments (4)

### Comment 1: migrated (2022-01-26T04:44:07.603-0800)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: Arisa Bot (2022-01-26T04:44:18.746-0800)

Please do not mark Unreleased Versions as affected. You don't have access to them yet.
-- I am a bot. This action was performed automatically! If you think it was incorrect, please notify us on Discord or Reddit

### Comment 3: pulpetti (2022-01-27T07:04:09.318-0800)

In 22w03a

### Comment 4: Avoma (2022-03-05T11:41:51.504-0800)

Can confirm in 1.18.2.
