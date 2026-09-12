# MC-249168: Dispensing a Bucket of Tadpole above or below a dimension dispenses the item, instead of a tadpole

**Mojira URL:** [https://bugs.mojang.com/browse/MC-249168](https://bugs.mojang.com/browse/MC-249168)

## Report details

- **Mojira categories:** Redstone
- **Project:** MC
- **Issue key:** MC-249168
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2022-03-16T16:15:48.071-0700
- **Updated:** 2025-03-25T13:39:49.211-0700
- **Resolution date:** 2022-03-31T11:06:17.477-0700
- **Affects versions:** 22w11a; 22w12a
- **Fix versions:** 22w13a
- **Watchers:** 1
- **Attachments:** 0

## Description

The bug
When a dispenser dispenses a Bucket of Tadpole above or below a dimension, the dispenser dispenses the Bucket of Tadpole item, rather than a tadpole. All other bucketed mobs dispense the entity when being dispensed above or below a dimension.
How to reproduce
- Enter the Nether

- Run the command:

```
/setblock ~ 255 ~ dispenser[facing=up]
```

- Run the command:

```
/tp @s ~ 256 ~
```

- Place a Bucket of Axolotl in the dispenser, and activate the dispenser with a button
 An axolotl is spawned above the dispenser

- Place a Bucket of Tadpole in the dispenser, and activate the dispenser with a button
 The Bucket of Tadpole item is dispensed, rather than the tadpole

Expected behavior
The tadpole would be spawned when activating the dispenser.
Actual behavior
The Bucket of Tadpole is dropped when activating the dispenser.

## Comments (3)

### Comment 1: migrated (2022-03-19T09:35:15.784-0700)

This happens in all dimensions, not just in the Nether.

### Comment 2: markderickson (2022-03-31T10:28:58.750-0700)

This has been fixed in 22w13a.

### Comment 3: ampolive (2022-03-31T10:36:22.212-0700)

Can confirm fixed in 22w13a.
