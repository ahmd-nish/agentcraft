# MC-248092: Untamed cats on lead despawn when attached to fence post

**Mojira URL:** [https://bugs.mojang.com/browse/MC-248092](https://bugs.mojang.com/browse/MC-248092)

## Report details

- **Mojira categories:** Mob behaviour; Mob spawning
- **Project:** MC
- **Issue key:** MC-248092
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-01-10T12:38:34.782-0800
- **Updated:** 2026-03-12T00:46:08.596-0700
- **Resolution date:** 2026-03-12T00:46:08.549-0700
- **Affects versions:** 1.18.1; 1.19.2; 1.19.4; 1.21.5; 25w20a
- **Fix versions:** 26.1 Pre-Release 2
- **Area:** Platform
- **Votes:** 1
- **Watchers:** 2
- **Attachments:** 3
- **Attachment filenames:** 2022-01-11_07.47.10.png; 2022-01-11_07.49.53.png; 2023-04-20 - Minecraft 1.19.4.mp4

## Description

Description Edited for Clarity...
When you have an untamed cat or ocelot on a lead and you attach it to a fence post, the cat will de-spawn after a short period of time if you move too far away from it. This has been tested in multiple versions of Vanilla Minecraft since 1.18.1 and is confirmed in each of those versions.
How to reproduce bug:
1. Spawn a wild cat with either commands or an egg.
2. Attach a lead to the cat.
3. Attach the other end of the lead to a fence post.
4. Move about 100 blocks away and watch the cat through a spyglass.
5. After 15-120 seconds, the cat will de-spawn and leave the lead on the ground.
Behavior expected:
Other mobs such as wolves, foxes and trader llamas do not de-spawn when attached to a fence post with a lead. It's expected that cats and ocelots should not de-spawn when attached to a fence post with a lead.

## Comments (7)

### Comment 1: migrated (2022-01-10T12:38:34.782-0800)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: osfanbuff63 (2022-01-10T13:17:59.617-0800)

Please attach a screenshot of this occurring while the F3 debug screen is enabled.
This issue is being temporarily closed as Awaiting Response. Once the requested information has been delivered, the report will be reopened automatically.
Quick Links:
📓 Bug Tracker Guidelines – 💬 Community Support – 📧 Mojang Support
📓 Project Summary – ✍️ Feedback and Suggestions – 📖 Game Wiki

### Comment 3: NerdyDavros (2022-01-10T13:55:04.752-0800)

Recreated this bug in creative mode because I didn't want to loose anymore wild cats. As shown in the screenshot, I spawned two cats with the cat egg in creative and attached them to a fence post with leads. I quickly flew a number of chunks away and when I came back, one had despawned. Repeated flying away and when I came back, the second was despawned.

### Comment 4: Moesh (2022-01-26T23:43:36.793-0800)

Is this the vanilla server, or are you using a third-party server? It's hard to tell from the screenshots.

### Comment 5: NerdyDavros (2022-01-27T05:25:23.810-0800)

The screenshots where taken in vannila minecraft in a single-player creative world on version "1.18.1". I originally discovered this bug on my FabricMC survival server.
As mentioned before, I didn't want to loose any more wild cats in survival.

### Comment 6: NerdyDavros (2022-12-01T18:54:46.838-0800)

Confirmed that this is still happening in vanilla java 1.19.2.

### Comment 7: NerdyDavros (2025-05-13T23:06:55.104-0700)

Confirmed still happening in java snapshot 25w20a.
