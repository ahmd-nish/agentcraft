# MC-236136: Strikethrough and underlined text in the F3 debug menu renders over subtitles

**Mojira URL:** [https://bugs.mojang.com/browse/MC-236136](https://bugs.mojang.com/browse/MC-236136)

## Report details

- **Mojira categories:** Debug; Rendering
- **Project:** MC
- **Issue key:** MC-236136
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2021-09-08T04:56:39.733-0700
- **Updated:** 2025-04-11T10:36:44.296-0700
- **Resolution date:** 2023-08-04T05:42:00.387-0700
- **Affects versions:** 1.17.1; 21w37a; 21w40a; 1.18; 1.18.1; 22w05a; 22w06a; 1.18.2 Pre-release 1; 1.18.2; 22w13a; 22w15a; 22w17a; 1.19; 1.19.1; 1.19.2
- **Fix versions:** 1.19.3 Release Candidate 1
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** MC-236136.mp4; MC-236136.png; MC-236136-1.png; MC-236136-2.png; MC-236136 - Behavior in 1.19.3-pre3.png; MC-236136 - Behavior in 1.19.3-rc1 (Fixed).png
- **Issue links:** Relates:outward:MC-264597:F3 debug menu underlined text renders over subtitles | Relates:inward:MC-193511:Title text renders in front of narrator text

## Description

The Bug:
Strikethrough and underlined text in the F3 debug menu renders over subtitles.
Steps to Reproduce:
- Create a new world with cheats enabled.

- Ensure that you have subtitles enabled in your accessibility settings.

- Enable the F3 debug screen.

- Teleport all entities to your position to produce lots of sounds and subtitles by using the command provided below.

```
/tp @e @s
```

- Look at the subtitles overlay.

- Take note as to whether or not strikethrough and underlined text in the F3 debug menu renders over subtitles.

Observed Behavior:
Strikethrough and underlined text in the F3 debug menu renders over subtitles.
Expected Behavior:
Strikethrough and underlined text in the F3 debug menu would not render over subtitles.

## Comments (4)

### Comment 1: migrated (2021-09-08T04:56:39.733-0700)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: Avoma (2021-09-08T04:56:58.178-0700)

Relates to .

### Comment 3: Avoma (2023-01-13T08:42:13.413-0800)

This issue was present in 1.19.3-pre3, but no longer occurs in versions above or equal to 1.19.3-rc1. With this being said, this issue has been fixed in 1.19.3-rc1.

### Comment 4: ampolive (2023-01-13T14:28:29.384-0800)

Confirmed fixed.
