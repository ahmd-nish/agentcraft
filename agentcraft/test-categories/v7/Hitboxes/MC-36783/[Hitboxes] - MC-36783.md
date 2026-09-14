# MC-36783: Item frames/Glow item frames don't change their hitbox if they contain a map

**Mojira URL:** [https://bugs.mojang.com/browse/MC-36783](https://bugs.mojang.com/browse/MC-36783)

## Report details

- **Mojira categories:** Entities; Hitboxes
- **Project:** MC
- **Issue key:** MC-36783
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2013-10-23T08:18:11.154-0700
- **Updated:** 2025-08-19T13:14:58.460-0700
- **Resolution date:** 2025-08-18T04:49:40.505-0700
- **Affects versions:** Minecraft 1.7.1; Minecraft 1.13.2; Minecraft 19w12b; Minecraft 19w13a; Minecraft 19w13b; Minecraft 19w14a; Minecraft 19w14b; Minecraft 1.14 Pre-Release 1; Minecraft 1.14 Pre-Release 2; Minecraft 1.14 Pre-Release 3; Minecraft 1.14 Pre-Release 4; Minecraft 1.14 Pre-Release 5; Minecraft 1.14; Minecraft 1.14.1 Pre-Release 1; Minecraft 1.14.1 Pre-Release 2; Minecraft 1.14.1; Minecraft 1.14.2 Pre-Release 1; Minecraft 1.14.2 Pre-Release 2; Minecraft 1.14.2 Pre-Release 3; Minecraft 1.14.2; Minecraft 1.14.3 Pre-Release 1; Minecraft 1.14.3 Pre-Release 2; Minecraft 1.14.3 Pre-Release 4; Minecraft 1.14.3; Minecraft 1.14.4 Pre-Release 1; Minecraft 1.14.4 Pre-Release 4; Minecraft 1.14.4 Pre-Release 5; Minecraft 1.14.4 Pre-Release 6; 1.14.4 Pre-Release 7; 1.14.4; 19w34a; 19w36a; 19w37a; 19w38b; 19w38a; 19w40a; 19w41a; 19w46b; 1.15 Pre-release 1; 1.15 Pre-release 4; 1.15.1; 1.15.2 Pre-release 2; 1.15.2; 20w06a; 20w07a; 20w09a; 20w10a; 20w11a; 20w12a; 20w13a; 20w13b; 20w14a; 20w15a; 20w16a; 20w21a; 1.16 Pre-release 6; 1.16.1; 20w30a; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4 Pre-release 1; 1.16.4 Pre-release 2; 1.16.4 Release Candidate 1; 1.16.4; 20w45a; 20w46a; 20w48a; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w07a; 21w10a; 21w11a; 21w17a; 1.17; 1.17.1; 1.18; 1.18.1 Release Candidate 2; 1.18.1; 1.18.2; 22w12a; 1.19 Pre-release 3; 1.19; 1.19.2; 1.19.4; 1.20 Release Candidate 1; 1.20; 1.20.1; 1.20.4; 1.21.6
- **Fix versions:** 22w15a; 25w34a
- **Area:** Platform
- **Votes:** 2
- **Watchers:** 3
- **Attachments:** 5
- **Attachment filenames:** 2013-10-23_16.32.11.png; 3.mp4; HitboxesComparison.png; MC-36783.mp4; MC-36783 - 1.19 Pre-release 3.png
- **Issue links:** Duplicate:inward:MC-220316:Item frames have a weird hitbox | Duplicate:inward:MC-146963:Maps in Item Frames do not have the proper hitbox | Relates:inward:MC-250162:Placing a map in an item frame will break any intersecting paintings and item frames with a map inside | Relates:outward:MC-301277:Item frames with maps and paintings cannot share a corner anymore

## Description

If you put a map in a item frame or glow item frame, the map has the size of a whole block, but the hitbox has the size of a normal item frame. If you aim at the top of the map, you can destroy the block on which the item frame with map is placed.
Video evidence: Itemframe Map Wrong Hitbox - Minecraft 19w12b
Steps to reproduce:
1) Give yourself an Item Frame, Map (make sure it's a filled Map. You can make a filled map by right-clicking on Empty Map)
2) Place Item Frame on the wall. Place Map into item Frame.
3) Try to interact in any way with map-filled Item Frame while aiming at corners or edges.
4) Any interaction will fail. You will interact with block behind item frame instead.
UPDATE: Both regular Item Frames and Glow Item Frames are affected.

## Comments (31)

### Comment 1: migrated (2013-10-23T08:18:11.154-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: Ezekiel (2013-11-27T10:23:11.834-0800)

Is this still a concern in the latest Minecraft version 13w48b? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 3: migrated (2014-01-15T10:34:46.479-0800)

This ticket is invalid without the requested information, no response has been received within a reasonable time and we are assuming the issue has been resolved. If you are still experiencing this issue, we can reopen it at your request.

### Comment 4: migrated (2019-03-23T00:00:13.617-0700)

This bug is still present in Minecraft 19w12b (latest snapshot at the moment. Also, it's present in latest stable release 1.13.2, too).
Video evidence: Itemframe Map Wrong Hitbox - Minecraft 19w12b (video is larger than 10MB, therefore linked instead of attached)
Steps to reproduce:
1) Give yourself an Item Frame, Map (make sure it's a filled Map. You can make a filled map by right-clicking on Empty Map)
2) Place Item Frame on the wall. Place Map into item Frame.
3) Try to interact in any way with map-filled Item Frame while aiming at corners or edges.
4) Any interaction will fail. You will interact with block behind item frame instead.

Please reopen and confirm.

### Comment 5: [Mod] violine1101 (2019-03-24T07:40:33.944-0700)

Done and transferred ownership to you upon request as the original reporter has been inactive since this ticket has been created. Feel free to update the ticket.

### Comment 6: GriffinRupe (2019-04-03T16:47:24.139-0700)

Update to include that this issue persists in 19w14a

### Comment 7: migrated (2019-05-07T19:00:36.750-0700)

Also present in Minecraft 1.14.1 Pre-Release 1, but I can't add that version for some reason.

### Comment 8: migrated (2019-06-14T02:44:02.542-0700)

Can't possibly test this due to crash in 1.14.3-pre3 due to bug MC-154499

### Comment 9: migrated (2019-10-02T08:04:57.975-0700)

Also in 19w40a itemframe hitboxes (F3+B) are displayed incorrectly (offset), but that's another unrelated bug.

### Comment 10: GriffinRupe (2019-11-17T12:05:55.190-0800)

Update to include that this issue persists in 19w46b

### Comment 11: migrated (2020-03-03T08:07:38.923-0800)

Still in 1.15.2

### Comment 12: [MOD] Greymagic27 (2020-03-03T08:17:12.169-0800)

1.15.2 is already an affected version.

### Comment 13: migrated (2021-01-20T07:37:54.909-0800)

Also affects glow item frames in 21w03a.

### Comment 14: migrated (2021-01-20T09:38:28.364-0800)

Should I change the title to reflect the fact that it also affects Glow Item Frames or description is enough?

### Comment 15: Avoma (2021-02-06T05:18:27.678-0800)

Can confirm in 21w05b.

### Comment 16: Avoma (2021-02-12T05:46:43.231-0800)

Can confirm in 21w06a.

### Comment 17: Avoma (2021-02-19T03:00:20.529-0800)

Can confirm in 21w07a.

### Comment 18: Avoma (2021-02-20T08:13:58.891-0800)

Video attached.

### Comment 19: migrated (2021-03-21T14:28:57.655-0700)

Can confirm in 21w11a

### Comment 20: Avoma (2021-05-01T07:31:39.827-0700)

Can confirm in 21w17a.

### Comment 21: Avoma (2021-06-22T04:45:24.746-0700)

Can confirm in 1.17.

### Comment 22: ampolive (2021-07-07T13:05:39.467-0700)

Can confirm in 1.17.1.

### Comment 23: Avoma (2021-12-08T05:01:58.389-0800)

Can confirm in 1.18.

### Comment 24: Avoma (2021-12-14T09:43:23.864-0800)

Can confirm in 1.18.1.

### Comment 25: Avoma (2022-03-30T06:39:37.406-0700)

Can confirm in 1.18.2 and 22w12a.

### Comment 26: Avoma (2022-05-25T05:49:37.702-0700)

This issue has reappeared in 1.19 Pre-release 3 very likely due to the fix of MC-250162.

### Comment 27: Avoma (2022-06-13T05:11:59.295-0700)

Can confirm in 1.19.

### Comment 28: Benats (2025-06-18T02:47:00.985-0700)

Can confirm in version 1.21.6

And I would like to take responsibility for this post, as the real owner has not updated it for a long time.

### Comment 29: noBANANA (2025-06-19T04:56:51.975-0700)

Is it possible to get temporary access to this report? To update the description

### Comment 30: [Mod] turbo (2025-06-19T07:48:18.699-0700)

Hi Mario, I’d like to give you ownership of this issue, but I want to be sure I’ve got the right Mario—there are a few with the same name here. Would you mind choosing a more unique name or handle?

### Comment 31: noBANANA (2025-06-19T11:36:26.594-0700)

@turbo
Hey I changed my nickname, hope it suits
