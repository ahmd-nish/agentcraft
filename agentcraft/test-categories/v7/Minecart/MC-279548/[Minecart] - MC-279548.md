# MC-279548: TNT minecart does not remember ignition source when exploding from a fall

**Mojira URL:** [https://bugs.mojang.com/browse/MC-279548](https://bugs.mojang.com/browse/MC-279548)

## Report details

- **Mojira categories:** Combat; Minecart
- **Project:** MC
- **Issue key:** MC-279548
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2025-01-15T16:47:05.430-0800
- **Updated:** 2026-03-11T03:47:17.982-0700
- **Resolution date:** 2025-08-04T08:35:55.538-0700
- **Affects versions:** 25w03a
- **Fix versions:** 25w32a
- **Area:** Platform HC
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** 2025-01-15_17.30.21.png

## Description

In 25w03a TNT minecarts now remember their ignition source when they are primed by a damage source that ignites TNT. However if the TNT minecart explodes from a fall or horizontal collision before the fuse runs out, this ignition source is forgotten.

Steps to reproduce:
- Build the setup shown in the attached screenshot.

- Be in creative mode.

- Run the command `/tick freeze`

- Prime the TNT block with a flint and steel.

- Run the command `/tick step 52`

- Turn the lever on to power the powered rails.

- Run the command `/tick step 28`. The TNT should explode and prime the TNT minecart.

- Stand close enough to the falling TNT minecart so you will be killed in one hit when it explodes, and switch to survival mode.

- Run the command `/tick unfreeze`. The TNT minecart will explode and kill the player.

- `player was blown up` is printed to the chat. There is a very low chance that instead, `player was blown up by player` will be printed to chat due to the random fuse time given to TNT minecarts causing the TNT minecart to explode before it touches the ground.

Expected behavior: `player was blown up by player` is printed to the chat.
Observer behavior: `player was blown up` is printed to the chat.
While this example setup uses creative mode, it's also possible for this to happen in a survival-only setting. Creative mode here is used to avoid getting damaged by the initial TNT block and the /tick command is used to make it more clear what is going on.

## Comments (2)

### Comment 1: migrated (2025-01-15T16:47:05.430-0800)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: clamlol (2025-01-19T15:23:54.036-0800)

Can confirm, but this may be intentional since the priming is unrelated to the proximate cause of the detonation.
