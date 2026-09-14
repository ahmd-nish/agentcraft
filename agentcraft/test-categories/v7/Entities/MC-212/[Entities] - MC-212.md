# MC-212: Fall damage is ignored for a couple of seconds when reloading into LAN or singleplayer worlds

**Mojira URL:** [https://bugs.mojang.com/browse/MC-212](https://bugs.mojang.com/browse/MC-212)

## Report details

- **Mojira categories:** Entities
- **Project:** MC
- **Issue key:** MC-212
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2012-10-24T14:27:49.393-0700
- **Updated:** 2025-05-29T09:20:56.860-0700
- **Resolution date:** 2024-12-13T06:33:58.170-0800
- **Affects versions:** Minecraft 1.4.2; Minecraft 1.5.1; Minecraft 1.5.2; Snapshot 13w26a; Minecraft 1.6; Minecraft 1.6.1; Minecraft 1.6.2; Minecraft 1.6.4; Minecraft 13w39b; Minecraft 13w41a; Minecraft 13w41b; Minecraft 13w42a; Minecraft 13w42b; Minecraft 1.7.4; Minecraft 14w02a; Minecraft 14w02b; Minecraft 14w05b; Minecraft 14w06b; Minecraft 14w07a; Minecraft 14w08a; Minecraft 14w10c; Minecraft 1.7.9; Minecraft 14w21b; Minecraft 14w25a; Minecraft 14w25b; Minecraft 14w26c; Minecraft 1.7.10; Minecraft 14w27a; Minecraft 14w27b; Minecraft 14w28b; Minecraft 14w29a; Minecraft 14w29b; Minecraft 14w30a; Minecraft 14w30b; Minecraft 14w30c; Minecraft 14w32a; Minecraft 14w32b; Minecraft 14w32c; Minecraft 14w32d; Minecraft 14w33a; Minecraft 14w33b; Minecraft 14w33c; Minecraft 14w34a; Minecraft 14w34b; Minecraft 14w34c; Minecraft 14w34d; Minecraft 1.8-pre1; Minecraft 1.8-pre2; Minecraft 1.8-pre3; Minecraft 1.8; Minecraft 1.8.1-pre2; Minecraft 1.8.1-pre3; Minecraft 1.8.1; Minecraft 1.8.2-pre1; Minecraft 1.8.2-pre4; Minecraft 1.8.8; Minecraft 15w31a; Minecraft 15w38a; Minecraft 15w43b; Minecraft 15w44a; Minecraft 15w44b; Minecraft 15w45a; Minecraft 15w46a; Minecraft 15w47a; Minecraft 15w47b; Minecraft 15w49a; Minecraft 15w49b; Minecraft 1.8.9; Minecraft 15w50a; Minecraft 15w51a; Minecraft 15w51b; Minecraft 16w02a; Minecraft 16w03a; Minecraft 16w04a; Minecraft 16w05b; Minecraft 16w06a; Minecraft 16w07a; Minecraft 16w07b; Minecraft 1.9 Pre-Release 1; Minecraft 1.9 Pre-Release 4; Minecraft 1.9; Minecraft 1.9.1 Pre-Release 1; Minecraft 1.9.1 Pre-Release 2; Minecraft 1.9.1 Pre-Release 3; Minecraft 1.9.1; Minecraft 1.9.2; Minecraft 16w14a; Minecraft 1.9.4; Minecraft 1.10; Minecraft 1.10.1; Minecraft 1.10.2; Minecraft 16w32a; Minecraft 16w32b; Minecraft 16w33a; Minecraft 16w35a; Minecraft 16w36a; Minecraft 16w38a; Minecraft 16w39c; Minecraft 16w40a; Minecraft 16w41a; Minecraft 16w42a; Minecraft 16w43a; Minecraft 16w44a; Minecraft 1.11 Pre-Release 1; Minecraft 1.11; Minecraft 16w50a; Minecraft 1.11.1; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 17w13a; Minecraft 17w13b; Minecraft 17w16b; Minecraft 17w17b; Minecraft 1.12; Minecraft 1.12.1; Minecraft 1.12.2; Minecraft 17w45b; Minecraft 17w46a; Minecraft 18w08a; Minecraft 18w11a; Minecraft 18w14a; Minecraft 18w14b; Minecraft 18w16a; Minecraft 18w22a; Minecraft 1.13-pre1; Minecraft 1.13-pre2; Minecraft 1.13-pre8; Minecraft 1.13.1; Minecraft 1.13.2-pre2; Minecraft 1.13.2; Minecraft 18w43b; Minecraft 18w43c; Minecraft 18w44a; Minecraft 19w03c; Minecraft 19w04b; Minecraft 19w12b; Minecraft 19w13b; Minecraft 19w14a; Minecraft 19w14b; Minecraft 1.14 Pre-Release 2; Minecraft 1.14 Pre-Release 3; Minecraft 1.14 Pre-Release 4; Minecraft 1.14 Pre-Release 5; Minecraft 1.14.2; 1.14.4; 1.15 Pre-release 4; 1.15.1; 1.15.2 Pre-release 2; 1.15.2; 20w15a; 20w16a; 20w21a; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 4; 1.16 Pre-release 5; 1.16 Pre-release 6; 1.16 Pre-release 7; 1.16.1; 20w27a; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Pre-release 2; 1.16.2 Release Candidate 1; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4 Pre-release 2; 1.16.4; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w08b; 21w11a; 21w14a; 21w17a; 1.17 Release Candidate 1; 1.17; 1.17.1; 21w39a; 21w40a; 21w42a; 21w44a; 1.18; 1.18.1; 22w05a; 1.18.2; 22w15a; 22w18a; 1.19; 1.19.1; 1.19.2; 1.19.3; 23w03a; 23w04a; 1.19.4; 1.20; 1.20.1; 23w32a; 23w33a; 1.20.2; 23w43a; 23w46a; 1.20.3 Pre-Release 1; 24w11a; 1.20.5 Pre-Release 1; 1.20.5; 1.20.6; 1.21; 1.21 Release Candidate 1; 1.21.1; 1.21.2 Pre-Release 3; 1.21.3
- **Fix versions:** Minecraft 1.4.3; Minecraft 1.9.3 Pre-Release 3; 24w45a
- **Area:** Platform
- **Labels:** mojang_internal_1
- **Votes:** 1
- **Watchers:** 2
- **Attachments:** 4
- **Attachment filenames:** MC-212.png; MC-212 - Multiplayer LAN Behavior.mp4; MC-212 - Multiplayer Server Behavior.mp4; MC-212 - Singleplayer Behavior.mp4
- **Issue links:** Relates:outward:MC-278261:There is no longer spawn immunity after respawning | Relates:inward:MC-21650:Player is immune to damage for a few seconds after saving the world and returning | Relates:inward:MC-278547:No damage immunity when respawning | Duplicate:inward:MC-266866:Bone mealing grass seems to cancel fall damage | Duplicate:inward:MC-265212:Nothing clutch | Relates:inward:MC-264206:When you fell from build limit to bottom of the world and if you log out right before you fall you don't get Caves & Cliffs advancement | Relates:inward:MC-112133:Eating chorus fruit does not reset fall distance | Duplicate:inward:MC-233834:Disconection damage deletion | Duplicate:inward:MC-228590:Fall Damage bug | Duplicate:inward:MC-227574:Fall damage bug | Duplicate:inward:MC-214355:No Fall Damage Glitch | Duplicate:inward:MC-210368:Fall damage negated on respawn when pushed by piston with a slimeblock | Duplicate:inward:MC-208426:Fall distance isn't saved | Duplicate:inward:MC-205630:Falling bug | Duplicate:inward:MC-198511:[Exploit] [Save/Load] The player's character is immune to damage for a few seconds after loading the savefile | Duplicate:inward:MC-197057:Anti-Fall Damage bug | Duplicate:inward:MC-190057:when saving and quit and falling dose not take fall damage when close to the ground | Duplicate:inward:MC-184479:Fall issue | Duplicate:inward:MC-166995:Leaving the game when your falling from a high place makes you not take damage | Duplicate:inward:MC-153228:Falling Damage Bug | Duplicate:inward:MC-126079:No Fall Damage | Duplicate:inward:MC-123979:No fall damage when you quit and rejoin. | Duplicate:inward:MC-122122:Fall damage Glitch | Duplicate:inward:MC-1496:When falling in the Nether you can log out and log back in and receive no fall damage | Duplicate:inward:MC-106203:Falling Glitch | Duplicate:inward:MC-105755:Fall damage can be negated exploit | Duplicate:inward:MC-105176:Save & Quit, Rejoin world prevents fall damage | Duplicate:inward:MC-91439:I found a bug that gives you invincibility for a few seconds on a single player world. | Duplicate:inward:MC-91417:A way to survive lethal fall damage. | Duplicate:inward:MC-50863:Jump Glitch | Duplicate:inward:MC-37752:Saving game in mid air ignores falling height | Duplicate:inward:MC-13087:Exiting a world while falling cancels your velocity | Duplicate:inward:MC-82581:Reloading World resets Fall Damage | Duplicate:inward:MC-38006:Not taking falling damage after quitting and coming back | Duplicate:inward:MC-21641:No-fall damage | Duplicate:inward:MC-967:No fall damage when quit and re-enter the game. | Duplicate:inward:MC-77794:No fall damage if you leave a world when falling | Duplicate:inward:MC-75332:No fall damage if you quit and reenter the world. | Duplicate:inward:MC-61922:Fall damage | Duplicate:inward:MC-18283:No fall damage in Overworld | Relates:inward:MCPE-188490:Fall momentum is forgotten upon reloading a world

## Description

The Bug:
Fall damage is ignored for a couple of seconds when reloading into LAN or singleplayer worlds.
Please note that multiplayer server worlds are not affected by this issue.
Steps to Reproduce:
- Summon a large tower of blocks by using the command provided below.

```
/fill ~3 ~ ~ ~3 ~45 ~ minecraft:polished_andesite
```

- Stand on top of the tower and switch into survival mode.

- Jump off the edge of the tower, but before you hit the ground, hit the ESC key and exit the world.

- Load into the world once again and as you do this, watch your health closely.

- Take note as to whether or not fall damage is ignored for a couple of seconds when reloading into LAN or singleplayer worlds.

Observed Behavior:
Fall damage is ignored for a couple of seconds when reloading into LAN or singleplayer worlds.
Expected Behavior:
Fall damage would not be ignored for a couple of seconds when reloading into LAN or singleplayer worlds.
Code Analysis:
Code analysis by  can be found in this comment.

## Comments (99)

### Comment 1: migrated (2012-10-24T14:27:49.393-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: migrated (2012-10-24T15:33:20.938-0700)

mattabase has reported this on his stream as well

### Comment 3: Erik Broes (2012-10-24T16:08:58.598-0700)

Falldamage can occur on a remote server with pvp turned on.

### Comment 4: migrated (2012-10-24T22:54:45.154-0700)

Grum, the bug is that fall-damage gets re-calculated when you login.

### Comment 5: Michael Wobst (2012-10-25T00:11:45.215-0700)

Yes, that is the point. Falldamage gets re-calculated after logging out/logging in. So if you logg out if you're three or four blocks above the ground, you won't get any fall damage at all when logging back in! Not sure if Grum misunderstood this issue.
This applies to single- as well as multiplayer, btw.

### Comment 6: Erik Broes (2012-10-25T00:22:16.458-0700)

No, the data is stored and loaded correctly, the only reason you do not get damage is because you get 3 seconds of invulnerability when you login. I spend a good 45 minutes with a debugger jumping of a pole seeing what happened

### Comment 7: migrated (2013-03-17T14:04:40.984-0700)

Does this mean you no longer get invulnerability upon login? Because the 2-5 seconds it takes to load a server texture would become brutal. I hope this fix only applies to fall damage.

### Comment 8: migrated (2013-06-24T19:10:12.202-0700)

I think a good fix would be to give you invulnerability only if you are on the ground, but if you were in the air, you dont get it. Just an idea, dont get mad if it is a bad one.
also, this bug applies to singleplayer in 1.5.2, too

### Comment 9: migrated (2013-06-25T10:13:36.979-0700)

Reopened as this is still an issue in 1.6 Singeplayer.

### Comment 10: migrated (2013-06-30T20:13:06.885-0700)

@
 already has put them up, he just hasn't taken off the fix version, probably because it was confirmed in multiplayer in 1.4.3 (but I haven't tested it yet, it could still be a bug in multiplayer)

### Comment 11: migrated (2013-12-19T00:54:29.142-0800)

I think that the 3 seconds of invulnerability needs to be kept, except for fall damage.  Or have a very large invisible health shield upon login, which would only be ignored by fall damage.

### Comment 12: migrated (2014-04-29T00:54:09.241-0700)

I think the current code rewrites are going to seperate certain kinds of damage and not into 1 category. It's just an guess, but that would make it possible to make invulnerability not count on fall damage.

### Comment 13: migrated (2014-07-06T11:56:57.606-0700)

Still exists in 1.7.10 single player.
In multiplayer, a player will fall to his death but in single player he will land without falldamage.

### Comment 14: Michael Wobst (2014-07-29T13:34:18.800-0700)

NOTE: this issue only appears in singleplayer. When playing in multiplayer, everything works as expected.

### Comment 15: migrated (2014-11-25T08:21:23.182-0800)

Still in 1.8.1

### Comment 16: migrated (2015-07-29T14:56:03.009-0700)

Confirmed for Snapshot 15w31a

### Comment 17: migrated (2015-11-18T13:35:53.931-0800)

Confirmed for 15w47a

### Comment 18: migrated (2015-11-19T11:25:48.442-0800)

Confirmed for 15w47b

### Comment 19: migrated (2015-12-02T13:48:10.304-0800)

Confirmed for 15w49a

### Comment 20: migrated (2015-12-22T13:17:08.779-0800)

Confirmed for 1.8.9 and 15w51b.

### Comment 21: marcono1234 (2015-12-23T10:26:07.925-0800)

Confirmed for
- 15w51b

This seems to not only affect FallDistance but also Motion. This can be seen when having a command block clock that teleports the player constantly upwards (for example /tp @p ~ ~1 ~), because of MC-79938 the player appears to "bounce", however when reopening the world the player is at a higher position than before.

### Comment 22: marcono1234 (2015-12-23T13:23:22.212-0800)

Cannot confirm for 15w51b
The fact that the player takes no damage is because he is always resistent against any kind of damage for the first seconds after entering a world.
To see that the fall damage is correct you can do this:
- Give yourself resistance

```/effect @p resistance 10000 3 true```

- Place a block at the height where you would survive the fall

```/setblock ~ ~103 ~ stone```

- Switch to Survival mode

- Teleport yourself up

```/tp ~2 ~115 ~```

- Once you passed the stone block leave the world

- Open the world again
You should die from the fall damage, this means the damage was not calculated from where you logged out / in

### Comment 23: marcono1234 (2015-12-23T13:40:38.747-0800)

Sorry for the confusion and please remove the note

### Comment 24: migrated (2015-12-23T20:43:42.832-0800)

People who have recently reproduced this: Please describe your test setup.

### Comment 25: marcono1234 (2016-02-17T10:34:25.164-0800)

please describe your test setup

### Comment 26: Michael Wobst (2016-02-17T10:44:20.992-0800)

What test setup? It's explained very well in the description. Log out/exit just before you hit the ground. Log back in and you won't get any fall damage.

### Comment 27: marcono1234 (2016-02-17T12:59:57.234-0800)

That is very likely caused by the resistance against all damage after logging in, see my comment

### Comment 28: Michael Wobst (2016-02-18T00:05:11.773-0800)

Well, it works as expected in SMP, so there's inconsistency between SSP and SMP. Also as mentioned, if this was intended behavior, you could completely remove fall-damage from the game since you can cheat around with ease. i.e. fall-damage gets rendered completely meaningless.

### Comment 29: marcono1234 (2016-02-18T09:48:38.839-0800)

Please link to this comment in the description of the report.
The following is based on decompiled version of Minecraft 1.8 using MCP. All method and class names are the names used in the decompiled version.
The way fall damage is handled while the respawn resistance is active is kind of strange. There are two requirements that have to be met to apply fall damage after the player logged in:
- The server must not be an integrated server

- PvP must be enabled

This seems not intended to me. To fix this the public boolean attackEntityFrom(DamageSource source, float amount) method of the net.minecraft.entity.player.EntityPlayerMP class needs to be modified.

```/**
 * Called when the entity is attacked.
 */
public boolean attackEntityFrom(DamageSource source, float amount)
{
    if (this.func_180431_b(source))
    {
        return false;
    }
    else
    {
        // Changed this
        //boolean var3 = this.mcServer.isDedicatedServer() && this.func_175400_cq() && "fall".equals(source.damageType);
        //if (!var3 && this.respawnInvulnerabilityTicks > 0 && source != DamageSource.outOfWorld)
        if (source != DamageSource.fall && source != DamageSource.outOfWorld && this.respawnInvulnerabilityTicks > 0)
        {
            return false;
        }
        else
        {
            //...
        }
    }
}```

### Comment 30: Michael Wobst (2016-02-18T10:41:58.294-0800)

Excellent work as always, Marcono1234. :thumbs up:

### Comment 31: migrated (2016-02-26T13:06:49.576-0800)

I can still confirm this bug for the 1.9 Pre-Release 4. Maybe this is also the reason why Villager Golems aren't aggressive anymore after relogging (at least in Singleplayer).

### Comment 32: marcono1234 (2016-02-28T06:02:58.136-0800)

In 1.8.9 VillagerGolems are not aggressive after reopening the world as well

### Comment 33: migrated (2016-03-15T16:02:17.669-0700)

Appears to be fixed in 1.9.1-pre3.
Testing results:
- Resistance IV

- Feather Falling IV, Protection IV diamond boots

- Falling 250m: 3hp left

- Falling 200m: 6hp left

- Falling 250m, relogging at 200m (after falling 50m): 3hp left

### Comment 34: kumasasa (2016-03-15T23:47:08.105-0700)

Can anyone confirm the fix in 1.9.1-pre3 ?

### Comment 35: Michael Wobst (2016-03-16T00:20:32.097-0700)

No, it's not fixed at all in 1.9.1-pre3

### Comment 36: migrated (2016-05-05T16:40:41.980-0700)

Cannot reproduce on 1.9.3-pre3...
- Non-integrated MP server

- PvP enabled in server.properties

- Resistance IV, Feather Falling VI

- Fall from 350 blocks, half a heart left

- Fall from 350 blocks, logout after falling ~150 blocks, still half a heart left

Can anyone confirm?

### Comment 37: kumasasa (2016-05-05T17:06:45.239-0700)

, when you still can confirm this issue, please provide steps to reproduce.

### Comment 38: migrated (2016-05-06T07:21:09.463-0700)

At least I can still confirm it in Singpleplayer, however I didn't test it in Multiplayer. (Version 1.9.3 Pre-Release)
Steps to reproduce:
1. Build some sort of high tower.
2. Fly/Climb on top of that tower. Then go into Survival Mode.
3. Jump down once to test if you would die when you hit the ground.
4. If you die, jump down again from top of the tower and log out right before you hit the ground.
5. Log back into the world.
6. See how you don't take any fall damage.

### Comment 39: kumasasa (2016-05-06T07:30:49.053-0700)

: This ticket is about multiplayer, see the description.

### Comment 40: Michael Wobst (2016-06-08T11:27:45.990-0700)

No, it's not about multiplayer. Also it's still an issue in 1.10. So why exactly has this ticket been marked as fixed?
Maybe the description should be reworked a bit since it's mainly an issue for map makers who intend to integrate fall traps into their singleplayer maps

### Comment 41: Ezekiel (2016-06-08T11:36:11.888-0700)

This issue is only currently present in single player, and as such I have reopened the ticket and edited it accordingly

### Comment 42: migrated (2016-06-08T14:53:34.901-0700)

Still cannot reproduce in 1.10:
- Integrated singleplayer server

- Resistance IV (4), Protection IV (4) Feather Falling IV (4) Diamond Boots

- Falling from 250 blocks: 3 HP left (1.5 hearts)

- Falling from 250 blocks, and relogging after falling ~150 blocks: 3 HP left (1.5 hearts)

 Could you please provide a list of steps to reproduce?

### Comment 43: Michael Wobst (2016-06-09T09:56:50.428-0700)

null: Block twenty-eight already explained it very well how to reproduce.
Block twenty-eight: you can remove that "EDIT: Irrelevant as I misunderstood the ticket. I'm sorry for that." from your latest post, as you totally understood the issue, and explained very well on how to reproduce it.

### Comment 44: migrated (2016-06-09T12:43:32.360-0700)

Ok, did that, thanks for mentioning.
Just something regarding the description of the bug: "This basically makes fall traps useless on PvP servers." is now actually useless since this ticket now is about a singleplayer bug.
And: Can confirm this bug for 1.10.

### Comment 45: FaRo1 (2016-06-22T14:23:08.657-0700)

Confirmed for 1.10.1.

### Comment 46: migrated (2016-06-23T09:01:38.672-0700)

Confirmed for 1.10.2.

### Comment 47: migrated (2016-09-10T04:18:19.450-0700)

Confirmed for 16w36a

### Comment 48: migrated (2016-10-30T01:50:40.672-0700)

The bug is still there in 16w43a snapshot of 1.11.

### Comment 49: SunCat (2016-10-30T05:24:49.337-0700)

, 16w43a is already in the list of affected versions

### Comment 50: FaRo1 (2016-12-20T14:07:00.015-0800)

If you can see that, that's enough for one version. Many people have seen it before in other versions and there's not a big chance that it was fixed accidentally.

### Comment 51: migrated (2017-03-31T14:39:57.548-0700)

Confirmed for 17w13b (If a bug should not be confirmed for every version, I apologize)

### Comment 52: Michael Wobst (2017-03-31T14:41:47.190-0700)

that's totally fine and helps a lot.

### Comment 53: migrated (2017-04-25T11:07:24.556-0700)

Confirmed for 17w16b

### Comment 54: migrated (2017-04-27T12:57:43.665-0700)

Confirmed for 17w17b

### Comment 55: migrated (2017-09-27T06:16:56.931-0700)

Confirmed in 1.12.2

### Comment 56: migrated (2018-03-28T07:58:29.327-0700)

Confirmed for 18w11a

### Comment 57: migrated (2018-04-05T06:53:39.904-0700)

Confirmed for 18w14a

### Comment 58: migrated (2018-04-05T15:33:42.760-0700)

Affects 18w14b

### Comment 59: migrated (2018-04-19T12:47:48.544-0700)

Affects 18w16a

### Comment 60: migrated (2018-05-29T13:47:34.821-0700)

Confirmed for 18w22a

### Comment 61: migrated (2018-06-04T13:39:56.392-0700)

Confirmed for 1.13-pre1

### Comment 62: migrated (2018-06-16T04:43:12.686-0700)

Confirmed for 1.13-pre2

### Comment 63: migrated (2018-08-24T13:12:31.816-0700)

Confirmed for 1.13.1.

### Comment 64: migrated (2018-10-19T15:23:11.615-0700)

Confirmed for 1.13.2-pre2.

### Comment 65: migrated (2019-03-29T11:47:50.642-0700)

Confirmed for 19w13b

### Comment 66: migrated (2019-12-05T03:30:06.021-0800)

Maybe it's that when you log out of a game the information of the fall is not saved and/or used when you log back in. So then the game registers it as a fall from that fall level.

### Comment 67: bluecrab2 (2020-04-14T21:20:29.703-0700)

Confirmed in 20w15a, part of me doesn't want them to fix this bug because it has saved my life so many times lol

### Comment 68: migrated (2020-04-19T15:14:08.913-0700)

Confirmed in 20w16a!

### Comment 69: migrated (2020-06-10T15:31:41.559-0700)

Confirmed in 1.16-pre3. Quite an old bug here.

### Comment 70: migrated (2020-06-11T13:44:07.161-0700)

Confirmed in 1.16-pre4.

### Comment 71: migrated (2020-06-12T14:18:23.693-0700)

Confirmed in 1.16-pre5.

### Comment 72: migrated (2020-06-16T06:33:41.129-0700)

Confirmed in 1.16-pre6.

### Comment 73: markderickson (2020-06-29T15:21:18.489-0700)

Hi there!
Can confirm for 1.16.1.

### Comment 74: markderickson (2020-07-02T09:06:25.779-0700)

Hi there!
Can confirm for 20w27a.

### Comment 75: Avoma (2020-11-26T02:24:44.537-0800)

Can confirm in 20w48a.

### Comment 76: Avoma (2020-12-02T11:30:17.332-0800)

Can confirm in 20w49a.

### Comment 77: Avoma (2020-12-20T04:10:37.771-0800)

Can confirm in 20w51a.

### Comment 78: Avoma (2021-01-17T10:19:54.065-0800)

Relates to MC-205304 and MC-105103.

### Comment 79: Avoma (2021-01-20T11:01:15.366-0800)

Can confirm in 21w03a. Requesting ownership if the reporter no longer wants to update the ticket.

### Comment 80: Avoma (2021-02-03T11:05:55.545-0800)

Can confirm in 21w05a.

### Comment 81: Avoma (2021-02-04T10:23:14.916-0800)

Can confirm in 21w05b.

### Comment 82: Avoma (2021-02-11T08:03:18.352-0800)

Can confirm in 21w06a.

### Comment 83: Avoma (2021-02-18T05:03:19.448-0800)

Can confirm in 21w07a.

### Comment 84: Avoma (2021-02-25T09:20:13.520-0800)

Can confirm in 21w08b.

### Comment 85: Avoma (2021-03-19T11:21:38.382-0700)

Can confirm in 1.16.5 and 21w11a.

### Comment 86: Avoma (2021-04-12T02:21:59.200-0700)

Can confirm in 21w14a.

### Comment 87: Avoma (2021-04-30T05:46:28.621-0700)

Can confirm in 21w17a.

### Comment 88: MMK21 (2021-06-12T01:27:05.426-0700)

Affects 1.17

### Comment 89: migrated (2021-07-07T13:02:56.093-0700)

Bug also applies to multiplayer in 1.17.1

### Comment 90: Avoma (2021-10-04T01:35:32.097-0700)

In regards to the above comment, I've done some further investigating regarding this issue and it appears that this problem doesn't exist in multiplayer server worlds, but does exist in multiplayer LAN and singleplayer worlds. I'm not exactly sure why this is the case, but I've provided some attachments that demonstrate this behavior.

### Comment 91: Avoma (2021-10-04T01:48:14.460-0700)

Can confirm this in 21w39a. As stated above by myself, this issue appears to affect only multiplayer LAN worlds and singleplayer worlds. Multiplayer server worlds are not affected by this problem. Here are some extra details regarding this issue,
The Bug:
Fall damage is ignored for a couple of seconds when reloading into a LAN or singleplayer world.
Please note that multiplayer server worlds are not affected by this issue.
Steps to Reproduce:
- Summon a large tower of blocks.

```/fill ~3 ~ ~ ~3 ~45 ~ minecraft:polished_andesite```
- Stand on top of the tower and switch into survival mode.

- Jump off the edge of the tower, but before you hit the ground, hit the ESC key and exit the world.

- Load into the world once again.

- Pay close attention to your health and to whether you receive any damage or not.

Observed Behavior:
Fall damage is ignored for a couple of seconds when reloading into a LAN or singleplayer world.
Expected Behavior:
Fall damage would not be ignored for a couple of seconds when reloading into a LAN or singleplayer world.
Code Analysis:
Code analysis by  can be found in this comment.

### Comment 92: FaRo1 (2021-10-04T02:13:09.860-0700)

I can confirm that this does NOT happen with a Vanilla server that I just freshly set up. Interestingly, it did work many times on a server I play on that used to be on Bukkit 1.16.5 and still works now that it is on Fabric 1.17.1.

### Comment 93: MMK21 (2021-12-10T08:31:53.668-0800)

Affects 1.18.1

### Comment 94: MMK21 (2022-02-28T10:50:17.521-0800)

Affects 1.18.2

### Comment 95: migrated (2022-04-15T11:40:54.126-0700)

confirm for 22w15a

### Comment 96: Brain81505 (2023-01-18T06:23:23.327-0800)

Can confirm in 23w03a

### Comment 97: Brain81505 (2023-01-24T23:19:36.408-0800)

Can confirm in 23w04a

### Comment 98: Brain81505 (2023-02-01T08:04:01.566-0800)

Can confirm in 23w06a

### Comment 99: migrated (2023-06-08T08:26:56.796-0700)

Can confirm in 1.20
