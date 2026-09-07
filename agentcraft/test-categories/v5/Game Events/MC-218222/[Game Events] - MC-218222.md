# MC-218222: Distance value for Sculk Sensors is limited to integers

**Mojira URL:** [https://bugs.mojang.com/browse/MC-218222](https://bugs.mojang.com/browse/MC-218222)

## Report details

- **Mojira categories:** Game Events; Redstone
- **Project:** MC
- **Issue key:** MC-218222
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-03-09T03:52:36.506-0800
- **Updated:** 2025-04-30T08:12:28.941-0700
- **Resolution date:** 2022-05-18T06:01:28.638-0700
- **Affects versions:** 21w08b; 21w11a; 1.17.1; 21w40a; 21w42a; 1.18 Pre-release 5; 1.18 Release Candidate 3; 1.18.1; 1.18.2; 22w14a; 22w17a; 22w18a; 22w19a
- **Fix versions:** 1.19 Pre-release 1
- **Labels:** block; redstone
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2021-03-09_20.03.38.png; 2021-03-09_20.04.14.png; mc-218222.nbt; MC-218222.png

## Description

Overview
When a sculk sensor outputs a signal, it is currently either 1, 15, or even. Odd signal strengths apart from 1 and 15 are never produced.
Even though blocks on the diagonals are technically further away from the sensor than those directly on the axes, it will still output the same (even) value for both blocks. This issue makes the sculk sensor slightly inaccurate, especially in regards to triangulation.
This happens because the sculk sensor can only receive 9 different integer inputs for how far away a vibration is, and as the equation to calculate what redstone signal to output is a function, you will never be able to get more than 9 outputs out.
This results in the observed behaviour of no odd outputs being produced apart from 1 and 15.

The following screenshot shows which distance currently outputs which signal strengths, and which signal strengths they would output if the sculk sensor could receive a range of distance values from 0-8 as opposed to a discrete set of 9 values. (Click to zoom:
)
Sculk Sensor Output Visualisation (desmos)

Code Analysis
The game calls on the distance value which is an integer
This integer can only have 9 values because the range of the sculk sensor is 8 blocks (0-8), meaning that the function can only output a maximum of 9 values:
public static int getPower({color:#de350b}*int*{color} {color:#57d9a3}distance{color}, int range) {
     double d = (double){color:#57d9a3}distance{color} / (double)range;
     return Math.max(1, 15 - MathHelper.floor(d * 15.0D));
{{}}}
The distance value seems to come from the SculkSensorListener class which initially comes from DistancePredicate and I am unsure as to how challenging it would be to calculate the distance as a double/float as opposed to an integer from the get-go.
Fix
The initial calculations for the distance value, wherever they are done, needs to be calculated as a double/float.
(The setup from this screenshot can be loaded via this structure file if you want to experiment with it yourself:
)
Video
This is a video showcasing a touchscreen display using sculk sensors, where this issue occurs in practice (two pixels cannot be distinguished from each other). The problem of the too imprecise outputs is mentioned and elaborated upon at the given timestamp.
https://youtu.be/y8gc6B_AmZE?t=498

## Comments (13)

### Comment 1: migrated (2021-03-09T03:52:36.506-0800)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: [Mod] violine1101 (2021-03-24T14:32:06.610-0700)

Confirmed.
I've rewritten your bug report to make it a bit more straightforward and easy to understand – I hope I didn't mangle anything; feel free to fix it if I did.

### Comment 3: ncolyer11 (2021-03-25T02:36:17.319-0700)

thanks, the new image is alot clearer (and the title too)

### Comment 4: ncolyer11 (2021-08-31T21:38:45.495-0700)

updated the report with in-depth code analysis and a proposed solution

### Comment 5: ncolyer11 (2021-09-06T00:52:02.347-0700)

got an actual working solution solution now, had to stretch out the prior equation to get it to work in-game haha

### Comment 6: ampolive (2021-10-07T17:58:36.494-0700)

Can confirm in 21w40a.

### Comment 7: ampolive (2021-10-21T17:20:42.870-0700)

Can confirm in 21w42a.

### Comment 8: ncolyer11 (2021-11-19T22:23:55.546-0800)

can confirm in pre-release 5

### Comment 9: ncolyer11 (2021-11-27T01:11:20.236-0800)

still in the latest Release Candidate (3)

### Comment 10: ncolyer11 (2022-03-15T06:58:16.222-0700)

confirmation for 1.18.2

### Comment 11: ncolyer11 (2022-04-11T08:40:06.263-0700)

can confirm for 22w14a

### Comment 12: ncolyer11 (2022-05-04T06:25:39.474-0700)

hey so I did a bit more analysis on this report and it turns out there was rounding/data type changing happening, but it was in a different place to which i originally thought
i've updated the report with all the new info and the fix should be as simple as keeping the distance value as a double instead of converting it to an integer

### Comment 13: pulpetti (2022-05-16T07:08:28.989-0700)

In 22w19a.
