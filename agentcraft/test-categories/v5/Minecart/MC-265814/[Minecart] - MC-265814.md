# MC-265814: Minecart with TNT explodes or just dies depending on the type of explosion that hits it

**Mojira URL:** [https://bugs.mojang.com/browse/MC-265814](https://bugs.mojang.com/browse/MC-265814)

## Report details

- **Mojira categories:** Minecart
- **Project:** MC
- **Issue key:** MC-265814
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2023-10-13T15:52:37.549-0700
- **Updated:** 2025-03-07T22:26:44.393-0800
- **Resolution date:** 2023-10-15T04:38:55.143-0700
- **Affects versions:** 1.20.2; 23w40a
- **Fix versions:** 23w41a
- **Watchers:** 1
- **Attachments:** 5
- **Attachment filenames:** image-2023-10-14-00-54-29-371.png; image-2023-10-14-00-55-01-830.png; image-2023-10-14-00-55-31-416.png; image-2023-10-14-00-55-53-474.png; image-2023-10-14-00-56-19-828.png

## Description

When an explosion hits a minecart with TNT, there are three possible situations :
- The explosion is a creeper explosion, a TNT explosion ignited by redstone, a TNT explosion ignited with flint and steel by a player in survival mode or an end crystal explosion triggered by a player in survival mode. In these cases, the minecart is ignited by the explosion and explodes too (everthing is fine here I guess).

- The explosion is a TNT explosion ignited with flint and steel by a player in creative mode or an end crystal explosion triggered by a player in creative mode. In these cases, the minecart just dies, apparently like a normal entity. It isn't ignited, doesn't explode and drops nothing.

- An explosion happens and triggers a chain of multiple explosions. The final explosion of the chain hits a minecart. The minecart dies or explodes depending on the nature of the first explosion of the chain. If the first explosion is a TNT explosion ignited with flint and steel by a player in creative mode, so the minecart dies. In all other cases, it explodes. The minecart explodes even if the first explosion of the chain is an end crystal explosion triggered by a player in creative mode (and all the following explosions are TNT explosions) which seems surprising and in contradiction with the case 2, but I can confirm I verified this several times.

Remark : In the cases listed above, the player's gamemode to take in account is the gamemode at the moment of the explosion which hits the minecart, not the one at the moment you ignite the TNT block, creeper, or etc. If you ignite a TNT block with flint and steel in survival mode and immediately change your gamemode to creative, so the minecart will die and not explode.
You can see the screenshots I took. Here is the initial situation : player in creative mode, TNT and minecart with TNT separated by four blocks. The obsidian is here to remember the places of the objects after the explosion.
First scenario : the TNT is ignited by placing a redstone torch next to it.
You can see two distinct explosion holes around each obsidian block.
Same initial situation as the first picture, but second scenario : the TNT is ignited with flint and steel.
You can see only one hole around the TNT location and none around the minecart location. The minecart just died dropping nothing.
I did a video showing the bug. Available at https://www.dropbox.com/scl/fo/mucpeu2wchlqblrdnr6lh/h?rlkey=m473odb5qgt6z09zbsu1fm3ts&dl=0
Obviously, I have reproduced all the situations I mentionned previously (with creeper, end crystal,... etc) but didn't take screenshots as they would be very similar to these ones.

## Comments (5)

### Comment 1: migrated (2023-10-13T15:52:37.549-0700)

This comment contained multiple image attachments (5), please login to view the attachments.

### Comment 2: j_p_smith (2023-10-13T23:21:59.042-0700)

For me, the TNT minecart always ignites and explodes, regardless of the type of explosion that ignited it. Are you using any game modifications? If possible, could you attach (or link to) a short video demonstrating the issue?

### Comment 3: migrated (2023-10-14T08:21:21.352-0700)

No, I don't use any game modification.
Here is the video showing the issue : https://www.dropbox.com/scl/fo/mucpeu2wchlqblrdnr6lh/h?rlkey=m473odb5qgt6z09zbsu1fm3ts&dl=0

### Comment 4: j_p_smith (2023-10-15T02:09:13.746-0700)

Thanks for the video. It turns out the reason I couldn't reproduce this is because it's fixed in the latest snapshot. Correct me if I'm wrong, though!

### Comment 5: migrated (2023-10-15T03:27:38.706-0700)

I can confirm it's fixed in 23w41a. Thanks for your help !
