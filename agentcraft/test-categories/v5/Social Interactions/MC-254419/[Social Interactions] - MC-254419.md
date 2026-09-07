# MC-254419: Local game hosting messages aren't prefixed with gray color indicators

**Mojira URL:** [https://bugs.mojang.com/browse/MC-254419](https://bugs.mojang.com/browse/MC-254419)

## Report details

- **Mojira categories:** Social Interactions
- **Project:** MC
- **Issue key:** MC-254419
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2022-07-21T05:28:09.194-0700
- **Updated:** 2025-03-08T10:38:13.461-0800
- **Resolution date:** 2022-07-21T13:28:07.565-0700
- **Affects versions:** 1.19.1 Pre-release 6
- **Fix versions:** 1.19.1 Release Candidate 2
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-254419.png; MC-254419 - Analysis.png

## Description

The Bug:
Local game hosting messages aren't prefixed with gray color indicators despite being system messages.
The 1.19.1 Pre-release 4 changelog states that
System message are now displayed with a gray color indicator
This means that any messages that are displayed by the system, for example, command feedback messages, are prefixed with gray color indicators. Despite messages displayed through opening a world to LAN (when not using the "/publish" command) being considered system messages, they are not prefixed with gray color indicators.
Steps to Reproduce:
- Join a singleplayer world and display a system message in chat by adding a tag to yourself by executing the following command.

```
/tag @s add test
```
- Take note of how the command feedback message is correctly prefixed with a gray color indicator as it's a system message.

- Open your world to LAN by pressing ESC > Open to LAN > Start LAN World and look at the message displayed in chat.

- Take note as to whether or not local game hosting messages are prefixed with gray color indicators.

Observed Behavior:
Local game hosting messages aren't prefixed with gray color indicators despite being system messages.
Expected Behavior:
Local game hosting messages would be prefixed with gray color indicators.

## Comments (2)

### Comment 1: migrated (2022-07-21T05:28:09.194-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: Avoma (2022-07-21T13:27:46.371-0700)

This issue has been fixed in 1.19.1 Release Candidate 2.
