# MC-214662: Redstone torches on repeaters and comparators are shaded differently from normal redstone torches

**Mojira URL:** [https://bugs.mojang.com/browse/MC-214662](https://bugs.mojang.com/browse/MC-214662)

## Report details

- **Mojira categories:** Parity; Rendering
- **Project:** MC
- **Issue key:** MC-214662
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2021-02-09T10:13:28.285-0800
- **Updated:** 2025-04-26T12:31:06.440-0700
- **Resolution date:** 2024-10-30T12:20:31.440-0700
- **Affects versions:** 1.16.5; 21w05b; 21w06a; 21w07a; 21w08b; 21w13a; 21w17a; 21w20a; 1.17 Pre-release 1; 1.17; 1.17.1 Pre-release 1; 1.17.1; 21w39a; 21w40a; 21w42a; 1.18 Pre-release 1; 1.18; 1.18.1 Pre-release 1; 1.18.1; 22w06a; 1.18.2; 22w11a; 1.19 Pre-release 1; 1.19; 1.19.1 Pre-release 3; 1.19.4; 23w14a; 1.20.1; 1.20.4; 1.21
- **Fix versions:** 24w33a
- **Labels:** 1.8-bad-model-conversion-remnants; 1.8-model-conversion-remnants; 14w25a; unwanted-model-shading; vanilla-parity
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 2021-02-09_17.43.30.png; 2021-02-09_18.13.56.png; TorchFix.zip
- **Issue links:** Relates:outward:MC-277950:Open potted eyeblossom is shaded (flower_pot_cross_emissive) | Relates:inward:MC-275520:Programmer Art: Lit torches on repeaters are still shaded when they should not be

## Description

The resource pack attached to MC-214686 offers a complete fix for this issue. Mojang have my full permission to (and are encouraged to) replace the affected vanilla model files with the contents of the resource pack.
The bug
The torches on redstone repeaters and redstone comparators appear darker than expected, and are shaded depending on the view direction. This is not the case with redstone torches themselves, which are fully lit regardless of the view direction.
This began in 1.8, and was not the case in 1.7 or earlier. In addition, this is not the case in Bedrock Edition, effectively also making this a parity issue.
While this was listed in , I still strongly consider this behaviour unintended for many reasons, including the two stated above. In addition, MC-67830's resolution contradicts such an assertion of this being intended. Other reasons are listed in MC-236474, a very similar issue.
How to reproduce
- Place down a redstone torch, noting how bright it appears when in the "on" state

- Place down a redstone repeater in a way that the torch powers it

- Note that the torches on said redstone repeater are darker than the standalone torch

- Now place down a comparator which also receives power

- Note that it, too, has darker torches than one would expect

Expected behaviour
The torches on repeaters and comparators would appear as bright as redstone torches themselves
Actual behaviour
Repeater and comparator torches are noticeably darker
How to fix
The resource pack attached to MC-214686 fixes this issue completely.

## Comments (23)

### Comment 1: migrated (2021-02-09T10:13:28.285-0800)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: Avoma (2021-02-10T02:08:11.507-0800)

Can confirm.

### Comment 3: Avoma (2021-02-11T08:13:26.947-0800)

Can confirm in 21w06a.

### Comment 4: Avoma (2021-02-19T12:23:49.183-0800)

Can confirm in 21w07a.

### Comment 5: Avoma (2021-02-26T06:51:36.751-0800)

Can confirm in 21w08b.

### Comment 6: Avoma (2021-04-02T09:16:20.777-0700)

Can confirm in 21w13a.

### Comment 7: Avoma (2021-04-29T01:12:23.987-0700)

Can confirm in 21w17a.

### Comment 8: SoloAlguien (2021-06-01T22:17:27.234-0700)

Can confirm in 1.17 Pre-release 3.

### Comment 9: SoloAlguien (2021-06-20T11:49:58.784-0700)

Can confirm in 1.17 and 1.17.1 Pre-release 1.

### Comment 10: SoloAlguien (2021-07-11T15:36:03.054-0700)

Can confirm in 1.17.1.

### Comment 11: SoloAlguien (2021-09-29T14:27:29.142-0700)

Can confirm in 21w39a.

### Comment 12: SoloAlguien (2021-10-10T14:14:58.398-0700)

Can confirm in 21w40a.

### Comment 13: SoloAlguien (2021-10-20T10:53:30.009-0700)

Can confirm in 21w42a.

### Comment 14: SoloAlguien (2021-11-11T10:36:15.350-0800)

Can confirm in 1.18 Pre-release 1.

### Comment 15: SoloAlguien (2021-12-03T15:06:02.177-0800)

Can confirm in 1.18 and 1.18.1 Pre-release 1.

### Comment 16: SoloAlguien (2021-12-17T21:31:31.063-0800)

Can confirm in 1.18.1.

### Comment 17: SoloAlguien (2022-03-01T12:11:01.704-0800)

Can confirm in 1.18.2.

### Comment 18: ZYX_2D (2022-05-22T22:30:39.944-0700)

Comparators and Repeaters cannot glow, you know. While Torches can.

### Comment 19: migrated (2022-05-22T22:38:38.395-0700)

Light emmision is not at all related to this report...

### Comment 20: Avoma (2022-07-25T02:55:57.936-0700)

Can confirm in 1.19.

### Comment 21: BeeTeeKay (2024-07-07T16:27:59.891-0700)

Affects 1.21

### Comment 22: bodakugga (2024-08-15T11:35:58.044-0700)

Partially fixed in 24w33a, only for lit redstone torches

### Comment 23: muzikbike (2024-08-16T16:19:30.953-0700)

As per  the issue is that normal redstone torches should appear darker, so this is completely fixed.
