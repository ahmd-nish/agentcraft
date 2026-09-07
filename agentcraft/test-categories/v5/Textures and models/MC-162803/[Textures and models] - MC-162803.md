# MC-162803: Lily Pad mirrors texture when placed

**Mojira URL:** [https://bugs.mojang.com/browse/MC-162803](https://bugs.mojang.com/browse/MC-162803)

## Report details

- **Mojira categories:** Textures and models
- **Project:** MC
- **Issue key:** MC-162803
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2019-10-05T08:13:14.238-0700
- **Updated:** 2025-04-29T20:04:03.939-0700
- **Resolution date:** 2022-02-21T06:10:33.910-0800
- **Affects versions:** 1.14.4; 19w40a; 1.16.2; 1.16.5; 21w11a; 21w13a; 21w14a; 21w16a; 21w17a; 21w18a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17; 1.17.1 Pre-release 1; 1.17.1; 21w39a; 21w40a; 21w42a; 1.18 Pre-release 1
- **Fix versions:** 1.18 Pre-release 5
- **Labels:** incorrect-uv; plane-mirroring
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** Derp.png

## Description

When seen from the top, the texture used by Lily Pads is mirrored when placed as a block, compared to the texture image itself and all other in-game uses of it (e.g. in-GUI display, as a held item, in an item frame...).

What I expected to happen was...:
The left side of the texture is on the left side of the Lily Pad block.

What actually happened was...:
The left side of the texture is on the right side of the Lily Pad block.

Steps to Reproduce:
- Create a world with the game mode set to Creative.

- Open the inventory and find a Lily Pad. (It can be found in the second tab on the top, Decoration Blocks, or you can search for it in the sixth tab, Search Items.)

- Take a Lily Pad into your hotbar, and close the inventory.

- Find a lake, a river, an ocean, or some other place with water.

- Place the Lily Pad on top of the water, and compare the placed Lily Pad to the one in the hotbar and in your hand.

Steps to Fix:
In the resource file assets/minecraft/models/block/lily_pad.json, change...

```
"down":  { "uv": [ 16, 16, 0,  0 ], "texture": "#texture", "tintindex": 0 },
                "up":    { "uv": [ 16,  0, 0, 16 ], "texture": "#texture", "tintindex": 0 }
```

...to...

```
"down":  { "uv": [ 0, 16, 16,  0 ], "texture": "#texture", "tintindex": 0 },
                "up":    { "uv": [ 0,  0, 16, 16 ], "texture": "#texture", "tintindex": 0 }
```

Screenshots:
I have attached two images of the problem, where a resource pack is in use to add a bright green line on the left of the texture. The images show the Lily Pad on the hotbar, in both the left and the right hand, in an item frame, and placed as a block on top of water. The line is on the left (correct) side of the Lily Pad in all cases except for when placed on the water, where it is on the right (incorrect) side instead. One image is in version 1.14.4 (with an irrelevant mod), and one image is in snapshot 19w40a (without any mods).

## Comments (18)

### Comment 1: migrated (2019-10-05T08:13:14.238-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: SoloAlguien (2021-03-17T15:49:00.430-0700)

Can confirm in 21w11a.

### Comment 3: SoloAlguien (2021-04-02T20:35:05.649-0700)

Can confirm in 21w13a.

### Comment 4: SoloAlguien (2021-04-08T16:19:50.696-0700)

Can confirm in 21w14a.

### Comment 5: SoloAlguien (2021-04-21T13:06:11.693-0700)

Can confirm in 21w16a.

### Comment 6: SoloAlguien (2021-05-02T11:36:42.301-0700)

Can confirm in 21w17a.

### Comment 7: SoloAlguien (2021-05-07T12:25:53.750-0700)

Can confirm in 21w18a.

### Comment 8: SoloAlguien (2021-05-15T17:59:54.459-0700)

Can confirm in 21w19a.

### Comment 9: SoloAlguien (2021-05-21T22:11:32.667-0700)

Can confirm in 21w20a.

### Comment 10: SoloAlguien (2021-05-28T16:52:59.252-0700)

Can confirm in 1.17 Pre-release 1.

### Comment 11: SoloAlguien (2021-05-31T17:32:28.403-0700)

Can confirm in 1.17 Pre-release 2.

### Comment 12: SoloAlguien (2021-06-01T22:28:12.600-0700)

Can confirm in 1.17 Pre-release 3.

### Comment 13: SoloAlguien (2021-06-20T11:52:29.293-0700)

Can confirm in 1.17 and 1.17.1 Pre-release 1.

### Comment 14: SoloAlguien (2021-07-11T15:38:27.716-0700)

Can confirm in 1.17.1.

### Comment 15: SoloAlguien (2021-09-29T14:30:18.939-0700)

Can confirm in 21w39a.

### Comment 16: muzikbike (2021-10-10T12:58:15.425-0700)

Confirmed for 21w40a.
Can I request ownership of this issue due to the author having no activity for over 12 months?

### Comment 17: SoloAlguien (2021-10-20T10:56:45.965-0700)

Can confirm in 21w42a.

### Comment 18: SoloAlguien (2021-11-11T10:37:42.531-0800)

Can confirm in 1.18 Pre-release 1.
