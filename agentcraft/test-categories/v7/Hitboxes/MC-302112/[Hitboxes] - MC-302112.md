# MC-302112: Posed mannequins don't use the correct hitbox

**Mojira URL:** [https://bugs.mojang.com/browse/MC-302112](https://bugs.mojang.com/browse/MC-302112)

## Report details

- **Mojira categories:** Hitboxes
- **Project:** MC
- **Issue key:** MC-302112
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2025-09-16T07:18:57.327-0700
- **Updated:** 2026-03-11T03:43:41.818-0700
- **Resolution date:** 2025-09-18T01:11:58.058-0700
- **Affects versions:** 1.21.9 Pre-Release 1
- **Fix versions:** 1.21.9 Pre-Release 2
- **Area:** Platform HC
- **Votes:** 7
- **Watchers:** 0
- **Attachments:** 3
- **Attachment filenames:** 2025-09-16_16.16.53-20250916-141653.png; 2025-09-16_16.17.01-20250916-141701.png; 2025-09-16_16.17.36-20250916-141736.png

## Description

When mannequin is uses pose of swimming, fall flying or crouching, it’s bounding box is not correct (using default / standing one).
Used commands:

```
/summon minecraft:mannequin
/data modify entity @n[type=minecraft:mannequin] pose set value crouching
```

## Comments (2)

### Comment 1: Patbox (2025-09-16T07:18:58.062-0700)

This comment contained an image attachment, please login to view the attachment.

This comment contained an image attachment, please login to view the attachment.

This comment contained an image attachment, please login to view the attachment.

### Comment 2: SightDash (2025-09-16T14:35:57.278-0700)

Can confirm. Also it seems that the sleeping pose is fine.
