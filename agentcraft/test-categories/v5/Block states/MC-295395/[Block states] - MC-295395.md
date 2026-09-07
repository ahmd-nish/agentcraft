# MC-295395: Entities interact differently with nether portals

**Mojira URL:** [https://bugs.mojang.com/browse/MC-295395](https://bugs.mojang.com/browse/MC-295395)

## Report details

- **Mojira categories:** Block states
- **Project:** MC
- **Issue key:** MC-295395
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2025-03-15T13:37:50.688-0700
- **Updated:** 2025-04-27T13:32:33.278-0700
- **Resolution date:** 2025-04-14T00:36:06.799-0700
- **Affects versions:** 1.21.5 Pre-release 2
- **Fix versions:** 25w16a
- **Area:** Platform
- **Votes:** 150
- **Watchers:** 2
- **Attachments:** 2
- **Attachment filenames:** 1.21.4.mp4; 25w09a.mp4
- **Issue links:** Relates:inward:MC-101556:Nether Portal teleport range is too large (equivalent to a full block) | Duplicate:inward:MC-297292:Portals only work when standing in the absolute center.

## Description

Affected versions: 25w04a, 25w05a, 25w06a, 25w07a, 25w08a, 25w09a, 25w09b, 25w10a, 1.21.5-pre1, 1.21.5-pre2
 Summary: All entities hitbox needs to be intersecting the nether portal blocks hitbox in order to teleport to the other dimension rather then just being in the same block space as the portal block like before. In the latest release (1.21.4) an entity's hitbox needed to be within the block space of a nether portal block to be teleported, in the latest snapshot their hitbox needs to intersect the portal blocks hitbox, this change wasn't mentioned in the changelog and can break some redstone contraptions such as the basic minecart or boat based chunk loaders.
Steps to Reproduce:
- Build a nether portal
- Load the nether side then come back. (This removes the initial lag from loading the nether for the first time)

- Place down a boat a few blocks away from the portal and get in it.

- Turn on hitboxes (F3 + B).

- Slowly ride the boat into the portal and keep an eye on where the edge of the hitbox is before being teleported (F5 helps).

- See that it doesn't get teleported until touching the portal blocks hitbox.

 See attached videos below of before/after with minecart example causing the minecart to take longer to go though the portal
Observed Results: Entities need to be intersecting the nether portal block to be teleported.
Expected Results: Entities should only need to be within the same block space as the nether portal block to be teleported like in previous versions.
Further information 05/03/25: after further testing i have found that the issue happens from a change to either nether portal blocks or entities (as it seems to affact boats/horses/items as well) where their hitbox now needs to touch the hitbox of the nether portal block rather then just being within the same block space as the portal block

## Comments (6)

### Comment 1: MrMuskle (2025-03-16T01:30:25.257-0700)

The previous behavior was tracked as a bug in MC-101556. However, since that report did not have a Mojang Priority and was not resolved by Piston, its resolution as Fixed does not conclusively indicate which behavior is the intended one.

### Comment 2: [Mojang] Triage Team (2025-03-20T01:01:30.340-0700)

Thank you for your report!
After consideration, the issue is being closed as Working as Intended.
Please note, that mechanics of the game may change between updates.
Things such as graphics, sounds, world creation, biomes, redstone, villagers, and animals may not work the same in current versions.
Full Version History – Snapshot Version History – The official Minecraft feedback site
Quick Links:
📓 Bug Tracker Guidelines – 💬 Community Support – 📧 Mojang Support (Technical Issues) – 📧 Microsoft Support (Account Issues)
📓 Project Summary – ✍️ Feedback and Suggestions – 📖 Game Wiki

### Comment 3: BJTMastermind (2025-03-20T15:04:15.411-0700)

Thanks for the clarification on the issue. MC-101556 wasn’t mentioned anywhere in the 25w04a or later snapshot changelogs as being fixed so i wasn’t sure if it was intended or not.

### Comment 4: MadMan25 (2025-03-26T14:24:12.065-0700)

This needlessly breaks so many technical contraptions that have worked for years.  Please reconsider this change.

### Comment 5: GaRLic_BrEd_ (2025-03-26T16:26:01.607-0700)

Please reconsider marking this as working as intended, many mob farms and chunk loaders are now broken because of this. Portals have behaved like that for years and it doesn’t make much sense to change it now.

### Comment 6: [Mod] turbo (2025-04-09T06:25:23.646-0700)

We delete comments that do not contribute anything new regarding the reproduction of the bug report, especially if they just repeat information that is already known. If you have feedback, please use the Minecraft Feedback website, and if you want to discuss, go to Reddit or Discord. The Jira comments section is not the right place for complaints, especially not in a dismissive tone. That said, this bug report is currently pending Mojang review for a second evaluation to determine whether this is actually working as intended or not. Please refrain from posting such comments (I will remove this one shortly, as it adds nothing of value).
