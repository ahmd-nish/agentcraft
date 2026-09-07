# MC-214885: Beacon beam only render 256 blocks from source

**Mojira URL:** [https://bugs.mojang.com/browse/MC-214885](https://bugs.mojang.com/browse/MC-214885)

## Report details

- **Mojira categories:** Beacon
- **Project:** MC
- **Issue key:** MC-214885
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-02-10T12:10:41.148-0800
- **Updated:** 2025-04-10T12:36:56.069-0700
- **Resolution date:** 2024-06-01T03:27:20.255-0700
- **Affects versions:** 21w06a
- **Fix versions:** 21w07a
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2021-02-10_16.26.25.png; 2021-02-10_16.26.27.png; 2021-02-10_16.30.30.png; 2021-02-10_16.30.31.png
- **Issue links:** Duplicate:inward:MC-214971:Beacon beams don't render at high Y levels when placed at low Y levels | Relates:outward:MC-151747:Beacon beams no longer stop at build limit height

## Description

The bug
Beacon beam can only extend 256 blocks, despite the new height of -64 to 320. To replicate this, place one beacon above Y=64, and one below Y=64, and then fly up. Once you get 256 blocks away from the lower beacon, the beam will disappear, while the other beam remains.

## Comments (3)

### Comment 1: migrated (2021-02-10T12:10:41.148-0800)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: markderickson (2021-02-10T16:35:25.523-0800)

This relates to .

### Comment 3: migrated (2021-02-11T23:32:52.991-0800)

Added pictures. The quadruple beam is from a beacon placed at bedrock. At y=192, it is no longer visible. A beacon placed at y=192 will continue above the built limit.
