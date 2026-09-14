# MC-243489: Console spam: Skipping update for removed player

**Mojira URL:** [https://bugs.mojang.com/browse/MC-243489](https://bugs.mojang.com/browse/MC-243489)

## Report details

- **Mojira categories:** Debug
- **Project:** MC
- **Issue key:** MC-243489
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2021-11-30T20:48:37.707-0800
- **Updated:** 2025-03-21T00:14:14.655-0700
- **Resolution date:** 2022-01-17T07:37:30.282-0800
- **Affects versions:** 1.18; 1.18.1 Release Candidate 1; 1.18.1
- **Fix versions:** 22w03a
- **Watchers:** 1
- **Attachments:** 0

## Description

Pages and pages of the message below.

[20:36:31] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'
[20:36:31] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'
[20:36:31] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'
[20:36:31] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'
[20:36:31] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'
[20:36:32] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'
[20:36:32] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'
[20:36:32] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'
[20:36:32] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'
[20:36:32] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'
[20:36:32] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'
[20:36:32] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'
[20:36:33] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'
[20:36:33] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'
[20:36:33] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'
[20:36:33] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'
[20:36:33] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'
[20:36:33] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'
[20:36:33] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'
[20:36:33] [Server thread/INFO]: Skipping update from removed player 'adj['Targeet'/262524, l='ServerLevel[world]', x=-100.70, y=132.00, z=20.30, removed=KILLED]'

## Comments (3)

### Comment 1: migrated (2021-12-08T02:59:43.009-0800)

I can confirm I am seeing this on 1.18.1-RC1, I have never seen it before, and I keep a terminal screen open 24x7 with the log output sent to it for multiple servers (to keep an eye on chat, mostly), message is nearly identical:

```[01:12:25] [Server thread/INFO]: Skipping update from removed player 'adj['removed'/25338, l='ServerLevel[farfarout]', x=-164.32, y=-23.67, z=-210.95, removed=KILLED]'
[01:12:25] [Server thread/INFO]: Skipping update from removed player 'adj['removed'/25338, l='ServerLevel[farfarout]', x=-164.32, y=-23.87, z=-210.95, removed=KILLED]'
[01:12:25] [Server thread/INFO]: Skipping update from removed player 'adj['removed'/25338, l='ServerLevel[farfarout]', x=-164.31, y=-23.98, z=-210.95, removed=KILLED]'
[01:12:25] [Server thread/INFO]: Skipping update from removed player 'adj['removed'/25338, l='ServerLevel[farfarout]', x=-164.31, y=-23.98, z=-210.95, removed=KILLED]'```

### Comment 2: migrated (2021-12-14T23:21:13.102-0800)

I am now seeing this on 1.18.1.
[22:53:23] [Server thread/INFO]: Skipping update from removed player 'EntityPlayer['Comander_Colt'/404944, uuid='5d7c606b-f1b7-47f9-8a23-696afd12d37b', l='ServerLevel[world]', x=-9114.74, y=29.00, z=-2818.30, cpos=[-570, -177], tl=13367485, v=false, removed=KILLED](Comander_Colt at -9114.742114977747,29.0,-2818.297427002529)'
This player is playing on a slow connection. when I reduced the server render distance to 6(down from 24) it resolved the issue

### Comment 3: migrated (2021-12-15T05:07:17.257-0800)

Confirmed for 1.18.1. Server and player are on high speed connections
view-distance=16
[02:51:23] [Server thread/INFO]: Skipping update from removed player 'adj['real_bendi'/2738705, l='ServerLevel[world]', x=106.30, y=95.94, z=-124.33, removed=KILLED]'
[02:51:24] [Server thread/INFO]: Skipping update from removed player 'adj['real_bendi'/2738705, l='ServerLevel[world]', x=106.30, y=95.94, z=-124.33, removed=KILLED]'
[02:51:25] [Server thread/INFO]: Skipping update from removed player 'adj['real_bendi'/2738705, l='ServerLevel[world]', x=106.30, y=95.94, z=-124.33, removed=KILLED]'
