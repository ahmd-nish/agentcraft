# MC-276965: Post shader ColorModulate uniform not reset properly after spectating spiders

**Mojira URL:** [https://bugs.mojang.com/browse/MC-276965](https://bugs.mojang.com/browse/MC-276965)

## Report details

- **Mojira categories:** Camera; Textures and models
- **Project:** MC
- **Issue key:** MC-276965
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-09-25T14:27:34.497-0700
- **Updated:** 2025-05-29T09:04:30.300-0700
- **Resolution date:** 2024-10-08T01:36:45.772-0700
- **Affects versions:** 24w39a
- **Fix versions:** 1.21.2 Pre-Release 1
- **Area:** Platform
- **Watchers:** 2
- **Attachments:** 2
- **Attachment filenames:** javaw_9GgvnisUf3.gif; postshaderuniformbug.png

## Description

The Issue
post/spider.json changes post/blit ColorModulate uniform from [1,1,1,1] to [1,0.8,0.8,1], making it red. Previously when using that program again elsewhere it would use the default value in post/x.json, but now it keeps whatever post effect overrides were done previously until they're overridden again by another post effect.
This means post/blit in post/invert.json for spectating endermen or post/transparency.json for Fabulous Graphics has the same red ColorModulate uniform applied after spectating a spider.
See
 for a visual comparison of the enderman shader before and after spectating a spider.
See
 for a demonstration of the spider tint persisting with Fabulous Graphics.
Note: This happens with all post shader uniforms, but the spider shader is the only place where it can be observed without resource packs.
Steps to Reproduce
- Open a creative world in an affected version (e.g. 24w39a).

- Set graphics quality to Fabulous Graphics.

- Spawn an enderman and a spider.

- Enter spectator mode.

- Spectate the enderman. Notice that the screen colors are precisely inverted while spectating the enderman.

- Stop spectating the enderman. Notice that the screen is returned to normal.

- Spectate the spider. Notice that the screen is tinted red and distorted while spectating the spider.

- Stop spectating the spider. Notice that the screen remains tinted red. This is because the ColorModulate uniform has not been properly reset from spectating the spider and it is applied in the transparency post shader.

- Set graphics quality to Fast Graphics. Notice that the screen is no longer tinted red. This is because no post shader is applied anymore.

- Spectate the enderman again. Notice that the screen colors are inverted once again, but with a red tint applied which makes it subtly different from before. This is because the ColorModulate uniform has not been properly reset from spectating the spider and it is applied in the enderman's post shader.

- Repeat these same steps in Minecraft Java Edition 1.21.1. Notice that the observed behavior does not occur.

## Comments (3)

### Comment 1: migrated (2024-09-25T14:27:34.497-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: [MOD] Greymagic27 (2024-09-29T10:52:37.857-0700)

How can I reproduce this ingame and see the difference?

### Comment 3: Evtema3 (2024-09-29T14:10:44.567-0700)

Here are the steps to reproduce (I will also amend the report to include these):
- Open a creative world in an affected version (e.g. 24w39a).

- Set graphics quality to Fabulous Graphics.

- Spawn an enderman and a spider.

- Enter spectator mode.

- Spectate the enderman. Notice that the screen colors are precisely inverted while spectating the enderman.

- Stop spectating the enderman. Notice that the screen is returned to normal.

- Spectate the spider. Notice that the screen is tinted red and distorted while spectating the spider.

- Stop spectating the spider. Notice that the screen remains tinted red. This is because the ColorModulate uniform has not been properly reset from spectating the spider and it is applied in the transparency post shader.

- Set graphics quality to Fast Graphics. Notice that the screen is no longer tinted red. This is because no post shader is applied anymore.

- Spectate the enderman again. Notice that the screen colors are inverted once again, but with a red tint applied which makes it subtly different from before. This is because the ColorModulate uniform has not been properly reset from spectating the spider and it is applied in the enderman's post shader.

- Repeat these same steps in Minecraft Java Edition 1.21.1. Notice that the observed behavior does not occur.

I performed these exact steps while I wrote them and observed the incorrect behavior.
