# MC-265060: Missing sprite for error in Loom GUI (loom.png)

**Mojira URL:** [https://bugs.mojang.com/browse/MC-265060](https://bugs.mojang.com/browse/MC-265060)

## Report details

- **Mojira categories:** Resource Packs; UI
- **Project:** MC
- **Issue key:** MC-265060
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2023-08-26T12:03:04.430-0700
- **Updated:** 2025-03-25T13:23:05.625-0700
- **Resolution date:** 2023-09-05T02:34:51.363-0700
- **Affects versions:** 23w33a
- **Fix versions:** 1.20.2 Pre-release 1
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** 1 without pack error not visible.png; 2 without pack correct banner.png; 3 with pack error  visible (red X).png; 4 with pack correct banner (no X).png; loom.png; Loom Error Demo.zip

## Description

The bug
When you try to add more than 6 patterns to a banner in a loom you don't get any error or message.
However, the Minecraft code can show an icon in the loom GUI when you add a banner with 6 or more patterns (for example, the Ominous banner).
The problem is that the gui/container/loom.png file does not have the appropiate sprite to show this error.
This bug exists also in the new 1.20.2 snapshots, because there is not an error sprite in gui/sprites/container/loom directory.
How to reproduce
Open the Loom GUI and put the Ominous banner in the first slot (or any banner with 6 patterns).
Actual behavior
The GUI does not show any error, but you cannot add more patterns to that banner. See picture "1 without pack error not visible.png"
Expected behavior
You should see something like a red X because you cannot add more patterns to than banner. See picture "3 with pack error  visible (red X).png"
Corrected file
I have attached a very simple resource pack with only a modified gui/container/loom.png file with an added sprite (Loom Error Demo.zip). I have also attached the file here directly.
When you use this resource pack and repeat the steps, then you get a red X in the final slot if the banner already has 6 or more patterns.
Regretly, this correction does not work in the 1.20.2 snapshots.
Disclaimer
I think this is a bug and not a change request because the code for using this sprite is already in Minecraft 1.20.1 (and earlier). It is just that the sprite is missing in the texture file.
I don't know if the code has changed for 1.20.2.
Sorry, I am not an English speaker. So, please rewrite this description if you think it is necessary for better understanding.

## Comments (3)

### Comment 1: migrated (2023-08-26T12:03:04.430-0700)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: migrated (2023-08-30T08:25:15.789-0700)

Not sure why you, , removed 1.20.1,as the sprite was missing there too, but could be added via resource pack.
Nature of the issue was slightly different, but the issue existed nonetheless.

### Comment 3: gegy (2023-09-04T03:39:28.008-0700)

Regarding affecting 1.20.1: it is not intended for the sprite to be present in the Vanilla pack, but we also want to maintain it as a supported use-case for resource packs. 🙂
