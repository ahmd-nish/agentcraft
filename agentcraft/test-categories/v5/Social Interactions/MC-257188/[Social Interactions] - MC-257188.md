# MC-257188: You aren't prompted that your draft reports will be discarded upon disconnecting from worlds by using the "Title Screen" button within the death screen

**Mojira URL:** [https://bugs.mojang.com/browse/MC-257188](https://bugs.mojang.com/browse/MC-257188)

## Report details

- **Mojira categories:** Social Interactions
- **Project:** MC
- **Issue key:** MC-257188
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-11-03T08:37:47.161-0700
- **Updated:** 2025-03-08T08:17:07.795-0800
- **Resolution date:** 2022-11-11T15:35:14.066-0800
- **Affects versions:** 22w44a; 22w45a
- **Fix versions:** 22w46a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-257188 - Behavior when disconnecting by using the Disconnect button.mp4; MC-257188 - Behavior when disconnecting by using the Title Screen button.mp4

## Description

The Bug:
You aren't prompted that your draft reports will be discarded upon disconnecting from worlds by using the "Title Screen" button within the death screen.
The 22w43a changelog states that:
Draft reports are kept until the player leaves the current server or world
- When leaving, the player will be prompted to either discard or finish and send the report

however, this isn't the case if the player disconnects from worlds by using the "Title Screen" button on the death screen. If players were to click the "Disconnect" button within the game menu, they would be prompted that their draft reports will be discarded upon leaving worlds, which is the correct and expected behavior.
To get a visual understanding of this issue, I've attached two videos that show the difference in behavior depending on if you disconnect the world by using the "Disconnect" button within the game menu, or the "Title Screen" button within the death screen.
Steps to Reproduce:
- Join a multiplayer world with another player online and get them to type in chat.

- Begin making a chat report for any of their messages and save the report as a draft.

- Hit the ESC key, click on the "Disconnect" button, and take note of how you're prompted that your draft report will be lost if you leave the world.

- Click on the "Continue Editing" button, then the "Back" button, and finally the "Save as Draft" button to save your report as a draft once again.

- Run the "/kill" command and leave the world by clicking on the "Title Screen" button within the death screen.

- Take note of how you aren't prompted that your draft reports will be discarded upon disconnecting from worlds by using the "Title Screen" button within the death screen.

Observed Behavior:
You aren't prompted that your draft reports will be discarded.
Expected Behavior:
You would be prompted that your draft reports will be discarded.

## Comments (1)

### Comment 1: migrated (2022-11-03T08:37:47.161-0700)

This comment contained multiple image attachments (2), please login to view the attachments.
