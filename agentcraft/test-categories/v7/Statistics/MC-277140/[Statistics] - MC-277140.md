# MC-277140: The statistics screen does not visually differentiate the creaking and creaking_transient entities

**Mojira URL:** [https://bugs.mojang.com/browse/MC-277140](https://bugs.mojang.com/browse/MC-277140)

## Report details

- **Mojira categories:** Statistics
- **Project:** MC
- **Issue key:** MC-277140
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2024-10-02T13:35:03.176-0700
- **Updated:** 2025-04-26T16:59:03.278-0700
- **Resolution date:** 2024-11-10T15:05:12.405-0800
- **Affects versions:** 24w40a; 1.21.3
- **Fix versions:** 24w46a
- **Area:** Expansion A
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** 2024-10-02_22.13.37.png
- **Issue links:** Relates:outward:MC-277152:The statistic for killing a creaking doesn't increment when breaking a creaking heart

## Description

Killing and/or being killed by a creaking entity and a creaking_transient entity are shown in the statistics screen separately yet indistinguishably from each other.
How to reproduce:
- In a world with the Winter Drop experiment enabled, spawn a creaking with a spawn egg or execute the following command:

```
/summon creaking
```

- Kill the creaking you spawned.

- Place a creaking heart between two correctly aligned pale oak logs.

- Execute the following command:

```
/time set night
```

- Wait for the creaking to spawn.

- Execute the following command:

```
/damage @n[type=minecraft:creaking_transient] 1 minecraft:out_of_world by @s
```

- Look at your statistics.

Expected result:
The statistics for the different creaking entities would either be visually distinct or combined together.
Observed result:
The statistics for the different creaking entities are separated and visually indistinguishable.

## Comments (3)

### Comment 1: migrated (2024-10-02T13:35:03.176-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: Bee (2024-10-03T05:21:20.699-0700)

I'm really curious why Mojang decided to split 'Creaking' into two different entities. I originally thought the difference between naturally generated and command-generated Creaking was just in their NBT data (e.g., "creaking_heart_pos": [10, 100, 10]), similar to Vex. The only reason I can think of is that there are technical issues I don't understand.

### Comment 3: migrated (2024-10-03T11:51:15.088-0700)

@beebee "Artificial" creakings (a) take damage, (b) don't process any connected hearts, and (c) don't despawn during the day. My guess is that the sum total of these differences made them easier to implement as separate entities.
