# MC-297339: Sign text is non-functional

**Mojira URL:** [https://bugs.mojang.com/browse/MC-297339](https://bugs.mojang.com/browse/MC-297339)

## Report details

- **Mojira categories:** Block states; Datafixer
- **Project:** MC
- **Issue key:** MC-297339
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2025-04-29T07:47:12.007-0700
- **Updated:** 2026-03-11T03:54:11.488-0700
- **Resolution date:** 2025-05-02T01:23:52.125-0700
- **Affects versions:** 25w18a
- **Fix versions:** 25w19a
- **Area:** Platform G
- **Votes:** 25
- **Watchers:** 0
- **Attachments:** 7
- **Attachment filenames:** 2025-04-29_10.42.02.png; 2025-04-29_10.42.04.png; 2025-04-29_10.44.01.png; 2025-05-02_02.19.05.png; Screenshot 2025-04-12 234217.png; Screenshot 2025-04-29 223242.png; Screenshot 2025-05-02 102330.png
- **Issue links:** Duplicate:inward:MC-297346:Non-writable sings | Duplicate:inward:MC-297356:Sign dont work | Duplicate:inward:MC-297371:Texts on sign completely disappear, relaunching doesn't work | Duplicate:inward:MC-297386:Sign text not showing up | Duplicate:inward:MC-297390:sign text not appearing | Duplicate:inward:MC-297401:All my Signs/Hanging signs Text (Including Dye color and glow) has been deleted | Duplicate:inward:MC-297399:Signs won't allow typing | Duplicate:inward:MC-297412:Signs do not work in multiplayer | Duplicate:inward:MC-297418:Sign message doesn't work | Duplicate:inward:MC-297430:Editing and creating signs not working | Duplicate:inward:MC-297443:I can't write on any sign | Duplicate:inward:MC-297451:Sign Texts Are Invisible or Blurred When Colored | Duplicate:inward:MC-297450:Sign issues | Duplicate:inward:MC-297444:when adding text to a sign it wont show up | Duplicate:inward:MC-297441:Glow ink sign only | Duplicate:inward:MC-297463:you can't write on the signs | Duplicate:inward:MC-297457:Signs | Duplicate:inward:MC-297468: Wooden Signs Problem | Duplicate:inward:MC-297478:Signs Not Working | Duplicate:inward:MC-297472:Somethings wrong with my signs | Duplicate:inward:MC-297500:Snapshot Sign Bug | Duplicate:inward:MC-297509:Cannot type on signs/text wont appear | Duplicate:inward:MC-297506:I will open sign GUI try to type, but nothing happens | Duplicate:inward:MC-297486:Text on signs will not render | Duplicate:inward:MC-297520:broken signs | Duplicate:inward:MC-297518:No Text On Signs | Duplicate:inward:MC-297522:Cannot write on signs | Duplicate:inward:MC-297523:Cannot write on signs

## Description

Pre-existing signs that had been placed in the world prior to updating to 25w18a no longer have visible text on them and just appear to be blank. When right clicked to try editing text, the sign UI pops up, but neither the text nor the cursor is visible, and any text you try to type does not appear on the screen. Even if you place a new sign down, it will not display text typed, neither in the UI, nor on the sign itself.
Issue was replicated both on a third party hosted server (Aternos), and in single player. Despite attempts to dye signs different colors, text never appeared. Issue occurs with all sign types, both hanging and regular, and occurs when signs are crafted and spawned in. I could not replicate any instance when placing a sign where the bug did not occur.

## Comments (10)

### Comment 1: Shadecoy (2025-04-29T07:47:12.635-0700)

This comment contained an image attachment, please login to view the attachment.

This comment contained an image attachment, please login to view the attachment.

This comment contained an image attachment, please login to view the attachment.

### Comment 2: Henry Harvey (2025-04-29T13:33:40.901-0700)

I have also experienced this issue on 25w18a, unable to type anything and pre-existing text was erased

### Comment 3: flow_santohyj123 (2025-04-29T23:45:28.834-0700)

Can also confirm (Intel Intergrated Graphics), looks like a rendering problem, since using /data get shows that the sign does have text data.

### Comment 4: Donovan Whysong (2025-04-30T10:36:19.853-0700)

Got a Nvidia 4070ti Super I also have this problem.

### Comment 5: bugman33 (2025-04-30T17:16:29.305-0700)

same. got same bug.

### Comment 6: Daniel Francisco (2025-05-01T12:45:58.597-0700)

Same issue on integrated intel graphics card, no text on sign, going back to 1.21.5 works. Seams like sign into is going into sign just not displaying. i.e. do not see the sign text in 25w18a but revert back to 1.21.5 you can see the text that was inputted.

### Comment 7: +merlan #flirora (2025-05-01T23:20:08.548-0700)

I also experience this issue.
GPU info:

```	Graphics card #0 name: Lucienne
	Graphics card #0 vendor: Advanced Micro Devices, Inc. [AMD/ATI] (0x1002)
	Graphics card #0 VRAM (MiB): 258.00
	Graphics card #0 deviceId: 0x164c
	Graphics card #0 versionInfo: unknown```
However, if I use a glow ink sac (but no dye), only the glow is visible:

### Comment 8: Elli Ojasuu (2025-05-02T03:12:39.805-0700)

Hi, my friends and I are also experiencing this issue. Here's proof showing how it looked before and after.

### Comment 9: Shadecoy (2025-05-02T09:05:35.902-0700)

This is marked as resolved, but still not fixed?

### Comment 10: flow_santohyj123 (2025-05-03T14:22:10.304-0700)

Fix Version: Future Update (Next Snapshot)
