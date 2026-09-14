# MC-265238: trade_rebalance loot tables have a wrong type

**Mojira URL:** [https://bugs.mojang.com/browse/MC-265238](https://bugs.mojang.com/browse/MC-265238)

## Report details

- **Mojira categories:** Loot tables
- **Project:** MC
- **Issue key:** MC-265238
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2023-09-05T09:21:28.347-0700
- **Updated:** 2025-04-29T12:19:41.918-0700
- **Resolution date:** 2023-09-14T02:09:50.093-0700
- **Affects versions:** 1.20.2 Pre-release 1
- **Fix versions:** 1.20.2 Release Candidate 1
- **Area:** Gameplay
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** image-2023-09-07-12-45-10-035.png; image-2023-09-07-12-45-46-229.png

## Description

Expected
Loot tables for the bundled trade_rebalance packs have the minecraft:chest type.
Actual
Loot tables for the packs have the minecraft:entity type.
Steps to reproduce
- Open the JAR file

- Check any file under /data/minecraft/datapacks/trade_rebalance/data/minecraft/loot_tables/chests/

- The type will be minecraft:entity instead of minecraft:chest

## Comments (4)

### Comment 1: migrated (2023-09-05T09:21:28.347-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: gnembon (2023-09-06T06:06:05.259-0700)

Is correct. Affects chest loot in various structures

### Comment 3: migrated (2023-09-06T06:13:09.176-0700)

How isit correct? it's container loot, not an entity death loot table, it receives different context from triggering. If it affects more, shouldn't they all be fixed, rather than just leaving them to use the improper type?

### Comment 4: Patbox (2023-09-07T03:46:08.658-0700)

After checking for myself, can confirm it's the case for datapack ones
Compared to original loottable
