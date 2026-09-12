# MC-307140: Chat messages can no longer be reported if the chat is enabled

**Mojira URL:** [https://bugs.mojang.com/browse/MC-307140](https://bugs.mojang.com/browse/MC-307140)

## Report details

- **Mojira categories:** Social Interactions
- **Project:** MC
- **Issue key:** MC-307140
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2026-03-30T04:28:41.121-0700
- **Updated:** 2026-04-01T06:30:37.498-0700
- **Resolution date:** 2026-03-31T02:34:39.623-0700
- **Affects versions:** 26.1
- **Fix versions:** 26.1.1 Release Candidate 1
- **Area:** Platform HC
- **Votes:** 2
- **Watchers:** 2
- **Attachments:** 1
- **Attachment filenames:** image-20260330-112856.png

## Description

The bug
You cannot report players' chat messages if you have the chat enabled, as the "Chat Messages" button is disabled with the tooltip "This player can't be reported because chat is disabled or blocked". Setting the chat to "Commands Only" or "Hidden" enables the button; the behavior is simply inverted.
Steps to reproduce
- Join an online mode server with two accounts. Ensure that the chat is enabled in the client settings.

- Send a message from one account.

- On the other account, open the Social Interactions menu and click on the "Report player" button. The "Report Player" screen will open.

- Move your mouse cursor to the "Chat Messages" button.

Observed behavior
The button will be disabled, and a tooltip will be shown stating that the chat is disabled or blocked.
Expected behavior
The button would be enabled, allowing the player to report the other player's chat message.

## Comments (3)

### Comment 1: MrKinau (2026-03-30T04:28:59.768-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: MrKinau (2026-03-30T04:45:23.627-0700)

```boolean chatDisabledOrBlocked = minecraft.player.chatAbilities().canReceivePlayerMessages() || socialManager.isBlocked(id);```
should be obvious whats wrong here

### Comment 3: Luke Murray (2026-04-01T06:30:37.498-0700)

Surely this could’ve been a patch within the same version no?
I’m aware all mods are third party and unassociated but everything that just came out for 26.1 now has to be updated for 26.1.1
