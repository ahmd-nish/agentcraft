# MC-275279: Raiders do not spawn on small islands even though there are close enough places around the village

**Mojira URL:** [https://bugs.mojang.com/browse/MC-275279](https://bugs.mojang.com/browse/MC-275279)

## Report details

- **Mojira categories:** Raids
- **Project:** MC
- **Issue key:** MC-275279
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-08-15T11:30:42.179-0700
- **Updated:** 2025-04-26T16:09:10.737-0700
- **Resolution date:** 2024-08-22T02:27:13.551-0700
- **Affects versions:** 24w33a
- **Fix versions:** 24w35a
- **Area:** Expansion B
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 2024-08-16_04.19.52.png; 2024-08-17_12.24.35.png; Screenshot_2024-08-14-20-50-04-430_com.mojang.minecraftpe.jpg

## Description

As the 24w33a changelog says:
- A triggered raid will no longer start if the raiders cannot find a place to spawn within a reasonable distance of the village they are trying to raid

However, I noticed that raiders sometimes would not spawn even if there are close enough places around the village.
Steps to reporduce:
- Create a default type world with seed: 23925373020405760

- Teleport to 204 65 110

- Place a composter at 202 62 111 and summon a villager beside it

- Drink a ominous bottle

- Wait for a minute and the raid ends without any raiders spawned

- Repeat steps 4 and 5

## Comments (6)

### Comment 1: migrated (2024-08-15T11:30:42.179-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: Alex_light (2024-08-15T11:44:03.415-0700)

related to .

### Comment 3: Youmiel (2024-08-15T13:55:56.366-0700)

Please don't add unrelated screenshot and issues. This is a new issue that only exists in 24w33a Java Edition, since Mojang has made changes to raid and stated that raiders would spawn "within a reasonable distance"

### Comment 4: BugTracker_ (2024-08-15T13:56:16.422-0700)

Can confirm.

### Comment 5: Ray (2024-08-17T10:26:33.944-0700)

it seems it only spawns them in a small area if village is same Y level as spawning area. iron block is where they spawn. notice that out ring has no problem spawning more on top of each other but inner ring only spawns at that Y level.

### Comment 6: litetex (2024-08-19T06:28:07.008-0700)

Just for further reference:
This likely describes the same problem as I already mentioned in https://bugs.mojang.com/browse/MC-274911#comment-1347741
