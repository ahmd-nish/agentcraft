# MC-55718: Dragon egg doesn't appear in Creative inventory

**Mojira URL:** [https://bugs.mojang.com/browse/MC-55718](https://bugs.mojang.com/browse/MC-55718)

## Report details

- **Mojira categories:** Inventory; Parity
- **Project:** MC
- **Issue key:** MC-55718
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2014-05-23T11:44:50.985-0700
- **Updated:** 2025-04-30T06:34:50.211-0700
- **Resolution date:** 2022-10-26T06:31:36.867-0700
- **Affects versions:** Minecraft 1.7.9; Minecraft 14w21b; Minecraft 17w15a; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 5; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w27a; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Pre-release 2; 1.16.2 Pre-release 3; 1.16.2 Release Candidate 1; 1.16.2 Release Candidate 2; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 20w46a; 20w48a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w07a; 21w17a; 1.17; 1.17.1 Pre-release 1; 1.17.1; 21w39a; 1.18 Pre-release 1; 1.18 Release Candidate 3; 1.18; 1.18.1 Release Candidate 2; 1.18.1; 22w03a; 22w07a; 1.18.2; 22w11a; 22w12a; 22w15a; 1.19; 22w24a; 1.19.1 Pre-release 1; 1.19.1 Pre-release 5; 1.19.2; 22w42a
- **Fix versions:** 22w43a
- **Game mode:** Creative
- **Labels:** creative-inventory-contents; dragon_egg; vanilla-parity
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 2014-05-23_14.40.12.png; MC-55718.mp4; MC-55718 - Comparison.png

## Description

For a comprehensive list of other examples of issues with item positions in the Creative inventory, click here.
The bug
The dragon egg is completely absent from the Creative inventory for some reason. It would be expected it would be there, as it isn't a very technical block like barriers or command blocks which have been intentionally kept out of the Creative inventory.
This is also a parity issue, as the dragon egg does appear in Bedrock Edition's creative inventory.
How to reproduce
- Give yourself a dragon egg: /give @p minecraft:dragon_egg

- Note the item name - this will be used for searching

- Open the Creative inventory

- Enter the Search tab

- Search for Dragon Egg

- See no relevant results

## Comments (23)

### Comment 1: migrated (2014-05-23T11:44:50.985-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: migrated (2014-05-23T12:11:22.490-0700)

The dragon egg isn't mean't to be a block. Its only obtainable in the end by using a piston, but is unobtainable in other parts.

### Comment 3: qmagnet (2014-05-23T13:52:07.810-0700)

you can also get the egg by typing

```/give @p dragon_egg```

### Comment 4: kumasasa (2014-05-23T14:07:44.706-0700)

Like command_block or barrier

### Comment 5: migrated (2020-06-07T19:08:32.051-0700)

Let me point out a part of the description:
Plus, middle-clicking on dragon egg in creative mode doesn't make it appear on your action bar.
It is false since Pick Block can be used on a Dragon Egg to obtain it in the inventory.

### Comment 6: anthony cicinelli (2020-06-17T06:27:29.356-0700)

Confirmed for 1.16 pre-release 7

### Comment 7: anthony cicinelli (2020-06-21T08:03:08.451-0700)

Confirmed for 1.16 rc-1

### Comment 8: Avoma (2021-02-06T06:20:42.650-0800)

Can confirm in 21w05b.

### Comment 9: Avoma (2021-02-12T06:07:50.878-0800)

Can confirm in 21w06a.

### Comment 10: Avoma (2021-02-19T03:43:53.617-0800)

Can confirm in 21w07a. Video attached.

### Comment 11: Avoma (2021-05-01T10:00:58.535-0700)

Can confirm in 21w17a.

### Comment 12: Avoma (2021-07-13T00:58:59.046-0700)

Can confirm in 1.17.1.

### Comment 13: migrated (2021-10-03T05:42:10.423-0700)

Affects 21w39a

### Comment 14: ampolive (2021-11-11T14:45:49.089-0800)

Can confirm in 1.18 Pre-release 1.

### Comment 15: Avoma (2021-11-17T04:39:35.150-0800)

Can confirm this in 1.18 Pre-release 2. I've attached a side-by-side comparison of the appearance of this item in the creative inventory in java edition and bedrock edition.

### Comment 16: Avoma (2021-12-08T05:03:36.002-0800)

Can confirm in 1.18.

### Comment 17: Avoma (2021-12-14T09:42:43.019-0800)

Can confirm in 1.18.1.

### Comment 18: Avoma (2022-03-24T09:29:22.926-0700)

Can confirm in 1.18.2 and 22w11a.

### Comment 19: migrated (2022-04-14T14:06:05.848-0700)

In 22w15a

### Comment 20: Avoma (2022-06-13T08:14:31.217-0700)

Can confirm in 1.19.

### Comment 21: Avoma (2022-08-17T07:12:35.760-0700)

Can confirm in 1.19.2.

### Comment 22: migrated (2022-10-26T06:16:05.441-0700)

Fixed in 22w43a,according to the changelog.

### Comment 23: Avoma (2022-10-26T06:27:31.492-0700)

I can also confirm that this has been fixed in 22w43a.
