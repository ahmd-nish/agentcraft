# MC-211194: Debug worlds are shown as being created in the incorrect game mode

**Mojira URL:** [https://bugs.mojang.com/browse/MC-211194](https://bugs.mojang.com/browse/MC-211194)

## Report details

- **Mojira categories:** Debug; UI
- **Project:** MC
- **Issue key:** MC-211194
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2021-01-11T17:46:40.146-0800
- **Updated:** 2025-04-30T05:41:31.733-0700
- **Resolution date:** 2023-02-01T15:31:36.583-0800
- **Affects versions:** 20w51a; 21w03a; 21w05b; 21w06a; 21w07a; 21w08b; 21w10a; 21w11a; 21w16a; 1.17 Pre-release 4; 1.17.1; 21w39a; 1.18 Release Candidate 4; 1.18; 1.18.2; 22w14a; 1.19.3
- **Fix versions:** 23w05a
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2021-05-04_14.11.49.png; Screen Shot 2021-01-11 at 9.25.51 AM.png
- **Issue links:** Duplicate:inward:MC-212786:Gamemode isn't correct in Debug Mode | Duplicate:inward:MC-218041:When the selected world type is debug mode, the game mode button in the create world screen displays the same as before debug mode was selected | Duplicate:inward:MC-220851:Debug mode Glitch | Duplicate:inward:MC-250072:Create World menu shows incorrect gamemode | Relates:outward:MC-205076:Game mode selection is ordered differently

## Description

The bug
When normally creating a debug world, the player is put in spectator mode: they can look, but can't touch. In the 1.17 snapshots, this is still the case.
However, now, the game mode for a debug world is not shown as "Spectator" on the world creation screen. In previous versions, this was correctly shown as "Spectator".
When generating the world, as said above, the player is put into spectator mode correctly.
This issue relates to MC-205076, but I am reporting it separately, as spectator mode is not part of the order described in MC-205076. Additionally, the text shown on the world creation screen is different than the actual behaviour, which is not the case in MC-205076.
How to reproduce
- Open Minecraft -> Singleplayer -> Create New World -> More World Options...

- Hold down the alt key (option) while toggling the World Type button, until you reach Debug Mode

- Click Done
  The Game Mode is shown incorrectly

- Click Create New World
  Your Game Mode is Spectator, as intended

Additional information
A screenshot demonstrating this issue has been attached, taken in snapshot 20w51a:

## Comments (8)

### Comment 1: migrated (2021-01-11T17:46:40.146-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: Brevort (2021-01-11T18:01:45.494-0800)

Can confirm. I just assumed it was intentional, but, now, I don't know why it would be.

### Comment 3: [Mod] violine1101 (2021-01-12T04:55:17.370-0800)

This used to say "Spectator" in previous versions.

### Comment 4: migrated (2021-02-03T14:30:07.493-0800)

The game mode is the same as when you first came onto the world creation screen and selected the game mode. Not always Survival.

### Comment 5: [Mod] ManosSef (2021-05-04T04:15:03.892-0700)

The issue fixes itself when toggling fullscreen. But it occurs again after you change the world type to something else. Screenshot attached.

### Comment 6: ISRosillo14 (2022-12-30T04:25:47.563-0800)

Can confirm in 1.19.3

### Comment 7: ISRosillo14 (2023-02-01T07:58:22.237-0800)

Seems fixed in 23w05a.

### Comment 8: markderickson (2023-02-01T15:31:36.582-0800)

I can confirm that this is fixed in 23w05a.
