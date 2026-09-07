# MC-229209: Loot table function set_count doesn't work with unstackable items anymore

**Mojira URL:** [https://bugs.mojang.com/browse/MC-229209](https://bugs.mojang.com/browse/MC-229209)

## Report details

- **Mojira categories:** Loot tables
- **Project:** MC
- **Issue key:** MC-229209
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2021-06-15T21:56:50.034-0700
- **Updated:** 2025-04-29T09:51:59.936-0700
- **Resolution date:** 2024-04-21T10:37:21.492-0700
- **Affects versions:** 1.17; 1.17.1; 1.19.3; 1.20.2
- **Fix versions:** 1.20.5 Pre-Release 1
- **Watchers:** 1
- **Attachments:** 7
- **Attachment filenames:** Binomial-After.png; Binomial-Before.png; Exact1-After.png; Exact1-Before.png; Loot-Table-Bug.zip; Range-After.png; Range-Before.png
- **Issue links:** Duplicate:inward:MC-237908:Cannot drop multiple totems of undying with custom loot table

## Description

Issue
After updating to 1.17 I discovered that the set_count function for a loot table only outputs a single item to the player when it had previously given the intended amount throughout the 1.16 releases. Note this applies to all count settings including exact, range, and binomial. The error only applies to unstackable items such as saddles and minecarts, in 1.16 multiple slots would be filled with a single unstackable item but now there is only one.
Recreate
Recreating this issue is simple and all you have to do is create a loot table with one roll that uses a function to set the count of an item. To assist with this report I have attached raw code, screenshots showing the transition between versions, and a map in 1.16.5 that contains all of the necessary loot tables.
Code 1: set_count exact (format 2)

```
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "weight": 1,
          "name": "minecraft:saddle",
          "functions": [
            {
              "function": "set_count",
              "count": 2
            },
            {
              "function": "set_nbt",
              "tag": "{CustomModelData:7}"
            },
            {
              "function": "set_name",
              "name": [
                {
                  "text": "Exact Format 2",
                  "color": "white",
                  "bold": "true"
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```
Code 2: set_count range

```
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:saddle",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{CustomModelData:7}"
            },
            {
              "function": "minecraft:set_name",
              "name": [
                {
                  "text": "Range",
                  "color": "white",
                  "bold": true
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```
 Code 3: set_count binomial

```
{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:saddle",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:binomial",
                "n": 4,
                "p": 1
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{CustomModelData:7}"
            },
            {
              "function": "minecraft:set_name",
              "name": [
                {
                  "text": "Binomial",
                  "color": "white",
                  "bold": true
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```
Notes
At first I thought it was because of the format I used to compress NBT data into one line. However, after changing the format I realized that this has no effect.
Code 4: Compressed NBT (format 1)

```
{
  "function": "minecraft:set_nbt","tag": "{display:{Name:'{\"text\":\"Exact Format 1\",\"color\":\"white\",\"bold\":true}'},CustomModelData:7}"
}
```
Code 5: Simplified NBT (format 2)

```
"functions": [
            {
              "function": "set_count",
              "count": 2
            },
            {
              "function": "set_nbt",
              "tag": "{CustomModelData:7}"
            },
            {
              "function": "set_name",
              "name": [
                {
                  "text": "Exact Format 2",
                  "color": "white",
                  "bold": "true"
                }
              ]
            }
```

## Comments (3)

### Comment 1: migrated (2021-06-15T21:56:50.034-0700)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: migrated (2023-01-07T03:01:49.024-0800)

Bug is still present in 1.19.3.

### Comment 3: ccJerrycc (2023-12-02T01:46:18.908-0800)

This was due to an additional clamp during generation (decompiled 1.20.2 with vanilla mapping:
net.minecraft.world.level.storage.loot.functions.SetItemCountFunction.class

```public ItemStack run(ItemStack $$0, LootContext $$1) {
    int $$2 = this.add ? $$0.getCount() : 0;
    $$0.setCount(Mth.clamp($$2 + this.value.getInt($$1), 0, $$0.getMaxStackSize()));
    return $$0;
}```
I thought it's WAI but here's also split operation before insertion, so decided by mojang ¯_(ツ)_/¯
