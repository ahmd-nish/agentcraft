# MC-265399: Players' heads are incorrectly positioned while exiting the swimming/crawling state when other players are on screen

**Mojira URL:** [https://bugs.mojang.com/browse/MC-265399](https://bugs.mojang.com/browse/MC-265399)

## Report details

- **Mojira categories:** Player Animation; Rendering
- **Project:** MC
- **Issue key:** MC-265399
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2023-09-14T07:35:19.782-0700
- **Updated:** 2025-04-11T10:37:06.675-0700
- **Resolution date:** 2024-09-05T09:25:34.043-0700
- **Affects versions:** 1.20.1; 1.20.2 Pre-Release 4; 1.20.2 Release Candidate 1; 24w19b; 1.21; 24w34a
- **Fix versions:** 24w37a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** MC-265399.mp4
- **Issue links:** Relates:inward:MC-267046:Players' heads are momentarily incorrectly positioned when entering the elytra flying state

## Description

The Bug:
Players' heads are incorrectly positioned while exiting the swimming/crawling state when other players are on screen.
While a player is exiting the swimming/crawling state, their head is correctly positioned, but only when another player is not on their screen. If you were to exit the swimming/crawling state while another player is present on your screen, your head would harshly snap to the correct position.
If you're struggling to understand what this report is about, please watch the following video which will hopefully clear up any confusion.
Steps to Reproduce:
- Get two players and label them "Player A" and "Player B".

- Get "Player A" to stand on a glass block that's completely isolated in the air.

- Make sure that "Player B" is out of sight and not on the screen of "Player A".

- Get "Player A" to begin crawling by summoning a block on their head by using the command provided below.

```
/setblock ~ ~1 ~ minecraft:glass
```

- Get "Player A" to look upwards and have them exit the crawling state by removing the block above their head by using the command provided below.

```
/setblock ~ ~1 ~ minecraft:air
```

- Get "Player A" to watch their head closely as they exit the animation.

- Take note of how their head is completely smooth as "Player A" exits the crawling state.

- Get "Player B" to enter the screen of "Player A".

- Get "Player A" to repeat steps 4 through 8.

- Take note as to whether or not players' heads are incorrectly positioned while exiting the swimming/crawling state when other players are on screen.

Observed Behavior:
Players' heads are incorrectly positioned while exiting the swimming/crawling state when other players are on screen.
Expected Behavior:
Players' heads would be correctly positioned while exiting the swimming/crawling state even when other players are on screen.

## Comments (1)

### Comment 1: migrated (2023-09-14T07:35:19.782-0700)

This comment contained an image attachment, please login to view the attachment.
