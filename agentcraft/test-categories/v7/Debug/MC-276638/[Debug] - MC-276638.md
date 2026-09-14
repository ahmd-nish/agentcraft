# MC-276638: The server console or LAN game output spammed with "PLAYER moved too quickly!" after a player dies and respawns

**Mojira URL:** [https://bugs.mojang.com/browse/MC-276638](https://bugs.mojang.com/browse/MC-276638)

## Report details

- **Mojira categories:** Debug; Performance; Player
- **Project:** MC
- **Issue key:** MC-276638
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-09-12T07:27:31.851-0700
- **Updated:** 2025-04-26T16:46:07.365-0700
- **Resolution date:** 2024-09-23T06:48:35.832-0700
- **Affects versions:** 24w37a; 24w38a
- **Fix versions:** 24w39a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** 2024-09-15_20_53_21-1_18t-24w37a.zip
- **Issue links:** Relates:outward:MC-248231:The server console is sometimes spammed with "PLAYER moved too quickly!" after a player switches dimensions or teleports long distances

## Description

The bug
The server console or LAN game output spammed with "PLAYER moved too quickly!" after a player dies and respawns.
Server console

```
[22:14:14 INFO]: [Les3awe: Killed Les3awe]
[22:14:15 WARN]: Les3awe moved too quickly! -11.28453520303416,-2.116501367928123,-62.12911357204942
[22:16:31 INFO]: Les3awe was killed
[22:16:31 INFO]: [Les3awe: Killed Les3awe]
[22:16:39 WARN]: Les3awe moved too quickly! -46.13969726382189,-14.112930305474706,-93.73915427829289
[22:16:46 INFO]: Les3awe was killed
[22:16:46 INFO]: [Les3awe: Killed Les3awe]
[22:16:47 WARN]: Les3awe moved too quickly! -35.19694635972356,-3.243413216081791,-13.679489466242739
[22:16:47 WARN]: Les3awe moved too quickly! -35.19694635972356,-3.243413216081791,-13.679489466242739
[22:16:51 INFO]: Les3awe was killed
[22:16:51 INFO]: [Les3awe: Killed Les3awe]
[22:16:52 WARN]: Les3awe moved too quickly! 5.169859688363443,-2.8685985614118863,-33.594936090566605
[22:16:52 WARN]: Les3awe moved too quickly! 5.169859688363443,-2.8685985614118863,-33.594936090566605
[22:16:52 WARN]: Les3awe moved too quickly! 5.169859688363443,-2.8685985614118863,-33.594936090566605
[22:16:52 WARN]: Les3awe moved too quickly! 5.169859688363443,-2.8685985614118863,-33.594936090566605
[22:16:52 WARN]: Les3awe moved too quickly! 5.169859688363443,-2.8685985614118863,-33.594936090566605
[22:16:52 WARN]: Les3awe moved too quickly! 5.169859688363443,-2.8685985614118863,-33.594936090566605
[22:16:52 WARN]: Les3awe moved too quickly! 5.169859688363443,-2.8685985614118863,-33.594936090566605
```
Steps to reproduce
- Join the official vanilla dedicated server.

- Move 3 chunks away from the respawn point. No need to use the teleport command.

- Use the following command:

```
/kill @p
```

- Click the "Respawn" button.

- Noticed some spam on the server console or LAN game output.

## Comments (3)

### Comment 1: migrated (2024-09-12T07:27:31.851-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: v-aalidoust (2024-09-13T00:09:41.713-0700)

Could you give us the computer specs? And test whether the issue happens with just the teleport command?

### Comment 3: [Mod]Les3awe (2024-09-13T03:13:41.614-0700)

@, the issue can't be reproduced using only the teleport command.
