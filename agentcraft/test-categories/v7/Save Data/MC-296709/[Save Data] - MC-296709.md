# MC-296709: All non-default jukebox_playable components are deleted from existing items when updating past 1.21.4

**Mojira URL:** [https://bugs.mojang.com/browse/MC-296709](https://bugs.mojang.com/browse/MC-296709)

## Report details

- **Mojira categories:** Commands; Save Data
- **Project:** MC
- **Issue key:** MC-296709
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2025-04-13T20:31:22.639-0700
- **Updated:** 2025-05-05T04:05:20.780-0700
- **Resolution date:** 2025-05-05T04:05:20.715-0700
- **Affects versions:** 1.21.5; 25w15a
- **Fix versions:** 25w19a
- **Area:** Platform
- **Votes:** 5
- **Watchers:** 1
- **Attachments:** 0
- **Issue links:** Duplicate:inward:MC-296708:Data from the 'jukebox_playable' component doesn't carry over from older versions.

## Description

When updating existing worlds from 1.21.4 to either 1.21.5 or 25w15a, all existing items with a non-default jukebox_playable component are not updated properly, resulting in the component being deleted and permanently altering all such items in the world. This is due to the jukebox_playable component changing forms in 1.21.5, although it seems like the datafixer was not properly updated to handle this specific case.

Steps to reproduce:
- Open a world in 1.21.4 and run the following give command

```
/give @s gravel[jukebox_playable={song:"13"}]
```
- Close the world and open in 1.21.5 (or a newer snapshot). Notice that the item no longer has a jukebox_playable component. If the item given in 1.21.4 was a vanilla record item but was given a custom song, the stored component will be lost, so the item would then default back to its usual song.

Opening the output log shows the following error:

```
Tried to load invalid item: 'Failed to parse either. First: Not a string; Second: Not a string missed input: {"minecraft:jukebox_playable":{song:"minecraft:13"}}'
```

Expected behavior:
The game should have automatically updated the component from {song:”minecraft:13”} to “minecraft:13” since this is the new format of the component as of 1.21.5. This doesn’t seem to have affected the other components that were similarly changed to no longer have a show_in_tooltip field, though I have not tested all of these other cases. This is quite a dangerous bug, as it results in a loss of data when updating between major versions.

## Comments (0)

No comments were available in the downloaded comment corpus.
