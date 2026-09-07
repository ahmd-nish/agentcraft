# MC-264003: Boats carrying players sometimes stop abruptly when sliding along ice

**Mojira URL:** [https://bugs.mojang.com/browse/MC-264003](https://bugs.mojang.com/browse/MC-264003)

## Report details

- **Mojira categories:** Entities; Player
- **Project:** MC
- **Issue key:** MC-264003
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2023-07-02T18:43:52.276-0700
- **Updated:** 2026-06-16T09:17:16.871-0700
- **Resolution date:** 2026-06-16T09:17:16.828-0700
- **Affects versions:** 1.20.1; 1.20.4; 24w04a; 1.21.8
- **Fix versions:** Future Update
- **Area:** Platform
- **Labels:** boat; ice; piston; slime_block
- **Votes:** 2
- **Watchers:** 1
- **Attachments:** 5
- **Attachment filenames:** 2023-07-02_21.12.44.png; 2023-07-02_21.12.53.png; 2023-07-02_21.13.17.png; 2024-01-26_14-42-53.mp4; LB_Error-MC-264003-IceBoatHalting.01.tar.bz2

## Description

The Bug
When a boat with a player in it is pushed by a slime and piston, the boat slides across ice. However, a significant percent (10-20+%) amount of the time, the boat won't slide smoothly and will halt an arbitrary distance along the slide. This can range from adjacent to the slime block up to 10 (or more) blocks away. This occurs on all ices (frosted, regular, packed, blue). If there isn't a player in the boat, it slides as expected.
Opinion/Hypothesis
On repeated testing, it 'feels' like there is a race condition between the player's velocity (0m/s) and the boat's pushed velocity. So if the game figures on the players speed first, the boat halts. Similarly, if a player boards a boat that is sliding, it appears to halt the boat in place instantly. However, this error does not require the player to board the boat after it is moving. Simply be in a boat that gets pushed by a slime on a piston, and sporadically the boat will insta-halt.
Steps to Reproduce
1. Create ice path ~10 blocks long [1-10].
2. Put two non-pushable, non-sticky blocks at either end [0 & 11].
3. Put slime blocks on top of non-stick blocks [Above 0 & 11].
4. Put sticky pistons facing slime and ice path. Extend and retract pistons once so slime blocks are attached. (Pistons at/above -2 & 13. Slimes now above -1 & 12)
5. Add block and button beside piston so player can extend piston while standing on the ice.
6. Place boat in path of slime block.
7. Get in boat.
8. Push button to extend piston.
9. Boat will be pushed and 'bounce' off of the slime block, move down the ice, and should collide with opposite slime block.
10. Player can push button on this end to return. Repeat until error is observed.
See attached screenshots for example setup.
Observed Results
No error message is provided.
Sometimes1 the boat will not move beyond the end of the slime block. Sometimes^1^ it slides part way and stops. And usually it will slide the length of the ice and stop at the opposing slime block. ([1] "sometimes" varies between every time and once in 5 minutes)
Expected Results
In the given setup, a boat on ice with a rider should be able to perpetually alternate between the extending pistons+slime blocks. More specifically, a player should be able to extend the piston, and have the boat start sliding, then come to a gradual stop on the ice, or a hard stop only if they collide with an obstruction.
References
User on reddit reported similar error.
Support Files
A compressed world save demonstrating the error has been attached. Uncompress. Load. Climb in boat. Release the lever and wait. The boat will eventually halt and a seemingly random location along the ice path. Usually in <30s. Longest I've waited to reproduce: 5 minutes. Too often it happens on the first piston extension.

## Comments (2)

### Comment 1: migrated (2023-07-02T18:43:52.276-0700)

This comment contained multiple image attachments (5), please login to view the attachments.

### Comment 2: Brain81505 (2024-01-25T08:14:03.252-0800)

Can confirm in 1.20.4
