# MC-302321: Chunks don't load while the player is being teleported

**Mojira URL:** [https://bugs.mojang.com/browse/MC-302321](https://bugs.mojang.com/browse/MC-302321)

## Report details

- **Mojira categories:** Chunk loading; Commands
- **Project:** MC
- **Issue key:** MC-302321
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2025-09-26T03:12:10.103-0700
- **Updated:** 2026-03-11T03:56:28.494-0700
- **Resolution date:** 2025-10-02T02:59:28.449-0700
- **Affects versions:** 1.21.9 Release Candidate 1; 1.21.9
- **Fix versions:** 1.21.10 Release Candidate 1
- **Area:** Platform EC
- **Votes:** 2
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** 2025-09-26 12-07-03.mov
- **Issue links:** Relates:outward:MC-302405:Repeating/chain command blocks with any form of a '/tp <player>' command doesn't constantly teleport the player to one spot

## Description

While the player is being teleported using, for example, a repeating command block, chunks don’t load.

Steps to reproduce:
- Set up a repeating command block with the following command. Note that adding the “p” tag isn’t strictly necessary to recreate the bug, I’ve added it so it’s easy to enable and disable the command.

```
execute as @p[tag=p] at @s run tp @s ~ ~ ~1
```

- Give yourself the “p” tag:

```
/tag @s add p
```

- You’ll now get teleported. Observe that chunks don’t load.

- Once finished, remove the “p” tag to stop getting teleported:

```
/tag @s remove p
```

- Observe that the chunks load again when the teleporting stops.

What I expected:
I expected the chunks to load. They used to in 1.21.8
What actually happened:
The chunks didn’t load

## Comments (2)

### Comment 1: 100percentme (2025-09-26T03:12:11.092-0700)

This comment contained multiple media attachments (2), please login to view the attachments.

### Comment 2: Creeper Juice (2025-09-27T13:10:24.293-0700)

This bug also seems to occurs when you ride an entity and that entity is being teleported.
