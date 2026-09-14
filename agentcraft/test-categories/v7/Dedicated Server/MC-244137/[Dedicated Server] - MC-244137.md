# MC-244137: The option "level-seed" is not present in server.properties by default

**Mojira URL:** [https://bugs.mojang.com/browse/MC-244137](https://bugs.mojang.com/browse/MC-244137)

## Report details

- **Mojira categories:** Dedicated Server
- **Project:** MC
- **Issue key:** MC-244137
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-12-03T04:53:33.111-0800
- **Updated:** 2025-04-10T12:25:54.134-0700
- **Resolution date:** 2024-07-29T02:43:19.809-0700
- **Affects versions:** 1.18; 1.18.1 Pre-release 1; 1.18.1
- **Fix versions:** 1.18.2 Pre-release 1
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** server.properties
- **Issue links:** Duplicate:inward:MC-229621:Generator Settings are not present in properties file by default | Duplicate:inward:MC-227819:server.properties not generating some lines | Duplicate:inward:MC-242343:level-seed missing from server.properties | Duplicate:inward:MC-244199:The parameter "Level-seed=" don't exist in the server.properties file

## Description

The bug
In the server.properties file level-seed isn't there and isn't generating when turning on server.
Adding the line manually allows the server to generate a world with a custom seed.
How to reproduce
- Start a server, and wait for the files to generate

- Read through server.properties
 No line for the level seed exists

Expected behavior
The level-seed line would be present in the server.properties file by default, but would be left blank.

## Comments (1)

### Comment 1: migrated (2021-12-03T04:53:33.111-0800)

This comment contained an image attachment, please login to view the attachment.
