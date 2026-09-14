# MC-240534: Clicking a JFR link copies full server-side path to clipboard

**Mojira URL:** [https://bugs.mojang.com/browse/MC-240534](https://bugs.mojang.com/browse/MC-240534)

## Report details

- **Mojira categories:** Commands; Dedicated Server
- **Project:** MC
- **Issue key:** MC-240534
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2021-11-03T15:07:17.802-0700
- **Updated:** 2025-04-29T21:34:04.390-0700
- **Resolution date:** 2021-11-05T03:37:40.931-0700
- **Affects versions:** 21w44a
- **Fix versions:** 1.18 Pre-release 1
- **Watchers:** 1
- **Attachments:** 0
- **Issue links:** Bonfire Testing:inward:MC-240502:JFR links copy the path to the report when clicked, inconsistent with other functions

## Description

Discovered while testing .
The bug
Stopping a JFR report and clicking the link sent in the chat copies the path of the JFR report to the clipboard. However, this is copied when connected to an external server, exposing the full path of the server to anyone with the ability to run the /jfr stop command.
For testing, I set up a Minecraft server on an Ubuntu server, and when clicking the link sent in the chat after stopping the jfr profiling (on another device, just to make sure this was an issue), the following was copied to the clipboard:

```
/home/ubuntu/mcservers/21w44a/debug/server-2021-11-03-214926.jfr
```
This is full path and could potentially expose usernames or other personal information.
How to reproduce
- Create a server

- Connect to the server

- Run /jfr start

- Run /jfr stop

- Click the link in the chat to copy the path to your clipboard

- Paste the link somewhere so that you can view it
 The full path of the server is visible

Observed behavior
The full path to the server is copied to the clipboard, even though the server is hosted from a different machine.
Expected behavior
The full path of the server would not be copied to the clipboard, and instead the /jfr stop command would not provide a link at all if the report was created on a server.

## Comments (1)

### Comment 1: MMK21 (2021-11-04T01:20:06.695-0700)

Can confirm.
