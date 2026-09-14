# MC-267806: Single shift-clicking on items while holding the same item with the cursor stacks the items

**Mojira URL:** [https://bugs.mojang.com/browse/MC-267806](https://bugs.mojang.com/browse/MC-267806)

## Report details

- **Mojira categories:** Inventory
- **Project:** MC
- **Issue key:** MC-267806
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-01-08T07:35:23.571-0800
- **Updated:** 2025-04-29T10:59:01.175-0700
- **Resolution date:** 2024-01-23T10:20:44.136-0800
- **Affects versions:** 23w51b
- **Fix versions:** 24w03a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 0
- **Issue links:** Relates:inward:MC-267433:Shift double-clicking while holding the same item on your cursor doesn't transfer items

## Description

The bug
Shift-clicking on items while holding the same item with the cursor stacks the items, essentially ignoring the fact you are shifting. This is a different behaviour than 1.20.4 where it would move them items to the other inventory. This is a very annoying bug as i frequently use this method to move a single or a couple of items to my inventory from containers, by picking up the entire stack, setting a few items in the stack down in the container, then shift-clicking the couple items into my inventory and placing the remainder back into the chest. It is more convienient that way because it does not require moving the mouse, however, this behaviour is completely broken in the 1.20.5 snapshots making inventory management much more frustrating.
This issue is closely related to but not the same issue as MC-267433. This particular bug is new to the 1.20.5 snapshots and does not regard shift-double clicking.
Steps to reproduce
- Place a stack blocks into a chest

- Pick up the item with your cursor and use the right click function to place a few of that item into the chest

- While holding the partial stack of items with your cursor, try to shift click the few items of the same type you just put in the chest into your inventory

- Notice it just stacks the items.

Observed behaviour
 Using shift-clicking to shift click items while holding the same item type ignores the shift function and instead just stacks the items
Expected behaviour
 The items do not stack and it allows you to move the partial stack into your inventory

## Comments (1)

### Comment 1: Brevort (2024-01-19T07:35:56.604-0800)

Fixed in 24w03a.
