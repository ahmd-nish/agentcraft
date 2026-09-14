# MC-249508: Light emitted from cave vines and glow lichens upon world generation still sometimes doesn't propagate across chunk borders

**Mojira URL:** [https://bugs.mojang.com/browse/MC-249508](https://bugs.mojang.com/browse/MC-249508)

## Report details

- **Mojira categories:** Lighting
- **Project:** MC
- **Issue key:** MC-249508
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2022-03-25T12:51:03.257-0700
- **Updated:** 2025-04-16T13:02:49.934-0700
- **Resolution date:** 2023-04-26T03:01:37.560-0700
- **Affects versions:** 22w12a; 22w13a; 22w15a; 22w17a; 1.19; 1.19.2; 1.19.3; 1.19.4 Release Candidate 1; 1.19.4
- **Fix versions:** 23w17a
- **Labels:** cave_vines; cave_vines_plant; glow_lichen
- **Watchers:** 1
- **Attachments:** 9
- **Attachment filenames:** 2022-03-25_17.02.17.png; MC-249508.mp4; MC-249508.png; MC-249508 (2).png; MC-249508 - 1.19.png; MC-249508 - 22w13a.png; MC-249508 - 22w15a.mp4; MC-249508 - 22w15a.png; MC-249508 - 22w17a.png
- **Issue links:** Duplicate:inward:MC-254198:Lighting fails over chunk borders in initial world generation | Cloners:outward:MC-218739:Glow berries and glow lichen generation does not cause light updates across chunk borders

## Description

The Bug:
Light emitted from cave vines and glow lichens upon world generation still sometimes doesn't propagate across chunk borders.
Please note that this issue occurs inconsistently and therefore cannot be reliably reproduced.
Here is an example:
Version: 1.19.4

```
Seed: -2284214782727173621
Coordinates: /execute in minecraft:overworld run tp @s 2824.69 -30.54 -1906.49 -672.08 25.00
```
Steps to Reproduce:
- Generate a world with the seed provided above and teleport to the given coordinates.

- Observe your surroundings and look closely at the lighting emitted from the cave vines or glow lichens.

- Take note as to whether or not light emitted from cave vines and glow lichens upon world generation still sometimes doesn't propagate across chunk borders.

Observed Behavior:
Light doesn't propagate across chunk borders.
Expected Behavior:
Light would propagate across chunk borders.

## Comments (6)

### Comment 1: migrated (2022-03-25T12:51:03.257-0700)

This comment contained multiple image attachments (9), please login to view the attachments.

### Comment 2: Avoma (2022-03-25T12:51:35.446-0700)

This ticket clones MC-218739.

### Comment 3: Panda4994 (2022-04-19T07:00:20.335-0700)

Hello , I couldn't find a way to reproduce the issue so far.
Did this by any chance occur together with  or an other chunk saving issue?
Some of the reasons for MC-218739 were chunks not saving properly, it could still be a similar cause.
Are there any warnings or errors in the log when it happens?
Also do you know if it can happen the first time chunks are loaded, or does it appear in worlds after moving around and loading/unloading the chunks?

### Comment 4: Avoma (2022-04-19T09:56:22.158-0700)

Hi , thanks for your response.
Nope, I can confidently say that this issue didn't occur together with  as that was fixed in 22w13a, and I'm still able to reproduce this same problem () in 22w15a, however, I'm unsure if this occurred alongside any other chunk saving issues, so I apologize in advance about this.
I've just tested this now using a vanilla instance of 22w15a with a completely new generated world and was able to reproduce this. At the time of when I did so, no errors or warnings were printed into the game output console and in my testing, this appeared to happen the first time chunks were loaded. Unloading and reloading the chunks where this issue was present in didn't appear to change anything and the lighting error still occurred.
Below is some information on where I experienced this in 22w15a. I've also attached an additional video along with a screenshot. Please let me know if you require any additional details and/or information regarding this problem and I'll do my best to supply you with it.  Thanks!
Version: 22w15a

```Seed: -168050448401021573
Coordinates: /execute in minecraft:overworld run tp @s -46.79 -39.73 242.87 201.68 42.11```

### Comment 5: ampolive (2022-04-19T10:41:10.715-0700)

This issue is related to and potentially caused by .

### Comment 6: Avoma (2022-07-14T11:30:17.945-0700)

This issue appears to occur with any naturally generating block upon world generation that emits light and is not just exclusive to cave vines and glow lichens. I saw this same problem with fire in the nether, sea pickles in warm oceans, torches in mineshafts, etc... Would it be okay to update this ticket to include this new information (since I'm the reporter)?
