# MC-67: Entities with passengers cannot travel through portals

**Mojira URL:** [https://bugs.mojang.com/browse/MC-67](https://bugs.mojang.com/browse/MC-67)

## Report details

- **Mojira categories:** Entities
- **Project:** MC
- **Issue key:** MC-67
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2012-10-24T09:02:25.801-0700
- **Updated:** 2025-05-29T09:21:00.692-0700
- **Resolution date:** 2024-05-29T16:25:20.820-0700
- **Affects versions:** Minecraft 1.4.2; Minecraft 1.14.3; 1.15 Pre-release 3; 1.16.1; 1.16.3; 1.16.4 Pre-release 2; 1.16.4 Release Candidate 1; 1.16.4; 20w45a; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w08a; 21w08b; 21w10a; 21w11a; 21w13a; 21w14a; 21w15a; 21w16a; 21w17a; 21w18a; 1.17 Release Candidate 1; 1.17; 1.17.1; 21w39a; 21w40a; 21w41a; 21w42a; 1.18; 1.18.1; 22w03a; 22w05a; 22w07a; 1.18.2 Pre-release 1; 1.18.2 Release Candidate 1; 1.18.2; 22w14a; 1.19; 1.19.1; 1.19.2; 22w43a; 22w45a; 1.19.3; 23w03a; 23w04a; 1.19.4; 1.20; 1.20.1; 24w11a; 1.20.6
- **Fix versions:** 24w21a
- **Area:** Platform
- **Labels:** end_portal; horse; minecart; nether_portal; passengers
- **Watchers:** 2
- **Attachments:** 4
- **Attachment filenames:** 2021-05-12_14.38.11.png; 2024-05-22_16.16.30.png; 2024-05-22_16.16.51.png; MC-67.mp4
- **Issue links:** Duplicate:inward:MC-18837:Horse through portal | Duplicate:inward:MC-5466:(dont know if actual bug) Minecart with player bug | Duplicate:inward:MC-13734:Horses - Killed With Nether Portal | Duplicate:inward:MC-13784:Cannot ride a horse through nether portal | Duplicate:inward:MC-14328:cannot enter the nether while riding a horse | Duplicate:inward:MC-14368:Mounted Horse by the Player | Duplicate:inward:MC-16634:Horses won't use an Nether portal when riding it. | Duplicate:inward:MC-16838:[Bug?] Mounted horses are unable to go through Nether portals | Duplicate:inward:MC-16868:unable to ride into a netherportal with a minecart | Duplicate:inward:MC-17861:Minecart cant travel in portal? | Duplicate:inward:MC-19216:While riding the horse you can not enter the ender portal. | Duplicate:inward:MC-19796:You cannot ride a horse into the end. | Duplicate:inward:MC-20293:Horses won't go into the END. | Duplicate:inward:MC-23692:you can't ride on a horse into the nether (portal) | Duplicate:inward:MC-27993:Horses causing bad game states when going through an End Portal | Duplicate:inward:MC-41160:horse trough nether portal | Duplicate:inward:MC-47166:cannot enter nether while in a minecart | Duplicate:inward:MC-72566:Entities in mine carts cannot go through portals. | Duplicate:inward:MC-102735:Cannot travel though nether portals while riding a skeleton horse | Duplicate:inward:MC-106095:Players cannot go through nether portal whilst in Minecart or Boat. | Duplicate:inward:MC-109754:Can't ride mobs thru portals | Duplicate:inward:MC-129923:Players in boats cannot enter/leave netherworld through portal | Duplicate:inward:MC-134423:Pigman chicken jockey won't go through the Nether Portal | Duplicate:inward:MC-155563:chicken jockey will not go through nether portal? | Duplicate:inward:MC-162728:zombie pigman chicken jockey won't go through nether portal | Duplicate:inward:MC-176114:Unable to ride a strider into a portal in general. | Duplicate:inward:MC-181440:Players in minecarts do not travel through Nether Portals | Duplicate:inward:MC-181504:Mobs in minecarts do not pass through Nether Portals | Duplicate:inward:MC-190418:Can't go through nether portal while on strider | Duplicate:inward:MC-193216:Mobs cannot be teleported to/from nether | Duplicate:inward:MC-201168:Shulker and Boat stuck in exit portal | Duplicate:inward:MC-204122:Entities ridden in boat or minecart cannot travel through portals | Duplicate:inward:MC-227620:Riding a pig into the end doesn't work | Duplicate:inward:MC-150:Can't use nether portals while riding a pig | Duplicate:inward:MC-1265:Villagers in minecarts cannot move through portal | Duplicate:inward:MC-4623:Can't Ride Through Nether Portals | Duplicate:inward:MC-4714:Villiger in Minecart will not go into the portal | Relates:outward:MC-260534:Entities cannot be teleported with a passenger | Relates:inward:MC-47288:All items dissapearing from inventory and chests 14w03b | Relates:inward:MC-149242:End gateways are no longer able to teleport boats with players riding in them | Relates:inward:MCPE-47288:Entities with passengers can't travel through portals

## Description

The Bug:
Entities with passengers cannot travel through portals.
Steps to Reproduce:
- Build a nether portal, light it, enter it, and return to the overworld.

- Summon an entity with a passenger by using the command provided below.

```
/summon minecraft:spider ~ ~ ~ {Passengers:[{id:"minecraft:skeleton",HandItems:[{id:"minecraft:bow",Count:1b}]}]}
```

- Push the spider jockey into the nether portal that you just previously built, in an attempt to make it change dimensions.

- Take note as to whether or not entities with passengers can travel through portals.

Observed Behavior:
Entities with passengers cannot travel through portals.
Expected Behavior:
Entities with passengers would be able to travel through portals.

## Comments (46)

### Comment 1: migrated (2012-10-24T09:02:25.801-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: migrated (2012-10-24T16:26:09.313-0700)

I can confirm this. Driving boats or riding pigs through a portal won't work either.

### Comment 3: migrated (2012-10-29T09:25:59.278-0700)

its true

### Comment 4: migrated (2012-11-22T11:43:26.434-0800)

Dinnerbone has confirmed that this is by design, and thus not a bug.

### Comment 5: migrated (2012-11-22T22:25:32.092-0800)

Oh, that's a shame . Does anybody have a link to Dinnerbone's confirmation?

### Comment 6: kumasasa (2012-11-22T23:02:52.370-0800)

There is no link, just take it what Mustek wrote.

### Comment 7: migrated (2012-11-25T11:46:06.820-0800)

so it will not be fixed? because the status is 'resolved'

### Comment 8: kumasasa (2012-11-25T12:08:10.709-0800)

Read the comments:
Dinnerbone has confirmed that this is by design, and thus not a bug.
thus
Works as Intended"

### Comment 9: migrated (2012-11-25T12:27:14.797-0800)

Yeah I read that, but the status says 'resolved'.

### Comment 10: migrated (2012-11-25T14:45:45.829-0800)

"Resolved", with a resolution of "Works As Intended".

### Comment 11: migrated (2012-11-25T22:52:23.470-0800)

Ah, ok. Thnks

### Comment 12: Torabi (2012-12-13T05:28:37.516-0800)

So has the status on this changed, since Dinnerbone has marked MC-1969 as fixed in 12w50a? This certainly seems contradictory with the claim that the behavior listed here is "by design, and thus not a bug", though I suppose he could have decided to change it anyway.

### Comment 13: kumasasa (2012-12-13T11:31:34.186-0800)

Status on this ticket is not changed.
Tested with 12w50a: Only unoccupied Minecarts travel through the portal.

### Comment 14: migrated (2012-12-28T08:59:32.853-0800)

Is there any mod that lets this work?

### Comment 15: migrated (2013-04-18T15:42:16.902-0700)

Confirmed with riding a horse.
Just updating this so that people who might report this issue have a possibility of seeing this one.
(the version affected should be updated as well)

### Comment 16: migrated (2013-06-24T05:09:17.006-0700)

this isn't a bug anymore since jeb told this is intended.

### Comment 17: migrated (2014-04-14T07:28:58.009-0700)

Why on earth is this intended? Why shouldn't you be able to ride a horse through a portal?

### Comment 18: migrated (2014-04-14T10:52:09.479-0700)

this is intended because it's to hard to fix and unnecessary

### Comment 19: markderickson (2020-09-16T07:55:46.277-0700)

Hi!
I can confirm for release 1.16.3.

### Comment 20: migrated (2020-11-07T17:03:37.873-0800)

A bug that was once fixed makes a return? Odds of that happening?

### Comment 21: Avoma (2020-11-25T11:17:55.894-0800)

Can confirm in 20w48a.

### Comment 22: Avoma (2020-12-20T12:28:01.691-0800)

Can confirm in 20w51a.

### Comment 23: migrated (2021-01-03T05:00:48.115-0800)

I’d like to request ownership, the original reporter hasn’t been active since April 2019, I will keep this report updated.

### Comment 24: Avoma (2021-02-03T11:04:33.667-0800)

Can confirm in 21w05a.

### Comment 25: Avoma (2021-02-04T10:21:39.487-0800)

Can confirm in 21w05b.

### Comment 26: Avoma (2021-02-10T10:29:43.278-0800)

Can confirm in 21w06a.

### Comment 27: Avoma (2021-03-14T06:21:11.222-0700)

Can confirm in 1.16.5. Video attached.

### Comment 28: MMK21 (2021-06-12T01:09:52.382-0700)

Affects 1.17

### Comment 29: MMK21 (2021-06-12T01:17:01.208-0700)

A bug that was once fixed makes a return? Odds of that happening?
Happened quite a few times, actually. See https://bugs.mojang.com/browse/MC-67?jql=project%20%3D%20%22Minecraft%3A%20Java%20Edition%22%20AND%20fixVersion%20is%20not%20EMPTY%20AND%20resolution%20!%3D%20Fixed%20ORDER%20BY%20fixVersion%20ASC

### Comment 30: Avoma (2021-07-08T07:31:41.887-0700)

Can confirm in 1.17.1.

### Comment 31: Creeper Juice (2021-08-01T19:28:33.662-0700)

This may be intentional. See https://youtu.be/EtKcphC4fIc?t=36

### Comment 32: migrated (2021-08-05T10:27:55.235-0700)

The ticket has recently been reopened and recieved Mojang priority, which means the developers classify this as a valid bug.

### Comment 33: windwend (2021-08-18T19:45:53.157-0700)

At this point, might actually treat this as a feature.

### Comment 34: Avoma (2021-10-04T00:20:16.393-0700)

Can confirm this behavior in 21w39a. Here are some extra details regarding this problem.
The Bug:
Entities with passengers cannot travel through portals.
Steps to Reproduce:
- Build a nether portal, light it, and enter it.

- Return to the overworld.

- Summon an entity with a passenger, for example, a spider jockey.

```/summon minecraft:spider ~ ~ ~ {Passengers:[{id:"minecraft:skeleton",HandItems:[{id:"minecraft:bow",Count:1b}]}]}```
- Push the spider jockey into the nether portal you previously built and watch it closely.

Observed Behavior:
Entities with passengers cannot travel through portals.
Expected Behavior:
Entities with passengers would be able to travel through portals.

### Comment 35: migrated (2021-11-16T17:56:12.021-0800)

For many years I have to dismount and push horses through the portal, never knew that it's a bug

### Comment 36: MMK21 (2021-12-10T08:10:09.885-0800)

Affects 1.18.1

### Comment 37: MMK21 (2022-02-28T08:22:42.807-0800)

Affects 1.18.2

### Comment 38: Brain81505 (2023-01-18T06:22:46.051-0800)

Can confirm in 23w03a

### Comment 39: Brain81505 (2023-01-24T23:18:55.852-0800)

Can confirm in 23w04a

### Comment 40: Brain81505 (2023-02-01T08:03:41.034-0800)

Can confirm in 23w06a

### Comment 41: migrated (2023-06-07T22:51:53.898-0700)

Can confirm in 1.20

### Comment 42: Brain81505 (2023-08-09T08:55:39.792-0700)

Can confirm in 23w32a

### Comment 43: migrated (2024-03-20T16:30:28.996-0700)

So did anyone find a mod for this? Immersive portals doesn't seem to support it: https://github.com/iPortalTeam/ImmersivePortalsMod/issues/681

I've yet to test https://www.spigotmc.org/resources/netherminecarts.110193/ but it's a plugin.

### Comment 44: muzikbike (2024-05-22T08:18:05.033-0700)

This doesn't appear to be fixed for me?

### Comment 45: anthony cicinelli (2024-05-22T08:20:32.190-0700)

Set the gamerule entitiesWithPassengersCanUsePortals to true

### Comment 46: [Mod] EVGENSYPERPRO (2024-05-29T15:18:07.227-0700)

The gamerule was removed in 1.21 pre-release 1, but it is now fixed even without the gamerules.
