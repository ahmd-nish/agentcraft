# MC-279233: Shulker boxes drop their contents when broken

**Mojira URL:** [https://bugs.mojang.com/browse/MC-279233](https://bugs.mojang.com/browse/MC-279233)

## Report details

- **Mojira categories:** Block states; Loot tables
- **Project:** MC
- **Issue key:** MC-279233
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2025-01-08T08:53:49.217-0800
- **Updated:** 2025-05-29T09:05:25.021-0700
- **Resolution date:** 2025-01-15T01:47:33.084-0800
- **Affects versions:** 25w02a
- **Fix versions:** 25w03a
- **Area:** Expansion A
- **Game mode:** Survival
- **Labels:** inventory; item; loot_table
- **Watchers:** 2
- **Attachments:** 2
- **Attachment filenames:** 2025-01-08 17-51-43.mp4; Screen Recording 2025-01-10 124015.mp4
- **Issue links:** Relates:inward:MC-279211:Shulker boxes both keep and drop their contents upon being broken via certain methods causing item duplication | Duplicate:inward:MC-279244:Shulker Box not retaining items when broken | Duplicate:inward:MC-279246:Shulker Box drops items inside when mined | Duplicate:inward:MC-279289:Shulker Boxes won't keep items | Duplicate:inward:MC-279324:Shulker Boxes dont drop correctly when broken | Duplicate:inward:MC-279333:Shulker Box Bug | Duplicate:inward:MC-279338:Items drop from shulker box when broken. | Duplicate:inward:MC-279347:Shulker dupes items. and drops all items within the shulker on the ground | Duplicate:inward:MC-279348:Shulker Boxes drop all their items when broken with a Pickaxe | Duplicate:inward:MC-279369:Breaking the shulker box spilled out all of its contents | Duplicate:inward:MC-279374:Breaking a shulker box drops items | Duplicate:inward:MC-279375:shulkers are useless | Duplicate:inward:MC-279388:Shulker Boxes do not keep their contents when broken | Duplicate:inward:MC-279404:Shulker Box Drops Items upon breaking in snaphot 1.21 25w02a | Duplicate:inward:MC-279419:Shulker Box Drops Contents | Duplicate:inward:MC-279421:Shulker Box drops the items that were inside it when it breaks. | Duplicate:inward:MC-279448:Shulker acting like broken chests | Duplicate:inward:MC-279469:Shulker isn't holding items. | Duplicate:inward:MC-279470:Shulker Boxes

## Description

The bug:
Shulker boxes drop their content on break
Steps to reproduce:
- Obtain a shulker box

- Place the shulker box

- Open it and fill it with random content

- Break the shulker box in survival with proper tool

Observed behavior:
The shulker box drops all its content and the shulker box item remains empty
Expected behavior:
The shulker box should keep it's content when broke

## Comments (6)

### Comment 1: migrated (2025-01-08T08:53:49.217-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: TheBoy358 (2025-01-08T09:18:17.455-0800)

Can confirm.

### Comment 3: [Mod] ManosSef (2025-01-11T13:45:47.143-0800)

There is no need to add confirmation comments on a report that's already confirmed. Doing so only clutters the comment section and creates unnecessary emails for all people watching the issue. I've cleaned up the comments section a bit.

### Comment 4: migrated (2025-01-12T03:24:28.164-0800)

This had some odd bugs too. If you tries to break the Shulker with either Piston or explosives, it will drops all its content, but it also kept its content inside at the same time, effectively duping the items.
https://twitter.com/abc_kuma1025/status/1877296801922900386?s=19

### Comment 5: migrated (2025-01-15T01:42:45.473-0800)

In the new snapshot where there's custom pig variants, and in this day that i just commented, it still hasn't patched.

### Comment 6: Dhranios (2025-01-15T01:47:33.084-0800)

It's marked as fixed for the next snapshot, which'll probably release today. Days never matters for game bugs, only versions.
