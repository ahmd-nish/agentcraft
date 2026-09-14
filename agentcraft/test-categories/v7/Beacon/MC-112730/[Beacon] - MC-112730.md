# MC-112730: Beacon beam and structure block render twice per frame

**Mojira URL:** [https://bugs.mojang.com/browse/MC-112730](https://bugs.mojang.com/browse/MC-112730)

## Report details

- **Mojira categories:** Beacon; Rendering
- **Project:** MC
- **Issue key:** MC-112730
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2017-01-22T12:55:16.770-0800
- **Updated:** 2025-05-19T08:04:25.256-0700
- **Resolution date:** 2025-05-19T08:04:25.180-0700
- **Affects versions:** Minecraft 1.11.2; Minecraft 1.12 Pre-Release 6; Minecraft 17w47b; 1.15.1; 1.16.3; 1.16.4; 20w48a; 1.19.2; 1.21.1; 1.21.3
- **Fix versions:** 25w21a
- **Area:** Platform
- **Labels:** beacon; beam; block-entity; rendering; structure_block
- **Watchers:** 1
- **Attachments:** 0
- **Issue links:** Duplicate:inward:MC-278464:Block entities render twice if shouldRenderOffScreen returns true and the block entity is in view | Duplicate:inward:MC-170106:Beacon outlayer loses texture opacity when looking up at high altitude

## Description

The bug
Beacon beams and structure block outlines will render themselves twice per frame if the chunk sector that the block entity is in is in view.
This can be observed by the opacity of a beacon beam changing:
The decreased opacity when looking upward indicates there is only a single render.
As side note this bug was introduced in the fix to MC-68247
Affected blocks
Last updated for 1.11.2
- beacon

- structure_block

Code analysis
Based on 1.11.2 decompiled using MCP 9.35 rc1
This happens because the method net.minecraft.client.renderer.RenderGlobal.renderEntities(Entity, ICamera, float) first renders all tile entities and then all "global" tile entities. These are in the set net.minecraft.client.renderer.RenderGlobal.setTileEntities because their overridden method net.minecraft.client.renderer.tileentity.TileEntitySpecialRenderer.isGlobalRenderer(T) returns true.

## Comments (2)

### Comment 1: Michael Wobst (2021-05-21T09:01:44.817-0700)

Can this still be reproduced in the latest 1.17 development snapshot?

### Comment 2: markderickson (2022-09-05T11:23:04.105-0700)

Yes, I can confirm in 1.19.2.
