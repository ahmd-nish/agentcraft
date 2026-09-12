# MC-254417: Screenshot messages aren't prefixed with gray color indicators

**Mojira URL:** [https://bugs.mojang.com/browse/MC-254417](https://bugs.mojang.com/browse/MC-254417)

## Report details

- **Mojira categories:** Social Interactions
- **Project:** MC
- **Issue key:** MC-254417
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2022-07-21T05:05:06.161-0700
- **Updated:** 2025-03-08T10:38:19.722-0800
- **Resolution date:** 2022-07-21T13:27:57.091-0700
- **Affects versions:** 1.19.1 Pre-release 6
- **Fix versions:** 1.19.1 Release Candidate 2
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-254417.png; MC-254417 - Analysis.png

## Description

The Bug:
Screenshot messages aren't prefixed with gray color indicators despite being system messages.
The 1.19.1 Pre-release 4 changelog states that
System message are now displayed with a gray color indicator
This means that any messages that are displayed by the system, for example, command feedback messages, are prefixed with gray color indicators. Despite messages displayed through using the screenshot button being considered system messages, they are not prefixed with gray color indicators.
Steps to Reproduce:
- Display a system message in chat by adding a tag to yourself by executing the following command.

```
/tag @s add test
```
- Take note of how the command feedback message is correctly prefixed with a gray color indicator as it's a system message.

- Take a screenshot by pressing the "Take Screenshot" button (F2 by default).

- Take note as to whether or not screenshot messages are prefixed with gray color indicators.

Observed Behavior:
Screenshot messages aren't prefixed with gray color indicators despite being system messages.
Expected Behavior:
Screenshot messages would be prefixed with gray color indicators.

## Comments (2)

### Comment 1: migrated (2022-07-21T05:05:06.161-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: markderickson (2022-07-21T13:27:57.089-0700)

This is fixed in 1.19.1 Release Candidate 2.
