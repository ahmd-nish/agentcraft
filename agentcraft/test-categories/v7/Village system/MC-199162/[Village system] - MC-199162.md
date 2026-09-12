# MC-199162: One farmland block in plains_large_farm_1 has moisture level 0

**Mojira URL:** [https://bugs.mojang.com/browse/MC-199162](https://bugs.mojang.com/browse/MC-199162)

## Report details

- **Mojira categories:** Structures; Village system
- **Project:** MC
- **Issue key:** MC-199162
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2020-08-28T12:28:58.430-0700
- **Updated:** 2025-04-10T14:56:48.332-0700
- **Resolution date:** 2022-09-13T00:14:02.057-0700
- **Affects versions:** 1.16.2; 1.16.3 Release Candidate 1; 1.19; 1.19.1 Pre-release 5; 1.19.2
- **Fix versions:** 22w42a
- **Labels:** village
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** 2020-08-28_15.22.13.png
- **Issue links:** Relates:inward:MC-248331:The "minecraft:woodland_mansion/1x2_a2" structure generates with one dehydrated farmland block

## Description

In the structure minecraft:village/plains/houses/plains_large_farm_1, one of the farmland blocks has its moisture value set to 0. This is inconsistent with all other farmland blocks in the farm, which have moisture level 7.
How to reproduce

```
/place template minecraft:village/plains/houses/plains_large_farm_1
```

## Comments (5)

### Comment 1: migrated (2020-08-28T12:28:58.430-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: anthony cicinelli (2020-08-28T14:10:10.504-0700)

Can confirm for 1.16.2

### Comment 3: Avoma (2022-02-09T04:48:47.505-0800)

Hi, due to the recent triaging of  and how it was considered to be a valid problem, (judging by the assigned "Mojang Priority"), would it be okay to request a review of this ticket? Of course, this is an extremely minor problem and one that most players won't even notice, however, it is a small inconsistency, which I feel should be reconsidered per .

### Comment 4: Avoma (2022-07-10T05:38:46.217-0700)

Can confirm in 1.19. This can now be more easily reproduced by using the "/place" command.

```/place template minecraft:village/plains/houses/plains_large_farm_1```

### Comment 5: Avoma (2022-08-30T03:29:20.435-0700)

Can confirm in 1.19.2.
