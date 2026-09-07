# MC-266318: Trapdoors and doors have inconsistent subtitles for being opened and closed

**Mojira URL:** [https://bugs.mojang.com/browse/MC-266318](https://bugs.mojang.com/browse/MC-266318)

## Report details

- **Mojira categories:** Accessibility; Sound
- **Project:** MC
- **Issue key:** MC-266318
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2023-11-02T09:43:05.043-0700
- **Updated:** 2025-05-29T09:08:44.348-0700
- **Resolution date:** 2025-03-25T09:51:07.285-0700
- **Affects versions:** 23w44a; 1.20.3 Pre-Release 1; 24w03b; 24w10a; 24w19b; 1.21; 1.21.1; 24w35a; 1.21.3; 1.21.4
- **Fix versions:** 25w15a
- **Area:** Expansion B
- **Labels:** door; trapdoor
- **Watchers:** 2
- **Attachments:** 1
- **Attachment filenames:** MC-266318.mkv

## Description

The Bug:
Trapdoors and doors have inconsistent subtitles for being opened and closed.
Affected Subtitles:
Before reading the tables, please note the following:
- Characters colored in GREEN are correct and show consistent behavior.

- Characters colored in RED are incorrect and show inconsistent behavior.

Trapdoor Type
Open Sound
Open Subtitle
Close Sound
Close Subtitle
Oak
minecraft:block.wooden_trapdoor.open
Trapdoor creaks
minecraft:block.wooden_trapdoor.close
Trapdoor creaks
Spruce
minecraft:block.wooden_trapdoor.open
Trapdoor creaks
minecraft:block.wooden_trapdoor.close
Trapdoor creaks
Birch
minecraft:block.wooden_trapdoor.open
Trapdoor creaks
minecraft:block.wooden_trapdoor.close
Trapdoor creaks
Jungle
minecraft:block.wooden_trapdoor.open
Trapdoor creaks
minecraft:block.wooden_trapdoor.close
Trapdoor creaks
Acacia
minecraft:block.wooden_trapdoor.open
Trapdoor creaks
minecraft:block.wooden_trapdoor.close
Trapdoor creaks
Dark Oak
minecraft:block.wooden_trapdoor.open
Trapdoor creaks
minecraft:block.wooden_trapdoor.close
Trapdoor creaks
Mangrove
minecraft:block.wooden_trapdoor.open
Trapdoor creaks
minecraft:block.wooden_trapdoor.close
Trapdoor creaks
Cherry
minecraft:block.cherry_wood_trapdoor.open
Trapdoor creaks
minecraft:block.cherry_wood_trapdoor.close
Trapdoor creaks
Bamboo
minecraft:block.bamboo_wood_trapdoor.open
Trapdoor creaks
minecraft:block.bamboo_wood_trapdoor.close
Trapdoor creaks
Crimson
minecraft:block.nether_wood_trapdoor.open
Trapdoor creaks
minecraft:block.nether_wood_trapdoor.close
Trapdoor creaks
Warped
minecraft:block.nether_wood_trapdoor.open
Trapdoor creaks
minecraft:block.nether_wood_trapdoor.close
Trapdoor creaks
Iron
minecraft:block.iron_trapdoor.open
Trapdoor opens
minecraft:block.iron_trapdoor.close
Trapdoor closes
Copper
minecraft:block.copper_trapdoor.open
Trapdoor opens
minecraft:block.copper_trapdoor.close
Trapdoor closes

Door Type
Open Sound
Open Subtitle
Close Sound
Close Subtitle
Oak
minecraft:block.wooden_door.open
Door creaks
minecraft:block.wooden_door.close
Door creaks
Spruce
minecraft:block.wooden_door.open
Door creaks
minecraft:block.wooden_door.close
Door creaks
Birch
minecraft:block.wooden_door.open
Door creaks
minecraft:block.wooden_door.close
Door creaks
Jungle
minecraft:block.wooden_door.open
Door creaks
minecraft:block.wooden_door.close
Door creaks
Acacia
minecraft:block.wooden_door.open
Door creaks
minecraft:block.wooden_door.close
Door creaks
Dark Oak
minecraft:block.wooden_door.open
Door creaks
minecraft:block.wooden_door.close
Door creaks
Mangrove
minecraft:block.wooden_door.open
Door creaks
minecraft:block.wooden_door.close
Door creaks
Cherry
minecraft:block.cherry_wood_door.open
Door creaks
minecraft:block.cherry_wood_door.close
Door creaks
Bamboo
minecraft:block.bamboo_wood_door.open
Door creaks
minecraft:block.bamboo_wood_door.close
Door creaks
Crimson
minecraft:block.nether_wood_door.open
Door creaks
minecraft:block.nether_wood_door.close
Door creaks
Warped
minecraft:block.nether_wood_door.open
Door creaks
minecraft:block.nether_wood_door.close
Door creaks
Iron
minecraft:block.iron_door.open
Door creaks
minecraft:block.iron_door.close
Door creaks
Copper
minecraft:block.copper_door.open
Door creaks
minecraft:block.copper_door.close
Door creaks
h3. Steps to Reproduce:
- Ensure that you have subtitles enabled.

- Place down a copper door and a copper trapdoor.

- Open and close them both and pay attention to the subtitles that are displayed.

Observed Behavior:
Iron and copper trapdoors have unique subtitles for being opened and closed, which is inconsistent.
Expected Behavior:
Iron and copper trapdoors would display the "Trapdoor creaks" subtitle upon being opened and closed, therefore maintaining consistency.

## Comments (4)

### Comment 1: migrated (2023-11-02T09:43:05.043-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: AMGAMES04 (2023-11-09T12:07:08.062-0800)

Can confirm in 23w45a

### Comment 3: migrated (2023-11-12T15:19:49.428-0800)

This may or may not be a bug. The fact that they are both ore and not wooden trap doors is a big difference. There are two possible things happening here. One, the copper trapdoor and iron trapdoor sounds are a bug, or two, they are not a bug and the iron door and copper door were accidentally given the same sounds as the wooden doors. This is confirmed though, so there is no doubt that there is a bug somewhere, be it with the trapdoor or the doors.

### Comment 4: muzikbike (2024-10-25T11:01:35.747-0700)

Expected behaviour could also be for the wooden door types to have specific open/close subtitles.
