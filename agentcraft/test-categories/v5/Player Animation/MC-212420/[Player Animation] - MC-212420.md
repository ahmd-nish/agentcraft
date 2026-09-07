# MC-212420: Sign dyeing sound and hand animation plays even when not consuming a dye

**Mojira URL:** [https://bugs.mojang.com/browse/MC-212420](https://bugs.mojang.com/browse/MC-212420)

## Report details

- **Mojira categories:** Player Animation; Sound
- **Project:** MC
- **Issue key:** MC-212420
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2021-01-22T03:14:09.272-0800
- **Updated:** 2025-03-25T13:02:14.579-0700
- **Resolution date:** 2024-06-10T15:08:34.920-0700
- **Affects versions:** 21w03a; 21w07a; 21w14a; 21w15a; 21w16a; 1.17; 1.17.1; 21w42a; 1.18.1; 1.18.2; 1.19; 1.19.1; 1.19.2; 1.19.3; 23w04a
- **Fix versions:** 23w12a
- **Area:** Gameplay
- **Labels:** hand-animation
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2021-01-22_12.08.49.png; 2024-06-10_13-35-15.mp4; MC-212420.mp4; MC-212420.png

## Description

The Bug
When you try to dye a sign that is already painted with that color, the dye in your hand does not consume, but the "Dye stains" sound still plays and the hand animation still occurs. Eg. in the attached picture, I click on a white text sign with a white dye and no item is consumed. Howewer, it can be seen from the subtitles that a sound plays.
Steps to Reproduce
-     Summon a sign that has some text and a magenta dye already applied to it.

```
/setblock ~ ~ ~ minecraft:dark_oak_sign{Color:"magenta",Text1:'{"text":"MC-212420"}'}
```

-     Obtain a magenta dye, switch into survival mode, and attempt to apply it to the sign you just summoned.

-     Take note as to whether or not the hand animation and sign dying sounds play even when not consuming dyes.

Observed Behavior
The hand animation and sign dying sounds play even when not consuming dyes.
Expected Behavior
The hand animation and sign dying sounds would not play when not consuming dyes.

## Comments (12)

### Comment 1: migrated (2021-01-22T03:14:09.272-0800)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: Avoma (2021-04-10T05:32:42.250-0700)

Can confirm in 21w14a.

### Comment 3: Avoma (2021-04-19T03:46:56.968-0700)

Can confirm in 21w15a. Video attached.

### Comment 4: Avoma (2021-04-25T02:25:05.320-0700)

Can confirm in 21w16a.

### Comment 5: Avoma (2021-06-10T03:07:18.324-0700)

Can confirm in 1.17.

### Comment 6: Avoma (2021-07-07T09:16:50.171-0700)

Can confirm in 1.17.1.

### Comment 7: Avoma (2021-10-27T02:23:16.545-0700)

Can confirm this behavior in 21w42a. Here are some extra details regarding this problem.
The Bug:
The hand animation and sign dying sounds play even when not consuming dyes.
Steps to Reproduce:
- Summon a sign that has some text and a magenta dye already applied to it.

```/setblock ~ ~ ~ minecraft:dark_oak_sign{Color:"magenta",Text1:'{"text":"MC-212420"}'}```
- Obtain a magenta dye, switch into survival mode, and attempt to apply it to the sign you just summoned.

- Take note as to whether or not the hand animation and sign dying sounds play even when not consuming dyes.

Observed Behavior:
The hand animation and sign dying sounds play even when not consuming dyes.
Expected Behavior:
The hand animation and sign dying sounds would not play when not consuming dyes.

### Comment 8: Avoma (2021-12-28T09:50:39.192-0800)

Can confirm in 1.18.1.

### Comment 9: Avoma (2022-03-09T11:41:06.773-0800)

Can confirm in 1.18.2.

### Comment 10: Avoma (2022-06-18T11:28:51.644-0700)

Can confirm in 1.19 and 22w24a.

### Comment 11: Avoma (2022-09-15T10:07:04.937-0700)

Can confirm in 1.19.2.

### Comment 12: [Mod] Jingy (2024-06-10T11:38:29.159-0700)

This issue was fixed in 23w12a, when editing signs was added to the game. Now when using dye on a sign, the sound and hand animation play only once. If the sign is waxed, it is no longer possible to edit, therefore making this issue no longer reproducable at all.
Video showcasing the difference in 1.19.4 and 23w12a:

Important note: The hand animation plays twice in 23w12a, which seems unexpected, but is the desired affect. The hand animation plays once for using the dye, then once for opening the GUI. (notice how the sound only plays once).
