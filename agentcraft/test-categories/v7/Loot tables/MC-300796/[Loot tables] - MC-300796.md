# MC-300796: Harvesting from sweet berry bushes can drop more sweet berries than before

**Mojira URL:** [https://bugs.mojang.com/browse/MC-300796](https://bugs.mojang.com/browse/MC-300796)

## Report details

- **Mojira categories:** Loot tables
- **Project:** MC
- **Issue key:** MC-300796
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2025-08-06T20:46:15.661-0700
- **Updated:** 2026-03-11T03:47:51.884-0700
- **Resolution date:** 2025-08-15T02:05:21.740-0700
- **Affects versions:** 25w32a; 25w33a
- **Fix versions:** 25w34a
- **Area:** Platform HC
- **Votes:** 1
- **Watchers:** 0
- **Attachments:** 0

## Description

The bug
In 25w32a, a dedicated loot table for harvesting sweet berry bushes is introduced. However, the drop count for sweet berries is different than previous versions:
- In 1.21.8
- Third growth stage yields 1-2

- Final growth stage yields 2-3

- In 25w32a
- Third growth stage yields 1-3

- Final growth stage yields 2-4

This is not mentioned in the 25w32a changelog, so I believe it is a bug.
To Reproduce
- Run the command

```
/fill ~ ~ ~ ~9 ~ ~9 minecraft:sweet_berry_bush[age=3]
```
- Right-click on the sweet berry bushes.

- Take note how many sweet berries you can obtain in a single harvest.

Observed Result
You sometimes obtain 4 sweet berries in a single harvest.
Expected Result
You only obtain no more than 3 sweet berries in a single harvest.
Analysis
The issue lies in the corresbonding loot table, which is located in data/minecraft/loot_table/harvest/sweet_berry_bush.json:

```
{
  "type": "minecraft:block_interact",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "conditions": [
            {
              "block": "minecraft:sweet_berry_bush",
              "condition": "minecraft:block_state_property",
              "properties": {
                "age": "3"
              }
            }
          ],
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:sweet_berries"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:sweet_berries"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:harvest/sweet_berry_bush"
}
```
We can conclude that the loot table always drops 1-3 sweet berries, and additionally drop one more if its age is 3, which demonstrates the bug behavior.
To fix the issue, simply adjust the maximum count at line 40:

```
"max": 3.0,
```
to:

```
"max": 2.0,
```

## Comments (0)

No comments were available in the downloaded comment corpus.
