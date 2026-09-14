# MC-210612: Strongholds do not generate in certain customized worlds despite /locate saying otherwise

**Mojira URL:** [https://bugs.mojang.com/browse/MC-210612](https://bugs.mojang.com/browse/MC-210612)

## Report details

- **Mojira categories:** Custom Worlds; Structures
- **Project:** MC
- **Issue key:** MC-210612
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-01-05T08:25:50.621-0800
- **Updated:** 2025-03-25T13:23:42.285-0700
- **Resolution date:** 2022-08-31T00:35:51.915-0700
- **Affects versions:** 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w10a; 21w11a; 21w15a; 1.17 Pre-release 5; 1.17
- **Fix versions:** 1.18.2 Pre-release 1
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** 210612.json

## Description

The bug
Strongholds do not generate in certain customized worlds despite /locate saying otherwise. At first, I thought it was caused by blackstone as default block. Later, it turned out that it was not generating at all. Then, I thought it might be caused by effects being set to nether. Even with overworld effects there was no stronghold.
How to reproduce
- Download the

-  file

- Import it to a new creative world

- Use /locate stronghold

- Teleport there

- Set your game to spectator mode

- Fly down
 →  No actual stronghold, but the message from /locate still says that there is a stronghold

Might be caused by the biome distribution having nether biomes. The best possible fix might be to make strongholds generation independent on biomes, but on the worldgen import.

## Comments (7)

### Comment 1: migrated (2021-01-05T08:25:50.621-0800)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: Michael Wobst (2021-02-02T09:22:46.999-0800)

Please provide an updated custom world file so the issue can be reproduced. The attached file causes the parser to throw several errors.

### Comment 3: migrated (2021-02-02T22:25:37.820-0800)

Here it is.

### Comment 4: migrated (2021-06-03T14:41:52.995-0700)

Cannot reproduce.

### Comment 5: migrated (2021-06-03T22:06:58.607-0700)

I can. Here's a new working worldgen import.

### Comment 6: migrated (2021-06-09T10:11:08.183-0700)

Can confirm in 1.17.

### Comment 7: Michael Wobst (2022-01-16T00:02:33.319-0800)

The attached settings file is no longer compatible with 1.18.1. If this is still an issue, please provided an updated worldgen settings file. Thanks!
