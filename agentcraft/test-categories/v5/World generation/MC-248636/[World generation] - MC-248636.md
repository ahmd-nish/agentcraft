# MC-248636: The game output and server console are logged and spammed with "Creating a MIN function between two non-overlapping inputs" when joining or creating a world

**Mojira URL:** [https://bugs.mojang.com/browse/MC-248636](https://bugs.mojang.com/browse/MC-248636)

## Report details

- **Mojira categories:** World generation
- **Project:** MC
- **Issue key:** MC-248636
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-02-16T10:38:45.092-0800
- **Updated:** 2025-04-29T20:02:36.108-0700
- **Resolution date:** 2022-02-23T01:23:40.244-0800
- **Affects versions:** 22w07a; 1.18.2 Pre-release 1; 1.18.2 Pre-release 2
- **Fix versions:** 1.18.2 Pre-release 3
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** MC-248636.png

## Description

The Bug:
The game output and server console are logged and spammed with "Creating a MIN function between two non-overlapping inputs" when joining or creating a world.
This issue was not present in 1.18.1 or 22w06a.
The following messages were printed into the server log shortly after booting up a server running 22w07a.

```
[18:30:43 WARN]: Creating a MIN function between two non-overlapping inputs: h[type=SQUEEZE, input=j[type=MUL, input=i[type=Interpolated, function=c[input=u[settings=ctz[minY=0, height=128, noiseSamplingSettings=cty@26e25469, topSlideSettings=cua[target=0.9375, size=3, offset=0], bottomSlideSettings=cua[target=2.5, size=4, offset=-1], noiseSizeHorizontal=1, noiseSizeVertical=2, islandNoiseOverride=false, isAmplified=false, largeBiomes=false, terrainShaper=cby@4426f128], input=i[type=CacheOnce, function=a[type=ADD, f1=j[type=MUL, input=h[type=QUARTER_NEGATIVE, input=a[type=MUL, f1=a[type=ADD, f1=a[type=ADD, f1=y[fromY=-64, toY=320, fromValue=1.5, toValue=-1.5], f2=i[type=FlatCache, function=i[type=Cache2D, function=a[type=ADD, f1=a[type=MUL, f1=INSTANCE, f2=j[type=ADD, input=j[type=MUL, input=i[type=CacheOnce, function=INSTANCE], minValue=-1.0, maxValue=-1.0, argument=-1.0], minValue=0.0, maxValue=0.0, argument=1.0], minValue=0.0, maxValue=0.0], f2=a[type=MUL, f1=v[continentalness=i[type=FlatCache, function=t[shiftX=i[type=FlatCache, function=i[type=Cache2D, function=q[offsetNoise=dht@f02f31f]]], shiftY=f[value=0.0], shiftZ=i[type=FlatCache, function=i[type=Cache2D, function=r[offsetNoise=dht@f02f31f]]], xzScale=0.25, yScale=0.0, noise=dht@13918009]], erosion=i[type=FlatCache, function=t[shiftX=i[type=FlatCache, function=i[type=Cache2D, function=q[offsetNoise=dht@f02f31f]]], shiftY=f[value=0.0], shiftZ=i[type=FlatCache, function=i[type=Cache2D, function=r[offsetNoise=dht@f02f31f]]], xzScale=0.25, yScale=0.0, noise=dht@164323f9]], weirdness=i[type=FlatCache, function=t[shiftX=i[type=FlatCache, function=i[type=Cache2D, function=q[offsetNoise=dht@f02f31f]]], shiftY=f[value=0.0], shiftZ=i[type=FlatCache, function=i[type=Cache2D, function=r[offsetNoise=dht@f02f31f]]], xzScale=0.25, yScale=0.0, noise=dht@469b28ac]], spline=ctx$$Lambda$3304/0x000000080133fde0@5e99a16b, minValue=-0.81, maxValue=2.5], f2=i[type=CacheOnce, function=INSTANCE], minValue=-0.81, maxValue=2.5], minValue=-0.81, maxValue=2.5]]], minValue=-2.31, maxValue=4.0], f2=a[type=MUL, f1=i[type=FlatCache, function=i[type=Cache2D, function=a[type=ADD, f1=j[type=MUL, input=j[type=ADD, input=j[type=MUL, input=i[type=CacheOnce, function=INSTANCE], minValue=-1.0, maxValue=-1.0, argument=-1.0], minValue=0.0, maxValue=0.0, argument=1.0], minValue=0.0, maxValue=0.0, argument=0.0], f2=a[type=MUL, f1=v[continentalness=i[type=FlatCache, function=t[shiftX=i[type=FlatCache, function=i[type=Cache2D, function=q[offsetNoise=dht@f02f31f]]], shiftY=f[value=0.0], shiftZ=i[type=FlatCache, function=i[type=Cache2D, function=r[offsetNoise=dht@f02f31f]]], xzScale=0.25, yScale=0.0, noise=dht@13918009]], erosion=i[type=FlatCache, function=t[shiftX=i[type=FlatCache, function=i[type=Cache2D, function=q[offsetNoise=dht@f02f31f]]], shiftY=f[value=0.0], shiftZ=i[type=FlatCache, function=i[type=Cache2D, function=r[offsetNoise=dht@f02f31f]]], xzScale=0.25, yScale=0.0, noise=dht@164323f9]], weirdness=i[type=FlatCache, function=t[shiftX=i[type=FlatCache, function=i[type=Cache2D, function=q[offsetNoise=dht@f02f31f]]], shiftY=f[value=0.0], shiftZ=i[type=FlatCache, function=i[type=Cache2D, function=r[offsetNoise=dht@f02f31f]]], xzScale=0.25, yScale=0.0, noise=dht@469b28ac]], spline=ctx$$Lambda$3306/0x0000000801340410@4197f379, minValue=0.0, maxValue=1.28], f2=i[type=CacheOnce, function=INSTANCE], minValue=0.0, maxValue=1.28], minValue=0.0, maxValue=1.28]]], f2=h[type=HALF_NEGATIVE, input=k[noise=dht@4e445c59, xzScale=1500.0, yScale=0.0], minValue=-3.137254901960784, maxValue=6.274509803921568], minValue=-4.015686274509803, maxValue=8.031372549019606], minValue=-6.325686274509803, maxValue=12.031372549019606], f2=i[type=FlatCache, function=i[type=Cache2D, function=a[type=ADD, f1=j[type=MUL, input=j[type=ADD, input=j[type=MUL, input=i[type=CacheOnce, function=INSTANCE], minValue=-1.0, maxValue=-1.0, argument=-1.0], minValue=0.0, maxValue=0.0, argument=1.0], minValue=0.0, maxValue=0.0, argument=10.0], f2=a[type=MUL, f1=v[continentalness=i[type=FlatCache, function=t[shiftX=i[type=FlatCache, function=i[type=Cache2D, function=q[offsetNoise=dht@f02f31f]]], shiftY=f[value=0.0], shiftZ=i[type=FlatCache, function=i[type=Cache2D, function=r[offsetNoise=dht@f02f31f]]], xzScale=0.25, yScale=0.0, noise=dht@13918009]], erosion=i[type=FlatCache, function=t[shiftX=i[type=FlatCache, function=i[type=Cache2D, function=q[offsetNoise=dht@f02f31f]]], shiftY=f[value=0.0], shiftZ=i[type=FlatCache, function=i[type=Cache2D, function=r[offsetNoise=dht@f02f31f]]], xzScale=0.25, yScale=0.0, noise=dht@164323f9]], weirdness=i[type=FlatCache, function=t[shiftX=i[type=FlatCache, function=i[type=Cache2D, function=q[offsetNoise=dht@f02f31f]]], shiftY=f[value=0.0], shiftZ=i[type=FlatCache, function=i[type=Cache2D, function=r[offsetNoise=dht@f02f31f]]], xzScale=0.25, yScale=0.0, noise=dht@469b28ac]], spline=ctx$$Lambda$3305/0x00000008013401f0@5185c375, minValue=0.0, maxValue=8.0], f2=i[type=CacheOnce, function=INSTANCE], minValue=0.0, maxValue=8.0], minValue=0.0, maxValue=8.0]]], minValue=-50.60549019607842, maxValue=96.25098039215685], minValue=-12.651372549019605, maxValue=96.25098039215685], minValue=-50.60549019607842, maxValue=385.0039215686274, argument=4.0], f2=dhq@4284a2d7, minValue=-2105.8414901960787, maxValue=2440.239921568628]]]]], minValue=-Infinity, maxValue=Infinity, argument=0.64], minValue=-0.4583333333333333, maxValue=0.4583333333333333] and f[value=64.0]
```

```
[18:30:43 WARN]: Creating a MIN function between two non-overlapping inputs: h[type=SQUEEZE, input=j[type=MUL, input=i[type=Interpolated, function=c[input=u[settings=ctz[minY=0, height=128, noiseSamplingSettings=cty@396bf87c, topSlideSettings=cua[target=-23.4375, size=64, offset=-46], bottomSlideSettings=cua[target=-0.234375, size=7, offset=1], noiseSizeHorizontal=2, noiseSizeVertical=1, islandNoiseOverride=true, isAmplified=false, largeBiomes=false, terrainShaper=cby@60f506ba], input=i[type=CacheOnce, function=a[type=ADD, f1=ctk$g@5a2ce771, f2=dhq@755eceb1, minValue=-687.2557499999999, maxValue=686.9744999999999]]]]], minValue=-Infinity, maxValue=Infinity, argument=0.64], minValue=-0.4583333333333333, maxValue=0.4583333333333333] and f[value=64.0]
```
Steps to Reproduce:
- Launch an instance of 22w07a with logs enabled.

- Create or join a world.

- Watch the game output log closely.

- Take note as to whether or not the game output and server console are logged and spammed with "Creating a MIN function between two non-overlapping inputs" when joining or creating a world.

Observed Behavior:
The game output and server console are logged and spammed with "Creating a MIN function between two non-overlapping inputs" when joining or creating a world.
Expected Behavior:
The "Creating a MIN function between two non-overlapping inputs" warnings wouldn't be logged.

## Comments (2)

### Comment 1: migrated (2022-02-16T10:38:45.092-0800)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: KirbAvion (2022-02-18T22:01:55.019-0800)

Can confirm for 1.18.2 pre-release 1.
