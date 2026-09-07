# MC-260874: Display entity chained interpolation has inconsistent behavior

**Mojira URL:** [https://bugs.mojang.com/browse/MC-260874](https://bugs.mojang.com/browse/MC-260874)

## Report details

- **Mojira categories:** Commands; Entities
- **Project:** MC
- **Issue key:** MC-260874
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2023-03-09T12:06:00.836-0800
- **Updated:** 2025-04-30T04:52:26.687-0700
- **Resolution date:** 2023-04-11T07:07:02.993-0700
- **Affects versions:** 1.19.4 Release Candidate 1; 1.19.4
- **Fix versions:** 23w13a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 12
- **Attachment filenames:** desyncpause.mp4; desyncpause2.mp4; desyncpause3 (epilepsy warning).mp4; desynctest.mp4; desynctest11.mp4; desynctest2.mp4; desynctest3.mp4; desynctest4.mp4; desynctest5.mp4; desynctest6.mp4; desynctest7.mp4; display_test.zip
- **Issue links:** Relates:inward:MC-261600:Inconsistent interpolation animations can result from desync on display entities | Relates:inward:MC-260897:Display entity's previous state of interpolation doesn't work as expected

## Description

Chained interpolation animations appear to have inconsistent behaviors.
This bug was partially fixed in 23w13a. The issue with Animation leaking is resolved, but the issue with Multiple animations from desync still happens. I have separated the second bug into  so that this one can be treated separately. I have kept the original description and repros here for context.
From my understanding, this is a result of two different bugs happening together that may affect a large amount of animations.
Bug 1: Animation leaking
Mid-animation interpolation is fundamentally broken, as it is prone to leaking and ghost-animating the previous animation instantaneously using the duration of the current animation, before starting the next animation, even if the previous animation is already finished.
To go more in depth: The following animation may continue at a position partway along the previous animation, even if the previous animation finished and even if the previous animation should have been instant with 0 duration, indicating that it somehow assumed there was an animation when there was none, by applying the duration of the latest animation to the previous animation. Additionally, it may continue from where the previous animation currently is mid-animation, but from the wrong point in time, and hence not continuing from the proper location.
Bug 2: Multiple animations from desync
See separate bug:
The game can desync, for example, depending on how much the user pauses. This then becomes evident when a transform animation is applied, which can cause animations to behave in multiple different ways based on how desynced they are.
Animations may appear to manifest in multiple ways with a single set of deterministic commands that are different from each other when desynced, when the expected behavior is a single animation.
Pausing the game for various lengths of time may trigger this desync. See:
 and
. This desync appears to be due to interpolation occasionally happening in the tick after it was set, resulting in different forms of the animation appearing for different desync timings. This may or may not be expected behavior by changes to how updates to transformations are handled in the release candidate.
Videos have been attached to demonstrate the varying ways this issue manifests.
This bug is different from  as this bug deals with live interpolation changes that are visible without the user rejoining or reloading mid-animation.
To Reproduce (0 interpolation duration on step 3)
- Place three impulse command blocks in a line

-

```
summon minecraft:block_display ~ ~1 ~ {Tags:[test],block_state:{Name:"stone"},transformation:{translation:[0.0f,0.0f,0.0f],scale:[0.0f,0.0f,0.0f],left_rotation:[0.0f,0.0f,0.0f,1.0f],right_rotation:[0.0f,0.0f,0.0f,1.0f]},start_interpolation:0,interpolation_duration:0}
```

-

```
execute as @e[tag=test] run data merge entity @s {transformation:{scale:[0.1f,0.1f,0.1f],translation:[0.0f,2.0f,0.0f]},start_interpolation:0,interpolation_duration:0}
```

-

```
execute as @e[tag=test] run data merge entity @s {transformation:{scale:[0.1f,0.1f,0.1f],translation:[0.0f,0.0f,0.0f]},start_interpolation:0,interpolation_duration:40}
```

- Power these with a redstone block in order, with varying delay, such as between 0.2 seconds and 5 seconds

- Observe that there are inconsistencies with how the animation occurs. Even though the second command implies immediately transformation, the third command may start from a completely different location and scale instead of continuing smoothly from the second command

- It appears duration from the last transformation gets immediately re-applied on the second transformation, hence the longer you wait to trigger the last command, the higher up the last interpolation seems to start, however this can also be inconsistent.

- See video:

To Reproduce (non-zero interpolation on step 3)
- Place three impulse command blocks in a line

-

```
summon minecraft:block_display ~ ~1 ~ {Tags:[test],block_state:{Name:"stone"},transformation:{translation:[0.0f,0.0f,0.0f],scale:[0.0f,0.0f,0.0f],left_rotation:[0.0f,0.0f,0.0f,1.0f],right_rotation:[0.0f,0.0f,0.0f,1.0f]},start_interpolation:0,interpolation_duration:0}
```

-

```
execute as @e[tag=test] run data merge entity @s {transformation:{scale:[0.1f,0.1f,0.1f],translation:[0.0f,2.0f,0.0f]},start_interpolation:0,interpolation_duration:10}
```

-

```
execute as @e[tag=test] run data merge entity @s {transformation:{scale:[0.1f,0.1f,0.1f],translation:[0.0f,0.0f,0.0f]},start_interpolation:0,interpolation_duration:40}
```

- Power these with a redstone block in order, with varying delay, such as between 0.2 seconds and 5 seconds

- Observe that there are still inconsistencies with how the animation and mid-animation interpolation that was introduced in 1.19.4-pre4 occurs.

To Reproduce (constant 20hz demonstration)
- Create a void superflat world

-

```
/scoreboard objectives add test dummy
```

- Place these 5 commands in order in a command block chain starting with a repeating command block

```
execute positioned 0 -58 0 run summon minecraft:block_display ~ ~ ~ {Tags:[bob],block_state:{Name:"stone"},transformation:{translation:[0.0f,0.0f,0.0f],scale:[0.0f,0.0f,0.0f],left_rotation:[0.0f,0.0f,0.0f,1.0f],right_rotation:[0.0f,0.0f,0.0f,1.0f]},start_interpolation:0,interpolation_duration:0}
scoreboard players add @e[tag=bob] test 1
execute as @e[tag=bob,scores={test=2}] run data merge entity @s {transformation:{scale:[0.1f,0.1f,0.1f],translation:[0.0f,2.0f,0.0f]},start_interpolation:0,interpolation_duration:0}
execute as @e[tag=bob,scores={test=20}] run data merge entity @s {transformation:{scale:[0.1f,0.1f,0.1f],translation:[0.0f,0.0f,0.0f]},start_interpolation:0,interpolation_duration:40}
kill @e[tag=bob,type=minecraft:block_display,scores={test=50..}]
```

- Notice that there are three different animations occurring when we should only be expecting one (the final animation)

- Pause the game for different lengths of time to observe the choice between the three animations may change, making evident there is some sort of desync happening as well

- This datapack can also be used to test the commands above:

- See video:

To Reproduce (20hz desync demonstration)
- Create a void superflat world

-

```
/scoreboard objectives add test dummy
```

- Place these 5 commands in order in a command block chain starting with a repeating command block

```
summon minecraft:block_display ~ ~1 ~ {Tags:[bob,joe],block_state:{Name:"stone"}}
execute as @e[tag=joe] run data merge entity @s {transformation:{scale:[0.1f,0.1f,0.1f],translation:[0.0f,2.0f,0.0f]},start_interpolation:0,interpolation_duration:40}
tag @e remove joe
scoreboard players add @e[tag=bob] test 1
kill @e[tag=bob,type=minecraft:block_display,scores={test=40..}]
```

- Notice that the animation occasionally appears to animate from default transformation instead of staying at the second transformation

- This appears to demonstrate the desync, where the data merge'd transformation is applying on the following tick instead of the summon tick

- Pause the game for different lengths of time to observe that the desync'd animation may or may not appear for different lengths of time.

- This may or may not be expected behavior by changes to how updates to transformations are handled in the release candidate

- See videos:

- ,

Additional analysis
For this video demonstrated in the third repro example:
Command Breakdown:
- in Tick 1 summon display with default values and scale 0

- in Tick 2 set the initial transformation of scale 0.1, translation 0,2,0 with 0 interpolation start/duration

- in Tick 20 set the first animation to scale 0.1, translation 0,0,0 with duration 40

Result: animation is happening in three different places
Expected animation: no scale change, single animation from 0,2,0 to 0,0,0
The three animations in the video:
- stone expands from 0 to 0.1 scale at 0,0,0

- stone expands from 0.05 to 0.1 scale while going from 0,1,0 to 0,0,0

- stone stays 0.1 scale while going from 0,2,0 to 0,0,0 (expected)

Animation analysis:
- This animation is occurring because it took the values in Tick 1 from SUMMON, then interpolated directly with Tick 20, skipping the values set in Tick 2

- This animation is occurring because it took the values in Tick 1 from SUMMON, then immediately applied the transformation in Tick 2. When it reaches Tick 20, it took the duration of 40 ticks, and pre-applied it onto the animation from Tick 2. The game then proceeded to immediately re-animate this made up animation for 18 ticks, (the duration between Tick 2 and Tick 20) between the transforms of Tick 1 and Tick 2, but got cut off afterwards (hence why the animation starts at half scale and half translation). We never see this ghost pre-animation visually as it happens in an instant. The game then started from wherever this position was, and started animating the animation in Tick 20 for the remaining duration.

- This is the proper animation

## Comments (11)

### Comment 1: migrated (2023-03-09T12:06:00.836-0800)

This comment contained multiple image attachments (12), please login to view the attachments.

### Comment 2: ampolive (2023-03-09T12:09:42.498-0800)

Seems similar to MC-259926?

### Comment 3: onnowhere (2023-03-09T12:11:28.186-0800)

See note in bug report I added: This bug is different from  as this bug deals with live interpolation changes that are visible without the user rejoining or reloading mid-animation.
This issue also appeared in this release candidate (possibly pre4 as well)

### Comment 4: onnowhere (2023-03-10T02:39:04.236-0800)

Related and/or same issue MC-260885

### Comment 5: onnowhere (2023-03-10T03:19:08.471-0800)

This is somewhat major issue as simply starting from a non-default transformation now becomes very difficult to make reliable: https://bugs.mojang.com/secure/attachment/527194/desynctest7.mp4
This repro is:
In a repeating command block chain

```scoreboard players add @e[tag=loop] test 1
execute as @e[tag=loop,scores={test=21}] run data merge entity @s {transformation:{translation:[0.0f,0.0f,0.0f],scale:[0.1f,0.1f,0.1f]},start_interpolation:0,interpolation_duration:0,block_state:{Name:"stone"}}
execute as @e[tag=loop,scores={test=41}] run data merge entity @s {transformation:{translation:[2.0f,0.0f,0.0f],scale:[0.1f,0.1f,0.1f]},start_interpolation:0,interpolation_duration:40}
execute at @e[tag=loop,scores={test=81..}] run summon minecraft:block_display ~ ~ ~ {Tags:[loop]}
kill @e[tag=loop,scores={test=81..}]```
Then run

```/scoreboard objectives add test dummy
/summon minecraft:block_display ~ ~1 ~ {block_state:{Name:"stone"},Tags:[loop]}```
This one is trying to best case it: I don't set the initial transformation until a full 20 ticks after summon, but still I cannot make a reliable starting animation. It still jumps to a different unexpected scale at tick 41 that is halfway between the default transformation and the transformation at tick 21.

### Comment 6: onnowhere (2023-03-10T03:58:11.596-0800)

I did one more experiment to verify if my understanding is correct, outlined below:
Video: https://bugs.mojang.com/secure/attachment/527204/desynctest11.mp4
- Assume we NBT summon (not execute/data merge in same tick) without specifying transform or interpolation at all

- at 30 ticks, we try to initialize the animation with scale 2, translation 0,2,0, start 0, duration 0

- at 40 ticks, we do an animation to scale 1, translation 0,0,0 with start 0, duration 20

- The game will animate from scale 2, translation 0,2,0 to scale 1, translation 0,0,0 across 20 ticks immediately, but get cut off at 40-30=10 ticks (this happens instantaneously before the tick 40 animation starts)

- The animation will then start from scale 1.5, translation 0,1.5,0 and THEN start animating to scale 1, translation 0,0,0 over 20 ticks

The video displays this phenomenon EXACTLY as described above, however, the first loop seems to animate the 80 duration animation instantly, resulting in no animation at all. This was unexpected. The second loop illustrates the above description precisely.
I was never able to observe the actual intended animation. Something with the normal function of interpolation animation does not work properly.
Repro:
In a repeating command chain:

```scoreboard players add @e[tag=loop] test 1
execute as @e[tag=loop,scores={test=20}] run data merge entity @s {transformation:{translation:[0f,2f,0f],scale:[2f,2f,2f]},start_interpolation:0,interpolation_duration:0}
execute as @e[tag=loop,scores={test=40}] run data merge entity @s {transformation:{translation:[0f,0f,0f],scale:[1f,1f,1f]},start_interpolation:0,interpolation_duration:80}```
Then:

```/scoreboard objectives add test
/summon block_display ~ ~1 ~ {block_state:{Name:"stone"},Tags:[loop]}```

### Comment 7: onnowhere (2023-03-10T04:24:38.283-0800)

From my understanding, this is a result of two different bugs happening together.
1. Animation leaking. Mid-animation interpolation is fundamentally broken, as it is prone to leaking and ghost-animating the previous animation instantaneously using the duration of the current animation, before starting the next animation, even if the previous animation is already finished.
2. Multiple animations from desync. The game can desync, for example, depending on how much the user pauses. This then becomes evident when a transform animation is applied, which can cause animations to behave in multiple different ways based on how desynced they are.

### Comment 8: onnowhere (2023-03-10T04:31:25.465-0800)

So, based on this finding, the best map-making workaround at the moment to ensure a reliable animation is:
- If you specify an interpolation_duration, the duration must be less than or equal to the total ticks from the last animation, to ensure the 'ghost animation' is fully finished
Example:

- If at 40 ticks from the last animation, you create an animation with > 40 duration, it will highly likely fail interpolation

- If at 40 ticks from the last animation, you create an animation at <= 40 duration, it will succeed

- *However, the caveat is that, even if you do it right, it might still desync and do something else unexpected*

### Comment 9: onnowhere (2023-04-05T02:14:27.858-0700)

This bug was partially fixed in 23w13a. The issue with animation leaking is resolved, but the desync still happens. The best way to reproduce this is with the 20hz demonstrations, along with holding down the pause (ESC) button.

### Comment 10: onnowhere (2023-04-05T02:28:25.672-0700)

I created  to separate the two apparent bugs. This issue should be focusing on the animation leaking that was fixed in 23w13a, and  should be focusing on the desync issue.
This issue can be resolved as fixed in 23w13a.

### Comment 11: onnowhere (2023-04-11T00:44:38.187-0700)

(bumping comment)
Bug can be resolved as fixed in 23w13a, and relates to
