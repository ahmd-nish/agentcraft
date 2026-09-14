# MC-270871: Upgrading a world with horses wearing leather horse armor makes the horse immune to freezing forever

**Mojira URL:** [https://bugs.mojang.com/browse/MC-270871](https://bugs.mojang.com/browse/MC-270871)

## Report details

- **Mojira categories:** Datafixer
- **Project:** MC
- **Issue key:** MC-270871
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-04-17T11:13:45.582-0700
- **Updated:** 2025-04-11T10:14:33.058-0700
- **Resolution date:** 2024-04-18T03:02:37.158-0700
- **Affects versions:** 1.20.5 Pre-Release 4
- **Fix versions:** 1.20.5 Release Candidate 1
- **Area:** Expansion A
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** image-2024-04-17-21-04-45-510.png; MC-270871.zip
- **Issue links:** Relates:outward:MC-270767:Leather horse armor no longer prevents horses from freezing in powder snow

## Description

Summary:
Relates to MC-270767. In 24w05a the way that horse armor is stored on horses was changed to use body_armor_item instead of ArmorItems[2]. However when upgrading a world, the horse armor is not removed from ArmorItems[2] but it is added to body_armor_item as expected. This causes duplicated horse armor storage. This means that the horse will behave as if it is still wearing the horse armor even when you remove it, causing enchantments to be applied when they shouldn't and allowing you to not experience , , . While the issue for enchantments doesn't affect survival gameplay, this issue causes the horse to still be immune to freezing even if it is no longer wearing leather horse armor.
Steps to reproduce:
You can use the world download
 to skip to step 5.
- Start version 1.20.4.

- Tame a horse.

- Saddle it and equip it with leather horse armor.

- Upgrade the world to the latest version.

- Unequip the leather horse armor from the horse.

- Ride the horse into powder snow.

-

```
/execute on vehicle run data get entity @s
```

Observed results:
The horse won't freeze in the powder snow even though it is no longer wearing the leather horse armor.
Expected results:
The horse should freeze, since it is not wearing leather horse armor anymore
Note: Fixing this by removing the ArmorItems array from horses entirely wouldn't be a good idea, since that will break things made by map makers. All mobs seem to have an ArmorItems array. The best way to fix this is probably by removing items from ArmorItems[2] on horses when upgrading the world to prevent duplicated horse armor storage.
Screenshots:

## Comments (1)

### Comment 1: migrated (2024-04-17T11:13:45.582-0700)

This comment contained multiple image attachments (2), please login to view the attachments.
