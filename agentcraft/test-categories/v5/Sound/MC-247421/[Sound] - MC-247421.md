# MC-247421: Console spam: "Error starting SoundSystem. Turning off sounds & music"

**Mojira URL:** [https://bugs.mojang.com/browse/MC-247421](https://bugs.mojang.com/browse/MC-247421)

## Report details

- **Mojira categories:** Performance; Sound
- **Project:** MC
- **Issue key:** MC-247421
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-01-02T02:28:23.084-0800
- **Updated:** 2025-05-29T09:10:04.823-0700
- **Resolution date:** 2023-11-20T08:33:07.979-0800
- **Affects versions:** 1.18.1; 1.19; 1.19.2; 22w44a; 1.19.3; 23w05a; 1.20.2
- **Fix versions:** 23w40a
- **Area:** Platform
- **Watchers:** 2
- **Attachments:** 2
- **Attachment filenames:** 2022-01-01-1.log.gz; Reproduce.png
- **Issue links:** Relates:inward:MC-254669:Causes a lot of missing sound spam when the audio device is set to a non-default | Duplicate:inward:MC-254049:No Sound or Frames on 1.19 | Duplicate:inward:MC-23349:signs wont work on posts correctly | Relates:outward:MC-265594:Game has no audio, closes with exit code -1073740791 | Duplicate:inward:MCL-23349:Launcher creates extremely large log files

## Description

I had Minecraft open for a while. After putting the computer into hibernation mode and turning it back on, the game printed out the following error message about once every 50 milliseconds.
There were so many of these errors in the launcher log, to the point where their time stamps lagged behind for several hours because the Minecraft launcher couldn't keep up. When I closed Minecraft, the logs kept going because they lagged behind that much. (The logs written to file didn't have any issue, just those displayed in the launcher log window, which means the launcher not keeping up with the logs is a launcher bug.)

```
Audio device was lost!

Error starting SoundSystem. Turning off sounds & music
java.lang.IllegalStateException: Failed to open OpenAL device
	at dqi.b(SourceFile:264)
	at dqi.a(SourceFile:151)
	at fdf.h(SourceFile:112)
	at fdf.a(SourceFile:103)
	at fdf.a(SourceFile:234)
	at fdi.a(SourceFile:253)
	at dxo.q(SourceFile:1761)
	at dxo.f(SourceFile:1086)
	at dxo.e(SourceFile:733)
	at net.minecraft.client.main.Main.main(SourceFile:238)
```
Currently it is unclear to me how the issue can be reproduced reliably. It might've been caused by some Windows issue where it might have thought a device was connected that actually wasn't connected.
The relevant log is
 (60 MB uncompressed).
Observed: If the game fails to connect to some audio device, the game will print an error message every 50ms.
Expected: The error message should show up, but either only once, or only in larger time intervals (e.g. once every 30 seconds).
Reproduce:
- Set the in-game audio device to your headset.

- Enter the following commands:

```
/playsound minecraft:music.dragon voice @p
```

```
/weather thunder
```

- Disable all audio devices connected to Windows.

- Notice that the game outputs spam to the logs at a rapid rate.

## Comments (16)

### Comment 1: migrated (2022-01-02T02:28:23.084-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: Avoma (2022-05-28T12:30:21.540-0700)

I experienced similar behavior when my audio output device was seemingly randomly disconnected. I'm not sure if this is the same issue but the following was logged multiple times in my game output console.

```Get attributes size1824945293136: Invalid device.

Error starting SoundSystem. Turning off sounds & music
java.lang.IllegalStateException: Failed to get OpenAL attributes
	at dxo.j(SourceFile:213)
	at dxo.a(SourceFile:169)
	at flx.h(SourceFile:113)
	at flx.a(SourceFile:103)
	at flx.a(SourceFile:235)
	at fma.a(SourceFile:249)
	at eeu.q(SourceFile:1809)
	at eeu.f(SourceFile:1087)
	at eeu.e(SourceFile:733)
	at net.minecraft.client.main.Main.main(SourceFile:237)```

### Comment 3: Bentroen (2022-08-11T22:00:07.371-0700)

I can confirm this on 1.19.2. Once triggered, it makes it pretty much impossible to use the game log when developing data packs/resource packs, and the only way out seems to be to restart the entire game.

### Comment 4: ljcool2006 (2022-10-08T00:17:44.741-0700)

Maybe contact Paul Lamb (the author of the SoundSystem) about this? He might think up of something.

### Comment 5: sovde (2023-04-29T08:00:42.742-0700)

Hello, just want to comment that I also regularly experience this issue. I have a bluetooth headset as my sole audio output, so when I turn it off Minecraft starts spitting out this error. This is exceptionally bad when I leave Minecraft running in the background while I sleep, as it leads to very large log files. I've recently had 15, 9 , 8, and 6 GB files to purge from my drive, and just testing this last night produced another 600 MB file. I'd like to see a solution for this, as it's causing my computer active issues as drives fill up with log files.

### Comment 6: migrated (2023-09-30T01:40:52.420-0700)

Seems to be related to , possibly not exactly the same.

### Comment 7: migrated (2023-10-06T12:32:04.150-0700)

I can confirm this issue in 1.20.2.
The game seems to scan all potential devices for audio (not just audio devices).
Thus far, I have discovered in 1.20.2 that the issue also occurs on a resource pack reload.
For example, this bug had been affecting my connected mouse which I had fixed by disconnecting the mouse (example 1). When my mouse was disconnected, the issue came back after a game relaunch and was fixed by connecting it (example 2).
Example 1:

```[21:02:38] [Render thread/INFO]: Audio device was lost!
[21:02:38] [Render thread/WARN]: Missing sound for event: minecraft:item.goat_horn.play
[21:02:38] [Render thread/WARN]: Missing sound for event: minecraft:entity.goat.screaming.horn_break
[21:02:38] [Render thread/WARN]: Failed to reset device: Invalid Device
[21:02:38] [Render thread/ERROR]: Get attributes size1616449638432: Invalid device.
[21:02:38] [Render thread/ERROR]: Error starting SoundSystem. Turning off sounds & music
java.lang.IllegalStateException: Failed to get OpenAL attributes
    at ejl.i(SourceFile:222) ~[1.20.2.jar:?]
    at ejl.a(SourceFile:178) ~[1.20.2.jar:?]
    at gdn.h(SourceFile:116) ~[1.20.2.jar:?]
    at gdn.a(SourceFile:106) ~[1.20.2.jar:?]
    at gdn.a(SourceFile:238) ~[1.20.2.jar:?]
    at gdq.a(SourceFile:272) ~[1.20.2.jar:?]
    at eqv.t(SourceFile:1961) ~[1.20.2.jar:?]
    at eqv.d(SourceFile:1237) ~[1.20.2.jar:?]
    at eqv.f(SourceFile:856) ~[1.20.2.jar:?]
    at net.minecraft.client.main.Main.main(SourceFile:253) ~[1.20.2.jar:?]```
Example 2:

```[21:29:37] [Render thread/INFO]: Audio device was lost!
[21:29:37] [Render thread/WARN]: Missing sound for event: minecraft:item.goat_horn.play
[21:29:37] [Render thread/WARN]: Missing sound for event: minecraft:entity.goat.screaming.horn_break
[21:29:38] [Render thread/ERROR]: Get attributes size2618220208336: Invalid device.
[21:29:38] [Render thread/ERROR]: Error starting SoundSystem. Turning off sounds & music
java.lang.IllegalStateException: Failed to get OpenAL attributes
    at ejl.i(SourceFile:222) ~[1.20.2.jar:?]
    at ejl.a(SourceFile:178) ~[1.20.2.jar:?]
    at gdn.h(SourceFile:116) ~[1.20.2.jar:?]
    at gdn.a(SourceFile:106) ~[1.20.2.jar:?]
    at gdn.a(SourceFile:238) ~[1.20.2.jar:?]
    at gdq.a(SourceFile:272) ~[1.20.2.jar:?]
    at eqv.t(SourceFile:1961) ~[1.20.2.jar:?]
    at eqv.d(SourceFile:1237) ~[1.20.2.jar:?]
    at eqv.f(SourceFile:856) ~[1.20.2.jar:?]
    at net.minecraft.client.main.Main.main(SourceFile:253) ~[1.20.2.jar:?]```

### Comment 8: migrated (2023-10-13T12:17:41.546-0700)

I initiated ticket , which was closed and resolved and is referred to me here. And I'm not sure if the problem described in this ticket accurately represents the case I make. I pointed 3 things on my ticket:
1. Lack of audio
2. A lag problem
3. An error message (error code -1073740791) that appears when closing the game.
And it seems that the 3 things are related. This ticket only discusses the audio issue only.
My question is, are these 3 problems going to be analyzed separately? Or are you going to consider analyzing globally?

### Comment 9: [MOD] Greymagic27 (2023-10-13T13:46:52.954-0700)

Hi Marchelino84.
I resolved your report as a duplicate of this report as I think it best describes the main point of your issue.
To address them in order,
1. Lack of audio will most likely be caused by this error as it states 'turning off music and sound as it failed to open openAL device'
2. The lag problem is most likely unrelated and would require another bug report only if you can find the specific cause for the lag. Otherwise, community support would be a better place to ask.
3. The error code -1073740791 would be something community support can take a look at as it's most likely a driver or hardware issue.
I hope this helps explain things a bit better. If you have any further questions don't hesitate to reach out to me on the mojira discord server, the link for which is below.
Quick Links:
📓 Bug Tracker Guidelines – 💬 Community Support – 📧 Mojang Support
📓 Project Summary – ✍️ Feedback and Suggestions – 📖 Game Wiki – 🐛Mojira discord server

### Comment 10: migrated (2023-10-14T22:31:34.013-0700)

Hello Greymagic27, Excuse my insistence but it is precisely because of the way in which I am experiencing these 3 problems, simultaneously, that I come to the conclusion that each one is a symptom of the same disease and should be seen together.
- The audio problem, which occurs from the beginning of the game. Due to some failure in the reading/initialization of the audio subsystem that the game has.

- The lag problem is precisely because in a very short period of time it occurs multiple times because you are trying to read a lost goat sound. Which is also seen in log. This reading is executed so frequently that it hogs all the resources and makes it difficult for the game to execute the rest of the commands/events such as moving, activating something, etc.

- The error code is perhaps the most difficult to explain, but the most obvious thought is that if the game experiences a problem when starting the system that is responsible for handling the audio, it also has a problem when finishing the game.

But hey, they are points of view. I just hope that nothing is left unchecked and hope that this is resolved soon.

### Comment 11: [MOD] Greymagic27 (2023-10-15T04:04:08.351-0700)

I did see a similar case to yours so if community support can't help with the bits I said they might be able to help with, leave a comment on your original bug report and I'll look into it a bit further.

### Comment 12: migrated (2023-10-15T05:34:57.925-0700)

Hi Greymagic27, I was sent here due to my issue being a duplicate of this issue
from MC-265825. Since then, a ran some test. With no connected peripheral except ones that are built-in (laptop user). I get the lag caused by this Issue. But, connecting any peripheral such as: a mouse, a pair of speakers, or printer fixes the issue. Disconnecting the devices doesn't seem to cause this issue for me. However, when quitting the game even with the spam being gone still crashes with Error code -1073740791.
This Issues only happen to me after updating Widows, but rolling back the update to a known update that the game worked fine with doesn't fix the issue.
Further debugging:
- Making sure using latest drivers (graphic, audio, etc) that doesn't break Windows.

- I use separate instances of the Official Minecraft launcher for modded Minecraft (for safety in case a mod corrupts an instance).
- Non-broken modded Minecraft instance uses launcher version 2.11.24-1.5.7 (doesn't seem to occur, or occurs not as often)

- Official Vanilla Minecraft uses launcher version 2.11.24-1.3.7 (the issue occurs most of the time)

- Uninstalling/Reinstalling Instances doesn't fix the issue.

The Following debugging occurs with all broken instances and Official Vanilla.
- Launching/Running the game with all audio output devices disabled even ones that aren't connected also causes issue but doesn't spam, but with no lag.

- Launching/Running the game with only one enabled audio device (wired headphones) doesn't cause the Issue.

- Launching/Running the game with only one enabled audio device (built-in speakers) cause the Issue with no lag, but the output log looks like Minecraft is scanning all connected devices (non-audio), but doesn't infinitely do it and will eventually hit the audio device and the Issue stops. But causes the game to crash upon quitting (Error code -1073740791)

- Launching/Running the game with only one enabled audio device (virtual speakers, Windows 11 built-in virtual desktop device) cause the Issue with no lag, but the output log looks like Minecraft is scanning all connected devices (non-audio) but does it infinitely. But causes the game to crash upon quitting (Error code -1073740791)

- Launching/Running the game with only one enabled audio device (Bluetooth headphones) doesn't cause the Issue.

- Launching/Running the game with all of these audio devices enabled, but with one connected cause the lag and the spam, probably caused by Minecraft constantly scanning for an audio device instead of using the computers default device.

Temporary fix (for those affected):
Disable all audio devices through settings > sound > (sound device here) > change Allow to Not Allow.  Do this for all but the device you use for audio.

### Comment 13: migrated (2023-10-15T06:01:58.217-0700)

In my case I have updated Windows and the drivers as well.
I partially solve the audio and lag problem by raising and lowering the volume when I start the game. But the error code -1073740791 still appears at the end when close the game.
I don't usually have another app making sound while I play because it distracts me. I could try to see what happens if I start the game with some other application making sound.

### Comment 14: [MOD] Greymagic27 (2023-10-15T11:19:56.391-0700)

Regarding the error "-1073740791", with the game lagging and not having any audio:
I have split this up from this report into  as it seems to be a new issue that relates to this, but isn't a direct duplicate. If you're having this issue please refer to  from now on and add any helpful information.

### Comment 15: migrated (2023-10-15T14:08:49.157-0700)

Okay. From now on I will go back to my original ticket. I will try to do more tests and investigate more about the error.

### Comment 16: gegy (2023-11-20T08:33:07.979-0800)

The issue with the log spam and lag has been resolved in 23w40a: if you're still experiencing issues with this version or newer with audio not loading, please see .
