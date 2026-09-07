# MC-51053: Furnace minecarts lose power after navigating corners

**Mojira URL:** [https://bugs.mojang.com/browse/MC-51053](https://bugs.mojang.com/browse/MC-51053)

## Report details

- **Mojira categories:** Minecart
- **Project:** MC
- **Issue key:** MC-51053
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2014-03-13T08:52:19.738-0700
- **Updated:** 2025-04-26T03:25:06.189-0700
- **Resolution date:** 2024-08-23T06:13:32.637-0700
- **Affects versions:** Minecraft 14w11a; Minecraft 14w11b; Minecraft 14w20b; Minecraft 14w31a; Minecraft 14w34b; Minecraft 1.8; Minecraft 1.8.1; Minecraft 1.8.3; Minecraft 1.8.7; Minecraft 1.8.8; Minecraft 15w31c; Minecraft 15w36b; Minecraft 15w36c; Minecraft 15w36d; Minecraft 15w37a; Minecraft 15w38a; Minecraft 15w39b; Minecraft 15w39c; Minecraft 15w40a; Minecraft 15w40b; Minecraft 15w41b; Minecraft 15w42a; Minecraft 15w43b; Minecraft 15w43c; Minecraft 15w44a; Minecraft 15w44b; Minecraft 15w45a; Minecraft 15w46a; Minecraft 15w47a; Minecraft 15w47b; Minecraft 15w47c; Minecraft 15w49a; Minecraft 15w49b; Minecraft 1.8.9; Minecraft 15w50a; Minecraft 15w51b; Minecraft 16w02a; Minecraft 16w03a; Minecraft 16w04a; Minecraft 16w05a; Minecraft 16w05b; Minecraft 16w06a; Minecraft 1.9; Minecraft 1.9.2; Minecraft 16w15a; Minecraft 16w15b; Minecraft 1.9.4; Minecraft 1.10; Minecraft 1.10.2; Minecraft 16w39a; Minecraft 16w39b; Minecraft 16w40a; Minecraft 16w41a; Minecraft 16w42a; Minecraft 16w43a; Minecraft 16w44a; Minecraft 1.11 Pre-Release 1; Minecraft 1.11; Minecraft 16w50a; Minecraft 1.11.1; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 17w13a; Minecraft 17w13b; Minecraft 17w14a; Minecraft 17w15a; Minecraft 17w16a; Minecraft 17w17a; Minecraft 17w17b; Minecraft 17w18a; Minecraft 17w18b; Minecraft 1.12 Pre-Release 1; Minecraft 1.12 Pre-Release 2; Minecraft 1.12 Pre-Release 3; Minecraft 1.12 Pre-Release 4; Minecraft 1.12 Pre-Release 5; Minecraft 1.12 Pre-Release 6; Minecraft 1.12 Pre-Release 7; Minecraft 1.12; Minecraft 17w31a; Minecraft 1.12.1 Pre-Release 1; Minecraft 1.12.1; Minecraft 1.12.2 Pre-Release 1; Minecraft 1.12.2 Pre-Release 2; Minecraft 1.12.2; Minecraft 17w43a; Minecraft 17w43b; Minecraft 17w45a; Minecraft 17w45b; Minecraft 17w46a; Minecraft 17w47a; Minecraft 17w47b; Minecraft 17w48a; Minecraft 17w50a; Minecraft 18w01a; Minecraft 18w03b; Minecraft 18w06a; Minecraft 18w09a; Minecraft 18w10d; Minecraft 18w14b; Minecraft 18w19a; Minecraft 1.13-pre1; Minecraft 1.13-pre3; Minecraft 1.13-pre4; Minecraft 1.13-pre6; Minecraft 1.13-pre7; Minecraft 1.13-pre9; Minecraft 1.13-pre10; Minecraft 1.13; Minecraft 18w30b; Minecraft 18w31a; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w48b; Minecraft 19w04b; Minecraft 19w12b; Minecraft 19w13b; Minecraft 1.14 Pre-Release 4; 1.14.4; 19w42a; 19w46a; 1.15 Pre-release 1; 1.15 Pre-Release 2; 1.15 Pre-release 3; 1.15 Pre-release 4; 1.15 Pre-release 5; 1.15 Pre-release 6
- **Fix versions:** 1.15.2 Pre-Release 1
- **Labels:** furnace_minecart; movement; rails
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** 2014-03-13_15.50.10.png; 2014-08-18_22.06.59.png; 2014-08-18_22.11.36.png; 2016-11-17_21.16.43.png; 2016-11-17_21.18.42.png; 2016-11-17_21.18.49.png
- **Issue links:** Relates:inward:MC-28222:Hopper minecarts glitch when pushed along a curve by a furnace minecart | Relates:inward:MC-275347:Minecart with Furnace does not travel correctly over curves | Relates:outward:MC-158363:Minecarts are failing to navigate corners if dragged along by a furnace minecart | Relates:inward:MC-100878:Minecart experiences 'friction' around corners | Relates:inward:MC-88038:Furnace minecart go backwards when throught the corner | Duplicate:inward:MC-162947:Furnace Minecarts Slow Down and Pause After Corners | Duplicate:inward:MC-131541:Using coal on furnace minecart doesn't make it keep moving | Duplicate:inward:MC-125151:Minecart with furnace stops even though it has power | Duplicate:inward:MC-53992:furnace carts do not stay powered | Duplicate:inward:MC-106976:Minecart Furnance losing fuel after L shape curve | Duplicate:inward:MC-99720:Minecarts trains and curves don't go well together | Duplicate:inward:MC-93428:Furnace carts slow to a stop while still fuelled | Duplicate:inward:MC-74753:Minecart with furnce bugs on corners | Duplicate:inward:MC-56145:Furnace minecart only being powered for a brief second | Duplicate:inward:MC-84936:furnace minecart does not work | Duplicate:inward:MC-84884:Furnace Minecarts | Duplicate:inward:MC-84693:Minecarts with Furnace! | Duplicate:inward:MC-76832:furnace in a minecart not working | Duplicate:inward:MC-74874:powered mine carts stop working after driving over curved rails | Duplicate:inward:MC-68425:Powered (furnace) minecart stops after curve | Duplicate:inward:MC-51257:The Minecart with Furnaces aren't working correctly | Duplicate:inward:MC-51103:Furnace Minecarts are glitchy

## Description

The bug
Furnace Minecarts lose power after navigating corners.
How to reproduce
- In creative mode, create a long straight section of track, with a shorter section at one end creating an L-shape

- Place a furnace minecart on the shorter section just before the corner

- Right click on the powered minecart with charcoal, while looking forwards but against the curve
→ After rounding the corner, the furnace minecart will roll to a stop 10 blocks along the track as though it was unpowered

Proposed fix
Provided by  in the comments: https://bugs.mojang.com/browse/MC-51053?focusedCommentId=223854&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-223854
Workaround
If the minecart is right-clicked again after it has stopped while you are facing in the correct direction, it will start moving again. Additional fuel doesn't need to be provided – just clicking it fixes the direction and will cause the old fuel to be used properly.

## Comments (88)

### Comment 1: migrated (2014-03-13T08:52:19.738-0700)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: migrated (2014-03-13T10:01:04.625-0700)

May or may not be intentional, this certainly seems strange however.

### Comment 3: ChaofanJ (2014-04-08T19:38:58.294-0700)

Confirmed. also Minecart with Furnace is way too slow and does not push other Minecarts correctly.

### Comment 4: migrated (2014-04-24T15:59:31.145-0700)

This problem exists in the most recent snapshot (14w17a) as well.

### Comment 5: migrated (2014-05-22T20:11:19.733-0700)

Also seeing it in 14w21b

### Comment 6: migrated (2014-06-23T20:10:20.612-0700)

I can confirm that this is also happening on 14w25b, and not just corners. It seems to loose power almost anywhere and disconnects with the carts its pulling right when it hits a curve.

### Comment 7: migrated (2014-07-31T15:37:11.755-0700)

Confirmed for 14w31a

### Comment 8: migrated (2014-08-18T19:27:40.925-0700)

Confirmed for 14w34b
There are still problems with how powered minecarts go around corners. If there are two corners, the powered minecart will go about 8-10 blocks then stop. Sometimes they keep going, and rarely they bounce back an go the wrong way before stopping.
Also, powered minecarts no longer push minecarts with chests when both are adjacent and started from a dead stop.
I'll attach some screenshots of the experiments I made. At first I thought the distance between corners made a difference, but after looking at the results I'm not sure.

### Comment 9: migrated (2014-08-26T10:24:36.832-0700)

Haven't you seen any problems when the furnace minecart is running on a straight track? That is what happens to me.
Version 1.8-pre2

### Comment 10: migrated (2014-08-26T10:28:06.798-0700)

There are also other reports marked as duplicate of this, but they don't mention corners.
MC-51103

### Comment 11: migrated (2014-09-02T08:03:03.939-0700)

Confirmed for 1.8 Release.
Powered minecarts seem to work on straight lines now, but after they hit a curve they will stop moving a few blocks away.

### Comment 12: migrated (2014-09-15T15:02:35.661-0700)

Confirmed 1.8/Linux

### Comment 13: migrated (2014-12-02T03:09:41.617-0800)

also happens occasionally on detector rails

### Comment 14: migrated (2014-12-22T09:17:58.887-0800)

An explanation of why this happens:
When a player right-clicks the furnace cart, it is given a push vector based on where the player is stood relative to the cart. In versions prior to 1.8, this vector would be updated every gametick to face in the direction that the minecart is moving - however in 1.8, the push vector is stuck in the direction that the player initially set it to.
If the angle between the push and motion vectors is over 90 degrees (i.e. scalar product is negative), the push vector is set to 0 and the cart will come to a halt.
For example, if you are facing South-West when you right-click the cart, it won't lose power on tracks which take it South or West, and there can be many corners alternating between those two directions.

### Comment 15: migrated (2015-01-13T22:25:43.487-0800)

So.. Can't anyone fix this? Its been quite awhile and as far as I can see, it just kills furnace powered mine carts.

### Comment 16: migrated (2015-01-20T12:50:27.061-0800)

Is it possible to have this issue reviewed? As jim lee said, it kills powered minecarts and makes them useless in the game.

### Comment 17: migrated (2015-01-20T17:10:43.829-0800)

There are thousands of unresolved bugs, Mojang will get to this one eventually. If they go ahead and add in the new minecart mechanics that they had in 14w11a, I'm sure this will be fixed then.

### Comment 18: migrated (2015-01-20T19:44:05.124-0800)

Issac, those "minecart mechanics" (a.k.a Jeb's Minecart Law) were removed by popular demand by the community, so as long as those mechanics stay removed, this is most likely unfixable.

### Comment 19: migrated (2015-01-20T19:58:46.371-0800)

Oh, they were? I didn't realise. That doesn't make this unfixable though, I was just saying that if they ever did something with minecarts, they would probably get to this too, as it also affects minecarts.

### Comment 20: migrated (2015-01-20T23:45:55.801-0800)

What? Powered mine carts were deleted by popular demand?!

### Comment 21: migrated (2015-01-21T09:09:04.060-0800)

@Sonic: this bug is currently making powered minecarts unusable, i would say that this should be high priority...
As for being unfixable, they said that they would "revert" minicarft mechanics, and they did so but they forgot to "revert" ( aka. fix) powered minecarts too

### Comment 22: migrated (2015-02-23T19:43:50.505-0800)

Is no one trying to use Furnace powered mine carts anymore? I have an entire world going back to using horses 'cause the rail system that connects everything won't run anymore.
Is there any way to get this looked at?
thanks!

### Comment 23: migrated (2015-02-23T23:51:07.592-0800)

@jim lee
There are over 3000 unresolved bugs, many of which have been around much longer than this one. Just wait. This will be looked at eventually.

### Comment 24: migrated (2015-03-09T20:36:49.498-0700)

Wait?! Its been a YEAR!
-jim lee

### Comment 25: migrated (2015-03-17T12:59:21.309-0700)

Confirmed and still existing in 1.8.3

### Comment 26: migrated (2015-04-06T10:54:40.583-0700)

```--- src/main/java/net/minecraft/server/EntityMinecartFurnace.java	2015-04-06 18:50:46.198347410 +0100
+++ src/main/java/net/minecraft/server/EntityMinecartFurnace.java	2015-04-06 18:50:46.214347410 +0100
@@ -58,17 +58,9 @@

         if (d0 > 1.0E-4D && this.motX * this.motX + this.motZ * this.motZ > 0.001D) {
             d0 = (double) MathHelper.sqrt(d0);
-            this.a /= d0;
-            this.b /= d0;
-            if (this.a * this.motX + this.b * this.motZ < 0.0D) {
-                this.a = 0.0D;
-                this.b = 0.0D;
-            } else {
-                double d1 = d0 / this.m();
-
-                this.a *= d1;
-                this.b *= d1;
-            }
+            double d1 = (double) MathHelper.sqrt(this.motX * this.motX + this.motZ * this.motZ);
+            this.a = (motX / d1) * d0;
+            this.b = (motZ / d1) * d0;
         }

     }```
Full source here: https://gist.github.com/thinkofname/1435c96a8d7efcd2698e
From my testing this seems to completely fix the issue although it might need some more testing

### Comment 27: migrated (2015-04-13T11:49:08.902-0700)

I've made an observation, which thus far has been consistent.
When the Furnace Minecart takes the turn, the orientation of the cart and/or furnace reverses.
1st example:
Cart is rolling with fire to the rear.
Cart transitions turn and fire remains to the rear, the cart continues rolling unabated.
2nd example (converse):
Cart is rolling with fire to the rear.
Cart transitions turn and the fire side flips to the frontward end, the cart stops rolling.
This holds true regardless to directional orientation of the cart (fire to the front side or to the trailing end of forward motion).
So long as the cart/furnace facing remains consistent through and after the turn, the cart continues rolling.
If it reverses, it stops.
There seems to be no rhyme or reason to when it happens. I've witnessed several consecutive turns where the flip did not occur.
I hope this helps. I look forward to the resolve.
Standing at the station waiting for a train that never comes.
Thinkofdeath, how does one apply the script you have posted, and does it address the issue as I have it described?

### Comment 28: migrated (2015-04-13T14:10:47.182-0700)

Should do, don't have it applied to test. The patch itself was applied against Spigot (Minecraft server mod) on the partially de-obfuscated source. Wouldn't recommend trying to apply it yourself unless you understand how to work with the mod, I just included it to show roughly to mojang were I fixed it.

### Comment 29: migrated (2015-07-14T22:23:08.018-0700)

Confirmed 1.8.7/Mac. Definitely looks like the push vector is stuck as described by .
Observations with a 12x12 loop of track:
- furnace cart started at southwest corner while facing northeast comes to rest at northwest corner (about 10 blocks from northeast corner where its motion vector presumably gets set to 0)

- furnace cart started at southwest corner while facing southeast comes to rest at northeast corner (about 10 blocks from southeast corner where its motion vector presumably gets set to 0)

### Comment 30: marcono1234 (2015-09-04T03:06:21.954-0700)

Relates to:
- MC-53992

- MC-88038

Confirmed for
- 15w36c The problem seems to be with PushX and PushZ. These are the as you called them vectors that determine the Motion of a MinecartFurnace (see comment on MC-88038). However these values are most of the time set to 0 when a MinecartFurnace navigates through a corner. This normally only happens when Fuel is 0, however for corners it does not matter.

### Comment 31: migrated (2015-09-08T11:07:01.989-0700)

The solution has already been fixed by ThinkofDeath just Mojang still has refused to implement it.. I mean unless we trying to get quasi-real physics working, the velocity should never go to zero on a turn regardless it should change the thrust vector to the new direction of travel.  It is a powered minecart with a fixed force of thrust.  This isnt a simulator so dont see why implementing code that fixes the problem still has not been implemented.

### Comment 32: migrated (2015-09-11T12:43:35.164-0700)

still an issue 15w37a and 15w38a

### Comment 33: migrated (2015-09-12T08:14:48.830-0700)

I'm currently trying to fix up the furnace minecart for my mod Vintagecraft - I can confirm from simple tests that Thinkofdeaths solution fixes the problem of coal powered carts slowing down after going through a curve.
In that regard, thanks for the fix Thinkofdeath!

### Comment 34: marcono1234 (2015-09-14T02:16:59.204-0700)

Mods could you please add the suggested fix to the description?

### Comment 35: migrated (2015-09-14T09:56:52.495-0700)

it is not a suggested fix unless you know what you doing because obfuscation changes in every version release..  best bet is use the 3rd party server or get alot of people to start upvoting this issue so they might finally implement it.   if MCP was kept up to date then this would be possible but since it hasnt been updated since 1.8 it would not be recommended.

### Comment 36: migrated (2015-09-21T14:50:33.883-0700)

still an issue 15w39a
... and 15w39b
... and 15w39c

### Comment 37: migrated (2015-09-30T09:32:45.824-0700)

still an issue 15w40a
... and 15w40b

### Comment 38: migrated (2015-10-07T08:21:00.711-0700)

Still an issue in 15w41b

### Comment 39: migrated (2015-10-14T07:08:37.383-0700)

Still an issue in 15w42a

### Comment 40: migrated (2015-10-22T12:02:05.640-0700)

Still an issue in 15w43b

### Comment 41: migrated (2015-10-23T08:52:13.797-0700)

Still an issue in 15w43c

### Comment 42: migrated (2015-10-28T15:20:49.106-0700)

Still an issue in 15w44a

### Comment 43: migrated (2015-10-30T05:59:23.420-0700)

Still an issue in 15w44b

### Comment 44: migrated (2015-11-05T06:36:07.535-0800)

Still an issue in 15w45a

### Comment 45: migrated (2015-11-12T08:08:53.292-0800)

Still an issue in 15w46a

### Comment 46: migrated (2015-11-18T08:25:10.957-0800)

please repair this feature @Mojang! Very important for mechanism: http://minecraft-de.gamepedia.com/Schienenverkehrsanlagen
still an issue in 15w47a

### Comment 47: migrated (2015-11-18T17:18:49.818-0800)

Mojang please check this video: https://www.youtube.com/watch?v=YVGFJRwSe2A.
Problem 2 shows the bug.  Problem 3 is the actual trick that players can workaround this bug today.
Problem 2 also does not occurs in 1.7.10 version.

### Comment 48: migrated (2015-11-18T18:29:36.569-0800)

or they could just have implemented the code that fixed the problem provided by one of 3rd party server devs which in fact was implemented and been fixed in said 3rd party server for over half a year now.

### Comment 49: migrated (2015-11-19T08:35:18.662-0800)

still an issue in 15w47b

### Comment 50: migrated (2015-11-20T09:59:16.243-0800)

still an issue in 15w47c

### Comment 51: migrated (2015-12-02T08:42:31.273-0800)

Still an issue in 15w49a

### Comment 52: migrated (2015-12-03T14:39:18.473-0800)

Still an issue in 15w49b

### Comment 53: migrated (2015-12-06T09:27:01.327-0800)

In my Opinion it would be really useful if powered minecarts were given a menue with a coal slot and buttons to define the direction of driving.
And its currently still being an issue in Minecraft 1.8.8

### Comment 54: migrated (2015-12-09T11:34:41.109-0800)

Still an issue in 15w50a and 1.8.9

### Comment 55: migrated (2015-12-17T10:49:08.047-0800)

still an issue in 15w51b

### Comment 56: migrated (2016-01-13T08:15:51.964-0800)

still an issue in 16w02a

### Comment 57: migrated (2016-01-20T08:10:25.407-0800)

still an issue in 16w03a

### Comment 58: migrated (2016-01-22T15:39:10.296-0800)

Console edition also has the same bug (after TU31)
https://bugs.mojang.com/browse/MCCE-1599

### Comment 59: migrated (2016-02-10T13:10:05.617-0800)

still an issue in 16w06a

### Comment 60: marcono1234 (2016-02-15T08:13:52.642-0800)

Please link to 's comment as his github page does not exist anymore

### Comment 61: migrated (2016-02-15T08:24:17.890-0800)

Jeb's opinion about the issue: https://twitter.com/jeb_/status/699241247391772672
"I think we will phase out the furnace minecraft"
Bad news for us, maybe. It needs being reworked, not removed!

### Comment 62: migrated (2016-02-15T08:44:37.866-0800)

Well, crap. That's one way to fix all the furnace minecart mechanics bugs, I guess. =/

### Comment 63: migrated (2016-02-15T14:34:51.913-0800)

Phase out the furnace?
They should at least make the power rails more cheap

### Comment 64: migrated (2016-03-03T15:22:01.011-0800)

MCCE-1599 was marked as "Works As Intended". Should this issue also be marked as "Works As Intended"?
PS: still an issue in 1.9

### Comment 65: kumasasa (2016-03-03T23:05:25.497-0800)

Funny. But most probably that's now WaI. But Furnace Minecarts will be removed from the game.

### Comment 66: migrated (2016-03-13T13:43:36.016-0700)

Will there be something created to replace them?

### Comment 67: migrated (2016-04-11T11:22:39.670-0700)

This isn't a descussion forum, that's why there is minecraft forum. Also yes this has been confirmed in 1.9.2 and 1.9.1

### Comment 68: migrated (2016-04-14T14:11:24.543-0700)

Confirmed in 16w15b

### Comment 69: migrated (2016-05-10T11:17:00.395-0700)

Still happens in 1.9.4

### Comment 70: migrated (2016-06-11T12:31:30.969-0700)

Confirmed in 1.10

### Comment 71: migrated (2016-11-17T18:21:39.398-0800)

I confirmed that this is still a bug in 1.11. Attached new screenshots

### Comment 72: migrated (2018-06-28T02:48:45.802-0700)

Affects 1.13-pre4

### Comment 73: migrated (2018-07-10T10:03:59.764-0700)

Affects 1.13-pre7

### Comment 74: migrated (2018-08-06T19:12:59.627-0700)

Affects 18w31a

### Comment 75: migrated (2018-12-01T06:21:08.633-0800)

Still an issue in snapshot 18w48b.
Please can this be fixed soon, it's been an issue since 1.8 which puts me off using the newer versions since furnace carts were one of my favorite items in the game.

### Comment 76: Makzevu (2019-03-29T13:46:56.504-0700)

Confirmed for 19w13b.

### Comment 77: Makzevu (2019-04-17T16:22:02.887-0700)

Confirmed for 1.14 Pre-Release 4.

### Comment 78: migrated (2019-04-18T00:20:35.747-0700)

If Dinnerbone or Mojang indeed plans to remove furnace minecarts, I suggest just marking this issue as "wontfix" instead of letting a ton of people waiting for this issue be fixed one day.

### Comment 79: [Mod] violine1101 (2019-04-18T03:46:05.794-0700)

Nobody at Mojang ever confirmed that furnace minecarts will be removed for sure, they only thought about it, but no decision has been taken as far as I know. Nevertheless, even if the furnace minecart was to be removed from the game, it still is part of the game until it is actually removed.

### Comment 80: migrated (2019-08-29T19:29:09.378-0700)

Confirmed for 1.14.4, still not fixed.

### Comment 81: migrated (2019-10-21T20:49:12.504-0700)

Still an issue on 19w42a, I'm practically begging you at this point to fix this since it has been an issue for nearly five years and I literally stopped playing vanilla minecraft versions because of this as furnace carts were my favourite item.

Please, if you have no intention on fixing this just do what liach said and save me, plus others, the pain by marking it as wontfix because at the moment I still have my hopes up that this will one day be fixed.

### Comment 82: migrated (2019-11-13T22:00:33.811-0800)

Confirmed in 19w46a. Also thanks for adding a mojang priority.

### Comment 83: migrated (2019-11-21T18:58:49.460-0800)

Affects 1.15 pre release 1.

### Comment 84: migrated (2019-11-25T11:08:33.665-0800)

Affects 1.15 pre release 2.

### Comment 85: migrated (2019-11-28T11:13:20.005-0800)

Affects 1.15 pre release 3

### Comment 86: migrated (2019-12-03T18:07:34.572-0800)

Affects 1.15 pre release 4

### Comment 87: migrated (2019-12-05T10:02:17.024-0800)

Affects 1.15 pre release 5

### Comment 88: migrated (2020-01-09T00:12:46.256-0800)

please, oh please, fix this one!
