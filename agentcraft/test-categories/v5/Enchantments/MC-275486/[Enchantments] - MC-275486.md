# MC-275486: Enchantable data component doesn't work with items that only have enchantments through a data pack

**Mojira URL:** [https://bugs.mojang.com/browse/MC-275486](https://bugs.mojang.com/browse/MC-275486)

## Report details

- **Mojira categories:** Data Packs; Enchantments
- **Project:** MC
- **Issue key:** MC-275486
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2024-08-16T21:30:19.540-0700
- **Updated:** 2025-04-26T16:15:42.072-0700
- **Resolution date:** 2024-08-20T01:01:35.940-0700
- **Affects versions:** 24w33a
- **Fix versions:** 24w34a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 9
- **Attachment filenames:** 2024-08-16_23.05.15.png; 2024-08-16_23.05.37.png; 2024-08-16_23.05.44.png; 2024-08-16_23.05.49.png; 2024-08-16_23.18.12.png; 2024-08-17_07.39.27.png; 2024-08-17_07.39.31.png; Enchantable test 24w33a.zip; Items compatible with enchantable.png
- **Issue links:** Relates:outward:MC-275436:Cannot enchant books in enchanting table

## Description

I'm not sure if this is a bug, or just an incomplete feature, but I feel it is important to make the team aware of this, just in case.
The backstory: I wanted to make custom enchantments for wolf armor show up in the enchanting table, but when giving myself enchantable wolf armor, nothing shows up. The data component works for all non-enchantable items in vanilla that can be enchanted with books in survival.
Steps to recreate:
- Add the attached datapack (

- ) to your world to add the archive:wolf_armor and archive:air_brake enchantments to wolf armor and elytra, respectively. They are defined by wolf_armor.json and air_brake.json

- run command

```
/give @p minecraft:elytra[enchantable={value:1}]
```

- run command

```
/give @p minecraft:wolf_armor[enchantable={value:1}]
```

- attempt to enchant both items in an enchanting table

Observed result:
Elytra can be enchanted with both vanilla and custom enchantments. No enchantments show up for the wolf armor, despite it being added to several enchantable item tags and having a functional custom enchant.
Expected result:
The expected outcome is that enchantments show up for both items, since the changelog states: "If present, and applicable enchantments are available, items with the component can be enchanted in an enchanting table."

## Comments (5)

### Comment 1: migrated (2024-08-16T21:30:19.540-0700)

This comment contained multiple image attachments (9), please login to view the attachments.

### Comment 2: cakeyeater99 (2024-08-16T21:37:37.212-0700)

I don't know why, but the correct command won't save in the report. it keeps forcing a \ after the = sign

### Comment 3: BugTracker_ (2024-08-16T21:40:25.755-0700)

Can confirm:
Elytra:
Wolf armor:
Correct commands:

```/give @p minecraft:elytra[enchantable={value:1}]```

```/give @p minecraft:wolf_armor[enchantable={value:1}]```

### Comment 4: NeunEinser (2024-08-17T02:05:24.141-0700)

Adding a space after the { fixed the \ in your description.
Can reproduce, and pack looks like it should work, I cannot think of anything that's missing. Elytra is configured the same by the, and works, even if you remove the additional air breaking enchantment.

### Comment 5: cakeyeater99 (2024-08-17T03:42:44.335-0700)

The reason I added the wolf armor to several enchantable tags was to try and give it more "available" enchantments using the base enchantments, but that didn't work.
I included the elytra enchantment to show that custom enchantments do make it into the enchanting table once the UI shows up, but that the UI doesn't show up unless the item can be enchanted (in an anvil) in the vanilla game.
If I had to guess, the check for wether "applicable enchantments are available" somehow only checks vanilla information. I wanted to change the files for the versions .jar file, and see if adding wolf_armor to enchantable/armor.json would work, but as expected, I can't open the game if I mess with the game files like that.
