# MC-251968: /execute running chat related commands logs "Received chat packet without valid signature" warning

**Mojira URL:** [https://bugs.mojang.com/browse/MC-251968](https://bugs.mojang.com/browse/MC-251968)

## Report details

- **Mojira categories:** Social Interactions
- **Project:** MC
- **Issue key:** MC-251968
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2022-05-20T03:26:58.985-0700
- **Updated:** 2025-04-30T07:45:50.339-0700
- **Resolution date:** 2022-06-29T06:56:23.098-0700
- **Affects versions:** 1.19 Pre-release 1
- **Fix versions:** 1.19 Pre-release 3
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** MC-251968.png

## Description

Steps to reproduce
1. Summon a creeper
2. Run /execute as @e[type=creeper] run say Hi from chat screen
3. Check the logs on client
Expected result
No warning gets logged.
Actual result
A warning gets logged: Received chat packet without valid signature from Creeper
Note that unlike MC-251872 no warning gets logged on the server.

## Comments (6)

### Comment 1: migrated (2022-05-20T03:26:58.985-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: ampolive (2022-05-20T03:28:51.607-0700)

Thank you for your report!
We're tracking this issue in MC-251872, so this ticket is being resolved and linked as a duplicate.
If you would like to add a vote and any extra information to the main ticket it would be appreciated.
If you haven't already, you might like to make use of the search feature to see if the issue has already been mentioned.
Quick Links:
📓 Bug Tracker Guidelines – 💬 Community Support – 📧 Mojang Support
📓 Project Summary – ✍️ Feedback and Suggestions – 📖 Game Wiki

### Comment 3: migrated (2022-05-20T03:33:56.616-0700)

Doesn't seem the same, as that's about using the selector in the /say command, not when running a selector-less say command from another entity.

### Comment 4: ampolive (2022-05-20T03:40:48.012-0700)

It's probably the same core issue, but yes, technically you're right. Confirmed.

### Comment 5: apple502j (2022-05-20T04:00:38.434-0700)

The observed behavior and the root cause are both different - no warning gets logged server-side, and the root cause is that the server uses the chat message packet for non-player sent messages (which has signature check) instead of the game message packet (does not have a signature).

### Comment 6: Avoma (2022-05-22T01:32:21.609-0700)

If not a duplicate, then this definitely would relate to MC-251872.
