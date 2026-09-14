# MC-306814: `environment_attribute` value providers give incorrect results on subsequent accesses within a tick

**Mojira URL:** [https://bugs.mojang.com/browse/MC-306814](https://bugs.mojang.com/browse/MC-306814)

## Report details

- **Mojira categories:** Data Packs
- **Project:** MC
- **Issue key:** MC-306814
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2026-03-11T11:43:28.775-0700
- **Updated:** 2026-03-12T06:47:19.567-0700
- **Resolution date:** 2026-03-12T06:47:19.502-0700
- **Affects versions:** 26.1 Pre-Release 1
- **Fix versions:** 26.1 Pre-Release 2
- **Area:** Platform EC
- **Votes:** 4
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** Bugreport Datapack.zip

## Description

Expected behaviour
Either:
- Whenever an environment attribute changes (e.g. as a result of a command inside a function), reading from the environment attribute using a number provider (e.g. in a loot table) retrieves the updated value
- (Note: Could be implemented by marking attributes as dirty when an associated timeline changes its value, and updating them when read while dirty, with the idea being that the attribute doesn’t update unnecessarily if a lot of timelines are associated)

- Environment attributes update at a pre-defined point in the tick order
- (Note: Simpler, but slightly less useful for users because reading would not take previous modifications earlier in the tick into account)

=> Reading an environment attribute should never affect the outcome of future reads
What happens instead
Reading from an environment attribute using a number provider “locks” it to the same value for all subsequent calls for the remainder of the tick, even though the actual value updates correctly (at least by the end of the tick).
How to reproduce
- Download the attached Data Pack and install it in a new world

- Run the function bugreport:test/1
- Observation: It works as expected, because the value is read only once, after the modification is complete

- Run the function bugreport:test/2
- Observation: The 2nd modification of the bugreport:test timeline (A function call for bugreport:test/1) changes the cloud height as expected, but the value that’s read is the same as before the modification

Data Pack Explanation
Timelines:
- bugreport:test’s value is added to the overworld’s cloud height

Functions:
- bugreport:test/reset_cloud_height sets the timeline to 0 and prints the (correct) default cloud height. Helper function for testing bugreport:test/1.

- bugreport:test/1 sets the timeline to 128 (adds 128 to the cloud height) and prints the cloud height in chat

- bugreport:test/2 first sets the timeline to 0, prints it in chat, then runs bugreport:test/1 (which prints the wrong value because it was already read after setting the timeline to 0)

## Comments (1)

### Comment 1: Automation for Jira (2026-03-11T11:43:36.058-0700)

Thank you for helping us improve Minecraft! We saved your files:
