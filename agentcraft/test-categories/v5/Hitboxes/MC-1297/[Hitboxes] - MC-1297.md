# MC-1297: You can attack and be attacked through glass panes

**Mojira URL:** [https://bugs.mojang.com/browse/MC-1297](https://bugs.mojang.com/browse/MC-1297)

## Report details

- **Mojira categories:** Entities; Hitboxes
- **Project:** MC
- **Issue key:** MC-1297
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2012-10-30T03:44:39.233-0700
- **Updated:** 2025-05-29T09:20:57.733-0700
- **Resolution date:** 2024-08-17T17:27:48.742-0700
- **Affects versions:** Minecraft 1.4.2; Minecraft 1.4.7; Snapshot 13w06a; Minecraft 1.5; Snapshot 13w11a; Minecraft 1.5.1; Minecraft 1.5.2; Minecraft 1.6.2; Minecraft 1.6.4; Minecraft 13w39a; Minecraft 13w39b; Minecraft 1.7.9; Minecraft 14w25b; Minecraft 1.7.10; Minecraft 14w33c; Minecraft 14w34a; Minecraft 14w34b; Minecraft 14w34c; Minecraft 14w34d; Minecraft 1.8-pre1; Minecraft 1.8; Minecraft 1.8.1-pre3; Minecraft 1.8.8; Minecraft 15w39c; Minecraft 1.9.1; Minecraft 1.9.2; Minecraft 16w14a; Minecraft 1.10; Minecraft 1.10.1; Minecraft 1.10.2; Minecraft 16w32a; Minecraft 16w32b; Minecraft 16w33a; Minecraft 16w35a; Minecraft 16w40a; Minecraft 16w41a; Minecraft 16w44a; Minecraft 1.11 Pre-Release 1; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 1.12; Minecraft 1.13-pre6; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w43a; Minecraft 18w43b; 1.14.4; 19w45b; 1.15.2; 1.16 Pre-release 2; 1.16.1; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Release Candidate 1; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4 Pre-release 2; 1.16.4; 20w46a; 20w49a; 20w51a; 21w03a; 21w05a; 21w05b; 21w06a; 21w07a; 21w11a; 1.17; 1.17.1; 21w42a; 1.18.2; 1.19; 1.19.1 Pre-release 5; 1.19.1; 1.19.2; 22w43a; 1.19.3; 23w03a; 23w04a; 23w05a; 23w06a; 1.19.4; 1.20; 1.20.1; 23w32a; 23w33a
- **Fix versions:** 23w35a
- **Labels:** glass_pane
- **Watchers:** 2
- **Attachments:** 4
- **Attachment filenames:** 2013-11-22_05.06.18.png; 2013-11-22_05.13.50.png; MC-1297.mp4; MC-1297.png
- **Issue links:** Relates:outward:MC-3059:Projectiles can pass through thin surfaces | Relates:outward:MC-2310:Wrong attack radius calculation damages/kills entities through blocks and corners | Relates:inward:MC-264915:Some mobs can still attack you through blocks | Duplicate:inward:MC-231720:Bees can sting you through blocks | Duplicate:inward:MC-208286:Crossbow can hit behind the slim glass if player stands behind slim glass. | Duplicate:inward:MC-183640:Glass Paine glitch | Duplicate:inward:MC-164840:Spiders can be shot through glass panes | Duplicate:inward:MC-158126:Zombies can attack through glass panes | Duplicate:inward:MC-157274:Mobs attack through glass | Duplicate:inward:MC-151712:Players can be shot through glass panes when standing right in front of / next to glass panes. | Duplicate:inward:MC-140668:Piercing Arrow Bug | Duplicate:inward:MC-137639:Illager beast can hit through glass pane | Duplicate:inward:MC-136728:Phantoms attack and do damage through glass pane | Duplicate:inward:MC-96735:Bow Shooting | Duplicate:inward:MC-20235:Zombies Attacking through Glass Pane | Duplicate:inward:MC-108576:If a player is standing against a window pane and you were to shoot the other side of the pane you can shoot the player on the other side | Duplicate:inward:MC-106487:Spiders can beat through the glass panel. | Duplicate:inward:MC-89422:Attacking thorugh glass panes | Duplicate:inward:MC-12890:Mobs can be shot through glass panes when nesting or flying nearby. | Duplicate:inward:MC-58180:Spiders harm player through glass pane | Duplicate:inward:MC-19197:Zombies can hit through iron bars | Duplicate:inward:MC-18830:Shooting players through glass panes | Relates:inward:MCPE-65219:Villagers can be punched through walls by zombies

## Description

The Bug:
You can attack and be attacked through glass panes.
Steps to Reproduce:
- Summon a box with a glass pane wall by using the commands provided below.

```
/fill ~1 ~-1 ~1 ~11 ~3 ~5 minecraft:tinted_glass hollow
```

```
/fill ~2 ~ ~1 ~10 ~2 ~1 minecraft:glass_pane
```

- Summon a zombie inside of the box and break any block of glass pane that's at eye height, so that the zombie can be able to notice you.

- Switch into survival mode and get the zombie to notice you.

- When it does, move away from the hole in the glass pane, but remain standing as close as you can to adjacent glass pane blocks.

- Wait for the zombie to approach you.

- Take note as to whether or not you can attack and be attacked through glass panes.

Observed Behavior:
You can attack and be attacked through glass panes.
Expected Behavior:
You would not be able to attack or be attacked through glass panes.

## Comments (58)

### Comment 1: migrated (2012-10-30T03:44:39.233-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: migrated (2012-10-30T04:52:47.526-0700)

This happens to me too

### Comment 3: migrated (2012-10-30T06:57:34.556-0700)

Nice bug report. Don't worry about duplication across projects.

### Comment 4: migrated (2012-10-30T22:46:17.970-0700)

Thanks, this is my first bug report, so I was just hoping I'd done it right.

### Comment 5: migrated (2013-02-04T20:26:12.311-0800)

Changed it, confirmed for the latest release.

### Comment 6: migrated (2013-02-05T07:57:30.371-0800)

Unable to reproduce. Not even cave spiders are able to poison me through glass panes.

### Comment 7: migrated (2013-02-07T06:39:17.530-0800)

I can confirm it does work in the latest update. I made a cell with one wall made of glass panes. I removed a glass pane to bring the zombies I had spawned closer. after checking that they could hit me (I let one hit me) I replaced the glass pane. the wall was now solid, and walking right up to the glass pane made the zombie hit me again.

### Comment 8: bugi74 (2013-02-07T07:01:47.721-0800)

I managed to repeat with Paul Davis' latest example. But only if the zombie was lured to the glass pane wall (with a hole) first, and then the wall was closed. Zombies that were a bit away, or which were pushed a little bit on the other side, could not punch me; only a zombie that had gotten a hit on me before the wall was closed could continue punching me.
The zombies that could punch me through the pane were also sort of stuck in it; they could only move along the glass pane wall; e.g. when I moved to other side, they could not leave the glass wall to get to me. (EDIT: they could leave it eventually as I moved around; once the got unstuck, they couldn't punch me through the panes.)
This could perhaps indicate that the zombies are actually somehow inside that glass pane.

### Comment 9: migrated (2013-07-01T14:00:37.013-0700)

I am having the same issue in 1.6.1. To specify, I am on a pre-release server using the release client. (Because they did not add the updated server to minecraft.net) I am running windows 8 and it is survival. The server itself is Ubuntu Linux. Thanks!

### Comment 10: CubeTheThird (2013-09-25T19:26:31.166-0700)

Is this still a concern in the current Minecraft version 1.6.4 / Launcher version 1.2.5 ? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 11: migrated (2013-09-29T13:49:47.555-0700)

Doesn't seem to be an issue for me anymore, I haven't been playing as much though.

### Comment 12: CubeTheThird (2013-09-29T19:53:10.453-0700)

Seems to be fixed.

### Comment 13: bugi74 (2013-09-29T23:47:56.967-0700)

Nope, the bug is still there. Read my previous comment how to reproduce. (I use creative mode to first create a small "hut" from normal blocks and glass pane walls, leave one pane out, use some zombie eggs from outside, switch to creative, let zombie(s) to hit, add the missing glass pane, approach the wall again and zombie(s) keep hitting...
Also, zombies can hit villagers through doors (another thin vertical block) in some situations, or at least could in 1.6.2, haven't tested yet on 1.6.4 or checked if there already exist another issue for that; both issues may or may not have the same cause.

### Comment 14: CubeTheThird (2013-09-30T06:54:08.241-0700)

Reopening

### Comment 15: _zombiehunter (2013-09-30T06:58:03.388-0700)

Affects Versions: 1.6.4, .... can confirm this up to 13w39b !

### Comment 16: migrated (2013-11-21T20:10:13.883-0800)

1.7.2 is also affected
I actually believe this applies to any gamemode and all blocks,
its just easier to notice with blocks that can easely be destroyed
See both attachments where i hit someone behind a wall/glass, in a grief-protected spawn/area, while having creative mode:
Glass: http://i.imgur.com/BcndZzd.png
Wood: http://i.imgur.com/iqMgH98.png

### Comment 17: migrated (2014-05-18T10:43:46.370-0700)

Cannot reproduce in 1.7.9

### Comment 18: bugi74 (2014-05-18T10:53:51.670-0700)

Can reproduce still in 1.7.9, just follow the steps in earlier comments (i.e. open one pane, let a zombie hit, close the glass pane "wall" again fully... and the hitting zombie can still keep hitting through the glass wall).

### Comment 19: migrated (2016-03-16T23:26:54.967-0700)

There are a number of bug reports about attack radius that are all very similar. MC-2310, MC-18326, MC-50668, MC-63965, MC-71834, and MC-74907 are all about the attack radius of mobs extending through blocks. (Some mobs are more bugged then others, but it’s the same basic problem). There are also a few related issues:
 is the same as the above, but for players.
MC-3059 is the same as the above, but for arrows.
Most or all of these reports should be consolidated into one, as they are all caused by the same base issue.

### Comment 20: bugi74 (2016-03-17T00:09:43.379-0700)

KingSupernova, unless you have confirmed in the code that they have indeed the same root cause, do not assume they are one issue. Minecraft's code is made in many places in ways (e.g. duplication) that causes same or similar issues for multiple things, yet need different fixes. And history proves Mojang devs are not very capable of handling such cases if they are under the same ticket.
But certainly mark them all as related.
Also, a bit of semantics, maybe, but the problem is not attack radius, per se, but more likely a bug in how entities can end up sort of inside things and/or how their line-of-attack is calculated. That is, their movement algorithms can think an entity is on one side, but attack code thinks it is already on the other side. (Or something, that is just my educated assumption, but an assumption nonetheless.)

### Comment 21: migrated (2016-03-17T00:25:07.373-0700)

When I say they are the same base issue, I don't mean it's the same code. I just mean that they are all the same problem- In this case, mobs attacking things behind blocks.
I haven't looked at the code, I was just using "attack radius" as a clear way of describing the problem. To the naked eye, that is how the problem appears.

### Comment 22: FaRo1 (2016-06-10T13:52:40.948-0700)

Confirmed for 1.10.

### Comment 23: FaRo1 (2016-06-22T14:26:04.086-0700)

Confirmed for 1.10.1.

### Comment 24: marcono1234 (2017-02-21T07:03:53.635-0800)

Cannot confirm that you as a player are able to hit through glass panes in 17w06a (at least not when trying to hit other mobs). Zombies or other mobs being able to attack through them is MC-2310.

### Comment 25: bugi74 (2017-02-21T08:40:09.209-0800)

Did you try it using the trick of first removing removing one pane, moving against another, then replacing the removed pane (allowed at least mobs to get a bit closer)? (Described in earlier comments for zombies attacking player, but could possibly apply also for players; I didn't check players back then, since at that time this issue was only about mobs attacking players, at least according to description. For some reason, MC-2310 has a mention about this issue being for players.)
Also, a prime example of the dangers of too eagerly claiming issues as duplicates. In this case, if the player side is indeed fixed, apparently player (with e.g. bow) vs. mobs could be handled more or less differently (in the code), and thus should have kept their issues only as "related to".

### Comment 26: marcono1234 (2017-02-21T09:05:38.631-0800)

I did not look at the screenshots carefully enough. It looks like this report contains multiple bugs:
- One close to MC-2310

- One describing kind of the opposite of MC-73162
- this comment

- attached screenshots

I hope the code analysis for MC-2310 is correct, if not please correct me. Because you mentioned doors in an older comment as well I was pretty sure it is a duplicate. I am going to re-check this now.
Edit: After testing it, I still feel like this zombie glass pane part is MC-2310.

### Comment 27: bugi74 (2017-02-21T09:49:24.410-0800)

At least with the zombies attacking through glass pane, back then years ago, it was not only attack distance; when the zombies could not hit through the pane, the player could go as close as he wanted and be safe (if i remember it correctly).  But code may have changed since. Also, I probably never got to fully reverse engineer this case, so it is just educated guesses and speculation from me. (I probably did try to take a look at the code, though, but likely gave up after a while in this particular case.)
Considering the door case / MC-2310, your analysis at least sounds plausible; relying only on distance could explain a lot (except that ancient glass pane -case, but again, things could have changed since).
(For getting code analysis (or checks) from me nowadays:  I have given up on doing the MCP level debugging on these Minecraft issues as it takes like hours to days for a single reverse-engineering, and few hours for a fix, but then, years for Mojang to do absolutely nothing about it... when they could probably find and fix most of the issues I've been meddling with in half the time, with no reverse-engineering phase needed.  (There has been few exceptions, though, where Mojang has finally applied my fixes or at least gotten some benefit from the analysis. But too few fixes, way too rarely.)  That is, the benefits for me digging into the obfuscated code are nearly zero, yet needing substantial effort from me.)
Zombie glass panes could be part of MC-2310, but as long as it is not certain, I'd keep them only as "related to", to avoid the common end result of Mojang closing one issue (in one or another resolution), yet leaving multiple other bugs combined to the one actually unhandled. Being just related to, Mojang has to actually itself check whether they are fixed with the same change or not. (Or like it has happened, they don't necessarily even look at the related issue, leaving it unfixed for more years, but in that case, the other issue is at least still open as it should be until properly resolved.)

### Comment 28: muzikbike (2018-07-06T05:25:49.115-0700)

Affects 1.13-pre6
Actually, said test was performed by throwing a snowball at a glass pane from a distance with a mob behind it; would that be considered a different issue?

### Comment 29: migrated (2018-08-24T14:16:35.247-0700)

I couldn't reproduce this for 1.13.1.
Second opinion?

### Comment 30: FaRo1 (2018-11-07T23:31:02.218-0800)

Does that happen because it moves its head forwards maybe? Can you reproduce with other mobs? Is the radius higher for the beast?

### Comment 31: migrated (2018-11-12T04:52:32.422-0800)

Have no idea about the head movement, radius does seem to be higher for the beast, And I can reproduce with other mobs too.

### Comment 32: TheBoy358 (2019-11-08T07:16:11.825-0800)

Confirmed in 1.14.4 and 19w45b.

### Comment 33: TheBoy358 (2019-11-08T07:16:13.652-0800)

Confirmed in 1.14.4 and 19w45a.

### Comment 34: migrated (2020-05-24T14:05:28.427-0700)

Confirmed in 1.16 20w20b.  A phantom was able to attack me through a wall of glass panes.

### Comment 35: migrated (2020-06-08T09:18:14.132-0700)

Confirmed in 1.16-pre2.

### Comment 36: migrated (2020-06-29T16:09:38.382-0700)

Confirmed in 1.16.1

### Comment 37: Avoma (2021-01-11T11:48:41.149-0800)

Can confirm in 20w51a.

### Comment 38: Avoma (2021-01-22T02:50:36.479-0800)

Can confirm in 21w03a.

### Comment 39: Avoma (2021-02-03T11:09:05.119-0800)

Can confirm in 21w05a.

### Comment 40: Avoma (2021-02-04T10:26:20.337-0800)

Can confirm in 21w05b.

### Comment 41: Avoma (2021-02-12T04:58:10.162-0800)

Can confirm in 21w06a.

### Comment 42: Avoma (2021-02-18T10:35:07.192-0800)

Can confirm in 21w07a.

### Comment 43: Avoma (2021-03-18T02:50:36.719-0700)

Can confirm in 21w11a.

### Comment 44: Avoma (2021-06-22T04:16:20.480-0700)

Can confirm in 1.17.

### Comment 45: Avoma (2022-03-02T06:00:04.461-0800)

Can confirm in 1.18.2.

### Comment 46: Avoma (2022-06-24T05:17:28.193-0700)

Can confirm in 1.19. I'd be happy to take ownership of this ticket and keep it updated since the reporter is no longer active.

### Comment 47: NBG-bootmgr (2022-07-20T03:51:28.235-0700)

in 1.19.1 pre5

### Comment 48: migrated (2022-07-22T16:42:50.290-0700)

this is because you can walk so close to the glass panes that your hitbox passes through the glass pane. making you hittable through  the panes

### Comment 49: bugi74 (2022-07-23T01:14:34.394-0700)

@Hubbi GamingTV, slightly incorrect: as described in earlier comments, at least in earlier versions (I have not checked the bug lately), in certain situations one could go as close to the pane as possible without getting hit by zombies.  If it was simply due to hitbox getting through the pane, zombies would have been able hit through the pane in all situations (where the player was close enough).

### Comment 50: Brain81505 (2023-01-18T08:14:27.623-0800)

Can confirm in 23w03a

### Comment 51: Brain81505 (2023-01-24T23:23:18.694-0800)

Can confirm in 23w04a

### Comment 52: Brain81505 (2023-02-01T08:05:02.417-0800)

Can confirm in 23w05a

### Comment 53: Brain81505 (2023-02-11T07:31:59.504-0800)

Can confirm in 23w06a

### Comment 54: AMGAMES04 (2023-08-16T05:31:46.273-0700)

Can confirm in 23w32a

### Comment 55: syarumi (2023-08-30T09:43:01.509-0700)

It's safe to assume this has been fixed in 23w35a due to the fixes for MC-2310 & MC-264915, at least for mobs. There's still the other minor issue that is already stated in the title, which is players being able to attack through panes/blocks, but that one could be considered a completely different issue.
In certain protected areas, such as the spawn protection in servers, the player can attack other entities through blocks, because when the player breaks a block client-side, the gap remains for a few milliseconds until it regenerates, giving the player the opportunity to strike the entity behind, as can be seen in these screenshots:

However, i haven't tested this so i don't know if it's still the case in 1.20.1. If it is, the report should probably be centered around that, or either be covered in a new report.

### Comment 56: bugi74 (2023-08-30T11:14:55.082-0700)

It is almost never "safe to assume", but...
It seems that the attack and pathing behaviors of zombies (and maybe spiders, too) have changed since I last tested this (i.e. very long time ago), too.. I could not reproduce with the old test method, not even to the point of zombies getting as close to glass panes as before (they don't "hug the pane" now, but stay about at the center of the full free block outside). And could not get them to even to try to attack as soon as there was glass in between. So whatever has changed (in addition to those other two issues), a proper fix or not, has apparently made them unable/unwilling to attack through at least glass panes (in normal situations).
Spiders could get closer the glass pane (as they climb it), but no attacks through the pane.
I tried with only 3 zombies simultaneously, so they didn't push each other much towards the pane, as they all tried to get to the center of the same block, not straight towards the player    Perhaps with a bigger horde, some could get pushed against the pane, close enough, but that would then probably be more about the problem of containing too many mobs in too little space.
... Or need new/better reproduction steps to catch the remaining situations, if any left.

### Comment 57: syarumi (2023-08-30T12:07:36.072-0700)

Yeah, what I meant by my comment was that i tested most of the mobs trying to attack through panes, even trapdoors and I wasn't able to reproduce this issue anymore.

### Comment 58: Avoma (2023-10-18T05:53:35.406-0700)

I tested this issue myself and it has indeed been fixed in 23w35a, so I've marked this ticket as fixed. Thank you!
