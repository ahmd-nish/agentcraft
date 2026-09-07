# MC-144761: Animated texture interpolation ignores alpha channel during transition from/to transparent pixels

**Mojira URL:** [https://bugs.mojang.com/browse/MC-144761](https://bugs.mojang.com/browse/MC-144761)

## Report details

- **Mojira categories:** Resource Packs; Textures and models
- **Project:** MC
- **Issue key:** MC-144761
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2019-02-22T18:26:11.321-0800
- **Updated:** 2025-10-07T00:33:13.147-0700
- **Resolution date:** 2024-07-29T07:11:21.173-0700
- **Affects versions:** Minecraft 1.13.2; Minecraft 19w07a; Minecraft 19w08b; 1.16.3; 1.16.4 Release Candidate 1; 1.16.4; 1.16.5; 21w11a; 1.17.1; 1.18; 1.18.1; 1.18.2; 1.20.2
- **Fix versions:** 24w33a
- **Area:** Platform
- **Labels:** animation; resource-pack-support
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** Diagram 1.png; Diagram 2.png; Diagram 3.png; Glass.gif; Interpolation test.zip; Items.gif
- **Issue links:** Relates:outward:MC-302364:Semitransparent pixels don't interpolate properly on animated textures where interpolate is set to true

## Description

The bug
If an animated texture that uses texture interpolation ({"interpolate": true} in the .mcmeta file) contains transparent pixels, the following behaviors can be observed:
- When fading TO transparent pixels, i.e. having a pixel that starts opaque and becomes transparent in the next frame, during the interpolation they will fade to whatever the RGB values for the pixels are, ignoring the alpha channel (the game just behaves as if the pixel was fully opaque). Once the transition is over, those pixels instantly change from that color to transparent, which creates a very jarring effect.

- When fading FROM transparent pixels, i.e. having a pixel that starts transparent and becomes opaque in the next frame, they'll appear completely transparent until the transition is over. Once it is over, the correct color will, again, appear all of a sudden.

Although this bug has no effect on the vanilla game, since no textures use interpolation and transparent pixels simultaneously, resource packs using both these features on the same texture should not encounter this issue.
Explanation
The example resource pack provided below (and shown above) is one I created to make a comparison between the old and new vanilla textures, which takes advantage of texture animations to cycle the textures every few seconds. Since many items have had their shape changed in the updated textures, many pixels that were transparent in an old texture are now "present" in the new texture, and vice-versa. As such, the effect described here became very apparent, which was what led me to uncover that bug in the first place.
The program I used to generate these textures happens to make every transparent pixel black (which is what most image editing software does), which at first made me think that the game would always use black as the color it transitioned towards before becoming transparent. After a few more tests, this has shown not to be the case.
Rather, any "color" that's stored in the RGB channels of transparent pixels will be used during the transition. For example, let's say I have a solid red pixel (255, 0, 0, 255) that fades to a transparent green pixel (0, 255, 0, 0). Notice how the alpha channel of the latter is 0; that means the game shouldn't care that there's green in there, as the pixel is simply transparent.
Instead of going from red straight to transparent, it will go slowly from red to GREEN, then become transparent all of a sudden. When returning from transparency to solid red, since it doesn't take into account the alpha channel of the next frame, it will just remain transparent all the way through the transition, then, again, become red immediately.

(The exact behavior described here can be seen on the apple texture on the provided resource pack.)
The reason for the game seeing "colors" when the pixels are actually transparent is that, when using straight alpha (as opposed to premultiplied alpha), as do PNG files, pixels with an alpha value of 0 can still hold other values in their RGB channels. This means that, despite looking the same to the user, "transparent black" is actually stored differently from "transparent white", which is stored differently from "transparent red" etc.
And the reason for the game not taking the alpha channel into account? Well, my first thought was that some blocks simply don't support partial opacity, as is the case of most solid blocks except ice, stained glass and a few other exceptions. For those blocks, any pixel with an alpha value above a certain threshold will be fully solid; everything else will be fully transparent. I thought that could be the case with interpolation too – since during the transition some pixels technically acquire partial opacity, the game could simply not be rendering that transparency because the block doesn't allow it. It could just be behaving the same way it would if you simply put a static texture with partial opacity, i.e. the problem is not in the interpolation itself, but in certain blocks not allowing partial transparency. That hypothesis was quickly discarded: after I set the same glass texture shown above to stained glass, one of the few blocks that support partial opacity, the black pixels appeared in the exact same way. This possibly points to a problem in the rendering engine, more specifically in the piece of code that calculates the intermediate values used for transitioning between frames, rather than a problem with the blocks themselves.
Steps to reproduce
- Download and install the attached test resource pack:

- .

- Get access to some glass or any of the items affected by this – those are easily noticeable in the Creative inventory. Alternatively, get an apple, which contains the example texture used in the above explanation.

- Notice, for a few seconds, how:
 → solid pixels that become transparent on the next frame, fade to some color instead of transparency until the transition is over, then finally acquire the proper transparency all of a sudden;
 → transparent pixels that become solid on the next frame aren't shown at all until the transition is over, then finally show the proper color all of a sudden.

Code analysis
See this comment

## Comments (11)

### Comment 1: migrated (2019-02-22T18:26:11.321-0800)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: migrated (2020-08-04T11:37:21.135-0700)

This is a pretty easy thing to fix, it's a two line change.
Using fabric names, in net.minecraft.client.textyre.Sprite$Interpolation.apply()V it does:

```for(int y = 0; y < n; ++y) {
  for(int x = 0; x < m; ++x) {
    int dest = getPixelColor(i, l, x, y);
    int source = getPixelColor(k, l, x, y);
    int red = lerp(delta, dest >> 16 & 255, source >> 16 & 255);
    int green = lerp(delta, dest >> 8 & 255, source >> 8 & 255);
    int blue = lerp(delta, dest & 255, source & 255);
    images[l].setPixelColor(x, y, (source & 0xFF000000 ) | (red << 16) | (green << 8) | blue);
  }
}```
And a fixed version would be as follows:

```for(int y = 0; y < n; ++y) {
  for(int x = 0; x < m; ++x) {
    int dest = getPixelColor(i, l, x, y);
    int source = getPixelColor(k, l, x, y);
    int red = lerp(delta, dest >> 16 & 255, source >> 16 & 255);
    int green = lerp(delta, dest >> 8 & 255, source >> 8 & 255);
    int blue = lerp(delta, dest & 255, source & 255);
    int alpha = lerp(delta, (dest >>> 24) & 255, (source >>> 24) & 255);
    images[l].setPixelColor(x, y, (alpha << 24) | (red << 16) | (green << 8) | blue);
  }
}```
The change is more specifically:

```images[l].setPixelColor(x, y, (source & 0xFF000000 ) | (red << 16) | (green << 8) | blue);```
becomes

```int alpha = lerp(delta, (dest >>> 24) & 255, (source >>> 24) & 255);
images[l].setPixelColor(x, y, (alpha << 24) | (red << 16) | (green << 8) | blue);```
It is because the alpha was always being used from the "source" texture of the interpolation pass. This makes it so the alpha is always interpolated.

### Comment 3: MMK21 (2020-08-04T12:21:45.126-0700)

The Fabric mod "MC-144761 Fix" claims to fix this bug.

### Comment 4: Juknum (2021-05-07T08:45:20.262-0700)

Can confirm in 21w16a

### Comment 5: MMK21 (2021-09-06T00:45:13.124-0700)

Affects 1.17.1

### Comment 6: MMK21 (2021-12-04T09:03:59.074-0800)

Affects 1.18

### Comment 7: MMK21 (2021-12-11T05:50:34.069-0800)

Affects 1.18.1
Note that the attached resource pack (
) seems to contain unnecessary vanilla assets in the /assets/minecraft/textures/items/ and /assets/minecraft/textures/blocks/ folders, which should probably be removed when/if the pack is remade.

### Comment 8: MMK21 (2022-03-01T09:35:18.784-0800)

Affects 1.18.2

### Comment 9: MMK21 (2023-07-20T07:52:34.762-0700)

I am able to reproduce this in 1.19.2, but some behaviour seems to have changed in 1.19.3 (specifically snapshot 22w42a), and the resource pack no longer appears to have any effect. There are no errors in my log when loading the pack.

### Comment 10: KirbAvion (2023-09-22T10:31:34.252-0700)

Affects 1.20.2.

### Comment 11: bayugoon (2024-07-29T07:09:42.221-0700)

As an FYI for anyone wanting to take advantage of this change if you want to transition from a colored opaque pixel to a fully transparent one you need to insure that the red, blue and green channels are the same same as the starting pixel and not 0, 0, 0 as it may be the default in most software. This is because although it will transition the alpha channel it is still going to transition the red, blue and green channels (unless it's been changed to be ignored for a fully transparent pixel) at the same time so it will be transitioned to black and fully transparent at the same time.
