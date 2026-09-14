# MC-301424: entity_data item component detection is broken in resource packs

**Mojira URL:** [https://bugs.mojang.com/browse/MC-301424](https://bugs.mojang.com/browse/MC-301424)

## Report details

- **Mojira categories:** Resource Packs
- **Project:** MC
- **Issue key:** MC-301424
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2025-08-23T01:10:23.913-0700
- **Updated:** 2025-11-04T03:24:35.951-0800
- **Resolution date:** 2025-11-04T03:24:35.904-0800
- **Affects versions:** 25w34b; 25w35a; 25w36b; 1.21.10; 25w44a
- **Fix versions:** 1.21.9 Pre-Release 1; 25w45a
- **Area:** Platform
- **Votes:** 2
- **Watchers:** 2
- **Attachments:** 3
- **Attachment filenames:** BrokenEntityDataExample.zip; WithPack1218.png; With Resource Pack.png

## Description

In 1.21.8 its possible to change item models/textures via component detection in resource packs. For items that carry the entity_data component in them, this now results in a missing model error for the item instead of previous behavior of using a fallback model if something was wrong.

Steps to reproduce:
1- Install the attached resource pack and open a world in or after 25w34b
2- Look at Item Frames in the creative inventory
3- Run the command /give @s item_frame[entity_data={id:"minecraft:item_frame",Invisible:1b}] 1
4- Repeat steps 1-3 in 1.21.8 and notice the missing model error doesn't happen

Expected Result:
The item frames with differing component data should be visually distinct, like in 1.21.8

Actual Result:
All item frame items use the missing model/texture error cube

## Comments (3)

### Comment 1: Cubeoidal (2025-08-23T01:10:24.699-0700)

This comment contained an image attachment, please login to view the attachment.

This comment contained an image attachment, please login to view the attachment.

This comment contained an image attachment, please login to view the attachment.

### Comment 2: Cubeoidal (2025-09-26T12:09:29.899-0700)

Not fixed as of 1.21.9 rc-1

### Comment 3: gegy (2025-09-29T00:08:26.953-0700)

Hi, thanks for the report!  It looks like there is a remaining issue here with the SNBT form of entity data - I’ve reopened the issue as this should be addressed, but you should be able to work around it for now by updating the selector syntax:

```"when": {
  "id": "minecraft:item_frame",
  "Invisible": true
}```
