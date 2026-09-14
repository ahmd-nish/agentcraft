# MC-233604: GUI / Item rendering can heavily impact frame rate performance

**Mojira URL:** [https://bugs.mojang.com/browse/MC-233604](https://bugs.mojang.com/browse/MC-233604)

## Report details

- **Mojira categories:** Performance
- **Project:** MC
- **Issue key:** MC-233604
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2021-08-01T23:03:20.681-0700
- **Updated:** 2026-04-11T10:16:33.037-0700
- **Resolution date:** 2025-09-19T12:07:30.211-0700
- **Affects versions:** 1.17.1; 21w37a; 21w42a; 21w44a; 1.18 Pre-release 1; 1.18 Pre-release 2; 1.18; 1.18.1 Pre-release 1; 1.18.1; 22w06a; 1.18.2; 22w12a; 22w16b; 22w19a; 1.19 Pre-release 4; 1.19; 1.19.2; 1.19.3 Pre-release 2; 1.19.3; 23w03a; 23w04a; 23w05a; 23w06a; 1.19.4 Pre-release 1; 1.19.4 Pre-release 3; 1.19.4; 23w16a; 23w18a; 1.20.1; 23w31a; 23w32a; 1.21.1; 24w33a; 1.21.4
- **Fix versions:** 25w16a
- **Votes:** 1
- **Watchers:** 2
- **Attachments:** 23
- **Attachment filenames:** 2021-08-01_21.10.57.png; 2021-08-01_21.11.33.png; 2021-08-01_21.19.00.png; 2021-08-01_21.19.14.png; 2021-08-02_16.52.13.png; 2021-08-02_16.53.38.png; 2022-06-07_21.14.56.png; 2022-06-07_21.15.57.png; 2025-04-18_02.41.12.png; 2025-04-18_02.41.30.png; benchmark1.jpg; benchmark2.jpg; benchmark3.jpg; benchmark4.jpg; benchmark5.jpg; benchmark6.jpg; container_1.png; container_2.png; MC-233604.png; obraz-20250417-185549.png; obraz-20250417-185556.png; recipe_1.png; recipe_2.png
- **Issue links:** Relates:inward:MC-226966:Signs increase lots of lag when using glowing ink sac | Relates:inward:MC-233605:Enchantment glint rendering can impact frame rate performance | Relates:inward:MC-253502:Obfuscated text has a significant impact on performance

## Description

Rendering a large amount of items can drastically decrease frame rate, notably in the GUI when opening inventories, containers/chests full of them. This can be very noticeable when arranging a large amount of items.

Seems to be that every single item rendered counts as a draw call, and considering the amount of items inside a full double chest and their separate layers, this can get up to dozens of draw calls, making rendering chest contents a resource intensive task.
A single item can have one of the next counted as a separate layer, which contributes to the lag considerably when stacked:
- Color layers (leather armor, tipped arrows, potions, etc).

- Pattern layers (banners, shields).

- Armor trims.

- Enchant glint (MC-233605).

- Item quantity label/number (MC-249635).

- Durability bar.

How to reproduce
- Create a void world, place a double chest full of items and another one empty.

- Open ALT+F3 and open both chests.

- Compare the frame rate.

## Comments (10)

### Comment 1: migrated (2021-08-01T23:03:20.681-0700)

This comment contained multiple image attachments (13), please login to view the attachments.

### Comment 2: Avoma (2021-08-24T01:41:01.852-0700)

I am able to confirm this in 1.17.1. I'm unsure as to whether this is an issue or not though.

### Comment 3: syarumi (2021-08-24T13:56:23.210-0700)

For every full double chest a player opens they could get a 50%~ fps decrease (might depend) just by rendering items. I thought it could be considered a performance issue, that's why i reported it.
Also mention the fact that opening inventories without items can still lower fps a bit, mostly the player inventory, but i didn't consider it.

### Comment 4: syarumi (2022-06-14T15:28:16.016-0700)

Something interesting to note about this is that items are actually laggier than blocks:

Apparently items are more expensive to render. From the info i've gathered, every pixel on their texture is rendered as a separate rectangle instead of rendering the 2D sprite in the GUI. It gets even worse with resource packs of higher resolutions.

### Comment 5: Brain81505 (2023-01-21T01:39:32.620-0800)

Can confirm in 1.19.3 and 23w03a

### Comment 6: syarumi (2023-08-10T11:44:37.449-0700)

That's strange, i can't see why that massive fps drop would happen when hovering in a tooltip with little text like that, i don't think it's related to the item data though? i can't seem to reproduce it. This report only accounts for large quantities of items displayed in the GUI so that one might be a different issue.
Edit: Previous comment was deleted.

### Comment 7: syarumi (2025-04-08T21:34:07.084-0700)

Testing in 25w15a seems to show a significant improvement over 1.25.5 for some of the mentioned cases.

The shown benchmarks aren’t that clean due to some issues on intel devices in the current snapshot cycle, but I’ll keep an eye out for future changes to the GUI rendering improvements.

### Comment 8: Ceresjanin123 (2025-04-17T11:56:53.037-0700)

I can confirm I am seeing significant improvements in these cases
However I’m also seeing significant regressions in other cases (notably the F3 menu) MC-296911

### Comment 9: syarumi (2025-04-17T17:07:56.363-0700)

I have tested this again in 25w16a, with a more stable frame rate. Item rendering on GUIs seems to now have a negligible impact on frame times to the point this can be now considered fixed.

### Comment 10: Ceresjanin123 (2025-04-17T17:43:01.032-0700)

I wouldn’t consider this fixed

While the performance was improved significantly it does still impact frame times by a lot
