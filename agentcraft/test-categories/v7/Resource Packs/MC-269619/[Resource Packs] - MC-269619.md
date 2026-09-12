# MC-269619: Scroller in Telemetry Data screen renders translucent pixels as opaque, unlike elsewhere

**Mojira URL:** [https://bugs.mojang.com/browse/MC-269619](https://bugs.mojang.com/browse/MC-269619)

## Report details

- **Mojira categories:** Rendering; Resource Packs; Textures and models
- **Project:** MC
- **Issue key:** MC-269619
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2024-03-20T08:34:35.804-0700
- **Updated:** 2025-04-29T10:00:31.641-0700
- **Resolution date:** 2024-04-15T01:36:39.604-0700
- **Affects versions:** 24w11a; 24w12a; 24w13a; 24w14a
- **Fix versions:** 1.20.5 Pre-Release 2
- **Area:** Platform
- **Labels:** translucency-nonfunctional
- **Watchers:** 1
- **Attachments:** 11
- **Attachment filenames:** 2024-03-20_15.23.20.png; 2024-03-20_15.23.27.png; 2024-03-20_15.23.31.png; 2024-03-20_15.23.35.png; 2024-03-20_15.23.37.png; 2024-03-20_15.23.42.png; 2024-03-20_15.23.45.png; 2024-03-20_15.23.55.png; 2024-03-20_15.23.56.png; 2024-03-20_15.23.57.png; transparent-scroller-test-24w11a-v1.0.zip
- **Issue links:** Relates:outward:MC-109447:Inconsistency in transparency of GUI PNG files - only some can be transparent + hover-bugs

## Description

More loosely relates to these issues:  MC-145821
The bug
If scroller.png is given a translucent texture, it will correctly render as translucent in most contexts. However, in the Telemetry Data menu, it renders completely opaque, which is notably inconsistent.
How to reproduce
- Download and apply the attached resource pack

- Navigate through menus that have a scroll bar

- Go to the "Telemetry Data" menu

Expected results
All places that use the scroller would render it as translucent.
Actual results
Most do, but Telemetry Data has it as opaque for some reason.

## Comments (2)

### Comment 1: migrated (2024-03-20T08:34:35.804-0700)

This comment contained multiple image attachments (11), please login to view the attachments.

### Comment 2: BugTracker_ (2024-04-11T19:50:29.857-0700)

Affects 1.20.5 pre-release.
