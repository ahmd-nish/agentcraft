# MC-271109: Trader llama inventory shifted, partially lost during upgrade

**Mojira URL:** [https://bugs.mojang.com/browse/MC-271109](https://bugs.mojang.com/browse/MC-271109)

## Report details

- **Mojira categories:** Datafixer; Save Data
- **Project:** MC
- **Issue key:** MC-271109
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2024-04-24T11:13:58.727-0700
- **Updated:** 2025-03-25T13:31:26.974-0700
- **Resolution date:** 2024-04-26T02:24:43.046-0700
- **Affects versions:** 1.20.5
- **Fix versions:** 1.20.6 Release Candidate 1
- **Area:** Expansion A
- **Votes:** 1
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 2024-04-24_23-54-57_MC-271109.zip; image-2024-04-24-23-39-10-540.png; image-2024-04-24-23-40-13-974.png

## Description

Summary:
Upgrading a world from 1.20.4 to 1.20.5, inventories of trader llamas are shifted, with items lost which end up in invalid slots. Any item in the carpet slot is also discarded. This does not affect regular llamas, only trader llamas.
Steps to reproduce:
You can go straight to step 5 using this world:
.
You can use the command to summon the trader llama to skip steps 2-4.

```
/summon trader_llama ~ ~ ~ {Tame:1b,ChestedHorse:1b,Items:[{Slot:2b,id:"minecraft:egg",Count:1b},{Slot:3b,id:"minecraft:fern",Count:1b},{Slot:4b,id:"minecraft:dirt",Count:1b}]}
```
- Create a world in 1.20.4.

- Summon trader llama.

- Tame the trader llama.

- Equip the chest on it.

- Upgrade to 1.20.5.

- Look at the trader llama's inventory.

Observed results:
Items from the two lower slots disappeared, and from the third they moved to the lowest one.
Expected results:
All items will be saved.
Screenshots:
1.20.4
1.20.5

## Comments (3)

### Comment 1: migrated (2024-04-24T11:13:58.727-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: migrated (2024-04-24T16:51:32.239-0700)

Can confirm this happens.
Tried from 1.20.4, put 3 items in and upgraded to 1.20.5 and only one item at the bottom remained.

### Comment 3: Misode (2024-04-25T05:49:56.715-0700)

It also appears like the DecorItem of trader llamas is lost and not upgraded to body_armor_item
