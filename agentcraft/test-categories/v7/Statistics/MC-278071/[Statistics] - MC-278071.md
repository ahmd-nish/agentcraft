# MC-278071: "minecraft.used:minecraft.trident" doesn't increase when throwing a trident

**Mojira URL:** [https://bugs.mojang.com/browse/MC-278071](https://bugs.mojang.com/browse/MC-278071)

## Report details

- **Mojira categories:** Items; Statistics
- **Project:** MC
- **Issue key:** MC-278071
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-11-03T01:51:57.474-0700
- **Updated:** 2025-02-11T06:46:17.012-0800
- **Resolution date:** 2024-11-06T01:34:12.513-0800
- **Affects versions:** 24w44a; 1.21.3
- **Fix versions:** 24w45a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** 1730623827775.jpg

## Description

This issue was not present in 1.21.1.
The bug:
Throwing a trident that is not enchanted with Riptide does not increment the minecraft.used:minecraft.trident statistic, nor any scoreboard objectives using said statistic.
How to reproduce:
- Execute the following commands in order to create a scoreboard objective tracking the times a player has thrown a trident:

```
/scoreboard objectives add MC-278071 minecraft.used:minecraft.trident
```

```
/scoreboard objectives setdisplay sidebar MC-278071
```

- Give yourself a trident.

- Throw the trident.
→  The objective does not increase.

- Check the Items tab in your statistics menu.
→  The statistic did not increase.

Expected result:
Throwing a trident would count as a use for the minecraft.used:minecraft.trident statistic.
Observed result:
Throwing a trident does not count as a use for the minecraft.used:minecraft.trident statistic.

## Comments (1)

### Comment 1: migrated (2024-11-03T01:51:57.474-0700)

This comment contained an image attachment, please login to view the attachment.
