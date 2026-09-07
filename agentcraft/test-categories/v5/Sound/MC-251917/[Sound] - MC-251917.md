# MC-251917: No gear equipping sound or subtitle when a shield is placed into the offhand slot

**Mojira URL:** [https://bugs.mojang.com/browse/MC-251917](https://bugs.mojang.com/browse/MC-251917)

## Report details

- **Mojira categories:** Sound
- **Project:** MC
- **Issue key:** MC-251917
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2022-05-19T07:16:16.658-0700
- **Updated:** 2025-05-29T09:10:20.380-0700
- **Resolution date:** 2023-02-08T01:55:19.052-0800
- **Affects versions:** 1.19 Pre-release 1; 1.19 Pre-release 2; 1.19; 1.19.2; 1.19.3; 23w04a
- **Fix versions:** 23w06a
- **Watchers:** 2
- **Attachments:** 7
- **Attachment filenames:** 2022-05-19_15.11.40.png; 2022-05-19_15.11.44_2.png; 2022-05-19_15.11.44.png; 2022-05-19_15.11.55.png; 2022-05-19_15.11.58_2.png; 2022-05-19_15.11.58.png; MC-251917.mp4

## Description

The bug
MC-94060 was fixed in the first 1.19 pre-release for most equipable items. However, shields are still completely silent when placed in the offhand slot, whether it be by dispenser, shift-clicking, mainhand/offhand switching or manually moving it to that slot. As the first two of these effectively imply that the shield is "gear" with a designated slot, the lack of a sound/subtitle for this is inconsistent.
How to reproduce
- Obtain an armor piece

- Obtain a shield

- Have dispensers equip both of these to you

Expected results
Both of these would play gear equipping sounds where appropriate.
Actual results
Only the armor piece plays a sound - the shield is completely silent.
Further notes
A unique sound event should be implemented for this as per , as a generic subtitle is undesirable.

## Comments (6)

### Comment 1: migrated (2022-05-19T07:16:16.658-0700)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: syarumi (2022-05-19T09:13:20.612-0700)

Wouldn't this also imply that equipping shields in the offhand would produce vibrations? They'd have to make a special case check only for shields.

### Comment 3: migrated (2022-05-20T15:51:16.536-0700)

@chava
the deep dark biome is supposed to be too hard.
so you need to be prepared "equip your shield" before going to the deep dark.

### Comment 4: Avoma (2022-06-07T08:28:42.149-0700)

Can confirm in 1.19.

### Comment 5: Avoma (2022-08-25T08:56:39.772-0700)

Can confirm in 1.19.2.

### Comment 6: Brain81505 (2023-01-31T06:49:52.433-0800)

Can confirm in 23w04a and 1.19.3
