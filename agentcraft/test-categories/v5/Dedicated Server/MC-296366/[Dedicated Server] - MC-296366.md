# MC-296366: Kicked for flying while flying happy ghast

**Mojira URL:** [https://bugs.mojang.com/browse/MC-296366](https://bugs.mojang.com/browse/MC-296366)

## Report details

- **Mojira categories:** Dedicated Server
- **Project:** MC
- **Issue key:** MC-296366
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2025-04-08T07:54:39.261-0700
- **Updated:** 2025-07-26T13:34:43.272-0700
- **Resolution date:** 2025-04-15T00:40:18.123-0700
- **Affects versions:** 25w15a
- **Fix versions:** 25w16a
- **Area:** Expansion A
- **Watchers:** 3
- **Attachments:** 1
- **Attachment filenames:** grafik-20250408-145305.png
- **Issue links:** Duplicate:inward:MC-296473:Kicked from happy ghast for flying

## Description

Steps to Reproduce:
- Join a server with allow-flight in server.properties set to false (default).

- Harness a happy ghast and fly around on it (you do not have to be in Survival).

- After a few seconds, you should get kicked for flying.

Observed Results:
The player gets kicked for the reason “Flying is not enabled on this server“ and the console shows “Player was kicked for floating a vehicle too long!“.
Expected Results:
The player would not be kicked.

## Comments (7)

### Comment 1: Phoenix3000 (2025-04-08T07:54:40.013-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: Nathan (2025-04-08T08:15:02.483-0700)

Thats normal not a bug, set it to true.

### Comment 3: Phoenix3000 (2025-04-08T09:00:34.483-0700)

I think this is a bug, or at least something that should be changed, as allow-flight is set to true by default. The Happy Ghast allows you to fly on an entity, it's a game mechanic and shouldn't be disabled by a setting that's there to kick players who move incorrectly.

### Comment 4: [MCQA] Zgajak (2025-04-09T04:22:21.021-0700)

Hi!
Can you please use this template for this issue?
Steps to Reproduce:
-

-

-

Observed Results:
(Briefly describe what happens)
Expected Results:
(Briefly describe what should happen)
This ticket will automatically reopen when you reply.

### Comment 5: Viradex (2025-04-09T13:37:26.130-0700)

I could successfully reproduce this bug consistently. Here is the requested information.
Steps to Reproduce:
- Join a server with allow-flight in server.properties set to false.

- Harness a Happy Ghast and fly around on it (you do not have to be in Survival).

- After a few seconds, you should get kicked for flying.

Observed Results:
The player gets kicked for the reason “Flying is not enabled on this server“.
Expected Results:
The player would not be kicked.

### Comment 6: Jivan (2025-07-26T11:34:43.698-0700)

Why has this ticket been marked as Fixed? Is this supposed to be Fixed or Won’tFix? Issue is still present in 1.21.8.

### Comment 7: [MOD] Greymagic27 (2025-07-26T13:34:43.272-0700)

If you’re still experiencing the issue on the latest release, please open a new bug report with a video and steps to reproduce.
