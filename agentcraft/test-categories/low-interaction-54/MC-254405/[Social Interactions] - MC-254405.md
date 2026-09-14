# MC-254405: Debug messages aren't prefixed with gray color indicators

**Mojira URL:** [https://bugs.mojang.com/browse/MC-254405](https://bugs.mojang.com/browse/MC-254405)

## Report details

- **Mojira categories:** Social Interactions
- **Project:** MC
- **Issue key:** MC-254405
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-07-20T13:20:00.642-0700
- **Updated:** 2025-03-08T10:38:34.831-0800
- **Resolution date:** 2022-07-21T06:42:32.816-0700
- **Affects versions:** 1.19.1 Pre-release 6
- **Fix versions:** 1.19.1 Release Candidate 2
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-254405.png; MC-254405 - Analysis.png

## Description

The Bug:
Debug messages aren't prefixed with gray color indicators despite being system messages.
The 1.19.1 Pre-release 4 changelog states that
System message are now displayed with a gray color indicator
This means that any messages that are displayed by the system, for example, command feedback, are prefixed with a gray color indicator. Despite messages displayed through using debug functions being considered system messages, they are not prefixed with gray color indicators.
Steps to Reproduce:
- Display a system message in chat by adding a tag to yourself by executing the following command.

```
/tag @s add test
```
- Take note of how the command feedback message is correctly prefixed with a gray color indicator as it's a system message.

- Use any debug function, for example, F3+B.

- Take note as to whether or not debug messages are prefixed with gray color indicators.

Observed Behavior:
Debug messages aren't prefixed with gray color indicators despite being system messages.
Expected Behavior:
Debug messages would be prefixed with gray color indicators.

## Comments (2)

### Comment 1: migrated (2022-07-20T13:20:00.642-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: migrated (2022-07-21T00:39:23.158-0700)

Can confirm
