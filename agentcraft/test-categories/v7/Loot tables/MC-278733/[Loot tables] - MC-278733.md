# MC-278733: Breaking a double resin brick slab block only returns a single slab

**Mojira URL:** [https://bugs.mojang.com/browse/MC-278733](https://bugs.mojang.com/browse/MC-278733)

## Report details

- **Mojira categories:** Items; Loot tables
- **Project:** MC
- **Issue key:** MC-278733
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-12-06T12:27:18.622-0800
- **Updated:** 2025-04-26T17:41:44.938-0700
- **Resolution date:** 2024-12-11T02:13:23.486-0800
- **Affects versions:** 1.21.4
- **Fix versions:** 25w02a
- **Area:** Expansion A
- **Watchers:** 1
- **Attachments:** 0

## Description

What I expected to happen was...:
When breaking a double resin slab block with any level of pickaxe 2 slab items should have appeared
What actually happened was...:
When breaking the double slab block only one slab item appeared
Steps to Reproduce:
- Place down two resin slabs on top of one another to make a full block

- Using any level of pick, break the block and only one appears instead of 2

Code analysis (official mappings)
In the VanillaBlockLoot#generate method:

```
this.dropSelf(Blocks.RESIN_BRICK_SLAB);
```
 instead of

```
this.add(Blocks.RESIN_BRICK_SLAB, $$1x -> this.createSlabItemTable($$1x));
```
Code analysis (Yarn mappings)
In the VanillaBlockLootTableGenerator#generate method:

```
this.addDrop(Blocks.RESIN_BRICK_SLAB);
```
instead of

```
this.addDrop(Blocks.RESIN_BRICK_SLAB, block -> this.slabDrops(block));
```

## Comments (1)

### Comment 1: haykam (2024-12-06T12:38:43.373-0800)

Code analysis (Yarn mappings)
In the VanillaBlockLootTableGenerator#generate method:

```this.addDrop(Blocks.RESIN_BRICK_SLAB);```
instead of

```this.addDrop(Blocks.RESIN_BRICK_SLAB, block -> this.slabDrops(block));```
