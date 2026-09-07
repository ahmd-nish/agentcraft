# MC-96449: Rabbits sometimes don't drop any raw rabbit upon being killed

**Mojira URL:** [https://bugs.mojang.com/browse/MC-96449](https://bugs.mojang.com/browse/MC-96449)

## Report details

- **Mojira categories:** Loot tables
- **Project:** MC
- **Issue key:** MC-96449
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2016-01-31T14:04:52.772-0800
- **Updated:** 2025-04-30T05:33:03.319-0700
- **Resolution date:** 2023-02-15T01:42:35.546-0800
- **Affects versions:** Minecraft 1.8.9; Minecraft 16w04a; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 1.12.1; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 19w05a; Minecraft 19w06a; Minecraft 19w07a; 1.15.2; 1.16.1; 1.16.4; 20w48a; 1.16.5; 21w05b; 21w06a; 21w07a; 21w11a; 21w16a; 21w17a; 1.17; 1.17.1; 21w40a; 21w42a; 21w43a; 21w44a; 1.18 Pre-release 1; 1.18 Pre-release 7; 1.18; 1.18.1; 22w03a; 22w05a; 22w06a; 1.18.2 Release Candidate 1; 1.18.2; 22w17a; 1.19; 1.19.2
- **Fix versions:** 22w42a
- **Labels:** rabbit
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-96449.mp4; MC-96449 - rabbit.json.png
- **Issue links:** Relates:outward:MCPE-167093:Rabbits don't always drop raw rabbit upon being killed

## Description

The Bug:
Rabbits sometimes don't drop any raw rabbit upon being killed.
Every passive mob drops at least one piece of meat upon being killed, however, this isn't the case for rabbits.
Steps to Reproduce:
- Summon a rabbit.

```
/summon minecraft:rabbit ~ ~ ~ {NoAI:1b,Health:1f}
```
- Kill it and take note of the loot it dropped.

- If it dropped some meat, continue to spawn and kill rabbits until one of them doesn't.

- Take note as to whether or not rabbits sometimes don't drop any raw rabbit upon being killed.

Observed Behavior:
Rabbits sometimes don't drop any raw rabbit upon being killed.
Expected Behavior:
Rabbits would always drop at least one piece of meat upon being killed.
Code Analysis:
Code analysis by  can be found below.
data > minecraft > loot_tables > entities > rabbit.json

```
{
  "type": "minecraft:entity",
  "pools": [
    ...
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            ...
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "minecraft:rabbit"
        }
      ],
      "rolls": 1.0
    },
    ...
```
If we look at the above json file, we can see that rabbits can drop a maximum of 1 raw rabbit and a minimum of 0 upon being killed, disregarding the use of the looting enchantment. This means that there is a 50% chance of a rabbit dropping raw rabbit upon death, thus resulting in this problem. Every other animal throughout the game such as cows, pigs, sheep, etc... have their minimum respective meat drop set to 1, meaning that they always have a guaranteed chance of dropping meat upon being killed, however, this isn't the case with rabbits as shown above.

## Comments (22)

### Comment 1: migrated (2016-01-31T14:04:52.772-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: migrated (2016-01-31T15:14:39.712-0800)

Rabbits are very small.

### Comment 3: migrated (2016-02-03T10:21:10.808-0800)

Wheat seeds are very small.

### Comment 4: [Mod] bemoty (2017-08-15T17:16:43.778-0700)

Can confirm for MC 1.12.1.

### Comment 5: migrated (2018-09-10T11:01:55.124-0700)

Confirmed for 1.13.1.
Although, this is most likely intended.

### Comment 6: migrated (2020-02-01T05:47:33.442-0800)

Confirmed for 1.15.2

### Comment 7: j_p_smith (2020-06-29T12:39:12.684-0700)

Confirmed in 1.16.1.

### Comment 8: DavidMohr2012 (2020-06-29T13:07:02.869-0700)

Actually is pretty normal for a rabbit to not drop meat sometimes, it has a chance of droping it, unlike pigs or cows that aways drop at least 1 meat

### Comment 9: Avoma (2020-11-26T11:18:42.674-0800)

Can confirm in 20w48a.

### Comment 10: Avoma (2021-02-06T12:42:46.453-0800)

Can confirm in 21w05b.

### Comment 11: Brevort (2021-02-14T11:25:46.430-0800)

Confirmed for 1.16.5

### Comment 12: Avoma (2021-02-16T06:18:24.765-0800)

Can confirm in 21w06a. Video attached.

### Comment 13: Avoma (2021-02-19T08:04:00.136-0800)

Can confirm in 21w07a.

### Comment 14: Avoma (2021-03-23T09:59:02.606-0700)

Can confirm in 21w11a.

### Comment 15: Avoma (2021-04-25T09:35:24.497-0700)

Can confirm in 21w16a.

### Comment 16: Avoma (2021-05-02T09:43:53.955-0700)

Can confirm in 21w17a.

### Comment 17: Avoma (2021-06-12T06:38:03.305-0700)

Can confirm in 1.17.

### Comment 18: Avoma (2021-07-08T11:43:25.996-0700)

Can confirm in 1.17.1.

### Comment 19: Avoma (2021-10-09T01:37:37.791-0700)

Can confirm this behavior in 21w40a. Here are some extra details regarding this problem.
The Bug:
Rabbits sometimes don't drop meat upon being killed.
Steps to Reproduce:
- Summon a rabbit.

```/summon minecraft:rabbit ~ ~ ~ {NoAI:1b,Health:1f}```
- Kill it and take note of the loot it dropped.

- If it dropped some meat, continue to spawn and kill rabbits until one of them doesn't.

Observed Behavior:
Rabbits sometimes don't drop meat upon being killed.
Expected Behavior:
Rabbits would always drop meat upon being killed, just like how every other animal does.

### Comment 20: Avoma (2021-10-20T07:31:59.246-0700)

Can confirm in 21w41a.

### Comment 21: Avoma (2021-10-25T03:30:31.670-0700)

Can confirm in 21w42a. I'd like to request ownership of this ticket since the current reporter has been inactive for over a year. I've willing to continue to provide all of the necessary information and will keep this report updated.

### Comment 22: migrated (2022-10-26T18:44:36.034-0700)

Good to see it's fixed after 7 years.
