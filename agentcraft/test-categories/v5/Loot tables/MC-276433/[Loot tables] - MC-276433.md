# MC-276433: set_enchantments function removes enchantments component from books

**Mojira URL:** [https://bugs.mojang.com/browse/MC-276433](https://bugs.mojang.com/browse/MC-276433)

## Report details

- **Mojira categories:** Data Packs; Loot tables
- **Project:** MC
- **Issue key:** MC-276433
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-09-06T03:09:16.090-0700
- **Updated:** 2025-04-26T16:40:31.616-0700
- **Resolution date:** 2024-09-09T02:01:14.155-0700
- **Affects versions:** 1.21.1; 24w36a
- **Fix versions:** 24w37a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** MC-276433.zip

## Description

Steps to reproduce:
- Create/open a world with the attached data pack applied:

- Run /loot give @s loot test:test

- While holding the enchanted book, run /data get entity @s SelectedItem.components."!minecraft:enchantments"

Observed result:
The command outputs:

```
<username> has the following entity data: {}
```
Expected result:
The command outputs:

```
Found no elements matching SelectedItem.components."!minecraft:enchantments"
```
Steps to reproduce (vanilla):
- Go to a trial chamber

- Open ominous vaults until you get an enchanted book. Keep opening ominous vaults until you get a wind burst enchanted book.

- Disenchant the book you just obtained from the ominous vault using a grindstone

- Try to enchant the book you just disenchanted in an enchantment table

- Try to stack the book with other normal books

Observed result:
The book that was obtained and disenchanted from the trial chambers will not stack with other books and cannot be enchanted. After checking with advanced tooltips, this book only has 8 components, compared to normal book items with 9 components. After examining this glitched item in an nbt editor, the book had a minecraft:enchantments component removed. This is what was causing the book to not stack with other normal book items and not be enchantable by normal means.
Expected result:
The book that was obtained and disenchanted from the trial chambers should stack with other books and should be enchanted.
Notes:
This does not happen with other enchanted items, nor does it happen when name is set to minecraft:enchanted_book instead of minecraft:book.

## Comments (3)

### Comment 1: migrated (2024-09-06T03:09:16.090-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: Jarl-Penguin (2024-09-06T06:31:01.613-0700)

We do not have enough information to reproduce this issue.
Please include the following information to help us understand your problem:
Steps to Reproduce:
1. (Explain what needs to be done for the issue to happen)
2.
3.
Observed Results:
(Briefly describe what happens)
Expected Results:
(Briefly describe what should happen)
Please also attach any needed commands, add-ons/behavior packs, data packs, resource packs, screenshots, videos, or worlds needed to help reproduce this issue.
Refer to the Bug Tracker Guidelines for more information about how to write helpful bug reports. Bug reports with insufficient information may be closed as Incomplete.
This issue is being temporarily resolved as Awaiting Response. Once the requested information has been delivered, the report will be reopened automatically.
Quick Links:
📓 Bug Tracker Guidelines – 💬 Community Support – 📧 Mojang Support (Technical Issues) – 📧 Microsoft Support (Account Issues)
📓 Project Summary – ✍️ Feedback and Suggestions – 📖 Game Wiki

### Comment 3: TheMightyDark (2024-09-06T09:19:22.825-0700)

Can confirm.
Steps to Reproduce:
- Go to a trial chamber.

- Open ominous vaults until you get an enchanted book. Keep opening ominous vaults until you get a wind burst enchanted book.

- Disenchant the book you just obtained from the ominous vault using a grindstone.

- Try to enchant the book you just disenchanted in an enchantment table.

- Try to stack the book with other normal books

Observed Results:
The book that was obtained and disenchanted from the trial chambers will not stack with other books and cannot be enchanted. After checking with advanced tooltips, this book only has 8 components, compared to normal book items with 9 components. After examining this glitched item in an nbt editor, the book had a minecraft:enchantments component disabled using !minecraft:enchantments component. This is what was causing the book to not stack with other normal book items and not be enchantable by normal means.
Expected Results:
The book that was obtained and disenchanted from the trial chambers should stack with other books and should be enchanted.
