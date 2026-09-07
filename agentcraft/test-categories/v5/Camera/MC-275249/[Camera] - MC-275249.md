# MC-275249: "FOV Effects" slider incorrectly modifying zoom values on the spyglass

**Mojira URL:** [https://bugs.mojang.com/browse/MC-275249](https://bugs.mojang.com/browse/MC-275249)

## Report details

- **Mojira categories:** Camera
- **Project:** MC
- **Issue key:** MC-275249
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2024-08-15T10:07:29.958-0700
- **Updated:** 2025-04-26T16:08:37.692-0700
- **Resolution date:** 2024-08-19T06:19:06.983-0700
- **Affects versions:** 24w33a
- **Fix versions:** 24w34a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 10
- **Attachment filenames:** 1.21.1 no zoom.png; 1.21.1 zoom.png; 1.21.1 zoom slider set to 0.png; 1.21.1 zoom slider set to 0-1.png; 2024-08-15_12.13.30.png; 2024-08-15_12.13.54.png; 24w33a no zoom.png; 24w33a zoom.png; 24w33a zoom slider set to 0.png; 24w33a zoom slider set to 0-1.png
- **Issue links:** Duplicate:inward:MC-275305:Spyglass does not work properly (zoom bugged) | Duplicate:inward:MC-275371:Spyglass not zooming in | Duplicate:inward:MC-275572:Spy glass effect is affected by FOV Effects option

## Description

The zoom effect is being effected by the "FOV Effects" slider inside Video settings, which it did not do in previous versions.
Steps to reproduce:
- Adjust the "Video Settings > FOV Effects" slider to 100% and try zoom in with the spyglass

- Adjust "Video Settings > FOV Effects" slider to anything lower than 100%

- Zoom in using the spyglass.

Observed results:
Zoom is directly affected by the FOV Effects slider, such that setting it to 0% causes the spyglass to not zoom in at all.
Expected results:
Spyglass zoom should be unaffected by the FOV Effects slider (as in previous versions).
Everything I have tested has been in vanilla versions of the game, no mods used.
The specific example here that I am using to compare zooms is just me creating a 4 block wide gap and zooming in from one side to the other to directly compare how the block appears. I have attached how setting FOV Effects to 0 appears in 1.21.1 and how it appears in 24w33a. One of my versions is set to windowed, as screenshotting with windows doesn't work properly in 1.21.1, but swapping to full-screen does not change the results.
1.21.1:
24w33a:

## Comments (5)

### Comment 1: migrated (2024-08-15T10:07:29.958-0700)

This comment contained multiple image attachments (10), please login to view the attachments.

### Comment 2: [Mod] Jingy (2024-08-15T10:14:35.388-0700)

I cannot reproduce this:

### Comment 3: [Mod] Jingy (2024-08-15T10:15:19.925-0700)

Are you on vanilla? If so; please clarify if I have reproduced the issue incorrectly.

### Comment 4: Jarl-Penguin (2024-08-15T13:20:49.462-0700)

I cannot reproduce this either. Please include the following information to help us understand your problem:
Steps to Reproduce:
1. (Explain what needs to be done for the issue to happen)
2.
3.
Observed Results:
(Briefly describe what happens)
Expected Results:
(Briefly describe what should happen)
Please also attach any needed commands, data packs, resource packs, screenshots, videos, or worlds needed to help reproduce this issue.
Refer to the Bug Tracker Guidelines for more information about how to write helpful bug reports. Bug reports with insufficient information may be closed as Incomplete.
This issue is being temporarily resolved as Awaiting Response. Once the requested information has been delivered, the report will be reopened automatically.
Quick Links:
📓 Bug Tracker Guidelines – 💬 Community Support – 📧 Mojang Support (Technical Issues) – 📧 Microsoft Support (Account Issues)
📓 Project Summary – ✍️ Feedback and Suggestions – 📖 Game Wiki

### Comment 5: H_CORP (2024-08-15T14:25:40.243-0700)

Hello
I have found what is causing this issue.
The zoom effect is being effected by the "FOV Effects" slider inside the video settings, which it did not do in previous versions. So:
Steps to reproduce:
1. Adjust the "Video Settings > FOV Effects" slider to 100% and try zoom in with the spyglass
2. Adjust "Video Settings > FOV Effects" slider to anything lower than 100%
3. Zoom in using the spyglass.
Observed results:
Zoom is directly affected by the FOV Effects slider, such that setting it to 0% causes the spyglass to not zoom in at all.
Expected results:
Spyglass zoom should be unaffected by the FOV Effects slider (as in previous versions).
Everything I have tested has been in vanilla versions of the game, no mods used.
The specific example here that I am using to compare zooms is just me creating a 4 block wide gap and zooming in from one side to the other to directly compare how the block appears. I have attached how setting FOV Effects to 0 appears in 1.21.1 and how it appears in 24w33a. One of my versions is set to windowed, as screenshotting with windows doesn't work properly in 1.21.1, but swapping to full-screen does not change the results.
1.21.1:
24w33a:
