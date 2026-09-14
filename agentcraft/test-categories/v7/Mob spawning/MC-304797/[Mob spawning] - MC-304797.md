# MC-304797: Zombie nautiluses generated in ocean ruins are not persistent

**Mojira URL:** [https://bugs.mojang.com/browse/MC-304797](https://bugs.mojang.com/browse/MC-304797)

## Report details

- **Mojira categories:** Mob spawning
- **Project:** MC
- **Issue key:** MC-304797
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2025-12-05T10:52:21.759-0800
- **Updated:** 2025-12-08T04:15:29.518-0800
- **Resolution date:** 2025-12-08T04:15:29.472-0800
- **Affects versions:** 1.21.11 Release Candidate 2
- **Fix versions:** 1.21.11 Release Candidate 3
- **Area:** Expansion A
- **Votes:** 12
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** 202512060118.mp4
- **Issue links:** Relates:inward:MC-302842:Nautiluses and zombie nautiluses never despawn

## Description

Zombie nautilus generated as part of ocean ruins can despawn, unlike the drowned that generate there. This makes them despawn immediately when generating a ruin by walking/swimming/flying into range of it with render distance 8 or more, making them much harder to find.
Steps To Reproduce:
- Load the seed -8790581265353131111.

- /tp -9591 63 8825

- /tp @n[type=zombie_nautilus]
You should be teleported to the zombie nautilus in the ocean ruin.

- /tp ~ 256 ~, then /tp ~ 64 ~

- /tp @n[type=zombie_nautilus] again

Expected Result
You should be teleported to the zombie nautilus.
Actual Result
It’ll show “No entity was found”. The zombie nautilus from the ocean ruin disappeared.

## Comments (6)

### Comment 1: COMETC2021A1 (2025-12-05T10:52:22.837-0800)

This comment contained multiple media attachments (2), please login to view the attachments.

### Comment 2: Willy (2025-12-05T10:56:37.900-0800)

Can confirm, the zombie nautilus is not persistent.

### Comment 3: LNXSeus (2025-12-05T15:27:36.377-0800)

This is a really big deal, especially if the zombie nautilus is required for monsters hunted and replaces and potentially useful for the “How Did We Get Here?“ advancement.

### Comment 4: clamlol (2025-12-06T12:12:19.030-0800)

This is strange. There was no zombie nautilus at those coordinates, but I found one at /tp -7326 46 6539, inside the iceberg. But it took several attempts of me loading and unloading it for it to despawn, even though its PersistenceRequired was 0b and my render distance was 20.

### Comment 5: Custom Name (2025-12-07T05:44:38.115-0800)

Can confirm.

### Comment 6: bluecrab2 (2025-12-07T10:47:44.796-0800)

Last night, my sister and I were playing 1.21.11 Release Candidate 2 searching for four zombie nautili, two for the Monsters Hunted advancement and another two for mounts. We were exploring a large ocean for 2.5 hours with night vision and didn’t find any, and I think this bug may be the cause! We found 5 drowned wielding tridents that spawned right at underwater ruins on generation but none of them were riding a zombie nautilus. We had our render distance high so that would cause them to instantly despawn. In comparison, we had only found 2 trident wielding drowned in the open ocean. Sharing our impact statement to support if this can get fixed before release!
