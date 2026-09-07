# MC-299782: Zombie villagers saved in jigsaw structures forget their biome variant and profession upon world generation

**Mojira URL:** [https://bugs.mojang.com/browse/MC-299782](https://bugs.mojang.com/browse/MC-299782)

## Report details

- **Mojira categories:** Save Data; World generation
- **Project:** MC
- **Issue key:** MC-299782
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2025-07-16T05:36:41.605-0700
- **Updated:** 2025-07-29T08:38:58.616-0700
- **Resolution date:** 2025-07-28T01:54:18.872-0700
- **Affects versions:** 1.21.7; 1.21.8 Release Candidate 1; 1.21.8
- **Fix versions:** 25w31a
- **Area:** Platform
- **Votes:** 4
- **Watchers:** 1
- **Attachments:** 5
- **Attachment filenames:** 2025-07-16_08.27.28.png; 2025-07-16_08.28.51.png; 2025-07-16_08.29.05.png; 2025-07-16_08.29.15.png; zombie_villager_bug_showcase.zip
- **Issue links:** Relates:inward:MC-298071:All naturally spawned zombie villagers are professionless since 25w16a

## Description

Previously, Zombie villagers with a specific profession and biome variant that were saved to a structure jigsaw piece would retain this data upon generated in a world. However, as of 1.21.6 onward (only discovered in 1.21.7), these details are not saved, resulting in the zombie villager generating with a random profession and biome variant. This bug also seems to occur with the /place structure command but not as /place template.
Steps to Reproduce:
- Download the attached datapack. It contains a structure that simply contains a zombie librarian villager that’s jungle variant and level 2.

- Generate into a world with the datapack and note the many zombie villagers across the surface. Note their professions and biome variant.

- Generate one with the /place structure command and observe the zombie villager produced from it. Example command: /place structure zombievillagertest:librarian

- Generate one with the /place template command and observe the zombie villager produced from it. Example command: /place template zombievillagertest:librarian

- Place a structure block down and load in the structure “zombievillagertest:librarian”. Observe the profession and biome variant.

Expected Result:
- All the zombie villagers generated will be librarian, jungle, and level 2.

Actual Result:
- The zombie villagers generated with the /place template command and via loading from a structure block are the only ones to maintain their profession and variant. Every other method resulted in random professions and biome relevant to the biome it generated in. It will however maintain the level of the villager consistently with all methods listed.

## Comments (2)

### Comment 1: miziragamez (2025-07-16T05:36:42.825-0700)

This comment contained an image attachment, please login to view the attachment.

This comment contained an image attachment, please login to view the attachment.

This comment contained an image attachment, please login to view the attachment.

This comment contained an image attachment, please login to view the attachment.

This comment contained an image attachment, please login to view the attachment.

### Comment 2: clamlol (2025-07-24T18:32:58.612-0700)

Can confirm, this is very likely caused by an imperfection in the fix for .
