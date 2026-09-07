# MC-188163: Abnormally very high RAM usage since 1.13 (client side)

**Mojira URL:** [https://bugs.mojang.com/browse/MC-188163](https://bugs.mojang.com/browse/MC-188163)

## Report details

- **Mojira categories:** Performance
- **Project:** MC
- **Issue key:** MC-188163
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2020-06-08T08:15:45.679-0700
- **Updated:** 2025-04-30T05:26:10.020-0700
- **Resolution date:** 2023-02-23T15:03:40.426-0800
- **Affects versions:** 1.15.2; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 4; 1.16 Pre-release 6; 1.16 Pre-release 7; 1.16 Pre-release 8; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w27a; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Pre-release 2; 1.16.2 Release Candidate 1; 1.16.2 Release Candidate 2; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4 Pre-release 1; 1.16.4 Pre-release 2; 1.16.4 Release Candidate 1; 1.16.4; 20w46a; 20w48a; 20w49a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w11a; 1.17; 1.17.1 Pre-release 1; 1.17.1; 21w37a; 21w41a; 21w44a; 1.18 Pre-release 1; 1.18 Pre-release 4; 1.18 Release Candidate 1; 1.18; 1.18.1; 22w11a; 22w13a; 22w16b; 1.19; 1.19.1 Release Candidate 1; 1.19.1 Pre-release 2; 1.19.1 Pre-release 4; 1.19.2; 22w45a; 1.19.3; 23w07a
- **Fix versions:** 1.19.4 Pre-release 1
- **Labels:** client; high; high-ram; memory-leak; ram; ram-usage
- **Watchers:** 1
- **Attachments:** 7
- **Attachment filenames:** Client RAM Test 1.12.2.mp4; Client RAM Test 1.13.2.mp4; Client RAM Test 1.14.4.mp4; Client RAM Test 1.15.2.mp4; Client RAM Test 1.16 Pre-2.mp4; Tuto 1.png; Tuto 2.png
- **Issue links:** Relates:inward:MC-190258:Abnormally very high RAM usage since 1.13 (server side) | Relates:outward:MC-185263:Non full chunks in cache memory "semi-leak" | Duplicate:inward:MC-191755:Possible Memory Leak issue with update 1.16 | Duplicate:inward:MC-193261:Java memory garbage collection bug | Duplicate:inward:MC-259868:Minecraft Using WAY Too Much Memory

## Description

The bug
Since 1.13, the RAM used by the game has increased drastically to reach more than 5 GB in 1.15.2 and higher when Minecraft is not limited by JVM default arguments (= put -Xmx8G for example)!
For comparison, 1.12.2 uses only 500 MB of RAM!
This problem is apparently due to the DataFixerUpper introduced in 1.13.
How to test
- Go to the "Installations" section of your Minecraft launcher.

- Click on the three dots that appear when you hover over the profile you want to use for this test, and then click "Edit". If you don't already have a profile, create one!

- Select the version you want to test.

- Click on "More Options"

- Change the "-Xmx" argument in the "JVM Arguments" section to allocate 6 GB of RAM or more. Example for 8 GB (recommended) : -Xmx8G

- Save your profile.

- Open the task manager of your operating system.

- Launch the game with the correct profile and observe the evolution of the RAM used by the game in the task manager.

- Repeat for each version you want to test.

Videos tests
Here are all the tests I did from 1.12.2 to 1.16 Pre-Release 2, on all stable versions of Minecraft.
I have allocated 8 GB of RAM each time so as not to restrict the game to too low a ceiling, which would not allow us to see the problem.
No other programs run on the PC (except Discord and my recording program).
I did the test on my two different machines and the results are the same.
- Minecraft 1.12.2 (~450 MB) :

- Minecraft 1.13.2 (~2.1 GB) :

- Minecraft 1.14.4 (~5.0 GB) :

- Minecraft 1.15.2 (~5.2 GB) :

- Minecraft 1.16 Pre-Release 2 (~5.2 GB) :

We can also observe that with each new version, the CPU is used harder and harder, even after the game is fully loaded (especially in 1.16).
Note: This ticket is attached to  which processes the server side.

## Comments (18)

### Comment 1: migrated (2020-06-08T08:15:45.679-0700)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: migrated (2020-06-12T02:49:40.836-0700)

Affects pre release 4 1.16

### Comment 3: migrated (2020-06-17T00:46:19.017-0700)

Confirmed in 1.16 Pre-release 7.

### Comment 4: marcono1234 (2020-06-27T07:04:01.668-0700)

It appears this is related to DataFixerUpper, which was introduced for 1.13. This would explain why this issue started occurring for 1.13. This applies to the dedicated server () as well.
I don't have enough experience in profiling Java applications, but it appears DataFixerUpper creates multiple hundred Mega Bytes of objects which it then discards.
Note that this apparently only affects start up of the game / server. Afterwards the the data is garbage and will be collected by the JVM garbage collector if necessary.

### Comment 5: migrated (2020-07-02T07:04:07.906-0700)

Can confirm for 20w27a

### Comment 6: migrated (2020-08-09T03:48:59.524-0700)

Can confirm in 1.16.2 RC-1, This happens not only at the start of the game, but also when during gameplay. I also noticed that after the game is launched, the process remains "MinecraftLauncher.exe", which if disabled, the game will be as if nothing had happened, but the process "MinecraftLauncher.exe" it remains to consume memory.

### Comment 7: marcono1234 (2020-08-09T07:27:05.552-0700)

@, if you are experiencing this issue with MinecraftLauncher.exe, please create a separate report for the launcher project (MCL) (after having searched for existing reports) and remove your attachment from this report. This project (MC) and this report are only about the game itself but not the launcher.

### Comment 8: migrated (2021-07-13T22:11:42.250-0700)

1.17.1 still have this issue. In fact, it got worse.

### Comment 9: ampolive (2021-08-21T14:39:17.338-0700)

If this issue stems from the datafixers, it seems logical that this will progressively worsen, as each snapshot or release introduces a new data version.

### Comment 10: ZeNico13 (2021-08-22T01:27:24.117-0700)

@ You are absolutely right.

### Comment 11: syarumi (2021-08-24T14:37:19.097-0700)

There's also  on the maxed CPU usage side of things due to DFU.

### Comment 12: ampolive (2021-09-17T10:26:10.059-0700)

Can confirm in 21w37a.

### Comment 13: ampolive (2021-10-17T12:45:42.068-0700)

Can confirm in 21w41a.

### Comment 14: ampolive (2021-11-09T08:59:28.089-0800)

Can confirm in 21w44a.

### Comment 15: ampolive (2021-11-12T13:07:07.283-0800)

Can confirm in 1.18 Pre-release 1.

### Comment 16: migrated (2022-06-30T09:57:25.477-0700)

Can confirm in 1.19, per the reason stated previously, it get even worse. Some even stated to have caused the PC to thermal shutdown as seen at

### Comment 17: santinocavazos (2022-07-10T11:30:58.959-0700)

That's caused by a phenomenon in 1.13 called The Flattening.

### Comment 18: ouroya (2023-02-15T12:05:30.720-0800)

I have had this issue happen so severely that my computer shuts down within minutes or seconds of launching the game, though an entire shutdown is rare and usually this just causes the computer to freeze or massively slow down. My suggestion is to make the DFU lazily loaded, so it is not always active.
