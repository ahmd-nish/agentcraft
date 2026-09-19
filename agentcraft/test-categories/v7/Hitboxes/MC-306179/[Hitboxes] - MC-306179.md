# MC-306179: The hitbox of baby foxes is offset from their model when sleeping

**Mojira URL:** [https://bugs.mojang.com/browse/MC-306179](https://bugs.mojang.com/browse/MC-306179)

## Report details

- **Mojira categories:** Hitboxes; Mob behaviour
- **Project:** MC
- **Issue key:** MC-306179
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2026-02-03T08:14:06.136-0800
- **Updated:** 2026-04-11T10:03:25.838-0700
- **Resolution date:** 2026-02-19T13:47:03.877-0800
- **Affects versions:** 26.1 Snapshot 6
- **Fix versions:** 26.1 Snapshot 8
- **Area:** Expansion A
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2026-02-03_14.29.43-20260203-192943.png; 2026-02-04_00.13.06.png

## Description

The hitbox of baby fox looks strange.
It looks far away from where the fox is.

## Comments (5)

### Comment 1: Automation for Jira (2026-02-03T08:14:16.183-0800)

Thank you for helping us improve Minecraft! We saved your files:

### Comment 2: kyleisNOTmyname (2026-02-03T11:30:33.272-0800)

Can confirm as of 26.1-snapshot-6

Reproduce with:
/summon minecraft:fox ~ ~ ~ {Age:-24000,Sleeping:1b}

### Comment 3: kyleisNOTmyname (2026-02-13T16:29:10.475-0800)

Reproduced in 26.1-snapshot-7

### Comment 4: MR (2026-02-17T09:22:30.351-0800)

It have been fixed in 26.1-snapshot-8, though the article didn’t mention.

### Comment 5: kyleisNOTmyname (2026-02-17T18:16:43.884-0800)

Can confirm that it was fixed.
