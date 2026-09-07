# MC-297888: Text no longer renders in a consistent order across different fonts

**Mojira URL:** [https://bugs.mojang.com/browse/MC-297888](https://bugs.mojang.com/browse/MC-297888)

## Report details

- **Mojira categories:** Rendering; Resource Packs
- **Project:** MC
- **Issue key:** MC-297888
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2025-05-14T13:19:54.140-0700
- **Updated:** 2026-03-11T03:51:39.620-0700
- **Resolution date:** 2025-05-15T07:35:47.593-0700
- **Affects versions:** 25w20a
- **Fix versions:** 25w21a
- **Area:** Platform G
- **Votes:** 2
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** Fetchr-Stripped.zip; Screenshot_20250514_221736.png; Screenshot_20250514_221823.png; Screenshot_20250514_221852.png

## Description

This behavior was introduced in 25w16a.
In the recent snapshot, text is no longer rendered in a consistent order. Reloading the resourcepack a bunch of times will give different results
This makes certain command tech that relies on overlapping text impossible. Different font definitions are required for different ascent values, to offset characters vertically.
This is admittedly very hacky but also very powerful and allows to render custom hud elements. An example for this is this Bingo card you will see when following the reproduction.
This works without issues in 1.21.5
Steps to reproduce
- Download this resourcepack and enable it:

- Run the following command:
- Readable version (for mcfunction):

```
title @a actionbar [\
	{ text: "\uff3d", shadow_color: 0, font: "fetchr:space" },\
	{ text: "a", font: "fetchr:card" },\
	"\uff99",\
	[\
		{ text: "\u0006", font: "fetchr:row0" }, { text: "\u0004", font: "fetchr:space" },\
		        "\u0072",                        { text: "\u0004", font: "fetchr:space" },\
		        "\u005e",                        { text: "\u0004", font: "fetchr:space" },\
		        "\u004d",                        { text: "\u0004", font: "fetchr:space" },\
		        "\u004c"\
	],\
	"\uff9b",\
	[\
		{ text: "\u0063", font: "fetchr:row1" }, { text: "\u0004", font: "fetchr:space" },\
		        "\u0020",                        { text: "\u0004", font: "fetchr:space" },\
		        "\u001a",                        { text: "\u0004", font: "fetchr:space" },\
		        "\u002a",                        { text: "\u0004", font: "fetchr:space" },\
		        "\u0067"\
	],\
	"\uff9b",\
	[\
		{ text: "\u001d", font: "fetchr:row2" }, { text: "\u0004", font: "fetchr:space" },\
		        "\u0026",                        { text: "\u0004", font: "fetchr:space" },\
		        "\u006f",                        { text: "\u0004", font: "fetchr:space" },\
		        "\u0066",                        { text: "\u0004", font: "fetchr:space" },\
		        "\u006b"\
	],\
	"\uff9b",\
	[\
		{ text: "\u005f", font: "fetchr:row3" }, { text: "\u0004", font: "fetchr:space" },\
		        "\u0002",                        { text: "\u0004", font: "fetchr:space" },\
		        "\u001e",                        { text: "\u0004", font: "fetchr:space" },\
		        "\u0065",                        { text: "\u0004", font: "fetchr:space" },\
		        "\u0021"\
	],\
	"\uff9b",\
	[\
		{ text: "\u0011", font: "fetchr:row4" }, { text: "\u0004", font: "fetchr:space" },\
		        "\u005a",                        { text: "\u0004", font: "fetchr:space" },\
		        "\u0055",                        { text: "\u0004", font: "fetchr:space" },\
		        "\u0037",                        { text: "\u0004", font: "fetchr:space" },\
		        "\u001f"\
	],\
	"\u005c"\
]
```

- Or single line for a command block:

```
title @a actionbar [{text:"\uff3d",shadow_color:0,font:"fetchr:space"},{text:"a",font:"fetchr:card"},"\uff99",[{text:"\u0006",font:"fetchr:row0"},{text:"\u0004",font:"fetchr:space"},"\u0072",{text:"\u0004",font:"fetchr:space"},"\u005e",{text:"\u0004",font:"fetchr:space"},"\u004d",{text:"\u0004",font:"fetchr:space"},"\u004c"],"\uff9b",[{text:"\u0063",font:"fetchr:row1"},{text:"\u0004",font:"fetchr:space"},"\u0020",{text:"\u0004",font:"fetchr:space"},"\u001a",{text:"\u0004",font:"fetchr:space"},"\u002a",{text:"\u0004",font:"fetchr:space"},"\u0067"],"\uff9b",[{text:"\u001d",font:"fetchr:row2"},{text:"\u0004",font:"fetchr:space"},"\u0026",{text:"\u0004",font:"fetchr:space"},"\u006f",{text:"\u0004",font:"fetchr:space"},"\u0066",{text:"\u0004",font:"fetchr:space"},"\u006b"],"\uff9b",[{text:"\u005f",font:"fetchr:row3"},{text:"\u0004",font:"fetchr:space"},"\u0002",{text:"\u0004",font:"fetchr:space"},"\u001e",{text:"\u0004",font:"fetchr:space"},"\u0065",{text:"\u0004",font:"fetchr:space"},"\u0021"],"\uff9b",[{text:"\u0011",font:"fetchr:row4"},{text:"\u0004",font:"fetchr:space"},"\u005a",{text:"\u0004",font:"fetchr:space"},"\u0055",{text:"\u0004",font:"fetchr:space"},"\u0037",{text:"\u0004",font:"fetchr:space"},"\u001f"],"\u005c"]
```

- Paste one of the versions into a function file or a command block and run the command.

- Reload the resource pack multiple times and observe how the Bingo card renders after each reload.

Observed Result
The item rows sometimes render in front of the card and sometimes behind it.
It is noteworthy that it is always consistent per row, either the entire row renders in front or the entire row renders behind. So my thinking is that it might be related to using different fonts, but it could be for some other reason.
Note that the font specified in the first element of each list carries over to the entire list, so the first list is all row0 font, and the second list is all row1 (except for the spaces).
Expected Result
Characters always render in order they are defined. So in “a<negspace>b”, b should always render on top of a, because b comes later

## Comments (1)

### Comment 1: NeunEinser (2025-05-14T13:25:48.564-0700)

This comment contained multiple image attachments (3), please login to view the attachments.
