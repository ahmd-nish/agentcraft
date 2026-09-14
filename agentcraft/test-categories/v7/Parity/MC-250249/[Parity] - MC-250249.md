# MC-250249: Parity Issue: Allays pick up arrow/potion items with other effects than the ones they're holding

**Mojira URL:** [https://bugs.mojang.com/browse/MC-250249](https://bugs.mojang.com/browse/MC-250249)

## Report details

- **Mojira categories:** Mob behaviour; Parity
- **Project:** MC
- **Issue key:** MC-250249
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2022-04-16T11:38:41.109-0700
- **Updated:** 2025-04-30T07:38:28.665-0700
- **Resolution date:** 2022-07-06T04:53:34.549-0700
- **Affects versions:** 22w15a; 22w17a; 1.19 Pre-release 1; 1.19 Pre-release 2; 1.19 Pre-release 4; 1.19 Pre-release 5; 1.19; 22w24a
- **Fix versions:** 22w42a
- **Labels:** vanilla-parity
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 2022-04-16_16.45.02.png; MC-250249.mp4; MC-250249.png

## Description

Steps to Reproduce:
- Give a tipped arrow with night vision effect (for example) to allay

- Drop tipped arrows with other effect on the floor

Observed Results:
Allay will pick up the tipped arrows with the other effect
Expected Results:
Allay should only pick up tipped arrows with the same effect

This bug was happening in BE to but has been fixed.

## Comments (11)

### Comment 1: migrated (2022-04-16T11:38:41.109-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: migrated (2022-04-16T12:17:18.475-0700)

Duplicate of MC-249819, they only look at item ID, all tipped arrows have the same item ID.

### Comment 3: ampolive (2022-04-16T12:35:31.491-0700)

However, this is a valid parity issue.

### Comment 4: Avoma (2022-04-17T05:54:59.032-0700)

If not a duplicate of MC-249819, then it's definitely related since it's essentially the same core problem.

### Comment 5: Goncalo47 (2022-04-22T10:09:33.844-0700)

Also affect potions

### Comment 6: Tinsel (2022-05-19T08:48:15.365-0700)

In 1.19 Pre-1

### Comment 7: Tinsel (2022-05-24T11:41:23.570-0700)

Still in 1.19 Pre-2

### Comment 8: Tinsel (2022-05-25T11:00:22.734-0700)

In 1.19 Pre-3

### Comment 9: Tinsel (2022-05-30T10:01:17.446-0700)

In  1.19 Pre-4

### Comment 10: Tinsel (2022-06-01T20:52:18.402-0700)

In 1.19 Pre-5

### Comment 11: migrated (2022-06-16T11:45:28.162-0700)

Can confirm it also happens with potions, splash potions, lingering potions in 1.19 Release
In Bedrock, Allays also differenciate between Lvl 1 potions and lvl 2 potions, and between lvl 1 potions and lvl 1 extended (with redstone) potions
