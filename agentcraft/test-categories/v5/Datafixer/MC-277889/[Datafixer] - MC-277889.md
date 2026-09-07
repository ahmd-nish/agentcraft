# MC-277889: Villagers' iron golem detection range is increased for villagers upgraded from 1.21.1 or earlier

**Mojira URL:** [https://bugs.mojang.com/browse/MC-277889](https://bugs.mojang.com/browse/MC-277889)

## Report details

- **Mojira categories:** Datafixer; Mob behaviour
- **Project:** MC
- **Issue key:** MC-277889
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2024-10-27T21:09:06.938-0700
- **Updated:** 2025-04-26T17:18:53.906-0700
- **Resolution date:** 2024-12-12T11:29:49.224-0800
- **Affects versions:** 24w44a; 1.21.3
- **Fix versions:** 1.21.4 Release Candidate 3
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2024-10-31_00-17-07_New World (1).zip; MC-277889.zip
- **Issue links:** Duplicate:inward:MC-277898:Iron Golem Not Spawn Anywhere

## Description

According to the Minecraft Wiki, an Iron Golem is detected by a Villager when it is within 16 blocks of the villager.
I have recently discovered that the Iron Golem Detection range for villager is far greater than that in 1.21.2 and 1.21.3, while it works as intended in 1.21.1. I assume it must be a bug as I have not seen any patch notes regarding the Iron Golem detection range.
The detection range in 1.21.2 and 1.21.3 is about 45 blocks instead of 16. This can easily be tested by placing three Villagers with a bed each and a Zombie to scare, and an Iron Golem more than 16 but less than about 45 blocks away from the Villagers - in every version up to 1.21.1 (including 1.21.1), the Villagers will spawn a new Iron Golem if there is any space for it. In 1.21.2 and upwards, the Villagers won't be able to spawn a new Iron Golem. Using gnembon's Carpet mod, you can also see the Villager's "Iron Golem Seen" counter go back to 600 ticks every 10 seconds after counting down.
How to reproduce:
Attached is a world in 1.21.1 containing an iron farm, an iron golem placed 18 blocks away from the villagers, and a repeating command block to check the last time a villager detected an iron golem around.
- Open the attached world (

- ) in 1.21.1.

- Periodically check the repeating command block's output until there is no number in the output, at which point the villagers will try to spawn a golem.

- Wait until the villagers spawn a golem.
→  The villagers successfully spawn a golem.

- Upgrade the world to 1.21.2 or higher.

- Periodically check the repeating command block's output.
→  The output never reaches 0, which means the villagers now detect the iron golem that is 18 blocks away, so they will never spawn a golem.

Expected result:
The villagers' iron golem detection range would not change when upgrading to a newer version.
Observed result:
The villagers' iron golem detection range changes from [0, 16] to [16, ~45] when upgrading to a newer version.

## Comments (10)

### Comment 1: migrated (2024-10-27T21:09:06.938-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: [Mod] ManosSef (2024-10-28T11:19:53.819-0700)

I cannot reproduce this. With an iron golem 21 blocks away from the villagers, more iron golems do spawn around the villagers for me.

### Comment 3: migrated (2024-10-28T14:08:56.385-0700)

It turned out this only happened after a version upgrade from my 1.20.1 world. Killing and respawning the villagers in question fixed the issue.

### Comment 4: Jarl-Penguin (2024-10-30T11:52:48.877-0700)

Do you happen to have a backup of the affected world that was last opened in 1.20.1?
This issue is being temporarily resolved as Awaiting Response. Once the requested information has been delivered, the report will be reopened automatically.
Quick Links:
📓 Bug Tracker Guidelines – 💬 Community Support – 📧 Mojang Support (Technical Issues) – 📧 Microsoft Support (Account Issues)
📓 Project Summary – ✍️ Feedback and Suggestions – 📖 Game Wiki

### Comment 5: migrated (2024-10-30T14:35:54.624-0700)

I have the same issue on a world which was fine on 1.21.1. Killing all the iron golems in a big radius (+-50) blocks makes the farm work again, but the moment one appears the farm breaks again.

### Comment 6: migrated (2024-10-30T16:23:35.093-0700)

The file limit is 10MB, my world is about 2.3GB, so I made a void world in 1.20.1 and tested it again before and after upgrading to 1.21.2. Same thing happened - worked fine in 1.20.1, breaks in 1.21.2. I uploaded a 1.20.1 backup of the void test world. The "village-setup" is located at X:0 Y:100 Z:0.

### Comment 7: [Mod] ManosSef (2024-10-31T09:53:02.200-0700)

I can reproduce this issue, and I have attached a world for easier reproduction.

### Comment 8: yukira2018 (2024-11-01T15:29:59.105-0700)

Similar issues my world is created on 1.20 upgraded it to and 1.21.3. When im tested i found villagers can now detect iron golem within 53blocks radius.

### Comment 9: migrated (2024-11-09T15:05:19.950-0800)

I can confirm I have also experienced this bug, world (Java Server, running Fabric), was upgraded from 1.21.1 to 1.21.3, upon update all Golems stopped spawning in my farm (I had a player-built, nametagged, Golem around 25-30 blocks from the villagers, said Golem had not been moved since before the update, it had been leashed to a fence post), within seconds of killing said Golem the farm immediately started working again.
I cannot provide a world download but I can link the exact farm design used and relative position of the player made Golem if needed

### Comment 10: Minecraft386882 (2024-11-10T21:50:43.239-0800)

Confirmed in 24w45a
