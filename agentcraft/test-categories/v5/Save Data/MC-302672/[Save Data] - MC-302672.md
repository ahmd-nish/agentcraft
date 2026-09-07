# MC-302672: "Invalid player data" error when loading a world in which you have an effect applied

**Mojira URL:** [https://bugs.mojang.com/browse/MC-302672](https://bugs.mojang.com/browse/MC-302672)

## Report details

- **Mojira categories:** Save Data
- **Project:** MC
- **Issue key:** MC-302672
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2025-10-09T08:02:24.722-0700
- **Updated:** 2025-11-03T12:42:40.567-0800
- **Resolution date:** 2025-10-12T23:34:18.300-0700
- **Affects versions:** 25w41a
- **Fix versions:** 25w42a
- **Area:** Platform
- **Votes:** 38
- **Watchers:** 6
- **Attachments:** 4
- **Attachment filenames:** 2025-10-09_17.00.42.png; 2025-10-09_17.00.45.png; image-20251012-133531.png; Screenshot 2025-10-09 165645.png
- **Issue links:** Duplicate:inward:MC-302710:Loading a world that you are riding a nautilus in causes you to be disconnected with the "invalid player data" message. | Duplicate:inward:MC-302706:Closing World While Riding Nautilus Causes Invalid Player Data Error on Relaunch | Duplicate:inward:MC-302747:Turtle Helmet when equipped causes corrupt player data | Duplicate:inward:MC-302738:Logging out with a status effect causes invalid player data | Duplicate:inward:MC-302730:Leaving and rejoining a world with a potion effect causes invalid player data | Duplicate:inward:MC-302739:can't load world | Duplicate:inward:MC-302800:Worlds get bricked | Duplicate:inward:MC-302797:Opening worlds does not work and instead says "Invalid Player Data" | Duplicate:inward:MC-302756:Invalid player data when trying to join worlds that aren't newly created | Duplicate:inward:MC-302821:Some save files cannot be opened | Duplicate:inward:MC-302779:Can't rejoin new world. Invalid Player Data error | Duplicate:inward:MC-302832:Quitting a world while mounting a nautilus ruins the save. | Duplicate:inward:MC-302833:Я когда вышел из мира я видел и сохранился нормально и тепер не могу зайти | Duplicate:inward:MC-302843:Players cannot enter the game while holding the effects of a potion | Duplicate:inward:MC-302850:"Invalid Player Data" error when upgrading world to 25w41a from previous version when within range of a beacon/conduit | Duplicate:inward:MC-302853:Worlds can't be reopened in 25w41a | Duplicate:inward:MC-302859:corrupted playerdata whuile disconnecting while mounted on nautilus 25w41a | Duplicate:inward:MC-302870:Spear crashes game. | Duplicate:inward:MC-302869:problem with entering the world | Duplicate:inward:MC-302863:PlayerData no Valid | Duplicate:inward:MC-302875:In the new snapshot, I can’t enter the world — it says "invalid player data". | Duplicate:inward:MC-302888:Unable to rejoin private worlds — “Invalid player data” error | Duplicate:inward:MC-302891:Sometimes, when logging into a singleplayer world, it shows this error: Invalid player data | Duplicate:inward:MC-302950:Player data error when on LAN Network | Duplicate:inward:MC-302921:Error related to Nautilus | Duplicate:inward:MC-302967:Game crashed with any status effect | Duplicate:inward:MC-302980:Unable to join a world by being kicked for "Invalid player data" | Duplicate:inward:MC-302981:Invalid player data when you enter in the world | Duplicate:inward:MC-303000:Invalid player Data Error When Loading a World | Duplicate:inward:MC-303035:25w41a Players with potion effects entering the world cause crashes. | Duplicate:inward:MC-302881:The F3+B hotkey crashes the game and corrupts minecraft world | Duplicate:inward:MC-303026:When I want to get in my world but I can’t do it because game say that the player data is invalid  | Duplicate:inward:MC-303044:Can't play in snapshot | Duplicate:inward:MC-303069:Minecraft “invalid player data” when you save a world with a potion effect applied. | Duplicate:inward:MC-303096:"Invalid player data" error while joining singleplayer world in snapshot 25w41a | Duplicate:inward:MC-303107:Game says invalid player data whenever trying to enter a world in singleplayer | Duplicate:inward:MC-302971:Cannot load world

## Description

Workaround
Open your world’s level.dat in an NBT editor such as this one, delete Data > Player > active_effects, save the file, replace your old level.dat with the edited one and load the world again.
Attempting to load a world in which you have a potion effect fails with an “Invalid player data” error message.
This can be reproduced while riding a nautilus or giving yourself the effect using /effect and saving and leaving the world, then proceeding to play the world where you gave yourself the effect.
Expected result
The world loads as normal.
Actual result
The world fails to load, displaying a server join attempt fail message, saying “Connection Lost, Invalid player data“.

## Comments (7)

### Comment 1: Keyaura (2025-10-09T08:02:25.398-0700)

This comment contained an image attachment, please login to view the attachment.

This comment contained an image attachment, please login to view the attachment.

This comment contained an image attachment, please login to view the attachment.

### Comment 2: Squid Eevee (2025-10-09T08:36:54.859-0700)

seems to be all potion effects - not just breath of the nautilus
i have several worlds i can’t open because the data pack gives saturation immediately
using nbtexplorer to remove the active_effects field lets me open the world again

### Comment 3: Octal (2025-10-09T11:02:36.849-0700)

Duplicate of MC-302730

### Comment 4: Johnden (2025-10-09T11:09:19.406-0700)

@Octal
This bug has been reported first, not a duplicate

### Comment 5: clamlol (2025-10-09T11:09:31.693-0700)

This one was created first and already has duplicates, so the issue will be tracked here.

### Comment 6: Skaggs (2025-10-09T12:17:11.282-0700)

Noticed this as well because my turtle helmet trapped me in a never ending state of having a potion effect.

### Comment 7: Lyndsbal (2025-10-09T16:06:49.809-0700)

Critical issue that impacts ability to test out Nautiluses among other mobs
