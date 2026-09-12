# MC-297491: Glyphs from TTF files are no longer rendered correctly on glow signs

**Mojira URL:** [https://bugs.mojang.com/browse/MC-297491](https://bugs.mojang.com/browse/MC-297491)

## Report details

- **Mojira categories:** Rendering; Resource Packs
- **Project:** MC
- **Issue key:** MC-297491
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2025-05-04T09:51:22.594-0700
- **Updated:** 2026-05-08T06:55:32.404-0700
- **Resolution date:** 2026-05-08T06:55:32.324-0700
- **Affects versions:** 1.21.5; 1.21.6
- **Fix versions:** 26.2 Snapshot 7
- **Area:** Platform G
- **Votes:** 5
- **Watchers:** 1
- **Attachments:** 8
- **Attachment filenames:** 2025-06-20_16.44.23.png; 2025-06-20_21.35.24.png; 2025-10-05_23.27.42-20251005-212742.png; font_from_png.mp4; font_from_png.zip; font_from_ttf.mp4; font_from_ttf.zip; sign_text.txt
- **Issue links:** Duplicate:inward:MC-298982:TTF fonts cause z-fighting on signs with glow ink sacks | Relates:outward:MC-300693:Object text components on glowing signs render incorrectly

## Description

This behavior was introduced in 25w09a.
The bug
When loading a font from a ttf file in a resource pack, the text isn't rendered correctly on glowing signs. The shape of the characters is correct, but the highlighting doesn't correctly appear behind the text, instead overlapping with it. Only the characters that are changed by the ttf file are affected.
Steps to reproduce
- Load the  resource pack (or any resource pack that uses a ttf font).

- Paste the text from  (or any character changed by a resource pack using a ttf font) into a sign.

- Use a glow ink sac on the sign.

Observed behavior
The text will exhibit an effect that looks like z-fighting (as seen in the video below, where the  resource pack is used).
Expected behavior
The glowing effect would be rendered behind the text, as was the case prior to 25w09a, and as still happens when a font is loaded from a png file (as seen in the video below, where the  resource pack is used).

## Comments (7)

### Comment 1: Eic (2025-05-04T09:51:23.962-0700)

This comment contained multiple media attachments (2), please login to view the attachments.

This comment contained an image attachment, please login to view the attachment.

This comment contained multiple media attachments (2), please login to view the attachments.

This comment contained an image attachment, please login to view the attachment.

This comment contained an image attachment, please login to view the attachment.

### Comment 2: [MOD] Greymagic27 (2025-05-05T03:40:30.090-0700)

Please do not mark issues as private, unless your bug report is an exploit or contains information about your username or server.

### Comment 3: Eic (2025-05-05T04:11:32.024-0700)

Sorry, I didn’t mean to mark it as private. It’s “shared with players” so I thought it meant it was public. How can I make it public?

### Comment 4: [MOD] Greymagic27 (2025-05-05T05:05:11.648-0700)

I’ve made it public now

### Comment 5: Andrew Burton (2025-06-21T16:02:31.965-0700)

Yes plz fix this, here are some images of my experience w/ the matter

### Comment 6: Andrew Burton (2025-09-11T08:41:46.612-0700)

CANCONFIRM 1.21.6-1.21.8

### Comment 7: Léah Gex-Collet (2025-10-05T14:28:31.196-0700)

Can confirm for 1.21.9, also, theres additional horribleness at lower resolutions, since there is no way to disable anti-aliasing.
