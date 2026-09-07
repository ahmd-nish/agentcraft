# MC-50614: Villager trading window is not closed when villager leaves interaction range

**Mojira URL:** [https://bugs.mojang.com/browse/MC-50614](https://bugs.mojang.com/browse/MC-50614)

## Report details

- **Mojira categories:** Trading; UI
- **Project:** MC
- **Issue key:** MC-50614
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2014-03-08T09:20:22.803-0800
- **Updated:** 2025-07-16T05:02:59.474-0700
- **Resolution date:** 2024-10-22T08:24:19.112-0700
- **Affects versions:** Minecraft 14w10c; Minecraft 14w19a; Minecraft 14w21b; Minecraft 14w28b; Minecraft 14w29b; Minecraft 14w30c; Minecraft 14w31a; Minecraft 1.8-pre1; Minecraft 15w33b; Minecraft 15w33c; Minecraft 1.11.2; Minecraft 1.12.1; Minecraft 1.12.2 Pre-Release 1; Minecraft 1.12.2 Pre-Release 2; Minecraft 1.12.2; Minecraft 18w21b; Minecraft 1.13-pre1; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w47a; Minecraft 18w47b; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 19w12b; Minecraft 19w13b; 1.15.1; 1.16.1; 1.16.4; 20w48a; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w07a; 21w15a; 1.17; 1.17.1; 1.18 Pre-release 6; 1.18.1; 1.19; 1.19.2; 1.20.1; 23w46a; 1.21
- **Fix versions:** 24w44a
- **Area:** Platform
- **Labels:** trading; villager
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2014-03-08_18.15.25.png; MC-50614.mp4
- **Issue links:** Relates:outward:MC-117815:The sign GUI remains open when the said sign is destroyed | Relates:outward:MC-19764:Trades are still possible after a villager/wandering trader died | Duplicate:inward:MC-242541:No matter how far the player travels away from the villager, it's UI will never close | Duplicate:inward:MC-219431:Villager trading GUI doesn't close when you go out of range | Duplicate:inward:MC-168798:Villagers do not close their trade GUI even if they are moved 100s of blocks away | Relates:inward:MC-154080:Wandering Trader trade GUI does not close when the Wandering Trader changes dimensions allowing you to trade infinitely | Relates:inward:MC-146521:Villagers move while trading | Relates:outward:MC-299736:Teleporting a villager or wandering trader to a location which is still within the player's entity interaction range closes its UI

## Description

The bug
The trading window remains open when a villager moves outside of the interaction range.
How to reproduce
- Spawn a villager and a zombie

- Start trading with the villager
→  The window stays open even after the villager left the interaction range

The trading window in the screenshot belongs to the villager in the right corner.

## Comments (19)

### Comment 1: migrated (2014-03-08T09:20:22.803-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: migrated (2014-05-07T12:24:46.105-0700)

Is this still a concern in the current Minecraft version 14w18b / Launcher version 1.3.11 or later? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 3: migrated (2014-05-11T04:52:59.375-0700)

Cannot reproduce.

### Comment 4: migrated (2018-06-13T21:10:48.978-0700)

Affects 1.13-pre1

### Comment 5: migrated (2018-08-25T13:13:34.830-0700)

Confirmed for 1.13.1.

### Comment 6: j_p_smith (2020-06-26T13:14:54.296-0700)

Confirmed in 1.16.1.

### Comment 7: Avoma (2020-11-26T02:28:26.122-0800)

Can confirm in 20w48a

### Comment 8: Avoma (2020-12-24T04:05:44.458-0800)

Can confirm in 20w51a.

### Comment 9: Avoma (2021-01-20T11:04:28.955-0800)

Can confirm in 21w03a.

### Comment 10: Avoma (2021-02-04T06:08:10.979-0800)

Can confirm in 21w05a.

### Comment 11: Avoma (2021-02-12T04:56:01.745-0800)

Can confirm in 21w06a.

### Comment 12: Avoma (2021-02-19T03:24:25.283-0800)

Can confirm in 21w07a.

### Comment 13: Avoma (2021-02-20T08:52:31.026-0800)

Video attached.

### Comment 14: Avoma (2021-04-17T07:19:22.977-0700)

Can confirm in 21w15a.

### Comment 15: Avoma (2021-06-17T07:00:51.240-0700)

Can confirm in 1.17.

### Comment 16: Avoma (2021-08-28T03:16:26.151-0700)

Can confirm in 1.17.1.

### Comment 17: Avoma (2022-06-13T05:31:00.286-0700)

Can confirm in 1.19.

### Comment 18: Avoma (2022-10-26T04:37:25.786-0700)

Can confirm in 1.19.2.

### Comment 19: Cybereggs1337 (2024-10-19T02:48:05.118-0700)

This thing can kill so-called "Void Trade Halls"... it is interesting to know other players' reaction.
