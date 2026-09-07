# MC-254421: Social interaction messages aren't prefixed with gray color indicators

**Mojira URL:** [https://bugs.mojang.com/browse/MC-254421](https://bugs.mojang.com/browse/MC-254421)

## Report details

- **Mojira categories:** Social Interactions
- **Project:** MC
- **Issue key:** MC-254421
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2022-07-21T06:18:20.719-0700
- **Updated:** 2025-03-08T10:38:15.433-0800
- **Resolution date:** 2022-07-21T13:38:47.811-0700
- **Affects versions:** 1.19.1 Pre-release 6
- **Fix versions:** 1.19.1 Release Candidate 2
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** MC-254421.png; MC-254421 - 1.19.1 Release Candidate 2 (Fixed).png; MC-254421 - Analysis.png

## Description

The Bug:
Social interaction messages aren't prefixed with gray color indicators despite being system messages.
The 1.19.1 Pre-release 4 changelog states that
System message are now displayed with a gray color indicator
This means that any messages that are displayed by the system, for example, command feedback messages, are prefixed with gray color indicators. Despite messages displayed from using the social interaction system being considered system messages, they are not prefixed with gray color indicators.
Steps to Reproduce:
- Join a multiplayer environment with other players on it and display a system message in chat by adding a tag to yourself by executing the following command.

```
/tag @s add test
```
- Take note of how the command feedback message is correctly prefixed with a gray color indicator as it's a system message.

- Open up the social interactions menu, select any player and click the "Hide/Show messages" button beside their name.

- Look at the message that's displayed in chat.

- Take note as to whether or not social interaction messages are prefixed with gray color indicators.

Observed Behavior:
Social interaction messages aren't prefixed with gray color indicators despite being system messages.
Expected Behavior:
Social interaction messages would be prefixed with gray color indicators.

## Comments (2)

### Comment 1: migrated (2022-07-21T06:18:20.719-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: Avoma (2022-07-21T13:38:31.821-0700)

This issue has been fixed in 1.19.1 Release Candidate 2.
