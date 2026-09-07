# MC-114265: Mipmaps are too dark around transparent edges in textures (e.g. side of grass)

**Mojira URL:** [https://bugs.mojang.com/browse/MC-114265](https://bugs.mojang.com/browse/MC-114265)

## Report details

- **Mojira categories:** Rendering
- **Project:** MC
- **Issue key:** MC-114265
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2017-02-28T08:09:01.871-0800
- **Updated:** 2025-10-08T05:27:10.301-0700
- **Resolution date:** 2025-10-08T00:52:03.260-0700
- **Affects versions:** Minecraft 1.11.2; Minecraft 17w06a; Minecraft 1.13; Minecraft 1.13.1-pre1; Minecraft 1.14.2; Minecraft 1.14.3 Pre-Release 2; Minecraft 1.14.3; Minecraft 1.14.4 Pre-Release 6; 1.14.4; 1.15 Pre-release 1; 1.15.2; 1.16.1; 1.16.5; 21w10a; 1.17; 1.17.1; 21w37a; 21w38a; 21w42a; 21w43a; 1.18 Pre-release 1; 1.18 Pre-release 7; 1.18 Pre-release 8; 1.18 Release Candidate 3; 1.18; 1.18.1 Release Candidate 1; 1.18.1; 22w03a; 22w05a; 1.18.2; 22w13a; 22w15a; 22w18a; 22w19a; 1.19 Pre-release 1; 1.19 Pre-release 2; 1.19 Pre-release 3; 1.19 Pre-release 4; 1.19; 1.19.1 Pre-release 5; 1.19.1; 1.19.2; 22w44a; 22w46a; 1.19.3 Pre-release 1; 1.19.3 Pre-release 2; 1.19.3; 23w03a; 23w04a; 23w05a; 1.19.4 Pre-release 1; 1.19.4; 23w12a; 23w13a; 1.20.1; 23w33a; 24w13a; 24w14a; 1.20.6; 24w36a; 1.21.3; 1.21.4 Release Candidate 3; 25w02a; 1.21.5; 25w16a; 1.21.6 Pre-Release 3; 1.21.6 Pre-Release 4; 1.21.6
- **Fix versions:** 25w41a
- **Area:** Platform
- **Votes:** 1
- **Watchers:** 2
- **Attachments:** 16
- **Attachment filenames:** 1.14.3 mipmap levels=4.png; 2021-10-21_00.28.24.png; 2021-11-11_13.24.08.png; grass_block_side_overlay.png; Grass1BigView.png; image-2024-10-25-16-12-59-287.png; image-2024-10-25-16-13-43-992.png; Max level 0.png; Max level 4.png; options.txt; Original 1.11.2.png; Proof of concept.png; SRGBAverager.java; SRGBCalculator.java; SRGBTable.java; World.zip
- **Issue links:** Duplicate:inward:MC-295967:Visual Bug | Duplicate:inward:MC-272611:Grass Blocks have a weird graphical glitch | Duplicate:inward:MC-270166:the grass was look like savanna, but in taiga | Duplicate:inward:MC-259491:Mipmapping causes some block faces to become too dark again in 1.19.3 | Relates:inward:MC-218609:Mipmapping causes some block faces to become too dark | Duplicate:inward:MC-230457:Grass Block Bug | Duplicate:inward:MC-226260:Grass & Snow doesn't play nicely with mip-mapping | Duplicate:inward:MC-176520:Mipmapping in 1.14 and 1.15 is Messed Up | Duplicate:inward:MC-155702:Far away grass blocks look like they have vines on the side, if viewed almost parallel | Duplicate:inward:MC-145394:Block Visual Bug

## Description

The bug
This has been an issue for a while. It's especially noticeable at level 3 of the side of grass. See the screenshots, where I placed a row of grass on a row of dirt. With mipmaps, half of the grass block is practically black at the 'optimal' distance where the 2x2 mipmap or further is used.
How to reproduce
Open this world
 with these settings
 and look straight ahead without moving.
 Observe the dark patches with the side of the grass.
Proposed solution
Using Yarn mappings for 1.14.4, replace this method:
net.minecraft.client.texture.Sprite

```
private static int blendPixels(int int_1, int int_2, int int_3, int int_4) {
        return SRGBAverager.average(int_1, int_2, int_3, int_4);
    }
```
using these classes provided by :
Original analysis
I've looked it up in MCP 9.30/9.31 (corresponding to Minecraft 1.10.2). In net.minecraft.client.renderer.texture.TextureUtil, generateMipmapData is responsible for mipmap generation. It turns out not to use proper weighting by the alpha channel. Anything that isn't fully transparent is given the full weight, and anything that is is treated as black. That's where the darkness comes from.
The correct model is most natural when using colors premultiplied by alpha: just average everything. If you don't use premultiplied colors, you must multiply colors by alpha before averaging and divide the resulting color by the resulting alpha afterward.
Premultiplied also has the advantage that any blending steps you don't control directly work correctly, like texture filtering and frame buffer blending. Minecraft won't really experience either the advantages or the disadvantages, but it's the cleaner model that would've prevented problems like this bug from the start. That's something to consider.
Adding to the problem is that Minecraft tries to apply gamma correction to the alpha channel. That blows up the opacity, only emphasizing exactly those texels that are too dark. Gamma correction of the alpha channel doesn't make sense anyway because colors can deviate either way depending on what's blended with what. The general standard—which is also what you'll get natively if you enable frame buffer and texture sRGB—is to use sRGB (which is a little more involved than x^2.2) for colors and keep the alpha channel linear.

## Comments (46)

### Comment 1: migrated (2017-02-28T08:09:01.871-0800)

This comment contained multiple image attachments (16), please login to view the attachments.

### Comment 2: marcono1234 (2017-02-28T08:38:41.354-0800)

Do you think this is also causing the fire animation of a burning mob to get black / dark at the edges when you move away?

### Comment 3: migrated (2017-02-28T10:05:58.326-0800)

: Yes, looks like it! Good catch. If I end up making a proof of concept mod, I'll include a burning mob in the screenshots which should demonstrate it nicely.

### Comment 4: migrated (2017-02-28T14:49:32.938-0800)

Here's a proof of concept based on MCP 9.37/Minecraft 1.11.2. Put the Java files in example/jonathan2520 (next to Start.java) as indicated by the package. In net.minecraft.client.renderer.texture.TextureUtil, change the line

```aint2[i1 + j1 * j] = blendColors(aint1[k1 + 0], aint1[k1 + 1], aint1[k1 + 0 + l], aint1[k1 + 1 + l], flag);```
to

```aint2[i1 + j1 * j] = example.jonathan2520.SRGBAverager.average(aint1[k1 + 0], aint1[k1 + 1], aint1[k1 + 0 + l], aint1[k1 + 1 + l]);```
Full changes:
- Proper weighting by alpha channel, obviously.

- Proper sRGB.

- According to the new model, if all four inputs are entirely transparent, the color is undefined. (Kind of like the Invisible Pink Unicorn. No way to tell from its appearance that it's supposed to be pink.) I've defined it by using an unweighted average in that case. Minecraft originally made it black. Doesn't really matter, I think, but there it is.

- Removed the special case where if at least one texel in the entire texture/atlas was fully transparent, alpha values under 96 would be cut to 0. Might serve some purpose but I don't see sense in it and it's inconvenient. It can be re-added if necessary.

- Although I haven't benchmarked, it should be significantly faster. For starters, all 4 Math.pow calls are gone. I came up with a table-based sRGB encoding scheme that's simple, fast and exact.

Indeed, it fixes the black edges around fire as well.

### Comment 5: migrated (2017-03-02T13:50:10.660-0800)

Some more observations:
Minecraft uses interpolation between mipmaps (GL_NEAREST_MIPMAP_LINEAR). That's what I remembered but the hard transitions to darkness on the side of grass threw me for a loop. What even causes those? Anyway, that interpolation sans premultiplication can cause further artifacts. The hard pixel art edges in Minecraft's textures make that as bad as it can be. It's also a case where my preservation of invisible colors can reduce the ensuing artifacts, if source images are authored with sensible invisible colors which they generally aren't. I guess it may be better to process the mipmap pyramid in reverse afterward, using the color of the lower-res mipmap to replace invisible colors. That will catch the worst of it regardless of authoring. You could actually do it in the forward pass because you only need to propagate back one level.
I don't know the full pipeline that well. If I did I might've been able to experiment with some more stuff like premultiplication. (Very invasive, requiring adjustments to all blend functions and colors passed to OpenGL. Would also have to check for pure alpha testing without blending which doesn't play nicely with it.) Oh well. Not like it or the work I've done so far is going to accomplish much anyway until Mojang sees it, which could take a while.
The sRGB constant I called alpha is really called a. What's in a name?

### Comment 6: migrated (2017-03-04T12:39:19.711-0800)

I did just try to make Minecraft use premultiplication. Turns out OpenGL is abstracted away enough to get away with a few hooks to adjust colors and blend functions. For the most part things look okay. But there's one major problem: fixed-function fog can't deal with premultiplication. Transparent stuff in the distance (water, clouds, stained glass, …) turns bright white. The general solution is to do the right calculation per fragment, which requires a fragment shader. So probably not going to happen for now.
An observation with my change to mipmap generation (and without the premultiplication stuff from above) is that leaves keep some holes in the distance even with mipmaps enabled. Normally they become darker and entirely opaque with mipmaps, for the same reason the uglier problems with mipmaps occur. Opacification is a side effect of gamma correction of the alpha channel, pushing it over the alpha test reference more easily. I explicitly took that out because it's nonsense.
Although the transparency introduced by my patch would be expected for transparent leaves, I must admit I liked the shimmer-free look of opaque leaves. I've never been able to decide what's better. If you want to, you can reintroduce the opacifying behavior on top of my mipmap generation by sRGB-decoding the reference alpha passed to glAlphaFunc. Where 0.5 is currently passed to render stuff like leaves, you'd pass ((0.5+0.055)/(1+0.055))^2.4 ≈ 0.214. The result will be virtually identical, except all the other problems like darkening and blend opacification will be gone.
I think this will be the final comment for now. Definitely enough analysis. The minimally invasive patch that I posted solves most of the problem with minimal regression potential. I'm putting my money on that.

### Comment 7: migrated (2019-06-27T05:44:53.191-0700)

Possibly related: since playing on 1.14, I keep seeing this sort of thing on grass on mipmap levels=4:

### Comment 8: migrated (2019-07-17T22:21:02.043-0700)

This issue also affects 1.14.4 Pre-Release 6.

### Comment 9: migrated (2019-07-19T12:06:36.596-0700)

And this bug made its way into the official 1.14.4 release.

### Comment 10: migrated (2020-08-01T09:38:23.953-0700)

Still occurs 1.16.1

### Comment 11: migrated (2021-03-10T10:06:05.480-0800)

This effect has become very noticable in snapshot 21w10a

### Comment 12: migrated (2021-03-10T10:10:37.626-0800)

Confirmed RX 580 Graphic card AMD

### Comment 13: migrated (2021-05-20T06:16:14.005-0700)

I made a fabric mod for 1.16.5 that uses 's classes and a very simple mixin. The mod works really well, however before uploading it anywhere I want to ask  for permission to do so. I'll make sure to credit him since 90% of the mod is literally his code.

### Comment 14: ampolive (2021-08-18T04:31:23.471-0700)

Can confirm in 1.17.1.

### Comment 15: Tinsel (2021-09-15T12:47:58.506-0700)

In 21w37a

### Comment 16: Tinsel (2021-09-23T13:54:15.172-0700)

In 21w38a

### Comment 17: Tinsel (2021-10-21T14:18:28.874-0700)

In 21w42a

### Comment 18: Tinsel (2021-10-27T10:28:34.111-0700)

In 21w43a

### Comment 19: migrated (2021-11-01T08:55:58.322-0700)

@jonathan2520 Under what license is the code? And may I use it in my own project?

### Comment 20: Tinsel (2021-11-11T14:25:53.942-0800)

Still in 1.18 pre-1, it gets really bad sometimes for me. Using level 4 mipmaps

### Comment 21: Tinsel (2021-11-23T13:23:40.204-0800)

In 1.18 Pre-7. Is there any computer settings perhaps that I can do it make this less noticeable? I fear it may not be fixed for next release

### Comment 22: Tinsel (2021-11-24T12:09:13.444-0800)

Still in 1.18 Pre-8

### Comment 23: Tinsel (2021-12-06T09:41:39.075-0800)

In 1.18.1 Pre-1

### Comment 24: Tinsel (2021-12-07T10:21:05.368-0800)

Still in 1.18.1 Release Candidate 1

### Comment 25: Tinsel (2022-02-02T12:20:02.206-0800)

In 22w05a

### Comment 26: Tinsel (2022-04-03T20:26:55.980-0700)

Still in 22w13a

### Comment 27: Tinsel (2022-04-18T20:14:45.766-0700)

Still in 22w15a

### Comment 28: Tinsel (2022-05-05T21:59:03.352-0700)

In 22w18a

### Comment 29: Tinsel (2022-05-12T18:09:12.409-0700)

In 22w19a

### Comment 30: Tinsel (2022-05-18T13:25:15.514-0700)

In 1.19 Pre-1

### Comment 31: Tinsel (2022-05-24T11:37:28.861-0700)

Can confirm for 1.19 Pre-2

### Comment 32: Tinsel (2022-05-25T10:34:28.915-0700)

In 1.19 Pre-3

### Comment 33: Tinsel (2022-05-30T09:59:37.540-0700)

In  1.19 Pre-4

### Comment 34: Tinsel (2022-06-01T20:50:29.098-0700)

Can confirm for 1.19 Pre-5

### Comment 35: Tinsel (2022-06-09T14:57:29.698-0700)

In 1.19

### Comment 36: Tinsel (2022-06-24T19:41:30.094-0700)

In 1.19.1 Release Candidate 1

### Comment 37: Tinsel (2022-07-15T09:20:24.793-0700)

In 1.19.1 Pre-5

### Comment 38: Tinsel (2022-11-05T16:16:16.170-0700)

In 22w44a

### Comment 39: Tinsel (2022-11-16T10:58:34.569-0800)

In 22w46a

### Comment 40: Tinsel (2022-11-22T12:08:39.286-0800)

In 1.19.3 Pre-1

### Comment 41: migrated (2023-01-07T09:35:29.038-0800)

Fixed if MipMap levels are set to 0

### Comment 42: migrated (2023-01-07T10:00:38.493-0800)

Because that literally disabled mipmapping, and the issue is with mipmapping...

### Comment 43: migrated (2023-01-07T19:28:03.302-0800)

Its going to be like permanently stuck in the game, because Mojang doesnt see it or something, i mean its been in the game for 4 years

### Comment 44: migrated (2023-02-25T10:46:10.583-0800)

I found out how to fix this. Take every pixel of a broken texture that has completely opaque and transparent pixels, and blur all of the pixels together in an image editing program to get the average color. Use the color picker on that pixel, erase the pixel, then replace every transparent pixel with that averaged color, at 49% or less opacity. Pixels under 50% opacity are invisible (unless they're on blocks like water or stained glass), but will be blurred with the mipmapping. Here's the overlay texture on the side of a grass block after I fixed it:
The reason you should use 49% opacity is because the lower the opacity, the lower the color quality will be. If you use 1% opacity, it'll probably get rounded to RGB(127,127,127). 49% is the highest opacity that will still be invisible but have the highest quality.

### Comment 45: Felix14_v2 (2024-10-25T06:17:21.981-0700)

Sodium has this bug fixed since 0.5.0:
— Mip-mapping has been greatly improved so that terrain no longer has a black outline around certain textures when viewed at extreme angles. (Note: This has the consequence that some textures, such as those used for leaves, may seem slightly brighter than they did before. However, we think this generally looks more accurate to the original texture work, and believe the original behavior was a bug.)

(Don't pay attention to the touch buttons, I tested this fix on PojavLauncher)
Can confirm in the latest MC version, by the way. Mipmaps generation is still broken in vanilla Minecraft.

### Comment 46: Xfrtrex (2024-11-26T19:34:53.107-0800)

Can confirm 1.21.4 Pre-Release 3
