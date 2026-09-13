# MC-121997: Every dimension's world border is operating independently, and doesn't appear where it actually is

**Mojira URL:** [https://bugs.mojang.com/browse/MC-121997](https://bugs.mojang.com/browse/MC-121997)

## Report details

- **Mojira categories:** Commands
- **Project:** MC
- **Issue key:** MC-121997
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2017-11-15T16:55:47.752-0800
- **Updated:** 2025-04-30T07:02:22.051-0700
- **Resolution date:** 2022-08-27T12:45:52.403-0700
- **Affects versions:** Minecraft 1.12.2; Minecraft 17w45b; Minecraft 17w46a; Minecraft 17w47a; Minecraft 17w47b; Minecraft 17w48a; Minecraft 17w49a; Minecraft 17w49b; Minecraft 17w50a; Minecraft 18w01a; Minecraft 18w02a; Minecraft 18w03b; Minecraft 18w05a; Minecraft 18w06a; Minecraft 18w07c; Minecraft 18w08a; Minecraft 18w10c; Minecraft 18w11a; Minecraft 18w14a; Minecraft 18w14b; Minecraft 18w20c; Minecraft 18w21b; Minecraft 18w22c; Minecraft 1.13-pre1; Minecraft 1.13-pre2; Minecraft 1.13-pre3; Minecraft 1.13-pre6; Minecraft 1.13-pre9; Minecraft 1.13; Minecraft 18w30a; Minecraft 18w30b; Minecraft 18w31a; Minecraft 18w32a; Minecraft 18w33a; Minecraft 1.13.1-pre1; Minecraft 1.13.1-pre2; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w43b; Minecraft 18w43c; Minecraft 18w44a; Minecraft 18w45a; Minecraft 18w46a; Minecraft 1.14; Minecraft 1.14.1; Minecraft 1.14.2 Pre-Release 1; Minecraft 1.14.2 Pre-Release 2; Minecraft 1.14.2; Minecraft 1.14.3; Minecraft 1.14.4 Pre-Release 1; Minecraft 1.14.4 Pre-Release 3; Minecraft 1.14.4 Pre-Release 4; Minecraft 1.14.4 Pre-Release 5; Minecraft 1.14.4 Pre-Release 6; 1.14.4; 19w34a; 19w35a; 19w36a; 19w37a; 19w38b; 19w39a; 19w40a; 19w41a; 19w42a; 19w44a; 19w45a; 19w45b; 19w46b; 1.15 Pre-release 1; 1.15 Pre-Release 2; 1.15 Pre-release 3; 1.15 Pre-release 4; 1.15 Pre-release 5; 1.15 Pre-release 6; 1.15 Pre-release 7; 1.15; 1.15.1; 1.15.1 Pre-release 1; 1.15.2 Pre-Release 1; 1.15.2 Pre-release 2; 1.15.2; 20w06a; 20w07a; 20w08a; 20w09a; 20w10a; 20w11a; 20w12a; 20w13a; 20w13b; 20w14a; 20w15a; 20w16a; 20w17a; 20w18a; 20w19a; 20w20a; 20w20b; 20w21a; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 8; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w28a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Release Candidate 1; 1.16.2 Release Candidate 2; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4 Pre-release 1; 1.16.4 Pre-release 2; 1.16.4 Release Candidate 1; 1.16.4; 20w46a; 20w48a; 20w51a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w10a; 21w11a; 1.17 Pre-release 2; 1.17; 1.17.1; 21w44a
- **Fix versions:** 1.18 Pre-release 1
- **Labels:** end; nether; overworld; the_end; the_nether; world-border
- **Watchers:** 1
- **Attachments:** 0
- **Issue links:** Relates:outward:MC-62550:Worldborder not correctly initialized for the End and Nether

## Description

The bug
Every dimension's world border is operating independently. Changing the world border in one dimension doesn't effect the other dimensions, and in the case of the Nether and End, won't visually change location even though it has.
How to reproduce
- Go into creative mode and do this command in the overworld:

```
/worldborder set 1000
```

- Go to the Nether and /tp to the world border there:

```
/tp @s 0 50 500
```

- Do this command while in the Nether:

```
/worldborder set 10
```
It looks as though the world border hasn't moved at all.

```
/worldborder get
```
and see that it says the border is 10 blocks, even though you can see otherwise. It looks like the original 1000-block length border.

- Stay within the bounds of the world border you see and put yourself in survival. You will die. The world border you saw wasn't the world border, it really did move to 10 blocks wide.

- Go back into creative mode and re-enter the nether, this time teleport to the world border's centre.

```
/tp @s 0 50 0
```

- Go into survival and walk around. The actual world border is invisible, but it's still at 10 blocks wide. You'll experience an invisible force hindering your walk.

- Return to the overworld and do the /worldborder get command again. Now it tells you it's 1000 blocks, which it is... for that dimension.

- Repeat for the End, but use a number other than 10 to ensure that the Nether world border and the End world border are operating separately from each other as well as the overworld's.
If you do the /worldborder get command in all three dimensions, you will get three different answers... and the Nether and End's world borders will not be where they look like they are. They will look like they have the same border as the overworld.

- Repeat the process, changing world border centres instead of size. Changing the worldborder's centre in the Nether won't be the coordinates you put in, they'll be divided by 8. All three dimensions can have different world border centres as they are all operating independently.

## Comments (16)

### Comment 1: migrated (2019-04-30T07:41:32.011-0700)

Still affects 1.14 full release

### Comment 2: ZeNico13 (2019-05-13T10:23:45.484-0700)

Still in 1.14.1 Release

### Comment 3: ZeNico13 (2019-05-17T12:19:33.402-0700)

Still in 1.14.2 Pre-Release 1 and 1.14.2 Pre-Release 2

### Comment 4: BisUmTo (2020-03-15T12:47:26.871-0700)

If you change the worlborder from the nether with the command
/execute in minecraft:overworld run worldborder set 10
It works fine

### Comment 5: migrated (2020-03-20T14:13:41.575-0700)

I can confirm it's still the case in 20w12a as well.
BisUmTo your command does put the border visuals in the nether to that area, but that also moves the worldborder in the overworld, which is not always what people want. Considering the coordinate system in the nether, one might want to limit the worldborder size in the nether to 1/8th the size of the overworld. I had one of my friends die on my private server due to also being able to walk over the worldborder due to there being no visual clue, which is how this bug was brought to my attention in the first place.
Basically the problem afaik is that no matter what dimension you're in, the visuals of the worldborder seem to match those of the overworld, but the actual worldborder can be set per dimension individually, which means there can be a mismatch between the visuals and the actual deadly area. If the overworld has the smallest worldborder, it'll only be a minor issue. If you have it the other way round however (like I did until I learnt about this bug and will again if this bug gets fixed), players have no idea that they're past the worldborder and will start taking damage, seemingly for no reason.

### Comment 6: gaspoweredpick (2020-05-05T16:51:27.082-0700)

The problem here is that world borders break when edited outside the overworld. To work around this glitch, add "execute in minecraft:overworld run" before editing the world border. All worldborder commands will work properly when executed in the overworld, regardless of which dimension you're in.

### Comment 7: migrated (2020-05-06T18:19:17.317-0700)

@gaspoweredpick that fixes the visual glitch yes but also move the border in the overworld. We can change the worldborder per dimension but having the visualglitch (border not present), or have the visual ok but have a common worlderborder in every dimensions.

### Comment 8: migrated (2020-06-11T06:39:01.777-0700)

confirmed for 1.16-pre release 1,2 & 3

### Comment 9: migrated (2020-07-25T13:24:44.894-0700)

For custom dimensions I view this as a feature, not a bug. It gives me a way to limit the size of custom dimensions easily. Barrier blocks are useful, but are not able to be water logged, so this looks better. The nether being a tiny dimension but the same size has always been a problem. This "bug" can fix that.
Please don't fix this bug.
Side note, am I the only one that doesn't see the world border visually in custom dimensions? I like that as well, as seeing it would be distracting for small pocket dimensions for mini games and adventures. To me, this is also a feature, not a bug. We can use the warning part of the worldboarder command to warn a player. Perhaps adding a distance to how close you have to be to see it would be a better option.

### Comment 10: migrated (2020-08-05T18:46:50.981-0700)

I agree that this is useful, especially for custom dimensions. But they really need to fix it so it actually works as one would hope. I noticed that the border size resets in dimensions other than the Overworld when you relog, and it's somehow split into two distinct pieces:
The visible part, which mirrors the border in the Overworld and stops player movement as well as block placement.
And the invisible part, which can be altered by the /worldborder command, causes damage when you cross it, and also stops block placement.
The most dangerous part about this in my opinion is that a player could pass the invisible border without realizing, until they start taking damage and can't interact with blocks that is.

### Comment 11: chokoboy3 (2020-08-16T07:56:34.102-0700)

It seems that the issue is that while the server respects world borders in multiple dimensions, the client only recognizes the world border in the overworld even when in another dimension. This means that visually, the world border is always in the position that it is in in the overworld.
If the overworld has a larger world border than the dimension that you are in, you will start taking damage at random and blocks will reappear as you break them, as the server recognizes that you have moved outside the world border but the client allows you to move.
If the overworld has a smaller world border than the dimension that you are in, it just seems like the dimensions have the same world border since the client prevents you from going outside even though it should be entirely possible. If you teleport outside of the world border, you will not take damage in this situation.
Also, it seems that the world border is reset server-side in other dimensions after reopening the world

### Comment 12: migrated (2021-03-12T05:41:41.329-0800)

Affects 21w10a

### Comment 13: ampolive (2021-06-08T18:00:08.315-0700)

Potential code analysis in the duplicate MC-213713.

### Comment 14: migrated (2021-06-08T21:56:47.198-0700)

So, i'm not sure if this is related. My world border in the overworld, nether and end work, they are correct to the size i want it to be and the world border appears. However, the world border in my custom dimension, it works but does not have a visual appearance. Its completely invisible and the only way we notice we are going past the world border is the damage taken.

### Comment 15: migrated (2021-10-15T17:55:11.910-0700)

If you have a server with similar issues Spigot will solve them I tested it

### Comment 16: ampolive (2021-11-09T05:28:53.732-0800)

Can confirm in 21w44a.
