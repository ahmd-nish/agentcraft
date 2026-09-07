# MC-275774: Observers no longer detect redstone dust powering/unpowering

**Mojira URL:** [https://bugs.mojang.com/browse/MC-275774](https://bugs.mojang.com/browse/MC-275774)

## Report details

- **Mojira categories:** Redstone
- **Project:** MC
- **Issue key:** MC-275774
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2024-08-21T09:10:15.600-0700
- **Updated:** 2025-04-26T16:23:17.045-0700
- **Resolution date:** 2024-08-25T03:20:56.164-0700
- **Affects versions:** 24w34a
- **Fix versions:** 24w35a
- **Area:** Platform
- **Labels:** experimental_redstone
- **Watchers:** 1
- **Attachments:** 5
- **Attachment filenames:** 2024-08-21_11.41.50.png; 2024-08-21 22-55-01.mp4; image-2024-08-21-11-07-19-071.png; image-2024-08-21-11-09-17-225.png; image-2024-08-21-12-52-19-731.png
- **Issue links:** Duplicate:inward:MC-275846:Redstone wire do not update observers | Duplicate:inward:MC-276001:Observers don't detect redstone dust changes

## Description

As the title says, in the current snapshot with experimental redstone features on, Observers do not detect a change in redstone dust when it becomes powered or unpowered. Observers still detect when dust has been placed in front of them and when the direction of the dust has been changed, but they do not detect the powered state, which is a major issue.
Steps to reproduce:
1. Enable the experimental Redstone Dust features
2. Create any sort of redstone circuit configuration that involves an Observer facing a piece of Redstone Dust (example image)
3. Attempt to make Observer send a signal when the dust has been powered or unpowered (In this example, attempt to make the Copper Bulb turn on when the Lever is activated)
Observed Result
The Observer does not send a signal (in this example, Copper Bulb should be on)
Expected Result
The Observer should send a signal (activating the Copper Bulb)

## Comments (8)

### Comment 1: migrated (2024-08-21T09:10:15.600-0700)

This comment contained multiple image attachments (5), please login to view the attachments.

### Comment 2: [Mod] Jingy (2024-08-21T09:42:09.667-0700)

I cannot reproduce this:

### Comment 3: Savvvage_ (2024-08-21T10:22:58.555-0700)

i can reproduce it, 24w34a, this seems very important

### Comment 4: Emdy (2024-08-21T10:26:18.809-0700)

Observer reacts to dust shape changing but not power level changing

### Comment 5: migrated (2024-08-21T10:52:39.696-0700)

the issue only appears to happen with the experimental redstone features ON, as opening a world with them off the issue does not happen

### Comment 6: Viradex (2024-08-21T10:55:11.315-0700)

Can confirm.

### Comment 7: [Mod] Jingy (2024-08-21T11:57:15.616-0700)

This seems to be a by-product of this change in the 24w33a changelog:
Redstone wire now only triggers block updates on blocks that may receive power from the wire
Observers detect block updates, and with redstone not outputting them anymore the observer cannot detect it.

### Comment 8: jjl21 (2024-08-21T12:55:26.183-0700)

Obsevers don't detect block updates, they detect shape updates. This bug is likely unrelated to this change, it happens even if you run redstone directly into the observer, as if you were powering it, which does send block update to the observer.
