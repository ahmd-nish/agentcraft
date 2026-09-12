# MC-266738: Subtitles string "subtitles.block.trial_spawner.spawn_mob" is misleading and inconsistent

**Mojira URL:** [https://bugs.mojang.com/browse/MC-266738](https://bugs.mojang.com/browse/MC-266738)

## Report details

- **Mojira categories:** Accessibility; Sound; Text
- **Project:** MC
- **Issue key:** MC-266738
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2023-11-16T13:44:20.662-0800
- **Updated:** 2025-03-25T13:22:48.120-0700
- **Resolution date:** 2023-12-08T02:21:30.243-0800
- **Affects versions:** 23w45a; 23w46a; 1.20.3 Pre-Release 1; 1.20.3 Pre-Release 2; 1.20.3 Pre-Release 3; 1.20.3 Pre-Release 4; 1.20.3 Release Candidate 1; 1.20.3; 1.20.4 Release Candidate 1; 1.20.4
- **Fix versions:** 23w51a
- **Area:** Expansion B
- **Watchers:** 1
- **Attachments:** 0

## Description

The bug
The subtitle string "Mob spawns" (subtitles.block.trial_spawner.spawn_mob) is misleading and inconsistent.
"Mob spawns" implies that the mob spawns itself or without a known originator. However, the creature is actually spawned by the Trial Spawner for that particular event, so I expect a text string like "Mob spawned".
Moreover, every other string from the subtitles.block.trial_spawner.* group mentions the Trial Spawner (Trial Spawner crackles, Trial Spawner closes, Trial Spawner charges up, Trial Spawner ejects items, Trial Spawner opens), only the reported one is not.
To merge both issues with this string, I expect a string like "Trial Spawner spawns mob".
Affected string
Translation Key
Current String
Expected String
String URL on Crowdin
subtitles.block.trial_spawner.spawn_mob
Mob spawns
Trial Spawner spawns mob
https://crowdin.com/translate/minecraft/10038/enus-de#5362648
h3. Steps to reproduce
- Activate subtitles in accessibility settings.

- Stand next to a Trial Spawner in survival mode and watch the subtitles.

Observed result
The current subtitle string, "Mob spawns", is misleading, suggesting that the mob spawns independently, whereas it is spawned by the Trial Spawner in this specific event.
Unlike other strings in the subtitles.block.trial_spawner.* group, the reported string does not mention the Trial Spawner, creating an inconsistency.
Expected result
The subtitle string accurately reflects that the creature is spawned by the Trial Spawner. A text string like "Mob spawned" would be more appropriate; however, in line with consistency, the subtitle should include the Trial Spawner, similar to other strings in the subtitles.block.trial_spawner.* group. Thus, a revised string like "Trial Spawner spawns mob" is expected.

## Comments (1)

### Comment 1: migrated (2023-12-06T15:17:30.712-0800)

Can also be checked by running following command

```/tellraw @s {"translate":"subtitles.block.trial_spawner.spawn_mob"}```
