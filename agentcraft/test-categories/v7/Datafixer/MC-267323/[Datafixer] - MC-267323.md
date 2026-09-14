# MC-267323: Items fields with old boolean JSON formatting are cleared upon world update

**Mojira URL:** [https://bugs.mojang.com/browse/MC-267323](https://bugs.mojang.com/browse/MC-267323)

## Report details

- **Mojira categories:** Datafixer; Items
- **Project:** MC
- **Issue key:** MC-267323
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2023-12-13T18:23:59.470-0800
- **Updated:** 2025-04-26T15:15:10.296-0700
- **Resolution date:** 2024-12-03T08:23:45.861-0800
- **Affects versions:** 1.20.4
- **Fix versions:** 25w02a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 0

## Description

When updating a world from 1.20.2 or below which contains items with fields containing boolean JSON components (e.g. bolded name...) to any version above 1.20.2, said fields are completely cleared instead of updating to the new format. Entities will update, but items will not.
What I expected to happen was...:
The item containing the old JSON format is updated to the new JSON format, such that the name, lore, etc. remain intact upon world update.
What actually happened was...:
The item containing the old JSON format has all subsequent fields that contain the old JSON format completely wiped. (resets to default name/and or deletes all lore)
Steps to Reproduce:
1. Give yourself an item using old JSON formatting in version 1.20.2 or below.
Example:

```
/give @p gold_block{display:{Name:'{"text":"Text","color":"yellow","bold":"true"}',Lore:['{"text":"Text","color":"gold","bold":"true"}']}} 1
```
2. Store the item in the player inventory or in a container
3. Update to 1.20.3, 1.20.4 or future versions.
Notice that upon reloading the world, the item will reset to its default name and its lore will clear upon the item being loaded into the world.

Fixing this bug may be important for those with custom items who wish to update to a newer version, but do not want said items to return to normal.
This can be fixed by updating the old JSON format to the new format upon loading (similar to entities), or adding compatibility such that both old and new JSON boolean format will work (as it may be noted that all maps and datapacks that contain these components, including essentially all realm maps, will become non-functional when updating between versions in the current state).

## Comments (2)

### Comment 1: migrated (2023-12-13T21:40:55.038-0800)

There's no upgrade path for any of those instances. Signs, entities and block entities just modify their save data to the "preferred" format (also changing key order), items never did this for any NBT inside "tag", let alone the name and lore. (MC-120371)
Your concern is valid, but that's a misconception that should've been corrected.
Thisisn't just for the boolean things, but all formattng which became more strict (invalid color name, malformatted click/hover event, etc.)

### Comment 2: Ceresjanin123 (2024-09-06T07:19:48.626-0700)

In 24w36a the item loses it's boldness but otherwise it upgrades fine, keeping it's custom name, color and lore.
The report should be updated accordingly, or closed and a new one made in it's place
