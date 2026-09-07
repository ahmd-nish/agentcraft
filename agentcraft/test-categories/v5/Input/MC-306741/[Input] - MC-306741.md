# MC-306741: Opening the chat forces a CJK input method when one is enabled in the system

**Mojira URL:** [https://bugs.mojang.com/browse/MC-306741](https://bugs.mojang.com/browse/MC-306741)

## Report details

- **Mojira categories:** Input
- **Project:** MC
- **Issue key:** MC-306741
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2026-03-05T21:22:30.640-0800
- **Updated:** 2026-03-13T17:25:48.974-0700
- **Resolution date:** 2026-03-13T05:35:38.346-0700
- **Affects versions:** 26.1 Snapshot 11; 26.1 Pre-Release 1
- **Fix versions:** 26.1 Pre-Release 2
- **Area:** Platform HC
- **Votes:** 12
- **Watchers:** 3
- **Attachments:** 3
- **Attachment filenames:** 2026-03-06_14-05-40.mp4; 2026-03-06_14-06-19.mp4; 2026-03-12_20-07-59.mp4

## Description

The bug
If you want to type in English, you have to press the keyboard button to switch between English and Japanese every time you open the chat.
To reproduce
- Open the chat or press "/" to start a command.

- Start typing.

The functionality should be updated to work as follows
- The default input language when starting Minecraft should be English.

- The system must remember the last used input language.

- It should be possible to switch between English and Japanese even when not typing, just like in older versions.

Regarding "remembering the last used language," the expected behavior is as follows
- Open chat → Switch from English to Japanese (keyboard operation) → Type in Japanese → Send chat → Open a new chat → Resume with Japanese input.

- Open chat → Switch from Japanese to English (keyboard operation) → Type in English → Send chat → Open a new chat → Resume with English input.

This issue affects all text input fields, including
- Chat

- "/" Command

- Command block

- Writable book

- Anvil

- Sign

- Creative inventory search

- Resource pack search

- Select world

- etc...

The impact on commands is particularly severe. Every time a single command is executed, the player must manually switch the input mode from Japanese back to English via keyboard operation.
This issue was introduced by the fix for the following bug
MC-91132
https://bugs.mojang.com/browse/MC/issues/MC-91132
While the update to prevent blocking control keys (WASD) is good, the fix implemented here was poorly designed as it did not take commands into account.
The only current workaround
Press the language switch key to change to English before the Japanese predictive text is confirmed. This only works with Microsoft IME.
Please refer to the third video.
Additional Context
Many Japanese players are aware of this serious problem, and it has become a major topic on social media. While the priority may be marked as Low, this is a significant issue in certain regions. It is a critical problem that needs to be fixed by the next major update.

## Comments (9)

### Comment 1: Automation for Jira (2026-03-05T21:22:38.752-0800)

Thank you for helping us improve Minecraft! We saved your files:

### Comment 2: Robot_005 (2026-03-09T05:00:39.098-0700)

While the priority is marked as Low, this is a significant issue in certain regions. It needs to be fixed by the next major update.

### Comment 3: serval7227 (2026-03-11T04:36:55.058-0700)

I agree.
For non-CJK users, a good analogy would be that it’s like having CAPS LOCK turned on every time you open a chat.
To type normally, you have to disable it each time.

### Comment 4: luan_wo_xin_zhe (2026-03-11T22:39:54.317-0700)

I disagree with @serval7227. When I downloaded and used Microsoft Pinyin Input Method (which is the default Chinese input method for the Windows operating system—it can be installed when you first install Windows or select Chinese as the language during subsequent setup), both when I pressed the "T" key and the "/" key, it remembered the last input language used by the player. This is the conclusion I came to in version 26.1 Pre-Release 1.

### Comment 5: Robot_005 (2026-03-12T04:33:25.068-0700)

This comment contained multiple media attachments (2), please login to view the attachments.

### Comment 6: Robot_005 (2026-03-12T04:40:35.814-0700)

Thanks to the comments, I found a workaround! Please refer to the only workaround listed in the description.
Try switching to English after the predictive text has been confirmed. You should be able to reproduce the bug, just like in the first video.

### Comment 7: luan_wo_xin_zhe (2026-03-12T11:39:25.013-0700)

@Robot_005
Thank you for your reply. It is confirmed that this issue occurs not only in the chat interface, but also anywhere text input is required.

### Comment 8: Robot_005 (2026-03-13T05:14:23.024-0700)

Could you please reconsider the priority? I believe it should be set to "Very Important." This is a very frustrating bug that blocks command inputs.

### Comment 9: Robot_005 (2026-03-13T17:25:48.974-0700)

It's fixed! Thank you!
