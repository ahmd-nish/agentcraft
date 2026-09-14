# MC-189365: Player can retain Soul Speed effect by bridging

**Mojira URL:** [https://bugs.mojang.com/browse/MC-189365](https://bugs.mojang.com/browse/MC-189365)

## Report details

- **Mojira categories:** Items; Player
- **Project:** MC
- **Issue key:** MC-189365
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2020-06-13T05:52:48.518-0700
- **Updated:** 2025-04-29T09:44:28.713-0700
- **Resolution date:** 2024-04-30T01:47:57.982-0700
- **Affects versions:** 1.16 Pre-release 5; 1.16 Pre-release 8; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w27a; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Release Candidate 1; 1.16.2 Release Candidate 2; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4; 20w45a; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w06a; 21w08b; 21w11a; 21w15a; 21w17a; 21w19a; 21w20a; 1.17; 1.17.1; 1.18; 1.18.1; 1.19; 1.19.2; 1.19.3; 23w05a; 1.19.4; 23w14a; 1.20.4; 24w09a
- **Fix versions:** 24w18a
- **Area:** Gameplay
- **Labels:** player; soul_speed
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** Minecraft 1.16 Pre-release 5 - Singleplayer 2020-06-13 08-51-28.mp4
- **Issue links:** Relates:inward:MC-189368:Soul Speed effect still persists when slow falling off a block | Relates:inward:MC-175312:Soul Speed changes players' FOV (field of view) | Duplicate:inward:MC-198621:Fast walk with shift, without speed potion | Duplicate:inward:MC-199709:When standing on the edge of a block near soul sand after you run, the soul speed enchant effect will work | Duplicate:inward:MC-205484:speed from soulspeed doesn't disappear when you place block while sneaking and stand on it. | Duplicate:inward:MC-209084:Soul Speed resists after crossing the Soul Sand | Duplicate:inward:MC-214229:Soul speed effect carrys on when shifting on the edge of blocks that aren't soul soil or soul sand | Duplicate:inward:MC-259677:Soul sand on the march back | Relates:outward:MC-177960:While standing on soul soil/sand with soul speed, replacing the block beneath you with a non-soul block keeps the soul speed

## Description

By sneaking and bridging, you can retain the soul speed effect on any block and vise versa. (sneaking and walking on soul speed also does not give the soul speed effect)
Steps to reproduce
- Bridge out 1 block using soul soil (soul sand sinks you too deep for this to work properly) while wearing soul speed boots. You still have the soul speed. Intended so far. (You might not get the soul speed effect if you accidentally reproduced step 4.)

- Bridge out another block with a none soul speed block while walking towards the direction of it.

- Keep doing so without walking back.
Result: You retain infinite soul speed, because your speed of normal sneaking is slower than sneaking with soul speed. You can do this forever if you don't walk back, and your boots never take durability damage.
Expected results: Your soul speed wears off as soon as you walk on the none soul speed block.

- Repeat step 1 and 2, but bridge out first with a normal block, then continue using soul speed blocks.
Result: You never get the soul speed effect.
Expected results: You get soul speed as soon as you walk on the soul speed blocks.

## Comments (13)

### Comment 1: migrated (2020-06-13T05:52:48.518-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: migrated (2020-09-07T12:01:51.681-0700)

Can confirm for 1.16.3rc1

### Comment 3: Avoma (2021-01-29T03:03:32.678-0800)

Can confirm in 21w03a.

### Comment 4: Avoma (2021-02-15T03:34:45.813-0800)

Can confirm in 21w06a. Feel free to use the following command to make reproducing this much easier:

```/give @s minecraft:netherite_boots{Enchantments:[{id:"soul_speed",lvl:3}]}```

### Comment 5: migrated (2021-03-19T14:27:53.413-0700)

Affects 21w11a.

### Comment 6: Avoma (2021-04-18T02:58:11.238-0700)

Can confirm in 21w15a.

### Comment 7: Avoma (2021-06-25T08:17:57.052-0700)

Can confirm in 1.17.

### Comment 8: Avoma (2021-08-04T07:29:33.822-0700)

Can confirm in 1.17.1.

### Comment 9: Avoma (2021-12-09T10:51:37.497-0800)

Can confirm in 1.18.

### Comment 10: MMK21 (2021-12-14T07:37:33.454-0800)

Note that the "prevent Soul Speed by sneaking on the edge on Soul Speed blocks" is actually , so should probably be removed.

### Comment 11: Avoma (2022-01-12T07:34:25.923-0800)

Can confirm in 1.18.1.

### Comment 12: Avoma (2022-07-23T08:38:18.171-0700)

Can confirm in 1.19.

### Comment 13: Avoma (2022-09-02T02:38:46.623-0700)

Can confirm in 1.19.2.
