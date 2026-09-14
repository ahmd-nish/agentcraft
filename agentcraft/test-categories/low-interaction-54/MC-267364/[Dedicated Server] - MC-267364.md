# MC-267364: Teleporting in the air is considered flying by server

**Mojira URL:** [https://bugs.mojang.com/browse/MC-267364](https://bugs.mojang.com/browse/MC-267364)

## Report details

- **Mojira categories:** Commands; Dedicated Server
- **Project:** MC
- **Issue key:** MC-267364
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2023-12-18T03:33:45.725-0800
- **Updated:** 2025-10-09T01:32:44.559-0700
- **Resolution date:** 2025-10-09T01:32:44.505-0700
- **Affects versions:** 1.20.4; 23w51b; 1.20.6; 24w21b; 1.21; 1.21.4
- **Fix versions:** 25w41a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** MC-267364.mp4

## Description

When being teleported into the air, a server with flying disabled will kick you for flying in survival/adventure mode.
Steps to reproduce:
- Create a server with allow-flight=false

- Enter the server

- Use

```
/gamemode survival
/setblock ~ ~-1 ~ chain_command_block{auto:1b,Command:"teleport @p ~ ~3 ~"}
/setblock ~ ~ ~ repeating_command_block[facing=down]{auto:1b,Command:"teleport @p ~ 0 ~"}
```

- Wait for a few seconds
->  Get kicked for flying

Expected behavior:
Since it's a command the server (via functions or command blocks) is running, the "fly timer" should be reset.

## Comments (5)

### Comment 1: migrated (2023-12-18T03:33:45.725-0800)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: Neliz (2024-01-14T12:54:57.538-0800)

I can confirm this in 1.20.4 and attached a video demonstrating the bug.

### Comment 3: COMETC2021A1 (2024-05-19T09:54:25.747-0700)

This happens since 1.8.9 or earlier.

### Comment 4: Lunarian (2024-05-27T00:33:02.597-0700)

Can confirm in 1.20.6 & 24w21b.

Requesting ownership (the op is marked as inactive).

### Comment 5: Dhranios (2025-01-02T03:17:57.029-0800)

Still in 1.21.4.
