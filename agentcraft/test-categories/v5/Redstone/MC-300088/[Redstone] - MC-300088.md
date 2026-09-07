# MC-300088: Items placed by a copper golem in a double chest do not update redstone comparators reading the right side of the double chest

**Mojira URL:** [https://bugs.mojang.com/browse/MC-300088](https://bugs.mojang.com/browse/MC-300088)

## Report details

- **Mojira categories:** Redstone
- **Project:** MC
- **Issue key:** MC-300088
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2025-07-29T08:05:58.634-0700
- **Updated:** 2025-09-01T08:30:15.898-0700
- **Resolution date:** 2025-08-29T05:16:16.164-0700
- **Affects versions:** 25w31a; 25w35a
- **Fix versions:** 25w36a
- **Area:** Expansion A
- **Votes:** 188
- **Watchers:** 1
- **Attachments:** 8
- **Attachment filenames:** 2025-07-29_09.01.49.png; 2025-07-29_09.01.59.png; 2025-07-29_09.02.43-20250729-150243.png; 2025-07-29_13.39.40.png; 2025-07-29_15.36.01.png; 2025-07-29_15.36.12.png; 2025-07-29_15.36.51.png; image-20250729-170841.png
- **Issue links:** Duplicate:inward:MC-300185:Redstone comparator don't update after copper golem put items in the chest | Duplicate:inward:MC-300224:Copper Golem Chest Insertion Doesn't Trigger Comparator Update | Duplicate:inward:MC-300265:Items placed into a chest by Copper Golems aren't pulled out by a hopper until a player moves an item | Duplicate:inward:MC-300483:copper golem doesn't update comparators in certain cases | Duplicate:inward:MC-300487:Copper Golem  loading chest does not seem to change the redstone signal output properly vis comparator to allow proper unlocking of the hopper below. only when I add items does the redstone seem to work | Duplicate:inward:MC-300681:Comparator doesn't detect when a copper golem puts items in a chest | Duplicate:inward:MC-300782:Copper golems do not force comparator block updates | Duplicate:inward:MC-300909:Copper Golem do not update blocks around chest when putting items in | Duplicate:inward:MC-301581:Comparators don't detect correctly | Duplicate:inward:MC-301704:Copper Golem does not update chest comparator signal when inserting items | Duplicate:inward:MC-301715:Comparator measuring a double chest does not update when copper golem adds/removes items in the opposite side

## Description

- Steps to reproduce the issue
- Place a copper chest and a double chest, with a comparator on the right side of the double chest

- Place 3 stacks and 54 items in the double chest

- Place 1 of the same item in the copper chest

- Spawn a Copper Golem and wait for it to move the item from the Copper Chest to the Double Chest

- Expected result
- Redstone Comparator outputs a power level of 2

- Actual result
- Redstone Comparator outputs a power level of 1

## Comments (14)

### Comment 1: CrazyTiger6 (2025-07-29T08:05:59.831-0700)

This comment contained an image attachment, please login to view the attachment.

This comment contained an image attachment, please login to view the attachment.

This comment contained an image attachment, please login to view the attachment.

### Comment 2: [MOD] Greymagic27 (2025-07-29T10:08:42.654-0700)

I cannot reproduce this. Using this setup, the comparator produces a redstone power level of '2' when the item is deposited by the copper golem

### Comment 3: CrazyTiger6 (2025-07-29T12:42:33.283-0700)

Not sure what the procedure it for updated information, but I have done a bit more testing following Graymagic27’s response. It seems as though the comparator on the side of the chest the copper golem placed the item in does not update properly, whereas a comparator on the other side updates fine, in order to reproduce the bug, I recommend using a setup like the one in the attached image.

### Comment 4: CrazyTiger6 (2025-07-29T14:37:42.283-0700)

Upon further examination, my response has changed. It is always the right side of the chest that does not update properly

### Comment 5: Hettyc_Tracyn (2025-07-31T06:16:12.918-0700)

I had the same issue, though I didn’t know it was a (directional? Side of chest?) issue…

Here’s my report that has been marked as duplicate by the mods:

### Comment 6: FunCool (2025-08-05T08:24:19.317-0700)

When the copper golem inserts an item into a double chest, it updates only the half (single chest) that corresponds to the slot where the item is placed. This means that a comparator placed behind or on the side of the specific half of the chest that received the item will detect the change, while a comparator behind the other half will not. As a result, comparators attached to different sides of the double chest can give different readings, because only one side is actually updated when the golem inserts an item, not the whole double chest.

### Comment 7: Ray (2025-08-06T08:45:56.042-0700)

The work around is to spam redstone next to the comparator. But I hope this gets fixed as a similar bug was in Crafter block before it was fixed.

### Comment 8: AFfa (2025-08-08T05:58:18.209-0700)

hope they fix it in the next snapshot

### Comment 9: Patate324 (2025-08-08T06:14:44.879-0700)

Please watch the video here, starting at the timestamp (10:51) to about 11:55.

Comparators seem to be reading the contents of chests in a directional manner. This is therefore resolved by orienting chests in a certain manner, so this is very unintuitive.

### Comment 10: Patate324 (2025-08-08T06:16:47.928-0700)

Adding to my above comment, while this may not be a strict bug (since double chests are actually two single chests with a fused UI), since double chests act as one from the player perspective, this should be patched to make the user experience seamless.

### Comment 11: Luuk Duisenberg (2025-08-09T00:24:22.404-0700)

I hope they fix this bug

### Comment 12: PokeJake1127 (2025-08-09T02:41:22.910-0700)

this sounds like a feature request rather than a bug

### Comment 13: Hettyc_Tracyn (2025-08-09T05:56:25.058-0700)

PokeJake1127 - How is this not a bug? The expected behaviour of chests, which has been the same for as long as comparators have been in the game, is not behaving right when interacting with a copper golem…

### Comment 14: Konrad Kohlrabi (2025-08-09T11:26:26.365-0700)

True
