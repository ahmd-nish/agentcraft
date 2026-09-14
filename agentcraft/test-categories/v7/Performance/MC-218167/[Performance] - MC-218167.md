# MC-218167: Chatting causes lag to occur

**Mojira URL:** [https://bugs.mojang.com/browse/MC-218167](https://bugs.mojang.com/browse/MC-218167)

## Report details

- **Mojira categories:** Performance
- **Project:** MC
- **Issue key:** MC-218167
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-03-08T23:58:19.065-0800
- **Updated:** 2025-04-29T20:24:56.547-0700
- **Resolution date:** 2022-01-06T17:47:57.854-0800
- **Affects versions:** 1.16.5; 21w08b; 21w11a; 21w15a; 21w16a; 21w17a; 21w18a; 1.17 Pre-release 1; 1.17; 1.17.1; 21w37a; 21w38a
- **Fix versions:** 21w39a
- **Labels:** chat; lag-spike; singleplayer
- **Watchers:** 1
- **Attachments:** 7
- **Attachment filenames:** 2021-03-09_15.28.22.png; image-2021-07-23-12-10-44-165.png; image-2021-07-23-12-10-53-823.png; MC-218167.mp4; profiling_chat.zip; profiling_prompt.zip; VisualVMSampling.png
- **Issue links:** Cloners:inward:WEB-5587:Chat causing subtle freezing after no activity in chat

## Description

Relates to MC-65587 and MC-225777
Possibly related to MC-131219, however, that bug takes place when you open chat; this is once you've hit enter to put something in the chat.
The bug
Often, I want to make a note to myself in singleplayer of something like coordinates. But lately, when I attempt to place such information in chat, it causes the game to freeze for a second for no reason even though I am in singleplayer.
Steps to reproduce:
1. Log into a singleplayer world that isn't open to LAN, etc.
2. Type something in chat and hit enter when you are done.
-->  Notice the big lag spike.

Additional Information
Note: It doesn't always happen, and it doesn't happen twice in a row.
Another note: Significantly less lag in 21w18a, but still there.
It seems like the game is trying to access the log and that is why it causes so much lag. It also occurs with command feedback. and feedback from debug profiling, but only the message including where the profile saved.

## Comments (21)

### Comment 1: migrated (2021-03-08T23:58:19.065-0800)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: Brevort (2021-03-09T12:29:18.232-0800)

I know the screenshot is from 05b, but it happens in the other versions listed as well.

### Comment 3: mtmjnb (2021-05-08T05:52:29.005-0700)

i have experienced this bug in multiplayer 1.16.5(modded server) and 21w18a(vanilla)

### Comment 4: migrated (2021-05-27T19:09:53.590-0700)

Can confirm in 1.17-pre1.

### Comment 5: SoloAlguien (2021-06-01T16:30:12.198-0700)

Can confirm in 1.17 Pre-release 3.

### Comment 6: migrated (2021-06-09T05:19:49.637-0700)

Can Confirm in 1.17 release

### Comment 7: migrated (2021-07-07T14:55:18.520-0700)

It occurs when you send the first text message on singleplayer world or on a hosted multiplayer server on 1.17.
The lag spike affects to everyone else, freezing the game completely for a second.
You can see a video of the bug here.

### Comment 8: migrated (2021-07-07T14:57:50.679-0700)

Can confirm in 1.17.1

### Comment 9: migrated (2021-07-22T20:32:21.670-0700)

It happens not only in chat, but also in displaying prompt texts when toggling mod functions (eg. tweakeroo, minihud, etc.), so it may be caused by text generation and rendering.
Besides, it is worth mentioning that the lag is even worse when Fabric is installed.

### Comment 10: migrated (2021-07-22T21:24:22.313-0700)

This is the result of profiling when chat lag and prompt lag occur.
Chat lag

Prompt lag

Looking the ticktime and CPU usage, when lag occurs, the ticktime is very high, but the CPU usage is relatively low. Therefore, I think a thread blocking may have occurred.
Chat lag: Tick 249:
[00] scheduledExecutables(1/1) - 98.28%/98.28%
[01] |   unspecified(1/1) - 100.00%/98.28%
[01] |   fabricClientEntityUnload(1/1) - 0.00%/0.00%
[00] updateDisplay(1/1) - 0.85%/0.85%
…
Prompt lag: Tick 70:
[00] updateDisplay(1/1) - 97.73%/97.73%
[01] |   unspecified(1/1) - 99.98%/97.71%
[01] |   mouse(556/556) - 0.02%/0.02%
[00] unspecified(1/1) - 0.96%/0.96%
[00] gameRenderer(1/1) - 0.74%/0.74%
…
When lag occurs, unspecified categories under scheduledExecutables and updateDisplay take up most of ticktime.

### Comment 11: migrated (2021-07-31T21:10:55.292-0700)

It seems that Minecraft Client is checking whether a player is blocked or not, this causes network request happen in the render thread. In bad network environment, the lag is way significant. On the other hand, if we tested the lag in offline mode, it will no longer exist. Here is a VisualVM Sampling result, you can see the Yggdrasil's HTTP API just blocked the render thread from handling user input and render the frame.
(used fabric intermediary names to debug and yarn names in blue marks above)
I used Mixin to skip the check, the lag I'm suffering is gone.
I think the HTTP Request should not happen in the Render Thread. The block list should be fetched either in other threads or before playing.

### Comment 12: clx_ (2021-09-03T03:04:42.002-0700)

Sharing my findings from MC-235836
Inside the clientbound chat message packet, there is a "sender" field to identify the chat message's author with their's player UUID.
Upon sending a chat message as a player (or receiving one from another player), the client will freeze for about a second, likely for the reasons leedagee mentioned above. The client no longer experiences this issue for future chat messages that are sent/received, until it has been restarted (from my experience).
The issue however cannot be reproduced if the sender field is empty, e.g. system messages using tellraw or modified server software where the server simply doesn't send the sender field / sets it to a blank UUID on player messages. Oddly enough, this issue also cannot be reproduced on systems with AMD graphics. I've only been able to reproduce it on systems with NVIDIA graphics.

### Comment 13: migrated (2021-09-03T20:31:36.753-0700)

However, this can also be reproduced on my laptop with AMD R7 M360 GPU and my desktop with AMD RX580 GPU. I don't think it is an issue relating to specific graphics.

### Comment 14: ampolive (2021-09-04T05:02:46.942-0700)

For me, this only seems to happen the first time the chat is opened, after that no lag occurs.

### Comment 15: ampolive (2021-09-15T12:46:51.157-0700)

Can confirm in 21w37a.

### Comment 16: MMK21 (2021-09-24T08:36:08.521-0700)

Affects 21w38a.
Whispers (/msg) are also affected by this bug.

### Comment 17: migrated (2022-01-05T19:31:12.806-0800)

affects 1.18.1
lag occurs again after a while of someone not chatting, likely due to the player name cache being cleared
this can be fixed fairly easily by making the server request asynchronous i assume

### Comment 18: migrated (2022-01-06T05:44:49.992-0800)

It appears this bug has re-arisen. 1.18+

### Comment 19: migrated (2022-01-06T06:02:52.115-0800)

Can confirm that this is occurring again in 1.18.1. client freezes for approximately 1-2 seconds whenever a player is silent for a while and sends a message.

### Comment 20: [Mod] violine1101 (2022-01-06T06:13:09.105-0800)

If you think this still affects the latest version, please file a new bug report. If possible with some information, i.e. video/f3 screenshot etc.

### Comment 21: Avoma (2022-01-06T12:26:22.346-0800)

MC-247973 is the new ticket for this issue as this behavior has reappeared in 1.18.1.
