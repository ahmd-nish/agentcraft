# MC-112257: Some NBT tags require the correct suffix

**Mojira URL:** [https://bugs.mojang.com/browse/MC-112257](https://bugs.mojang.com/browse/MC-112257)

## Report details

- **Mojira categories:** Commands; Data Packs
- **Project:** MC
- **Issue key:** MC-112257
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2017-01-04T17:18:57.616-0800
- **Updated:** 2025-05-29T09:20:38.490-0700
- **Resolution date:** 2024-07-23T01:18:47.157-0700
- **Affects versions:** Minecraft 1.11.2; Minecraft 17w15a; Minecraft 17w16a; Minecraft 1.12.2; Minecraft 1.13-pre5; 1.15.1; 1.15.2; 20w10a; 1.16.3; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w08b; 1.17 Pre-release 3; 1.17.1; 1.18.1; 1.18.2; 22w19a; 1.19.2; 1.20.1; 1.21
- **Fix versions:** 24w33a
- **Area:** Platform
- **Labels:** NBT
- **Watchers:** 2
- **Attachments:** 2
- **Attachment filenames:** MC-112257.mp4; MC-112257.png
- **Issue links:** Duplicate:inward:MC-227156:"CanPickUpLoot" is inconsistent with other boolean tags | Relates:outward:MC-112253:Primitive NBT Lists that are not of type int need a type suffix | Relates:inward:MC-120371:Data types and formatting are not corrected within items' tag NBT

## Description

NBT CanPickUpLoot requires byte suffix, but most other NBTs don't.
Steps to reproduce
- /summon zombie ~ ~ ~ {CanPickUpLoot:1}

- Throw an item at the zombie

- The zombie will not pickup the item

If you use

```
/summon zombie ~ ~ ~ {CanPickUpLoot:1b}
```
it will work.
Possible fix
Based on the decompiled code of 1.10.2 using forge the issue comes from here:
net.minecraft.entity.EntityLiving.readEntityFromNBT(NBTTagCompound):511

```
/**
     * (abstract) Protected helper method to read subclass entity data from NBT.
     */
    public void readEntityFromNBT(NBTTagCompound compound)
    {
        super.readEntityFromNBT(compound);

        if (compound.hasKey("CanPickUpLoot", 1))
        {
            this.setCanPickUpLoot(compound.getBoolean("CanPickUpLoot"));
        }
```
Instead of compound.hasKey("CanPickUpLoot", 1), it should be compound.hasKey("CanPickUpLoot", 99) to work with all primitive types.
net.minecraft.nbt.NBTTagCompound.hasKey(String, int):215

```
/**
     * Returns whether the given string has been previously stored as a key in this tag compound as a particular type,
     * denoted by a parameter in the form of an ordinal. If the provided ordinal is 99, this method will match tag types
     * representing numbers.
     */
    public boolean hasKey(String key, int type)
    {
        int i = this.getTagId(key);
        return i == type ? true : (type != 99 ? false : i == 1 || i == 2 || i == 3 || i == 4 || i == 5 || i == 6);
    }
```
Here are some other affected nbts:
- color: net.minecraft.item.ItemArmor.getColor(ItemStack):161

- RepairCost: net.minecraft.item.ItemStack.getRepairCost():1001

- ShowParticles: net.minecraft.potion.PotionEffect.readCustomPotionEffectFromNBT(NBTTagCompound):241

- rewardExp: net.minecraft.village.MerchantRecipe.readFromTags(NBTTagCompound):152

## Comments (18)

### Comment 1: migrated (2017-01-04T17:18:57.616-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: migrated (2017-01-06T07:37:17.099-0800)

removed the following:
- trackingPosition: net.minecraft.world.storage.MapData.readFromNBT(NBTTagCompound):69

- DifficultyLocked: net.minecraft.world.storage.WorldInfo.WorldInfo(NBTTagCompound):217

These 2 can't be touched by commands.

### Comment 3: migrated (2017-01-06T07:54:54.641-0800)

@FVbico I think it would be better to change all affected nbt, even those that can not be touched by commands. That has the advantage of beeing consistent and it is better for mods. I actually reported this bug because I am writing a mod.

### Comment 4: migrated (2017-01-06T08:00:32.811-0800)

The thing is, your ticket is about requiring the correct suffix for some tags (none for some int tags) but editing those 2 requires third party software and the use of that is not supported.

### Comment 5: migrated (2017-01-06T08:03:14.656-0800)

Still it would be more consistent in the code and therefor easier for mojang to maintain.

### Comment 6: migrated (2017-01-06T20:38:26.730-0800)

@FBbico. So it's a bug since it's not consistent in the vanilla code, additionally he's showing it in the case for modding that it causes issues. It still causes issues in vanilla with commands as you require the "1b" part unlike most nbt tags with only needs an integer (like "NoGravity:1").

### Comment 7: migrated (2017-01-06T22:04:18.437-0800)

he's showing it in the case for modding that it causes issues. It still causes issues in vanilla with commands as you require the "1b" part unlike most nbt tags with only needs an integer (like "NoGravity:1").
 read my previous comment again.

### Comment 8: Avoma (2021-01-06T07:05:09.806-0800)

Can confirm in 20w51a.

### Comment 9: Avoma (2021-01-25T02:49:21.663-0800)

Can confirm in 21w03a.

### Comment 10: [MOD] Greymagic27 (2021-01-25T02:49:29.199-0800)

I'm still able to reproduce this in 21w03a

### Comment 11: Avoma (2021-02-07T06:08:57.466-0800)

Can confirm in 21w05b.

### Comment 12: Avoma (2021-02-13T11:09:48.098-0800)

Can confirm in 21w06a.

### Comment 13: Avoma (2021-03-05T03:22:00.403-0800)

Can confirm in 1.16.5 and 21w08b.

### Comment 14: Avoma (2021-08-07T10:36:51.534-0700)

Can confirm in 1.17.1.

### Comment 15: FX - PR0CESS (2021-09-26T21:23:31.486-0700)

Armor Color no longer seems to use key 1, it uses 99
Updated Names: (yarn 1.17.1)
ShowParticles + ShowIcon: net.minecraft.entity.effect.StatusEffectInstance.fromNbt()
rewardExp + xp + priceMultiplier: net.minecraft.village.TradeOffer
repairCost did not change at all

### Comment 16: Avoma (2022-02-16T06:32:21.629-0800)

Can confirm in 1.18.1.

### Comment 17: Avoma (2022-05-15T04:23:31.407-0700)

Can confirm in 1.18.2 and 22w19a.

### Comment 18: Avoma (2022-10-22T10:26:29.272-0700)

Can confirm in 1.19.2.
